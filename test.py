from shapely.geometry import MultiPoint

# Set of points
points = [(0, 0), (1, 2), (3, 1), (4, 3)]

# Create a MultiPoint geometry
multi_point = MultiPoint(points)

# Calculate the convex hull
convex_hull = multi_point.convex_hull

# Print the coordinates of the convex hull
print(convex_hull.exterior.coords.xy)