
import overpy
import geopandas as gpd
from shapely.geometry import LineString
import pandas as pd

def query_overpass(api, query):
    result = api.query(query)
    return result

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

    print(type(data))


    gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")
    gdf = gdf.to_crs("EPSG:31468")
    return gdf

def main():

    api = overpy.Overpass()
    city_name = "Dresden"

    # types used in the FoPS projekt
    street_types_list = ["primary", "secondary", "tertiary", "unclassified"]
    list_of_gdf = []

    for street_type in street_types_list:

        # Example query for highways in germany/dresden

        overpass_query = f"""
        area["ISO3166-1"="DE"][admin_level=2]->.country;
        area[name="{city_name}"]->.city;
            way[highway={street_type}](area.city)(area.country);
            (._;>;);
            out body;
    """

        result = query_overpass(api, overpass_query)
        gdf = parse_osm_result(result)
        list_of_gdf.append(gdf)


    gdf = pd.concat(list_of_gdf)


    # # Save the GeoDataFrame as a Shapefile
    # output_shapefile = "highways.shp"
    # gdf.to_file(output_shapefile)
    # Save the GeoDataFrame as a GeoPackage
    output_geopackage = "dresden_netz.gpkg"
    gdf.to_file(output_geopackage, layer='data', driver='GPKG')

if __name__ == "__main__":
    main()