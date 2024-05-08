import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
RICHTUNGSFEIN = True
TITLE = "TITLE"
LEGENDTITLE = "Fußverkehrsaufkommen"
X_LABEL = "X-Achse"
Y_LABEL = "Y-Achse"





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


    

# Function to add random numbers for testing
def add_random_numbers(file_dic,filename):
    """
    Adds random numbers to a specific DataFrame in the file dictionary for testing purposes.

    Args:
        file_dic (dict): A dictionary containing DataFrames.
        filename (str): The key of the DataFrame to which random numbers will be added.
    """
    file_dic[filename]["count"] = np.random.randint(20, 400, size=len(file_dic[filename]))

# Function to plot data

def plot_data(file_dic, srv_df): 
    """
    Plots the data from the provided file dictionary.

    Args:
        file_dic (dict): A dictionary containing the CSV files, where the keys are the filenames and the values are the corresponding pandas DataFrames.

    Returns:
        None
    """
    _, ax = plt.subplots()
    for filename, df in file_dic.items():
        # last row 
        df['start time(ohne Tag)'] = pd.to_datetime(df['start time'], format='ISO8601').dt.time
        
        
        
        # Extract time component from datetime columns
        summed_up_count = df["count"].sum()
        df["count_anteilig"] = df["count"] / summed_up_count
        df_grouped_by_flow = df.groupby(['start time(ohne Tag)', 'flow'])['count_anteilig'].sum().reset_index()
        
        df_total = df.groupby('start time(ohne Tag)')['count_anteilig'].sum().reset_index()
        #df_total.drop(df_total.iloc[-1].name, inplace=True)
        df_total.sort_values(by=['start time(ohne Tag)'], inplace=True)
        df_total.reset_index(drop=True, inplace=True)
        print(df_total['start time(ohne Tag)'])


        ax.plot(df_total.index, df_total['count_anteilig'], linestyle='-', label=filename+"_total")
        if RICHTUNGSFEIN:
            for flow, group in df_grouped_by_flow.groupby('flow'):
                group.drop(group.iloc[-1].name, inplace=True)
                group.sort_values(by=['start time(ohne Tag)'], inplace=True)
                group.reset_index(drop=True, inplace=True)
                ax.plot(group.index, group['count_anteilig'], linestyle='-', label=f'{flow, filename}', linewidth=1.5)
                
    # Plot srv_df
    ax.plot(srv_df.index, srv_df['Summe_alle.1'], linestyle='-', label="srv_total", linewidth=1.5)
    
    ax.set_xticks(range(len(df_total['start time(ohne Tag)'])))
    ax.set_xticklabels(df_total['start time(ohne Tag)'], rotation=90)
    # Adjust the limits of the x-axis
    ax.set_xlim(-0.5, len(df_total['start time(ohne Tag)']) - 0.5)
    # Customize the x-axis ticks using a list of datetime values
    plt.title(TITLE, fontsize=14)
    plt.xlabel(X_LABEL, fontsize=12)
    plt.ylabel(Y_LABEL, fontsize=12)
    
    plt.yticks(fontsize=8)
    plt.grid(True, alpha=0.5)
    plt.legend(title=LEGENDTITLE, fontsize=10)
    #plt.xlim(df_total['start time(ohne Tag)'].min(), df_total['start time(ohne Tag)'].max())
    plt.tight_layout() 
    plt.show()

# Main function
def main():
    # Specify the folder containing CSV files
    folder = r"C:\Users\Goerner\Desktop\Hamburg_zaehlstellen"
    
    # SrV-Data
    file_path_srv_data=r"C:\Users\Goerner\Desktop\Hamburg_zaehlstellen\Ganglinien_RegioStaR_v7.xlsx"
    
    # Read CSV files into a dictionary
    file_dic = read_csv_files(folder)
    
    srv_df = read_excel(file_path_srv_data, sheet_name="Schül")
    
    # Assuming df is your DataFrame and 'column_name' is the column for which you want unique values

    
    # Add random numbers for testing
    add_random_numbers(file_dic, "HH9_OTC23")
    
    # Plot data
    plot_data(file_dic, srv_df)

# Entry point of the script
if __name__ == "__main__":
    main()
