import pandas as pd
from correlation_ganglinien import write_correlation_matrix
import seaborn as sns
import matplotlib.pyplot as plt

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
    file_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\Matrix_Zählstellen_kategorisiert2.xlsx"
    
    
    #txt_output_file = f"data\output\correlation_output\correlation_matrix_{sheet_name}.txt"
    #excel_output_file = f"data\output\correlation_output\correlation_matrix_{sheet_name}.xlsx"
    
    
    dataframe = read_excel_sheet(file_path)
    print(dataframe.iloc[:,3:12])
    dataframe = dataframe.iloc[:,3:12]
    #df_filtered = dataframe[~dataframe.isin([2500]).any(axis=1)]
    
    ranked_df = dataframe.rank()
    print(ranked_df)
    
    # Columns to reverse
    columns_to_reverse = ['Entfernung Hochschule', 'Entfernung Schule','Entfernung Bushaltestelle','EntfernungStraßenbahnhaltestelle', 'Entfernung SPNV-Haltestelle']

    # Reverse the ranks only for selected columns
    reversed_ranks = ranked_df.copy()  # Copy the ranked DataFrame
    # small distance has high rank, big distance has low rank
    for column in columns_to_reverse:
        reversed_ranks[column] = ranked_df[column].max() + 1 - ranked_df[column]
        

    
    # txt_output_file = "Matrix_Variablen_reversed_ranks.txt"
    # excel_output_file = "Matrix_Variablen_reversed_ranks.xlsx"    
    corr_matrix = reversed_ranks.corr(method="spearman")
    #corr_matrix = ranked_df.corr(method="spearman")
    
    plt.figure(figsize=(12, 12))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Korrelationsmatrix')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()  # Adjust layout to make room for label

    # Adjust subplot parameters to give more space to the labels
    plt.subplots_adjust(bottom=0.3)  # Increase bottom margin
    plt.show()
    
    sns.pairplot(data=dataframe)
    plt.show()
    
    # write_correlation_matrix(corr_matrix, txt_output_file, excel_output_file)