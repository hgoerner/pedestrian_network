import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.cm import get_cmap
import sys

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

# Import the utility function
from plot_utils import apply_plot_settings

# Define the main folder path
main_folder_path = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\10_Typisierung\Clusterung1'
main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\10_Typisierung\Clusterung1\Cluster_ohne_ausreißer\C2"
main_folder_path2 = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\10_Typisierung\Clusterung1\Cluster_ohne_ausreißer\C3"
main_folder_path3 = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\10_Typisierung\Clusterung1\Cluster_ohne_ausreißer\C1"
main_folder_path4 = r"C:\Users\Goerner\Desktop\pedestrian_network\Zählstelle_Folders"
PLOTTITLE = 'Ganglinie aller Zählquerschnitte'

# Define the colormap (Set1) for the subfolders
colormap = get_cmap('Set1')
# colormap = get_cmap('tab20')
# colormap2 = get_cmap('tab20c')

# Extract 20 colors from tab20b
#tab20b_colors = [colormap2(i) for i in range(colormap2.N)]


colors = [colormap(i) for i in range(20)]

color_map = {}

# Append the tab20b colors to the existing colors list
#colors.extend(tab20b_colors)

# Initialize the plot
fig, ax = plt.subplots(figsize=(12,6))

# Loop through each CSV file in the folder
j = 0
#addon =[" Entfernung < 30m", " Entfernung 30m bis 100m"," Entfernung 100m bis 250m", " Entfernung > 250m" ]
addon =""

legend = ["Cluster 5 n=14", "Cluster 1 n=7", "Cluster 2 n=2", "Cluster 3 n=5"]

first_plot = True
for i, csv_file in enumerate(os.listdir(main_folder_path4)):
    
    print(i)
    if csv_file.endswith('.csv'):
        #legend = csv_file.split("_")[0]
        color_map[csv_file] = colors[j % len(colors)]
        csv_file_path = os.path.join(main_folder_path4, csv_file)

        # Read the CSV file
        df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')

        legend_handle = legend[0] if first_plot else None
        #n = df["n"].unique().tolist()[0]
        #legend_with_n =legend+" n="+str(n)
        # Plot the data
        ax.plot(df['start time(ohne Tag)'], df['gleitender_Stundenwert_aus_MW'], color=colors[7], label=legend_handle)
        first_plot = False
        j += 1
first_plot = True

# for i, csv_file in enumerate(os.listdir(main_folder_path3)):
    
#     print(i)
#     if csv_file.endswith('.csv'):
#         #legend = csv_file.split("_")[0]
#         color_map[csv_file] = colors[j % len(colors)]
#         csv_file_path = os.path.join(main_folder_path3, csv_file)

#         # Read the CSV file
#         df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')

#         legend_handle = legend[1] if first_plot else None
#         #n = df["n"].unique().tolist()[0]
#         #legend_with_n =legend+" n="+str(n)
#         # Plot the data
#         ax.plot(df['start time(ohne Tag)'], df['gleitender_Stundenwert_aus_MW'], color=colors[1], label=legend_handle)
#         first_plot = False
#         j += 1

# first_plot = True
# for i, csv_file in enumerate(os.listdir(main_folder_path)):
    
#     print(i)
#     if csv_file.endswith('.csv'):
#         #legend = csv_file.split("_")[0]
#         color_map[csv_file] = colors[j % len(colors)]
#         csv_file_path = os.path.join(main_folder_path, csv_file)

#         # Read the CSV file
#         df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')

#         legend_handle = legend[2] if first_plot else None
#         #n = df["n"].unique().tolist()[0]
#         #legend_with_n =legend+" n="+str(n)
#         # Plot the data
#         ax.plot(df['start time(ohne Tag)'], df['gleitender_Stundenwert_aus_MW'], color=colors[2], label=legend_handle)
#         first_plot = False
#         j += 1

# first_plot = True
# for i, csv_file in enumerate(os.listdir(main_folder_path2)):
    
#     print(i)
#     if csv_file.endswith('.csv'):
#         #legend = csv_file.split("_")[0]
#         color_map[csv_file] = colors[j % len(colors)]
#         csv_file_path = os.path.join(main_folder_path2, csv_file)

#         # Read the CSV file
#         df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')

#         legend_handle = legend[3] if first_plot else None
#         #n = df["n"].unique().tolist()[0]
#         #legend_with_n =legend+" n="+str(n)
#         # Plot the data
#         ax.plot(df['start time(ohne Tag)'], df['gleitender_Stundenwert_aus_MW'], color=colors[3], label=legend_handle)
#         first_plot = False
#         j += 1

# Apply the plot settings using the utility function
apply_plot_settings(ax, "Mitte Stundenintervall", "Anteil der gleitenden Stunde", PLOTTITLE, 'Legende')

# Set x-axis labels and limits
x_values = df['start time(ohne Tag)']
x_ticks = range(0, len(x_values), 4)
ax.set_xticks(x_ticks)
ax.set_xticklabels([x_values[i] for i in x_ticks], rotation=90)
ax.set_xlim(0, len(x_values) - 1)

# Set y-axis labels and limits
ax.set_ylim(0, 0.15)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
ax.yaxis.set_major_locator(FixedLocator([0.01 * i for i in range(0, 16)]))

# Move the legend outside the plot
#ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.grid(True, alpha=0.5)

# Show plot
plt.savefig("Zählstelle_Folders/Plot.png")
plt.show()
