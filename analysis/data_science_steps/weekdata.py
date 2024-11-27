# %%

import pandas as pd
import os


folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\00_Datenaufbereitung\02_Mehrtageserhebung\7Tage"

cats = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
df_dic = {}

# def plot_weekdata(folder_path):


def find_dataframefilepath_with_same_basename(folderpath):
    """
    Find and group file paths with the same base name prefix in a folder.

    Args:
        folderpath (str): The path to the folder containing the files.

    Returns:
        list: A list of grouped file paths based on the same base name prefix.
    """

    zaehlstellen_list = []

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


# %%
for filename in os.listdir(folder_path):
    if filename.endswith('.csv') and not filename.startswith('~$'):

        file_path = os.path.join(folder_path, filename)
        basename = filename.split(".")[0]

        # Read the file without 'Unnamed: 0' column
        df = pd.read_csv(os.path.join(folder_path, filename),
                         usecols=lambda column: column != 'Unnamed: 0')

        df_dic[basename] = df

# %%
all_data = pd.DataFrame()

for key, _ in df_dic.items():

    # Convert the 'start time' column to datetime for easy manipulation
    df_dic[key]['start time'] = pd.to_datetime(df_dic[key]['start time'])

    # Extract the date part for grouping
    # df_dic[key]['date'] = df_dic[key]['start time'].dt.date

    # Group by date and count the number of intervals (rows) for each date
    # interval_counts = df_dic[key].groupby('date').size()

    # print(interval_counts)
    weekday_grouped = df_dic[key].groupby(
        'Weekday')['count'].sum().reset_index()
    print(weekday_grouped.head())

    summe_woche = df_dic[key]["count"].sum()

    weekday_grouped["count_anteilig"] = weekday_grouped["count"] / summe_woche
    weekday_grouped['Weekday'] = pd.Categorical(
        weekday_grouped['Weekday'], categories=cats, ordered=True)
    weekday_grouped = weekday_grouped.sort_values('Weekday')
    #weekday_grouped.to_csv(key+".csv", index=False)
    weekday_grouped_short = weekday_grouped[['Weekday', "count_anteilig"]]
    # Pivot the DataFrame to make 'Weekday' the columns and 'count' the values
    print(weekday_grouped_short)
    df_pivot = weekday_grouped_short.set_index('Weekday').T
    
    # Set the file name as the index of the pivoted DataFrame
    df_pivot.index = [key]
    all_data = pd.concat([all_data, df_pivot])

#all_data.to_csv("wochenzählung.csv", index=True)

# %%

folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\13_Wochenanalyse\02_Mehrtageserhebung\7Tage\Aufbereitet"

grouped_data = find_dataframefilepath_with_same_basename(folder_path)

corr_dic = {}
list_of_zaehlstellen_dic =[]
for group in grouped_data:
    df1 = pd.read_csv(group[0])
    df2 = pd.read_csv(group[1])

    filename1 = os.path.basename(group[0])
    filename2 = os.path.basename(group[1])
    basename1 = filename1.split(".")[0]
    basename2 = filename2.split(".")[1]   
    
    corr_weekdays = df1["count_anteilig"].corr(df2["count_anteilig"])
    # print(df1.head())
    # print(df2.head())
    n1 = df1["count"].sum()
    n2 = df2["count"].sum()
    dic = {"zaehlstelllen_seite1":basename1,  "zaehlstelllen_seite2": basename2 
            , "corr_Wochentag": corr_weekdays,"n1 zaehlstelllen_seite1":n1,"n2 zaehlstelllen_seite2": n2, "Summe": n1+n2 }
    
    list_of_zaehlstellen_dic.append(dic)
df = pd.DataFrame(list_of_zaehlstellen_dic)
df.to_csv("corr_wochengang.csv")

# %%
folder_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\13_Wochenanalyse\02_Mehrtageserhebung\7Tage\Aufbereitet"

grouped_data = find_dataframefilepath_with_same_basename(folder_path)

all_data = pd.DataFrame()
#mo bis fr
for group in grouped_data:
    df1 = pd.read_csv(group[0])
    df2 = pd.read_csv(group[1])
    filename1 = os.path.basename(group[0])
    filename2 = os.path.basename(group[1])
    basename1 = filename1.split("_")[0]

    df1["count"] = (df1["count"] + df2["count"])
    
    df1 = df1[~df1["Weekday"].isin(['Saturday', 'Sunday'])]
    
    summe_woche = df1["count"].sum()
    df1["count_anteilig"] = df1["count"] / summe_woche
    
    df_pivot = weekday_grouped_short.set_index('Weekday').T
    df_pivot.index = [basename1]
    
    df1[["Weekday", "count_anteilig"]].to_csv(basename1+"_mo_fr"+".csv")
    
    all_data = pd.concat([all_data, df_pivot])   
    print(df1["count_anteilig"].sum())



    
#all_data.to_csv("wochenzählung_mo_fr.csv", index=True)
# %%

