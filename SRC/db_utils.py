# Imports
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import yaml

# Read database credentials
def read_credentials(db_credentials_file_yaml):
    """
    This function:
        Reads a yaml file with credentials to connect to a database and returns them as a Python dictionary.

    Prameters:
        db_credentials_file (str): 
            Path to the yaml file with the credentials to connect to a data base.

    Returns: 
        Credentials_dict (dict):
            Python dictionary that contains the credentials to connact to a data base.
    """
    # Open and reads yaml file
    with open(db_credentials_file_yaml) as file:
        credentials_dict = yaml.safe_load(file)

    # Return yaml file data as a Python dictionary
    return credentials_dict

# Class
class RDSDatabaseConnector:
    """ 
    Class that allow you to connect, select, save and load data from the Amazon Relational Database Service (RDS).
    
    Parameter:
        Credentials_dict (dict):
            Python dictionary that contains the credentails to connect to a data base.

    Attributes:
        Credentials(dict): 
            Python dictionary that contains the credentails to connact to a data base.
        

    Methods:
        db_connect():
            Connects to the cloud database and prints the names of all the tables stored.

        extract_data():
            Allows the user to extract a specified table from the database.
            
        save_data():
            Allows the user to save a specified table from the database as a csv into the local machine.

        load_data():
            Load the previous data into Python as a dataframe.
    """

    def __init__(self, credentials):
        self.credentials = credentials

    def db_connect(self):
            """
            This function:
            Connects to the cloud database and prints the names of all the tables stored.
            
            Returns:
                engine.connect():
                    Initiates connection to the cloud database.
            """
            # Connection credentials
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            ENDPOINT = self.credentials['RDS_HOST']
            USER = self.credentials['RDS_USER']
            PASSWORD = self.credentials['RDS_PASSWORD']
            PORT = self.credentials['RDS_PORT']
            DATABASE = self.credentials['RDS_DATABASE']
            
            # Setting up engine
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            engine.connect()

            # Get the names of the tables store
            insp = inspect(engine)

            # Print all tables stored in the database
            print(f"The connected database has the following tables: {insp.get_table_names()}")
            return engine.connect()
    
    def extract_data(self):
        """
        This function:
            Allows the user to extract a specified table from the database.

        Returns: 
            df (df):
                Dataframe created from the user specify table from the connected database.
        """
        # Connects to database
        engine_connect = self.db_connect()

        # Ask user to select the table
        table_name = input("Enter name of the desire table:").replace(" ", "")

        # Transform table in SQL
        df = pd.read_sql(table_name, engine_connect)
        return df
    
    def save_data(self):
        """
        This function:
            Allows the user to save a specified table from the database as a csv into the local machine.
        
        Returns
            file (CSV):
                Database data saved into a csv file.
        """
        # Asks the user to choose a name for the file
        name_data = input("Create a name for the file in which the data  will be saved: ").replace(" ", "")

        # Extracts table form database
        df = self.extract_data()

        # Save table as csv
        df.to_csv(name_data, index=False)
    
    def load_data(self, data_file_path):
      """
      This function:
            Loads the csv files into Python as a dataframe.
        
        Returns
            dataframe (df)):
                Load data converted into a Pyhton dataframe.
      """

      # Loads data as dataframe
      df = pd.read_csv(data_file_path)
      return df 