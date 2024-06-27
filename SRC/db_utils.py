#%%
import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
#%%
def read_credentials(db_credentials_file_yaml):
    """
    This function:
        Reads a yaml file with credentials to connect to a database and returns them as a dictionary.
    Prameters:
        db_credentials_file (str): 
            Path to the yaml file with the credentilas to connact to a data base.
    Returns: 
        Credentials_dict (dict):
            Python dictionary that contains the credentails to connact to a data base.
    """
    
    with open(db_credentials_file_yaml) as file:
        credentials_dict = yaml.safe_load(file)
    return credentials_dict
#%%
class RDSDatabaseConnector:
    """ 
    Class that allow you to connect, select save and load data from the Amazon Relational Database Service (RDS).
    
    Parameter:
        Credentials_dict (dict):
            Python dictionary that contains the credentails to connact to a data base.

    Attributes:
        Credentials(dict): 
            Python dictionary that contains the credentails to connact to a data base.
        
    
    Methods:
    db_connect():
         Connects to the database in Amazon RDS and prints the names of all the tables of the database.
    extract_data():
        Allows the user to extract data from a specified table from the database in Amazon RDS.
    save_data():
        Allows the user to save the data from a specified table rom the database in Amazon RDS as a csv.
    load_data():
        Allows the user to load the previously data saved as a csv from save_data() into Python as a dataframe.
    """
    def __init__(self, credentials):
        self.credentials = credentials

    def db_connect(self):
            """
            This function:
            Connects to data base in AWS and prints the names of all the tables of the database.
            
            Returns:
                engine.connect():
                    Initiates connection to the cloud database.
            """
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            ENDPOINT = self.credentials['RDS_HOST']
            USER = self.credentials['RDS_USER']
            PASSWORD = self.credentials['RDS_PASSWORD']
            PORT = self.credentials['RDS_PORT']
            DATABASE = self.credentials['RDS_DATABASE']
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            engine.connect()
            insp = inspect(engine)
            print(f"The connected database has the following tables: {insp.get_table_names()}")
            return engine.connect()
    
    def extract_data(self):
        """
        This function:
            Extract the data from a user specify table from the connected database and saves it as a pandas dataframe.

        Returns: 
            df (df):
                Dataframe created from the user specify table from the connected database.
        """
        engine_connect = self.db_connect()
        table_name = input("Enter name of the desire table:").replace(" ", "")
        df = pd.read_sql(table_name, engine_connect)
        return df
    
    def save_data(self):
        """
        This function:
            Save the extracted data from the connected data base as a csv file in the user's machine, under the user specified filename.
        
        Returns
            file (CSV):
                Database data saved into a csv file.
        """
        name_data = input("Create a name for the file in which the data  will be saved: ").replace(" ", "")
        df = self.extract_data()
        df.to_csv(name_data, index=False)
    
    def load_data(self, data_file_path):
      """
      This function:
            This function loads the saved data into Python.
        
        Returns
            dataframe (df)):
                Saved data laod into Pyhton as a dataframe.
      """
      df = pd.read_csv(data_file_path)
      return df 