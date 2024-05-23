import pandas as pd


    # Confirm if the user wants to proceed
def abort_option():
    proceed = input("Do you want to proceed(yes/no): ").strip().lower()
    
    if proceed != 'y':
        print("Operation aborted by the user.")
        return


def wirte_correlation_matrix(correlation_matrix, txt_output_file, excel_output_file, sheet_name):
    with open(txt_output_file, 'w',encoding="utf-8") as file:
        file.write(f"Correlation matrix for sheet '{sheet_name}':\n")
        file.write(help(pd.DataFrame.corr)"\n")
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
    dataframe = dataframe.iloc[:, 10:15]

    print(dataframe.columns)
    print(dataframe)

    abort_option()

    return dataframe.corr()


if __name__ == "__main__":
    # Define file paths and sheet name
    file_path = r"Ganglinien_RegioStaR_v7.xlsx"
    sheet_name = "Tätigkeit"
    txt_output_file = f"correlation_matrix_{sheet_name}.txt"
    excel_output_file = f"correlation_matrix_{sheet_name}.xlsx"
    
    
    dataframe = read_excel_sheet(file_path, sheet_name)
    
    corr_matrix = create_correlation_matrix(dataframe)
    
    wirte_correlation_matrix(corr_matrix, txt_output_file, excel_output_file, sheet_name)
    
    
    
    