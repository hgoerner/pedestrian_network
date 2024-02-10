
import overpy
import pandas as pd
from data.downlaod_osm_streets import query_overpass, parse_osm_result
from data.save_data import safe_gdf_as_gpkg


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


    osm_streets = pd.concat(list_of_gdf)

    safe_gdf_as_gpkg((osm_streets,"dresden_netz"))
if __name__ == "__main__":
    main()