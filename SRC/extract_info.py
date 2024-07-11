# Imports
import numpy as np
import pandas as pd 
from scipy.stats import normaltest

# Class
class DataFrameInfo:
    """ 
    Allows the user to extract useful information from the dataframe.
    
    Parameters:
        dataframe (df): 
            Dataframe to extract information from.

    Attributes:
        dataframe (df): 
            Dataframe to extract information from.

    Methods:
        check_columns_type:
            Checks and displays the data types of all the columns of in a dataframe.

        descriptive_stats:
            Calculates the mean, median and standard deviation for a column or columns with data type float64 or int64.

        unique_valus_count:
            Displays the total number of unique values and their counts within categorical data type columns.

        data_shape:
            Displays the number of rows and columns of a dataframe.

        count_null:
            Calculates the number or percentage of nulls for each column of the dataframe.

        norm_test:
            Calculates the the normality statistic for a chosen column.

        skew_check:
            Calculates the skewness for all numeric and date type columns in the chosen dataframe.

        z_score:
            Calculates the Z_cores for a specify column of a dataframe and can filter based on specified cutoff value.

        IQR_filter_outliers:
            Returns outlier values of a selected column based on the interquartile range.
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe


    def check_columns_type(self):
        """
        This function:
            Checks and displays the data types of all the columns of a dataframe.


        Returns: 
            dataframe (series):
                Panda series displaying the column names and their corresponding data types.
        """

        columns_types = self.dataframe.dtypes
        return columns_types
    
    def descriptive_stats(self, selected_column = [], exclude_columns = []):
        """
        This function:
            Calculates the mean, median and standard deviation of a column or columns wiht data type float64 or int64.
            It also allows the user to eliminate dataframe columns before the descriptive statistics are run.

        Prameters:
            exclude_columns (list):
                List of column name or names to remove before running the descriptive statistics.

            selected_column (list):
                List of column name or names to calculate the descriptive statistics from.
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
        
        # If not exclude columns or columns are specified, run for all dataframe columns
        elif len(exclude_columns) == 0 and len(selected_column) == 0:
                # Compute descriptive statistics
                for column in self.dataframe:
                    if self.dataframe[column].dtype == "float64" or  self.dataframe[column].dtype == "int64" or self.dataframe[column].dtype == '<M8[ns]':
                        mean = self.dataframe[column].mean(axis=0)
                        median = self.dataframe[column].median()
                        standard_deviation = self.dataframe[column].std()
                        print(f"\n \n{column}: \n mean:{mean}  \n median:{median} \n standard_deviation: {standard_deviation}")
        
        # if columns are specified run descriptive stats just for them
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
                Displays the total number of unique values and their counts within categorical data type columns.
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
                If the paremeter value is "True" calculates percentage of nulls in each column of the dataframe based on the total number of fata points of the dataframe.

            individual_total:
                Allows the percentage of nulls to be calculated per total values for their corresponding column.
        """

        if percentage == True:
            null_percentage = self.dataframe.isnull().sum()/len(self.dataframe)*100
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
            A exclude column parameter will be implemented in the future to skip numeric column such as ID columns.

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
                List of column or columns names to be checked for skewness.

            cutoff(int):
                Only values bigger than or equal to cuttoff will be return.
        """

        # Calculate skewness for all numeric and date type column in the dataframe
        if len(columns) == 0:
            for column in self.dataframe:
                if self.dataframe[column].dtype == "float64" or self.dataframe[column].dtype == "int64":
                    column_skewness = round(self.dataframe[column].skew(), 2)
                    if column_skewness >= 0.5:
                        print(f"\n {column}: \n skewness:{column_skewness} \n")
    
        
        # Calculate skewness only for the specified column or columns
        if len(columns) > 0:
            for column in columns:
                if self.dataframe[column].dtype == "float64" or  self.dataframe[column].dtype == "int64":
                    column_skewness = round(self.dataframe[column].skew(), 2)
                    if column_skewness >= cutoff:
                        print(f"\n {column}: \n skewness:{column_skewness} \n")


    def z_score(self, dataframe, column, cutoff = 2, filter=False):
        """"
        This function:
             Calculates the Z_cores for a specify column of a dataframe and can filter based on specified cutoff value.

        Prameters:
            Columns (str):
                Name of the column with the values taht will be use to calculate the Z_scores.
            filter (str):
                Filters the z_values based on the cutoff provided by the user, inclusive.
        Returns:
            dataframe (df):
                Dataframe with z_score values or filtered dataframe based on the provided cutoff value.
        """
        dataframe= pd.DataFrame(dataframe[column])
        mean = np.mean(dataframe[column])
        stde = np.std(dataframe[column])
        z_scores = pd.DataFrame({"z_score":(dataframe[column] - mean)})
        dataframe["z_scores"] = z_scores
        if filter == False:
            return dataframe
        elif filter == True:
            return dataframe[dataframe["z_scores"] >= cutoff]
        
    def IQR_filter_outliers(self, column, dataframe = pd.DataFrame()):
        """"
        This function:
             Display outlier values of a selected column based on the calculation on the interquartile range of that column.


        Prameters:
            Dataframe (df):
                Dataframe with the data to check for outliers. Only use if the dataframe has the calculated z_scores column for the same column, which the user is going to use for this method.
                
            Columns (str):
                Name of the column with the values that will be use to calculate, which values are classified as outliers.
        """
        if dataframe.get("z_scores") is not None:
            Q1 = dataframe[column].quantile(0.25)
            Q3 = dataframe[column].quantile(0.75)

            # Calculate Interquantile range
            IQR = Q3 - Q1

            print(f"Q1 (25th percentile): {Q1}")
            print(f"Q3 (75th percentile): {Q3}")
            print(f"IQR: {IQR}")

            # Idetifying outliers
            outliers = dataframe[(dataframe[column] < (Q1 - 1.5 * IQR)) | (dataframe[column] > (Q3 + 1.5 * IQR))]
            return outliers
 
        else:
            dataframe= pd.DataFrame(dataframe[column])
            Q1 = dataframe[column].quantile(0.25)
            Q3 = dataframe[column].quantile(0.75)

            # Calculate Interquantile range
            IQR = Q3 - Q1

            print(f"Q1 (25th percentile): {Q1}")
            print(f"Q3 (75th percentile): {Q3}")
            print(f"IQR: {IQR}")

            # Idetifying outliers
            outliers = dataframe[(dataframe[column] < (Q1 - 1.5 * IQR)) | (dataframe[column] > (Q3 + 1.5 * IQR))]
            return outliers

   

