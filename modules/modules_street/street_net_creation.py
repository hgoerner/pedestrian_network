import geopandas as gpd

import sys
sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')

from shapely.ops import linemerge
from data.save_data import safe_gdf_as_gpkg
from utils.helper import start_end_points
from utils.config_loader import config_data



def optimize_street_network(gdf_osm_net: gpd.GeoDataFrame):
    """combines the linestring elements in a geodataframe to one entity

    Args:
        gdf_osm_net (geodataframe): represents a network of a city 

    Returns:
        geodataframe: geodataframe that contains one linestring element
    """

    # Use unary_union to merge the LineStrings into a single MultiLineString
    merged_multilinestring = gdf_osm_net["geometry"].unary_union
    # Merge every LineString that can be merged
    merged_linestring = linemerge(merged_multilinestring)


    street_net_gdf= gpd.GeoDataFrame(geometry=[merged_linestring], crs=gdf_osm_net.crs)
    return street_net_gdf.reset_index(drop=True).explode(index_parts=False)

def create_support_points(gdf):

    # extract support points as first and last point of an line
    result_list  = gdf['geometry'].apply(start_end_points).to_list()

    # listcomprehension from tuple of points
    points_list = [point for tuple_points in result_list for point in tuple_points]

    # Create a new GeoDataFrame from the result list
    support_points_gdf = gpd.GeoDataFrame(geometry=points_list, crs=gdf.crs)

    # Reset the index abd explode possible multipoints
    return support_points_gdf.reset_index(drop=True).explode(index_parts=False)


def buffer_points(support_points_gdf):
    support_points_gdf = support_points_gdf.explode(index_parts=False)

    buffered_points_gdf = gpd.GeoDataFrame(geometry=support_points_gdf['geometry'].buffer(0.5),crs=support_points_gdf.crs)
    buffered_points_gdf.reset_index(drop=True, inplace=True)

    return buffered_points_gdf

def find_intersecting_lines(gdf_lines, gdf_buffers, gdf_support_points):
    """
    Finds the points that represents intersections 

    Args:
        gdf_lines: A GeoDataFrame representing the lines.
        gdf_buffers: A GeoDataFrame representing the buffered support points.
        gdf_support_points: A GeoDataFrame representing the support points.

    Returns:
        A GeoDataFrame containing the support points that intersect with at least 3 lines.
    """

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

    return gdf_support_points[gdf_support_points["Number_of_intersections"] >= 3]

def create_street_net_and_intersection_gpkg(osm_street_net:gpd.GeoDataFrame):
        """
        Create a street network and intersection GeoPackage.

        Args:
            osm_street_net: GeoDataFrame containing the downloaded OSM street network.

        Returns: None
        """
        
        # combine downloaded osm net
        gdf_street_net = optimize_street_network(osm_street_net)

        #create gdf with support points
        gdf_support_points = create_support_points(gdf_street_net)
        
        #buffer support points
        gdf_bufferd_points = buffer_points(gdf_support_points)
        #count intersecting lines in buffered points and write to support point with same ID  
        gdf__intersections_points = find_intersecting_lines(gdf_street_net,gdf_bufferd_points, gdf_support_points)

        safe_gdf_as_gpkg((gdf_street_net,"street_net_"+config_data["city_name"]),(gdf__intersections_points,"node_points_"+config_data["city_name"]),(gdf_support_points,"support_points_"+config_data["city_name"],True), (gdf_bufferd_points,"buffer_points_"+config_data["city_name"],True    ))



def main():
    # function for testing
   
    test_gdf = gpd.read_file(config_data["test_package"])

    create_street_net_and_intersection_gpkg(test_gdf)


if __name__ == "__main__":
    main()