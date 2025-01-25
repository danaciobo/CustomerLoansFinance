import pandas as pd
import numpy as np


class DataFrameInfo:

    """
    A class to provide summary statistics and information about a DataFrame.

    Attributes:
        df (pd.DataFrame): The pandas DataFrame to analyze.
    """

    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        return self.df.dtypes

    def extract_statistics(self):
        return self.df.describe().loc[["mean", "50%", "std"]]

    def count_distinct_values(self):
        return self.df.select_dtypes(include=["category", "object"]).nunique()

    def get_shape(self):
        return self.df.shape

    def count_null_values(self):
        return self.df.isnull().sum().sort_values(ascending=False)

    def percentage_null_values(self):
        return (self.df.isnull().sum() / len(self.df)) * 100

    def print_head(self, n=5):
        print(self.df.head(n))
