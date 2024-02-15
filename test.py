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

# Save the map as an HTML file
m.save("simple_map.html")
