import folium

# Create a Folium map centered on a specific location
map_center = [37.7749, -122.4194]  # Example coordinates for San Francisco, CA
m = folium.Map(location=map_center, zoom_start=12)

# Add a marker to the map
folium.Marker(
    location=[37.7749, -122.4194],
    popup="Hello, Folium!",
    icon=folium.Icon(color='blue')
).add_to(m)

<<<<<<< HEAD
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
=======
# Save the map as an HTML file
m.save("simple_map.html")
>>>>>>> 840e115a4d0120048247be77784be4ff31759d39
