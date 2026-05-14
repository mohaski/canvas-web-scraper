# What are Pandas Dataframes and Series?

# What are Pandas Dataframes and Series?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What are Pandas Dataframes and Series?

Icon Progress Bar (browser only)

10 min read

This topic centers around understanding the key data structures of Pandas and how to access and manipulate information contained within them. The two workhorse data structures are:

* **Pandas Series:** A one-dimensional labeled array that holds data of any type (numbers, text, etc.) and allows you to access elements by their labels. Think of it as a single, named column in a spreadsheet. Series support specialized numeric and string operations*—*making data cleaning and transformation across records easy.
* **Pandas DataFrame:** A two-dimensional, size-mutable labeled data structure with rows and columns, like a spreadsheet. It can hold different data types in each column and allows you to access data by row labels or column names. Imagine it as a full-fledged spreadsheet with labeled rows and columns.

### Loading Data

Data can be loaded into pandas DataFrames and Series from a variety of sources. Some source include other Python data structures (dictionaries, lists, etc.) or files on disk (CSVs, JSONs, excel files). Below are some key commands that you should be familiar with and we will go through how to use:

* **pd.DataFrame():** Calling this on a list of dictionaries or a nested list will create a pandas DataFrame. Pandas will interpret dictionary keys as column names automatically.
* **pd.Series():** Calling this on a dictionary or a list will create a pandas Series. When called on a dictionary, Pandas will interpret dictionary keys as the named index automatically.
* **pd.read\_csv():** Loads delimited text data (e.g., a CSV) into a DataFrame given a file path name is provided. Has a lot of options for different delimiters, parsing headers to get column names, etc. Intelligently parses columns and converts columns to appropriate data types automatically.

#### Essential DataFrame and Series Attributes

* **.index:** Gets the named indices for Series and for rows of DataFrame
* **.columns:** Gets the named indices for columns of DataFrame
* **.shape:** Gets the numbers of rows and columns in a DataFrame
* **.dtype:** Returns the Python data type of a Series
* **.values:** Returns the data contained with a pandas Series or DataFrame as a numpy array

#### High Level Data Inspection

* **DataFrame.info():** Provides a high level overview of a DataFrame. This includes column names, data type within each column, total number of rows, and number of missing values in each column. This is a starting point for digging into a dataset you have just loaded into a DataFrame.
* **DataFrame.summary():** Provides key summary statistics for numeric columns. These include min, max, mean, quartiles, standard deviation, etc. Allows you to quickly assess the scale and spread of each numeric column and quickly identify columns potentially possessing outliers.
* **DataFrame.head():** Gets the first five rows of the dataset. Always useful when you want to look explicitly at the structure of the data.
* **DataFrame.tail():** Gets the last five rows of the dataset.

#### Pandas Data Types

Pandas encodes data within a Series (or columns of a DataFrame) with particular data types (dtypes). You will encounter these data types frequently when inspecting columns with the .info() method or converting a column from one dtype to another:

**Numeric Types:**

* **int64 (integer):** Represents whole numbers, typically stored as 64-bit integers. This is the default integer type in pandas.
* **float64 (floating-point):** Represents numbers with decimal points, typically stored as 64-bit floating-point numbers.
* **int32 (integer):** Similar to int64 but uses 32 bits, suitable for smaller integer ranges.
* **float32 (floating-point):** Similar to float64 but uses 32 bits, offering less precision but potentially faster processing for large datasets.

**Boolean Type:**

* **bool:** Represents Boolean values (True or False).

**Object Type:**

* **object:** This is a catch-all type for data that doesn't fit into a more specific category. It can hold strings, lists, dictionaries, or other complex data types. However, using object can be less efficient for numerical operations.

**Time-Based Types:**

* **datetime64[ns]:** Special data type ideal for parsing datetimes.

**Category Type:**

* **Category:** This type represents a collection of text labels (similar to strings) but with additional metadata for efficient handling of categorical data.

### Accessing Data

Pandas DataFrames and Series have accessor attributes that can be used to both retrieve columns/rows of interest and to reassign values within these selected subsets.

**The .loc[] accessor:** Used for accessing data by label within a DataFrame. It allows you to retrieve specific rows, columns, or even a subset of both based on their named label and/or using Boolean conditions.

**The .iloc[] accessor:** Used for accessing data by integer positional indexing of rows and columns within a DataFrame. Similar to accessing data in Python nested lists and multidimensional Numpy arrays.

#### Setting Column Names and Indices

* **.rename():** Renames columns or index labels in your DataFrame or Series.
* **.set\_index():** Converts a column into the new row index for your DataFrame.
* **.sort\_index():** Sorts your DataFrame or Series by its current index labels.

#### Pandas Vectorization

* **Vectorized Operations:** Instead of writing loops to manipulate data element by element, vectorized operations apply calculations or functions to entire arrays simultaneously. This takes advantage of the underlying hardware capabilities for efficient parallel processing.
* **Built-in Functionality:** Pandas provides a rich set of vectorized functions like .mean(), .sum(), .apply(), and comparison operators (e.g., >, <). These functions operate on entire Series or DataFrames, enabling efficient calculations and transformations.
* **Broadcasting:** This mechanism allows vectorized operations between Series or DataFrames with different shapes under certain conditions. For instance, adding a scalar value to a Series performs the addition element-wise.

### Transforming Data

* **.replace():** A method useful for replacing values in a Series or a DataFrame with other values. Often used with a dictionary that provides the mapping between old and new values.
* **.map(): S**imilar to the Pandas .replace() method. Can take in dictionaries or functions that are used for a 1-1 mapping of all elements in a Series or DataFrame.
* **.apply(func):** Method that applies a function to a DataFrame or a Series. For DataFrames this method is flexible and can be used to apply functions across columns or across rows.

#### Calculating Summary Statistics

##### Numeric Data

* .mode() -- the mode of the column
* .mean() – the mean of column
* .std(ddof = 1): sample standard deviation
* .quantile(): takes in decimal value to get the corresponding percentile from the column.
* .count() -- the count of the total number of entries in a column
* .var(ddof = 1) -- sample variance for the column
* .sum() -- the sum of all values in the column
* .cumsum() -- the cumulative sum, where each cell index contains the sum of all indices lower than, and including, itself.

Acting on DataFrames, these functions take in optional axis arguments. I.e. .sum(axis = 0) returns a Series with the sum tallied for each column. The axis = 1 arguments sums up all rows and returns a Series.

##### Categorical Data

* Series.unique(): Gets the unique entries in a Series. Particularly useful for categorical data.
* Series.value\_counts(): Gets the unique entries and counts for each entry in the original Series.

### How Does Pandas Series and Dataframes Work?

Pandas is an essential library for data analysis in Python. You will be making frequent use of it in this course and in your future work as a data analyst/scientist. Understanding Pandas’ data structures*—*the Series and DataFrames*—*is an absolute must. These structures possess a range of built-in methods which make standard practices and procedures streamlined. These practices include:

* Data Loading
* Data Type Handling
* Dealing with Column/Index information
* Selecting Data Subsets relevant to an analysis
* Transforming Data
* Calculating relevant summary statistics

Pandas Series and DataFrame methods make performing these standard operations easy. You can implement your wrangling and analysis with very few lines of code. Additionally, Pandas’ under-the-hood vectorized implementation of various operations often results in substantial reductions in computation time over similar operations implemented in base Python.

Pandas hosts a huge number of functions for data analysis. While we cover the most important methods you should know, it is not feasible or useful to memorize every method that exists. Thus you should not devote too much time to memorization. Nor should you get flustered if you have not seen a pandas function before or if there is something you want to do with a Pandas DataFrame or Series that was not covered. It is very likely that the functionality exists in Pandas and that you need to look through documentation to find it.

Indeed, one of the most important parts of a data scientist's job is to investigate documentation to learn about components of these tools on your own. You should get comfortable with reading the [Pandas documentation


Links to an external site.](https://pandas.pydata.org/pandas-docs/stable/), Googling, and poring through StackOverflow to see what Series and DataFrame functionality you need for your task.

### Conceptualization: Pandas Dataframes and Series

Key Pandas terms with definition and example

| Term | Definition | Example |
| --- | --- | --- |
| Pandas Series | A one-dimensional labeled array that holds data of any type (numbers, text, etc.) and allows you to access elements by their labels. | s = pd.Series([1,2,3,4,5], index=[‘a’,’b’,’c’,’d’,’e’]) |
| Pandas DataFrame | A two-dimensional, size-mutable labeled data structure with rows and columns, like a spreadsheet. | df = pd.DataFrame({‘A’: [1,2,3], ‘B’: [4,5,6]}) |
| pd.DataFrame() | Constructor for creating a new DataFrame from data. | df = pd.DataFrame(data) |
| pd.Series() | Constructor for creating a new Series from data. | s = pd.Series(data) |
| pd.read\_csv() | Function to read a CSV file into a DataFrame. | df = pd.read\_csv(‘data.csv’) |
| .index | Attribute of a DataFrame or Series holding the index labels. | df.index |
| .columns | Attribute of a DataFrame holding column labels. | df.columns |
| .shape | Attribute of a DataFrame or Series indicating its dimensions (rows, columns). | df.shape |
| .dtype | Attribute of a DataFrame or Series indicating the data type of elements. | df[‘column’].dtype |
| .values | Attribute of a DataFrame or Series providing the actual data as a NumPy array. | df.values |
| .info() | Method providing a summary of a DataFrame reviewing data types and memory usage. | df.info() |
| .head() | Method to display the first n rows of a DataFrame (default n=5). | df.head() |
| .tail() | Method to display the last n rows of a DataFrame (default n=5). | df.tail() |
| int | Data type representing integer values in Python and Pandas. | pd.Series([1,2,3], dtype=int) |
| float | Data type representing floating-point values in Python and Pandas. | pd.Series([1.1, 2.2, 3.3], dtype=float) |
| bool | Data type representing boolean values in Python and Pandas (ex. True or False). | pd.Series([True, True, False], dtype=bool) |
| object | Data type representing text, string, or mixed data types in Python and Pandas. | pd.Series([‘a’,’b’,’c’], dtype=object) |
| datetime64 | Data type representing date and time values in Pandas. | pd.Series([‘2024-01-01’, ‘2024-01-02’], dtype=’datetime64’) |
| .loc accessor | Accessor for selecting rows and columns by label(s) in a DataFrame | df.loc[row\_label, col\_label] |
| .iloc accessor | Accessor for selecting rows and columns by integer position(s) in a DataFrame. | df.iloc[row\_index, col\_index] |
| .rename() | Method to rename index labels or column names in a DataFrame. | df.rename(columns={‘A’: ‘Column\_A’}, inplace=True) |
| .set\_index() | Method to set a specific column as the index of a DataFrame. | df.set\_index(‘column\_name’, inplace=True) |
| .sort\_index() | Method to sort a DataFrame by index labels. | df.sort\_index(ascending=False) |
| Vectorized Operations | Operations that are applied element-wise across arrays (Series or DataFrames) without explicit looping. | df[‘A’] \* 2 |
| .replace() | Method to replace specific values in a DataFrame or Series. | df.replace(to\_replace=9999, value=np.nan) |
| .map() | Method to map values of a Series according to input correspondence. | df['column'].map(mapping\_dict) |
| .apply(func) | Method to apply a function along an axis of a DataFrame or Series | df.apply(np.sum, axis=0) |
| .mode() | Method to compute the mode(s) of each element along the specified axis. | df.mode() |
| .mean() | Method to compute the mean of each element along the specified axis. | df.mean() |
| .std() | Method to compute the standard deviation of each element along the specified axis. | df.std() |
| .quantile() | Method to compute the quantile(s) of each element along the specified axis. | df.quantile(0.5) |
| .count() | Method to count non-NA/null observations across the specified axis. | df.count() |
| .var() | Method to compute the variance of each element along the specified axis. | df.var() |
| .sum() | Method to compute the sum of each element along the specified axis. | df.sum() |
| .cumsum() | Method to compute the cumulative sum of each element along the specified axis. | df.cumsum() |
| .unique() | Method to return unique elements in a Series or DataFrame. | df[‘column’].unique() |
| .value\_counts() | Method to count occurrences of each unique value in a Series. | df[‘column’].value\_counts() |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243582

Scraped At: 2026-05-14T20:56:07.261106
