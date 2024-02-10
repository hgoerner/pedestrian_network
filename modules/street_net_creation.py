import geopandas as gpd

from shapely.ops import linemerge
from data.save_data import safe_gdf_as_gpkg
from utils.helper import start_end_points
from data.config_loader import config_data

print(config_data)


def create_streetnet(gdf_osm_net: gpd.GeoDataFrame):
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

    return (
        gpd.GeoDataFrame(geometry=[merged_linestring], crs=gdf_osm_net.crs)
        .reset_index(drop=True, inplace=True)
        .explode(index_parts=False)
    )

def create_support_points(gdf):

    # extract support points as first and last point of an line
    result_list  = gdf['geometry'].apply(start_end_points).to_list()

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

    return gpd.GeoDataFrame(
        geometry=support_points_gdf['geometry'].buffer(buffer_distance),
        crs=support_points_gdf.crs,
    ).reset_index(drop=True, inplace=True)

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
    gdf__intersections_points = gdf_support_points[gdf_support_points["Number_of_intersections"] >= 3]
                
    return gdf_support_points, gdf__intersections_points

def combined_function(test_gpkg):
        # combine downloaded osm net
        gdf_street_net = create_streetnet(gdf = test_gpkg)

        #create gdf with support points
        gdf_support_points = create_support_points(gdf_street_net)
        
        #buffer support points
        gdf_bufferd_points = buffer_points(gdf_support_points)

        #count intersecting lines in buffered points and write to support point with same ID  
        find_intersecting_lines(gdf_street_net,gdf_bufferd_points, gdf_support_points)

def main():
    #load existing GeoPackage with test_network from city
    test_gdf = gpd.read_file(config.test_gpkg)

    support_points = combined_function(test_gdf)


if __name__ == "__main__":
    main()