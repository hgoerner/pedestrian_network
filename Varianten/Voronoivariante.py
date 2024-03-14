import os
import sys
import geopandas as gpd


current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import safe_gdf_as_gpkg
from utils.load_data import find_geo_packages

geo_packages = find_geo_packages()

pois_filepath = geo_packages["pois"]
area_filepath = geo_packages["areas"]


#load necessary geopackages
voroinoi_montreal_gdf = gpd.read_file("data\output\montreal_voronoi.gpkg")
pois_gdf = gpd.read_file(pois_filepath)
area_gdf = gpd.read_file(area_filepath)

print(pois_gdf)

