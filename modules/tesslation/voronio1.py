import geopandas as gpd
from shapely.geometry import Point
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import Voronoi, voronoi_plot_2d

# Generate random shop and restaurant locations for illustration
np.random.seed(0)
num_points = 100
city_center = np.array([0, 0])
radius_inner_city = 10
radius_outer_city = 30

# Generate points in the inner city
inner_city_points = city_center + radius_inner_city * np.random.randn(num_points, 2)

# Generate points in the outskirts
outskirts_points = city_center + radius_outer_city * np.random.randn(num_points, 2)

# Combine the points for the GeoDataFrame
all_points = np.vstack([inner_city_points, outskirts_points])
geometry = [Point(xy) for xy in all_points]
gdf = gpd.GeoDataFrame(geometry=geometry, crs='EPSG:4326')

# Extract x and y coordinates from the 'Point' objects
gdf['x'] = gdf['geometry'].x
gdf['y'] = gdf['geometry'].y

# Perform clustering (e.g., k-means) on x and y coordinates
k = 20  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=0)
gdf['cluster'] = kmeans.fit_predict(gdf[['x', 'y']])

# Find cluster centers
cluster_centers = gdf.groupby('cluster')[['x', 'y']].mean().to_numpy()

# Compute the Voronoi diagram with cluster centers
vor = Voronoi(cluster_centers)

# Plot the Voronoi diagram on a map
fig, ax = plt.subplots(figsize=(10, 10))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='gray', line_width=2, line_alpha=0.6)

# Plot the original shop and restaurant locations
gdf.plot(ax=ax, column='cluster', cmap='viridis', markersize=20, legend=True, alpha=0.8)

# Set plot limits for clarity
ax.set_xlim(city_center[0] - radius_outer_city - 5, city_center[0] + radius_outer_city + 5)
ax.set_ylim(city_center[1] - radius_outer_city - 5, city_center[1] + radius_outer_city + 5)

# Legend
ax.legend(['Voronoi Diagram', 'Shops/Restaurants'])

# Show the plot
plt.show()