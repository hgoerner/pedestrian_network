from data.download.osm_area import create_osm_area_gdf
from modules.area_processing import assign_group_categorie_to_area
from utils.save_data import save_gdf_as_gpkg
from utils.config_loader import config_data

# create_osm_area_gdf()
def main():
    
    osm_area_gdf = create_osm_area_gdf()
    osm_area_gdf_updated = assign_group_categorie_to_area(osm_area_gdf)
    
    save_gdf_as_gpkg(osm_area_gdf_updated, "osm_area_"+config_data["city_name"], version= "1.1")


if __name__ == "__main__":
    main()