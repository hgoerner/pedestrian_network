import os
import sys
from shapely.geometry import Point
import geopandas as gpd
import rtree
from tqdm import tqdm
from shapely.geometry import Polygon
import math

current_directory = os.getcwd()

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import save_gdf_as_gpkg
from utils.load_data import find_geo_packages
from utils.config_loader import config_data


def buffer_points(points_gdf):
    
    buffered_points_gdf = points_gdf.buffer(10)

    return buffered_points_gdf


gdf_points = gpd.read_file(r'data\output\Montréal\intersections_with_counts_montreal_updated_v1.2.gpkg')

buffered_points_gdf = buffer_points(gdf_points)

save_gdf_as_gpkg(buffered_points_gdf, "intersections_with_counts_montreal_updated_buffered", final=True, version="1.0")


def split_circle(polygon):
    # Get the center and radius of the circle
    centroid = polygon.centroid
    radius = polygon.exterior.distance(centroid)
    
    # Define the rotated angles for splitting the circle
    angles = [0, math.pi / 2, math.pi, 3 * math.pi / 2]
    rotated_angles = [angle + math.pi / 4 for angle in angles]
    
    # Create the four sectors
    sectors = []
    for i in range(len(rotated_angles)):
        p1 = Point(centroid.x + radius * math.cos(rotated_angles[i]), centroid.y + radius * math.sin(rotated_angles[i]))
        p2 = Point(centroid.x + radius * math.cos(rotated_angles[(i + 1) % 4]), centroid.y + radius * math.sin(rotated_angles[(i + 1) % 4]))
        sector = Polygon([(centroid.x, centroid.y), (p1.x, p1.y), (p2.x, p2.y), (centroid.x, centroid.y)])
        sectors.append(sector)
    
    return sectors

# Apply the split function to the circular polygons
split_polygons = []

for polygon in buffered_points_gdf.geometry:
    if isinstance(polygon, Polygon) and polygon.exterior.is_closed:
        sectors = split_circle(polygon)
        split_polygons.extend(sectors)
    else:
        split_polygons.append(polygon)

# Create a new GeoDataFrame with the split polygons
split_gdf = gpd.GeoDataFrame(geometry=split_polygons, crs=buffered_points_gdf.crs)

save_gdf_as_gpkg(split_gdf, "intersections_with_counts_montreal_updated_buffered_splitted", final=True, version="1.0")