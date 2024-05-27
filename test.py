import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D

def prepare_dataframe(dataframe):
    pass

class PlotManager:
    def __init__(self, title, xlabel, ylabel):
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
            self.ax.plot(df['x'], df['y'], label=f"{label}", color=color)
            self.legend_elements.append(Line2D([0], [0], color=color, label=f"{label}"))

    def show(self):
        # Custom legend handling to include group headers
        self.ax.legend(handles=self.legend_elements, title='Zählstelle', loc='upper left', bbox_to_anchor=(1,1))
        plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to make space for legend
        plt.show()

# Example usage

# Create an instance of the plot manager
pm = PlotManager('Anteil Fußverkehr je Zeitscheibe', 'Beginn 15-min-Intervall', 'Anteil je 15-min-Intervall (gleitend)')

# Example DataFrames
data1 = pd.DataFrame({'x': range(10), 'y': np.random.rand(10)})
data2 = pd.DataFrame({'x': range(10), 'y': np.random.rand(10) * 0.5})
data3 = pd.DataFrame({'x': range(10), 'y': np.random.rand(10) * 1.5})
data4 = pd.DataFrame({'x': range(10), 'y': np.random.rand(10)})
data5 = pd.DataFrame({'x': range(10), 'y': np.random.rand(10) * 0.5})

# Define color maps
reds = plt.cm.Reds
blues = plt.cm.Blues

# Plot groups with respective color themes and headers
pm.plot_group([data1, data2, data3], ['Data1', 'Data2', 'Data3'], reds, 'PH EH')
pm.plot_group([data4, data5], ['Data4', 'Data5'], blues, 'PH EN')

# Display the plot
pm.show()