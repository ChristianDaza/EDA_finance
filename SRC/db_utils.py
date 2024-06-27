#%%
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd

#%%
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials

    def db_connect(credentials):
            """
            This function:
            Connects  to data base in AWS and prints the names of all the tables of the database.
            
            Prameters:
                credentials (dict):
                    Python dictionary that contains the credetails to connact to a data base.
            """
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            ENDPOINT = credentials['RDS_HOST']
            USER = credentials['RDS_USER']
            PASSWORD = credentials['RDS_PASSWORD']
            PORT = credentials['RDS_PORT']
            DATABASE = credentials['RDS_DATABASE']
            global engine
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            engine.connect()
            insp = inspect(engine)
            print(f"The connected database has the following tables: {insp.get_table_names()}")
        
    def save_data():
       """
        This function:
            Save the extravted data from the connected data base as a csv file in the user's machine, under the user specified filename.
   
        Returns: 
            file (CSV):
                Database data saved into a csv file.
        """
       name_data = input("Create a name for the file in which the data  will be saved: ").replace(" ", "")
       df.to_csv(name_data, index=False)

# %%
# Read yaml credetial files    
import yaml
def read_credentials(db_credentials_file_yaml):
    """
    This function:
        Reads a yaml file with credentials to connect to a database and returns them as a dictionary.
    Prameters:
        db_credentials_file (str): 
            Path to the yaml file with the credentilas to connact to a data base.
    Returns: 
        redentials_dict (dict):
            Python dictionary that contains the credetails to connact to a data base.
    """
    
    with open(db_credentials_file_yaml) as file:
        credentials_dict = yaml.safe_load(file)
    return credentials_dict
      
# %%
def db_connect(credentials):
            from sqlalchemy import create_engine
            from sqlalchemy import inspect
            """
            This function:
            Connects  to data base in AWS and prints the names of all the tables of the database.
            
            Prameters:
                credentials (dict):
                    Python dictionary that contains the credetails to connact to a data base.
            """
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            ENDPOINT = credentials['RDS_HOST']
            USER = credentials['RDS_USER']
            PASSWORD = credentials['RDS_PASSWORD']
            PORT = credentials['RDS_PORT']
            DATABASE = credentials['RDS_DATABASE']
            global engine
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            engine.connect()
            insp = inspect(engine)
            print(f"The connected database has the following tables: {insp.get_table_names()}")
            
            

# %%
import pandas as pd
def extract_data():
      table_name = input("Enter name of the desire table:").replace(" ", "")
      global df
      df = pd.read_sql(table_name, engine.connect())
      return df
     
# %%
def save_data():
       name_data = input("Create a name for the file in which the data  will be saved: ").replace(" ", "")
       df.to_csv(name_data, index=False)

      
# %%
credentials = read_credentials("/Users/ChAre/OneDrive/Desktop/aicore/EDA_finance/credentials.yaml")    
db_connect(credentials)
extract_data()
save_data()
# %%

# %%
