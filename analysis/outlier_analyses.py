from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import geopandas as gpd
import pandas as pd


def find_outliers(osm_points_gdf: gpd.GeoDataFrame):
    """
    Find outliers in a GeoDataFrame of OpenStreetMap points.

    Extracts and normalizes the coordinates of the points for clustering.
    Applies DBSCAN clustering to identify clusters of points.
    Identifies outliers as points not assigned to any cluster or in small clusters.
    Returns two GeoDataFrames: one with the points without outliers and one with the outliers.

    Args:
        osm_points_gdf: The GeoDataFrame containing the OpenStreetMap points.

    Returns:
        gdf_points_without_outliers: The GeoDataFrame containing the points without outliers.
        gdf_points_with_outliers: The GeoDataFrame containing the outliers.
    """

    # Extract and normalize the coordinates for clustering
    coords = StandardScaler().fit_transform(
        osm_points_gdf.geometry.apply(lambda geom: [geom.x, geom.y]).tolist())

    # Apply DBSCAN clustering
    dbscan = DBSCAN(eps=1, min_samples=5)
    osm_points_gdf['cluster'] = dbscan.fit_predict(coords)

    # Identify outliers as points not assigned to any cluster (-1) or in small clusters
    gdf_points_with_outliers = osm_points_gdf[(osm_points_gdf['cluster'] == -1) | (
        osm_points_gdf.groupby('cluster')['cluster'].transform('count') < 5)]

    # Subtract df2 from df1
    gdf_points_without_outliers = pd.merge(osm_points_gdf, gdf_points_with_outliers, how='outer', indicator=True).query(
        '_merge == "left_only"').drop('_merge', axis=1)

    return gdf_points_without_outliers, gdf_points_with_outliers
