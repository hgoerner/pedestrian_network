import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
import statsmodels.api as sm
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
import os
import re

def convert_columns(df):
    """
    Convert columns to appropriate types:
    - Object columns (strings) to categorical
    - Categorical columns to dummy variables (one-hot encoding)
    - Handle missing values
    """
    for col in df.columns:
        if df[col].dtype == 'object':  # Convert string/object columns to categorical
            df[col] = df[col].astype('category')

    return df

def calculate_vif(df):# Calculate VIF for each feature
    X = df.dropna()  # Ensure there are no NaN values
    X = sm.add_constant(X)  # Add cons tant term
    vif = pd.DataFrame()
    vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif["features"] = X.columns

    print(vif)
    
    

def multinomiale_regression_model(dependent_col_index, df, ref_category, independent_col_index, results_list ):
    try:

        # Convert the dependent variable to categorical
        # Convert categorical variables to dummy variables if any
        df[df.columns[dependent_col_index]] = df[df.columns[dependent_col_index]].astype('category')
        #Bdf[df.columns[independent_col_index]] = df[df.columns[independent_col_index]].astype('category')
        # Ensure all columns are numeric

                
        # Define the dependent variable (y)
        y = df[df.columns[dependent_col_index]]
        # Define the independent variables (X)
        # for single features

        #X = df[df.columns[independent_col_index]]
        
        #for multiple features
        # Example of dynamically chosen column indices
        X = df.iloc[:, independent_col_index] 
        # Multinomial Regression
        # Add a constant (intercept) term to the independent variables
        #X = sm.add_constant(X)


        model = sm.MNLogit(y, X)
        
        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always")  # Capture all warnings
    

            result = model.fit(method='newton',maxiter=1000, disp=True)
        
            # Process the warnings, if any
            for warning in caught_warnings:
                if issubclass(warning.category, ConvergenceWarning):
                    warning_message = f"Warning with variable: {df.columns[independent_col_index]} - {str(warning.message)}\n"
                    # Open in append mode
                    f1.write(warning_message)
                    
        # Get the entire summary of the regression results (not just the table)
        full_summary = result.summary()  # Fetch the full summary object
        column_names = df.columns[independent_col_index].tolist()
        column_names_str = "_".join(column_names)
        # Create a valid filename for storing the result
        filename = df.columns[dependent_col_index]
        valid_filename = filename.replace('\n', ' ').replace(" ", "_")
        folder = r"analysis\clustering\results"
        filepath = os.path.join(folder, valid_filename)
        print(full_summary)
        # Write the full summary to a text file
        with open(filepath+".txt", 'w') as f:
            f.write(full_summary.as_text())

    except Exception as e:
        # If an error occurs, log the independent variable and the error message to a text file
        error_message = f"Error with variable: {df.columns[independent_col_index]} - {str(e)}\n"
        
        # Write the error message to the file
        #with open('failing_variables.txt', 'a') as f:
        f2.write(error_message)
        print(error_message)
        



if __name__ == "__main__":
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    filepath = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\10_Typisierung\mutlinominiale_regression\01_Datengrundlage_gesamt2.csv"
    df = pd.read_csv(filepath, sep=";", encoding='ISO-8859-1' )

    
    # filter cluster ohne ausreiser
    df = df[df[df.columns[6]].isin([0, 1, 2, 3])]
    #print(df[df.columns[6]])    
    # with open("Analyse_variablen.txt", 'w') as f:
    #     for index, column_name in enumerate(df.columns):
    #         f.write(f"{index}: {column_name}\n")

    # Compute the correlation matrix
    #corr_matrix = df.iloc[:,5:].corr().abs()
    # # Set the correlation threshold
    # threshold = 0.5

    # # Select the upper triangle of the correlation matrix
    # upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    # # Find columns with correlation above the threshold
    # to_drop = [column for column in upper_triangle.columns if any(upper_triangle[column] > threshold)]
    # # Drop those columns
    # print(to_drop)
    # df_reduced = df.drop(columns=to_drop)

    # Print the reduced DataFrame

    # Display all columns and rows

    # print(df_reduced)
    # # Now when you print the DataFrame, it will show the full table
    all_results = []

    # for i in range(0,5,1):
    #     dependent_col_index = i
    #     clusterlist = list(df[df.columns[i]].unique())
    #     # drop strings
    #     clusterlist = [item for item in clusterlist if item != ' ' and not pd.isna(item)]
    #     print(clusterlist)
    #dependent_col_index = 6
   # clusterlist = list(df[df.columns[dependent_col_index]].unique())
   #[10, 16, 36,44,29,140]
    list_of_testing_variables = [10,11,12,13,14,15,16,17,18,26,29,36,44,50,53,61,140]
    list_of_testing_variables = [[29, 44,36]]
    with open('mle_fail.txt', 'w') as f1, open("variable_fail.txt", 'w') as f2:
        for independt_col_index in list_of_testing_variables:
            multinomiale_regression_model(dependent_col_index=6,df= df ,ref_category= 0, independent_col_index=independt_col_index, results_list=all_results)

    # # Convert all results into a DataFrame
    # df_all_results = pd.DataFrame(all_results)

    # # Ensure 'p-value' is numeric, coercing errors to NaN
    # df_all_results['p-value'] = pd.to_numeric(df_all_results['p-value'], errors='coerce')

    # # Filter out rows with NaN or infinite 'p-value'
    # df_all_results = df_all_results[~df_all_results['p-value'].isna()]  # Remove NaNs
    # df_all_results = df_all_results[np.isfinite(df_all_results['p-value'])]  # Remove infinities

    # Extract significant results where 'p-value' is less than 0.1
    #significant_results = df_all_results[df_all_results['p-value'] < 0.1]

    # Display significant results
    #print(significant_results)
    independt_col_index = []
    
    #add multible features
    #multinomiale_regression_model(dependent_col_index=6,df= df ,ref_category= 0, independent_col_index=independt_col_index)