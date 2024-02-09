from shapely.ops import linemerge
from shapely.geometry import LineString
import geopandas as gpd
# Create a list of LineStrings
linestrings = [LineString([(0, 0), (1, 1), (2, 0)]), LineString([(3, 0), (4, 1), (5, 0)]), LineString([(6, 0), (7, 1), (8, 0)])]

# Merge the LineStrings into a single LineString
merged_linestring = linemerge(linestrings)
merged_linestring_gdf = gpd.GeoDataFrame(geometry=[merged_linestring], crs="EPSG:31468")
merged_linestring_gdf = merged_linestring_gdf.explode()
# Print the result
print(merged_linestring_gdf)

