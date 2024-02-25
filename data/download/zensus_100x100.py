from utils.config_loader import config_data
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import urllib.request
from zipfile import ZipFile
from io import BytesIO

def download_zensus_data():
    """
    Downloads the zensus data from the specified URL, extracts the contents of the zip file, and returns a GeoDataFrame.

    Returns:
        gdf_zensus (GeoDataFrame): The extracted zensus data as a GeoDataFrame.

    Raises:
        None

    Examples:
        gdf = download_zensus_data()
    """
    
    config_data["zensus_url"]
    # Download the zip file using urllib
    response = urllib.request.urlopen(config_data["zensus_url"])
    zip_content = BytesIO(response.read())


    # Extract the contents of the zip file from memory
    with ZipFile(zip_content, 'r') as zip_ref:
        # Assuming there is only one CSV file in the zip, find it
        csv_files = [file for file in zip_ref.namelist() if file.endswith(".csv")]
        if len(csv_files) == 1:
            csv_filename = csv_files[0]
            with zip_ref.open(csv_filename) as csv_file:
                # Read the CSV file directly from the zip
                zensus_dataframe = pd.read_csv(csv_file, sep=";")
                
                # Filter the DataFrame
                zensus_dataframe = zensus_dataframe[zensus_dataframe['Einwohner'] != -1]
                
                # Create a GeoDataFrame
                geometry = [Point(xy) for xy in zip(zensus_dataframe['x_mp_100m'], zensus_dataframe['y_mp_100m'])]
                gdf_zensus = gpd.GeoDataFrame(zensus_dataframe, geometry=geometry, crs=config_data["zensus_crs"]).to_crs("EPSG:31468")
                
                # Save the GeoPackage
                return gdf_zensus
                
        else:
            print("Error: Unable to determine the CSV filename or multiple CSV files found.")




