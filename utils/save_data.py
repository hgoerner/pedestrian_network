from utils.config_loader import config_data
from typing import Tuple
import geopandas as gpd
import zipfile
import os

def safe_gdf_as_gpkg(*args: Tuple[gpd.GeoDataFrame, str, bool]):
    """
    Saves a GeoDataFrame as a GeoPackage file.

    Args:
        *args: A tuple containing the GeoDataFrame, filename, and interimresult flag.
            - GeoDataFrame: The GeoDataFrame to be saved.
            - filename: The name of the output file.
            - interimresult: if True resluts gets saved in the interim_result folder.

    Returns:
        None

    Examples:
        safe_gdf_as_gpkg(gdf, 'output_file', False)
    """
    city = config_data["city_name"]

    for arg in args:
        gdf, filename, interimresult = arg + (False,) if len(arg) == 2 else arg
        if interimresult and config_data["safe_interim_results"]:
            gdf.to_file(f'data\output\interim_result\{filename}.gpkg', driver='GPKG')
        elif not interimresult:
            gdf.to_file(f'data\output\{filename}.gpkg', driver='GPKG')
            

def zip_geopackage(input_geopackage, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Add the GeoPackage file to the zip archive
        zip_file.write(input_geopackage, os.path.basename(input_geopackage))

