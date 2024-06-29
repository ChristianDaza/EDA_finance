#%%
import pandas as pd
df = pd.read_csv('./loan_payments')
# %%
# %%
df_test= df
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
def category_convert(dataframe, column):
    if type(column) is str:
        dataframe[column] = dataframe[column].astype("category")
    elif type(column) is list:
        for col in column:
            dataframe[col] = dataframe[col].astype("category")
    return dataframe

# %%
df_cotegory_converted = category_convert(df_test, ["home_ownership", "verification_status", "loan_status"])
# %%
df_cotegory_converted.info()
# %%
print(type("hi"))
# %%
