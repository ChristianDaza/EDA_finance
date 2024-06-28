#%%
import pandas as pd
df = pd.read_csv('./loan_payments')
# %%
# %%
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
