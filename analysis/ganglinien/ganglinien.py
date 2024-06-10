import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.lines import Line2D
import numpy as np


# Define color maps
reds = plt.cm.Reds
blues = plt.cm.Blues
Set2 = plt.cm.Set2
CMRmap = plt.cm.CMRmap

X_LABEL = "Beginn 15-min-Intervall"
Y_LABEL = "Anteil je 15-min-Intervall"
PLOTTITLE = 'Anteil Fußverkehr je Zeitscheibe'
LEGENDTITLE = "Zählstelle"

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

class PlotManager:
    def __init__(self, title = PLOTTITLE, xlabel = X_LABEL, ylabel = Y_LABEL):
        """
        Initializes a plot with the specified title, x-label, and y-label.

        Args:
            title: The title of the plot.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.

        Returns:
            None
        """
        self.fig, self.ax = plt.subplots(figsize=(14, 8))
        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.grid(True)
        self.legend_elements = []

    def plot_group(self, dataframes, labels, color_map, group_label):
        """Plots a group of dataframes with a common colormap but distinct intensities."""
        # Create a color map based on the length of the dataframes list
        colors = color_map(np.linspace(0.3, 1, len(dataframes)))

        # Header for the group in the legend
        self.legend_elements.append(Line2D([0], [0], color='w', label=group_label, markerfacecolor='w', markersize=15))

        for df, label, color in zip(dataframes, labels, colors):

            self.ax.plot(df['start time(ohne Tag)'], df['gleitender_Mittelwert'], label=f"{label}", color=color)
            self.legend_elements.append(Line2D([0], [0], color=color, label=f"{label}"))
        
        
    def show(self, dataframes: list, filename:str):
        """
        Displays the plot with customized x-axis and y-axis labels and limits.

        Args:
            dataframes: A list of dataframes containing the plot data.

        Returns:
            None
        """
        # Set x-axis labels to show every 4th tick / just take the first dataframe
        dataframe = dataframes[0]
        xticks = range(0, len(dataframe['start time(ohne Tag)']), 4)
        self.ax.set_xticks(xticks)
        self.ax.xaxis.set_major_locator(FixedLocator(xticks))
        labels = dataframe['start time(ohne Tag)'].iloc[xticks]
        self.ax.set_xticklabels(labels, rotation=90)
        self.ax.set_xlim(-0.5, len(dataframe['start time(ohne Tag)']) - 0.5)
        # Set y-axis labels to percentage and limits from 0% to 8%
        self.ax.set_ylim(0, 0.08)
        self.ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
        self.ax.yaxis.set_major_locator(FixedLocator([0.01 * i for i in range(0, 9)]))
        # Set plot details
        
        # Custom legend handling to include group headers
        self.ax.legend(handles=self.legend_elements, title=LEGENDTITLE, loc='upper left', bbox_to_anchor=(1,1))
        # plt.title(plot_title, fontsize=16)
        # plt.xlabel(X_LABEL, fontsize=14)
        # plt.ylabel(Y_LABEL, fontsize=14)
        plt.yticks(fontsize=10)
        plt.xticks(fontsize=10)
        plt.grid(True, alpha=0.5)
        plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to make space for legend       
        plt.savefig(filename, dpi=100)
        plt.show()

        


def return_and_process_dataframes(folderpath):
    """
    Reads and processes CSV files in the specified folder path, returning a list of dataframes and corresponding basenames.

    Args:
        folderpath: The path to the folder containing the CSV files.

    Returns:
        A tuple containing a list of dataframes and a list of basenames.
    """
    dataframes_list = []
    basename_list = []
    for filename in os.listdir(folderpath):
        if filename.endswith('.csv'):
            filepath = os.path.join(folderpath, filename)
            dataframe, basename, n = read_and_process_file(filepath)
            dataframes_list.append(dataframe)
            basename_list.append(basename+' n='+str(n))
            
            
    return dataframes_list, basename_list



# Main function
def main(): 
    
    #folder to catogorized csv-files
    folderpath =r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\Umfeld_Kategorie\PH_EH" 
    
    # Example usage
    # Create an instance of the plot manager
    pm = PlotManager()
       
    dataframes_list, basename_list= return_and_process_dataframes(folderpath)
    print(dataframes_list[0])
    # Plot groups with respective color themes and headers
    pm.plot_group(dataframes_list, basename_list, Set2, 'PH EH')
    # Display the plot
    pm.show(dataframes_list)
    

# Entry point of the script
if __name__ == "__main__":
    main()