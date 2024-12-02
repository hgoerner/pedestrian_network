import os

import geopandas as gpd

from modules.street_net_creation import assign_values_to_new_street_net


def update_true_street_name():
    main_folder_path =r"C:\Users\Goerner\Desktop\pedestrian_network\data\output"

    for subfolder in os.listdir(main_folder_path):
        subfolder_path = os.path.join(main_folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):                               
                if filename.endswith('.gpkg'):
                    print(filename)
                    filepath = os.path.join(subfolder_path, filename)
                    geopackage  = gpd.read_file(filepath)
                    # filter geopackage
                    filename_splitted = filename.split(".")[0]
                    # Check for non-null and non-empty strings
                    mask = geopackage["Zaehlstelle"].notna() & (geopackage["Zaehlstelle"].str.strip() != "")

                    # Apply the mask to filter the GeoDataFrame
                    geopackage_filtered = geopackage[mask].copy()
                    # Find the second GeoPackage in the "interim" folder
                    interim_folder_path = os.path.join(subfolder_path, 'interim')
                    if os.path.exists(interim_folder_path) and os.path.isdir(interim_folder_path):
                        for interim_filename in os.listdir(interim_folder_path):
                            if interim_filename.endswith('v0.0.gpkg'):
                                print(interim_filename)
                                interim_filepath = os.path.join(interim_folder_path, interim_filename)
                                gdf_osm_net = gpd.read_file(interim_filepath)

                                # Call the function with both GeoDataFrames
                                gdf_true_street_name = assign_values_to_new_street_net(gdf_osm_net=gdf_osm_net, gdf_street_net_optimized=geopackage_filtered)
                                gdf_true_street_name.to_excel(filename_splitted+"_true_streetname"+".xlsx", sheet_name="Filtered Data", index=False)
                                break  # Stop after finding the first matching v0.0.gpkg file
                    else:
                        print(f"No 'interim' folder found in {subfolder_path}")
            
                    


if __name__ == "__main__":
    main()
