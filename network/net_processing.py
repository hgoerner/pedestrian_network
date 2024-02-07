import geopandas as gpd
import networkx as nx
from shapely.geometry import Point, LineString
from shapely.ops import unary_union
from config import test_package
from config import safe_interim_results
import pandas as pd
import math



#first combine every netelement

def safe_gdf_as_gpkg(gdf, filename, interim_result: bool = True, safe = safe_interim_results): 
    if interim_result and safe:
        gdf.to_file(f'network\output\interim_result\{filename}.gpkg', driver='GPKG')
    elif not interim_result and safe:
        gdf.to_file(f'network\output\{filename}.gpkg', driver='GPKG')


def combine_netelement(gdf):
    """combines the linestring elements in a geodataframe to one entity

    Args:
        gdf (geodataframe): represents a network of a city 

    Returns:
        geodataframe: geodataframe that contains one linestring element
    """
    # Combine the entire network into one geometry
    combined_geometry = unary_union(gdf['geometry'])
    # Create a GeoDataFrame with the combined geometry
    # check isf necessary
    combined_gdf = gpd.GeoDataFrame(geometry=[combined_geometry], crs=gdf.crs)

    safe_gdf_as_gpkg(combined_gdf, "combined_network")
   
    return combined_gdf

def explode_network(gdf):


    exploded_gdf = gdf.explode(index_parts=False)

    # Reset the index to remove the 'level_1' column
    exploded_gdf = exploded_gdf.reset_index(drop=True)

    safe_gdf_as_gpkg(exploded_gdf, "exploded_network")

    return exploded_gdf

def extract_support_points(line):

    start_point = Point(line.coords[0])
    end_point = Point(line.coords[-1])

    return start_point, end_point


def create_support_points(gdf):

    # Create an empty GeoDataFrame to store support points
    #support_points_gdf = gpd.GeoDataFrame(geometry=[], crs=gdf.crs)
    # Apply the function to each geometry in the GeoDataFrame

    # Apply the function with additional variable 'existing_points'
    result_list  = gdf['geometry'].apply(extract_support_points).to_list()

    # Create a new GeoDataFrame from the result list
    points_list = [point for tuple_points in result_list for point in tuple_points]

    support_points_gdf = gpd.GeoDataFrame(geometry=points_list, crs=gdf.crs)

    # Reset the index
    support_points_gdf.reset_index(drop=True, inplace=True)
    support_points_gdf = support_points_gdf.explode(index_parts=False)

    safe_gdf_as_gpkg(support_points_gdf, "support_points")
    

    return support_points_gdf

def buffer_points(support_points_gdf):
    # Buffer the support points by 1 meters
    buffer_distance = 0.5
    print(support_points_gdf.head())
    support_points_gdf = support_points_gdf.explode(index_parts=False)

    # Create a GeoDataFrame with buffered geometries
    support_points_buffered_gdf = gpd.GeoDataFrame(
        geometry=support_points_gdf['geometry'].buffer(buffer_distance),
        crs=support_points_gdf.crs
    )
        # Reset the index to remove the 'level_1' column
    support_points_buffered_gdf.reset_index(drop=True, inplace=True)
    print(support_points_buffered_gdf.head())
    print(support_points_gdf.head())
    # Explode the GeoDataFrame to get individual support points
    safe_gdf_as_gpkg(support_points_buffered_gdf, "buffered_support_points")

    return support_points_buffered_gdf

def find_intersecting_lines(gdf_lines, gdf_buffers, support_points):
    # Create spatial index for buffered support points
    # NOTE:like a bb around the point
    spatial_index = gdf_buffers.sindex

    # creat column with number of lines that intersect with the buffered support points
    gdf_buffers['Number_of_intersections']= 0
    support_points['Number_of_intersections']= 0

    # Iterate through each line and use spatial index for intersection check
    # umdrehen!°
    for line_id, line in gdf_lines.iterrows():
        possible_matches_index = list(spatial_index.intersection(line.geometry.bounds))
        possible_matches = gdf_buffers.iloc[possible_matches_index]

        for buffer_id, buffer_point in possible_matches.iterrows():
            if line.geometry.intersects(buffer_point.geometry):
                gdf_buffers.at[buffer_id, 'Number_of_intersections'] += 1
                support_points.at[buffer_id, 'Number_of_intersections'] += 1
                #print(buffer_id,gdf_buffers.at[buffer_id, 'Number_of_intersections'])

    # Save the result, overwrite existing buffert buffered_support_points gpkg
    safe_gdf_as_gpkg(gdf_buffers, "buffered_support_points")
    safe_gdf_as_gpkg(support_points, "support_points")

    return support_points

def create_splitting_line(point, angle=45, distance=0.25):
    x, y = point.x, point.y
    angle_rad = math.radians(angle)
    
    # Calculate the coordinates for the second point based on the angle and distance
    x2 = x + distance * math.cos(angle_rad)
    y2 = y + distance * math.sin(angle_rad)
    
    # Create a LineString from the two points
    line = LineString([(x, y), (x2, y2)])
    
    return line

def split_net_with_line(gdf_support_points):

    # Apply the function to each geometry in the GeoDataFrame

    # Apply the function with additional variable 'existing_points'
    result_list  = gdf_support_points['geometry'].apply(create_splitting_line).to_list()

    split_line_gdf = gpd.GeoDataFrame(geometry=result_list, crs=gdf_support_points.crs)

    safe_gdf_as_gpkg(split_line_gdf, "split_line_gdf")         

def combined_function(test_gpkg):
        gdf = combine_netelement(test_gpkg)
        gdf_lines = explode_network(gdf)


        gdf_support_points = create_support_points(gdf_lines)
        gdf_bufferd_points = buffer_points(gdf_support_points)

        gdf_buffer = find_intersecting_lines(gdf_lines,gdf_bufferd_points, gdf_support_points)
        # filter buffer
        #load bufferd support points with number of intersection
        gdf_buffer = gdf_buffer[gdf_buffer["Number_of_intersections"] >= 3]
        print(gdf_buffer)
        split_net_with_line(gdf_support_points)


def main():
    #load existing GeoPackage with test_network from city
    test_gdf = gpd.read_file(test_package)

    support_points = combined_function(test_gdf)


if __name__ == "__main__":
    main()