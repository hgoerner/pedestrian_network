#%%

import pandas as pd
import os
from IPython.display import display
from regex import P




#%%

class DataProcessor:
    def __init__(self):
        """
        Initialize the DataProcessorWithGaps class with a dictionary of file paths.

        :param files: Dictionary of CSV file paths, where the key is the name and the value is the file path.
        """
        self.final_outer_join_df = None
        self.count_dic = {}
        self.pivot_data = pd.DataFrame()

    def load_data(self, folder_path):
        """Load CSV data files from a specified folder.

        This function scans the specified folder for CSV files, excluding any temporary files, 
        and loads them into a dictionary of dataframes stored in the instance variable `count_dic`.

        Args:
            folder_path (str): The path to the folder containing the CSV files.

        Returns:
            None
        """
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv') and not filename.startswith('~$'):
                file_path = os.path.join(folder_path, filename)
                basename = filename.split(".")[0]

                # Read the file without 'Unnamed: 0' column
                df = pd.read_csv(os.path.join(folder_path, filename),
                                 usecols=lambda column: column != 'Unnamed: 0')
                
                # Get the columns from the dataframe (these will be the sub-levels of the MultiIndex)
                #columns = list(df.columns)

                # Create the MultiIndex
                # multi_index = pd.MultiIndex.from_product(
                #     [[basename], columns], names=["Zählstelle", "Zählinfo"])

                # Assign the MultiIndex to the dataframe columns
                #df.columns = multi_index
                # Store the dataframe in the count_dic dictionary
                self.count_dic[basename] = df
                
    def assign_flow_markers(self):
        """Assign unique flow_marker values based on the unique flow directions in each dataframe."""
        for name, _ in self.count_dic.items():
            # Get unique flow directions
            unique_flows = self.count_dic[name][(name, 'flow')].unique()
            # Map each unique flow to a distinct number
            flow_map = {flow: idx + 1 for idx, flow in enumerate(unique_flows)}
            self.count_dic[name][(name, 'flow_marker')] = self.count_dic[name][(
                name, 'flow')].map(flow_map)

    def create_multiindex(self):
        """Create a MultiIndex for each dataframe based on 'Weekday', 'start occurrence time', and 'flow_marker'."""
        for name, _ in self.count_dic.items():
            # Create the MultiIndex for rows as you're already doing
            tuples = list(zip(self.count_dic[name][(name, 'Weekday')],
                              self.count_dic[name][(
                                  name, 'start occurrence time')],
                              self.count_dic[name][(name, 'flow_marker')]))
            # Set MultiIndex for rows
            self.count_dic[name].index = pd.MultiIndex.from_tuples(
                tuples, names=["Weekday", "start occurrence time", 'flow_marker'])

            self.count_dic[name] = self.count_dic[name][[
            (name, "start occurrence date"),
            (name, "count"),
            (name, "factor"),
            (name, "count_scaled"),
            
        ]]
            self.count_dic[name]= self.count_dic[name].sort_index(level=['Weekday','start occurrence time'])      

                     
    def sort_readable(self):
        self.final_outer_join_df.sort_index(level=['Weekday','start occurrence time'], inplace=True)

    def outer_join(self):
        """Perform an outer join on all the dataframes along axis=1 using the MultiIndex."""
        self.final_outer_join_df = pd.concat(
            self.count_dic.values(), axis=1, join='outer')
        self.sort_readable()

    def process(self, folder_path):
        """Run all steps sequentially to process the data."""
        self.load_data(folder_path)
        self.assign_flow_markers()
        self.create_multiindex()
        #self.outer_join()
    def pivoting_files(self):
        """
        Purpose: 
        """
        for name, _ in self.count_dic.items():
            #print(self.count_dic[name])
            print(name)
            df = self.count_dic[name]
            df = df[["start time(ohne Tag)", "gleitender_Stundenwert_aus_MW"]]
            #df =df.drop(columns=["count","gleitender_MW_15min", "count_anteilig"])
            df_pivot = df.set_index('start time(ohne Tag)').T
            df_pivot.index = [name]
            print(df_pivot)
            self.pivot_data = pd.concat([self.pivot_data,df_pivot]) 
        
    # end def


#%%

# concat and pivot dataframes
file_path = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\01_Zählstellenseiten_Korrelation\01_Zählstellen_Seiten_zusammengefasst\unskaliert\mit_außreiser"

processor = DataProcessor()
processor.load_data(file_path)

#print(processor.count_dic)
processor.pivoting_files()

print(processor.pivot_data.to_csv("Dategrundlage.csv"))

# processor.count_dic["HD14_OTC17"].
# processor.count_dic["HD14_OTC17"].to_csv("test2.csv", index=True)

#processor.final_outer_join_df.to_csv("test.csv", index=True)
# Load, assign flow markers, create multiindex, and perform outer join
# filled_df = processor.fill_time_gaps(freq='15T')  # Fill time gaps

# %%
