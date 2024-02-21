import os
import sys
from distutils import config

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')


import logging

import geopandas as gpd
import overpy
from overpy.exception import OverpassBadRequest
from shapely.geometry import Polygon
from tqdm import tqdm

from data.queries.queries import osm_area_queries
from utils.config_loader import config_data
from utils.helper import concatenate_geodataframes
from utils.save_data import safe_gdf_as_gpkg

# Configure logging
#logging.basicConfig(filename='missing_queries.txt', level=logging.WARNING)
logging.basicConfig(filename='Result_insights.txt', level=logging.INFO, filemode='w')

api = overpy.Overpass()

def _query_overpass(api,query):
    """
    Query the Overpass API with the given query.

    Args:
        api: The Overpass API object.
        query: The query string to be executed with keys and values form osm.

    Returns:
        The result of the query.

    Raises:
        OverpassBadRequest: If the query is invalid.
    Examples:
        >>> api = OverpassAPI()
        >>> query = siehe queryservice
        >>> result = _query_overpass(api, query)
    """

    try:
        return api.query(query)
    except OverpassBadRequest as e:
        # Handle the exception (e.g., print an error message)
        print(f"OverpassBadRequest: {e}")
    


def _parse_osm_area_result(result: overpy.Result, osm_key: str,osm_value: str,**kwargs):
    """
    Parses the result of a query to a GeoDataFrame.

    Args:
        result: The result of the query.
    """

    # Create an empty dictionary to store the data 
    data = {'id': [], 'osm_key': [], 'osm_value': [], 'geometry': []}
    
    for relation in result.relations:
        
        # Initialize lists to store outer and inner coordinates for each polygon
        outer_polygons = []
        inner_polygons = []
        result_polygons = []
        for member in relation.members:
            member_ref = member.ref
            polygon_line_query = f"way({member_ref});(._;>;);out geom;"
            polygon_line_result = api.query(polygon_line_query)
            for polygon_line in polygon_line_result.ways:
                if len(polygon_line.nodes) >= 4:
                    coordinates = [(node.lon, node.lat) for node in polygon_line.nodes]
                    print(member,len(coordinates))

                    polygon = Polygon(coordinates)
                    if polygon.is_valid:

                        # Check if the member role is "inner" or "outer"
                        if member.role == "outer":
                            outer_polygons.append(polygon)
                        elif member.role == "inner":
                            inner_polygons.append(polygon)  
                        
        for outer_polygon in outer_polygons:
            # Attempt to subtract each inner polygon from the current outer polygon
            try:
                for inner_polygon in inner_polygons:
                    outer_polygon = outer_polygon.difference(inner_polygon)
                
                # If the result is not empty, append it to the list
                if outer_polygon.is_empty:
                    # Handle the case where the subtraction results in an empty geometry
                    print(f"Subtraction resulted in an empty geometry for outer polygon {outer_polygon}")
                else:
                    result_polygons.append(outer_polygon)
            except Exception as e:
                # Handle the exception, log it, or take appropriate action
                print(f"Error subtracting inner polygons from outer polygon: {e}")            
                #polygon_nodes = polygon_line_result.ways[0].nodes
        # # Update the data dictionary with information for each polygon
        for polygon in result_polygons:
            data['id'].append(relation.id)
            data['osm_key'].append(osm_key)
            data['osm_value'].append(osm_value)
            data['geometry'].append(polygon) 

    #create a GeoDataFrame from the dictionary
    return gpd.GeoDataFrame(data, crs="EPSG:4326").to_crs("EPSG:31468")
def create_osm_area_gdf():
    """
    Creates a GeoDataFrame of OpenStreetMap streets.

    Returns: None
    """
    #empty list to store the gdf
    list_of_gdf = []


    for query_info in tqdm(osm_area_queries, desc="Querying Overpass"):
        area_query = query_info['query']

        osm_key = query_info['key']
        osm_value = query_info['value']

        print(osm_value)
        result = _query_overpass(api, area_query)
        if result is not None:
            gdf = _parse_osm_area_result(result, osm_key, osm_value)
            list_of_gdf.append(gdf)
            #add information to logfile
            number_of_areas = len(result.areas)
            logging.info(f"osmKey: {osm_key} Anzahl_areas {number_of_areas}")

        else:
            # Log the missing query to the log file
            #logging.warning(f"Missing result for query: {osm_key} - {osm_value} in {poi_query}")

            continue
    if list_of_gdf is not None:

        osm_area_gdf = concatenate_geodataframes(list_of_gdf)
        safe_gdf_as_gpkg((osm_area_gdf,"osm_area_plain_"+config_data["city_name"]))
    else:
        logging.info("No area result in " + config_data["city_name"])

def main():

    create_osm_area_gdf()
if __name__ == "__main__":
    main()