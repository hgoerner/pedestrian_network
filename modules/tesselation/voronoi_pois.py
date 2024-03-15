import os
import sys

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from tesspy import Tessellation
import matplotlib.pyplot as plt
from utils.save_data import safe_gdf_as_gpkg
from utils.config_loader import config_data
from utils.helper import write_params_to_textfile

plt.rcParams["figure.dpi"] = 100
plt.rcParams["figure.figsize"] = (8, 8)
import contextily as ctx
from time import sleep
import warnings

warnings.simplefilter("ignore")

#n_polygons = config_data["number_of_polygons"]
poi_categories = config_data["poi_categories"]
min_cluster_size = config_data["min_cluster_size"]

# create textfile with params
write_params_to_textfile(["poi_categories", "min_cluster_size"], "tesselation_params", "calculation of voronoi_geopackage")

# Create a tessellation object
montreal = Tessellation("Montreal, Canada")

# get polygon of the investigated area
montreal_polygon = montreal.get_polygon()
fig, ax = plt.subplots(1, 1, figsize=(10, 6))

montreal_vor_hdbscan = montreal.voronoi(
    cluster_algo="hdbscan", min_cluster_size=min_cluster_size, poi_categories="all"
)

montreal_vor_hdbscan.to_crs("EPSG:3857").plot(
    ax=ax, facecolor="none", edgecolor="k", lw=0.5
)


print(type(montreal_vor_hdbscan))
ctx.add_basemap(ax=ax, source=ctx.providers.CartoDB.Voyager)

#axs[0].set_title("Voronoi Tessellation: All POI Categories", fontsize=15)
ax.set_title(f"Clustering Algorithm: HDBSCAN")


plt.tight_layout()
plt.show()

# convert to gausskrueger ==> helps for later calculation
montreal_vor_hdbscan = montreal_vor_hdbscan.to_crs("EPSG:31468")
safe_gdf_as_gpkg((montreal_vor_hdbscan, "montreal_voronoi" ))

print(montreal_vor_hdbscan.crs)