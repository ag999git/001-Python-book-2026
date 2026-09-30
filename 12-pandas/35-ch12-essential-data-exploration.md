# Research Project: Essential Data Exploration in Pandas

## Research Question

> How can a Data Analyst quickly understand the structure, quality, and patterns of an unknown dataset using Pandas DataFrame exploration methods such as `.head()`, `.tail()`, `.sample()`, `.info()`, `.describe()`, `.value_counts()`, and `.nunique()`?
>
> Using the **Palmer Penguins dataset**, perform a systematic exploration and explain how each method contributes to understanding the dataset from both a structural and statistical perspective.

***

## Learning Objectives

You will learn to:

* Inspect raw data using `.head()`, `.tail()`, `.sample()`
* Understand structure using `.info()`
* Generate statistical summaries using `.describe()`
* Analyze categorical distributions using `.value_counts()` and `.nunique()`
* Interpret outputs meaningfully (not just run code)

## Flowchart showing the steps of Essential Data Exploration in Pandas

![Essential Data Exploration in Pandas](../resources/S12-LR-ch12-Essential-Data-Exploration.png)

**Reading the figure**

- **Step 1:** Load the Palmer Penguins dataset into a DataFrame with `sns.load_dataset('penguins')`.
- **Step 2:** Peek at the rows: `head()` for the first rows, `tail()` for the last rows, `sample()` for random rows.
- **Step 3:** Structural summary with `info()`: column names, data types and non-null counts.
- **Step 4:** Statistical summary with `describe()`: count, mean, standard deviation, minimum, quartiles and maximum (and, with `include='all'`, the text columns too).
- **Step 5:** `nunique()` counts the distinct values in each column.
- **Step 6:** `value_counts()` shows how often each species and each island appears.
- **Step 7:** `isnull().sum()` counts the missing values in each column.

## Script showing usage of Pandas DataFrame exploration methods such as `.head()`, `.tail()`, `.sample()`, `.info()`, `.describe()`, `.value_counts()`, and `.nunique()`

```python
import pandas as pd
import seaborn as sns

# STEP 1: Load Dataset
# The dataset is loaded from seaborn
df = sns.load_dataset('penguins')

print("STEP 1: Dataset Loaded")
print(df.head())
# OUTPUT HINT:
# species island bill_length_mm bill_depth_mm flipper_length_mm body_mass_g sex
# 0 Adelie Torgersen 39.1 18.7 181 3750 Male
# 1 Adelie Torgersen 39.5 17.4 186  3800 Female
# 2 Adelie Torgersen 40.3 18.0 195  3250 Female
# 3 Adelie Torgersen NaN NaN NaN NaN NaN    
# 4 Adelie Torgersen 36.7 19.3 193  3450 Female


# STEP 2: Peeking at Data
# These methods help quickly view data without loading entire dataset

print("\nSTEP 2A: First 5 Rows using head()")
print(df.head())
# OUTPUT HINT:
# head() → shows first 5 rows of the dataset, useful for a quick peek at the structure and content of the data.

print("\nSTEP 2B: Last 5 Rows using tail()")
print(df.tail())
# OUTPUT HINT:
# tail() → shows last 5 rows of the dataset, useful for checking if there are any anomalies 
# or patterns towards the end of the data, such as missing values or outliers.

print("\nSTEP 2C: Random Sample using sample()")
print(df.sample(5))
# OUTPUT HINT:
# sample(5) → shows a random sample of 5 rows from the dataset, which can help identify if 
# there are any inconsistencies or patterns that are not visible in the first or last few rows.

# OVERALL OUTPUT HINT:
# head() → first rows
# tail() → last rows
# sample() → random rows


# STEP 3: Structural Summary
# Provides column names, data types, and missing values

print("\nSTEP 3: DataFrame Info")
df.info()

# OUTPUT HINT:
# Columns: species, island, bill_length_mm, etc.
# Shows:
# - Non-null counts
# - Data types (float, object)
# - Memory usage


# STEP 4: Statistical Summary
# Gives numeric summary (mean, std, min, max, etc.)

print("\nSTEP 4: Statistical Summary (Numeric Columns)")
print(df.describe())
# OUTPUT HINT:
# count → number of non-null entries
# mean → average value
# std → standard deviation (spread of data)
# min → minimum value
# 25% → first quartile (25th percentile)
# 50% → median (50th percentile)
# 75% → third quartile (75th percentile)
# max → maximum value
# ACTUAL OUTPUT
# bill_length_mm bill_depth_mm flipper_length_mm body_mass_g
# count 342.000000 342.000000 342.000000 342.000000
# mean 43.921930 17.151170 200.915205 4201.754386
# std 5.459584 1.974793 14.061714 801.954536
# min 32.100000 13.100000 172.000000 2700.000000
# 25% 39.225000 15.600000 190.000000 3550.000000
# 50% 44.450000 17.300000 197.000000 4050.000000
# 75% 48.500000 18.700000 213.000000 4750.000000
# max 59.600000 21.500000 231.000000 6300.000000


print("\nSTEP 4B: Statistical Summary (All Columns)")
print(df.describe(include='all'))

# OUTPUT HINT:
# Numeric → mean, std, quartiles
# Categorical → unique, top, freq

# ACTUAL OUTPUT
# species island bill_length_mm bill_depth_mm flipper_length_mm body_mass_g sex
# count 344 344 342 342 342 342 333 
# unique 3 3 NaN NaN NaN NaN 2
# top Adelie Biscoe NaN NaN NaN NaN Male
# freq 152 168 NaN NaN NaN NaN 168  
# mean NaN NaN 43.921930 17.151170 200.915205 4201.754386 NaN
# std NaN NaN 5.459584 1.974793 14.061714 801.954536 NaN
# min NaN NaN 32.100000 13.100000 172.000000 2700.000000 NaN
# 25% NaN NaN 39.225000 15.600000 190.000000 3550.000000 NaN
# 50% NaN NaN 44.450000 17.300000 197.000000 4050.000000 NaN
# 75% NaN NaN 48.500000 18.700000 213.000000 4750.000000 NaN
# max NaN NaN 59.600000 21.500000 231.000000 6300.000000 NaN

# STEP 5: Unique Values Analysis

print("\nSTEP 5A: Unique Count per Column")
print(df.nunique())

# ACTUAL OUTPUT:
# species 3
# island 3
# bill_length_mm 164
# bill_depth_mm 80
# flipper_length_mm 55  
# body_mass_g 94
# sex 2 
# dtype: int64

# STEP 6: Value Counts (Categorical Analysis)

print("\nSTEP 6A: Species Distribution")
print(df['species'].value_counts())

# ACTUAL OUTPUT:
# Adelie 152
# Gentoo 124
# Chinstrap 68

print("\nSTEP 6B: Island Distribution")
print(df['island'].value_counts())

# ACTUAL OUTPUT:
# Biscoe 168
# Dream 124
# Torgersen 52


# STEP 7: Handling Missing Values (Optional Insight)

print("\nSTEP 7: Missing Values Check")
print(df.isnull().sum())
# ACTUAL OUTPUT:
# species 0
# island 0
# bill_length_mm 2
# bill_depth_mm 2
# flipper_length_mm 2
# body_mass_g 2
# sex 11

# ERROR EXAMPLE (COMMENTED)
# print(df['wrong_column'].value_counts())  # KeyError



```

## Comparison Table

| Method           | Purpose         | Output Type | When to Use      |
| ---------------- | --------------- | ----------- | ---------------- |
| .head()          | View first rows | DataFrame   | Quick preview    |
| .tail()          | View last rows  | DataFrame   | Check end data   |
| .sample()        | Random rows     | DataFrame   | Avoid bias       |
| .info()          | Structure       | Summary     | Data cleaning    |
| .describe()      | Statistics      | DataFrame   | Numeric insights |
| .nunique()       | Unique count    | Series      | Category size    |
| .value\_counts() | Frequency       | Series      | Distribution     |

## Key Difference Table

| Feature  | .describe()           | .value\_counts()   |
| -------- | --------------------- | ------------------ |
| Works on | Numeric (default)     | Single column      |
| Output   | Summary stats         | Frequency count    |
| Use case | Distribution overview | Category dominance |

## Some Common errors/ omissions

Given below are some common errors/ omissions in Essential Data Exploration in Pandas

```python
# ERROR 1: Wrong column name. Pandas is case-sensitive and exact-match on column names is required. 
# A typo or case difference will cause a KeyError.    
# df['Species']  # KeyError (case-sensitive)

# ERROR 2: Using value_counts on DataFrame. 
# value_counts is a Series method, not DataFrame. You must specify a column to use it on. 
# df.value_counts()  # Works differently than expected

# ERROR 3: describe on non-numeric. By default, describe() only summarizes numeric columns. 
# If you want to include categorical columns, you must specify include='all'. 
# df.describe()  # Ignores categorical unless include='all'

# ERROR 4: Not handling missing values. If your dataset has missing values, it can affect your analysis. 
# Always check for missing values and decide how to handle them (e.g., drop, fill, etc.).
# df.isnull().sum()  # Check for missing values 

# ERROR 5: Not checking unique values. If you have categorical data, it's important to check the unique values and their
# counts to understand the distribution of your data.
# df['species'].unique()  # Check unique values in 'species' column 

# ERROR 6: Not using .to_frame() when needed. If you want to convert a Series to a DataFrame, you need to use .to_frame().
# df['species'].value_counts().to_frame()  # Convert Series to DataFrame for better presentation    

# ERROR 7: Not checking data types. If your columns have the wrong data type, it can affect your analysis and calculations.
# Always check and convert data types as needed.
# df.dtypes  # Check data types of columns  

# ERROR 8: Not using .head() or .tail() for large datasets. If you print a large DataFrame without using .head() or .tail(),
# it can flood your console and make it hard to read. Always use these methods to preview your data.
# print(df)  # Avoid printing entire DataFrame for large datasets   

# ERROR 9: Not using .info() for a quick overview. The .info() method provides a concise summary of the DataFrame,
# including the number of non-null entries and data types. Not using it can lead to missing important information about your dataset.
# df.info()  # Get concise summary of DataFrame 

```

## Conclusion

> Data exploration is the first and most critical step in data analysis. These simple Pandas methods provide powerful insights within seconds, helping analysts understand structure, detect issues, and guide further analysis.
