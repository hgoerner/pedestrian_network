import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.cm import get_cmap
# Define the main folder path
main_folder_path = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\09_2Infrastrukturmerkmale\EntfernungSchule\Stundenmittelwerte'

# Define the colormap (Set1) for the subfolders
colormap = get_cmap('Set1')
colors = [colormap(i) for i in range(5)]
color_map = {}

X_LABEL = "Mitte Stundenintervall"
Y_LABEL = "Anteil der gleitenden Stunde"
PLOTTITLE = 'Anteil Fußverkehr je Stunde\nunterteilt nach Entfernung Schule in Quantile\ngemittelt'
LEGENDTITLE = 'Legende'

# Initialize the plot
fig, ax = plt.subplots(figsize=(12,6))

# Loop through each subfolder
 #color_map[subfolder] = colors[i % len(colors)]

# Loop through each CSV file in the subfolder
for i, csv_file in enumerate(os.listdir(main_folder_path)):
    print(csv_file)
    if csv_file.endswith('.csv'):
        legend = csv_file.split("_")[0]
        color_map[csv_file] = colors[i % len(colors)]
        legend_name = csv_file
        csv_file_path = os.path.join(main_folder_path, csv_file)
        print(csv_file)
        # Read the CSV file
        df = pd.read_csv(csv_file_path, usecols=lambda column: column != 'Unnamed: 0')
        n = df["n"].unique().tolist()[0]
        # Assuming the CSV file has columns 'x' and 'y'
        ax.plot(df['start time(ohne Tag)'], df['gleitender_Stundenwert_aus_MW'], color=color_map[csv_file], label=legend)
                
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
ax.set_ylim(0, 0.12)
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
ax.yaxis.set_major_locator(FixedLocator([0.01 * i for i in range(0, 13)]))
# Add labels and title

plt.title(PLOTTITLE, fontsize=18, pad=20)
plt.xlabel(X_LABEL, fontsize=16, labelpad=15)
plt.ylabel(Y_LABEL, fontsize=16, labelpad=15)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.grid(True, alpha=0.5)
plt.tight_layout(rect=[0, 0, 0.85, 1]) 
# Show plot
plt.show()