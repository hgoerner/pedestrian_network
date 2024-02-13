import sys
import os

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')


import overpy
import geopandas as gpd
from shapely.geometry import Polygon
from data.queries.queries import osm_area_queries
from utils.save_data import safe_gdf_as_gpkg
from utils.helper import concatenate_geodataframes
from utils.config_loader import config_data
import logging
from tqdm import tqdm
from overpy.exception import OverpassBadRequest

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
    


def _parse_osm_area_result(result: overpy.Result, osm_key: str, osm_value: str, **kwargs):
    """
    Parses the result of a query to a GeoDataFrame.

    Args:
        result: The result of the query.
    """
    # Create an empty dictionary to store the data 
    data = {'id': [],'osm_key': [],'osm_value': [],'geometry': []}
    for area in result.areas:
        print(len(result.areas))
        # Accessing key-value pairs in the tags dictionary
        data['id'].append(area.id)
        data['osm_key'].append(osm_key)
        data['osm_value'].append(osm_value)
            # Extract polygon coordinates from the area
        coordinates = [(node.lon, node.lat) for node in area.nodes]
        
        # Create a Polygon object
        polygon = Polygon(coordinates)
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
        result = _query_overpass(api, area_query)
        if result is not None:
            gdf = _parse_osm_area_result(result, osm_key,osm_value)
            list_of_gdf.append(gdf)
            #add information to logfile
            number_of_areas = len(result.areas)
            logging.info(f"osmKey: {osm_key} OsmValue: {osm_value} Anzahl_areas {number_of_areas}")
            
        else:
            # Log the missing query to the log file
            #logging.warning(f"Missing result for query: {osm_key} - {osm_value} in {poi_query}")
            #for testin
            continue

    osm_area_gdf = concatenate_geodataframes(list_of_gdf)
    safe_gdf_as_gpkg((osm_area_gdf,"osm_area_plain_"+config_data["city_name"]))

def main():

    create_osm_area_gdf()
if __name__ == "__main__":
    main()