import os
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


min_n = 1600

def read_excel(filepath):
    df = pd.read_excel(filepath)
    
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    base_filename1 = base_filename.split(' ')[0]
    base_filename_n = base_filename.split(' ')[1]
    
    
    return df, base_filename1, base_filename_n

def return_and_process_dataframes(folderpath, check_min:bool=True, excelname:str=None ):
    """
    Reads and processes CSV files in the specified folder path, returning a list of dataframes and corresponding basenames.

    Args:
        folderpath: The path to the folder containing the CSV files.

    Returns:
        A tuple containing a list of dataframes and a list of basenames.
    """
    list_of_columns = []
    new_column_names = []
    for filename in os.listdir(folderpath):

        if filename.endswith('.xlsx') and not filename.startswith('~$'):
            filepath = os.path.join(folderpath, filename)
            
            df, base_filename1, base_filename_n = read_excel(filepath)

            print(base_filename1, base_filename_n)
            
            match = re.search(r'\d+', base_filename_n)
            n = int(match.group())
            if check_min:
                if n >= min_n:

                    df.rename(columns={'gleitender_Mittelwert': base_filename1 +" "+ base_filename_n}, inplace=True)
                    print(df[base_filename1 +" "+ base_filename_n])

                    list_of_columns.append(df[base_filename1 +" "+ base_filename_n])
                    new_column_names.append(base_filename1 +" "+ base_filename_n)
                
            else:
                    df.rename(columns={'gleitender_Mittelwert': base_filename1 +" "+ base_filename_n}, inplace=True)
                    print(df[base_filename1 +" "+ base_filename_n])

                    list_of_columns.append(df[base_filename1 +" "+ base_filename_n])
                    new_column_names.append(base_filename1 +" "+ base_filename_n)
            

    # Concatenate all the columns into a new DataFrame
    corr_df = pd.concat(list_of_columns, ignore_index=True, axis=1)
    corr_df.columns = new_column_names
  
    # Display the new DataFrame
    corr_df.to_excel(excelname+".xlsx", float_format='%.4f')
    
def create_corr_plot(folderpath):
    """
    Creates a correlation plot based on Excel files in the specified folder path.

    Args:
        folderpath: The path to the folder containing Excel files.

    Returns:
        None
    """
    for filename in os.listdir(folderpath):
        if filename.endswith('.xlsx') and not filename.startswith('~$'):
            filepath = os.path.join(folderpath, filename)
            corr_df = pd.read_excel(filepath, index_col=0)     
            
            corr_df = corr_df.iloc[24:88]   
           # print(corr_df)
            corr_matrix = corr_df.corr()
            corr_matrix = corr_matrix.round(2)
            
            #print(corr_matrix)
            
            corr_matrix.index = [" "] + corr_matrix.index.tolist()[1:]
            corr_matrix.columns = corr_matrix.columns.tolist()[:-1] + [" "]
            # Create a mask for the upper triangle
            mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
            
            plt.figure(figsize=(14, 14))
            ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', mask=mask, linewidths=0.5, vmin=-1, vmax=1, 
                            cbar_kws={"shrink": 0.5, "ticks": np.linspace(-1, 1, 11)}, annot_kws={"size": 8})
            plt.title('Korrelationsmatrix Anteil Fußverkehr je Zeitscheibe \n Umfeldkategorie PH-EN', fontsize=20)
            plt.xticks(rotation=45, ha="right", fontsize=12)
            plt.yticks(fontsize=12, rotation=0)
            plt.tight_layout()  # Adjust layout to make room for label
            # Move the color bar to the left
            cbar = ax.collections[0].colorbar
            cbar.ax.yaxis.set_ticks_position('right')
            cbar.ax.yaxis.set_label_position('right')

            # Adjust the position of the title and bottom margin
            plt.subplots_adjust(top=0.9, bottom=0.3, right=1)  # Adjust 'bottom' to increase margin for x-axis labels

            plt.show()
                    
                
 
def main():
    #folderpath =r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\01_Umfeld_Kategorie\PH_EN\excel_daten"
    #return_and_process_dataframes(folderpath, False, "corr_gesamt")
    
    #folderpath_corr = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\01_Umfeld_Kategorie\PH_EH\correlation"
    #create correlation plot
    #create_corr_plot(folderpath_corr)

if __name__ == "__main__":
    main()
    
    
    