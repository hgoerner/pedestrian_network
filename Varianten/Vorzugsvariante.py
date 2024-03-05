import os
import sys
import geopandas as gpd
import pandas as pd
from shapely import Point
from tqdm import tqdm

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import safe_gdf_as_gpkg
from utils.load_data import find_files_by_city

#buffer in meter
BUFFERSIZE = 250

Cologne_counts_csv_filepath = r""
#census = r"data\input\Sonstiges\98-401-X2021020_English_CSV_data.csv"

#census_data = pd.read_csv(census, encoding='latin-1',sep=",")

#print(census_data)

#filepaths to files using
street_net_optimized_filepath = r"data\output\street_net_optimized_Cologne.gpkg"
area_Cologne_filepath = r"data\output\osm_area_updated_Cologne.gpkg"
pois_Cologne_filepath = r"data\output\osm_pois_updated_Cologne.gpkg"
nodes_filepath = r"data\output\node_points_Cologne.gpkg"
census_filepath = r""

#read geopackages
street_net_optimized_gdf = gpd.read_file(street_net_optimized_filepath)
area_Cologne_gdf = gpd.read_file(area_Cologne_filepath)
pois_Cologne_gdf = gpd.read_file(pois_Cologne_filepath)


#filter street net to only use streets thar are longer than 100
street_net_optimized_gdf = street_net_optimized_gdf[street_net_optimized_gdf["laenge [km]"] >= 0.1]

#buffer street net by buffersize
street_net_optimized_buffered_gdf = street_net_optimized_gdf.buffer(BUFFERSIZE)

#safe_gdf_as_gpkg((street_net_optimized_buffered_gdf, "street_net_buffered_Cologne", True))

#buffer pois
pois_Cologne_buffered_gdf = pois_Cologne_gdf.copy()
pois_Cologne_buffered_gdf['geometry'] = pois_Cologne_gdf.apply(lambda row: row['geometry'].buffer(row['Einflussbereich']), axis=1)

#buffer areas
area_Cologne_buffered_gdf = area_Cologne_gdf.copy()
area_Cologne_buffered_gdf['geometry'] = area_Cologne_gdf.apply(lambda row: row['geometry'].buffer(row['Einflussbereich']), axis=1)

#safe_gdf_as_gpkg((pois_Cologne_buffered_gdf, "pois_buffered_Cologne", True))

#Initialize a new column for the sum of values
street_net_optimized_gdf['Summe POI*Bedeutung'] = 0
street_net_optimized_gdf['Summe AREA*Bedeutung'] = 0

# Iterate through lines and update the Summe POI*Bedeutung column
for idx, line in tqdm(street_net_optimized_gdf.iterrows()):
    intersected_points = pois_Cologne_buffered_gdf[pois_Cologne_buffered_gdf['geometry'].intersects(line['geometry'])]
    street_net_optimized_gdf.at[idx, 'Summe POI*Bedeutung'] = intersected_points['Bedeutung'].sum()
    
for idx, line in tqdm(street_net_optimized_gdf.iterrows()):
    intersected_areas = area_Cologne_buffered_gdf[area_Cologne_buffered_gdf['geometry'].intersects(line['geometry'])]
    street_net_optimized_gdf.at[idx, 'Summe AREA*Bedeutung'] = intersected_areas['Bedeutung'].sum()
    

street_net_optimized_gdf["Bedeutung je km"] = round((street_net_optimized_gdf["Summe AREA*Bedeutung"] + street_net_optimized_gdf['Summe POI*Bedeutung']) /street_net_optimized_gdf["laenge [km]"] ,2)

# Drop the intermediate column 'intersected_points'
safe_gdf_as_gpkg((street_net_optimized_gdf, "street_net_optimized_updated_Cologne", True))