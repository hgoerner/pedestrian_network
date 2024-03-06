import os
import sys

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from data.download.osm_streets import create_osm_streets_gdf
from modules.street_net_creation import \
    create_street_net_and_intersection_gpkg
from utils.save_data import safe_gdf_as_gpkg
from utils.config_loader import config_data




# create_osm_area_gdf()
def main():

    osm_street_net = create_osm_streets_gdf()

    gdf_street_net_optimized,gdf_intersections_points = create_street_net_and_intersection_gpkg(osm_street_net)
    
    safe_gdf_as_gpkg((gdf_street_net_optimized, "street_net_optimized_"+config_data["city_name"]), (gdf_intersections_points, "node_points_"+config_data["city_name"]))


if __name__ == "__main__":
    main()
