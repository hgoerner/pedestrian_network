import sys
import os

current_directory = os.getcwd()
print(current_directory)


sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
import overpy
import geopandas as gpd
from shapely.geometry import Point
from queries.queries import osm_poi_queries
from save_data import safe_gdf_as_gpkg
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
    


def _parse_osm_poi_result(result: overpy.Result, osm_key: str, osm_value: str, **kwargs):
    """
    Parses the result of a query to a GeoDataFrame.

    Args:
        result: The result of the query.
    """
    # Create an empty dictionary to store the data 
    data = {'id': [],'osm_key': [],'osm_value': [],'geometry': []}

    for node in result.nodes:
        # Accessing key-value pairs in the tags dictionary
        data['id'].append(node.id)
        data['osm_key'].append(osm_key)
        data['osm_value'].append(osm_value)
        data['geometry'].append(Point(node.lon, node.lat))

    #create a GeoDataFrame from the dictionary
    return gpd.GeoDataFrame(data, crs="EPSG:4326").to_crs("EPSG:31468")
def create_osm_poi_gdf():
    """
    Creates a GeoDataFrame of OpenStreetMap streets.

    Returns: None
    """
    #empty list to store the gdf
    list_of_gdf = []

    for query_info in tqdm(osm_poi_queries, desc="Querying Overpass"):
        poi_query = query_info['query']
        osm_key = query_info['key']
        osm_value = query_info['value']
        result = _query_overpass(api, poi_query)
        if result is not None:
            gdf = _parse_osm_poi_result(result, osm_key,osm_value)
            list_of_gdf.append(gdf)
            number_of_pois = len(result.nodes)
            logging.info(f"osmKey: {osm_key} OsmValue: {osm_value} Anzahl_pois {number_of_pois}")
        else:
            # Log the missing query to the log file
            #logging.warning(f"Missing result for query: {osm_key} - {osm_value} in {poi_query}")
            continue

    osm_poi_gdf = concatenate_geodataframes(list_of_gdf)
    safe_gdf_as_gpkg((osm_poi_gdf,"osm_pois_plain"+config_data["city_name"]))

def main():

    create_osm_poi_gdf()
if __name__ == "__main__":
    main()