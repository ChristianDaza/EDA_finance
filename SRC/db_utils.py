#%%
import psycopg2
from sqlalchemy import create_engine
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials

    def init_sqlalchemy(self, credentials):
            """
            This function:
            initialises sql alchemy and connect it wiht the database in aws.
            
            Prameters:
                credentials (dict):
                    Python dictionary that contains the credetails to connact to a data base.
            """
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            ENDPOINT = credentials['RDS_HOST']
            USER = 'postgres'
            PASSWORD = credentials['RDS_PASSWORD']
            PORT = credentials['RDS_PORT']
            DATABASE = credentials['RDS_DATABASE']
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            engine.connect()

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
read_credentials("/Users/ChAre/OneDrive/Desktop/aicore/EDA_finance/credentials.yaml")
# %%
def init_sqlalchemy(credentials):
            from sqlalchemy import create_engine
            """
            This function:
            initialises sql alchemy and connect it wiht the database in aws.
            
            Prameters:
                credentials (dict):
                    Python dictionary that contains the credetails to connact to a data base.
            """
            DATABASE_TYPE = 'postgresql'
            ENDPOINT = credentials['RDS_HOST']
            USER = 'postgres'
            PASSWORD = credentials['RDS_PASSWORD']
            PORT = credentials['RDS_PORT']
            DATABASE = credentials['RDS_DATABASE']
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            engine.connect()
# %%
credentials = read_credentials("/Users/ChAre/OneDrive/Desktop/aicore/EDA_finance/credentials.yaml")
init_sqlalchemy(credentials)

#engine.close()
# %%
