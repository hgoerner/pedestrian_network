from data.download.zensus_100x100 import download_zensus_data
from utils.helper import file_exists



def main():
    
    if not file_exists("data\output\zensus_100x100.gpkg"):
    
        gdf_zensus = download_zensus_data()
        
        gdf_zensus.to_file("data\output\zensus_100x100.gpkg", driver='GPKG')

if __name__ == "__main__":
    main()