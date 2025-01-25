# Customer Loans Finance

# Financial Loan Data Transformation

This project involves transforming and cleaning a customer loan dataset to prepare it for analysis. The goal is to handle missing data, remove highly correlated features, detect and correct skewed distributions, and remove outliers. The project also includes visualizations of key transformations to monitor the progress.

## Features

- **Data Cleaning**: Handles missing values, cleans date columns, and converts categorical data to appropriate types.
- **Handling Missing Values**: Imputes missing data using both domain-specific calculations and general imputation techniques.
- **Outlier Detection & Removal**: Detects and removes outliers based on a threshold.
- **Skewed Data Handling**: Identifies skewed columns and transforms them to make data more normally distributed.
- **Correlation Matrix**: Visualizes correlations and removes highly correlated columns based on a specified threshold.
- **Data Saving**: Saves the transformed dataset to CSV files.

## File Structure:

- **Python Scripts**:
  - `data_transform.py`: Handles the main data transformations such as cleaning and preprocessing.
  - `data_frame_transform.py`: Provides additional transformation functions for more specific data manipulation.
  - `data_frame_info.py`: Helps summarize and describe the dataset, with utility functions to explore it.
  - `plotter.py`: Contains functions for visualizing the data at various stages of transformation.
  - `table_data.py`: Loads the dataset from CSV files and manages basic data operations.

- **Jupyter Notebook**
 - `data_transformation.ipynb`: A Jupyter notebook for running the data transformations and analysis.

- **Output Files**:
  - `processed_loan_data.csv`: The final cleaned and transformed dataset (optional).
  - `financial_loan_data.csv`: Intermediate file containing the data during transformations (optional).

- **Other Files**:
  - `README.md`: Contains the documentation for the project.
  - `requirements.txt`: Lists all necessary dependencies (e.g., pandas, numpy, matplotlib).



## Prerequisites

To run this project, you’ll need the following Python packages:

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- jupyter


You can install these dependencies using `pip`:

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
