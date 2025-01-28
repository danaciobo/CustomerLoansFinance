# Customer Loans Finance

## Financial Loan Data Transformation & Loss Analysis


This project involves transforming and analyzing a customer loan data set to assess financial risk. It focuses on cleaning the data, handling missing values, and detecting outliers and highly correlated features. The current state of loans is evaluated to visualize projected payments over time. The analysis includes calculating the loss from charged-off loans, projecting potential losses from loans at risk, and identifying indicators that may predict default.


## Data Transformation & Preprocessing

- **Data Cleaning**: handles missing values, cleans date columns, and converts categorical data to appropriate types.
- **Handling Missing Values**: fills missing data using both domain-specific calculations and general imputation techniques.
- **Outlier Detection & Removal**: detects and removes outliers based on a threshold.
- **Skewed Data Handling**: identifies skewed columns and transforms them to make data more normally distributed.
- **Correlation Matrix**: visualizes correlations and removes highly correlated columns based on a specified threshold.

## Loss Analysis

- **Current State of the Loans**: calculates the percentage of loans recovered compared to the total amount due, including interest, and estimates how much will be paid back in the next 6 months.
- **Calculating Loss, Projected and Possible Loss**: Calculates the percentage of charged-off loans and the total amount paid before being charged off. It also estimates the potential loss for customers behind on payments and projects the loss if these loans continue until the end of the term.
- **Indicators of Loss**: Identifies columns like loan grade, employment length, purpose of loan, and home ownership that may indicate default risk. Customers behind on payments are compared to charged-off customers to identify if loans are at risk.

## File Structure:

- **Python Scripts**:
  - `data_transform.py`: Handles the main data transformations such as cleaning and preprocessing.
  - `data_frame_transform.py`: Provides additional transformation functions for more specific data manipulation.
  - `data_frame_info.py`: Helps summarize and describe the dataset, with utility functions to explore it.
  - `plotter.py`: Contains functions for visualizing the data at various stages of transformation.
  - `table_data.py`: Loads the dataset from CSV files and manages basic data operations.
  - `data_transformation.ipynb`: A Jupyter notebook for running the data transformations and analysis.
  - `data_analysis_current_state.ipynb`: Jupyter notebook analyzing the current state of the loan data.
  - `data_analysis_charged_off.ipynb`: Jupyter notebook analyzing the impact of charged-off loans.
  - `data_analysis_late_loans.ipynb`: Jupyter notebook analyzing loans that are behind on payments.
  - `data_analysis_indicators_loss.ipynb`: Jupyter notebook that calculates and projects loss and revenue indicators.


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
