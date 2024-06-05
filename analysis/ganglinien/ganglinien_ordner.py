import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from matplotlib.ticker import FixedLocator, FuncFormatter, MaxNLocator
from matplotlib.lines import Line2D

LEGENDTITLE = "Zählstelle"
X_LABEL = "Beginn 15-min-Intervall"
Y_LABEL = "Anteil je 15-min-Intervall (gleitend)"


def read_and_process_file(filepath):
    """
    Reads a CSV file, processes it, and returns the processed DataFrame.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The processed DataFrame.
        str: The base filename.
        int: The total count of pedestrians.
    """
    df = pd.read_csv(filepath)
    
    # Extract filename without extension
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    base_filename = base_filename.split('.')[0]
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

    return df_grouped, base_filename, total_count

def plot_data_from_folders(folderpath, title, subtitle): 
    """
    Plots the data from CSV files in the provided folders.

    Args:
        folderpaths (list): A list of folder paths containing CSV files.
        title (str): The title of the plot.
        subtitle (str): The subtitle of the plot.

    Returns:
        None
    """
    plot_title = f"{title}\n{subtitle}"
    
    plt.figure(figsize=(12, 8))
    ax = plt.gca()
    
    all_handles = []
    all_labels = []
        
        
    for filename in os.listdir(folderpath):
        if filename.endswith('.csv'):
            filepath = os.path.join(folderpath, filename)
            df_grouped, base_filename, total_count = read_and_process_file(filepath)
            
            # Plot the rolling mean with color from the colormap
            line, = ax.plot(df_grouped['start time(ohne Tag)'], df_grouped['gleitender_Mittelwert'], 
                                            label=f"{base_filename} n={total_count}")
            all_handles.append(line)
            all_labels.append(f"{base_filename} n={total_count}")
        

    
    # Set x-axis labels to show every 4th tick
    xticks = range(0, len(df_grouped['start time(ohne Tag)']), 4)
    ax.set_xticks(xticks)
    ax.xaxis.set_major_locator(FixedLocator(xticks))
    
    labels = df_grouped['start time(ohne Tag)'].iloc[xticks]
    ax.set_xticklabels(labels, rotation=90)

    # Set y-axis labels to percentage and limits from 0% to 8%
    ax.set_ylim(0, 0.08)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
    ax.yaxis.set_major_locator(FixedLocator([0.01 * i for i in range(0, 9)]))
    # Set plot details
    ax.set_xlim(-0.5, len(df_grouped['start time(ohne Tag)']) - 0.5)
    plt.title(plot_title, fontsize=16)
    plt.xlabel(X_LABEL, fontsize=14)
    plt.ylabel(Y_LABEL, fontsize=14)
    plt.yticks(fontsize=10)
    plt.xticks(fontsize=10)
    plt.grid(True, alpha=0.5)
        # Create separate legends for each folder
    # Create one legend on the right
    legend = plt.legend(handles=all_handles, labels=all_labels, title=LEGENDTITLE, loc='upper left')
        
    plt.tight_layout(rect=[0, 0, 0.8, 1])
    
    # Save the plot
    #plot_path = os.path.join(folderpaths[0], )
    plt.savefig("ganglininien_PN_EN_Hamburg_Kiel.png", dpi=100)
    plt.close()

def main():

    folder = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\Umfeld_Kategorie\PN_EN"
    plot_data_from_folders(folder, "Anteil Fußverkehr je Zeitscheibe", "Umfeldkategorie: PN EN")

if __name__ == "__main__":
    main()
