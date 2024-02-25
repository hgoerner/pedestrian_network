from utils.config_loader import config_data
from utils.load_data import zensus_dataframe
from utils.save_data import safe_gdf_as_gpkg
import geopandas as gpd
from shapely.geometry import Point


print(zensus_dataframe.head())

# Assuming df is your DataFrame
geometry = [Point(xy) for xy in zip(zensus_dataframe['x_mp_100m'], zensus_dataframe['y_mp_100m'])]

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(zensus_dataframe, geometry=geometry, crs=config_data["zensus_crs"]).to_crs("EPSG:31468")

print(gdf.head())

safe_gdf_as_gpkg((gdf, "zensus_data"))