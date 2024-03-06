import os
import sys
import geopandas as gpd
import pandas as pd

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import safe_gdf_as_gpkg
from utils.config_loader import config_data
from utils.load_data import area_key_value_df

# assign group, categorie and einflussbereich

def assign_group_categorie_to_area(osm_area_gdf: gpd.GeoDataFrame):
    """
    Assigns group and category to each area in the given GeoDataFrame.

    Args:
        osm_area_gdf (gpd.GeoDataFrame): The GeoDataFrame containing the areas to be assigned.

    Returns:
        gpd.GeoDataFrame: The updated GeoDataFrame with group and category assigned to each area.
    """

    # merge group and categorie
    # updates and overwrites the osm_area_gdf
    osm_area_gdf = pd.merge(osm_area_gdf, area_key_value_df, left_on=[
                           'osm_key', 'osm_value'], right_on=['Key', 'value'], how='left')

    return osm_area_gdf

def main():

    #osm_area_gdf = create_osm_area_gdf()
    
    osm_area_gdf = gpd.read_file(r"C:\Users\Hendr\OneDrive\Desktop\pedestrian_network\output\interim_result\osm_area_plain_Dresden.gpkg")
    osm_area_gdf_uptated = assign_group_categorie_to_area(osm_area_gdf)
    print(osm_area_gdf)
    
    safe_gdf_as_gpkg(
            (osm_area_gdf_uptated, "osm_area_updated_"+config_data["city_name"]))


if __name__ == "__main__":
    main()
