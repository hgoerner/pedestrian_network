import numpy as np
import geopandas as gpd
import os
import sys
import geopandas as gpd


current_directory = os.getcwd()

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import save_gdf_as_gpkg
from utils.config_loader import config_data

def calculate_direction(line):
    x1, y1 = line.coords[0]
    x2, y2 = line.coords[-1]
    angle = np.degrees(np.arctan2(y2 - y1, x2 - x1)) % 360
    if (angle > 45 and angle < 135) or (angle > 225 and angle < 315):
        return 'East-West'
    else:
        return 'North-South'
    
    
lines_gdf = gpd.read_file(r'data\output\Montréal\street_net_Montréal_v1.2.gpkg')    
    # Calculate directions for each line
lines_gdf['Direction'] = lines_gdf['geometry'].apply(calculate_direction)


save_gdf_as_gpkg(lines_gdf, "street_net_"+config_data["city_name"], final=True, version="1.3")
print(lines_gdf.head())