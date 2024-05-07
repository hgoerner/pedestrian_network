import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

current_directory = os.getcwd()

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

RICHTUNGSFEIN = True

TITLE = "TITLE"
LEGENDTITLE = "Fußverkehrsaufkommen"
X_LABEL = "X-Achse"
Y_LABEL = "Y-Achse"

#folder to csv
folder = r"C:\Users\Goerner\Desktop\Hamburg_zaehlstellen"

#read metadaten

file_dic = {}

for filename in os.listdir(folder):
    # Get the full file path
    if filename.endswith('.csv'):
        file_path = os.path.join(folder, filename)
        
        # Get the file basename
        file_basename = os.path.splitext(filename)[0]
        
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Store the filename along with the DataFrame in the dictionary
        file_dic[file_basename] = df
        
#import csv
# df1 = pd.read_csv(r"C:\Users\Goerner\Desktop\HH6_OTC26.csv")
# df2 = pd.read_csv(r"C:\Users\Goerner\Desktop\HH9_OTC23.csv")

# # create random numbers for testing
# df2["count"] = np.random.randint(20, 400, size=len(df2))


fig, ax = plt.subplots()
for filename, df in file_dic.items():
    # Convert start time column to datetime
    df['start time'] = pd.to_datetime(df['start time'], format='ISO8601')

    summed_up_count = df["count"].sum()

    df["count_anteilig"] = df["count"]/summed_up_count

    # Group by 'start time' and sum the 'count'
    df_grouped_by_flow = df.groupby(['start time', 'flow'])['count_anteilig'].sum().reset_index()

    # Group by 'start time' and sum the 'count' without grouping by flow
    df_total = df.groupby('start time')['count_anteilig'].sum().reset_index()
    # Plot the dataframe
    

    # Plot the line without grouping by flow
    ax.plot(df_total['start time'], df_total['count_anteilig'], linestyle='-', label=filename)
    
    if RICHTUNGSFEIN:
        # Loop through unique 'flow' values
        for flow, group in df_grouped_by_flow.groupby('flow'):
            ax.plot(group['start time'], group['count_anteilig'], linestyle='-',  label=f'{flow, filename}', linewidth=1.5)


# Set plot title and labels
plt.title(TITLE, fontsize=14)
plt.xlabel(X_LABEL, fontsize=12)
plt.ylabel(Y_LABEL, fontsize=12)

# Format x-axis ticks to show only time
# Show every tick on x-axis
plt.xticks(rotation=45, ticks=df_grouped_by_flow['start time'], ha='right')

# Set font size of x-axis ticks
plt.xticks(fontsize=8)

# Set y-axis ticks at intervals of 10
#plt.yticks(range(0, df_total['count_anteilig'].max() + 10, 10))

# Format x-axis ticks to show only time
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))
# Add grid
plt.grid(True, alpha=0.5)
# Add legend
plt.legend(title=LEGENDTITLE, fontsize=10)

# Set x-axis limits to match the data range
plt.xlim(df_total['start time'].min(), df_total['start time'].max())

# Show plot
plt.tight_layout()
# Show plot
plt.show()