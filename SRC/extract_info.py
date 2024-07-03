#%%
import pandas as pd 
import numpy as np
from scipy.stats import normaltest
df= pd.read_csv("./loan_payments")
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
    count_null:
        Calculates the number or percentage of nulls for each column of the dataframe.
    norm_test:
        Calculates the the normality statistic for a chosen column.
    skew_check:
        Calculates the skewness for all numeric and date type columns in the chosen dataframe.

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
    
    def descriptive_stats(self, selected_column = [], exclude_columns = []):
        """
        This function:
            Calculates the mean, median and standard deviation of datafraem columns wiht data type float64 or int64.
            It also allows the user to eliminate dataframe columsn before the descriptive statistics are run.

        Prameters:
            exclude_columns (list):
                List of column names the user want to remove before runnign the descriptive statistics.
            selected_column (list):
                List of column names the user want to get the descriptive statistics from.
        """
        if len(exclude_columns) > 0:
            # Delete undesired columns
            for column in exclude_columns:
                df_clean = self.dataframe.drop(exclude_columns, axis=1)

            # Compute descriptive statistics
            for column in df_clean:
                if  df_clean[column].dtype == "float64" or  df_clean[column].dtype == "int64" or df_clean[column].dtype == '<M8[ns]':
                    mean = df_clean[column].mean(axis=0)
                    median = df_clean[column].median()
                    standard_deviation = df_clean[column].std()
                    print(f"\n \n{column}: \n mean:{mean}  \n median:{median} \n standard_deviation:{standard_deviation}")
        
        elif len(exclude_columns) == 0 and len(selected_column) == 0:
                # Compute descriptive statistics
                for column in self.dataframe:
                    if self.dataframe[column].dtype == "float64" or  self.dataframe[column].dtype == "int64" or self.dataframe[column].dtype == '<M8[ns]':
                        mean = self.dataframe[column].mean(axis=0)
                        median = self.dataframe[column].median()
                        standard_deviation = self.dataframe[column].std()
                        print(f"\n \n{column}: \n mean:{mean}  \n median:{median} \n standard_deviation: {standard_deviation}")
        
        elif len(exclude_columns) == 0 and len(selected_column) > 0:
                for columns in selected_column:
                    if self.dataframe[columns].dtype == "float64" or self.dataframe[columns].dtype == "int64" or self.dataframe[columns].dtype == '<M8[ns]':
                        mean = self.dataframe[columns].mean(axis=0)
                        median = self.dataframe[columns].median()
                        standard_deviation = self.dataframe[columns].std()
                        print(f"\n \n{columns}: \n mean:{mean}  \n median:{median} \n standard_deviation: {standard_deviation}")
        

            
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

    def count_null(self, percentage = False, individual_total = False):
        """
        This function:
            Calculates the number or percentage of nulls for each column of the dataframe.

        Prameters:
            percentage (str):
                If the paremeter value is "True" calculates percentage of nulls in each column of the dataframe based on the lenght of the dataframe.
            individual_total:
                Allows the percentage of nulls per column to be calculated based on the lenght of each column.
        """

        if percentage == True:
            null_percentage = self.dataframe.isnull().sum()/len(df)*100
            print(null_percentage)

        elif individual_total == True:
            for column in self.dataframe:
                column_nulls = round(self.dataframe[column].isnull().sum()/len(self.dataframe[column])*100, 2)
                print(f"{column}: {column_nulls}")
        else:
            null_count =  self.dataframe.isnull().sum()
            print(null_count)

    
    def norm_test(self, column):
        """
        This function:
            Calculates the the normality statistic for a chosen column.

        Prameters:
            Columns(str):
                Name of the column to test for normality.
            
        """
        data = self.dataframe[column]
        stat, p = normaltest(data, nan_policy='omit')
        print('Statistics=%.3f, p=%.3f' % (stat, p))

    def skew_check(self, columns = [], cutoff = 0.5):
        """
        This function:
            Calculates the skewness for all numeric and date type columns in the chosen dataframe.

        Prameters:
            Columns(list):
                List of column or columns to be checked for skewness.
            cutoff(int):
                Only values bigger than or equal to cuttoff will be return.
        """

        # Calculate skewness for all numeric and date type column in the dataframe
        if len(columns) == 0:
            for column in self.dataframe:
                if self.dataframe[column].dtype == "float64" or  self.dataframe[column].dtype == "int64" or self.dataframe[columns].dtype == '<M8[ns]':
                    column_skewness = round(self.dataframe[column].skew(), 2)
                    if column_skewness >= 0.5:
                        print(f"\n {column}: \n skewness:{column_skewness} \n")
    
        
        # Calculate skewness only for the specified column or columns
        if len(columns) > 0:
            for column in columns:
                if self.dataframe[column].dtype == "float64" or  self.dataframe[column].dtype == "int64" or self.dataframe[columns].dtype == '<M8[ns]':
                    column_skewness = round(self.dataframe[column].skew(), 2)
                    if column_skewness >= cutoff:
                        print(f"\n {column}: \n skewness:{column_skewness} \n")
