
import geopandas as gpd
from shapely.geometry import LineString

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

            # Capture all tags for each way as a dictionary
            # there way more keys and values
            # its possible to catch all the keys and possible value
            # Enter code to do this here!

            # for key in way.tags.keys():
            #     if key not in data.keys():
            #        data[key] = []

    return gpd.GeoDataFrame(data, crs="EPSG:4326").to_crs("EPSG:31468")

