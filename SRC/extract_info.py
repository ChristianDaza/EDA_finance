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

#%%
de = DataFrameInfo(df)

# %%
#Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
def descritive_stats(dataframe):
    #for column in ignore_columns:
        #df_clean = dataframe.drop(column, axis =1)
        #print(df_clean.info())
    for column in dataframe:
        if  dataframe[column].dtype == "float64" or "int64":
            mean = dataframe[column].mean
            median =  dataframe[column].median()
            standard_deviation =dataframe[column].std()
        return print(f"{column}: \n mean:{mean}  \n median:{median} \n stadard_deviation:{standard_deviation}")
# %%
#Count distinct values in categorical columns 
descritive_stats(df)

# %%
#Print out the shape of the DataFrame

for column in df:
        if df[column].dtype == "float64" or "int64":
            print(df[column].std())
# %%
#Generate a count/percentage count of NULL values in each column
df.info()
# %%
#Any other methods you may find useful 