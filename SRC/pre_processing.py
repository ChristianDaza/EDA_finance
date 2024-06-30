
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
    remove_characters:
        Remove a charcter or characters from the specified dataframe column.
    rename_column:
        Changes the name of a specified column.
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def category_convert(self, columns):
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
    
    def date_convert(self, columns):
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
    
    def string_tranform(self, columns):
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
    def string_tranform(self, columns, numeric_type):
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
            self.dataframe[column] = self.dataframe[column].astype(numeric_type)
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
