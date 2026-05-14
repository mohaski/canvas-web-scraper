# Lab: Getting Started with Databases and SQL

## ![](https://moringa.instructure.com/courses/1406/files/625319/preview) Lab: Getting Started with Databases and SQL

In this assessment lab, you will explore basic techniques for retrieving and transforming data using SQL (Structured Query Language) in Python. You will be working with the employees table stored in the data.sqlite file. Imagine that you are working within the HR department of the fictional Northwinds Company as a data specialist/analyst and need to be able to easily access select employee records.

SQL is a powerful language that allows us to interact with relational databases and perform various operations on the data. By leveraging SQL queries, we can efficiently retrieve specific subsets of data, create meaningful aliases for improved readability, transform selected columns using CASE statements, and utilize built-in SQL functions to perform advanced transformations.

### Tools and Resources

* [GitHub Repository: SQL Select


  Links to an external site.](https://github.com/learn-co-curriculum/DS_Course1_Week1_Module1_SQLSelectLab/tree/main)

### Instructions

### [Part 1: Connecting to the Data](#dpPanel0)

A SQL database file has been provided that contains the Northwind company's product, customer and employee data (fictional). For the scope of this assessment you will focus mostly on the employees tables. You will be asked to retrieve specific information/data using SQL queries in tandem with Pandas to load the results into a DataFrame.

**Example:**

```
df_answer = pd.read_sql("""SELECT * FROM some_table""", connection)
```

#### Step 1

Import the necessary libraries, sqlite3 and pandas. Use the standard alias for the pandas library. Create a connection to the data.sqlite database file and store it as the variable conn.

```
# CodeGrade step1  
# Replace None with your code  
  
# SQL Library and Pandas  
import sqlite3  
import pandas as pd  
  
# Connect to the database  
conn = None
```

As previously stated, this database contains multiple tables but for this assessment you will focus on querying data from the employees table and later from the orderDetails table. In the cell below we have provided code that selects all columns and rows from the employees table for you to use as reference.

```
# Run this cell without changes  
# First look at full table  
pd.read_sql("""SELECT * FROM employees""", conn)
```

### [Part 2: Basic Select Filtering](#dpPanel1)

#### Step 2

Return the employee number and last name from all employees in the employees table in the database. Your result should only contain those two columns.

```
# CodeGrade step2  
# Replace None with your code  
df_name_number = None
```

#### Step 3

Repeat Step 2, but have the last name come before the employee number.

```
# CodeGrade step3  
# Replace None with your code  
df_reverse = None
```

### [Part 3: Aliasing in Select](#dpPanel2)

#### Step 4

Repeat Step 3, but this time use an alias to rename the employee number column as 'ID'.

```
# CodeGrade step4  
# Replace None with your code  
df_alias = None
```

### [Part 4: CASE Function](#dpPanel3)

#### Step 5

Use 'CASE' to bin where the jobTitles of President, VP Sales, or VP Marketing have the 'role' of "Executive", and the rest of the employees are "Not Executive".

Define the result of the 'CASE' as a new column called 'role.'

**Hint:** For the WHEN clause if we were looking at Managers, we'd have:

```
WHEN jobTitle = "Sales Manager (APAC)" OR jobTitle = "Sale Manager (EMEA)" OR jobTitle = "Sales Manager (NA)" THEN "Manager"
```

```
# CodeGrade step5  
# Replace None with your code  
df_executive = None
```

### [Part 5: Built-In Functions - Strings](#dpPanel4)

#### Step 6

Find the length of the last name for all employees, return only this data as a new column called 'name\_length'.

```
# CodeGrade step6  
# Replace None with your code  
df_name_length = None
```

#### Step 7

Return only one new column called 'short\_title', that contains the first two letters of each person's job title.

```
# CodeGrade step7  
# Replace None with your code  
df_short_title = None
```

### [Part 6: Built-In Functions - Numerics](#dpPanel5)

#### Bring in another table from the database

In the cell below we have provided a look at a new table within the database provided. This table contains data pertaining to orders placed with the company and has some good numerical and date columns to explore.

```
# Run this cell without changes  
  
pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
```

#### Step 8

Find the total amount for all orders, calculated as the sum of rounded total prices, where the total price for each order is the 'priceEach' multiplied by the 'quantityOrdered'. Make sure you are rounding this internal product result.

**Hint:** Append .sum() to the end of your returned query that contains total price for each order, in order to create the total amount. You could also use the SUM() built-in SQL function as well. For example:

```
sum_total = pd.read_sql("""  
SELECT total_price  
FROM some_table  
""", conn).sum()
```

```
# CodeGrade step8  
# Replace None with your code  
sum_total_price = None
```

#### Step 9

It is common in other parts of the world as well as the US Military to have dates as Day/Month/Year. Return the original order date column followed by three new columns that display the order date in this format with column names 'day', 'month', and 'year' respectively.

```
# CodeGrade step9  
# Replace None with your code  
df_day_month_year = None
```

#### Close the connection

```
# Run this cell without changes  
  
conn.close()
```

### Submission and Grading Criteria

1. Review the rubric below as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
3. When you are ready to submit, launch CodeGrade.
   * Click on + Create Submission. Upload your Jupyter notebook file for this lab.
   * For additional information on submitting assignments in CodeGrade: [Getting Started in CanvasLinks to an external site.


     Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
   * You can review your submission in CodeGrade and see your score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243698

Scraped At: 2026-05-14T21:08:24.193221
