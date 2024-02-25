from data.download.zensus_100x100 import download_zensus_data
from utils.save_data import safe_gdf_as_gpkg
from utils.helper import file_exists

def main():
    
    if not file_exists("data\output\zensus_100x100.gpkg"):
    
        gdf_zensus = download_zensus_data()
        
        safe_gdf_as_gpkg((gdf_zensus, "zensus_100x100" ))


if __name__ == "__main__":
    main()