
import os
import sys

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

#from analysis.outlier_analyses import find_outliers
from data.download.osm_pois import create_osm_poi_gdf
from modules.poi_processing import assign_group_categorie_poi

# create_osm_area_gdf()
def main():

    osm_poi_gdf = create_osm_poi_gdf()
   
    #gdf_pois_without_outliers, gdf_pois_with_outliers = find_outliers(osm_poi_gdf)
    assign_group_categorie_poi(osm_poi_gdf)
     
    
    # create_plot_of_pois_outlier(gdf_pois_without_outliers, gdf_pois_with_outliers)
    # create_plot_of_pois(gdf_pois_without_outliers, basemap=True, markersize=5)


if __name__ == "__main__":
    main()
