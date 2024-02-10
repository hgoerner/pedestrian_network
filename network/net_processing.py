import geopandas as gpd
import networkx as nx
from shapely.geometry import Point, LineString, MultiLineString
from shapely.ops import unary_union, linemerge
from config import test_package
from config import safe_interim_results
import pandas as pd
import math

print("test")

#first combine every netelement

def safe_gdf_as_gpkg(gdf, filename, interim_result: bool = True, safe = safe_interim_results): 
    if interim_result and safe:
        gdf.to_file(f'network\output\interim_result\{filename}.gpkg', driver='GPKG')
    elif not interim_result and safe:
        gdf.to_file(f'network\output\{filename}.gpkg', driver='GPKG')


def combine_netelement(gdf_osm_net):
    """combines the linestring elements in a geodataframe to one entity

    Args:
        gdf_osm_net (geodataframe): represents a network of a city 

    Returns:
        geodataframe: geodataframe that contains one linestring element
    """
    # Merge the LineStrings into a single LineString
    # Use unary_union to merge the LineStrings into a single MultiLineString
    merged_multilinestring = gdf_osm_net["geometry"].unary_union

    # Merge every LineString that can be merged
    merged_linestring = linemerge(merged_multilinestring)

    gdf_street_net = gpd.GeoDataFrame(geometry=[merged_linestring], crs=gdf_osm_net.crs)
    gdf_street_net.reset_index(drop=True, inplace=True)   
    gdf_street_net = gdf_street_net.explode(index_parts=False)

    safe_gdf_as_gpkg(gdf_street_net, "street_net")

    return gdf_street_net

def extract_support_points(line):

    start_point = Point(line.coords[0])
    end_point = Point(line.coords[-1])

    return start_point, end_point


def create_support_points(gdf):

    # extract support points as first and last point of an line
    result_list  = gdf['geometry'].apply(extract_support_points).to_list()

    # listcomprehension from tuple of points
    points_list = [point for tuple_points in result_list for point in tuple_points]

    # Create a new GeoDataFrame from the result list
    support_points_gdf = gpd.GeoDataFrame(geometry=points_list, crs=gdf.crs)

    # Reset the index
    support_points_gdf.reset_index(drop=True, inplace=True)   
    support_points_gdf = support_points_gdf.explode(index_parts=False)

    safe_gdf_as_gpkg(support_points_gdf, "support_points")  

    return support_points_gdf

def buffer_points(support_points_gdf):
    # Buffer the support points by 0.5 meters (good measure to find intersections)
    buffer_distance = 0.5
    support_points_gdf = support_points_gdf.explode(index_parts=False)

    # Create a GeoDataFrame with buffered geometries
    support_points_buffered_gdf = gpd.GeoDataFrame(
        geometry=support_points_gdf['geometry'].buffer(buffer_distance),
        crs=support_points_gdf.crs
    )
    # Reset the index to remove the 'level_1' column
    support_points_buffered_gdf.reset_index(drop=True, inplace=True)

    # safe the geodataframe
    safe_gdf_as_gpkg(support_points_buffered_gdf, "buffered_support_points")

    return support_points_buffered_gdf

def find_intersecting_lines(gdf_lines, gdf_buffers, gdf_support_points):
    # Create spatial index for buffered support points
    # NOTE:like a boundingbox around the point
    spatial_index = gdf_buffers.sindex

    # creat column with number of lines that intersect with the buffered support points
    gdf_buffers['Number_of_intersections']= 0
    gdf_support_points['Number_of_intersections']= 0

    # Iterate through each line and use spatial index for intersection check
    for line_id, line in gdf_lines.iterrows():
        possible_matches_index = list(spatial_index.intersection(line.geometry.bounds))
        possible_matches = gdf_buffers.iloc[possible_matches_index]

        for buffer_id, buffer_point in possible_matches.iterrows():
            if line.geometry.intersects(buffer_point.geometry):
                gdf_buffers.at[buffer_id, 'Number_of_intersections'] += 1
                gdf_support_points.at[buffer_id, 'Number_of_intersections'] += 1
                #print(buffer_id,gdf_buffers.at[buffer_id, 'Number_of_intersections'])

    # Save the result, overwrite existing buffert buffered_support_points gpkg
    # filter geodataframe (more than 3 intersections with lines is considered as trafficintersection)
    gdf_support_points_intersections = gdf_support_points[gdf_support_points["Number_of_intersections"] >= 3]
                
    safe_gdf_as_gpkg(gdf_support_points_intersections, "node_points")
    safe_gdf_as_gpkg(gdf_buffers, "buffered_support_points")
    safe_gdf_as_gpkg(gdf_support_points, "support_points")

    return gdf_support_points

def create_splitting_line(point, angle=45, distance=0.25):
    # not necessary
    x, y = point.x, point.y
    angle_rad = math.radians(angle)
    
    # Calculate the coordinates for the second point based on the angle and distance
    x2 = x + distance * math.cos(angle_rad)
    y2 = y + distance * math.sin(angle_rad)
    
    # Create a LineString from the two points
    line = LineString([(x, y), (x2, y2)])
    
    return line

def create_split_lines_gdf(gdf_support_points):
    # create line at intersection to split net (not necessary anymore)

    # filter geodataframe (more than 3 intersections with lines is considered as trafficintersection)
    gdf_support_points_intersections = gdf_support_points[gdf_support_points["Number_of_intersections"] >= 3]
    #create line out of the support points

    #not necessary
    result_list  = gdf_support_points_intersections['geometry'].apply(create_splitting_line).to_list()

    # create geodataframe with split line
    split_line_gdf = gpd.GeoDataFrame(geometry=result_list, crs=gdf_support_points.crs)
    
    safe_gdf_as_gpkg(split_line_gdf, "split_line_gdf")


def combined_function(test_gpkg):
        # combine downloaded osm net
        gdf_street_net = combine_netelement(test_gpkg)
        # explode the lines at each breaking point
        #gdf_lines = explode_network(gdf_combined_net)

        #create gdf with support points
        gdf_support_points = create_support_points(gdf_street_net)
        
        #buffer support points
        gdf_bufferd_points = buffer_points(gdf_support_points)

        #count intersecting lines in buffered points and write to support point with same ID  
        find_intersecting_lines(gdf_street_net,gdf_bufferd_points, gdf_support_points)

        # create gdf with line to split net with
        #split_line_gdf = create_split_lines_gdf(gdf_support_points)

        #split_streets_gdf = recursive_split_multilinestring(gdf_combined_net,split_line_gdf)

def main():
    #load existing GeoPackage with test_network from city
    test_gdf = gpd.read_file(test_package)

    support_points = combined_function(test_gdf)


if __name__ == "__main__":
    main()