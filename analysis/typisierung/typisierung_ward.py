import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import fcluster
from sklearn.cluster import AgglomerativeClustering, KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

# Setze den Zufalls-Seed für Reproduzierbarkeit
np.random.seed(42)

# Anzahl der Zeitreihen und Datenpunkte
num_series = 20
num_points = 96

# Erstelle ein Array, das drei verschiedene Gruppen von Zeitreihen enthält
data = np.zeros((num_series, num_points))

# Gruppe 1
for i in range(7):
    baseline = 0.5  # Baseline-Shift für die Gruppe
    noise = np.random.normal(0, 0.1, num_points)  # Rauschen hinzufügen
    pattern = np.sin(np.linspace(0, 2 * np.pi, num_points))  # Grundmuster
    data[i] = baseline + pattern + noise

# Gruppe 2
for i in range(7, 14):
    baseline = 1.0  # Ein anderer Baseline-Shift
    noise = np.random.normal(0, 0.1, num_points)
    pattern = np.cos(np.linspace(0, 2 * np.pi, num_points))  # Ein anderes Muster
    data[i] = baseline + pattern + noise

# Gruppe 3
for i in range(14, 20):
    baseline = 1.5
    noise = np.random.normal(0, 0.1, num_points)
    pattern = np.sin(np.linspace(0, 4 * np.pi, num_points))  # Doppelte Frequenz
    data[i] = baseline + pattern + noise
    
    
# Füge kleine zufällige Störungen hinzu
noise_level = 0.05  # Stelle das Rauschlevel ein, abhängig von der Skala deiner Daten
noisy_data = data + np.random.normal(0, noise_level, data.shape)

# Führe hierarchisches Clustering durch
Z_original = linkage(data, 'ward', optimal_ordering= False)
Z_noisy = linkage(noisy_data, 'ward', optimal_ordering= False)

# Visualisiere die Dendrogramme
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
dendrogram(Z_original)
plt.title("Original Data")

plt.subplot(1, 2, 2)
dendrogram(Z_noisy)
plt.title("Noisy Data")

plt.show()



def dendrogram_to_labels(Z):
    """Hilfsfunktion zur Umwandlung von Linkage-Matrix in Cluster-Labels"""

    return fcluster(Z, t=3, criterion='distance')  # t ist die Distanzschwelle

# Berechne den Silhouetten-Score für beide Datensätze
score_original = silhouette_score(data, dendrogram_to_labels(Z_original))
score_noisy = silhouette_score(noisy_data, dendrogram_to_labels(Z_noisy))

print("Silhouetten-Score Original: ", score_original)
print("Silhouetten-Score Noisy: ", score_noisy)

# Funktion zur Berechnung der SSE für eine gegebene Anzahl von Clustern
def calculate_sse(Z, num_clusters):
    from scipy.cluster.hierarchy import fcluster
    clusters = fcluster(Z, num_clusters, criterion='maxclust')
    sse = 0
    for cluster in set(clusters):
        cluster_data = data[clusters == cluster]
        centroid = np.mean(cluster_data, axis=0)
        sse += np.sum((cluster_data - centroid) ** 2)
    return sse

# Berechne die SSE für unterschiedliche Clusteranzahlen
sse_values = [calculate_sse(Z_original, k) for k in range(1, 11)]  # Von 1 bis 10 Cluster

# Visualisiere die Änderung der SSE
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), sse_values, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')
plt.title('SSE vs. Number of Clusters')
plt.grid(True)
plt.show()

# Führe KMeans-Clustering durch
kmeans = KMeans(n_clusters=3, random_state=42).fit(data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualisiere die Cluster und Zentroide
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o', alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75)
plt.title('Cluster Visualisation with Centroids')
plt.show()

clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
clustering.fit_predict(data)
print(data)
print(clustering.labels_)

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Time vector for x-axis (24 hours in 15-minute intervals)
time_vector = np.linspace(0, 24, num_points, endpoint=False)

# Define colors for each cluster
colors = plt.cm.get_cmap('viridis', np.unique(clustering.labels_).size)

# Plot each series
for i in range(20):
    # Calculate a small offset within the cluster to prevent complete overlap
    offset = 0  # Small offset for each series in the same cluster
    y_value = clustering.labels_[i] + offset  # Assign y based on cluster label + offset
    ax.plot(time_vector, np.full(num_points, y_value), data[i])


ax.set_xlabel('Time of Day (hours)')
ax.set_ylabel('Series Index')
ax.set_zlabel('Data Value')

plt.title('3D Plot of Time Series Data')
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(data, cmap='viridis', xticklabels=24, yticklabels=True)
plt.title('Heatmap of Time Series Data')
plt.xlabel('Time of Day')
plt.ylabel('Series Index')
plt.show()


import plotly.graph_objects as go
# Color map
colors = plt.cm.get_cmap('viridis', np.unique(clustering.labels_).size)


fig = go.Figure()
for i in range(num_series):
    fig.add_trace(go.Scatter3d(x=time_vector, y=np.full(num_points, i), z=data[i],
                               mode='lines',
                               line=dict(color=colors(clustering.labels_[i]), width=2),
                               name=f'Cluster {clustering.labels_[i]}'))

fig.update_layout(scene=dict(
                    xaxis_title='Time of Day (hours)',
                    yaxis_title='Series Index',
                    zaxis_title='Data Value'),
                  title='3D Plot of Time Series Data by Cluster')
fig.show()