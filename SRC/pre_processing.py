#%%
import pandas as pd
df = pd.read_csv('./loan_payments')
# %%
# %%
df_og = df
df_test= df
df_test_2= df
df.info()
# %%
print(df['issue_date'].unique())
# %%
# Term : 36 months_ strip number and sting 
# Grade category
# sub grade category
# employment years
# home_ownerhsip catgory
# verification_status catgeorical
# issue_date date time
#  loan_status Categorycal 
# payment_plan Categorical
# purpose categorical
# earliest_credit_line dtatetime
# last_payment_date datetime
# next_payment_date datetime
# last_credit_pull_date datetime
# application_type categoricaltidy data pyhton

# %%
# convert column data into category
def category_convert(dataframe, columns):
    """
    This function:
        Transforms specified dataframe column or columns into categorical data.
    Prameters:
        dataframe(df): 
            Dataframe with the desired colum or columns to transform into categorical data.
        columns (list): 
            List of name or names as strings of columns to change into catgorical data.
    Returns: 
        dataframe:
            Dataframe wiht specified column or columns changed into categorical data.
    """
    for column in columns:
        dataframe[column] = dataframe[column].astype("category")
    return dataframe
# %%
import datetime as dt
def date_convert(dataframe, columns):
    """ 
    This function:
        Transforms specified columns that contain dates in string form into date type data.
    Prameters:
        dataframe(df): 
            Dataframe with the desired colum or columns to transform into date type data.
        columns (list): 
            List of name or names of columns to change into date type data.
    Returns: 
        dataframe:
            Dataframe with specified column or columns changed into date type data.
    """
    for column in columns:
        dataframe[column]= dataframe[column].apply(pd.to_datetime) 
    return dataframe

#%%
def date_format(dataframe, columns, format):
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
            dataframe:
                Dataframe with specified date type column or columns reformatted.
        """
        for column in columns:
            dataframe[column]= dataframe[column].dt.strftime(format)
        return dataframe

# %%
c = date_convert(df_test, ["issue_date", "last_payment_date", "next_payment_date"], "%m-%Y")
# %%
df_dt = date_format(df_test, ["issue_date", "last_payment_date", "next_payment_date"], "%m-%Y")
# %%
# %%

# %%


# %%

# %%
