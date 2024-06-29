#%%
import pandas as pd
df = pd.read_csv('./loan_payments')
# %%
# %%
df_test= df
df_test_2= df
df.info()
# %%
print(df['application_type'].unique())
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
            List of name or names of columns to change into catgorical data.
    Returns: 
        dataframe:
            Dataframe wiht specified column or columns changed into categorical data.
    """
    for column in columns:
        dataframe[column] = dataframe[column].astype("category")
    return dataframe

# %%
type(df['application_type'])
# %%

# %%

# %%
# %%
