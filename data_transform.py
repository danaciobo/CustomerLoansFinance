import pandas as pd
import numpy as np


class DataTransform:
    """
    A class that provides data transformation functions to clean and preprocess data.

    Attributes:
        df (pd.DataFrame): The pandas DataFrame to be transformed.
    """

    def __init__(self, df):
        self.df = df

    # converts date columns to datetime type
    def convert_to_datetime(self, columns):
        for col in columns:
            self.df[col] = pd.to_datetime(self.df[col], errors="coerce")
        return self.df

    # changes employment length to integer
    def clean_employment_length(self, column):
        mapping = {
            "< 1 year": 0.5,
            "1 year": 1,
            "2 years": 2,
            "3 years": 3,
            "4 years": 4,
            "5 years": 5,
            "6 years": 6,
            "7 years": 7,
            "8 years": 8,
            "9 years": 9,
            "10+ years": 10,
            np.nan: np.nan,
        }
        col_index = self.df.columns.get_loc(column)
        self.df.insert(col_index, "employment_term_years", self.df[column].map(mapping))
        self.df = self.df.drop(columns=[column])
        return self.df

    # converts term to numeric by extracting number
    def convert_term_to_numeric(self, column):
        col_index = self.df.columns.get_loc(column)
        self.df.insert(
            col_index,
            "term_months",
            self.df[column].str.extract(r"(\d+)").astype(float),
        )
        self.df = self.df.drop(columns=[column])
        return self.df

    # converts object colmuns to categorical data type
    def convert_categorical_columns(self, categorical_columns):
        self.df[categorical_columns] = self.df[categorical_columns].astype("category")
        return self.df
