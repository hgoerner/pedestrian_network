
import sys
sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')

import geopandas as gpd
from shapely.geometry import LineString
import overpy
from queries.queries import osm_street_queries
from save_data import safe_gdf_as_gpkg
from utils.helper import concatenate_geodataframes
from utils.config_loader import config_data

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

    Returns: None
    """
    #empty list to store the gdf
    list_of_gdf = []

    for street_query in osm_street_queries:
    
        result = _query_overpass(api, street_query)
        gdf = _parse_osm_result(result)
        list_of_gdf.append(gdf)

    osm_streets = concatenate_geodataframes(list_of_gdf)

    safe_gdf_as_gpkg((osm_streets,"osm_street_net_"+config_data["city_name"],True))




