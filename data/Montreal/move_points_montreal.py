import os
import sys
from shapely.geometry import Point
import geopandas as gpd
from tqdm import tqdm

current_directory = os.getcwd()

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import save_gdf_as_gpkg
from utils.config_loader import config_data


def closest_endpoint_on_line(point, lines, sindex, buffer_distance=1000):
    closest_point = None
    min_distance = float('inf')
    
    # Use the spatial index to find candidate lines within the buffer distance
    possible_matches_index = list(sindex.intersection(point.buffer(buffer_distance).bounds))
    possible_matches = lines.iloc[possible_matches_index]
    
    for line in possible_matches.geometry:
        start_point = Point(line.coords[0])
        end_point = Point(line.coords[-1])
        
        start_distance = point.distance(start_point)
        end_distance = point.distance(end_point)
        
        if start_distance < min_distance:
            min_distance = start_distance
            closest_point = start_point
        
        if end_distance < min_distance:
            min_distance = end_distance
            closest_point = end_point
    
    return closest_point


# Example usage
# Load your GeoDataFrames

gdf_points = gpd.read_file(r'data\Montreal\Studienarbeit\intesection_counts_montreal_ohne21_aprl_okt.gpkg')

print(f"old_crs: {gdf_points.crs}")

gdf_lines = gpd.read_file(r'data\output\Montréal\street_net_Montréal_v1.2.gpkg')

# Create a spatial index for the lines
lines_sindex = gdf_lines.sindex

# Convert the CRS of the points GeoDataFrame to EPSG:31468
gdf_points = gdf_points.to_crs(epsg=31468)
print(f"new_crs: {gdf_points.crs}")

# Update the coordinates of the points with the coordinates of the closest endpoints
# Iterate over each point to find and update with the closest endpoint of any line
for index, point in tqdm(gdf_points.iterrows()):
    closest_point = closest_endpoint_on_line(point.geometry, gdf_lines, lines_sindex)
    gdf_points.at[index, 'geometry'] = closest_point
    
save_gdf_as_gpkg(gdf_points, "intersections_with_counts_montreal_StDa", final=True, version="1.3")

# Save the updated points GeoDataFrame to a new shapefile if needed
