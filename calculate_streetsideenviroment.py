import geopandas as gpd
import pandas as pd
from tqdm import tqdm
import os


def load_geopackage():
    # Pfad zur GeoPackage-Datei
    geopackage_path = r"src\data\output\Seitendaten\Seitendaten.gpkg"
    # Laden des GeoPackages (mit Angabe der Ebene/Layer)
    return gpd.read_file(geopackage_path)

def load_all_poi_gdf():
    list_of_poi_gdf = []
    mainfolder = r"C:\Users\Goerner\Desktop\poi_geopackages"
    for geopackage in os.listdir(mainfolder):
        filepath = os.path.join(mainfolder, geopackage)
        poi_gdf = gpd.read_file(filepath)
        print(poi_gdf)
        list_of_poi_gdf.append(poi_gdf)
    return list_of_poi_gdf


def create_columnhead(streetside_polygon_gdf):
    
    # create columnsheader
    list_of_header = []

    # read key-value csv to get klassen und gruppen
    poi_key_value_df = pd.read_csv(r"src\data\input\poi_key_value.CSV", sep=";")
    list_of_group = list(poi_key_value_df["Gruppe"].unique())
    list_of_class = list(poi_key_value_df["Klasse"].unique())

    area_key_value_df = pd.read_csv(r"src\data\input\area_key_value.CSV", sep=";")

    # append list with unique values
    list_of_group.extend(area_key_value_df["Gruppe"].unique())
    list_of_class.extend(area_key_value_df["Klasse"].unique())
    
    for group in list_of_group:
        group_Anzahl_header = group + ": Anzahl"
        group_Summe_bedeutung_header = group + ": Summe_Bedeutung"
        list_of_header.extend([group_Anzahl_header, group_Summe_bedeutung_header])


    for klasse in list_of_class:
            klasse_Anzahl_header = klasse + ": Anzahl"
            klasse_Summe_bedeutung_header = klasse + ": Summe_Bedeutung"
            list_of_header.extend([klasse_Anzahl_header, klasse_Summe_bedeutung_header])
            
    # needed columns
    for header in list_of_header:
        streetside_polygon_gdf[header] = 0
    return streetside_polygon_gdf

def iterate_through_polygon(streetside_polygon_gdf, list_of_poi_gdf):
    for idx, polygon in tqdm(streetside_polygon_gdf.iterrows()):
        for poi_gdf in list_of_poi_gdf:
            print(idx, polygon, poi_gdf)


def main():
    streetside_polygon_gdf = load_geopackage()
    streetside_polygon_gdf = create_columnhead(streetside_polygon_gdf)
    list_of_pois_gdf = load_all_poi_gdf()

    iterate_through_polygon(streetside_polygon_gdf, list_of_pois_gdf)


if __name__ == "__main__":
    main()
