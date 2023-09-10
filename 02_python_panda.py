# Pandas in Python: A University Course Guide

---

## Table of Contents
1. [Introduction](#introduction)
2. [Why Use Pandas?](#why-use-pandas)
3. [What is a DataFrame?](#what-is-a-dataframe)
4. [Data Wrangling with Pandas](#data-wrangling-with-pandas)
5. [Code Snippets](#code-snippets)
6. [Polars: An Alternative to Pandas](#polars-an-alternative-to-pandas)
7. [Further Reading](#further-reading)

---

## Introduction

Pandas is a Python library that provides flexible and expressive data structures designed to make working with labeled data more intuitive and efficient.

---

## Why Use Pandas?

### Data Analysis and Cleaning

Pandas provides a convenient way to clean and analyze large datasets, allowing you to extract meaningful insights and prepare data for further uses.

### Flexibility

Pandas works well with a variety of data sources and formats, making it a versatile choice for different projects.

---

## What is a DataFrame?

A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. It is the most commonly used pandas object and is similar to a spreadsheet or SQL table.

### Characteristics

- **Labeled axes**: Rows and columns are labeled for easy data manipulation.
- **Size mutable**: DataFrames can be resized by adding or deleting columns.
- **Heterogeneous data**: Different columns can have different data types like integers, floats, and strings.

---

## Data Wrangling with Pandas

Data wrangling involves cleaning, structuring and enriching raw data into a format for better decision making. Pandas offers a variety of techniques to wrangle data.

### Tidy Data

In a tidy dataset, each variable is saved in its own column, and each observation is saved in its own row. This structure complements Pandas' vectorized operations.

### Cheatsheet for Common Operations

#### Subset Observations (Rows)

- `df[df.Length > 7]`: Extract rows that meet logical criteria.
- `df.drop_duplicates()`: Remove duplicate rows.
- `df.sample(frac=0.5)`: Randomly select fraction of rows.

#### Subset Variables (Columns)

- `df[['width', 'length', 'species']]`: Select multiple columns with specific names.
- `df['width'] or df.width`: Select single column with specific name.
- `df.filter(regex='regex')`: Select columns whose name matches regular expression regex.

#### Subset Both Rows and Columns

- `df.iloc[10:20]`: Select rows 10-20.
- `df.iloc[:, [1, 2, 5]]`: Select columns in positions 1, 2 and 5.

#### Access Single Value

- `df.iat[1, 2]`: Access single value by index.
- `df.at[4, 'A']`: Access single value by label.

---

## Code Snippets

### Reading Data

```python
import pandas as pd

# Reading from a CSV file
mydata_csv = pd.read_csv("C:\\\\Users\\\\Username\\\\Documents\\\\file1.csv")
# Reading from an online source
mydata_url = pd.read_csv("http://winterolympicsmedals.com/medals.csv")
# Reading from an Excel file
mydata_excel = pd.read_excel("https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls", sheet_name="Data 1", skiprows=2)
```

## Polars: An Alternative to Pandas

Polars is another data manipulation library that can be used as an alternative to Pandas. It also provides a variety of functionalities for data wrangling and manipulation but is optimized for performance.

```python
import polars as pl

# Reading from a local CSV file
mydata_csv = pl.read_csv("/home/file1.csv")
# Reading from an online source
mydata_url = pl.read_csv("http://winterolympicsmedals.com/medals.csv")
```

## Further Reading
