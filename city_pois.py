
from analysis.outlier_analyses import find_outliers
from analysis.visualisation import create_plot_of_pois_outlier, create_plot_of_pois


import geopandas as gpd


# create_osm_area_gdf()
def main():

    # osm_poi_gdf = create_osm_poi_gdf()
    # osm_poi_gdf_updated = assign_group_categorie_einflussbereich(osm_poi_gdf)
    osm_poi_gdf_updated = gpd.read_file("output\osm_pois_dresden_updated.gpkg")
    print(osm_poi_gdf_updated)

    gdf_pois_without_outliers, gdf_pois_with_outliers = find_outliers(
        osm_poi_gdf_updated)
    create_plot_of_pois_outlier(gdf_pois_without_outliers, gdf_pois_with_outliers)
    create_plot_of_pois(gdf_pois_without_outliers, basemap=True, markersize=5)


if __name__ == "__main__":
    main()
