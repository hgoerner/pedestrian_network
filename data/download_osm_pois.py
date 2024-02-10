import geopandas as gpd
from shapely.geometry import LineString
import sys

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')


def query_overpass(api, query):
    return api.query(query)

def parse_osm_result(result):
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