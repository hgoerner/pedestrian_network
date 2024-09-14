import os
from matplotlib.colors import ListedColormap
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.lines import Line2D
import numpy as np

#code berechnet gleitenden mittlelwert
#sortiert den tag nach zeit

def interpolation_nan_values(dataframe):
    """
    Interpolates NaN values in a DataFrame representing pedestrian count data.
    
    Args:
        dataframe (pandas.DataFrame): The DataFrame containing pedestrian count data.
        
    Returns:
        pandas.DataFrame: The DataFrame with interpolated NaN values.
    """    
    #a dataframe needs to be over 24hours
    expected_times = pd.date_range(start='00:00', end='23:45', freq='15min').strftime('%H:%M')
    
    dataframe = dataframe.infer_objects(copy=False)
    
    # Convert 'start time' to time and set as index
    #dataframe['start time(ohne Tag)'] = pd.to_datetime(dataframe['start occurrence time'], format='%H:%M').dt.strftime('%H:%M')
    dataframe.set_index('start time(ohne Tag)', inplace=True)

    #never change this!
    dataframe = dataframe.reindex(expected_times)
    # Interpolate NaN values if reindex was created new rows
    dataframe.interpolate(inplace=True)
    dataframe.reset_index(inplace=True)
    dataframe.rename(columns={'index': 'start time(ohne Tag)'}, inplace=True)    

    return dataframe

def cut_nighttime_from_dataframe(dataframe):
    """get hours from 6 to 22 o clock

    Args:
        dataframe (_type_): _description_

    Returns:
        pd.dataframe: dataframe
    """

    return dataframe.iloc[24:88]


def gleitende_werte(df, column_input, colum_output, mean=True, sum=False):
    previous_2 = df[column_input].shift(2) 
    previous_1 = df[column_input].shift(1)  
    current = df[column_input] 
    next_1 = df[column_input].shift(-1) 
    
    # Combine them into a DataFrame - 2 davor - 1 danach
    rolling_df = pd.DataFrame({'previous_2': previous_2, 'previous_1': previous_1, 'current': current, 'next_1': next_1})
    if mean:
        df[colum_output] = rolling_df.mean(axis=1)
    if sum:
        df[colum_output] = rolling_df.sum(axis=1)
        
    #first_df.drop('gleitender_Mittelwert', axis=1, inplace=True)    
                
    return df

def zaehlstellenseiten_richtungen_zusammenfassen(folderpath):
    """
    Reads a CSV file, processes it, and returns the processed DataFrame.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The processed DataFrame.
        str: The base filename.
        int: The total count of pedestrians.
    """
    for filename in os.listdir(folderpath):
        if filename.endswith('.csv') and not filename.startswith('~$'):
            filepath = os.path.join(folderpath, filename)
            base_filename = os.path.splitext(os.path.basename(filepath))[0]
            
            df_ped = pd.read_csv(filepath)  

            #df_ped = interpolation_nan_values(df_ped)
            # Extract filename without extension
            base_filename = os.path.splitext(os.path.basename(filepath))[0]
            base_filename = base_filename.split('.')[0]
            # Convert 'start time' to datetime and extract the time component
            print(df_ped)
            columns_to_check = ['end occurrence date', "end occurrence time"]
            
            if  "start time(ohne Tag)" not in df_ped.columns:
            # Check if both columns exist
                if all(column in df_ped.columns for column in columns_to_check):
                    print("No missing columns")
                else:
                    print("One or both columns are missing.")
                    print(base_filename)
                    df_ped['end occurrence date'] = pd.to_datetime(df_ped['end time']).dt.date
                    df_ped["start occurrence time"] = pd.to_datetime(df_ped['start time'], format="%H:%M:%S").dt.time
                    df_ped["end occurrence time"] = pd.to_datetime(df_ped['start occurrence time'], format="%H:%M:%S").dt.time
                df_ped['start time(ohne Tag)'] = pd.to_datetime(df_ped['start occurrence time'], format="%H:%M:%S").dt.strftime('%H:%M')
               
            # only if otc is better than gt 

            #df_ped.drop('gleitender_Mittelwert', axis=1, inplace=True)      
            #df_ped.rename(columns={'count': 'count_scaled'}, inplace=True)     
            #df_ped.rename(columns={'count_scaled': 'count'}, inplace=True)   
            # Calculate the proportion of counts
                      

            # Group by 'start time(ohne Tag)' and sum the 'count_anteilig' and 'count'
            df_grouped = df_ped.groupby('start time(ohne Tag)').agg({'count': 'sum' }).reset_index()
            
            #sort by time
            df_grouped.sort_values(by='start time(ohne Tag)', inplace=True)
            total_count = df_grouped["count"].sum()
            df_grouped["count_anteilig"] = df_grouped["count"] / total_count
            # Calculate rolling mean with window size of 4 (old version)
            #df_grouped['gleitender_Mittelwert'] = df_grouped['count_anteilig'].rolling(window=4, min_periods=1).mean()
            
            if len(df_grouped) < 96:
                print("interpolation is performed") 
                df_grouped = interpolation_nan_values(df_grouped)
            
            # Manually adjust the first three values of 'gleitender_Mittelwert'
            # if len(df_grouped) >= 4:
            #     df_grouped.at[0, 'gleitender_Mittelwert'] = (df_grouped['count_anteilig'][-3:].sum() + df_grouped['count_anteilig'][:2].sum()) / 4
            #     df_grouped.at[1, 'gleitender_Mittelwert'] = (df_grouped['count_anteilig'][-2:].sum() + df_grouped['count_anteilig'][:3].sum()) / 4
            #     df_grouped.at[2, 'gleitender_Mittelwert'] = (df_grouped['count_anteilig'][-1:].sum() + df_grouped['count_anteilig'][:4].sum()) / 4
            # if len(df_grouped) < 96:
            #     print("interpolation is performed") 
            #     df_grouped = interpolation_nan_values(df_grouped)               
            
            df = gleitende_werte(df_grouped, "count_anteilig", "gleitender_MW_15min", mean=True, sum=False)
            # #df = gleitende_werte(df_grouped, "count_anteilig", "gleitender_Stundenwert", mean=False, sum=True)
            df["gleitender_Stundenwert_aus_MW"] = df["gleitender_MW_15min"]*4
            
            print(df)
            df.to_csv(base_filename+".csv",index=False)


    #return df_grouped, base_filename, total_count


def zaehlstellenseiten_zusammenfassen(list_of_dataframe_filepaths):
    """
    Combines data from pairs of CSV files representing pedestrian counts at different locations.

    Args:
        list_of_dataframe_filepaths (list): A list of file paths to pairs of CSV files.

    Returns:
        None
    """

    for pairwise_filepaths in list_of_dataframe_filepaths:
        #print(pairwise_filepaths)
        filename1 = os.path.basename(pairwise_filepaths[0])
        zaehlstelle = filename1.split('_')[0]
        zaehlstellen_seite1 = filename1.split('.')[0]
        
        # Define the expected range of time points
        #expected_times = pd.date_range(start='00:00', end='23:45', freq='15min').strftime('%H:%M')
        
        df_ped1 = pd.read_csv(pairwise_filepaths[0])
        
        # Convert 'start time' to time and set as index
        df_ped1['start time(ohne Tag)'] = pd.to_datetime(df_ped1['start time(ohne Tag)'], format='%H:%M').dt.strftime('%H:%M')
        #df_ped1.set_index('start time(ohne Tag)', inplace=True)

        filename2 = os.path.basename(pairwise_filepaths[1])
        zaehlstellen_seite2 = filename2.split('.')[0]
        
        df_ped2 = pd.read_csv(pairwise_filepaths[1])
        
        
        # Convert 'start time' to time and set as index
        df_ped2['start time(ohne Tag)'] = pd.to_datetime(df_ped2['start time(ohne Tag)'], format='%H:%M').dt.strftime('%H:%M')
        #df_ped2.set_index('start time(ohne Tag)', inplace=True)
        print(df_ped2.head())

        #aufsummieren der Seiten je Intervall
        df_ped1["count"] = df_ped1["count"] +df_ped2["count"]
        
        total_n = df_ped1['count'].sum()
        df_ped1["count_anteilig"] = df_ped1["count"] / total_n
        print(df_ped1["count_anteilig"].sum())
        print(df_ped1.head())

        
        df = gleitende_werte(df_ped1, "count_anteilig", "gleitender_MW_15min", mean=True, sum=False)
        df["gleitender_Stundenwert_aus_MW"] = df["gleitender_MW_15min"]*4

        # Manually adjust the first three values of 'gleitender_Mittelwert'

        print(df)
        df.to_csv(zaehlstelle+"_Seiten_zusammengefasst"+".csv", index=False )

        #return first_df, zaehlstelle        

def arithmethischer_mittelwert_aus_zaehlstellen(folderpath):
    """
    Calculates the average values from multiple CSV files containing pedestrian count data.
    
    Args:
        folderpath (str): The path to the folder containing the CSV files.
        
    Returns:
        pandas.DataFrame: A DataFrame with the calculated average values.
    """    
    list_of_filepaths  = []
    for filename in os.listdir(folderpath):

        if filename.endswith('.csv') and not filename.startswith('~$'):
            filepath = os.path.join(folderpath, filename)
            list_of_filepaths.append(filepath)
            
    # Define the expected range of time points
    expected_times = pd.date_range(start='00:00', end='23:45', freq='15min').strftime('%H:%M')
            
    # Load the existing DataFrame from the first file
    first_df = pd.read_csv(list_of_filepaths[0], usecols=lambda column: column != 'Unnamed: 0')
    # interpolate initial 
    #first_df.interpolate(inplace=True)
    # Convert 'start time' to time and set as index
    first_df['start time(ohne Tag)'] = pd.to_datetime(first_df['start time(ohne Tag)'], format='%H:%M').dt.strftime('%H:%M')
    # first_df.set_index('start time(ohne Tag)', inplace=True)
    # first_df = first_df.reindex(expected_times)
    # first_df = first_df.infer_objects(copy=False)
    # interpolate if reindex created new rows
    #first_df.interpolate(inplace=True)
    
    #reset the index again
    #first_df.reset_index(inplace=True)
    first_df.rename(columns={'index': 'start time(ohne Tag)'}, inplace=True)
    
    number_of_csv_files = len(list_of_filepaths)
    for filepath in list_of_filepaths[1:]:
        
        # add columns to the first df in the folder
        df = pd.read_csv(filepath,usecols=lambda column: column != 'Unnamed: 0')
        # df = df.infer_objects(copy=False)
        # # interpolate initial 
        # df.interpolate(inplace=True)
        
        # Convert 'start time' to time and set as index
        df['start time(ohne Tag)'] = pd.to_datetime(df['start time(ohne Tag)'], format='%H:%M').dt.strftime('%H:%M')
        #df.set_index('start time(ohne Tag)', inplace=True)

        # #never change this! 
        # df = df.reindex(expected_times)
        # # Interpolate NaN values if reindex was created new rows
        # df.interpolate(inplace=True)
        # df.reset_index(inplace=True)
        # df.rename(columns={'index': 'start time(ohne Tag)'}, inplace=True)
        
        #aufsummieren der Spalten
        first_df["count"] += df["count"]
        first_df["gleitender_Stundenwert_aus_MW"] += df["gleitender_Stundenwert_aus_MW"]
        first_df["gleitender_MW_15min"] += df["gleitender_MW_15min"]
    # Mittelwert bestimmen
    first_df["gleitender_Stundenwert_aus_MW"] = first_df["gleitender_Stundenwert_aus_MW"] / number_of_csv_files
    first_df["gleitender_MW_15min"] = first_df["gleitender_MW_15min"] / number_of_csv_files
    first_df["count"] = first_df["count"] / number_of_csv_files
    first_df["n"] = number_of_csv_files
    total_n = first_df['count'].sum()
    
    #Anteil neu bestimmen
    first_df["count_anteilig"] = first_df["count"] / total_n
    
    print(number_of_csv_files)
   
    return first_df

def gewichteteter_mittelwert_aus_zaehlstellen(folderpath):
    

    list_of_filepaths  = []
    for filename in os.listdir(folderpath):

        if filename.endswith('.csv') and not filename.startswith('~$'):
            filepath = os.path.join(folderpath, filename)
            list_of_filepaths.append(filepath)
            
    # Define the expected range of time points   
    expected_times = pd.date_range(start='00:00', end='23:45', freq='15min').strftime('%H:%M')       
    
    # Load the existing DataFrame from the first file
    first_df = pd.read_csv(list_of_filepaths[0], usecols=lambda column: column != 'Unnamed: 0')
    first_df = first_df.infer_objects(copy=False)
    first_df.interpolate(inplace=True)

    # Convert 'start time' to time and set as index
    first_df['start time(ohne Tag)'] = pd.to_datetime(first_df['start time(ohne Tag)'], format='%H:%M').dt.strftime('%H:%M')
    first_df.set_index('start time(ohne Tag)', inplace=True)
    first_df = first_df.reindex(expected_times)
    
    # interpolate if reindex created new rows
    first_df.interpolate(inplace=True)
    
    #reset the index again
    first_df.reset_index(inplace=True)
    first_df.rename(columns={'index': 'start time(ohne Tag)'}, inplace=True)
    first_df['count_anteilig'] = first_df['count_anteilig'] * first_df['count']
       
    for filepath in list_of_filepaths[1:]:
        # add columns to the first df in the folder
        df = pd.read_csv(filepath,usecols=lambda column: column != 'Unnamed: 0')
        
        # Convert object columns to inferred types
        df = df.infer_objects(copy=False)
        # interpolate initial
        df.interpolate(inplace=True)
        
        # Convert 'start time' to time and set as index
        df['start time(ohne Tag)'] = pd.to_datetime(df['start time(ohne Tag)'], format='%H:%M').dt.strftime('%H:%M')
        df.set_index('start time(ohne Tag)', inplace=True)

        #never change this!
        df = df.reindex(expected_times)
        # Interpolate NaN values if reindex was created new rows
        df.interpolate(inplace=True)
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'start time(ohne Tag)'}, inplace=True)
        
        # übern Bruchstrich       
        first_df['count_anteilig'] += (df['count_anteilig'] * df['count'])
        #aufsummieren (unter dem Bruchstrich)
        first_df['count'] += df['count']
     
    #overwrite column 'gleitendender Mittelwert for easier plotting    
    first_df['gewichteter_Mittelwert'] = first_df['count_anteilig'] / first_df["count"]
    first_df.fillna(0, inplace=True)
    #gleitender Mittelwert
    first_df["gleitender_gewichteter_Mittelwert"] = first_df['gewichteter_Mittelwert'].rolling(window=4, min_periods=1).mean()
        
    # Manually adjust the first three values of 'gleitender_Mittelwert'
    if len(first_df) >= 4:
        first_df.at[0, 'gleitender_gewichteter_Mittelwert'] = (first_df['gewichteter_Mittelwert'][-3:].sum() + first_df['gewichteter_Mittelwert'][:2].sum()) / 4
        first_df.at[1, 'gleitender_gewichteter_Mittelwert'] = (first_df['gewichteter_Mittelwert'][-2:].sum() + first_df['gewichteter_Mittelwert'][:3].sum()) / 4
        first_df.at[2, 'gleitender_gewichteter_Mittelwert'] = (first_df['gewichteter_Mittelwert'][-1:].sum() + first_df['gewichteter_Mittelwert'][:4].sum()) / 4        
    return first_df

def gleitenden_stundenwerte_aus_zaehlstellen(folderpath):
    
    list_of_filepaths  = []
    for filename in os.listdir(folderpath):

        if filename.endswith('.csv') and not filename.startswith('~$'):
            filepath = os.path.join(folderpath, filename)
            list_of_filepaths.append(filepath)
       
    number_of_csv_files = len(list_of_filepaths)        
    # Define the expected range of time points   
    #expected_times = pd.date_range(start='00:00', end='23:45', freq='15min').strftime('%H:%M')       
    
    # Load the existing DataFrame from the first file
    first_df = pd.read_csv(list_of_filepaths[0], usecols=lambda column: column != 'Unnamed: 0')
    #print(first_df.head())
    # Shift the series to get the previous and next rows
    previous_2 = first_df['count_anteilig'].shift(2) 
    previous_1 = first_df['count_anteilig'].shift(1)  
    current = first_df['count_anteilig'] 
    next_1 = first_df['count_anteilig'].shift(-1) 
    next_2 = first_df['count_anteilig'].shift(-2) 
    #fill nans with true values
    
       
    for filepath in list_of_filepaths[1:]:
        # add columns to the first df in the folder
        df = pd.read_csv(filepath,usecols=lambda column: column != 'Unnamed: 0')
        first_df['count'] += df['count']
        first_df['count_anteilig'] += df['count_anteilig'] 
        print(filepath)
        print(len(df))


        # aufsummieren der anteile
        previous_2 += df['count_anteilig'].shift(2)
        previous_1 += df['count_anteilig'].shift(1)
        current += df['count_anteilig']
        next_1 += df['count_anteilig'].shift(-1)
        

    # Mittelwerte für alle Spalten
    previous_2 = previous_2 / number_of_csv_files
    previous_1 = previous_1 / number_of_csv_files
    current = current / number_of_csv_files
    next_1 = next_1 / number_of_csv_files
    next_2 = next_2 / number_of_csv_files
    
    first_df['count_anteilig'] =  first_df['count_anteilig'] / number_of_csv_files 
    first_df['count'] =  first_df['count'] / number_of_csv_files
    
    
    # Combine them into a DataFrame - 2 davor - 1 danach
    rolling_df = pd.DataFrame({'previous_2': previous_2, 'previous_1': previous_1, 'current': current, 'next_1': next_1})
    
    # Combine them into a DataFrame - 1 davor - 2 danach 
    #rolling_df = pd.DataFrame({'previous_1': previous_1, 'current': current, 'next_1': next_1, 'next_2': next_2})
                                                                                                        
    # rolling_df the mean across these 4 columns, ignoring NaNs
    # Summe da stundenwerte    
    first_df['gleitender_Stundenwert'] = rolling_df.sum(axis=1)
    
    #first_df.drop('gleitender_Mittelwert', axis=1, inplace=True)    
                
    return first_df

def find_dataframefilepath_with_same_basename(folderpath):
    """
    Find and group file paths with the same base name prefix in a folder.

    Args:
        folderpath (str): The path to the folder containing the files.

    Returns:
        list: A list of grouped file paths based on the same base name prefix.
    """
    
    zaehlstellen_list =  []
    
    for filename in os.listdir(folderpath):
        if filename.endswith('.csv') and not filename.startswith('~$'):
            filepath = os.path.join(folderpath, filename)
            base_filename = os.path.splitext(os.path.basename(filepath))[0]
            zaehlstelle = base_filename.split('_')[0]
            zaehlstellen_list.append((zaehlstelle, filepath))
    # Sort the list by prefix to group them
    zaehlstellen_list.sort(key=lambda x: x[0])
    
    # Group files with the same prefix
    grouped_zaehlstelle = []
    current_group = []
    last_zaehlstelle = None
    
    for zaehlstelle, filepath in zaehlstellen_list:
        if zaehlstelle != last_zaehlstelle:
            if current_group:
                grouped_zaehlstelle.append(current_group)
            current_group = [filepath]
            last_zaehlstelle = zaehlstelle
        else:
            current_group.append(filepath)
    
    # Add the last group if not empty
    if current_group:
        grouped_zaehlstelle.append(current_group)
    
    return grouped_zaehlstelle


def main():
    
    main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\10_Typisierung\Clusterung1"
    #group_by_time(main_folder_path)
    #main_folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\01_Zählstellenseiten_Korrelation\00_Zaehlstellenseiten_n1000\nachgeliefert"
    #zaehlstellenseiten_richtungen_zusammenfassen(main_folder_path)
    
    #arithmethischer_mittelwert_aus_zaehlstellen(main_folder_path)
    # for filename in os.listdir(main_folder_path):

    #     if filename.endswith('.csv') and not filename.startswith('~$'):
    #         filepath = os.path.join(main_folder_path, filename)
    #         df = pd.read_csv(filepath, index=False)
    #         print(df)
        
    #list_of_grouped_filepaths = find_dataframefilepath_with_same_basename(main_folder_path)
    #zaehlstellenseiten_zusammenfassen(list_of_grouped_filepaths)
    #print(list_of_grouped_filepaths)
    #gleitender_df_stundenwerte = gleitenden_stundenwerte_aus_zaehlstellen(main_folder_path)
    #gewichtet_gleitender_df = gewichteteter_mittelwert_aus_zaehlstellen(folderpath)
    #gleitender_df_stundenwerte.to_csv("XX_gleitender_Stundenwert_aller_Zs_1-2.csv", index=False)
    
    #Loop through each subfolder
    for i, subfolder in enumerate(os.listdir(main_folder_path)):
        
        subfolder_path = os.path.join(main_folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            print(subfolder_path)
            lage = subfolder.split(" ")[-1]
            print(lage)
            #df = gewichteteter_mittelwert_aus_zaehlstellen(subfolder_path)
            #df = gleitenden_stundenwerte_aus_zaehlstellen(subfolder_path)
            df = arithmethischer_mittelwert_aus_zaehlstellen(subfolder_path)
            df.to_csv(subfolder+"_gleitender_Stundenwert_aller_zs.csv", index=False)

# Entry point of the scrip
if __name__ == "__main__":
    main()
    
    