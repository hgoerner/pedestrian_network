import sys
import os

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')


import geopandas as gpd
from data.load_data import poi_key_value_df
import pandas as pd
from utils.config_loader import config_data
from data.save_data import safe_gdf_as_gpkg

#assign group, categorie and einflussbereich
def assign_group_categorie_einflussbereich(osm_poi_gdf):
    """
    Merges the 'group' and 'categorie' columns of the osm_poi_gdf DataFrame with the poi_key_value_df DataFrame.
    The osm_poi_gdf DataFrame is updated and overwritten with the merged result.

    Args:
        osm_poi_gdf: The GeoDataFrame containing the OpenStreetMap points of interest data.

    Returns:
        The updated osm_poi_gdf DataFrame with the 'group' and 'categorie' columns merged.

    """    
    #merge group and categorie
    #updates and overwrites the osm_poi_gdf
    osm_poi_gdf = pd.merge(osm_poi_gdf, poi_key_value_df, left_on=['osm_key','osm_value'], right_on=['Key', 'value'], how='left')


    return osm_poi_gdf



def main():
    # function for testing

    osm_pois_gdf = gpd.read_file(config_data["test_osm_poi_package"])
    osm_pois_gdf = assign_group_categorie_einflussbereich(osm_pois_gdf)
    safe_gdf_as_gpkg((osm_pois_gdf,"osm_pois_dresden_updated" ))
    



if __name__ == "__main__":
    main()

