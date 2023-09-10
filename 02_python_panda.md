# Advanced Pandas in Python: A University Course Guide

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
