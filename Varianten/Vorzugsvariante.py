import os
import sys
import geopandas as gpd
from tqdm import tqdm


current_directory = os.getcwd()
print(current_directory)

sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\Code2\\pedestrian_network')
sys.path.append('C:\\Users\\Goerner\\Desktop\\pedestrian_network')

from utils.save_data import safe_gdf_as_gpkg
from utils.load_data import find_geo_packages
from utils.config_loader import config_data
#buffer in meter
BUFFERSIZE = 250


counts_csv_filepath = r""
#census = r"data\input\Sonstiges\98-401-X2021020_English_CSV_data.csv"

#census_data = pd.read_csv(census, encoding='latin-1',sep=",")

#print(census_data)

geo_packages = find_geo_packages()

print(geo_packages)

#filepaths to files using
street_net_optimized_filepath = geo_packages["streets"]
area_filepath = geo_packages["areas"]
pois_filepath = geo_packages["pois"]
nodes_filepath = geo_packages["nodes"]
census_filepath = r"data\output\zensus_100x100.gpkg"

#read geopackages
street_net_optimized_gdf = gpd.read_file(street_net_optimized_filepath)
area_gdf = gpd.read_file(area_filepath)
pois_gdf = gpd.read_file(pois_filepath)
census_gdf = gpd.read_file(census_filepath)

#filter street net to only use streets thar are longer than 100
street_net_optimized_gdf = street_net_optimized_gdf[street_net_optimized_gdf["laenge [km]"] >= 0.1]

#buffer street net by buffersize ands create new geodataframe
street_net_optimized_buffered_gdf = street_net_optimized_gdf.copy()
street_net_optimized_buffered_gdf["geometry"] = street_net_optimized_gdf["geometry"].buffer(BUFFERSIZE)

#buffer pois
pois_buffered_gdf = pois_gdf.copy()
pois_buffered_gdf['geometry'] = pois_gdf.apply(lambda row: row['geometry'].buffer(row['Einflussbereich']), axis=1)

#buffer areas
area_buffered_gdf = area_gdf.copy()
area_buffered_gdf['geometry'] = area_gdf.apply(lambda row: row['geometry'].buffer(row['Einflussbereich']), axis=1)

#Initialize a new column for the sum of values
street_net_optimized_gdf['Summe POI*Bedeutung'] = 0
street_net_optimized_gdf['Summe AREA*Bedeutung'] = 0
street_net_optimized_gdf['Summe Einwohner'] = 0

# Create a spatial index for the census GeoDataFrame
census_sindex = census_gdf.sindex

# Calculate Zensusdensity   
for idx, buffered_line in tqdm(street_net_optimized_buffered_gdf.iterrows()):
    print(idx)
    possible_matches_index = list(census_sindex.intersection(buffered_line['geometry'].bounds))
    possible_matches = census_gdf.iloc[possible_matches_index]
    
    intersected_points = possible_matches[possible_matches['geometry'].intersects(buffered_line['geometry'])]
    # assign to id in original gdf
    street_net_optimized_gdf.at[idx, 'Summe Einwohner'] = intersected_points['Einwohner'].sum()  

# Iterate through lines and update the Summe POI*Bedeutung column
for idx, line in tqdm(street_net_optimized_gdf.iterrows()):
    intersected_pois = pois_buffered_gdf[pois_buffered_gdf['geometry'].intersects(line['geometry'])]
    street_net_optimized_gdf.at[idx, 'Summe POI*Bedeutung'] = intersected_pois['Bedeutung'].sum()
    
# Iterate through lines and update the Summe AREA*Bedeutung column    
for idx, line in tqdm(street_net_optimized_gdf.iterrows()):
    intersected_areas = area_buffered_gdf[area_buffered_gdf['geometry'].intersects(line['geometry'])]
    street_net_optimized_gdf.at[idx, 'Summe AREA*Bedeutung'] = intersected_areas['Bedeutung'].sum()
 
street_net_optimized_gdf["Bedeutung je km"] = round((street_net_optimized_gdf["Summe AREA*Bedeutung"] + street_net_optimized_gdf['Summe POI*Bedeutung']) /street_net_optimized_gdf["laenge [km]"] ,2)
street_net_optimized_gdf["Einwohner je km"] = round(street_net_optimized_gdf['Summe Einwohner']/street_net_optimized_gdf["laenge [km]"] ,2)

# create Faktor
street_net_optimized_gdf["Einwohner-Faktor"] = round(street_net_optimized_gdf["Einwohner je km"]  * 1/15000, 2)

# Drop the intermediate column 'intersected_points'
safe_gdf_as_gpkg((street_net_optimized_gdf, f"street_net_optimized_updated_"+config_data["city_name"]))