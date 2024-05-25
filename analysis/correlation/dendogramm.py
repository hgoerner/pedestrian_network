import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from dtaidistance import dtw

# Generate synthetic traffic volume data
np.random.seed(0)
base_traffic = np.concatenate([np.random.poisson(20, 32), np.random.poisson(100, 16), np.random.poisson(50, 32), np.random.poisson(10, 16)])
data = np.array([base_traffic + np.random.normal(0, 10, 96) for _ in range(10)])

# Calculate DTW distances
dist_matrix = dtw.distance_matrix_fast(data)

# Perform hierarchical clustering using the complete linkage method
Z = linkage(dist_matrix, method='complete')

# Plot the dendrogram
plt.figure(figsize=(10, 8))
dendrogram(Z)
plt.title('Dendrogram of Traffic Volume Patterns')
plt.xlabel('Day Index')
plt.ylabel('DTW Distance')
plt.show()