from utils.config_loader import config_data
import pandas as pd

csv_file_path = config_data["path_to_poi_csv"]
# Read the CSV file into a DataFrame
poi_key_value_df = pd.read_csv(csv_file_path, sep=';')

# Convert DataFrame to a dictionary
poi_key_value_dic = poi_key_value_df.to_dict('index')

#TODO: create load function for the different used geodataframes
# like osm street net, osm_pois, 