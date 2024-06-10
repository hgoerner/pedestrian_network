import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from ganglinien import return_and_process_dataframes





def main():
    
    folderpath =r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\Alle_Zählstellen"
    list_of_dataframes, basename = return_and_process_dataframes(folderpath)
    
    for df in list_of_dataframes:
        df.set_index("start time(ohne Tag)", inplace=True)
    print(list_of_dataframes)
    df1 = list_of_dataframes[0]
        
    list_of_dataframes = [df.reindex(df1.index) for df in list_of_dataframes]
    
    # Interpolate missing values in each DataFrame
    for df in list_of_dataframes:
        df.interpolate(method='linear', inplace=True)
       
    print(len(list_of_dataframes))
    print(len(basename))
        
    # Create a dictionary to map the original index to cluster labels
    index_to_cluster = {i: f"{i} : {label}" for i, label in enumerate(basename)}
    
    data = [df['gleitender_Mittelwert'].values for df in list_of_dataframes]  # Erstellen einer Liste von Arrays
    data = np.array(data)  # Konvertierung in ein Numpy-Array
    
    # Distanzmatrix berechnen (hier einfache euklidische Distanz)
    dist_matrix = squareform(pdist(data, metric='euclidean'))
    # Hierarchisches Clustering durchführen
    Z = linkage(dist_matrix, 'ward')
    print(Z)
    # Dendrogramm zeichnen
    plt.figure(figsize=(10, 7))
    plt.title('Dendrogramm der DataFrames')
    dendrogram(Z, labels=[index_to_cluster[i] for i in range(len(basename))], orientation="right", color_threshold=0.1)
    plt.show()
    
# Entry point of the script
if __name__ == "__main__":
    main()