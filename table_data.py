import pandas as pd


# function to load data from csv and transform to df
def load_data_from_csv(file_path):

    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded from {file_path} successfully.")
        return df
    except Exception as e:
        print(f"Error loading data from CSV: {e}")
        return None


if __name__ == "__main__":

    file_path = "../loan_payments.csv"

    df = load_data_from_csv(file_path)

    if df is not None:
        pd.set_option("display.max_columns", None)
        print(df.head(10))
        print(df.info())
