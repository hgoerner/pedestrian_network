from utils.config_loader import config_data
from utils.save_data import safe_gdf_as_gpkg
from utils.save_data import zip_geopackage
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import urllib.request
import os
from zipfile import ZipFile

# Define the local filename for the zip file
zip_filename = "csv_Bevoelkerung_100m_Gitter.zip"

# Define the directory where you want to save the CSV file
output_directory = "data\input\zensusfile"

downloaded_file_path = os.path.join(output_directory, zip_filename)
url = "https://www.zensus2011.de/SharedDocs/Downloads/DE/Pressemitteilung/DemografischeGrunddaten/csv_Bevoelkerung_100m_Gitter.zip?__blob=publicationFile&v=2"
# Download the zip file using urllib
urllib.request.urlretrieve(url, downloaded_file_path)


# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)


# Extract the contents of the zip file
with ZipFile(downloaded_file_path, 'r') as zip_ref:
    zip_ref.extractall(output_directory)

    # Assuming there is only one CSV file in the zip, find it
    csv_files = [file for file in os.listdir(output_directory) if file.endswith(".csv")]
    print(csv_files)
    if len(csv_files) == 1:
        csv_filename = csv_files[0]
        print(f"CSV file '{csv_filename}' downloaded and extracted successfully.")
    else:
        print("Error: Unable to determine the CSV filename or multiple CSV files found.")


zensus_dataframe = pd.read_csv("data\input\zensusfile\Zensus_Bevoelkerung_100m-Gitter.csv", sep=";")

# Assuming df is your DataFrame
zensus_dataframe = zensus_dataframe[zensus_dataframe['Einwohner'] != -1]

# Assuming df is your DataFrame
geometry = [Point(xy) for xy in zip(zensus_dataframe['x_mp_100m'], zensus_dataframe['y_mp_100m'])]

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(zensus_dataframe, geometry=geometry, crs=config_data["zensus_crs"]).to_crs("EPSG:31468")

safe_gdf_as_gpkg((gdf, "zensus_data"))

