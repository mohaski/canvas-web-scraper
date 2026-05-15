# Practice: Using PySpark and Python

# Practice: Using PySpark and Python

## ![Blue FS Logo](https://moringa.instructure.com/courses/1426/files/631314/preview) Practice: Using PySpark and Python

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

For this practice, you'll be using a dataset from a Taiwanese financial company, and the task is to determine which individuals are going to default on their credit card based on characteristics such as limit balance, past payment history, age, marriage status, and sex.

This practice is a structured data exploration process, covering:

* **Initial Data Exploration:** Understanding data structure, displaying records, and identifying non-numeric features.
* **Data Visualization:** Using bar plots to evaluate categorical variables and identify distribution patterns.
* **Data Binning:** Consolidating rarely occurring values to improve model readiness.
* **Target Variable Analysis:** Examining class balance and segmenting data to identify patterns by demographics.

Each step is relevant in building data familiarity and preparing for machine learning tasks. See our problem-solving process outline for additional context.

The objective here is to develop skills in handling financial datasets, using tools in PySpark to manage large data, and drawing insights from initial exploration steps. This practice will also strengthen your ability to identify trends and imbalances, essential for predictive modeling tasks. By the end, you’ll be able to approach a dataset with a systematic process, refining your skills in data wrangling and visualization.

### Resources

* CSV File: credit\_card\_default.csv, which comes from the [UCI ML Repository


  Links to an external site.](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients).
* [GitHub Repository: Machine Learning with Spark 


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-machine-learning-with-spark-lab/tree/solution)

### Instructions

#### Part 1: Initial Data Exploration

##### **Step 1: Import and Initialize**

* Get started by writing the relevant import statement and creating a local SparkSession called spark, then use that SparkSession to read credit\_card\_default.csv into a Spark SQL DataFrame.

```
# import necessary libraries  
  
# initialize Spark Session  
spark = None  
  
# read in csv to a spark dataframe  
spark_df = None
```

##### **Step 2: Display and Print**

* Use .head() to display the first 5 records, and print out the schema.

```
# Display the first 5 records  
# Print out the schema
```

##### **Step 3: Select and show all distinct categories**

* It looks like we have three non-numeric features. For each non-numeric (string) feature, select and show all distinct categories.

```
# Select and show all distinct categories
```

* It looks like we have some extraneous values in our categories. For example both EDUCATION and MARRIAGE have a category 0.

Let's create some visualizations of each of these to determine just how many of them there are.

##### **Step 4: Barplots of EDUCATION and MARRIAGE**

Create bar plots of the variables EDUCATION and MARRIAGE to see how the records are distributed between the categories.

* To create a bar plot, you need to group by the category (.groupBy()) and then aggregate by the count in that category (.count()). That will result in a small DataFrame containing EDUCATION and count columns.
* Then the easiest way to create a bar plot is to call .toPandas() to make that small Spark SQL DataFrame into a pandas DataFrame, and call .plot() on the pandas DataFrame.

```
# Create bar plot of EDUCATION  
# Create bar plot of MARRIAGE
```

#### Part 2: Binning

##### **Step 5: Bin EDUCATION and MARRIAGE**

* It looks like there are barely any records in the 0, 5, and 6 categories. Let's go ahead and bin (combine) those with the current Other records into a single catch-all Other category for both EDUCATION and MARRIAGE.

```
# Bin EDUCATION categories  
  
# Bin MARRIAGE categories  
  
# Select and show all distinct categories for EDUCATION and MARRIGE again
```

##### **Step 6: Plot the bins**

* Let's also re-create the plots from earlier, now that the data has been binned:

```
# Plot EDUCATION  
# Plot MARRIAGE
```

Much better. Now, let's do a little more investigation into our target variable before diving into the machine learning aspect of this project.

#### Part 3: Class Balance Exploration

First, let's look at the overall distribution of class balance of the default column (the target for our upcoming machine learning process).

##### **Step 7: Barcharts for (non-)defaults**

* Create a bar plot to compare the number of defaults (0) vs. non-defaults (1). Consider customizing your plot labels as well, since 0 and 1 are not particularly understandable values.

```
# Group and aggregate target data  
  
# Plot target data
```

Looks like we have a fairly imbalanced dataset.

##### Step 8: Group by DEFAULT and SEX

* Let's also visualize the difference in default rate between males and females in this dataset. **Group** by both default and SEX and visualize the comparison.

```
# Group and aggregate target and sex data  
  
# Plot target and sex data
```

It looks like males have an ever so slightly higher default rate than females, and also represent a smaller proportion of the dataset.

### Solution

#### Select for Solution

##### Part 1

###### **Step 1 Import and Initialize**

Get started by writing the relevant import statement and creating a local SparkSession called spark, then use that SparkSession to read credit\_card\_default.csv into a Spark SQL DataFrame.

```
# import necessary libraries  
from pyspark.sql import SparkSession  
# initialize Spark Session  
spark = SparkSession.builder.master('local').getOrCreate()  
  
# read in csv to a spark dataframe  
spark_df = spark.read.csv('credit_card_default.csv', header='true', inferSchema='true')
```

###### **Step 2 Display and Print**

Use .head() to display the first 5 records, and print out the schema.

```
# Display the first 5 records  
spark_df.head(5)
```

**Expected Output:**

```
[Row(ID=2, LIMIT_BAL=120000.0, SEX='Female', EDUCATION='College', MARRIAGE='Single', AGE=26, PAY_0=-1, PAY_2=2, PAY_3=0, PAY_4=0, PAY_5=0, PAY_6=2, BILL_AMT1=2682.0, BILL_AMT2=1725.0, BILL_AMT3=2682.0, BILL_AMT4=3272.0, BILL_AMT5=3455.0, BILL_AMT6=3261.0, PAY_AMT1=0.0, PAY_AMT2=1000.0, PAY_AMT3=1000.0, PAY_AMT4=1000.0, PAY_AMT5=0.0, PAY_AMT6=2000.0, default=1),  
 Row(ID=3, LIMIT_BAL=90000.0, SEX='Female', EDUCATION='College', MARRIAGE='Single', AGE=34, PAY_0=0, PAY_2=0, PAY_3=0, PAY_4=0, PAY_5=0, PAY_6=0, BILL_AMT1=29239.0, BILL_AMT2=14027.0, BILL_AMT3=13559.0, BILL_AMT4=14331.0, BILL_AMT5=14948.0, BILL_AMT6=15549.0, PAY_AMT1=1518.0, PAY_AMT2=1500.0, PAY_AMT3=1000.0, PAY_AMT4=1000.0, PAY_AMT5=1000.0, PAY_AMT6=5000.0, default=0),  
 Row(ID=4, LIMIT_BAL=50000.0, SEX='Female', EDUCATION='College', MARRIAGE='Married', AGE=37, PAY_0=0, PAY_2=0, PAY_3=0, PAY_4=0, PAY_5=0, PAY_6=0, BILL_AMT1=46990.0, BILL_AMT2=48233.0, BILL_AMT3=49291.0, BILL_AMT4=28314.0, BILL_AMT5=28959.0, BILL_AMT6=29547.0, PAY_AMT1=2000.0, PAY_AMT2=2019.0, PAY_AMT3=1200.0, PAY_AMT4=1100.0, PAY_AMT5=1069.0, PAY_AMT6=1000.0, default=0),  
 Row(ID=5, LIMIT_BAL=50000.0, SEX='Male', EDUCATION='College', MARRIAGE='Married', AGE=57, PAY_0=-1, PAY_2=0, PAY_3=-1, PAY_4=0, PAY_5=0, PAY_6=0, BILL_AMT1=8617.0, BILL_AMT2=5670.0, BILL_AMT3=35835.0, BILL_AMT4=20940.0, BILL_AMT5=19146.0, BILL_AMT6=19131.0, PAY_AMT1=2000.0, PAY_AMT2=36681.0, PAY_AMT3=10000.0, PAY_AMT4=9000.0, PAY_AMT5=689.0, PAY_AMT6=679.0, default=0),  
 Row(ID=6, LIMIT_BAL=50000.0, SEX='Male', EDUCATION='Graduate', MARRIAGE='Single', AGE=37, PAY_0=0, PAY_2=0, PAY_3=0, PAY_4=0, PAY_5=0, PAY_6=0, BILL_AMT1=64400.0, BILL_AMT2=57069.0, BILL_AMT3=57608.0, BILL_AMT4=19394.0, BILL_AMT5=19619.0, BILL_AMT6=20024.0, PAY_AMT1=2500.0, PAY_AMT2=1815.0, PAY_AMT3=657.0, PAY_AMT4=1000.0, PAY_AMT5=1000.0, PAY_AMT6=800.0, default=0)]
```

```
# Print out the schema  
spark_df.printSchema()
```

**Expected Output:**

```
root  
 |-- ID: integer (nullable = true)  
 |-- LIMIT_BAL: double (nullable = true)  
 |-- SEX: string (nullable = true)  
 |-- EDUCATION: string (nullable = true)  
 |-- MARRIAGE: string (nullable = true)  
 |-- AGE: integer (nullable = true)  
 |-- PAY_0: integer (nullable = true)  
 |-- PAY_2: integer (nullable = true)  
 |-- PAY_3: integer (nullable = true)  
 |-- PAY_4: integer (nullable = true)  
 |-- PAY_5: integer (nullable = true)  
 |-- PAY_6: integer (nullable = true)  
 |-- BILL_AMT1: double (nullable = true)  
 |-- BILL_AMT2: double (nullable = true)  
 |-- BILL_AMT3: double (nullable = true)  
 |-- BILL_AMT4: double (nullable = true)  
 |-- BILL_AMT5: double (nullable = true)  
 |-- BILL_AMT6: double (nullable = true)  
 |-- PAY_AMT1: double (nullable = true)  
 |-- PAY_AMT2: double (nullable = true)  
 |-- PAY_AMT3: double (nullable = true)  
 |-- PAY_AMT4: double (nullable = true)  
 |-- PAY_AMT5: double (nullable = true)  
 |-- PAY_AMT6: double (nullable = true)  
 |-- default: integer (nullable = true)
```

###### **Step 3 Select and show all distinct categories**

It looks like we have three non-numeric features. For each non-numeric (string) feature, select and show all distinct categories.

```
# Select and show all distinct categories  
  
# Loop over all column dtypes and display information if  
# the dtype is 'string'  
# (Alternatively you could just list out the column names)  
for column, data_type in spark_df.dtypes:  
    if data_type == 'string':  
        # Select and show distinct values in that column  
        spark_df.select(column).distinct().show()
```

**Expected Output:**

```
+------+  
|   SEX|  
+------+  
|Female|  
|  Male|  
+------+  
  
+-----------+  
|  EDUCATION|  
+-----------+  
|High School|  
|          0|  
|          5|  
|          6|  
|      Other|  
|   Graduate|  
|    College|  
+-----------+  
  
+--------+  
|MARRIAGE|  
+--------+  
|       0|  
|   Other|  
| Married|  
|  Single|  
+--------+
```

It looks like we have some extraneous values in our categories. For example both EDUCATION and MARRIAGE have a category 0.

Let's create some visualizations of each of these to determine just how many of them there are.

###### **Step 4 Barplots of EDUCATION and MARRIAGE**

Create bar plots of the variables EDUCATION and MARRIAGE to see how the records are distributed between the categories.

To create a bar plot, you need to group by the category (.groupBy()) and then aggregate by the count in that category (.count()). That will result in a small DataFrame containing EDUCATION and count columns.

Then the easiest way to create a bar plot is to call .toPandas() to make that small Spark SQL DataFrame into a pandas DataFrame, and call .plot() on the pandas DataFrame.

```
# Create bar plot of EDUCATION  
# First, aggregate data  
education_cats = spark_df.groupBy('EDUCATION').count()  
education_cats.show()  
# Then plot data  
education_cats.toPandas().plot(x="EDUCATION", y="count", kind="bar", rot=0);
```

**Expected Output:**

```
+-----------+-----+  
|  EDUCATION|count|  
+-----------+-----+  
|High School| 4917|  
|          0|   14|  
|          5|  280|  
|          6|   51|  
|      Other|  123|  
|   Graduate|10585|  
|    College|14029|  
+-----------+-----+
```

![Education bar chart of the customers.](https://moringa.instructure.com/courses/1426/files/631510/download)

```
# Create bar plot of MARRIAGE  
# First, aggregate data  
marriage_cats = spark_df.groupby('MARRIAGE').count()  
marriage_cats.show()  
# Then plot data  
marriage_cats.toPandas().plot(x="MARRIAGE", y="count", kind="bar", rot=0);
```

**Expected Output:**

```
+--------+-----+  
|MARRIAGE|count|  
+--------+-----+  
|       0|   54|  
|   Other|  323|  
| Married|13658|  
|  Single|15964|  
+--------+-----+
```

![Marriage bar chart of the customers.](https://moringa.instructure.com/courses/1426/files/631383/download)

##### Part 2

It looks like there are barely any records in the 0, 5, and 6 categories. Let's go ahead and bin (combine) those with the current Other records into a single catch-all Other category for both EDUCATION and MARRIAGE.

The approach we'll use is similar to the CASE WHEN technique in SQL. If this were a SQL query, it would look something like this:

```
SELECT CASE  
       WHEN EDUCATION = '0' THEN 'Other'  
       WHEN EDUCATION = '5' THEN 'Other'  
       WHEN EDUCATION = '6' THEN 'Other'  
       ELSE EDUCATION  
       END AS EDUCATION  
  FROM credit_card_default;
```

With Spark SQL DataFrames, this is achieved using .withColumn() in conjunction with .when() and .otherwise().

###### **Step 5 Bin EDUCATION and MARRIAGE**

```
from pyspark.sql import functions as F  
# Bin EDUCATION categories  
df_education_binned = spark_df.withColumn('EDUCATION',  
                                          F.when(spark_df['EDUCATION'] == '0', 'Other')\  
                                          .when(spark_df['EDUCATION'] == '5', 'Other')\  
                                          .when(spark_df['EDUCATION'] == '6', 'Other')\  
                                          .otherwise(spark_df['EDUCATION'])  
                                         )  
# Bin MARRIAGE categories  
df_all_binned = df_education_binned.withColumn('MARRIAGE',  
                                               F.when(df_education_binned['MARRIAGE'] == '0', 'Other')\  
                                               .otherwise(df_education_binned['MARRIAGE'])  
                                              )  
  
# Select and show all distinct categories for EDUCATION and MARRIGE again  
df_all_binned.select('EDUCATION').distinct().show()  
df_all_binned.select('MARRIAGE').distinct().show()
```

**Expected Output:**

```
+-----------+  
|  EDUCATION|  
+-----------+  
|High School|  
|      Other|  
|   Graduate|  
|    College|  
+-----------+  
  
+--------+  
|MARRIAGE|  
+--------+  
|   Other|  
| Married|  
|  Single|  
+--------+
```

###### **Step 6 Plot the bins**

Let's also re-create the plots from earlier, now that the data has been binned:

```
# Plot EDUCATION  
df_all_binned.groupBy('EDUCATION')\  
             .count()\  
             .toPandas()\  
             .plot(x="EDUCATION", y="count", kind="bar", rot=0);
```

**Expected Output:**

![Bar chart results of customers&#39; education level after data has been binned.](https://moringa.instructure.com/courses/1426/files/631514/download)

```
# Plot MARRIAGE  
df_all_binned.groupBy('MARRIAGE')\  
             .count()\  
             .toPandas()\  
             .plot(x="MARRIAGE", y="count", kind="bar", rot=0);
```

**Expected Output:**

![Bar chart results of customers&#39; marriage status after data has been binned.](https://moringa.instructure.com/courses/1426/files/631367/download)

Much better. Now, let's do a little more investigation into our target variable before diving into the machine learning aspect of this project.

##### Part 3

Let's first look at the overall distribution of class balance of the default column.

###### **Step 7 Barcharts for (non-)defaults**

Create a bar plot to compare the number of defaults (0) vs. non-defaults (1). Consider customizing your plot labels as well, since 0 and 1 are not particularly understandable values.

```
import matplotlib.pyplot as plt  
  
# Group and aggregate target data  
target_cats = df_all_binned.groupBy('default').count().orderBy('default')  
target_cats.show()  
  
# Plot target data  
fig, ax = plt.subplots()  
target_cats.toPandas().plot(x='default', y='count', kind='bar', ax=ax, rot=0)  
ax.set_xlabel("Target")  
ax.set_xticklabels(['Does Not Default (0)','Defaults (1)']);
```

**Expected Output:**

```
+-------+-----+  
|default|count|  
+-------+-----+  
|      0|23364|  
|      1| 6635|  
+-------+-----+
```

![Bar chart results of customers&#39; default status.](https://moringa.instructure.com/courses/1426/files/631365/download)

Looks like we have a fairly imbalanced dataset.

###### **Step 8 Group by DEFAULT and SEX**

Let's also visualize the difference in default rate between males and females in this dataset. Group by both default and SEX and visualize the comparison.

```
# Group and aggregate target and sex data  
target_by_sex = df_all_binned.groupBy(['default', 'SEX']).count().orderBy(['default', 'SEX'])  
target_by_sex.show()  
  
# Plot target and sex data  
fig, ax = plt.subplots()  
  
target_by_sex.toPandas().pivot(index='SEX', columns='default')\  
               .plot(kind='bar', ax=ax, rot=0)  
  
ax.legend(title="Count", labels=['Does Not Default (0)','Defaults (1)']);
```

**Expected Output:**

```
+-------+------+-----+  
|default|   SEX|count|  
+-------+------+-----+  
|      0|Female|14349|  
|      0|  Male| 9015|  
|      1|Female| 3762|  
|      1|  Male| 2873|  
+-------+------+-----+
```

![Bar chart results of customers&#39; default status by sex.](https://moringa.instructure.com/courses/1426/files/631363/download)

It looks like males have an ever so slightly higher default rate than females, and also represent a smaller proportion of the dataset.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248296

Scraped At: 2026-05-15T09:55:11.386953
