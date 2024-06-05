import os
import sys

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from data.download.osm_streets import create_osm_streets_gdf
from modules.street_net_creation import \
    create_street_net_and_intersection_gpkg





# create_osm_area_gdf()
def main():

    osm_street_net = create_osm_streets_gdf()

    create_street_net_and_intersection_gpkg(osm_street_net)
    


if __name__ == "__main__":
    main()
