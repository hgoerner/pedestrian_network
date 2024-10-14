

import os
import shutil
import pandas as pd
import sys

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from analysis.data_science_steps.data_manipulation import arithmethischer_mittelwert_aus_zaehlstellen


# Path to your Excel file
file_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\10_Typisierung\01_Datengrundlage_gesamt.xlsx"
# Path to the existing CSV files
source_folder = r'Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\01_Zählstellenseiten_Korrelation\01_Zählstellen_Seiten_zusammengefasst\unskaliert\mit_außreiser'

# Base path where new folders will be created
base_path = 'Zählstelle_Folders'
os.makedirs(base_path, exist_ok=True)

column_to_use = 'ohne Außreißer Cluster = 2\n(manuelle Zusammenfassung) '

# Load the Excel file and extract relevant sheet
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name='Tabelle1')
print(df.columns)
# Extract relevant columns
df_filtered = df[['Zählstelle', column_to_use]].dropna()

# Iterate through the rows and organize them into folders


def create_folders_with_zs():
    for index, row in df_filtered.iterrows():
        zaehlstelle = row['Zählstelle']
        cluster_value = row[column_to_use]
        #foldername = "Basisganglinie"

        if cluster_value == 0:
            foldername = "Cluster 0"
        if cluster_value == 1:
            foldername = "Cluster 1"

        # Create a folder for the cluster value if it doesn't exist
        #folder_path = os.path.join(base_path, f"Cluster {int(cluster_value)}")
        folder_path = os.path.join(base_path, foldername)
        os.makedirs(folder_path, exist_ok=True)

        # Construct the source file path (where the original CSV is located)
        source_file = os.path.join(source_folder, f"{zaehlstelle}_Seiten_zusammengefasst.csv")

        # Check if the file exists in the source folder
        if os.path.exists(source_file):
            # Move or copy the file to the respective cluster folder
            shutil.copy(source_file, folder_path)
        else:
            print(f"File {source_file} not found.")

    print(f"Files organized in directory: {base_path}")


# Loop through each subfolder

def calculate_mean_folder():
    for i, subfolder in enumerate(os.listdir(base_path)):

        subfolder_path = os.path.join(base_path, subfolder)
        if os.path.isdir(subfolder_path):
            print(subfolder_path)
            lage = subfolder.split(" ")[-1]
            print(lage)
            #df = gewichteteter_mittelwert_aus_zaehlstellen(subfolder_path)
            #df = gleitenden_stundenwerte_aus_zaehlstellen(subfolder_path)
            df = arithmethischer_mittelwert_aus_zaehlstellen(subfolder_path)
            df.to_csv(base_path+"/"+subfolder+"_gleitender_Stundenwert_aller_zs.csv", index=False)


create_folders_with_zs()
calculate_mean_folder()
