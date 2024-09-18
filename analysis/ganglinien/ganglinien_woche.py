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
main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\13_Wochenanalyse\02_Mehrtageserhebung\Woche_sa_so"


PLOTTITLE = 'Wochenganglinien Samstag und Sonntag'

# Define the colormap (Set1) for the subfolders
colormap = get_cmap('Set1')
colors = [colormap(i) for i in range(10)]
color_map = {}

# Initialize the plot
fig, ax = plt.subplots(figsize=(6,6))

# Loop through each CSV file in the folder
j = 0
#addon =[" Entfernung < 30m", " Entfernung 30m bis 100m"," Entfernung 100m bis 250m", " Entfernung > 250m" ]
addon =""
for csv_file in os.listdir(main_folder_path):
    if csv_file.endswith('.csv'):
        legend = csv_file.split("_")[0]
        legend = csv_file.split(".")[0]
        color_map[csv_file] = colors[j % len(colors)]
        csv_file_path = os.path.join(main_folder_path, csv_file)

        # Read the CSV file
        df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')

        #n = df["n"].unique().tolist()[0]
        #legend_with_n =legend+" n="+str(n)
        # Plot the data
        ax.plot(df['Weekday'], df['count_anteilig'], color=color_map[csv_file], label=legend)
        j += 1




# Apply the plot settings using the utility function
apply_plot_settings(ax, "Wochentag", "Anteil des täglichen Aufkommens", PLOTTITLE, 'Legende')

# Move the legend outside the plot
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.,title = "Legende" )

# Set x-axis labels and limits
x_values = df['Weekday']
x_ticks = range(0, len(x_values))
#ax.set_xticks([i - 0.5 for i in x_ticks])
ax.set_xticklabels([x_values[i] for i in x_ticks], rotation=90)
#ax.set_xlim(-0.5, len(x_values) - 0.5)

# Set y-axis labels and limits
ax.set_ylim(0.15, 0.90)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
ax.yaxis.set_major_locator(FixedLocator([0.01 * i for i in range(0, 81)]))

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.grid(True, alpha=0.5)



# Show plot
plt.savefig("Zählstelle_Folders/Plot.png")
plt.show()