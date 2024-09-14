import os
import pandas as pd

def cut_nighttime_from_dataframe(dataframe):
    """get hours from 6 to 22 o clock

    Args:
        dataframe (_type_): _description_

    Returns:
        pd.dataframe: dataframe
    """

    return dataframe.iloc[24:88]



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

def get_correlation_coefficent(list_of_dataframe_filepaths):
    """
    Calculate the correlation coefficient between two sets of dataframes.

    Args:
        list_of_dataframe_filepaths (list): A list of file paths to the dataframes.

    Returns:
        list: A list of dictionaries containing correlation coefficients and other data.
    """
    
    
    list_of_zaehlstellen_dic = []
    for pairwise_filepaths in list_of_dataframe_filepaths:
        #print(pairwise_filepaths)
        filename1 = os.path.basename(pairwise_filepaths[0])
        zaehlstelle = filename1.split('_')[0]
        zaehlstellen_seite1 = filename1.split('.')[0]
        
        df_ped1 = pd.read_csv(pairwise_filepaths[0])
        df_ped1 = cut_nighttime_from_dataframe(df_ped1)
        n1 = df_ped1["count"].sum()

        filename2 = os.path.basename(pairwise_filepaths[1])
        zaehlstellen_seite2 = filename2.split('.')[0]
        
        df_ped2 = pd.read_csv(pairwise_filepaths[1])
        df_ped2 = cut_nighttime_from_dataframe(df_ped2)
        n2 = df_ped2["count"].sum()
        df_new = pd.concat([df_ped1["start time(ohne Tag)"],df_ped1["gleitender_Mittelwert"], df_ped2["gleitender_Mittelwert"]], axis=1)
        
        korrelation_koefficient = df_ped1["gleitender_Mittelwert"].corr(df_ped2["gleitender_Mittelwert"])
        #print(n1, n2, df_new, korrelation_koefficient)
        
        dic = {"zaehlstelle": zaehlstelle , "zaehlstelllen_seite1":zaehlstellen_seite1,  "zaehlstelllen_seite2": zaehlstellen_seite2 
         , "Korrelationskoeffizent": korrelation_koefficient, "n1 zaehlstelllen_seite1":n1,"n2 zaehlstelllen_seite2": n2, "Summe": n1+n2 }

        list_of_zaehlstellen_dic.append(dic)
    return list_of_zaehlstellen_dic
        
def main():
    folderpath =r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\00_Datenaufbereitung\05_Daten_aufbereitet\04_Richtungen_aufsummiert\unskaliert"

    list_of_grouped_filepaths = find_dataframefilepath_with_same_basename(folderpath)
    
    
    list_of_zaehlstellen_dic = get_correlation_coefficent(list_of_grouped_filepaths)
    #print(list_of_zaehlstellen_dic)
    
    # Creating the DataFrame
    df = pd.DataFrame(list_of_zaehlstellen_dic)
    df.to_excel("zaehlstellenseiten_korrelation2008.xlsx", index=False, engine='openpyxl')
    print(df)
    
if __name__ == "__main__":
    main() 
