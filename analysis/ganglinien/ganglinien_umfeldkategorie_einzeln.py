#Information 

# plot for 


import os
import pandas as pd
import matplotlib.pyplot as plt


# Constants
RICHTUNGSFEIN = False
LEGENDTITLE = "Zählstelle"
X_LABEL = "Beginn 15-min-Intervall"
Y_LABEL = "Anteil je 15-min-Intervall"


# Function to read CSV files from a folder
def read_csv_files(folder):
    """
    Reads all CSV files in the specified folder and returns a dictionary where keys are the base names of the files and values are DataFrames.

    Args:
        folder (str): The path to the folder containing CSV files.

    Returns:
        dict: A dictionary where keys are file base names and values are DataFrames.
    """
    file_dic = {}
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder, filename)
            file_basename = os.path.splitext(filename)[0]
            df = pd.read_csv(file_path)
            file_dic[file_basename] = df
    return file_dic

def read_excel(file_path, sheet_name: str):
    """
    Reads an Excel file and returns a DataFrame.
    """
    srv_df = pd.read_excel(file_path, sheet_name=sheet_name, header=2)
    srv_df.drop(srv_df.tail(1).index, inplace=True)
    
    srv_df['Start gerundet'] = pd.to_datetime(srv_df['Start gerundet'], format='%H:%M:%S').dt.time
    
    srv_df.sort_values(by=['Start gerundet'], inplace=True)
    srv_df.reset_index(drop=True, inplace=True)
    return srv_df


def plot_data(file_dic, folderpath, title, subtitle): 
    """
    Plots the data from the provided file dictionary.

    Args:
        file_dic (dict): A dictionary containing the CSV files, where the keys are the filenames and the values are the corresponding pandas DataFrames.
        folderpath (str): The path to the folder where the plot will be saved.
        title (str): The title of the plot.
        subtitle (str): The subtitle of the plot.

    Returns:
        list: A list of DataFrames, each containing the count_anteilig for each file.
    """
    plot_title = f"{title}\n{subtitle}"
    plotfilename = title+"_"+subtitle
    list_of_columns = []
    
    plt.figure(figsize=(12, 6))
    ax = plt.gca()
    
    for filename, df in file_dic.items():
        # Extract filename without extension
        base_filename = os.path.splitext(filename)[0]
        
        # Convert 'start time' to datetime and extract the time component
        df['start time(ohne Tag)'] = pd.to_datetime(df['start time'], format='ISO8601').dt.strftime('%H:%M')
        
        # Filter to only include pedestrians
        df = df[df['classification'] == 'pedestrian'].copy()
        
        # Calculate the proportion of counts
        total_count = df["count"].sum()
        df["count_anteilig"] = df["count"] / total_count
        
        # Group by 'start time(ohne Tag)' and sum the 'count_anteilig'
        df_grouped = df.groupby('start time(ohne Tag)')['count_anteilig'].sum().reset_index()
        df_grouped.sort_values(by='start time(ohne Tag)', inplace=True)
        
        # Calculate rolling mean with window size of 4
        df_grouped['gleitender_Mittelwert'] = df_grouped['count_anteilig'].rolling(window=4, min_periods=1).mean()
        
        # Manually adjust the first three values of 'gleitender_Mittelwert'
        if len(df_grouped) >= 4:
            df_grouped.at[0, 'gleitender_Mittelwert'] = (df_grouped['count_anteilig'][-3:].sum() + df_grouped['count_anteilig'][:2].sum()) / 4
            df_grouped.at[1, 'gleitender_Mittelwert'] = (df_grouped['count_anteilig'][-2:].sum() + df_grouped['count_anteilig'][:3].sum()) / 4
            df_grouped.at[2, 'gleitender_Mittelwert'] = (df_grouped['count_anteilig'][-1:].sum() + df_grouped['count_anteilig'][:4].sum()) / 4
        
        # Plot the rolling mean
        ax.plot(df_grouped['start time(ohne Tag)'], df_grouped['gleitender_Mittelwert'], label=f"{base_filename} n={total_count}")
        
        # Store the count_anteilig column in the list
        df_grouped[base_filename] = df_grouped['count_anteilig']
        list_of_columns.append(df_grouped[base_filename])
    
    # Set x-axis labels
    ax.set_xticks(range(len(df_grouped['start time(ohne Tag)'])))
    ax.set_xticklabels(df_grouped['start time(ohne Tag)'], rotation=90)
    
    # Set plot details
    ax.set_xlim(-0.5, len(df_grouped['start time(ohne Tag)']) - 0.5)
    plt.title(plot_title, fontsize=14)
    plt.xlabel(X_LABEL, fontsize=14)
    plt.ylabel(Y_LABEL, fontsize=14)
    
    plt.yticks(fontsize=10)
    plt.xticks(fontsize=10)
    plt.grid(True, alpha=0.5)
    plt.legend(title=LEGENDTITLE, fontsize=10)
    #plt.xlim(df_total['start time(ohne Tag)'].min(), df_total['start time(ohne Tag)'].max())
    plt.tight_layout() 
    #plt.show()
    
    # Save the plot
    plot_path = os.path.join(folderpath, plotfilename+".png")
    plt.savefig(plot_path, dpi=100)
    plt.close()
   

# Main function
def main():  
     
    # SrV-Data

    # Specify the directory path
    directory_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\Umfeld_Kategorie"  

    # List only directories
    folders = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]

    unfeldkategorien = ["PH_EH", "PH_EN", "PN_EH", "PN_EN",]

    for folder, unfeldkategorien in zip(folders,unfeldkategorien ):
        file_dic = read_csv_files(folder)
        # Plot data
        plot_data(file_dic,folder, title="Anteil Fußverkehr je Zeitscheibe", subtitle=unfeldkategorien)
        
        #combined_df = pd.concat(list_of_columns, axis=1)

        #combined_df.to_csv(folders)


# Entry point of the script
if __name__ == "__main__":
    main()
