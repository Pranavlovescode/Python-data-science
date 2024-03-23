# This is the case study 1 for the income.csv dataset
import pandas as pd
import numpy as np
import seaborn as sns

# Load the data
data = pd.read_csv('income(1).csv')
print(data.head())

# Making the copies of the data
data1 = data.copy()
# Printing the information of the data
print("The information of the data is as follows")
print(data1.info())

# Check for missing values
print('The missing values are as follows\n',data1.isnull().sum())


# Summary statistics of the data
# summary for numerical data
print("The summary for numerical data is as follows")
summary_num = data1.describe()
print(summary_num)

# summary for categorical data
print("The summary for categorical data is as follows")
print(data1.describe(include='object'))


print(data1['JobType'].value_counts())
print(np.unique(data1['JobType']))


data2 = pd.read_csv('income(1).csv',na_values=['?'])
print(data2['JobType'].value_counts())
print(data1.isnull().any(axis=1))
# Dropping the missing values
print("Droped the missing values")
data3=data1.dropna(axis=0)
print(data3)

# Finding the correlation between the numerical data
print("The correlation between the numerical data is as follows")
# Select only the numeric columns
numeric_cols = data3.select_dtypes(include=[np.number])
# Compute the correlation
correlation = numeric_cols.corr()
print(correlation)  