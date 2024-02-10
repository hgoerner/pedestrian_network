from .config_loader import config_data
from typing import Tuple
import geopandas as gpd

def safe_gdf_as_gpkg(*args: Tuple[gpd.GeoDataFrame, str, bool]):
    """
    Saves a GeoDataFrame as a GeoPackage file.

    Args:
        *args: A tuple containing the GeoDataFrame, filename, and interimresult flag.
            - GeoDataFrame: The GeoDataFrame to be saved.
            - filename: The name of the output file.
            - interimresult: A flag indicating whether the file is safed in the interim result folder

    Returns:
        None

    Examples:
        safe_gdf_as_gpkg(gdf, 'output_file', False)
    """

    for arg in args:
        gdf, filename, interimresult = arg + (False,) if len(arg) == 2 else arg
        if interimresult and config_data["safe_interim_results"]:
            gdf.to_file(f'output\interim_result\{filename}.gpkg', driver='GPKG')
        else:
            gdf.to_file(f'output\{filename}.gpkg', driver='GPKG')