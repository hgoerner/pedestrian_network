import matplotlib.pyplot as plt
import geopandas as gpd
from utils.config_loader import config_data
# Import contextily
import contextily as cx
import xyzservices.providers as xyz
import mplleaflet  # Import mplleaflet for creating an interactive leaflet map


def create_plot_of_pois_outlier(gdf_without_outliers: gpd.GeoDataFrame, gdf_outliers: gpd.GeoDataFrame, **kwargs):
    """
    Create a plot of original points and outliers.

    Plots the original points and outliers on a map using customizable markers.
    The size of the markers can be customized using the 'markersize' parameter.

    Args:
        gdf_without_outliers: The GeoDataFrame containing the original points without outliers.
        gdf_outliers: The GeoDataFrame containing the outliers.
        **kwargs: Additional keyword arguments for customizing the plot.
            - markersize (int): The size of the markers. Default is 5.

    Returns:
        None
    """

    # Pass plot parameters as kwargs
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot all points
    gdf_without_outliers.plot(ax=ax, color='blue', alpha=0.5,
                              markersize=kwargs.get('markersize', 5), label='Original Points')

    # Plot outliers
    gdf_outliers.plot(ax=ax, color='red', alpha=0.5,
                      markersize=kwargs.get('markersize', 5), label='Outliers')

    ax.set_title(
        f"Original Points and Outliers for {config_data['city_name']}")
    ax.legend()
    plt.show()


def create_plot_of_pois(gdf_without_outliers: gpd.GeoDataFrame, **kwargs):
    """
    Create a plot of points of interest (POIs) with optional basemap.

    Args:
        outliers_gdf_without_outliers: The GeoDataFrame containing the POIs without outliers.
        **kwargs: Additional keyword arguments for customizing the plot.
            - basemap (bool): Whether to add a basemap using contextily (default: False).
            - markersize (int): The size of the markers for the POIs (default: 5).

    Returns:
        None

    Examples:
        create_plot_of_pois(outliers_gdf, basemap=True, markersize=10)
    """

    # Pass plot parameters as kwargs
    fig, ax = plt.subplots()

    # Plot all points
    gdf_without_outliers.plot(ax=ax, column="Klasse", alpha=0.5,
                              markersize=kwargs.get('markersize', 5), label='Original Points')

    ax.set_title(
        f"Original Pois of {config_data['city_name']}")

    plt.show()
