from data.download.zensus import download_zensus_data
from utils.helper import file_exists


def main():
    
    if not file_exists("src\data\output\zensus_100x100.gpkg"):
    
        gdf_zensus = download_zensus_data()
            
        gdf_zensus.to_file("src\data\output\zensus_100x100.gpkg", driver='GPKG') # type: ignore

if __name__ == "__main__":
    main()