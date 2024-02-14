import sys
import os
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

import overpy
import geopandas as gpd
from shapely.geometry import Point
from data.queries.queries import osm_poi_queries
from utils.save_data import safe_gdf_as_gpkg
from utils.helper import concatenate_geodataframes
from utils.config_loader import config_data
import logging
from tqdm import tqdm
from overpy.exception import OverpassBadRequest
import matplotlib.pyplot as plt

# Configure logging
#logging.basicConfig(filename='missing_queries.txt', level=logging.WARNING)
logging.basicConfig(filename='Result_insights.txt', level=logging.INFO, filemode='w')

api = overpy.Overpass()

def _query_overpass(api,query):
    """
    Query the Overpass API with the given query.

    Args:
        api: The Overpass API object.
        query: The query string to be executed with keys and values form osm.

    Returns:
        The result of the query.

    Raises:
        OverpassBadRequest: If the query is invalid.
    Examples:
        >>> api = OverpassAPI()
        >>> query = siehe queryservice
        >>> result = _query_overpass(api, query)
    """

    try:
        return api.query(query)
    except OverpassBadRequest as e:
        # Handle the exception (e.g., print an error message)
        print(f"OverpassBadRequest: {e}")
    


def _parse_osm_poi_result(result: overpy.Result, osm_key: str, osm_value: str, **kwargs):
    """
    Parses the result of a query to a GeoDataFrame.

    Args:
        result: The result of the query.
    """
    # Create an empty dictionary to store the data 
    data = {'id': [],'osm_key': [],'osm_value': [],'geometry': []}

    for node in result.nodes:
        # Accessing key-value pairs in the tags dictionary
        data['id'].append(node.id)
        data['osm_key'].append(osm_key)
        data['osm_value'].append(osm_value)
        data['geometry'].append(Point(node.lon, node.lat))

    #create a GeoDataFrame from the dictionary
    return gpd.GeoDataFrame(data, crs="EPSG:4326").to_crs("EPSG:31468")



def create_osm_poi_gdf():
    """
    Creates a GeoDataFrame of OpenStreetMap streets.

    Returns: None
    """
    #empty list to store the gdf
    list_of_gdf = []

    for query_info in tqdm(osm_poi_queries, desc="Querying Overpass"):
        poi_query = query_info['query']
        osm_key = query_info['key']
        osm_value = query_info['value']
        result = _query_overpass(api, poi_query)
        if result is not None:
            gdf = _parse_osm_poi_result(result, osm_key,osm_value)
            list_of_gdf.append(gdf)
            #add information to logfile
            number_of_pois = len(result.nodes)
            logging.info(f"osmKey: {osm_key} OsmValue: {osm_value} Anzahl_pois {number_of_pois}")
        else:
            # Log the missing query to the log file
            #logging.warning(f"Missing result for query: {osm_key} - {osm_value} in {poi_query}")
            continue

    osm_poi_gdf = concatenate_geodataframes(list_of_gdf)
    safe_gdf_as_gpkg((osm_poi_gdf,"osm_pois_plain_"+config_data["city_name"]))


def find_outliers():
    # Your GeoDataFrame with points
    points_gdf = gpd.read_file(r"output\osm_pois_dresden_updated.gpkg")

    # Extract and normalize the coordinates for clustering
    coords = StandardScaler().fit_transform(points_gdf.geometry.apply(lambda geom: [geom.x, geom.y]).tolist())

    # Apply DBSCAN clustering
    dbscan = DBSCAN(eps=1, min_samples=5)
    points_gdf['cluster'] = dbscan.fit_predict(coords)

    # Identify outliers as points not assigned to any cluster (-1) or in small clusters
    outliers_gdf = points_gdf[(points_gdf['cluster'] == -1) | (points_gdf.groupby('cluster')['cluster'].transform('count') < 5)]
    print(outliers_gdf.size)
    print(points_gdf.size)
    #Plot the original points and outliers for visual inspection
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot all points
    points_gdf.plot(ax=ax, color='blue', alpha=0.5, markersize=5, label='Original Points')

    # Plot outliers
    outliers_gdf.plot(ax=ax, color='red', alpha=0.5, markersize=5, label='Outliers')
    safe_gdf_as_gpkg((outliers_gdf,"osm_pois_outliers_"+config_data["city_name"], True), (points_gdf,"osm_pois_original"+config_data["city_name"], True))

    ax.set_title('Original Points and Outliers for Dresden')
    ax.legend()
    plt.show()


def main():
    #create_osm_poi_gdf()
    find_outliers()
if __name__ == "__main__":
    main()