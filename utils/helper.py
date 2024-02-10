from shapely.geometry import Point, LineString
import geopandas as gpd
from typing import List
import pandas as pd

def start_end_points(line: LineString):
    
    start_point = Point(line.coords[0])
    end_point = Point(line.coords[-1])

    return start_point, end_point


def concatenate_geodataframes(gdf_list: List[gpd.GeoDataFrame]):
    #Concatenate a list of GeoDataFrames
    return pd.concat(gdf_list, ignore_index=True)