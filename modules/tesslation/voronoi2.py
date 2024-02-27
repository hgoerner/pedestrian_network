import geopandas as gpd
from shapely.geometry import Point
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import Voronoi, voronoi_plot_2d

# Laden Sie den GeoDataFrame aus dem Geopackage
gdf = gpd.read_file('data\output\osm_pois_updated_Dresden.gpkg')

# Extrahieren Sie die Koordinaten aus dem GeoDataFrame
city_points = np.array(gdf.geometry.apply(lambda point: (point.x, point.y)).tolist())

# Perform clustering (e.g., k-means)
k = 25  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=0)
gdf['cluster'] = kmeans.fit_predict(city_points)

# Find cluster centers
cluster_centers = gdf.groupby('cluster').geometry.apply(lambda x: x.iloc[0]).to_numpy()

# Scale the cluster centers by a factor (e.g., 100)
scaling_factor = 10
scaled_cluster_centers = np.array([(point.x, point.y) for point in cluster_centers]) * scaling_factor

# Berechnen Sie das Voronoi-Diagramm mit den skalierten Cluster-Centers
vor = Voronoi(scaled_cluster_centers)

# Zeichnen Sie das Voronoi-Diagramm auf einer Karte
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='gray', line_width=2, line_alpha=0.6)

# Zeichnen Sie die Stadtgrenzen aus dem GeoDataFrame
gdf.boundary.plot(ax=ax, color='blue', linewidth=2)

# Plot the original shop and restaurant locations with color-coded clusters
gdf.plot(ax=ax, column='cluster', cmap='viridis', markersize=20, legend=True, alpha=0.8)

# Legende hinzufügen
ax.legend(['Voronoi Diagram', 'City Boundary', 'Clusters'])

# Zeigen Sie das Diagramm an
plt.show()