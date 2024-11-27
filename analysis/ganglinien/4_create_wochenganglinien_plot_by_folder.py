
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

main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\13_Wochenanalyse\Tagesaufkommen\mo-so"

PLOTTITLE = "Anteil Fußverkehr je Tag\nWochenganglinien Montag bis Sonntag nach Cluster"

# Define the colormap (Set1) for the subfolders
colormap = get_cmap('Set1')
#colormap = get_cmap('tab20')
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

legend_list = ["Cluster 0", "Cluster 1", "Cluster 2", "Cluster 3"]
#addon = ""
# Loop through each subfolder
for i, subfolder in enumerate(os.listdir(main_folder_path)):
    subfolder_path = os.path.join(main_folder_path, subfolder)

    if os.path.isdir(subfolder_path):
        #color_map[subfolder] = colors[i % len(colors)]
        print(subfolder_path)
        #legend = subfolder.split('_')[1]

        # Loop through each CSV file in the subfolder
        for csv_file in os.listdir(subfolder_path):
            if csv_file.endswith('.csv'):
                csv_file_path = os.path.join(subfolder_path, csv_file)

                # Read the CSV file
                df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')
               
                ax.plot(df["Weekday"], df['count_anteilig'],
                        color=colors[i], label=legend_list[i])
        j += 1

# Apply the plot settings using the utility function
apply_plot_settings(ax, "Wochentag", "Anteil am Wochenaufkommen", PLOTTITLE, 'Legende')

# Set x-axis labels and limits
#x_values = df['Weekday']
# x_ticks = range(0, len(x_values), 4)
# Manual x-axis labels
weekdays = ["Montag","Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
ax.set_xticklabels(weekdays)  # Set the custom weekday labels  # 96 rows per day, 7 days, tick in the middle


# Set y-axis labels and limits
ax.set_ylim(0.0, 0.40)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
ax.yaxis.set_major_locator(FixedLocator([0.1 * i for i in range(0, 51)]))

# Move the legend outside the plot
#ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.grid(True, alpha=0.5)

# Show plot
plt.savefig("Zählstelle_Folders/Plot.png")
plt.show()
