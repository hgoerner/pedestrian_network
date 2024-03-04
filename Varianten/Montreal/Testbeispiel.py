import os
import sys
import geopandas as gpd
import pandas as pd
from shapely import Point

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')


from utils.save_data import safe_gdf_as_gpkg

montreal_counts_csv_filepath = r"data\input\Sonstiges\comptages_vehicules_cyclistes_pietons.csv"

#montreal crs TODO: transfer all necessarry gpkg to this crs

crs = "EPSG:4326"
# CRS from website
#crs = "EPSG:32188"

monetreal_counts_df = pd.read_csv(montreal_counts_csv_filepath, sep=",")

#filter only pedestrians
monetreal_counts_ped_df = monetreal_counts_df[monetreal_counts_df["Description_Code_Banque"] == "Pietons"]
print(monetreal_counts_ped_df)

# Create a GeoDataFrame with Point geometries
geometry = [Point(xy) for xy in zip(monetreal_counts_ped_df['Longitude'], monetreal_counts_ped_df['Latitude'])]

# return 729 Knotenpunkte
print(len(monetreal_counts_ped_df["Nom_Intersection"].unique()))
# Create a GeoDataFrame with the original DataFrame and the geometry
monetreal_counts_ped_gdf = gpd.GeoDataFrame(monetreal_counts_ped_df, geometry=geometry, crs=crs)

safe_gdf_as_gpkg((monetreal_counts_ped_gdf, "intersections_with_counts_montreal"))

#montreal_counts = gpd.read_file()