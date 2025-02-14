import os
import sys

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

import geopandas as gpd
import overpy
from shapely.geometry import LineString
from tqdm import tqdm

from data.download.queries.create_queries import osm_street_queries
from utils.config_loader import config_data
from utils.helper import concatenate_geodataframes
from utils.save_data import save_gdf_as_gpkg

api = overpy.Overpass()

def _query_overpass(api,query):
    return api.query(query)

def _parse_osm_result(result):
    data = {'id': [], 'highway': [], 'name': [], 'geometry': []}

    for way in result.ways:
        #if 'highway' in way.tags and way.tags['highway'] == 'primary':
        line = LineString([(node.lon, node.lat) for node in way.nodes])
        data['id'].append(way.id)
        data['highway'].append(way.tags.get('highway'))
        data['name'].append(way.tags.get('name'))
        data['geometry'].append(line)
        # Capture all tags for each way as a dictionary

    #create a GeoDataFrame from the dictionary
    return gpd.GeoDataFrame(data, crs="EPSG:4326").to_crs("EPSG:31468")

def create_osm_streets_gdf():
    """
    Creates a GeoDataFrame of OpenStreetMap streets.

    This function queries the Overpass API with predefined street queries to retrieve OpenStreetMap street data.
    It then parses the result of the query and creates a GeoDataFrame of the streets.
    The resulting GeoDataFrame is saved as a GeoPackage file.

    Returns:
        GeoDataFrame: GeoDataFrame of OpenStreetMap streets.
    """

    #empty list to store the gdf
    list_of_gdf = []

    for street_query in tqdm(osm_street_queries, desc="Querying Overpass"):
    
        result = _query_overpass(api, street_query)
        gdf = _parse_osm_result(result)
        list_of_gdf.append(gdf)

    osm_streets_gdf = concatenate_geodataframes(list_of_gdf)

    save_gdf_as_gpkg(osm_streets_gdf,"osm_street_net_"+config_data["city_name"],interimresult=True, version="0.0")

    return osm_streets_gdf



def main():
    
    create_osm_streets_gdf()



if __name__ == "__main__":
    main()
