import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Plotter:
    """
    A class for visualizing aspects of the DataFrame,
    including missing values, skewness, outliers, and correlation matrix.

    Attributes:
        df (pd.DataFrame): The pandas DataFrame to be visualized.
    """

    def __init__(self, df):
        self.df = df

    # method that plots the number of missing values for each column that contains null values.
    def plot_nulls(self, title="Missing Values Before/After Handling"):
        null_counts = self.df.isnull().sum()
        null_counts = null_counts[null_counts > 0]
        null_counts.sort_values(ascending=False, inplace=True)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=null_counts.index, y=null_counts.values, color="#2E8B57")
        plt.title(title)
        plt.ylabel("Number of Missing Values")
        plt.xticks(rotation=45)
        plt.show()

    # method that plots graphs for the numerical columns to visualize skewness.
    def plot_skewness(self, columns, title="Skewness of Columns"):
        self.df[columns].hist(bins=50, figsize=(15, 10))
        plt.suptitle(title)
        plt.show()

    #  method that creates boxplots for the specified numerical columns to visualize outliers.
    def plot_outliers(self, columns, title="Outliers before changes"):
        num_cols = len(columns)
        num_rows = (num_cols // 3) + (num_cols % 3 > 0)  # Calculate rows dynamically

        plt.figure(figsize=(15, 5 * num_rows))  # Adjust figure size based on rows

        for idx, col in enumerate(columns, 1):
            plt.subplot(num_rows, 3, idx)
            sns.boxplot(x=self.df[col])
            plt.title(f"Outliers in {col}")

        plt.tight_layout()  # Adjust layout to prevent overlap
        plt.show()

    # Plots the correlation matrix of the DataFrame, considering only numeric columns.
    def plot_correlation_matrix(self, title="Correlation Matrix", figsize=(12, 8)):

        numeric_df = self.df.select_dtypes(include=[np.number])

        if numeric_df.empty:
            print("No numeric columns found for correlation matrix.")
            return

        plt.figure(figsize=figsize)
        sns.heatmap(
            numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5
        )
        plt.title(title)
        plt.show()
