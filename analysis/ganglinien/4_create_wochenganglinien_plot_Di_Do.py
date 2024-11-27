
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.cm import get_cmap
import sys

# sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
# sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')


from plot_utils import apply_plot_settings
# Import the utility function

# Define the main folder path

main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\13_Wochenanalyse\7Tage\Datengrundlage\Seiten_zusammengefasst\Di-Do_summen"

PLOTTITLE = "Anteil Fußverkehr je Tag\nWochenganglinien Dienstag bis Donnerstag"

# Define the colormap (Set1) for the subfolders
colormap = get_cmap('Set1')
colormap = get_cmap('tab20')
#colormap2 = get_cmap('tab20c')

# Extract 20 colors from tab20b
#tab20b_colors = [colormap2(i) for i in range(colormap2.N)]


colors = [colormap(i) for i in range(20)]

color_map = {}

# Append the tab20b colors to the existing colors list
# colors.extend(tab20b_colors)

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Loop through each CSV file in the folder
j = 0

index_list = [0,7]

addon = ["Cluster 0"]
#addon = ""
for i, csv_file in enumerate(os.listdir(main_folder_path)):
    first_plot = True
    print(i)
    if csv_file.endswith('.csv'):
        legend = csv_file.split("_")[1]
        #legend = addon[i]
        csv_file_path = os.path.join(main_folder_path, csv_file)

        # Read the CSV file
        df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')

        #n = df["n"].unique().tolist()[0]
        #legend_with_n = "Ganglinie"+" n="+str(n)
        # Plot the data
        ax.plot(df["Weekday"], df['count_anteilig'],
                color=colors[j], label=legend)
        j += 1

# Apply the plot settings using the utility function
apply_plot_settings(ax, "Mitte Stundenintervall", "Anteil der gleitenden Stunde", PLOTTITLE, 'Legende')

# Set x-axis labels and limits
#x_values = df['Weekday']
# x_ticks = range(0, len(x_values), 4)
# Manual x-axis labels
weekdays = ["Samstag", "Sonntag"]

ax.set_xticklabels(weekdays)  # Set the custom weekday labels
# ax.set_xticklabels([x_values[i] for i in x_ticks], rotation=90)
# Adjust x-axis limits
#ax.set_xlim(ticks[0] - 48, ticks[-1] + 48)  # Extend limits to start and end just before/after the first/last tick

# Set y-axis labels and limits
ax.set_ylim(0.2, 0.50)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
ax.yaxis.set_major_locator(FixedLocator([0.1 * i for i in range(0, 51)]))

# Move the legend outside the plot
#ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.grid(True, alpha=0.5)

# Show plot
plt.savefig("Zählstelle_Folders/Plot.png")
plt.show()
