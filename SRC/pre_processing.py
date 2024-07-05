
import pandas as pd
from scipy import stats
import numpy as np

class DataTransform:
    """ 
    Helps the user transform the data types of columns on dataframes.
    
    Parameters:
        dataframe (df): 
            Dataframe which the users need to transform.

    Attributes:
        dataframe (df): 
            Dataframe which the users need to transform..

    Methods:
    category_convert:
        Transforms specified dataframe column or columns into categorical data.
    date_convert:
        Transforms specified columns that contain dates in string form into date type data.
    date_format:
        Transforms the specified column or columns into the string data type.
    string_tranform:
        Transforms the specified column or columns into the string data type.
    numeric_tranform:
        Transforms the specified column or columns into the numeric data type.
    remove_characters:
        Remove a charcter or characters from the specified dataframe column.
    rename_column:
        Changes the name of a specified column.
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def category_transform(self, columns):
        """
        This function:
            Transforms specified dataframe column or columns into categorical data.
        
        Prameters:
            dataframe(df): 
                Dataframe with the desired colum or columns to transform into categorical data.
            columns (list): 
                List of name or names as strings of columns to change into catgorical data.
        
        Returns: 
            dataframe (df):
                Dataframe wiht specified column or columns changed into categorical data.
        """
        for column in columns:
            self.dataframe[column] = self.dataframe[column].astype("category")
        return self.dataframe
    
    def date_transform(self, columns):
        """ 
        This function:
            Transforms specified columns that contain dates in string form into date type data.
        
        Prameters:
            dataframe(df): 
                Dataframe with the desired colum or columns to transform into date type data.
            columns (list): 
                List of name or names of columns to change into date type data.
        
        Returns: 
            dataframe (df):
                Dataframe with specified column or columns transformed into date type data.
        """
        for column in columns:
            self.dataframe[column]= self.dataframe[column].apply(pd.to_datetime) 
        return self.dataframe
    
    def date_format(self, columns, format):
        """ 
        This function:
            Formats data type dates in dataframe columns.

        Prameters:
            dataframe(df): 
                Dataframe with the desired date types colum or columns to format.
            columns (list): 
                List of date type column name or names to format.
            Format (str):
                String specifying the format the user what the date type columns to changed into following datatime module symbols.
                %Y (year), %m (month), %d(day): one or all symbols ordered wihthin the same string with or without a delimiter between them.
        
        Returns: 
            dataframe (df):
                Dataframe with specified date type column or columns reformatted.
        """
        for column in columns:
            self.dataframe[column]= self.dataframe[column].dt.strftime(format)
        return self.dataframe
    
    def string_transform(self, columns):
        """ 
        This function:
            Transforms the specified column or columns into the string data type.
        
        Prameters:
            dataframe(df): 
                Dataframe with the desired date types colum or columns to format.
            columns (list): 
                List of column name or names to format.
        
        Returns: 
            dataframe (df):
                Dataframe with the values in the specified column or columns transform into strings.
        """
        for column in columns:
            self.dataframe[column] = self.dataframe[column].astype("string")
        return self.dataframe
    
    def numeric_transform(self, columns):
        """ 
        This function:
            Transforms the specified column or columns into the numeric data type.
        
        Prameters:
            dataframe(df): 
                Dataframe with the desired column to chnage the data type.
            columns (list): 
                List of column name or names to format.
        
        Returns: 
            dataframe (df):
                Dataframe with the values in the specified column or columns transform into numeric data type.
        """
        for column in columns:
            self.dataframe[column] = pd.to_numeric(self.dataframe[column])
        return self.dataframe
    
    def remove_characters(self, column, characters):
        """ 
        This function:
            Remove a charcter or characters from the specified dataframe column.
        
        Prameters:
            dataframe (df): 
                Dataframe with the desired colum or columns to transform into date type data.
            columns (str): 
                Name of column from which the characters are going to be removed.
            Character (str):
                Charcters to removed from the specified dataframe column.
        
        Returns: 
            dataframe (df):
                Dataframe with the specified characters removed.
        """
        for character in characters:
            self.dataframe[column] = self.dataframe[column].str.replace(character, "")
        return self.dataframe
        
    def rename_column(self, old_column_name, new_column_name):
        """ 
        This function:
            Changes the name of a specified column.
       
        Prameters:
            dataframe(df): 
                Dataframe with the desired colum to change the name.
            columns (str): 
                List of name or names of columns to change into date type data.
        old_column_name: 
                Name of the column the user's want to change.
        new_column_name (str):
                The name the user wants the column to be.
        
        Returns:
            dataframe (df):
                Dataframe with the columns new name.
        """
        self.dataframe.rename(columns = {old_column_name:new_column_name}, inplace = True)
        return self.dataframe
    
    def replace_null(self, column, value):
        """
        This function:
                Replaces null values on a specified column of a dataframe.
            
            Prameters:
                columns (list): 
                    Column which have null values.
                Value (str, num):
                    Value to substitute the null values in the column.
            
            Returns: 
                dataframe (df):
                    Dataframe with with the null values replaced.
        """

        if self.dataframe[column].isnull().sum() > 0:
            self.dataframe[column] = self.dataframe[column].fillna(value)
            return self.dataframe 
        else:
            raise ValueError(f"No null found in the {column} column, please choose another column.")
        
    def remove_columns(self, columns):
        """
        This function:
                remove selected column or columns by the user.
            
            Prameters:
                column (str): 
                    Name of the column or columns to remove from the dataframe.
            
        Returns: 
            dataframe (df):
                Dataframe with with the removed column or columns.
        """
        
        self.dataframe = self.dataframe.drop(columns, axis = 1)
        return self.dataframe 
    
    def skew_transform(self, dataframe, transformation):
        """
        This function:
            Calculates the skewness for all numeric and date type columns in the chosen dataframe.

        Prameters:
            Columns (str):
                Name of the column with the values to be transformed.
            Tranformation (str):
                Specifies the type of transformation: log, BC(Box-Cox) and YJ(Yeo-Johnson).
        """
        data = dataframe.to_numpy()

        if transformation == "log":
            log_transform = pd.DataFrame({"log":np.log(data)})
            return log_transform

        elif transformation == "BC" :
            BC_transform = stats.boxcox(data)
            BC_transform = pd.DataFrame({"Box-Cox":BC_transform[0]})
            return BC_transform

        elif transformation == "YJ":
            BY_transform = stats.yeojohnson(data)
            BY_transform = pd.DataFrame({"Yeo-Johnson":BY_transform[0]})
            return BY_transform 
        
        #elif transformation == "all" and not data.any():
            
            #log_transform = np.log(data)
            #BC_transform = stats.boxcox(data)
            #BC_transform = pd.Series(BC_transform[0])
            #BY_transform = stats.yeojohnson(data)
            #BY_transform = pd.Series(BY_transform[0])
            #df_skew_transform = pd.DataFrame({"origional_values": data, "log":log_transform, "Box-Cox":BC_transform, "Yeo-Johnson":BY_transform})
            #return df_skew_transform
        
        #elif transformation == "all" and np.any(data >= 0):
            #log_transform = np.log(data)
            #BY_transform = stats.yeojohnson(data)
            #BY_transform = pd.Series(BY_transform[0])
            #df_skew_transform = pd.DataFrame({"origional_values": data, "log":log_transform, "Yeo-Johnson":BY_transform})
            #return df_skew_transform

    
    # %%
