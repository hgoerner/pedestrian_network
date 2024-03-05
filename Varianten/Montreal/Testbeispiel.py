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

montreal_counts_csv_filepath = r"data\input\Sonstiges\comptages_vehicules_cyclistes_pietons.csv"
census = r"data\input\Sonstiges\98-401-X2021020_English_CSV_data.csv"

<<<<<<< HEAD
census_data = pd.read_csv(census, encoding='latin-1',sep=",")
print(census_data)

#filepaths to files using
street_net_optimized_filepath = r"data\output\street_net_optimized_Montreal.gpkg"
area_montreal_filepath = r"data\output\osm_area_updated_Montreal.gpkg"
pois_montreal_filepath = r"data\output\osm_pois_updated_Montreal.gpkg"
nodes_filepath = r"data\output\node_points_Montreal.gpkg"
=======
#montreal crs TODO: transfer all necessarry gpkg to this crs
crs = "EPSG:4326"
>>>>>>> parent of 387eb5d (update to 4326 crs)

#read geopackages
street_net_optimized_gdf = gpd.read_file(street_net_optimized_filepath)
area_montreal_gdf = gpd.read_file(area_montreal_filepath)
pois_montreal_gdf = gpd.read_file(pois_montreal_filepath)

#filter street net to only use streets thar are longer than 100
street_net_optimized_gdf = street_net_optimized_gdf[street_net_optimized_gdf["laenge [km]"] >= 0.1]

#buffer street net by buffersize
street_net_optimized_buffered_gdf = street_net_optimized_gdf.buffer(BUFFERSIZE)

<<<<<<< HEAD
#safe_gdf_as_gpkg((street_net_optimized_buffered_gdf, "street_net_buffered_montreal", True))
=======
# return 729 Knotenpunkte
print(len(monetreal_counts_ped_df["Nom_Intersection"].unique()))

# Create a GeoDataFrame with the original DataFrame and the geometry
monetreal_counts_ped_gdf = gpd.GeoDataFrame(monetreal_counts_ped_df, geometry=geometry, crs=crs)
>>>>>>> parent of 387eb5d (update to 4326 crs)

#buffer pois
pois_montreal_buffered_gdf = pois_montreal_gdf.copy()
pois_montreal_buffered_gdf['geometry'] = pois_montreal_gdf.apply(lambda row: row['geometry'].buffer(row['Einflussbereich']), axis=1)

#buffer areas
area_montreal_buffered_gdf = area_montreal_gdf.copy()
area_montreal_buffered_gdf['geometry'] = area_montreal_gdf.apply(lambda row: row['geometry'].buffer(row['Einflussbereich']), axis=1)

#safe_gdf_as_gpkg((pois_montreal_buffered_gdf, "pois_buffered_montreal", True))

#Initialize a new column for the sum of values
street_net_optimized_gdf['Summe POI*Bedeutung'] = 0
street_net_optimized_gdf['Summe AREA*Bedeutung'] = 0

# Iterate through lines and update the Summe POI*Bedeutung column
for idx, line in tqdm(street_net_optimized_gdf.iterrows()):
    intersected_points = pois_montreal_buffered_gdf[pois_montreal_buffered_gdf['geometry'].intersects(line['geometry'])]
    street_net_optimized_gdf.at[idx, 'Summe POI*Bedeutung'] = intersected_points['Bedeutung'].sum()
    
for idx, line in tqdm(street_net_optimized_gdf.iterrows()):
    intersected_areas = area_montreal_buffered_gdf[area_montreal_buffered_gdf['geometry'].intersects(line['geometry'])]
    street_net_optimized_gdf.at[idx, 'Summe AREA*Bedeutung'] = intersected_areas['Bedeutung'].sum()
    

street_net_optimized_gdf["Bedeutung je km"] = round((street_net_optimized_gdf["Summe AREA*Bedeutung"] + street_net_optimized_gdf['Summe POI*Bedeutung']) /street_net_optimized_gdf["laenge [km]"] ,2)

# Drop the intermediate column 'intersected_points'
safe_gdf_as_gpkg((street_net_optimized_gdf, "street_net_optimized_updated_montreal", True))


# #montreal crs TODO: transfer all necessarry gpkg to this crs

# crs = "EPSG:4326"
# # CRS from website
# #crs = "EPSG:32188"

# monetreal_counts_df = pd.read_csv(montreal_counts_csv_filepath, sep=",")

# #filter only pedestrians
# monetreal_counts_ped_df = monetreal_counts_df[monetreal_counts_df["Description_Code_Banque"] == "Pietons"]

# # Create a GeoDataFrame with Point geometries
# geometry = [Point(xy) for xy in zip(monetreal_counts_ped_df['Longitude'], monetreal_counts_ped_df['Latitude'])]

# # return 729 Knotenpunkte
# #print(len(monetreal_counts_ped_df["Nom_Intersection"].unique()))
# # Create a GeoDataFrame with the original DataFrame and the geometry
# monetreal_counts_ped_gdf = gpd.GeoDataFrame(monetreal_counts_ped_df, geometry=geometry, crs=crs)

# #safe_gdf_as_gpkg((monetreal_counts_ped_gdf, "intersections_with_counts_montreal"))

# #montreal_counts = gpd.read_file()