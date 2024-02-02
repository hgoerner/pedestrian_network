import geopandas as gpd
import networkx as nx
from shapely.geometry import Point
from shapely.ops import unary_union
from config import test_package
from config import safe_interim_results



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
    safe_gdf_as_gpkg(gdf, "combined_network")
   
    return combined_gdf

def explode_network(gdf):

    exploded_gdf = gdf.explode()

    safe_gdf_as_gpkg(exploded_gdf, "exploded_network")
    print(exploded_gdf)
    return exploded_gdf

def extract_support_points(line):
    # Function to extract support points from a LineString
    return [Point(coord) for coord in line.coords]

def create_support_points(gdf):

    # Create an empty GeoDataFrame to store support points
    support_points_gdf = gpd.GeoDataFrame(geometry=[], crs=gdf.crs)
    # Apply the function to each geometry in the GeoDataFrame
    support_points_gdf['geometry'] = gdf['geometry'].apply(extract_support_points)

    # Explode the GeoDataFrame to get individual support points
    support_points_gdf = support_points_gdf.explode()

    # Reset index for the GeoDataFrame
    support_points_gdf.reset_index(drop=True, inplace=True)   

    safe_gdf_as_gpkg(support_points_gdf, "support_points")
    

    return support_points_gdf

def buffer_points(support_points_gdf):
    # Buffer the support points by 0.5 meters
    buffer_distance = 100
    support_points_gdf = support_points_gdf.explode()
    support_points_buffered_gdf = support_points_gdf['geometry'].buffer(buffer_distance)
    # Explode the GeoDataFrame to get individual support points
    safe_gdf_as_gpkg(support_points_buffered_gdf, "buffered_support_points")


def combined_function(test_gpkg):
        gdf = combine_netelement(test_gpkg)
        gdf = explode_network(gdf)
        gdf = create_support_points(gdf)
        gdf = buffer_points(gdf)

def main():
    #load existing GeoPackage with test_network from city
    test_gdf = gpd.read_file(test_package)

    support_points = combined_function(test_gdf)


if __name__ == "__main__":
    main()