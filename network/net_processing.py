import geopandas as gpd
import networkx as nx
from shapely.geometry import LineString, Point, MultiPolygon
from shapely.ops import unary_union


gdf = gpd.read_file(r'C:\Users\Goerner\Desktop\pedestrian_network\network\output\dresden_netz.gpkg')
# Combine the entire network into one geometry
combined_geometry = unary_union(gdf['geometry'])

# Create a GeoDataFrame with the combined geometry
combined_gdf = gpd.GeoDataFrame(geometry=[combined_geometry], crs=gdf.crs)
print(combined_gdf)
# Save the combined GeoDataFrame to a new GeoPackage
combined_gdf.to_file('network\output\combined_network.gpkg', driver='GPKG')

# Now, explode the combined geometry into individual edges
exploded_gdf = combined_gdf.explode()

# Save the exploded GeoDataFrame to a new GeoPackage
exploded_gdf.to_file('network\output\exploded_network.gpkg', driver='GPKG')

# Function to extract support points from a LineString
def extract_support_points(line):
    return [Point(coord) for coord in line.coords]
# Load GeoPackage with the segmented network
gdf = gpd.read_file('network\output\exploded_network.gpkg')

# Create an empty GeoDataFrame to store support points
support_points_gdf = gpd.GeoDataFrame(geometry=[], crs=gdf.crs)

# Apply the function to each geometry in the GeoDataFrame
support_points_gdf['geometry'] = gdf['geometry'].apply(extract_support_points)


# Explode the GeoDataFrame to get individual support points
support_points_gdf = support_points_gdf.explode()

# Reset index for the GeoDataFrame
#support_points_gdf.reset_index(drop=True, inplace=True)
print(support_points_gdf)
# Save the resulting GeoDataFrame to a new GeoPackage
support_points_gdf.to_file('network\output\support_points.gpkg', driver='GPKG')

# Buffer the support points by 0.5 meters
buffer_distance = 100
support_points_buffered_gdf = support_points_gdf['geometry'].buffer(buffer_distance)
print(support_points_buffered_gdf)

# # Save the resulting GeoDataFrame to a new GeoPackage
support_points_buffered_gdf.to_file('network\output\support_points_buffered.gpkg', driver='GPKG')