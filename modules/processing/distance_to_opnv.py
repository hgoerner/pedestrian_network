import os
import sys
import geopandas as gpd
from tqdm import tqdm
import pandas as pd
from geopy.distance import geodesic


current_directory = os.getcwd()

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import safe_gdf_as_gpkg
from utils.load_data import find_geo_packages
from utils.config_loader import config_data

geo_packages = find_geo_packages()


#filepaths to files using
street_net_filepath = geo_packages["streets"]
area_filepath = geo_packages["areas"]
pois_filepath = geo_packages["pois"]
nodes_filepath = geo_packages["nodes"]

#read geopackages
street_net_optimized_gdf = gpd.read_file(street_net_filepath)
area_gdf = gpd.read_file(area_filepath)
pois_gdf = gpd.read_file(pois_filepath)

# filter pois 
pois_opnv_gdf = pois_gdf[pois_gdf["Gruppe"] == "Haltestellen des OPNV"]


# Iterate through lines and update the Summe AREA*Bedeutung column    
for idx, line in tqdm(street_net_optimized_gdf.iterrows()):
    min_dist = float('inf')  # Initialize minimum distance to infinity
    closest_point = None
    
    # Iterate through each point
    for point_idx, point in pois_opnv_gdf.iterrows():
        # Calculate geodesic distance between line and point
        dist = line.geometry.distance(point.geometry)
        
        # Check if this point is closer than the current closest point
        # dist in meters
        if dist < min_dist:
            min_dist = dist
            closest_point = point
           
   
    # Assign the closest point to the 'closest_point' column of the line
    street_net_optimized_gdf.at[idx, 'distance_to_opnv'] = dist
    
safe_gdf_as_gpkg((street_net_optimized_gdf, f"street_net_optimized_updated_"+config_data["city_name"]))