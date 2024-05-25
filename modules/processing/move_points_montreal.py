import os
import sys
import geopandas as gpd
from shapely.geometry import Point
from tqdm import tqdm

current_directory = os.getcwd()

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import save_gdf_as_gpkg
from utils.load_data import find_geo_packages
from utils.config_loader import config_data



def find_closest_line_end(point, lines):
    # Initialize minimum distance to a large number
    min_distance = float('inf')
    closest_point = None
    
    # Iterate over each line to find the closest endpoint
    for line in tqdm(lines.geometry, desc="Querying Overpass"):
        start_point = Point(line.coords[0])
        end_point = Point(line.coords[-1])
        
        # Calculate distances to start and end points of the line
        distance_to_start = point.distance(start_point)
        distance_to_end = point.distance(end_point)
        
        # Update the closest point if a closer endpoint is found
        if distance_to_start < min_distance:
            min_distance = distance_to_start
            closest_point = start_point
        if distance_to_end < min_distance:
            min_distance = distance_to_end
            closest_point = end_point

    return closest_point

def read_geo_packages():
    """
    Reads and returns GeoDataFrames for street network and points of interest from the found geo packages.

    Returns:
        Dictionary with keys "street_net" and "pois" mapping to the respective GeoDataFrames.
    """
    geo_packages = find_geo_packages()
    return {
        "street_net": gpd.read_file(geo_packages["streets"]),
        
    } 
    
def main():  
    geo_packages = read_geo_packages()
    street_net_optimized_updated_gdf = geo_packages["street_net"]
    # Update each point's geometry to the closest line endpoint
    points_df = gpd.read_file("data\output\intersections_with_counts_montreal.gpkg")
    points_df['geometry'] = points_df['geometry'].apply(lambda point: find_closest_line_end(point, street_net_optimized_updated_gdf))
   
    save_gdf_as_gpkg(points_df, f"intersection_with_counts_updated_" + config_data["city_name"], final=True)

if __name__ == "__main__":
    main()