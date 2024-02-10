import sys
sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
import overpy
import geopandas as gpd
from shapely.geometry import Point
from queries.queries import osm_poi_queries
from save_data import safe_gdf_as_gpkg
from utils.helper import concatenate_geodataframes
from utils.config_loader import config_data

api = overpy.Overpass()

def _query_overpass(api,query):
    return api.query(query)

def _parse_osm_poi_result(result):
    data = {'id': [],'key': [],'value': [],'geometry': []}

    for node in result.nodes:
        # Accessing key-value pairs in the tags dictionary
        for key, value in node.tags.items():
            data['id'].append(node.id)
            data['key'].append(key)
            data['value'].append(value)
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

    for poi_query in osm_poi_queries:  
        print(poi_query)
        result = _query_overpass(api, poi_query)
        gdf = _parse_osm_poi_result(result)
        list_of_gdf.append(gdf)

    osm_streets = concatenate_geodataframes(list_of_gdf)

    safe_gdf_as_gpkg((osm_streets,"osm_pois_"+config_data["city_name"],True))


def main():

    create_osm_poi_gdf()
if __name__ == "__main__":
    main()