#!/usr/bin/python3

"""Read in the file diabetes.csv, and after obtaining the pandas dataframe, do the following:"""

"""(i) Print all the column names"""
import pandas as pd
a=pd.read_csv('diabetes.csv')
print(f'i) The columns names of the given files: ',a.columns.tolist())
print(f'----------------------------------------------------------')

"""(ii) Print the first 10 rows"""
a=pd.read_csv('diabetes.csv')
print(f'ii) The first 10 rows:', a.head(10))
print(f'----------------------------------------------------------')

"""(iii)Print the mean of the BloodPressure column values"""
a=pd.read_csv('diabetes.csv')
print(f'iii)The mean of the BloodPressure column values:', a['BloodPressure'].mean())
print(f'----------------------------------------------------------')

"""(iv)Print the first 4 rows of columns 3,4,5"""
a=pd.read_csv('diabetes.csv')
b=a.columns[3:6].tolist()
c=a[b][:4]
print(f'iv) The first 4 rows of columns 3,4,5: {c}')
print(f'-----------------------------------------------')

"""(v)Add another column ’NormalizedBP’ using (max-min) normalization to the dataframe as:
BP[i] -min(BP) / (max(BP) - min(BP))."""
bp_min=a['BloodPressure'].min()
bp_max=a['BloodPressure'].max()
a['NormalizedBP']=(a['BloodPressure']-bp_min)/(bp_max - bp_min)
b=a[['BloodPressure','NormalizedBP']].head()
print(f'New column:{b} ')
print(f'-----------------------------------------------')

"""(vi)Write a function categorize_age(age) that returns ”Youth”, ”Adult” or ”Senior”
based on the age brackets (1-18, 19-50, ¿50). Create a new column in the dataframe 
with this function called age category."""

def categorize_age(age):
    if 1 <= age <= 18:
        return "Youth"
    elif 19 <= age <= 50:
        return "Adult"
    else:
        return "Senior"

a['age_category'] = a['Age'].apply(categorize_age)
print(f'The new column is:', a['age_category'])

