# This is the case study 1 for the income.csv dataset
import pandas as pd
import numpy as np
import seaborn as sns

# Load the data
data = pd.read_csv('income(1).csv')
print(data.head())
print(data.describe())


# Printing the information of the data
print("The information of the data is as follows")
print(data.info())

# Check for missing values
print('The missing values are as follows\n',data.isnull().sum())