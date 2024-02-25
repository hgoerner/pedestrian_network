
from analysis.outlier_analyses import find_outliers
from analysis.visualisation import create_plot_of_pois_outlier, create_plot_of_pois
from data.download.osm_pois import create_osm_poi_gdf
from modules.poi_processing import assign_group_categorie_poi
from utils.config_loader import config_data
import geopandas as gpd

from utils.save_data import safe_gdf_as_gpkg


# create_osm_area_gdf()
def main():

    osm_poi_gdf = create_osm_poi_gdf()
   
    gdf_pois_without_outliers, gdf_pois_with_outliers = find_outliers(osm_poi_gdf)
    osm_poi_gdf_updated = assign_group_categorie_poi(gdf_pois_without_outliers)
    safe_gdf_as_gpkg((osm_poi_gdf_updated, "osm_pois_updated_"+config_data["city_name"]))   
    
    # create_plot_of_pois_outlier(gdf_pois_without_outliers, gdf_pois_with_outliers)
    # create_plot_of_pois(gdf_pois_without_outliers, basemap=True, markersize=5)


if __name__ == "__main__":
    main()
