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
    file_dic = {}
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder, filename)
            file_basename = os.path.splitext(filename)[0]
            df = pd.read_csv(file_path)
            file_dic[file_basename] = df
    return file_dic

# Function to add random numbers for testing
def add_random_numbers(file_dic,filename):
        file_dic[filename]["count"] = np.random.randint(20, 400, size=len(file_dic[filename]))

# Function to plot data
def plot_data(file_dic):
    fig, ax = plt.subplots()
    for filename, df in file_dic.items():
        df['start time'] = pd.to_datetime(df['start time'], format='ISO8601')
        summed_up_count = df["count"].sum()
        df["count_anteilig"] = df["count"] / summed_up_count
        df_grouped_by_flow = df.groupby(['start time', 'flow'])['count_anteilig'].sum().reset_index()
        df_total = df.groupby('start time')['count_anteilig'].sum().reset_index()
        
        ax.plot(df_total['start time'], df_total['count_anteilig'], linestyle='-', label=filename+"_total")
        if RICHTUNGSFEIN:
            for flow, group in df_grouped_by_flow.groupby('flow'):
                ax.plot(group['start time'], group['count_anteilig'], linestyle='-', label=f'{flow, filename}', linewidth=1.5)

    plt.title(TITLE, fontsize=14)
    plt.xlabel(X_LABEL, fontsize=12)
    plt.ylabel(Y_LABEL, fontsize=12)
    plt.xticks(df_total['start time'], fontsize=8, rotation=90)
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))
    plt.grid(True, alpha=0.5)
    plt.legend(title=LEGENDTITLE, fontsize=10)
    plt.xlim(df_total['start time'].min(), df_total['start time'].max())
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # Specify the folder containing CSV files
    folder = r"C:\Users\Goerner\Desktop\Hamburg_zaehlstellen"
    
    # Read CSV files into a dictionary
    file_dic = read_csv_files(folder)
    
    # Add random numbers for testing
    add_random_numbers(file_dic, "HH9_OTC23")
    
    # Plot data
    plot_data(file_dic)

# Entry point of the script
if __name__ == "__main__":
    main()
