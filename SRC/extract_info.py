#%%
import pandas as pd 
df = pd.read_csv("./loan_payments")
# %%
class DataFrameInfo:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def check_columns_type(self):
        """
        This function:
            Checks and displays the data types of all the columns of a specified dataframe.

        Prameters:
            dataframe(df): 
                Dataframe that the user wants the columns' data types to be checked.

        Returns: 
            dataframe (series):
                Panda series displaying the column names and their corresponding datatypes for the specified dataframe.
        """
        columns_types = self.dataframe.dtypes
        return columns_types

#%%
de = DataFrameInfo(df)

# %%
#Extract statistical values: median, standard deviation and mean from the columns and the DataFrame

# %%
#Count distinct values in categorical columns

# %%
#Print out the shape of the DataFrame

# %%
#Generate a count/percentage count of NULL values in each column

# %%
#Any other methods you may find useful 