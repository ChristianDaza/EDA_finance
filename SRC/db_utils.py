#%%
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials

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
        
    import pandas as pd
    def extract_data(t):
        table_name = input("Enter name of the desire table:").replace(" ", "")
        df = pd.read_sql(table_name, engine.connect())
        print(df.head(5))

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
credentials = read_credentials("/Users/ChAre/OneDrive/Desktop/aicore/EDA_finance/credentials.yaml")        
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
db_connect(credentials)

# %%
import pandas as pd
def extract_data():
      table_name = input("Enter name of the desire table:").replace(" ", "")
      df = pd.read_sql(table_name, engine.connect())
      print(df.head(5))
     
# %%
extract_data()
# %%
print(engine)
# %%
print('hello')
# %%
