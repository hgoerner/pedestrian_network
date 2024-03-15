import os
import sys
import geopandas as gpd
from tqdm import tqdm


current_directory = os.getcwd()


sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import safe_gdf_as_gpkg
from utils.load_data import find_geo_packages
from utils.config_loader import config_data

geo_packages = find_geo_packages()

pois_filepath = geo_packages["pois"]
area_filepath = geo_packages["areas"]

#load necessary geopackages
voroinoi_montreal_gdf = gpd.read_file("data\output\montreal_voronoi.gpkg")
pois_gdf = gpd.read_file(pois_filepath)
area_gdf = gpd.read_file(area_filepath)

#Initialize a new column for the sum of values
voroinoi_montreal_gdf['Summe POI*Bedeutung'] = 0
voroinoi_montreal_gdf['Summe AREA*Bedeutung'] = 0
#voroinoi_montreal_gdf['Summe Einwohner'] = 0

# Iterate through lines and update the Summe POI*Bedeutung column
for idx, polygon in tqdm(voroinoi_montreal_gdf.iterrows()):
    intersected_pois = pois_gdf[pois_gdf['geometry'].intersects(polygon['geometry'])]
    voroinoi_montreal_gdf.at[idx, 'Summe POI*Bedeutung'] = intersected_pois['Bedeutung'].sum()
    
# Iterate through lines and update the Summe AREA*Bedeutung column    
for idx, polygon in tqdm(voroinoi_montreal_gdf.iterrows()):
    intersected_areas = area_gdf[area_gdf['geometry'].intersects(polygon['geometry'])]
    voroinoi_montreal_gdf.at[idx, 'Summe AREA*Bedeutung'] = intersected_areas['Bedeutung'].sum()


voroinoi_montreal_gdf["Bedeutung"] = voroinoi_montreal_gdf["Summe POI*Bedeutung"] + voroinoi_montreal_gdf['Summe AREA*Bedeutung']
voroinoi_montreal_gdf['Bedeutung je quadratmeter'] = voroinoi_montreal_gdf["Bedeutung"] / voroinoi_montreal_gdf.geometry.area


print(voroinoi_montreal_gdf)

# # Drop the intermediate column 'intersected_points'
safe_gdf_as_gpkg((voroinoi_montreal_gdf, f"voronoi_optimized_updated_"+config_data["city_name"]))


