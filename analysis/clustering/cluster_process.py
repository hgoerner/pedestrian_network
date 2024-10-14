import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, set_link_color_palette
import matplotlib.pyplot as plt
import os
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.cluster import AgglomerativeClustering, KMeans
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def create_dataframe_with_all_zaehlstellen(folderpath):
    dataframe_dict = {}
    all_data = []
    for filename in os.listdir(folderpath):
        
        if filename.endswith('.csv'):
            filepath = os.path.join(folderpath, filename)
            df_ped = pd.read_csv(filepath, usecols=['gleitender_Stundenwert_aus_MW']) 
            #df_ped = pd.read_csv(filepath, usecols=['gleitender_MW_15min']) 
            #print(df_ped)
            df_ped = df_ped.iloc[24:88]  # von 6 bis 22 Uhr
            
            base_filename = os.path.splitext(os.path.basename(filepath))[0]
            base_filename = base_filename.split('_')[0]
            all_data.append(base_filename)

            # Concatenate all dataframes vertically or horizontally depending on your requirement
            dataframe_dict[base_filename] = df_ped
            #print(len(dataframe_dict))
            
    return dataframe_dict

def plot_elbow_method(data, max_clusters):
    wcss = []
    range_n_clusters = range(1, max_clusters + 1)
    for n_clusters in range_n_clusters:
        kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
        kmeans.fit(data.T)
        wcss.append(kmeans.inertia_)

    plt.figure(figsize=(10, 6))
    plt.title('Elbow Method For Optimal k')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.grid(True)

    # Plot all points
    plt.plot(range_n_clusters, wcss, marker='o', linestyle='-', color='b')

    # Overlay the segment from 5 to 10 with a red line
    if max_clusters >= 10:
        plt.plot(range(4, 6), wcss[3:5], 'r-o')  # Adjust the slicing to include exactly 6 elements

    plt.show()

def plot_silhouette(combined_df, n_clusters_list, title=None ):
    # Determine the number of subplots needed
    num_plots = len(n_clusters_list)
    #print(num_plots)
    # Create a figure with a specific size, adjusting based on the number of subplots
    fig, axes = plt.subplots(2, 5, figsize=(18, 12))  # Adjust figsize as needed
    axes = axes.flatten()  # Flatten the 2D array of axes to iterate easily
    
    
    if num_plots == 1:
        axes = [axes]  # Make sure axes is iterable if there's only one plot
    print(title)
    for ax, n_clusters in zip(axes, n_clusters_list):
        # Perform clustering
        clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
        cluster_labels = clustering.fit_predict(combined_df.T)

        # Print the cluster labels for each data point (column in your case)
        clustered_features = pd.DataFrame({'Feature': combined_df.columns, 'Cluster': cluster_labels})
        print(f"\nCluster labels for {n_clusters} clusters:\n", clustered_features)

        # Calculate silhouette score
        silhouette_avg = silhouette_score(combined_df.T, cluster_labels)
        #print(f'Silhouette Score for {n_clusters} clusters: {silhouette_avg}')

        # Plot silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(combined_df.T, cluster_labels)

        y_lower = 10

        for i in range(n_clusters):
            #print(i, n_clusters, cluster_labels)
            ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
            
            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = sns.color_palette("Set3")[i]
            ax.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, 
                             facecolor=color, edgecolor=color, alpha=0.7)
            ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i), fontsize=12, verticalalignment='center')

            y_lower = y_upper + 10  # 10 for the 0 samples

        ax.axvline(x=silhouette_avg, color="red", linestyle="--")
        ax.set_title(f"{n_clusters} Cluster")
        ax.set_xlabel("Silhouettenkoeffizent")
        ax.set_ylabel("Cluster")
        ax.set_yticks([])
        ax.set_xticks(np.arange(-0.1, 1.1, 0.1))
    
    
        # Remove any unused axes (if n_clusters_list has less than 6 items)
    for i in range(len(n_clusters_list), len(axes)):
        fig.delaxes(axes[i])

    plt.suptitle("Silhouetten-Score - Clusteranzahl")
    plt.tight_layout()
    plt.show()

def plot_dendrogramm_single_linkage(combined_df, undertitle=None):
    linked = linkage(combined_df.T, method='single')
    plt.figure(figsize=(10, 7))
    dendrogram(linked,
               labels=combined_df.columns,
               orientation='top',
               distance_sort='descending',
               show_leaf_counts=True)
    plt.title('Dendrogram der Zählstellen\n Typiserung Single-linkage', fontsize=18, pad=20)
    plt.xlabel('Zählstelle', fontsize=16, labelpad=10)
    plt.ylabel('euklidische Distanz', fontsize=16, labelpad=15)
    plt.show()   


    
def plot_dendrogramm_ward(combined_df, undertitle=None, color_threshold=0.2):
    linked = linkage(combined_df.T, method='ward')

    # Plot the dendrogram
    plt.figure(figsize=(12, 6))

    set_link_color_palette(["r", "b","g", "m"])
    
    dendrogram(linked, labels=combined_df.columns, orientation='top', distance_sort='descending', show_leaf_counts=True, color_threshold=color_threshold,above_threshold_color='tab:grey' )
    plt.title('Dendrogram der Zählstellen\n Typiserung Ward-Methode', fontsize=18)
    plt.xlabel('Zählstelle',fontsize=16, labelpad=15)
    plt.ylabel('Varianzzuwachs',fontsize=16, labelpad=15)
    plt.show()    
    
    
def hist_boxplot(combined_df, ncols=5):
    nplots = combined_df.shape[1]
    nrows = (nplots // ncols) + (nplots % ncols > 0)  # Calculate required rows
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols*3, nrows*3))  # Adjust figure size as needed
    axes = axes.flatten()  # Flatten the 2D array of axes
    
    # Plot histograms
    for i, ax in enumerate(axes):
        if i < nplots:
            ax.hist(combined_df.iloc[:, i], bins=20)
            ax.set_title(combined_df.columns[i])
        else:
            ax.set_visible(False)  # Hide unused axes
    plt.xlabel('Value Range')  # Label for the x-axis
    plt.ylabel('Frequency')    # Label for the y-axis
    plt.tight_layout(pad=4.0)
    plt.show()
    
    # Boxplot to see the distribution ranges
    combined_df.boxplot(figsize=(12, 6))
    plt.xticks(rotation=90)  # Rotate x labels for better readability
    plt.show()
    

def main():
    # ohne außreiser
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\01_Zählstellenseiten_Korrelation\01_Zählstellen_Seiten_zusammengefasst\unskaliert\mit_außreiser'
    
    # mit ausreißer
    #folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\01_Zählstellenseiten_Korrelation\01_Zählstellen_Seiten_zusammengefasst\unskaliert\mit_außreiser'
    dataframe_dict = create_dataframe_with_all_zaehlstellen(folderpath)
    
    # Combine all dataframes into one
    combined_df = pd.concat(dataframe_dict.values(), axis=1)  
    combined_df.columns = dataframe_dict.keys()  # Set the column names to subfolder names
    
    #standadize dataframe
    # Assuming combined_df is your dataset
    scaler = StandardScaler()
    scaled_array = scaler.fit_transform(combined_df)

    #hist_boxplot(combined_df)
    
    # Perform hierarchical clustering
    # Transpose the DataFrame: combined_df.T transposes the DataFrame, swapping rows and columns.
    # This is necessary because clustering algorithms typically expect samples
    # (e.g., zaehlstellen) as rows and features (e.g., time intervals or measurements) as columns.

    #print(combined_df)
    #print(scaled_array)
    
    # Convert the scaled array back to a DataFrame for easier handling
    scaled_df = pd.DataFrame(scaled_array, index=combined_df.index, columns=combined_df.columns)
    #hist_boxplot(scaled_df)
    
    #merging process of clusters
    #plot_dendrogramm_ward(combined_df, "ohne Ausreißer")
    plot_dendrogramm_single_linkage(combined_df)
    
    #merging process of clusters
    #plot_dendrogramm_ward(scaled_df, "ohne Ausreißer und standardisiert", 5.5)
    #plot_dendrogramm_single_linkage(scaled_df, "ohne Ausreißer und standardisiert")
    
    
    n_clusters_list = [3,4,5,6,7,8,9,10]

    #plot_silhouette(scaled_df, n_clusters_list, "ohne Ausreißer" )
    
    #plot_silhouette(scaled_df, n_clusters_list, "mit Ausreißer standardisiert" )   
    #plot_elbow_method(scaled_df, 25)  # Now considering up to 32 clusters
    
    # Statistiken vor der Standardisierung
    # print("Vor der Standardisierung:")
    # print("Mittelwerte:\n", combined_df.mean())
    # print("Standardabweichungen:\n", combined_df.std())

    # # Standardisierung der Daten
    # scaler = StandardScaler()
    # data_standardized = pd.DataFrame(scaler.fit_transform(combined_df), columns=combined_df.columns)

    # # Statistiken nach der Standardisierung
    # print("\nNach der Standardisierung:")
    # print("Mittelwerte:\n", data_standardized.mean())
    # print("Standardabweichungen:\n", data_standardized.std())
    
    
    #nachtstunden 
      
    # "gleitender_Stundenwert_aus_MW" mit außreiser
    # Silhouette Score for 3 clusters: 0.11240545225800143
    # Silhouette Score for 4 clusters: 0.11922795316792732
    # Silhouette Score for 5 clusters: 0.13854697088133675
    # Silhouette Score for 6 clusters: 0.14717448341746922
    # Silhouette Score for 7 clusters: 0.15048709247662828
    # Silhouette Score for 8 clusters: 0.15515118603678568
    # Silhouette Score for 9 clusters: 0.12572826241966076
    # Silhouette Score for 10 clusters: 0.12495944708714773
    
    # "gleitender_Stundenwert_aus_MW" mit außreiser standardisiert 
    # Silhouette Score for 3 clusters: 0.17300796085607695
    # Silhouette Score for 4 clusters: 0.17369951660724414 Vorauswahl
    # Silhouette Score for 5 clusters: 0.11033745293748354
    # Silhouette Score for 6 clusters: 0.12547802825472543
    # Silhouette Score for 7 clusters: 0.12591295308856365
    # Silhouette Score for 8 clusters: 0.13223220089307808
    # Silhouette Score for 9 clusters: 0.14007617673064093
    # Silhouette Score for 10 clusters: 0.15573335896422752
    
    # "gleitender_Stundenwert_aus_MW" ohne außreiser
    # Silhouette Score for 3 clusters: 0.164106644497806
    # Silhouette Score for 4 clusters: 0.17873007059765378 <-Auswahl
    # Silhouette Score for 5 clusters: 0.1500075939312791
    # Silhouette Score for 6 clusters: 0.14775480160065935
    # Silhouette Score for 7 clusters: 0.14236542113322068
    # Silhouette Score for 8 clusters: 0.14340970580310589
    # Silhouette Score for 9 clusters: 0.1286488324142896
    # Silhouette Score for 10 clusters: 0.1156868011522335   
 
    # "gleitender_Stundenwert_aus_MW" ohne außreiser standardisiert
    # Silhouette Score for 3 clusters: 0.1475907435948964
    # Silhouette Score for 4 clusters: 0.150091242566622 <-
    # Silhouette Score for 5 clusters: 0.13729231069554507
    # Silhouette Score for 6 clusters: 0.146930690170238
    # Silhouette Score for 7 clusters: 0.15431918130786662
    # Silhouette Score for 8 clusters: 0.15863335064106635 
    # Silhouette Score for 9 clusters: 0.15880102860519063
    # Silhouette Score for 10 clusters: 0.1465963758577142
    
    #consider 10 clusters minimizing within-cluster variance is your main goal.
    #If you prioritize well-defined, distinct clusters, then 4 clusters, which have the highest silhouette score, might be optimal.  

    #multinomiale_regression()

# Entry point of the scrip
if __name__ == "__main__":
    main()

