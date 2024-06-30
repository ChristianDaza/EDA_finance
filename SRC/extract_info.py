#%%
import pandas as pd 
import numpy as np
import pre_processing as pp
df = pd.read_csv("./loan_payments")
#%%
# Preprocess original df
pre_pro = pp.DataTransform(df)
pre_pro.category_transform(["grade", "sub_grade", "home_ownership", "verification_status", "loan_status", "payment_plan", "purpose", "application_type", "employment_length"])
pre_pro.date_transform(["issue_date", "earliest_credit_line", "last_payment_date", "next_payment_date", "last_credit_pull_date"])
pre_pro.string_transform(["employment_length", "term"])
pre_pro.remove_characters("employment_length", ["years", "year"])
pre_pro.remove_characters("term", ["months"])
pre_pro.rename_column("employment_length", "years_of_employment")
pre_pro.rename_column("term", "term_in_months")
pre_pro.numeric_transform(["term_in_months"])
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
 #%%
df_info = DataFrameInfo(pre_pro.dataframe)

#%%
df_info.unique_valus_count()

        

        

        
# %%
#Count distinct values in categorical columns 

unique_value_count(df)
#%%
#Generate a count/percentage count of NULL values in each column
type
# %%
#Any other methods you may find useful 