
import overpy
import pandas as pd

from osm_data_recieve import query_overpass, parse_osm_result



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
    output_geopackage = "network\output\dresden_netz.gpkg"
    gdf.to_file(output_geopackage, layer='data', driver='GPKG')



if __name__ == "__main__":
    main()