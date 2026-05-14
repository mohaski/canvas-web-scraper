# What is Data Cleaning with Pandas?

# What is Data Cleaning with Pandas?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What is Data Cleaning with Pandas?

Icon Progress Bar (browser only)

23 min read

### Dealing with Missing Data

### [Why is Missing Data a Problem?](#dpPanel0)

Missing data presents a significant challenge in Data Science. Its presence can lead to several critical issues that compromise the validity and reliability of analysis.

* **Reduced Representativeness:** Missing data can cause the remaining data to become unrepresentative of the entire population under study. This can lead to biased conclusions, as the analysis focuses on an incomplete picture.
* **Statistical Challenges:** Many statistical methods rely on complete datasets for accurate calculations. Missing values can distort summary statistics (means, medians) and make it difficult to determine true relationships between variables. This can lead to misleading interpretations and unreliable inferences.
* **Machine Learning Issues:** Machine Learning algorithms depend on identifying patterns within data. Missing values disrupt these patterns, potentially leading to inaccurate predictions or models that are biased towards data with fewer missing values. In essence, the model is trained on an incomplete picture, limiting its ability to generalize effectively.
* **Analytical Limitations:** Missing data can restrict the types of analyses that can be performed. Depending on the extent of missingness, it might be necessary to remove entire rows or columns, reducing the overall size and richness of the dataset. This can limit the scope of the analysis and hinder the ability to explore the data more comprehensively.

### [Representations of Missing Data in DataFrames](#dpPanel1)

Data can be missing for various reasons, and DataFrames offer several ways to represent these absences. Understanding these representations is crucial for accurate data analysis.

**Common Missing Data Indicators:**

* **NaN (Not a Number):** This is the most common representation for missing data in Pandas. Pandas automatically parses empty values in files containing tabular data (i.e. CSVs) into NaNs. Pandas provides a whole host of built-in Series and DataFrame methods to identify and handle NaN values effectively.
* **None:** Python’s None Type. Also indicates a missing value*—*particularly in object dtype columns.

**Beyond NaNs: PlaceHolder Representations**

* **Empty Strings (""):** In some datasets, empty strings might indicate missing data. However, it's essential to verify this assumption by checking the data dictionary or exploring the data itself. Empty strings could also represent textual data with no content.
* **Placeholder Numeric Values:** Occasionally, specific values (e.g., -999, 0) are used as placeholders for missing data. These codes can vary depending on the data source and require context-specific interpretation. Understanding the data's origin and any relevant documentation is crucial for deciphering such placeholder values.

### [Identifying Missing Data in Pandas DataFrames](#dpPanel2)

#### Detecting and Tallying Missing Values encoded as NaNs

Pandas provides efficient methods to detect NaNs within your DataFrames.

**Utilizing .isna():**

The .isna() function serves as a key tool for identifying NaNs. When acting on a DataFrame, it returns a boolean DataFrame with the following behavior:

* **True:** Indicates the presence of a missing value (NaN) in the corresponding cell.
* **False:** Indicates a valid data point exists in the cell.

This creates a new data structure acting as a "mask" that highlights the locations of missing data within your DataFrame.

Example:

```
import pandas as pd  
  
# Sample DataFrame with NaNs  
data = {'Age': [25, None, 30], 'City': ['Boston', 'New York', 'Chicago'], 'Salary': [None, 139000, None]}  
df = pd.DataFrame(data)  
print(df)
```

**Output:**

```
   Age      City    Salary  
0  25.0    Boston       NaN  
1   NaN  New York  139000.0  
2  30.0   Chicago       NaN
```

As we can see, Pandas encodes empty values (e.g. None types) as NaNs. The DataFrame.isna() method returns the following:

```
missing_val_mask = df.isna() # returns a Boolean DataFrame: True indicates NaN  
print(missing_val_mask)
```

**Output:**

```
    Age   City  Salary  
0  False  False    True  
1   True  False   False  
2  False  False    True
```

The .isna() method can also be used with a Series:

* **True:** Indicates a missing value (NaN) in the corresponding position.
* **False:** Indicates a valid data point exists.

Let’s create a sample Series with various data types. The Series has None and np.nan values. Both are interpreted by Pandas as NaN. Let’s see what happens when we apply the .isna() method to this Series:

```
Python  
data = pd.Series([25, None, "New York", np.nan])  
  
  
# Detect missing values using .isna()  
missing_value_indicators = data.isna()  
print(missing_value_indicators)
```

**Output:**

```
0    False  
1     True  
2    False  
3     True  
dtype: bool
```

As expected, .isna() effectively pinpoints the missing values in the Series.

**The .notna() method**

Conversely the .notna() pinpoints the non-null values in the Series.

**Counting Missing Values with .isna().sum()**

Beyond pinpointing locations, you might want to know the total number of NaNs present. This is where .isna().sum() comes in.

Since True translates to 1 and False translates to 0 in Python, applying .sum() to the result of .isna() returns the number of missing values (represented by True values) in each column (or row) of the entire DataFrame.

Example counting NaNs in each DataFrame Column:

```
# Count total missing values  
missing_count_col = df.isna().sum()  
print(missing_count_col)
```

**Output:**

```
Age       1  
City      0  
Salary    2  
dtype: int64
```

This results in a Series that contains the tally of NaNs for each column.

**Example counting NaNs in each DataFrame Rows:**

By specifying the axis parameter on the sum() method to axis = 1, we get the NaN counts by row:

```
# Count total missing values  
missing_count_row = df.isna().sum(axis = 1)  
print(missing_count_row)
```

**Output:**

```
0    1  
1    1  
2    1  
dtype: int64
```

**Identifying columns/rows containing NaNs with  DataFrame.isna().any(axis = \_\_)**

The .isna().any() chained method pattern by default scans down each column and returns True if any NaNs exist in a given column.

```
df.isna().any()
```

**Output:**

```
Age        True  
City      False  
Salary     True  
dtype: bool
```

Changing the .any() axis parameter to axis = 1 will do this checking for rows.

```
df.isna().any(axis = 1)
```

**Output:**

0    True  
1    True  
2    True  
dtype: bool

A similar pattern emerges with DataFrame.isna().all(axis = \_\_). In this case it only returns True if all the entries in a given column (or row) are NaNs.

### [Detecting Missing Values Encoded with Numeric Placeholders](#dpPanel3)

Detecting missing values encoded as placeholders require a more nuanced approach than simply looking for NaNs.

#### Challenges with Numeric Placeholders:

Unlike NaN, numeric placeholders can blend in with valid data points, especially if the placeholder value is chosen to be within a plausible range for the actual data. This can lead to underestimating the extent of missing data and potentially skew analysis results. Additionally, the meaning of these placeholders might not be readily apparent, requiring additional investigation to understand how they were used in the data collection process.

##### Strategies for Detection:

Here are some strategies to identify missing data encoded with numeric placeholders:

* **Data Understanding / Domain Knowledge:** If you have access to documentation or background information about the data source, it can provide valuable insights into the use of placeholders. Look for mentions of specific values used to represent missing data. Domain knowledge and/or common sense can also be extremely useful in identifying placeholders for missing values. For example, you might have blood pressure readings where you notice a bunch of zero values floating around. As this is an impossible value for a blood pressure, zero very likely functions as a placeholder for a missing measurement.
* **Descriptive Statistics and Visualization:** Explore the descriptive statistics (mean, median, quartiles, mode) of your data to identify any outliers or unusual values that deviate significantly from the expected range. These outliers might be placeholders. In addition, looking at the .value\_counts() or the mode of a numeric column can be enlightening. A specific value with an unreasonably high count might be a signal that the value is being used as a placeholder. This is especially true when the column contains continuous numeric measurements and where a single value is very unlikely to appear repeatedly. Additionally, visualizations can be really helpful. Assessing data distributions through histograms or boxplots can reveal outliers or improbably frequent values that could indicate placeholder usage. An example of a histogram of a dataset containing the weights of 50 people revealing a placeholder at zero:

![Histogram for weight distribution](https://moringa.instructure.com/courses/1406/files/625093/download)

Assuming that the main data is distributed clustered about a value of central tendency, a boxplot could also help reveal outliers:

![Boxplot revealing possible placeholder for weight outliers](https://moringa.instructure.com/courses/1406/files/625004/download)

The zero values shows up outside the 1.5\*IQR below/above Q1/Q3 respectively flagging the value as a distribution outlier.

##### Combining Techniques:

For optimal results, you’ll want to combine these techniques. In the absence of documentation, leverage any domain knowledge you have to identify potential placeholder values. Then, use descriptive statistics and data visualization to pinpoint data points that align with those placeholders. By employing this dual approach, you can increase your confidence in detecting missing data encoded with numeric values.

### [Identifying Placeholder Values in Categorical Data](#dpPanel4)

You can identify unexpected values using the .unique()method. In some cases, the encoding of missing values in categorical data will be really clear and show up as strings like ‘UNK., ‘Unknown , ‘Missing’, etc. Other times, the encoding will be a bit more ambiguous and data definitions or domain knowledge can be really helpful in determining if an entry is truly a missing value placeholder or indicates other issues (e.g.  a typo).

For example, imagine you're analyzing a column of a particular dataset that contains information on where passengers embarked from on a cruise. Using .unique() on this column, let’s say, returns "S", "C", "Q", and "X". Based on your knowledge of embarkation points being Southampton (S), Cherbourg (C), and Queenstown (Q), "X" might be a placeholder for a missing value or an error in data entry. This ambiguity can be tricky to resolve, but if we knew how that “X” was a common way of encoding nulls in naval manifest data that would certainly be helpful.

### [Converting Placeholder Values to Pandas Null Types](#dpPanel5)

In pandas DataFrames, replacing placeholder values (specific characters or strings) with null types (NaN for numerics and None for strings) can improve data cleaning and analysis. This ensures these placeholders are treated as missing data (i.e., they are recognized as nulls by .isna() and .info() methods), preventing them from being misinterpreted as valid values during calculations or skewing statistical results.

Here is an example demonstrating how to replace placeholders with null types using the .replace() method:

#### Replacing a String Placeholder:

```
data = {'column1': ['apple', 'placeholder', 'banana']}  
df = pd.DataFrame(data)  
  
  
# Replace 'placeholder' with null type (None)  
df['column1'] = df['column1'].replace('placeholder', None)
```

There are some notable exceptions for categorical data where you might not want to convert your string placeholder to a None. This is particularly true when a missing value tells you something important and you want to keep all missing values as their own category. We will discuss this in some more depth in the subsequent section.

### [Strategies for dealing with missing data](#dpPanel6)

Detecting missing values isn't enough -- we need to deal with them in order to move forward. We have three options for dealing with missing values: -- dropping them from the dataset, keeping them, or replacing them with another value.

#### Drop

One way to deal with missing values is to drop rows and/or columns with missing values in them. The downside to this is that you lose all non-null data contained within the given row or column in the process. Whether the dropping NaN strategy is a good one will really depend on several factors, including:

* **Proportion of Missing Data:** If only a small percentage of data points are missing (NaNs), dropping them might be acceptable. However, if there are a  significant number of NaNs scattered throughout the dataset, dropping records (rows) can lead to a substantial loss of data and leave you with an amount insufficient for downstream analysis.
* **Missing Data Pattern (Random vs. Systematic):** If missing data is random and unrelated to other variables, dropping NaNs might be less problematic. However, if missing data is systematic (e.g., missing values tend to occur for specific subgroups or under certain conditions), dropping them can introduce bias into your analysis.
* **Impact on Analysis:** Consider the impact of dropping NaNs on your specific analysis. If the missing data is not directly relevant to the research question, dropping it might be acceptable. However, if the missing data is crucial for understanding the relationships between variables, dropping it can significantly weaken your analysis.
* **Alternative Techniques:** Evaluate alternative techniques for handling missing data besides dropping them. These include imputation (filling in missing values with estimates based on other available data). If there's not enough information in the remaining data to make reliable estimates for missing values, imputation might not be suitable. For example, if a large portion of a specific variable is missing and there are no strong correlations with other variables, imputation might introduce artificial bias or noise to your dataset. In these cases, dropping  data for that variable might be the best option.

If you have determined that dropping rows or a particular column with a lot of NaNs is the way to go, then Pandas has got you covered.

##### **Dropping Rows NaNs with DataFrame.dropna()**

**DataFrame.dropna()** by default returns a new DataFrame with all rows containing NaNs dropped. It’s behavior can be seen where we apply the method on a dataFrame concerning a few shark individuals of different species:

```
shark_df
```

**Output:**

```
                  Species  Length (cm)  Weight (kg)  
0        Great White Shark          600       3200.0  
1              Tiger Shark          325        635.0  
2         Hammerhead Shark          300        400.0  
3              Whale Shark         1200      21500.0  
4               Zebrashark          350          NaN  
5            Basking Shark          800       6800.0  
6               Blue Shark          300        130.0  
7      Blacktip Reef Shark          180          NaN  
8   Oceanic Whitetip Shark          350        170.0  
9              Nurse Shark          300        225.0  
10        Sand Tiger Shark          300        150.0  
11           Spiny Dogfish          120          9.0  
12        Great Hammerhead          600        500.0  
13         Greenland Shark          700          NaN  
14             Lemon Shark          300        180.0  
15                    None          250        100.0  
16              Angelshark          400         80.0  
17                    None          150         30.0  
18  Pacific Whitetip Shark          300        150.0  
19     Shortfin Mako Shark          450        500.0  
20   Bigeye Thresher Shark          500        350.0  
21      Cookiecutter Shark           45          2.0  
22    Caribbean Reef Shark          200         80.0  
23           Bramble Shark           90          1.0  
24                    None          100         15.0
```

The method returns a new DataFrame that we save to the variable dropped\_row\_df:

```
dropped_row_df = shark_df.dropna()  
print(dropped_row_df)
```

**Output:**

```
                  Species  Length (cm)  Weight (kg)  
0        Great White Shark          600       3200.0  
1              Tiger Shark          325        635.0  
2         Hammerhead Shark          300        400.0  
3              Whale Shark         1200      21500.0  
5            Basking Shark          800       6800.0  
6               Blue Shark          300        130.0  
8   Oceanic Whitetip Shark          350        170.0  
9              Nurse Shark          300        225.0  
10        Sand Tiger Shark          300        150.0  
11           Spiny Dogfish          120          9.0  
12        Great Hammerhead          600        500.0  
14             Lemon Shark          300        180.0  
16              Angelshark          400         80.0  
18  Pacific Whitetip Shark          300        150.0  
19     Shortfin Mako Shark          450        500.0  
20   Bigeye Thresher Shark          500        350.0  
21      Cookiecutter Shark           45          2.0  
22    Caribbean Reef Shark          200         80.0  
23           Bramble Shark           90          1.0
```

All rows with None values for the Species and for the Weight have been removed from the dataset. If you want the changes to be made to the original DataFrame you can reassign the result to the original DataFrame or use the .dropna(inplace = True) keyword argument.

A very important option is **DataFrame.dropna(subset = ...)**.  This keyword argument takes in a list of column names. Only rows containing NaNs in the specified columns will be dropped. This can be useful when confronted with columns containing a few or moderate number of NaNs where imputation is not feasible.

A perfect example of this might be the Species column in our shark dataset. It would be hard to guess what an individual’s Species is just from length and weight measurements alone. If it is important to the analysis to know the shark’s species, then the best is to drop rows where the Species is unknown.

```
print(shark_df.dropna(subset=['Species']))
```

**Output:**

```
                  Species  Length (cm)  Weight (kg)  
0        Great White Shark          600       3200.0  
1              Tiger Shark          325        635.0  
2         Hammerhead Shark          300        400.0  
3              Whale Shark         1200      21500.0  
4               Zebrashark          350          NaN  
5            Basking Shark          800       6800.0  
6               Blue Shark          300        130.0  
7      Blacktip Reef Shark          180          NaN  
8   Oceanic Whitetip Shark          350        170.0  
9              Nurse Shark          300        225.0  
10        Sand Tiger Shark          300        150.0  
11           Spiny Dogfish          120          9.0  
12        Great Hammerhead          600        500.0  
13         Greenland Shark          700          NaN  
14             Lemon Shark          300        180.0  
16              Angelshark          400         80.0  
18  Pacific Whitetip Shark          300        150.0  
19     Shortfin Mako Shark          450        500.0  
20   Bigeye Thresher Shark          500        350.0  
21      Cookiecutter Shark           45          2.0  
22    Caribbean Reef Shark          200         80.0  
23           Bramble Shark           90          1.0
```

The rows with missing values in the Species column are gone but the NaNs in the Weight column remain.

##### **Dropping columns with NaNs with DataFrame.dropna()**

Changing the axis parameter to DataFrame.dropna(axis = 1) will drop any column from the DataFrame that contains NaNs. Given our shark DataFrame, the command

```
shark_df.dropna(axis=1)
```

will return a DataFrame with all columns of shark\_df contains nulls removed. This would mean that the Species and Weight (kg) columns would be removed. Again, this change could be made to the dataframe in place with the inplace = True option.

---

#### Impute

##### **Domain Knowledge Based Imputation**

Imputation is the process of estimating and filling in missing values within your dataset. One strategy is to use domain knowledge to fill in likely values. For example, an easy way to impute the weights of individuals in the shark dataset would be to look up the average weight of a given shark species. For example, take the following row:

```
Blacktip Reef Shark          180          NaN
```

Looking through various sources, we find that an estimate of average weight for this species is 18 kg. It is reasonable then to impute with this number*—*provided that we know that there is not too much spread about this value of central tendency.

Source: [Carcharhinus limbatus information page from the Florida Museum 


Links to an external site.](https://www.floridamuseum.ufl.edu/discover-fish/species-profiles/carcharhinus-limbatus/#:~:text=The%20maximum%20length%20of%20the,6%2D7%20years%20for%20females).

In this case, you can just use the .loc[] accessor here to directly impute a given element.

This works pretty much the same way with missing categorical data. Domain knowledge can point the way as to how to impute.

##### **Statistical Imputation**

Another common method is simple statistical imputation. This is where you impute all missing values in a given column with a value of central tendency.

* **Mean Imputation:** This method replaces missing values with the average value of the entire column. It's a straightforward approach, but it can be problematic if the data is skewed. For instance, consider a dataset with income levels. A few very high incomes can significantly inflate the mean, leading to an inaccurate estimate for missing values. Additionally, care must be taken to drop outliers before imputing with the mean.
* **Median Imputation:** This technique replaces missing values with the middle value of the column, once the data is sorted numerically. It's a more robust option compared to mean imputation for skewed data. The median is less influenced by outliers, offering a more central representation of the data.
* **Mode Imputation:** This method replaces missing values with the most frequent value (mode) in the column. It's suitable for categorical data where there are distinct categories. However, it can be misleading if there isn't a clear dominant category. Additionally, using the mode for continuous numerical data might not make much sense, as it wouldn't necessarily reflect a value of central tendency.

Pandas’ Series.fillna() method can be used to impute all missing values in a column with a particular value. For example, if you wanted to impute missing values of a numeric column with its median:

```
df[column_name].fillna(df[column_name].median())
```

**Upsides and Caveats**:

**Distributional Assumptions:** The upside of simple statistical imputation is that it is easy to do and often pretty effective. But there are some assumptions that you implicitly make when doing this:

* + Missing values for a given feature are distributed in the same way as the rest of the data in that column.
  + The characteristic value (e.g., median) is a good characteristic measure of the feature’s distribution.
  + That the missing values are not dependent in any way on other features.

Such dependencies may arise when:

* The missing values occur predominantly for particular groups of a categorical variable (e.g., less reliable data collection for underrepresented or marginalized social groups).
* The missing values occur predominantly when other numeric variables enter certain ranges (e.g., the reliability of collecting chemical composition data on oil in a reserve may depend on the depth, pressure, and temperature at which the samples are collected. High temperature and pressure can result in sensor malfunction).

Imputing with simple imputation methods can introduce statistical bias and errors in downstream analysis. This is no laughing matter. It could indeed be a matter of fairness and equity as the first example above highlights. Thus, it is important to think carefully about the distribution of missing values and the collected data in general before applying simple imputation.

**Effect of Simple Imputation on the Data Distribution and Summary Statistics**

As you are imputing with a single value (i.e., the median, mean, or mode), you will be directly affecting your data distribution. In particular, you are going to end up generally reducing the overall spread (variance) of your data. This can be problematic if you're interested in the true variability within your dataset. Of course, this problem gets worse the higher the fraction of missing values that you have in a given feature. Furthermore, simple imputation can shift or bias central tendency measures like the mean or median, especially if missing values aren't random. We will see some of these effects at play in your Practice Lab It is thus important to consider these trade-offs before applying simple imputation.

As one can probably surmise, imputation is an art and a science unto itself. There are many sophisticated tools that exist for dealing with missing values. We won’t get into these here. But the main point is that despite its limitations simple imputation can be a very good option when used with some thought and is very easy to implement with the help of Pandas.

---

#### Keep

Sometimes, the knowledge that a value is missing can itself be informative. If knowing that a value is missing tells you something or is potentially useful for a predictive task , then it is often worth keeping the missing values using the following strategies.

##### **Categorical data**

This one is the easiest*—*just treat missing values as its own category. This may require replacing missing values with a string to denote this, as your model will still likely throw errors if the actual NaN values are not replaced. In that case, just replace the NaN values with the string 'NaN', or another string that makes it obvious that this value is 'missing'.

##### **Numerical data**

Often, missing values inside a continuously-valued column will cause all sorts of havoc in your models, so leaving the NaNs alone isn't usually an option here. Instead, consider using **Coarse Classification**, also referred to as **Binning**. This allows us to convert the entire column from a numerical column to a categorical column by binning our data into categories. For instance, we could deal with the missing values in the Age column by creating a categorical column that separates each person into 10-year age ranges. Anybody between the ages of 0 and 10 would be a 1, 11 to 20 would be a 2, and so on.

Once we have binned the data in a new column, we can throw out the numerical version of the column, and just leave the missing values as one more valid category inside our new categorical column.

### Dealing with Duplicate Data

You might end up with duplicate entries in a DataFrame for various reasons during the data entry/collection/merging process. Leaving duplicate entries in the data, however, can pose a problem. This is particularly true when you have a lot of duplicate entries and you are computing summary statistics. The duplicate values will end up biasing the results of any statistical analysis you might do.

Unlike nulls or missing values, these can’t be discerned so easily by looking at the df.info() or df.describe() method. However, Pandas has two methods that can be used to detect and eliminate duplicate records:

* **DataFrame.duplicated():** returns a boolean Series indicating duplicate rows in your DataFrame. By default, it considers all columns to identify duplicates, highlighting rows with identical values. However, you can specify which particular columns to consider for identifying duplicates by passing a list of column names into the subset keyword argument.
* **DataFrame.drop\_duplicates():** The DataFrame.drop\_duplicates() function in Pandas efficiently removes duplicate rows from your DataFrame. You can specify which columns to consider for identifying duplicates, and optionally keep the first or last occurrence of duplicates if needed.

We can use the .duplicated() method to select all duplicate records via Boolean masking and filtering:

```
duplicates = df[df.duplicated()]
```

The Boolean mask created by df.duplicated() returns a Series with True for any row that contains an exact duplicate in the dataset. Filtering the DataFrame as above then returns all rows that have duplicates elsewhere in the dataset.

Dropping any duplicate rows from the dataframe is done as follows:

```
df = df.drop_duplicates()
```

Instead of reassigning you could also use the .inplace = True argument in the .drop\_dupllicates() command modifying the original DataFrame in-place.

### Additional Cleaning Concerns

While missing values and duplicates are common hurdles, data cleaning typically involves other common tasks. We list these issues and some Pandas functionality that can be used to address them. Note that you saw many of these functions already in the context of selecting and altering values in DataFrames.

* **Inconsistent Formatting:** Pandas offers functions like to\_datetime() for consistent date handling and astype() to convert data types (e.g., strings to numbers) for uniformity.
* **Incorrect Data:** Techniques like replace() allow you to replace typos or specific patterns with corrected values.
* **Unnecessary Columns:** The drop() function removes unwanted columns from your DataFrame.
* **Inconsistent Categorical Data:** Standardizing case (lowercase/uppercase) for category labels using str.lower() or str.upper() ensures consistency.

#### Taming Outliers with Boolean Masking

Outliers, data points far removed from the main body of data, can skew results. Here's where boolean masking shines:

* **Identify Outliers:** Define a threshold based on techniques like Interquartile Range (IQR). Values below a lower bound (Q1 - 1.5 \* IQR) or above an upper bound (Q3 + 1.5 \* IQR) can be considered outliers.
* **Create a Boolean Mask:** Use boolean operators (<, >) to compare your data to the thresholds, creating a Series of True/False values indicating outliers.
* **Filter with the Mask:** Apply the mask to your DataFrame using the square brackets selector [] or the .loc[] accessor.

### Summary

By systematically applying the data cleaning techniques discussed and understanding the capabilities of the Pandas library, you can transform your raw data from a tangled mess into a clean and structured Pandas DataFrame. This ready-to-analyze format paves the way for robust statistical analysis and generation of valuable insights from your data.

In essence, data cleaning with Pandas equips you with the tools to address common data quality issues within your Python code. It ensures that the data you feed into your analysis is reliable and consistent, ultimately leading to more accurate and trustworthy results.

### Conceptualization: Data Cleaning with Pandas

  

Data Cleaning with Pandas terms, definitions, and example of term

| Term | Definition | Example |
| --- | --- | --- |
| (NaN) Not a Number | This is the most common representation for missing data in Pandas | [3, 4, NaN, 6] |
| None | Python representation for missing or undefined data | x = None |
| .isna() | Detects missing values (NaN) | df[‘column’].isna() |
| .notna() | Detects non-missing values | df[‘column’].notna() |
| .unique() | Get unique values excluding Nan | df[‘column’.unique() |
| .replace() | Replace values with another value | df['column'].replace(to\_replace=9999, value=np.nan) |
| .dropna() | Drop rows with any missing values (NaN) | df.dropna() |
| .fillna() | Fill missing values with a specific value | df[‘column’].fillna(value) |
| Statistical Imputation | This is where you assign all missing values in a given column with a value of central tendency | Filling missing values with the statistical mean, median, or mode of the variable |
| Binning | Converting a numerical column to a categorical column by using ranges of values as categories | Creating a categorical variable of low, medium, and high budget films from numeric variable of budgets. |
| .duplicated() | Identify duplicate rows | df.duplicated() |
| .drop\_duplicates() | Drop duplicate rows | df.drop\_duplicates() |
| to\_datetime() | Convert column to datetime format | pd.to\_datetime(df[‘date\_column’]) |
| astype() | Convert column to a specified datatype | df.[‘numeric\_column’].astype(float) |
| Outlier | Data points far removed from the main body of data, which can skew results | In the list of integers, 100 is an outlier: [1,2,3,4,100] |
| Boolean Masking | Use boolean arrays for indexing and filtering data | df[df[‘column’] > 10] |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243591

Scraped At: 2026-05-14T20:56:52.829127
