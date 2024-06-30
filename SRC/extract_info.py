#%%
import pandas as pd 
import numpy as np
# %%
class DataFrameInfo:
    """ 
    Allows the user to extrcat useful information from the dataframe.
    
    Parameters:
        dataframe (df): 
            Dataframe which the users need to transform.

    Attributes:
        dataframe (df): 
            Dataframe which the users need to transform..

    Methods:
    check_columns_type:
        Checks and displays the data types of all the columns of a specified dataframe.
    descriptive_stats:
         Calculates the mean, median and standard deviation of datafraem columns wiht data type float64 or int64.
    unique_valus_count:
        Displays the total number of unqiues values and the count of each unique values within categorical data type columns.
    data_shape:
        Displays the number of rows and columsn of a dataframe.
    """

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
    
    def descriptive_stats(self, exclude_columns = []):
        """
        This function:
            Calculates the mean, median and standard deviation of datafraem columns wiht data type float64 or int64.
            It also allows the user to eliminate dataframe columsn before the descriptive statistics are run.

        Prameters:
            exclude_columns (list):
                List of column names the user want to remove before runnign the descriptive statistics.
        """
        if len(exclude_columns) > 0:
            # Delete undesired columns 
            exclude_columns = ["id", "member_id"]
            for column in exclude_columns:
                df_clean = self.dataframe.drop(exclude_columns, axis=1)

            # Compute descriptive statistics
            for column in df_clean:
                if  df_clean[column].dtype == "float64" or  df_clean[column].dtype == "int64":
                    mean = round( df_clean[column].mean(axis=0), 2)
                    median = round(df_clean[column].median(), 2)
                    standard_deviation = round( df_clean[column].std(), 2)
                    print(f"\n \n{column}: \n mean:{mean}  \n median:{median} \n standard_deviation:{standard_deviation}")
        
        else:
            # Compute descriptive statistics
            for column in self.dataframe:
                if  self.dataframe[column].dtype == "float64" or  self.dataframe[column].dtype == "int64":
                    mean = round(self.dataframe[column].mean(axis=0), 2)
                    median = round(self.dataframe[column].median(), 2)
                    standard_deviation = round(self.dataframe[column].std(), 2)
                    print(f"\n \n{column}: \n mean:{mean}  \n median:{median} \n standard_deviation: {standard_deviation}")
            
    def unique_valus_count(self):
        """
        This function:
                Displays the total number of unqiues values and the count of each unique values within categorical data type columns.
        """
        for column in self.dataframe:
            if self.dataframe[column].dtype == "category":
                unique_values = self.dataframe[column].value_counts()
                number_uniques = len(unique_values)
                print(f"{unique_values} \nTotal numer of unique values: {number_uniques} \n")

    def data_shape(self):
        """
        This function:
                    Displays the number of rows and columsn of a dataframe.
        """
        d_shape = self.dataframe.shape
        print(f"Rows: {d_shape[0]} \nColumns: {d_shape[1]}")
