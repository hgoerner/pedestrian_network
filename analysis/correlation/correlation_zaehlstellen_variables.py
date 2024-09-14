import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Confirm if the user wants to proceed
def read_excel_sheet(file_path):
    """
    Reads an Excel sheet from the specified file path and sheet name.

    Args:
        file_path (str): The path to the Excel file.
        sheet_name (str): The name of the sheet to read.

    Returns:
        pandas.DataFrame: The data from the specified Excel sheet, skipping the first 2 rows.
    """
    return  pd.read_excel(file_path)
    

if __name__ == "__main__":
    # Define file paths and sheet name
    file_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\Matrix_Zählstellen_kategorisiert_plausibel_20240715.xlsx"
    
    
    #txt_output_file = f"data\output\correlation_output\correlation_matrix_{sheet_name}.txt"
    #excel_output_file = f"data\output\correlation_output\correlation_matrix_{sheet_name}.xlsx"
    
    
    dataframe = read_excel_sheet(file_path)
    dataframe = dataframe.iloc[:,3:12]
    print(dataframe.columns)
    
    #df_filtered = dataframe[~dataframe.isin([2500]).any(axis=1)]
    #print(df_filtered)
    
    ranked_df = dataframe.rank()
    
    # Columns to reverse
    columns_to_reverse = ['Entfernung Hochschule', 'Entfernung Schule','Entfernung Bushaltestelle','Entfernung Straßenbahnhaltestelle', 'Entfernung SPNV-Haltestelle']

    # Reverse the ranks only for selected columns
    reversed_ranks = ranked_df.copy()  # Copy the ranked DataFrame
    # small distance has high rank, big distance has low rank
    for column in columns_to_reverse:
        reversed_ranks[column] = ranked_df[column].max() + 1 - ranked_df[column]
       
    # txt_output_file = "Matrix_Variablen_reversed_ranks.txt"
    # excel_output_file = "Matrix_Variablen_reversed_ranks.xlsx"    
    corr_matrix = reversed_ranks.corr(method="spearman", )
    #corr_matrix = ranked_df.corr(method="spearman")
    #Rename the first row index name and the first column name to " "
    corr_matrix.index = [" "] + corr_matrix.index.tolist()[1:]
    corr_matrix.columns = corr_matrix.columns.tolist()[:-1] + [" "]
    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    
    plt.figure(figsize=(14, 14))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', mask=mask, linewidths=0.5, vmin=-1, vmax=1, 
                     cbar_kws={"shrink": 0.5, "ticks": np.linspace(-1, 1, 11)}, annot_kws={"size": 14})
    plt.title('Korrelationsmatrix Variablen der Zählstellen', fontsize=20)
    plt.xticks(rotation=45, ha="right", fontsize=16)
    plt.yticks(fontsize=16)
    plt.tight_layout()  # Adjust layout to make room for label
        # Move the color bar to the left
    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.set_ticks_position('right')
    cbar.ax.yaxis.set_label_position('right')

    # Adjust the position of the title and bottom margin
    plt.subplots_adjust(top=0.9, bottom=0.3, right=1)  # Adjust 'bottom' to increase margin for x-axis labels

    plt.show()
    
   #sns.pairplot(data=dataframe)
   #plt.show()
    
   #write_correlation_matrix(corr_matrix, txt_output_file, excel_output_file)