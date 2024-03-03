import os
import sys
import geopandas as gpd

current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.config_loader import config_data
from utils.load_data import find_files_by_city

#create dictionary with data to use

# filter streets by length

# buffer pois with einfluss column

# intersect with street net and ad up "bedeutung"


#load poi-geopackage



def main():

    list_of_geopackages = find_files_by_city()
    
    print(list_of_geopackages)

if __name__ == "__main__":
    main()