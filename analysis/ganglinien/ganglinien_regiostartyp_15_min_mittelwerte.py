import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.cm import get_cmap
# Define the main folder path
main_folder_path = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\03_RegioStarGem7_Typen_Mittelwerte'

# Define the colormap (Set1) for the subfolders
colormap = get_cmap('Set1')
colors = [colormap(i) for i in range(5)]
color_map = {}

X_LABEL = "Beginn 15-min-Intervall"
Y_LABEL = "Anteil je 15-min-Intervall"
PLOTTITLE = 'Anteil Fußverkehr je Zeitscheibe\nMittelwerte der Zählstellen je RegioStarGem7-Typ'

# X_LABEL = "Beginn Stundenntervall"
# Y_LABEL = "Anteil je Stundenintervall am Gesamtaufkommen"
# PLOTTITLE = 'Anteil Fußverkehr je Stunde\ngleitende Stunden Mittelwerte der Zählstellen je RegioStarGem7-Typ'

LEGENDTITLE = 'Legende'

# Initialize the plot
fig, ax = plt.subplots()

# Loop through each subfolder
for i, subfolder in enumerate(os.listdir(main_folder_path)):
    subfolder_path = os.path.join(main_folder_path, subfolder)
    
    if os.path.isdir(subfolder_path):
        color_map[subfolder] = colors[i % len(colors)]
        
        legend_name = subfolder.split('_')[-1]
        
        # Loop through each CSV file in the subfolder
        for csv_file in os.listdir(subfolder_path):
            if csv_file.endswith('.csv'):
                csv_file_path = os.path.join(subfolder_path, csv_file)
                
                # Read the CSV file
                df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')
                n = df["n"].unique().tolist()[0]
                # Assuming the CSV file has columns 'x' and 'y'
                ax.plot(df['start time(ohne Tag)'], df['gleitender_MW_15min'], color=color_map[subfolder], label=legend_name + " n="+str(n)  )
                
# Create legend
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(),  title=LEGENDTITLE)

# Set x-axis labels and limits
x_values = df['start time(ohne Tag)']
x_ticks = range(0, len(x_values), 4)  # Every 4th value
ax.set_xticks(x_ticks)
ax.set_xticklabels([x_values[i] for i in x_ticks], rotation=90)
ax.set_xlim(0, len(x_values) - 1) 
# Set y-axis labels to percentage and limits from 0% to 8%
ax.set_ylim(0, 0.08)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
ax.yaxis.set_major_locator(FixedLocator([0.01 * i for i in range(0, 9)]))
# Add labels and title

plt.title(PLOTTITLE, fontsize=18, pad=20)
plt.xlabel(X_LABEL, fontsize=16, labelpad=15)
plt.ylabel(Y_LABEL, fontsize=16, labelpad=15)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.grid(True, alpha=0.5)
plt.tight_layout(rect=[0, 0, 0.85, 1]) 

plt.show()