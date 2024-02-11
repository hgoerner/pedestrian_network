from utils.config_loader import config_data
import pandas as pd

poi_csv = config_data["path_to_poi_csv"]
area_csv = config_data["path_to_area_csv"]
# Read the CSV file into a DataFrame

poi_key_value_df = pd.read_csv(poi_csv, sep=';')
area_key_value_df = pd.read_csv(area_csv, sep=';')

# Convert DataFrame to a dictionary
poi_key_value_dic = poi_key_value_df.to_dict('index')
area_key_value_dic = area_key_value_df.to_dict('index')

#TODO: create load function for the different used geodataframes
# like osm street net, osm_pois, 