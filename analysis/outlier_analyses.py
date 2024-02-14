from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import geopandas as gpd
from utils.config_loader import config_data
from utils.save_data import safe_gdf_as_gpkg
import matplotlib.pyplot as plt

def find_outliers(osm_points_gdf: gpd.GeoDataFrame):
    # Your GeoDataFrame with points
    points_gdf = gpd.read_file(r"output\osm_pois_dresden_updated.gpkg")

    # Extract and normalize the coordinates for clustering
    coords = StandardScaler().fit_transform(points_gdf.geometry.apply(lambda geom: [geom.x, geom.y]).tolist())

    # Apply DBSCAN clustering
    dbscan = DBSCAN(eps=1, min_samples=5)
    points_gdf['cluster'] = dbscan.fit_predict(coords)

    # Identify outliers as points not assigned to any cluster (-1) or in small clusters
    outliers_gdf = points_gdf[(points_gdf['cluster'] == -1) | (points_gdf.groupby('cluster')['cluster'].transform('count') < 5)]

    #Plot the original points and outliers for visual inspection
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot all points
    points_gdf.plot(ax=ax, color='blue', alpha=0.5, markersize=5, label='Original Points')

    # Plot outliers
    outliers_gdf.plot(ax=ax, color='red', alpha=0.5, markersize=5, label='Outliers')
    safe_gdf_as_gpkg((outliers_gdf,"osm_pois_outliers_"+config_data["city_name"], True))

    city = config_data["city_name"]

    ax.set_title(f'Original Points and Outliers for {city}')
    ax.legend()
    plt.show()