import pandas as pd


    # Confirm if the user wants to proceed

def write_correlation_matrix(correlation_matrix, txt_output_file, excel_output_file, sheet_name="Zeitreihe"):
    
    proceed = input("Do you want to proceed(yes/no): ").strip().lower()
    
    if proceed != 'y':
        print("Operation aborted by the user.")
        return
    
    with open(txt_output_file, 'w',encoding="utf-8") as file:
        file.write(f"Correlation matrix for sheet '{sheet_name}':\n")
        file.write("Help text for pd.DataFrame.corr:\n")
        file.write("\n\n")
        file.write("Parameters\n")
        file.write("----------\n")
        file.write("method : {'pearson', 'kendall', 'spearman'} or callable\n")
        file.write("    Method of correlation:\n")
        file.write("    * pearson : standard correlation coefficient\n")
        file.write("    * kendall : Kendall Tau correlation coefficient\n")
        file.write("    * spearman : Spearman rank correlation\n")
        file.write("    * callable: callable with input two 1d ndarrays\n")
        file.write("        and returning a float. Note that the returned matrix from corr\n")
        file.write("        will have 1 along the diagonals and will be symmetric\n")
        file.write("        regardless of the callable's behavior.\n\n")
        file.write(f"{correlation_matrix}\n\n")
        
    with pd.ExcelWriter(excel_output_file) as writer:
        correlation_matrix.to_excel(writer, sheet_name=sheet_name)       
    
        
def read_excel_sheet(file_path, sheet_name):
    """
    Reads an Excel sheet from the specified file path and sheet name.

    Args:
        file_path (str): The path to the Excel file.
        sheet_name (str): The name of the sheet to read.

    Returns:
        pandas.DataFrame: The data from the specified Excel sheet, skipping the first 2 rows.
    """
    return  pd.read_excel(file_path, sheet_name=sheet_name, skiprows=2)
    

def create_correlation_matrix(dataframe):
    """
    Creates a correlation matrix based on a subset of columns from the input dataframe.

    Args:
        dataframe (pandas.DataFrame): The input dataframe containing the data.

    Returns:
        pandas.DataFrame: The correlation matrix of the selected columns.
    """
    #von 6 bis 21 Uhr
    dataframe = dataframe.iloc[25:85, 10:15]

    print(dataframe.columns)
    print(dataframe)

    return dataframe.corr()


if __name__ == "__main__":
    # Define file paths and sheet name
    file_path = r"Ganglinien_RegioStaR_v7.xlsx"
    sheet_name = "Stadtgröße"
    txt_output_file = f"data\output\correlation_output\correlation_matrix_{sheet_name}.txt"
    excel_output_file = f"data\output\correlation_output\correlation_matrix_{sheet_name}.xlsx"
    
    
    dataframe = read_excel_sheet(file_path, sheet_name)
    
    corr_matrix = create_correlation_matrix(dataframe)
    
    write_correlation_matrix(corr_matrix, txt_output_file, excel_output_file, sheet_name)
    
    
    
    