from typing import List

import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString, Point


def start_end_points(line: LineString):
    
    start_point = Point(line.coords[0])
    end_point = Point(line.coords[-1])

    return start_point, end_point


def concatenate_geodataframes(gdf_list: List[gpd.GeoDataFrame]):
    #Concatenate a list of GeoDataFrames
    return pd.concat(gdf_list, ignore_index=True)

def overay_geo_data(optimized_gdf, osm_gdf):
    return gpd.overlay(optimized_gdf, osm_gdf, how='identity')
