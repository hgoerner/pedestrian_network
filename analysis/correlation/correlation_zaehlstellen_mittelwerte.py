import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def create_list_of_mittelwert_dataframes(folderpath, subfolder_split_icon="_"):

    # Dictionary to store dataframes with their subfolder names as keys
    dataframe_dict = {}
    for subfolder in os.listdir(folderpath):
        subfolder_path = os.path.join(folderpath, subfolder)

        if os.path.isdir(subfolder_path):
            #color_map[subfolder] = colors[i % len(colors)]
            if subfolder_split_icon:
                legend_name = subfolder.split(subfolder_split_icon)[-1]
            else:
                print("abort")
                
            # Create an empty list to store data from each CSV in the current subfolder
            all_data = []
            # Loop through each CSV file in the subfolder
            for csv_file in os.listdir(subfolder_path):
                

                if csv_file.endswith('.csv'):
                    csv_file_path = os.path.join(subfolder_path, csv_file)
                    
                    # Read the CSV file 
                    df_mittelwerte_tag = pd.read_csv(csv_file_path, usecols=['gleitender_Stundenwert_aus_MW'])
                    #df_mittelwerte_tag = pd.read_csv(csv_file_path, usecols=['gleitender_MW_15min'])
                    # Append the data to the list
                    df_mittelwerte_tag = df_mittelwerte_tag.iloc[24:88] # 6 bis 22 Uhr

                    all_data.append(df_mittelwerte_tag)
                    
            # Concatenate all dataframes vertically or horizontally depending on your requirement
            if all_data:
                combined_df = pd.concat(all_data, axis=1)  # Change axis=1 for horizontal concatenation if needed
                dataframe_dict[legend_name] = combined_df
            
    return dataframe_dict

def plot_correlation_matrix(corr_matrix, plottitle=None):
    #Rename the first row index name and the first column name to " "
    corr_matrix.index = [" "] + corr_matrix.index.tolist()[1:]
    corr_matrix.columns = corr_matrix.columns.tolist()[:-1] + [" "]
    
    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    # Set up the matplotlib figure
    plt.figure(figsize=(14, 14))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', mask=mask,
                    linewidths=0.5, vmin=-1, vmax=1,
                    cbar_kws={"shrink": 0.5, "ticks": np.linspace(-1, 1, 11)},
                    annot_kws={"size": 14})
    plt.title(plottitle, fontsize=20)
    plt.xticks(rotation=45, ha="right", fontsize=16,)
    plt.yticks(fontsize=16, rotation=0)
    
    # Explicitly hide the first and last ticks
    ax.xaxis.set_tick_params(which='both', width=0)  # Hide x-axis ticks
    ax.yaxis.set_tick_params(which='both', width=0)  # Hide y-axis ticks
    for label in ax.get_xticklabels():
        if label.get_text() == " ":
            label.set_visible(False)
    for label in ax.get_yticklabels():
        if label.get_text() == " ":
            label.set_visible(False)
    plt.tight_layout()  # Adjust layout to make room for labels

    # Adjust the color bar to be on the right side
    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.set_ticks_position('right')
    cbar.ax.yaxis.set_label_position('right')

    # Further adjust the plot to accommodate the rotated y-ticks if needed
    plt.subplots_adjust(top=0.92, bottom=0.3, right=0.85, left=0.15)
    plt.show()   
    

def main():
    
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\03_RegioStarGem7_Typen_Mittelwerte'
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\06_Umfeld_Kategorie_Mittelwerte'
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\08_Lage_im_Stadtgebiet_Mittelwerte'
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\09_Distanz_OPNV\Entfernung_Bushaltestelle\Quartile\Stundenmittelwerte'
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\09_Distanz_OPNV\Entfernung_SPNV_Haltestelle\Quartile\Stundenmittelwerte'
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\09_Distanz_OPNV\Entferrnung_Straßenbahnhaltestelle\Quartile\Stundenmittelwerte'
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\09_2Infrastrukturmerkmale\EntfernungKita\Quartile\Stundenmittelwerte'
    folderpath = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\09_2Infrastrukturmerkmale\EntfernungHochschule\Stundenmittelwerte'
    df_dict = create_list_of_mittelwert_dataframes(folderpath)
    print(df_dict)
    
    # Combine all dataframes into one
    combined_df = pd.concat(df_dict.values(), axis=1)  
    print(combined_df)
    combined_df.columns = df_dict.keys()  # Set the column names to subfolder names

    # Calculate the correlation matrix
    correlation_matrix = combined_df.corr()
    plot_correlation_matrix(correlation_matrix, "Korrelationsmatrix")


# Entry point of the scrip
if __name__ == "__main__":
    main()