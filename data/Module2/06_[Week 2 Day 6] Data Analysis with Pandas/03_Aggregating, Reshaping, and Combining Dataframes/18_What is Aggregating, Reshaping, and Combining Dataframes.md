# What is Aggregating, Reshaping, and Combining Dataframes?

# What is Aggregating, Reshaping, and Combining Dataframes?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What is Aggregating, Reshaping, and Combining Dataframes?

* [Page: Introduction to Data Analysis with Pandas (1 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243579 "Page: Introduction to Data Analysis with Pandas (1 of 26)")
* [Page: Introduction to Pandas Dataframes and Series (2 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243581 "Page: Introduction to Pandas Dataframes and Series (2 of 26)")
* [Page: What are Pandas Dataframes and Series? (3 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243582 "Page: What are Pandas Dataframes and Series? (3 of 26)")
* [Page: Process: Using Pandas Series and Dataframes (4 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243583 "Page: Process: Using Pandas Series and Dataframes (4 of 26)")
* [Page: Summary: Pandas Series and Dataframes (5 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243584 "Page: Summary: Pandas Series and Dataframes (5 of 26)")
* [Page: Check for Understanding: Pandas Dataframes and Series (6 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243586 "Page: Check for Understanding: Pandas Dataframes and Series (6 of 26)")
* [Page: Technical Lesson: Pandas Dataframe and Series (7 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243587 "Page: Technical Lesson: Pandas Dataframe and Series (7 of 26)")
* [Page: Practice: Pandas Dataframes and Series (8 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243588 "Page: Practice: Pandas Dataframes and Series (8 of 26)")
* [Page: Introduction to Data Cleaning with Pandas (9 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243590 "Page: Introduction to Data Cleaning with Pandas (9 of 26)")
* [Page: What is Data Cleaning with Pandas? (10 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243591 "Page: What is Data Cleaning with Pandas? (10 of 26)")
* [Page: Example: Data Cleaning in Healthcare Using Pandas (11 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243592 "Page: Example: Data Cleaning in Healthcare Using Pandas (11 of 26)")
* [Page: Process: Data Cleaning with Pandas (12 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243594 "Page: Process: Data Cleaning with Pandas (12 of 26)")
* [Page: Summary: Data Cleaning with Pandas (13 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243595 "Page: Summary: Data Cleaning with Pandas (13 of 26)")
* [Page: Check for Understanding: Data Cleaning with Pandas (14 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243596 "Page: Check for Understanding: Data Cleaning with Pandas (14 of 26)")
* [Page: Technical Lesson: Data Cleaning with Pandas (15 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243597 "Page: Technical Lesson: Data Cleaning with Pandas (15 of 26)")
* [Page: Practice: Data Cleaning with Pandas (16 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243598 "Page: Practice: Data Cleaning with Pandas (16 of 26)")
* [Page: Introduction to Aggregating, Reshaping, and Combining Dataframes (17 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243600 "Page: Introduction to Aggregating, Reshaping, and Combining Dataframes (17 of 26)")
* [Page: Current: What is Aggregating, Reshaping, and Combining Dataframes? (18 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243602 "Page: Current: What is Aggregating, Reshaping, and Combining Dataframes? (18 of 26)")
* [Page: Example: Aggregating, Reshaping, and Combining Dataframes (19 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243603 "Page: Example: Aggregating, Reshaping, and Combining Dataframes (19 of 26)")
* [Page: Process: How to Aggregate, Reshape, and Combine DataFrames (20 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243604 "Page: Process: How to Aggregate, Reshape, and Combine DataFrames (20 of 26)")
* [Page: Summary: Aggregating, Reshaping, and Combining Dataframes (21 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243605 "Page: Summary: Aggregating, Reshaping, and Combining Dataframes (21 of 26)")
* [Page: Check for Understanding: Aggregating, Reshaping, and Combining Dataframes (22 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243606 "Page: Check for Understanding: Aggregating, Reshaping, and Combining Dataframes (22 of 26)")
* [Page: Technical Lesson: Aggregating, Reshaping, and Combining Dataframes (23 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243607 "Page: Technical Lesson: Aggregating, Reshaping, and Combining Dataframes (23 of 26)")
* [Page: Practice: Aggregating, Reshaping, and Combining Dataframes (24 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243609 "Page: Practice: Aggregating, Reshaping, and Combining Dataframes (24 of 26)")
* [Lab: Data Analysis with Pandas (25 of 26), Assignment](https://moringa.instructure.com/courses/1406/modules/items/243611 "Lab: Data Analysis with Pandas (25 of 26), Assignment")
* [Quiz: Data Analysis with Pandas (26 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243612 "Quiz: Data Analysis with Pandas (26 of 26)")

17 min read

Read through the following areas to know about aggregating, reshaping, and combining dataframes.

### [Grouping and Aggregation Operations](#dpPanel0)

#### The Split-Apply-Combine Paradigm

##### Split

**Pandas' .groupby():** splits a DataFrame into subgroups for comparison. Use it with a categorical column: (e.g., df.groupby(categorical\_column\_name)). This splits the elements of your dataframe up by the unique groups contained within the categorical column.

##### Apply

**Groupbys** are often used with other methods that apply transformations or compute statistics over each group. For example, we can aggregate (i.e., compute a statistic) over each group.

##### Combine

At the end, we want to combine the results of calculations for each group: i.e., getting summary statistics for various features computed across each group in the given categorical variable.

The aggregation and combine steps are accomplished by chaining the groupby with an aggregation method. This typically takes the pattern of:

`df.groupby(categorical_column_name).aggregation_method()`

where aggregation\_method() could be the mean (e.g., .mean() ) or some other summary statistic. This will generally result in a given summary statistic for applicable features in the dataset computed across each group.

For example, **if** we take the Titanic dataset (first five lines shown):

Data Table with Titanic passenger information (first five lines)

| PassengerId | Survived | Pclass | Name | Sex | Age | SibSp | Parch | Ticket | Fare | Cabin | Embarked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 3 | Braund, Mr. Owen Harris | male | 22 | 1 | 0 | A/S 3 33 | 3.33 |  | S |
| 1 | 1 | 1 | Cumings, Mrs. Margaret (Emily Pauline) | female | 38 | 1 | 0 | PC 175 | 71.28 | C | C |
| 2 | 1 | 3 | Vandiver, Miss. Edith Marion | female | 19 | 0 | 0 | C 2331 | 8.05 |  | S |
| 3 | 1 | 1 | Douglas, Mrs. John B. (Nellie Louise) | female | 16 | 0 | 0 | C 277 | 13 |  | S |
| 4 | 0 | 3 | Ms. Kristine Ludvigsen | female | 18 | 1 | 2 | F/C 2789 | 8.05 |  | S |

**Then**

```
#numeric_only = True required as computing mean across string columns isnt well-defined  
titanic_df.groupby('Sex').mean(numeric_only = True)
```

computes the mean of all numeric columns in the dataset by sex (our groupby categorical) and returns it as a DataFrame with row indices being the unique group values and columns being numeric features for which the mean can be computed.

```
        PassengerId  Survived    Pclass        Age     SibSp     Parch  \  
Sex                                                                        
female   431.028662  0.742038  2.159236  27.915709  0.694268  0.649682     
male     454.147314  0.188908  2.389948  30.726645  0.429809  0.235702     
  
             Fare    
Sex                  
female  44.479818    
male    25.523893  
```

Groupby aggregations allow for efficient comparison of summary statistics across subsets of our data. For example, we can immediately notice that the mean survival rate among women was generally higher than among men. This sort of statistical comparison across groups will generally be the bread and butter of any analysis you do.

#### Common Aggregation Functions Chained on Groupbys

Commonly used aggregation methods chained on groupbys are:

* **.min():** returns the minimum value for each column by group
* **.max():** returns the maximum value for each column by group
* **.mean():** returns the average value for each column by group
* **.median():** returns the median value for each column by group
* **.count():** returns the count of each column by group

#### Groupby with Multiple Groups

You can also split data into different levels of groups by passing in an array containing the name of every categorical you want to group by.

For instance, we can look at the mean of various numeric features grouped by Sex and Pclass:

```
df.groupby(['Sex', 'Pclass']).mean(numeric_only = True)
```

The code above would return the following DataFrame where the sex and passenger class are outer and inner indices of what is known as a **hierarchical Multi-level Index**.

![Dataframe with sex and passenger class as outer and inner indices of a hierarchical multi-level index](https://moringa.instructure.com/courses/1406/files/624999/download)

#### Selecting Information from Grouped and/or Multi-Indexed Objects

Since the resulting object returned is a DataFrame, you can also slice a selection of columns you're interested in from the DataFrame returned.

The example below demonstrates the syntax for returning the mean of the Survived class for every combination of Sex and Pclass:

```
df.groupby(['Sex', 'Pclass'])['Survived'].mean(numeric_only = True)
```

The code returns the following DataFrame.

![DataFrame results of Survived class for every combination of sex and pclass](https://moringa.instructure.com/courses/1406/files/624760/download)

The above example slices by column, but you can also slice by index. Take a look:

```
grouped = df.groupby(['Sex', 'Pclass'])['Survived'].mean(numeric_only = True)  
  
# gets survival rate for females of all classes  
print(grouped['female'])  
  
# gets survival rate for females of first class  
print(grouped['female'][1])
```

```
Output:  
  
Pclass  
1    0.968085  
2    0.921053  
3    0.500000  
Name: Survived, dtype: float64  
0.9680851063829787
```

Note that you need to provide only the value female as the index, and are returned all the groups where the passenger is female, regardless of the Pclass value. The second example shows the results for female passengers with a 1st-class ticket.

Additionally, the same result could have been achieved by using the .loc[] accessor.

The behavior of the .loc[] accessor is the same when getting data associated with a particular value of the outer-level index:

```
grouped.loc['female']
```

**Output:**

```
Pclass  
1    0.968085  
2    0.921053  
3    0.500000  
Name: Survived, dtype: float64
```

To get data indexed at a particular value of the outer and inner level, use a tuple in the row selector containing the names of the indices by level e.g. (first\_level, second\_level):

```
grouped.loc[('female', 1)]
```

**Output:**

```
0.9680851063829787
```

Row and column selections can be made on a Multi-indexed dataframe in the standard pattern with the .loc[] accessors:

```
grouped.loc[row_accessor, column_accessor]
```

However, the row accessor is now a tuple or list of tuples corresponding to a set of multi-level indices:

```
grouped_sex_pclass = df.groupby(['Sex', 'Pclass']).mean(numeric_only = True)
```

Selecting mean Age and Fare for Females of third class is easy:

```
grouped_sex_pclass.loc[('female', 3), ['Age', 'Fare']]
```

**Output:**

Age     21.75000  
Fare    16.11881  
Name: (female, 3), dtype: float64

### [Data Formats and Reshaping](#dpPanel1)

Pandas can be used to index and structure data sets to make it easier to process or understand. We start by distinguishing between Wide vs. Long format, then introduce multi-hierarchical index structures and compare it to basic flattened index structures. We then discuss various commands relevant to changing between wide vs. long formats and and reorganization using multi-level indices.

#### Long vs. Wide Formats

**Wide Format:** This is the common setup you're probably used to seeing. In the wide format, each column of data represents a variable, and each row represents an observation. In the example below, each row corresponds to a Tree species and each column is used to represent a measurement, in this case average Diameter at Breast Height (DBH), at a given site.

**Long Format:** In Long format, the data is broken down so that each row represents measurements for a given tree species and for a specific site. See the following diagram for comparison of the two:

![Comparison of wide versus long data tables](https://moringa.instructure.com/courses/1406/files/624722/download)

##### Related Pandas Commands

**df.pivot():** takes a long format DataFrame and “pivots” it into a wide format. This causes unique values in a particular column in long format to become individual columns in wide format.

```
# Converting from long format to wide in example above  
df_pivoted = long_df.pivot(index ='Tree Species', columns = 'Site', values ='DBH (cm)') 
```

This keeps tree species the same, but the unique values in ‘Site’ get pivoted over to the column name. The values for this pivoted table are specified to be DBH.

**Purpose:** Useful when comparing a measurement across similar/related categories  for a given individual directly.

**df.pivot\_table():** A variant of the .pivot() command. Required when you are trying to pivot your data but there are multiple values corresponding to the same index and column variable in long format.

See a nice example below. Pivoting our data on area (as index) and agent (as column) would enable a side-by-side comparison of price and size by agent for each area.

![pivot table example on area and index](https://moringa.instructure.com/courses/1406/files/625281/download)

The problem is that there are two values for price and size for area 1111 and agent b. Pandas .pivot() can’t resolve this: which of the two sets of values for price and size  does it put in the corresponding index row and column in wide format?

The .pivot\_table() has the same arguments as .pivot() but also takes in an `aggfunc` keyword argument. The value in the pivot table is now the result of aggregating (in the specified way) over the values corresponding to the same index and column.  
The pattern is:

```
# Converting from long format to wide in example above  
df_pivoted = long_df.pivot_table(index = [index_variable], columns = [column_variable], values = [value_columns], aggfunc = ...) 
```

Some aggfunc strings are:

* ‘mean’
* ’count’
* ‘sum’
* ‘median’

Default aggregation function is ‘mean’.

**df.melt():** takes a wide format DataFrame and "melts" it into a long format, converting multiple columns with similar structures into a single "variable" column.

```
# Converting from wide to long format in tree example above  
df_melted = wide_df.melt(id_vars='Tree Species', var_name ='Site', value_name='DBH (cm)') 
```

By default, takes the column names and un-pivots the columns*—*creating separate rows for each column name. There are options for selecting which columns in the wide-format data to select unpivot and how the resultant columns in long format should be named. See documentation for more information.

**Purpose:** Useful for restructuring data for analysis when you have many related variables spread across columns (as in this case*—*with different sites).

#### Multi-Hierarchical Indexing with Long Format Data

It is often useful to organize data using a Multi-level index. We saw the Multi-index appear naturally as a result of groupby/aggregation on multiple columns.

There are other circumstances that might lead you to organize your data using a Multi-Index. However, there are other circumstances that might lead you to organize your data using a Multi-Index, such as when you have a dataset that can be organized in a hierarchical manner  (e.g., measurements of GDP and life expectancy organized hierarchically by continent, country, and year).

In the example, we could organize the data so that the measurements are indexed hierarchically by continent, country, and then year:

![Comparison of flat tabular and hierarchical multi-index organization](https://moringa.instructure.com/courses/1406/files/624729/download)

#### Setting a Multi-Level Index

Setting a multi-level index from the columns of a DataFrame is a straightforward extension of the .set\_index() method you have already seen when setting a standard row index from a single column:

```
# sets a 2-level Multi-index with level1_col as outer level and level2_col as inner level  
  
col_list = [level1_col, level2_col] # column names for level 1 and level 2  
# not using in-place = True creates new DataFrame  
df.set_index(col_list, inplace = True) 
```

The pattern generalizes to many levels with the first column in the list being the outermost level of the hierarchy and the last column being the innermost level. In the example above, we would call:

```
col_list = ['continent', 'country', 'year']   
df.set_index(col_list, inplace = True) 
```

Finally, the Multi-Index needs to be sorted to fully set the hierarchy. This is accomplished with the .sort\_index() method.

```
df.sort_index(inplace = True) 
```

The data can then be addressed hierarchically using the .loc[] accessor.

#### Stacking and Unstacking Data

The .stack() and unstack() methods operates on Multi-indexed DataFrames in a manner that is reminiscent of pivoting and melting.

The DataFrame.unstack() method takes in either the name of a level of the index or an integer that indicates the level of the Multi-index you wish to unstack (0 being the outermost level).

![Example of a multi-index stack converted with unstack](https://moringa.instructure.com/courses/1406/files/625217/download)

The .unstack() moves the index level specified over to the right as variable columns*—*an operation that is similar to a pivot. The data is now in wide format.

The .stack() does the exact opposite, moving the columns to the innermost level of the Multiindex and converting the data back into long format.

There are a lot of options here, so see the documentation for [unstack


Links to an external site.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html) and [stack


Links to an external site.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack) for more detail.

### [Combining DataFrames With Pandas](#dpPanel2)

There are two main flavors of combining data frames drawn from multiple sources: Concatenation and Joins.

**Concatenation (pd.concat):**

* Combines DataFrames along a specific axis (rows or columns)
* Useful for stacking DataFrames on top of each other (rows) or creating side-by-side comparisons (columns)
* Row (column) based concatenation is useful when dataframes share common columns (rows) respectively

![ Row-based concatenation of three DataFrames](https://moringa.instructure.com/courses/1406/files/625151/download)

**Syntax**

By default pd.concat takes in a list of dataframes and concatenates them. The corresponding code for our example above:

```
# row based concatenation  
objs = [df1, df2, df3] # list of dataframes to concatenate  
pd.concat(objs, axis=0)
```

**Syntax:**

* objs: List of DataFrames to concatenate
* axis: 0 for rows, 1 for columns (default 0)

There are other useful options for this command, such as the `join` keyword argument specifying what to do if the DataFrames you are row-wise concatenating share some but not all of the columns ([see documentation for further details


Links to an external site.](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)).

**Joins:**

This is useful when you have datasets that do not necessarily share the same structure (as had to be the case when concatenating), but do share a common feature that relates the two datasets in some way.

A simple example can be seen below, where we have two dataframes:

* df1 that contains employees at a company and the department they work in
* df2 that contains the information about each department and the department’s supervisor

We want to join these datasets so that we have a combined table containing employee, department they work in, and their supervisor.

![Two dataframes to join that will combine employee, department, and supervisor data](https://moringa.instructure.com/courses/1406/files/624759/download)

**Primary key**

The entries of the first table can be uniquely indexed by **employee**. The entries of the second table are uniquely indexed by **group**. These are called **primary keys** for their respective tables, as each table can be indexed by these columns.

**Foreign key**

In the example above, each dataset contains a column called **group** containing common information. For the first dataset df1, group is known as a **foreign key***—*a column that is not the primary key for the given dataset but contains information common to the primary key for the other dataset. In this case, this primary key in the second dataset is the column group.

Connecting information in the foreign key of one table to the primary key in the other, allows one to join the two tables in a sensible and unique way. In our example, rows in df1 can be lined up with and joined to rows in df2 using the group columns.

#### Types of Joins

There are four different types of joins you can execute between the Left Table (in the example, df1) and a Right Table (df2).

* An Inner Join returns only the records with matching keys in both tables.
* A Left Join returns all the records from the left table, as well as any records from the right table that have a matching key with a record from the left table.
* A Right Join returns all the records from the right table, as well as any records from the left table that have a matching key with a record from the right table
* An Outer Join returns all records from both tables with rows with matching keys lined up.

It is useful to conceptualize the different joins with Venn diagrams.

![Venn diagram of the four join types](https://moringa.instructure.com/courses/1406/files/625215/download)

##### Pandas functions for Joins

There are two functions that you can use to execute a join in Pandas: pd.merge() and df.join().

**pd.merge():** Flexible function for merging two dataframes.

**Syntax:**

```
pd.merge(df1, df2, how = ...., on = ...)
```

Merges left dataframe df1 with right dataframe df2 on a key.

* The how argument species the type of join: takes ‘inner’, ‘left’, ‘right’, ‘outer’ for the corresponding types of joins.
* The on argument specifies the key to merge on – if the keys have the same name in both tables. If the common key has different column names you can use left\_on = …, right\_on = .... instead.

For the joins dataframes example, we get the following behavior for different kinds of joins:

**Inner:**

```
pd.merge(df1, df2, how = 'inner', on = 'group')
```

![Inner join example result](https://moringa.instructure.com/courses/1406/files/624765/download)

Note that Jimbo Jr. and Chadwick got dropped as the ‘’Compliance’ and ‘Building’ are not contained in the group column of df2.

**Left:**

```
pd.merge(df1, df2, how = 'left', on = 'group')
```

![Left merge join results](https://moringa.instructure.com/courses/1406/files/624723/download)

Chadwick and Jimbo Jr. from the left table are back along with their key values*—*but the supervisor column has NaNs as these are not contained in the right table.

**Outer:**

All entries from the left and the right table are included with rows having matching keys aligned.

![Outer join results](https://moringa.instructure.com/courses/1406/files/625001/download)

**df.join(df2, …):** This is a built-in DataFrame joining method that is commonly employed. It is a little less flexible but faster than pd.merge (which has options for joining on multiple columns in both the left and right table, automatically creating placeholders for NaNs, etc.).

In order to use this method, the column we merge on (the primary key in the second table) must be set as the index of the second table.

**Syntax**

```
df2.set_index(key_to_merge_on, inplace = True) # if index hasn't been set  
  
df1.join(df2, how = ..., on = ...)
```

* **how:** has same options as pd.merge()
* **on:** specifies the foreign key in the left table that will corresponds to the index (primary key) of the second table

To execute the inner join with our example dataframes using df.join():

```
df2.set_index('group', inplace = True) # index hasn't been set yet  
  
df1.join(df2, how = 'inner', on = 'group')
```

**NOTE:** If both tables contain columns with the same name, df.join() will throw an error due to a naming collision, since the resulting table would have multiple columns with the same name. To solve this, pass in a value to lsuffix= or rsuffix=, (e.g. lsuffix=’\_x’ or rsuffix=’\_y’  which will append the respective suffixes to the offending columns to resolve the naming collisions.

### Conceptualization: Data Visualization Best Practices

Data visualization terminology with definitions and examples

| **Term** | **Definition** | **Example** |
| --- | --- | --- |
| pandas.groupby() | Method to split data into groups based on specified columns, and apply functions (e.g., aggregation) to each group. | grouped = df.groupby(‘column\_name’) |
| Aggregation method | Functions applied to grouped data to compute summative statistics. | grouped.mean() |
| .min() | Method to compute the minimum value in a Series or DataFrame. | df.min() |
| .max() | Method to compute the maximum value in a Series or DataFrame. | df.max() |
| .mean() | Method to compute the mean value in a Series or DataFrame. | df.mean() |
| .median() | Method to compute the median value in a Series or DataFrame. | df.median() |
| .count() | Method to count non-NA/null observations across the specified axis. | df.count() |
| Wide Format | Data representation where variables are in columns and observations are in rows. | Example table dimensions: 1000 rows (customers) by 20 columns (product categories). |
| Long Format | Data representation where variables are in rows, and will often but not always outnumber the columns. | Example table dimensions: 365 (days) \* N (number of cities) rows, with a few columns (city, date, temperature). |
| df.pivot() | Method to reshape data from long to wide format based on column values. | df.pivot(index=’column1’, columns=’column2’, values=’values’) |
| df.pivot\_table() | Method to create a spreadsheet-style pivot table as a DataFrame. | pd.pivot\_table(df, values=’values’, index=’index’, columns=’columns’) |
| df.melt() | Method to unpivot a DataFrame from wide to long format. | pd.melt(df, id\_vars=[‘id\_vars’], value\_vars=[‘value\_vars’]) |
| Multi-Index | Index with multiple levels, allowing hierarchical indexing. |  |
| .stack() | Method to pivot a level of the (possibly hierarchical) column labels. | df.stack() |
| .unstack() | Method to pivot a level of the index label. | df.unstack() |
| pd.concat | Function to concatenate pandas objects along a particular axis. | pd.concat([df1, df2]) |
| Joins | Combining columns or indices of two potentially differently-indexed DataFrames into a single DataFrame. |  |
| Primary key | Unique identifier for each row in a table. |  |
| Foreign key | Field in a table that points to the primary key of another table. |  |
| Inner Join | Join operation that returns only the rows that have matching keys in both DataFrames | pd.merge(df1, df2, how=’inner’, on=’key\_column’) |
| Left Join | Join operation that returns all rows from the left DataFrame and matching rows from the right DataFrame. | pd.merge(df1, df2, how=’left’, on=’key\_column’) |
| Right Join | Join operation that returns all rows from the right DataFrame and matching rows from the left DataFrame. | pd.merge(df1, df2, how=’right’, on=’key\_colum’) |
| Outer Join | Join operation that returns all rows from both DataFrames, with NaNs wherever there are no matching keys. | pd.merge(df1, df2, how=’outer’, on=’key\_column’) |
| pd.merge() | Function to merge DataFrame or named Series objects with a database-style join. | pd.merge(df1, df2, how=’inner’, on=’key\_column’) |
| df.join() | Method to join columns of another DataFrame. | df.join(other\_df, on=’key\_column’) |
| how argument | Argument in merge functions specifying the type of join (e.g., ‘inner’,’left’,’right’,’outer’). | pd.merge(df1, df2, how=’inner’) |
| on argument | Argument in merge functions specifying the column(s) to join on. | pd.merge(df1, df2, on=’key\_column’) |
| left\_on() | Method to specify the left DataFrame’s column(s) to join on when merging. | pd.merge(df1, df2, left\_on=’key\_column1’, right\_on=’key\_column2’) |
| right\_on() | Method to specify the right DataFrame’s column(s) to join on when merging. | pd.merge(df1, df2, left\_on=’key\_column1’, right\_on=’key\_column2’) |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243602

Scraped At: 2026-05-14T20:57:52.770108
