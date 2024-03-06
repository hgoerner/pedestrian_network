from utils.config_loader import config_data
import pandas as pd
import os

def find_files_by_city(folder_path = f'data\output', target_name=config_data["city_name"]):
    matching_files = []
    
    # Get the list of files in the specified folder
    files_in_folder = os.listdir(folder_path)
    
    # Check if the target_name is in the file names
    matching_files = [file for file in files_in_folder if target_name in file]

    # Return the list of matching files
    return matching_files


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

