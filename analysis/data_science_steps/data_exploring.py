import pandas as pd
import os
import geopandas as gpd

#code explanation
# that finds day the maximum n in weekdays tuesday, wednesday, thursday for in a whole week
# for csv data with pedestrian detection finds 24 hours connected hours with maximum n



def get_weekday(df_ped):
    df_ped["start time"] = pd.to_datetime(df_ped["start time"])
    df_ped['Weekday'] = df_ped['start time'].dt.day_name()

    return df_ped

def read_and_process_file(folderpath):    

    for filename in os.listdir(folderpath):
        if filename.endswith('.csv'):
            filepath = os.path.join(folderpath, filename)
            
            # Extract filename without extension
            base_filename = os.path.splitext(os.path.basename(filepath))[0]
            base_filename = base_filename.split('.')[0]
            
            df = pd.read_csv(filepath, usecols=lambda column: column != 'Unnamed: 0')   
            df_ped = df[df['classification'] == 'pedestrian'].copy()           
            df_ped = get_weekday(df_ped)
            
            df_ped = df_ped.fillna(0)
            df_ped['datetime'] = pd.to_datetime(df_ped["start time"])
            df_ped = df_ped.sort_values(by='datetime')
            df_ped.reset_index(drop=True, inplace=True)

            nan_rows = df_ped[df_ped.isna().any(axis=1)]
            print(nan_rows)
            
            
            #df_ped.to_csv(base_filename+".csv", index=False)

    
def get_weekday_with_maximum(folderpath):
    """
    Finds the weekday with the maximum count in each CSV file within the specified folderpath.

    Args:
        folderpath: The path to the folder containing the CSV files.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified folderpath does not exist.
    """

    for filename in os.listdir(folderpath):
       
        if filename.endswith('.csv'):
            filepath = os.path.join(folderpath, filename)
            df_ped = pd.read_csv(filepath, usecols=lambda column: column != 'Unnamed: 0')  
            df_ped = df_ped.fillna(0)
            unique_weekdays_list = df_ped['Weekday'].unique().tolist()
            df_ped['start occurrence date'] = pd.to_datetime(df_ped["start occurrence date"])
            print(df_ped['start occurrence date'])
            unique_date_list = df_ped['start occurrence date'].unique().tolist()
            #print("Unique weekdays as list:", unique_weekdays_list)
            max_count = 0
            for date in unique_date_list:
                filtered_df_ped = df_ped[df_ped['start occurrence date'] == date]
                weekday = date.day_name()
                if weekday in ['Tuesday', 'Wednesday', 'Thursday']:
                    # Filter the DataFrame for the specified weekday
                    filtered_df_ped = df_ped[df_ped['Weekday'] == weekday]
                    
                    if len(filtered_df_ped) == 192:

                        count_sum = filtered_df_ped["count"].sum()

                        max_count = max(count_sum, max_count)
                        
                        if max_count == count_sum:
                            max_df_ped = filtered_df_ped.copy()
                                  
                        #print(filename, count_sum, max_count, weekday, len(filtered_df_ped))
                      
            print(max_df_ped)
            max_df_ped.to_csv(filename, index=False)

def find_maximum_24h_of_two_days(folderpath):
    list_to_short_files = []
    for filename in os.listdir(folderpath):
       
        if filename.endswith('.csv'):
            filepath = os.path.join(folderpath, filename)
            df_ped = pd.read_csv(filepath, usecols=lambda column: column != 'Unnamed: 0')  
            df_ped = df_ped.fillna(0)
            if len(df_ped) >= 192:          
                df_ped['datetime'] = pd.to_datetime(df_ped["start time"])
                # Ensure the DataFrame is sorted by datetime
                df_ped = df_ped.sort_values(by='datetime')
                df_ped.reset_index(drop=True, inplace=True)
                # Calculate rolling sum over 192 rows
                df_ped['rolling_sum'] = df_ped['count'].rolling(window=192).sum()
                # Find the start index of the window with the maximum rolling sum
                max_rolling_sum_index = df_ped['rolling_sum'].idxmax()

                            # # Extract the rows corresponding to the maximum rolling sum
                max_rows = df_ped.loc[max_rolling_sum_index - 191:max_rolling_sum_index]
                print(max_rows[["count","factor","count_scaled"]].head())
                # Optionally drop the rolling_sum column
                max_rows = max_rows.drop(columns=['rolling_sum',"datetime" ])
                # Save the result to a CSV file
                max_rows.to_csv(filename, index=False)

            else:
                list_to_short_files.append(filename)
    print(list_to_short_files)

def get_scalefactor(main_folder_path):
    """Obtain the scale factor for data normalization.

    This function is designed to retrieve a scale factor that is essential for normalizing data in analysis processes. It ensures that the data is appropriately scaled for accurate interpretation and comparison.

    Args:
        None

    Returns:
        float: The scale factor used for normalization.
    """
    dict_factors = []
    for i, subfolder in enumerate(os.listdir(main_folder_path)):
        
        subfolder_path = os.path.join(main_folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):
                
                
                if filename.endswith('.csv') and not filename.startswith('~$'):
                    
                    filepath = os.path.join(subfolder_path, filename)
                    df = pd.read_csv(filepath)
                    basename = filename.split(".")[0]
                    df1 = df[df['start occurrence time'] == "07:00:00"]
                    df2 = df[df['start occurrence time'] == "13:00:00"]
                    df3 = df[df['start occurrence time'] == "17:00:00"]
                    df4 = df[df['start occurrence time'] == "21:00:00"]
                    
                    # Extract the two factors for the time "00:00:00"
                    df1['factor'].tolist()

                    dic = {basename : {"07:00":df1['factor'].tolist(), "13:00":df2['factor'].tolist(), "17:00":df3['factor'].tolist(), "21:00":df4['factor'].tolist()}}
                    dict_factors.append(dic)
    print(dict_factors)
    # Initialize an empty list to collect data
    rows = []
    
    # Initialize an empty dataframe
    df = pd.DataFrame()
    
    # Loop through the list of dictionaries
    for entry in dict_factors:
        for key, value in entry.items():
            # Flatten the sub-dictionary and add the main key as a column
            flat_data = {}
            for time, values in value.items():
                flat_data[f'{time}_1'] = values[0]
                flat_data[f'{time}_2'] = values[1]
            flat_data['Key'] = key
            rows.append(flat_data)

    # Create the DataFrame from the list of flattened dictionaries
    df = pd.DataFrame(rows)
    # Set the 'Key' as the index
    df.set_index('Key', inplace=True)

    # Display the DataFrame
    print(df)
    df.to_csv("zaehlstellen_faktoren.csv",)
    
def explore_geopacke(filepath):
    pass
    

    


def main(): 
    
    #folder to catogorized csv-files
    main_folder_path =r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\00_Datenaufbereitung\XX_nachgeliefert_Datenskaliert\05_Daten_aufbereitet\Überprüfen_Skalierungsfaktor"
    main_folder_path =r"C:\Users\Goerner\Desktop\pedestrian_network\data\output"
    #read_and_process_file(folderpath)
    #get_weekday_with_maximum(folderpath) # für erhebungen über mehr als zwei ganze Tage           
    #find_maximum_24h_of_two_days(folderpath)       
    #filter_time_uneven_day(df_ped=None)
    
    for i, subfolder in enumerate(os.listdir(main_folder_path)):
        
        subfolder_path = os.path.join(main_folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):                               
                if filename.endswith('v1.4.gpkg'):
                    print(filename)
                    filepath = os.path.join(subfolder_path, filename)
                    geopackage  = gpd.read_file(filepath)
                    # filter geopackage
                    filenameplitted = filename.split(".")[0]
                    # Check for non-null and non-empty strings
                    mask = geopackage["Zaehlstelle"].notna() & (geopackage["Zaehlstelle"].str.strip() != "")

                    # Apply the mask to filter the GeoDataFrame
                    geopackage_filtered = geopackage[mask].copy()
                    
                    print(geopackage_filtered)
                    geopackage_filtered.to_excel(filenameplitted+".xlsx", sheet_name="Filtered Data", index=False)

    
if __name__ == "__main__":
    main()