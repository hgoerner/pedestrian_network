
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
# main_folder_path = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\10_Typisierung\Clusterung1'
# main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\12_Basisganglinie\Bedeutung_je_km_vs_Basisganglinie\unteres_quantil"
# main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\05_Umfeldkategorie\Mittelwerte_Umfeldkategorie"
# main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\09_Distanz_OPNV\Entfernung_Bushaltestelle\Quartile\Stundenmittelwerte"
# main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\09_Distanz_OPNV\Entfernung_BusQ1"
main_folder_path = r"C:\Users\Goerner\Desktop\plotordner"


PLOTTITLE = "Anteil Fußverkehr je Stunde\nStundenmittelwerte Cluster 0"

# Define the colormap (Set1) for the subfolders
colormap = get_cmap('Set1')
#colormap = get_cmap('tab20')
# colormap2 = get_cmap('tab20c')

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
        legend = csv_file.split("_")[0]
        #legend = addon[i]
        csv_file_path = os.path.join(main_folder_path, csv_file)

        # Read the CSV file
        df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')
        print(df)
        n = df["n"].unique().tolist()[0]
        legend_with_n = "Ganglinie"+" n="+str(n)
        # Plot the data
        ax.plot(df['start time(ohne Tag)'], df['gleitender_Stundenwert_aus_MW'],
                color=colors[3], label=legend_with_n,linewidth=5)
        j += 1

# Apply the plot settings using the utility function
apply_plot_settings(ax, "Mitte Stundenintervall", "Anteil der gleitenden Stunde", PLOTTITLE, 'Legende')

# Set x-axis labels and limits
x_values = df['start time(ohne Tag)']
x_ticks = range(0, len(x_values), 4)
# Set specific x-axis labels at 06:00, 12:00, and 18:00
x_ticks = ["06:00", "12:00", "18:00"]
ax.set_xticks([df[df['start time(ohne Tag)'] == time].index[0] for time in x_ticks])
ax.set_xticklabels(x_ticks, fontsize=28)
ax.set_xlim(0, len(x_values) - 1)

# Set specific y-axis labels and limits
ax.set_ylim(0, 0.12)

ax.set_yticklabels(labels=ax.set_yticks([0.05, 0.10]), fontsize=28)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))


plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.grid(True, alpha=0.5)

# Remove grid and legend
ax.grid(False)
ax.get_legend().remove()

# Show plot
plt.savefig("Zählstelle_Folders/Plot.png")
plt.show()
