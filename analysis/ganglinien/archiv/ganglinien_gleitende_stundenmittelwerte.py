import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.cm import get_cmap
# Define the main folder path
main_folder_path = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\03_RegioStarGem7_Typen_Mittelwerte'

# Define the colormap (Set1) for the subfolders
colormap = get_cmap('tab20')
colors = [colormap(i) for i in range(20)]
color_map = {}

X_LABEL = "Beginn Stundenintervall"
Y_LABEL = "Anteil je Stundenintervall"
PLOTTITLE = 'Anteil Fußverkehr je Stunden\ngemittelte Stundenwerte der Zählstellen je RegioStarGem7-Typ\n '
LEGENDTITLE = 'Legende'

# Initialize the plot
fig, ax = plt.subplots()

# Loop through each subfolder
for i, subfolder in enumerate(os.listdir(main_folder_path)):
    subfolder_path = os.path.join(main_folder_path, subfolder)
    print(subfolder)
    if os.path.isdir(subfolder_path):
        j = 0
        color_map[subfolder] = [colors[(2*i) % len(colors)], colors[(2*i+1) % len(colors)]]  # Store two colors per subfolder
        
        legend_name = subfolder.split('_')[1]
        
        # Loop through each CSV file in the subfolder
        for j, csv_file in enumerate(os.listdir(subfolder_path), start=1):
            if csv_file.endswith('.csv'):
                csv_file_path = os.path.join(subfolder_path, csv_file)
                print(csv_file, j)
                # Read the CSV file
                df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')
                if j == 1:
                    # Assuming the CSV file has columns 'x' and 'y'
                    ax.plot(df['start time(ohne Tag)'], df['gleitender_Stundenwert_aus_MW'], color=color_map[subfolder][0], label=legend_name + " (2-1)")
                elif j == 2:
                    # Assuming the CSV file has columns 'x' and 'y'
                    ax.plot(df['start time(ohne Tag)'], df['gleitender_Stundenwert_aus_MW'], color=color_map[subfolder][1], label=legend_name + " (1-2)")


handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(),  title=LEGENDTITLE)

# Set x-axis labels and limits
ax.set_xticklabels(df['start time(ohne Tag)'], rotation=90)
ax.set_xlim(-0.5, len(df['start time(ohne Tag)']) - 0.5)
# Set y-axis labels to percentage and limits from 0% to 8%
ax.set_ylim(0, 0.25)
# original für Viertelstundew
#ax.set_ylim(0, 0.08)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
ax.yaxis.set_major_locator(FixedLocator([0.01 * i for i in range(0, 25)]))
# Add labels and title

plt.title(PLOTTITLE, fontsize=16)
plt.xlabel(X_LABEL, fontsize=14)
plt.ylabel(Y_LABEL, fontsize=14)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.grid(True, alpha=0.5)
plt.tight_layout(rect=[0, 0, 0.85, 1]) 
# Show plot
plt.show()