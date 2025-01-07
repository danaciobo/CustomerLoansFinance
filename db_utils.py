import yaml
import pandas as pd
from sqlalchemy import create_engine


credentials_file_path = "credentials.yaml"

def load_credentials(file_path):

  with open(file_path, 'r') as file:
    credentials = yaml.safe_load(file)
  return credentials



class RDSDatabaseConnector:
  def __init__(self, credentials):
    self.credentials = credentials
    self.engine = None


  def initialize_engine(self):
    try:
      self.engine = create_engine(
        f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@"
        f"{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/"
        f"{self.credentials['RDS_DATABASE']}"
        )
      print("Database engine initialized successfully.")
    except Exception as e:
          print(f"Error initializing database engine: {e}")

  def extract_data_to_df(self, table_name):

    if not self.engine:
      raise Exception("Engine is not initialized.")
    try:
      query = f"SELECT * FROM {table_name}"
      df = pd.read_sql(query, self.engine)
      print(f"Data extracted from table '{table_name}' successfully.")
      return df
    except Exception as e:
      print(f"Error extracting data: {e}")
      return None

  def save_data_to_csv(self, df, file_path):
    try:
      df.to_csv(file_path, index=False)
      print(f"DataFrame saved to {file_path}")
    except Exception as e:
      print(f"Error saving DataFrame to CSV: {e}")



if __name__ == "__main__":

    # Load credentials from a YAML file
    credentials = load_credentials(credentials_file_path)

    # Initialize the RDSDatabaseConnector with the credentials
    rds_connector = RDSDatabaseConnector(credentials)

    # Initialize the SQLAlchemy engine
    rds_connector.initialize_engine()

    # Extract data from the 'loan_payments' table
    table_name = "loan_payments"
    df = rds_connector.extract_data_to_df(table_name)

    # Save the DataFrame to a CSV file
    if df is not None:
        csv_file_path = "loan_payments.csv"
        rds_connector.save_data_to_csv(df, csv_file_path)