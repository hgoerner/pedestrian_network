from sklearn.cluster import DBSCAN
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt


points_gdf = gpd.read_file(r"output\osm_pois_dresden_updated.gpkg")
print(points_gdf)

# Replace with your actual point data
points_array = np.array(
    list(zip(points_gdf.geometry.x, points_gdf.geometry.y)))

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.1, min_samples=5)
points_gdf['cluster'] = dbscan.fit_predict(points_array)

# Plot the clusters
fig, ax = plt.subplots(figsize=(10, 10))
points_gdf.plot(column='cluster', cmap='viridis', legend=True, ax=ax)
plt.show()
