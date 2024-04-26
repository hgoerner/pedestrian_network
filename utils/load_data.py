import os
import sys
import pandas as pd

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.config_loader import config_data
import os

def find_geo_packages(city_name = config_data["city_name"], output_folder="data\output"):
    """
    Find GeoPackage files in the specified output folder that match the given city name.

    Args:
        city_name (str, optional): The name of the city to search for in the file names. Defaults to the value from config_data.
        output_folder (str, optional): The path to the output folder where the GeoPackage files are located. Defaults to "data\output".

    Returns:
        dict: A dictionary mapping the file keys to their corresponding file paths.

    """
    gpkg_files = {}
    
    for file in os.listdir(output_folder):
        if file.endswith(".gpkg"):
            if "street" in file and city_name in file:
                gpkg_files["streets"] = os.path.join(output_folder, file)
            elif "area" in file and city_name in file:
                gpkg_files["areas"] = os.path.join(output_folder, file)  
            elif "pois" in file and city_name in file:
                gpkg_files["pois"] = os.path.join(output_folder, file)
            elif "node" in file and city_name in file:
                gpkg_files["nodes"] = os.path.join(output_folder, file)
            elif "zensus" in file:
                gpkg_files["census"] = os.path.join(output_folder, file)

    return gpkg_files

poi_csv = config_data["path_to_poi_csv"]
area_csv = config_data["path_to_area_csv"]
# Read the CSV file into a DataFrame

poi_key_value_df = pd.read_csv(poi_csv, sep=';')
area_key_value_df = pd.read_csv(area_csv, sep=';')

# Convert DataFrame to a dictionary
poi_key_value_dic = poi_key_value_df.to_dict('index')
# dictionary is wrong, better a diffferent attapt
area_key_value_dic = area_key_value_df.to_dict('index')

#TODO: create load function for the different used geodataframes
# like osm street net, osm_pois, 

