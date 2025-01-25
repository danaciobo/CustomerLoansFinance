import pandas as pd
import numpy as np
from scipy.stats import boxcox, zscore


class DataFrameTransform:
    """
    A class providing data transformation methods for cleaning, imputing, and modifying a DataFrame.

    Attributes:
        df (pd.DataFrame): The pandas DataFrame to be transformed.
    """

    def __init__(self, df):
        self.df = df

    # method that checks for missing values in the DataFrame and provides a summary of null counts and percentages.
    def check_nulls(self):
        null_counts = self.df.isnull().sum()
        null_percentage = (null_counts / len(self.df)) * 100
        null_summary = pd.DataFrame(
            {"null_count": null_counts, "null_percentage": null_percentage}
        ).sort_values(by="null_percentage", ascending=False)
        return null_summary

    #  method that drops columns from the DataFrame that have a higher percentage of missing values than 50%
    def drop_columns_by_nulls(self, threshold=50):
        null_summary = self.check_nulls()
        columns_to_drop = null_summary[
            null_summary["null_percentage"] > threshold
        ].index
        self.df = self.df.drop(columns=columns_to_drop)
        print(f"Dropped columns: {list(columns_to_drop)}")
        return self.df

    # fills missing values for specific columns using calculations.
    def impute_calculated_values(self):

        # fills 'int_rate' using the formula: (instalment * term_months / loan_amount) * 100
        if "int_rate" in self.df.columns and self.df["int_rate"].isnull().sum() > 0:
            mask = (
                self.df["int_rate"].isnull()
                & self.df["instalment"].notnull()
                & self.df["loan_amount"].notnull()
                & self.df["term_months"].notnull()
            )
            self.df.loc[mask, "int_rate"] = (
                (self.df.loc[mask, "instalment"] * self.df.loc[mask, "term_months"])
                / self.df.loc[mask, "loan_amount"]
            ) * 100

        # fills 'term_months' using the formula: loan_amount / instalment * 12 & taking closest value to 36 or 60
        if (
            "term_months" in self.df.columns
            and self.df["term_months"].isnull().sum() > 0
        ):
            mask = (
                self.df["term_months"].isnull()
                & self.df["loan_amount"].notnull()
                & self.df["instalment"].notnull()
            )
            # Calculate the estimated term that doesn't take into account interest
            estimated_term = (
                self.df.loc[mask, "loan_amount"] / self.df.loc[mask, "instalment"]
            ) * 12

            # Assign the closest value between 36 and 60
            self.df.loc[mask, "term_months"] = estimated_term.apply(
                lambda x: 36 if abs(x - 36) < abs(x - 60) else 60
            )

        # fills 'funded_amount' using loan amount as the same in most cases
        if (
            "funded_amount" in self.df.columns
            and self.df["funded_amount"].isnull().sum() > 0
        ):
            mask = self.df["funded_amount"].isnull() & self.df["loan_amount"].notnull()
            self.df.loc[mask, "funded_amount"] = self.df.loc[mask, "loan_amount"]

        print("Calculated imputations applied successfully.")

        return self.df

    # fills rest of missing values with median value for numeric columns and mode for categorical
    def impute_missing_values(self):

        for col in self.df.columns:
            if self.df[col].isnull().any():
                if self.df[col].dtype in ["float64", "int64"]:
                    # fills numerical columns with median
                    self.df.loc[self.df[col].isnull(), col] = self.df[col].median()
                else:
                    # fills categorical columns with mode
                    mode_value = self.df[col].mode()
                    self.df.loc[self.df[col].isnull(), col] = (
                        mode_value[0] if not mode_value.empty else "Unknown"
                    )

        return self.df

    # identifies skewed columns
    def detect_skewed_columns(self, threshold=0.75):
        skewness = self.df.skew(numeric_only=True)
        skewed_columns = skewness[abs(skewness) > threshold].index.tolist()
        return skewed_columns

    # transforms the skewed columns using box-cox method
    def transform_skewed_columns(self, columns):

        for col in columns:
            if (self.df[col] > 0).all():  # Check if all values are positive
                self.df[col], _ = boxcox(
                    self.df[col] + 1e-5
                )  # Add small constant to avoid zero values
            else:
                # Apply square root transformation for non-negative values
                self.df[col] = np.sqrt(self.df[col].clip(lower=0))
        return self.df

    # method that removes outliers using IQR method
    def remove_outliers(self, columns=None, factor=1.75):

        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns

        before_removal = len(self.df)

        for col in columns:
            if self.df[col].isnull().all():
                print(f"Skipping {col}: all values are NaN.")
                continue

            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - (factor * IQR)
            upper_bound = Q3 + (factor * IQR)

            self.df = self.df[
                (self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)
            ]
            removed = before_removal - len(self.df)
            print(f"Removed {removed} outliers from {col}.")
            before_removal = len(self.df)

        print("Outliers removed based on IQR method.")
        return self.df

    # method that removes highly correlated columns
    def remove_highly_correlated_columns(self, threshold=0.9):

        numeric_df = self.df.select_dtypes(include=[np.number])

        if numeric_df.empty:
            print("No numeric columns found for correlation analysis.")
            return []

        correlation_matrix = numeric_df.corr()

        cols_to_drop = set()

        # exclude diagonal elements (correlation with itself)
        upper_triangle = correlation_matrix.where(
            np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)
        )

        # finding highly correlated columns and add to the drop list
        for col in upper_triangle.columns:
            if col == "instalment":
                continue  # Skip 'instalment' column as needed for calculations later
            high_correlation = upper_triangle[col][upper_triangle[col] > threshold]
            if not high_correlation.empty:
                print(
                    f"Dropping {col} due to high correlation with {list(high_correlation.index)}"
                )
                cols_to_drop.add(col)

        # Drop columns with high correlation
        self.df.drop(columns=list(cols_to_drop), inplace=True)

        self.df.dropna(axis=1, how="all", inplace=True)

        print(
            f"Removed {len(cols_to_drop)} highly correlated columns: {list(cols_to_drop)}"
        )

        return self.df
