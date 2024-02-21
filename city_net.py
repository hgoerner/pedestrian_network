from data.download_osm.download_osm_streets import create_osm_streets_gdf
from modules.modules_street.street_net_creation import \
    create_street_net_and_intersection_gpkg


# create_osm_area_gdf()
def main():

    osm_street_net = create_osm_streets_gdf()

    create_street_net_and_intersection_gpkg(osm_street_net=osm_street_net)


if __name__ == "__main__":
    main()
