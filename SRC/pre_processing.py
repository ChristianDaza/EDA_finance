# Imports
import numpy as np
import pandas as pd
from scipy import stats

# Class
class DataTransform:
    """ 
    Helps the user to manipulate and transform the dataframe and its columns.
    
    Parameters:
        dataframe (df): 
            Dataframe to manipulate.

    Attributes:
        dataframe (df): 
            Dataframe to manipulate.

    Methods:
        category_transform:
            Transforms the values of a specified dataframe column or columns into categorical data.

        date_transform:
            Transformsthe values of a specified columns or column into date type data.

        date_format:
            Transforms the date type data format e.g day:month:year into another format specified by the user but returns them as strings.

        string_tranform:
            Transforms the values of a specified column or columns into the string data type.

        numeric_tranform:
            Transforms the values of a specified column or columns into the integer data type.

        remove_characters:
            Remove a character or characters from the values of a specified dataframe column.

        rename_column:
            Changes the name of a specified column.

        rename_column:
            Changes the name of a specified column.y the user but returns them as strings.

        replace_null:
            Replaces null values on a specified column of a dataframe.

        skew_transform:
            Transformed skew data distribution.

        remove_outlier:
            Deletes rows from the selected dataframe based on a list of indeces.
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def category_transform(self, columns):
        """
        This function:
            Transforms the values of a specified dataframe column or columns into categorical data.
        
        Prameters:
            columns (list): 
                List of name or names of columns which values will be chnaged into catgorical data.
        
        Returns: 
            dataframe (df):
                Dataframe with specified column or columns values chnaged to categorical data.
        """

        for column in columns:
            self.dataframe[column] = self.dataframe[column].astype("category")
        return self.dataframe
    
    def date_transform(self, columns):
        """ 
        This function:
            Transforms the values of a specified columns or column into date type data.

        Prameters:
            columns (list): 
                List of name or names of columns, which values will be change into date type data.
        
        Returns: 
            dataframe (df):
                Dataframe with the values of specified column or columns transformed into date type data.
        """

        for column in columns:
            self.dataframe[column]= self.dataframe[column].apply(pd.to_datetime) 
        return self.dataframe
    
    def date_format(self, columns, format):
        """ 
        This function:
            Transforms the date type data format e.g day:month:year into another format specified by the user but returns them as strings.

        Prameters:
            columns (list): 
                List of column name or names, which date formats wish to be changed.

            Format (str):
                String specifying the format to change dates into, following datatime module symbols.
                %Y (year), %m (month), %d(day): one or all symbols ordered wihthin the same string with or without a delimiter between them.
        
        Returns: 
            dataframe (df):
                Dataframe with formatted date type values in columns.
        """
        for column in columns:
            self.dataframe[column]= self.dataframe[column].dt.strftime(format)
        return self.dataframe
    
    def string_transform(self, columns):
        """ 
        This function:
            Transforms the values of a specified column or columns into the string data type.
        
        Prameters:

            columns (list): 
                List of column name or names, which values will be transformed into strings.
        
        Returns: 
            dataframe (df):
                Dataframe with the values in the specified column or columns transformed into strings.
        """

        for column in columns:
            self.dataframe[column] = self.dataframe[column].astype("string")
        return self.dataframe
    
    def remove_characters(self, column, characters):
        """ 
        This function:
            Remove a character or characters from the values of a specified dataframe column.
        
        Prameters:
            columns (str): 
                Column name or names from which the characters are going to be removed.

            Character (str):
                Charcter to removed from the specified column.
        
        Returns: 
            dataframe (df):
                Dataframe with the specified character removed form the specified column or columns.
        """
        
        for character in characters:
            self.dataframe[column] = self.dataframe[column].str.replace(character, "")
        return self.dataframe
    
    def numeric_transform(self, columns):
        """ 
        This function:
            Transforms the values of a specified column or columns into the integer data type.
        
        Prameters:
            columns (list): 
                List of column name or names, which values will be transfromed into integer type data.
        
        Returns: 
            dataframe (df):
                Dataframe with the values in the specified column or columns transform into the integer data type.
        """
        
        for column in columns:
            self.dataframe[column] = pd.to_numeric(self.dataframe[column])
        return self.dataframe
        
    def rename_column(self, old_column_name, new_column_name):
        """ 
        This function:
             Changes the name of a specified column.
       
        Prameters:
            old_column_name: 
                    Name of the column, which will be changed.

            new_column_name (str):
                    The name the column will be changed to.
        
        Returns:
            dataframe (df):
                Dataframe with the column name chnaged.
        """

        self.dataframe.rename(columns = {old_column_name:new_column_name}, inplace = True)
        return self.dataframe
    
    def replace_null(self, column, value):
        """
        This function:
                Replaces null values on a specified column of a dataframe.
            
            Prameters:
                columns (list): 
                    Name of a column with null values.

                Value (str, num):
                    Value to substitute the null values for.
            
            Returns: 
                dataframe (df):
                    Dataframe with the null values replaced.
        """

        # Check that the column have missing values
        if self.dataframe[column].isnull().sum() > 0:

            # Replace missing values
            self.dataframe[column] = self.dataframe[column].fillna(value)
            return self.dataframe 
        else:
            raise ValueError(f"No null found in the {column} column, please choose another column.")
        
    def remove_columns(self, columns=[]):
        """
        This function:
                Removes selected column or columns from the dataframe.
            
        Prameters:
            columns (list): 
                List of column  name or names to be removed from the dataframe.
            
        Returns: 
            dataframe (df):
                Dataframe with the specified columns removed.
        """

        # Remove columns
        self.dataframe = self.dataframe.drop(columns, axis = 1)
        return self.dataframe 
    
    def skew_transform(self, dataframe=pd.DataFrame(), transformation = ""):
        """
        This function:
            Transformed skew data distribution.

        Prameters:
            Columns (str):
                Name of the column with the values to be transformed.

            Tranformation (str):
                Specifies the type of transformation: log, BC(Box-Cox) and YJ(Yeo-Johnson).
        """
        data = dataframe.to_numpy()

        # Log transformation
        if transformation == "log":
            log_transform = pd.DataFrame({"log":np.log(data)})
            return log_transform

        # Box-Cox transformation
        # This function is incompatible with zero and nagtive values.
        # A future implementation will chekc for these incompatible values and skip this transformation fi they are present.
        elif transformation == "BC" :
            BC_transform = stats.boxcox(data)
            BC_transform = pd.DataFrame({"Box-Cox":BC_transform[0]})
            return BC_transform

        # Yeo-Johnson
        elif transformation == "YJ":
            BY_transform = stats.yeojohnson(data)
            BY_transform = pd.DataFrame({"Yeo-Johnson":BY_transform[0]})
            return BY_transform 
        
    def remove_outlier(self, outlier_delete_index):
        """    
        This function:
                Deletes rows from the selected dataframe based on a list of indeces.

        Prameters:
            outlier_delete_index (list):
                List of row indices to be deleted.

            Dataframe_column (df):
                Dataframe with deleted specified rows.
        """

        self.dataframe.drop(outlier_delete_index, inplace=True)
        return self.dataframe

