import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is in a CSV file, load the data (adjust the path to your file)
# Replace 'your_file.csv' with the actual CSV file containing your data
folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\00_Datenaufbereitung\Dategrundlage.csv"

# Load your CSV data (make sure the separator and decimal options are correct)
df = pd.read_csv(folder_path, delimiter=';', decimal=',')

# Set the 'Zähstelle' column as the index (row labels)
df.set_index('Zaehstelle', inplace=True)

# Convert the dataframe values to numeric (in case there are issues with decimals)
df = df.apply(pd.to_numeric, errors='coerce')

# Create a figure for the plot
plt.figure(figsize=(10, 6))

# Plot each row as a line on the same axes, sharing the y-axis
for index, row in df.iterrows():
    plt.plot(df.columns, row, label=index)

# Customize the plot
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Line Plot for Each Zähstelle')
plt.xticks(rotation=45)
plt.legend(loc='best')
plt.tight_layout()

# Show the plot
plt.show()