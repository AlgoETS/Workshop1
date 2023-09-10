# Pandas in Python: A Guide

---

## Table of Contents

1. [Introduction to Pandas](#introduction-to-pandas)
2. [Why Choose Pandas?](#why-choose-pandas)
3. [Understanding DataFrame](#understanding-dataframe)
4. [Data Wrangling Techniques](#data-wrangling-techniques)
5. [Advanced Pandas Functions](#advanced-pandas-functions)
6. [Pandas and AI](#pandas-and-ai)
7. [Useful Code Snippets](#useful-code-snippets)
8. [Polars: An Alternate Library](#polars-an-alternate-library)
9. [Further Resources](#further-resources)

---

## 1. Introduction to Pandas

Pandas is a Python library designed to make data manipulation and analysis more intuitive and effective.

---

## 2. Why Choose Pandas?

### Data Cleaning and Analysis

Pandas simplifies the process of data cleaning and analysis, making it easier to gain insights from your datasets.

### Versatility

Pandas is highly flexible, capable of working with various data sources and formats.

---

## 3. Understanding DataFrame

DataFrame is the primary data structure in Pandas, resembling a spreadsheet or SQL table.

### Key Features

- **Labeled Axes**: Simplifies data manipulation.
- **Resizable**: Easily add or remove columns.
- **Supports Different Data Types**: Handle integers, floats, strings, and more in different columns.


## Creating DataFrames

### From a CSV File

To create a DataFrame from a CSV file, use the `pd.read_csv` function.

```python
df = pd.read_csv('telco_churn.csv')
```

### From a Dictionary

To create a DataFrame from a dictionary, use `pd.DataFrame.from_dict`.

```python
tempdict = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
dictdf = pd.DataFrame.from_dict(tempdict)
```

## Reading DataFrames

### Top and Bottom Rows

To view the top `n` rows, use `df.head(n)`. To view the bottom `n` rows, use `df.tail(n)`.

```python
df.head(10)
df.tail(15)
```

### Columns and Data Types

To see the column names and data types, use `df.columns` and `df.dtypes`.

```python
df.columns
df.dtypes
```

### Summary Statistics

For numerical columns, use `df.describe()`. To include object data types, use `df.describe(include='object')`.

```python
df.describe()
df.describe(include='object')
```

## Filtering Data

### Columns

To filter columns, you can use either dot notation or bracket notation.

```python
df.State
df['International plan']
df[['State', 'International plan']]
```

### Rows

To filter rows based on conditions, use boolean indexing.

```python
df[df['International plan']=='No']
df[(df['International plan']=='No') & (df['Churn']==True)]
```

## Indexing

### Using `iloc`

To index with integer-location based indexing, use `df.iloc[]`.

```python
df.iloc[14]
df.iloc[14,-1]
df.iloc[22:33]
```

### Using `loc`

To index with label-based indexing, use `df.loc[]`.

```python
state = df.copy()
state.set_index('State', inplace=True)
state.loc['OH']
```


### Creating a DataFrame

```python
# Create a DataFrame from a dictionary
import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 24, 35],
        'Occupation': ['Engineer', 'Doctor', 'Teacher']}

df = pd.DataFrame(data)
```

### Viewing Data

```python
# Display the first 5 rows
df.head()

# Display the last 5 rows
df.tail()
```

### Information about Data

```python
# Get the summary
df.info()

# Get the shape
df.shape
```

### Data Selection

```python
# Select a single column by column name
df['Name']

# Select multiple columns by column names
df[['Name', 'Age']]
```

### Data Filtering

```python
# Rows where Age is greater than 25
df[df['Age'] > 25]

# Rows where Occupation is 'Engineer'
df[df['Occupation'] == 'Engineer']
```

### Handling Missing Data

```python
# Drop rows with any missing values
df.dropna()

# Replace missing values with a specified value
df.fillna(value=0)
```

### Basic Statistics

```python
# Calculate the mean of all numeric columns
df.mean()

# Calculate the standard deviation
df.std()
```

### Data Manipulation

```python
# Adding a new column
df['Salary'] = [50000, 60000, 55000]

# Dropping a column
df.drop('Salary', axis=1, inplace=True)
```

### Data Aggregation

```python
# Count of unique values in a column
df['Occupation'].value_counts()

# Sum of all ages
df['Age'].sum()
```

---

## 4. Data Wrangling Techniques

Data wrangling is the process of cleaning and structuring data. Pandas offers multiple ways to achieve this.

### Tidy Data Principles

In a tidy dataset, each column represents a variable, and each row represents an observation.

### Common Operations Cheatsheet

- **Row Filtering**: `df[df.Length > 7]`
- **Remove Duplicates**: `df.drop_duplicates()`
- **Random Sampling**: `df.sample(frac=0.5)`

---

## 5. Advanced Pandas Functions

### Data Aggregation and Grouping

```python
# Group by a column and calculate mean
df.groupby('column_name').mean()
```

### Pivot Tables

```python
# Create a pivot table
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
```

### Time Series Analysis

```python
# Converting a column to datetime
df['datetime_column'] = pd.to_datetime(df['datetime_column'])
```

---

## 6. Pandas and AI

Pandas can be a powerful tool in AI for data preprocessing and feature engineering.

### Data Preprocessing

```python
# Standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['col1', 'col2']] = scaler.fit_transform(df[['col1', 'col2']])
```

### Feature Engineering

```python
# Creating interaction terms
df['interaction_term'] = df['col1'] * df['col2']
```

### Model Training

```python
# Using Pandas DataFrame with scikit-learn
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(df[['feature1', 'feature2']], df['target'])
```

### Panda AI
PandasAI is a Python library that enhances the capabilities of the popular data manipulation and analysis library, Pandas, by integrating Generative AI. It allows you to interact with your data in a conversational manner, asking questions in natural language and getting precise answers.PandasAI leverages Generative AI to understand the questions you ask and generates Python code to answer them. The code is then executed, and the results are returned to you.

```
from pandasai import SmartDataframe
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "country": ["USA", "UK", "France", "Germany"],
    "gdp": [20.8, 2.8, 2.5, 3.8]
})

# Convert to SmartDataframe
df = SmartDataframe(df)

# Query in natural language
df.chat('Which country has GDP greater than 3 trillion?')
```


```
# Clean data
df.clean_data()

# Impute missing values
df.impute_missing_values()

# Generate features
df.generate_features()

```

---

## 7. Useful Code Snippets

### Reading Data

```python
# From a local CSV file
mydata_csv = pd.read_csv("path/to/file.csv")

# From an online source
mydata_url = pd.read_csv("http://example.com/data.csv")

# From an Excel file
mydata_excel = pd.read_excel("path/to/file.xlsx", sheet_name="Sheet1")
```

---

## 8. Polars: An Alternate Library

Polars is an alternative to Pandas for data manipulation, optimized for performance.

```python
# From a local CSV file
mydata_csv = pl.read_csv("path/to/file.csv")

# From an online source
mydata_url = pl.read_csv("http://example.com/data.csv")
```

---

## 9. Further Resources

- [Pandas Official Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Polars GitHub Repository](https://github.com/pola-rs/polars)
