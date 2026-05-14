# Lab: SQL-Style Syntax with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/625319/preview?) Lab: SQL-Style Syntax with Pandas

In this lab assessment, you will practice using SQL statements and the .query() method provided by Pandas to manipulate datasets. Pandas and SQL are both powerful tools for data manipulation and analysis, but they excel in different areas. SQL is designed for querying and managing relational databases, while pandas is a Python library for data manipulation and analysis in memory. By combining these tools, you can leverage the strengths of both:

* Data Extraction: Use SQL to efficiently query large datasets stored in databases. SQL is optimized for this and can handle complex joins and aggregations at the database level.
* Data Loading: Transfer the query results into pandas DataFrames. This brings the data into Python's ecosystem, where it can be further manipulated and analyzed.
* Data Manipulation: Once the data is in a DataFrame, use pandas' rich set of functions for cleaning, transforming, and analyzing data. Pandas is particularly good at handling time series data and performing operations on entire columns or datasets at once.
* Analysis and Visualization: With the data in pandas, you can easily perform statistical analyses, create visualizations, or feed the data into machine learning models.

This combination allows you to work with large datasets that might not fit into memory by using SQL to pre-process and filter the data before bringing it into pandas. It also lets you use familiar SQL syntax for initial data extraction before switching to pandas' pythonic interface for further analysis.

You will be able to:

* Compare accessing data in a DataFrame using query methods and conditional logic.
* Query DataFrames with SQL using the pandasql library.

### Tools and Resources

* [GitHub repository


  Links to an external site.](https://github.com/learn-co-curriculum/DS_Course1_Week1_Module4_SQLPandas)

### Instructions

In this assessment, you will be working with the Titanic Survivors dataset. This dataset contains information pertaining to whether a passenger survived the Titanic ship disaster or not. It also contains data about each passenger such as cabin, class number, and family members that were onboard.

Imagine that you're a data analyst working for a modern cruise line company. The company is planning to launch a new marketing campaign emphasizing their commitment to passenger safety. They want to use historical data from the Titanic disaster to create compelling narratives and inform their safety policies. You have been tasked with analyzing what factors might have affected survivorship.

Begin by running the provided code imports.

```
# Run this cell without changes  
  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from pandasql import sqldf
```

### [Part 1: Load Data](#dpPanel0)

1. Using pandas, read in the data from titanic.csv and store it as a DataFrame in the variable df. Pass in index\_col=0 as an argument when loading in the data. Display the .head() to ensure that everything is loaded correctly.

### [Part 2: Slicing Dataframes](#dpPanel1)

In this section, you're looking to investigate whether women and children survived more than men, or that rich passengers were more likely to survive than poor passengers. The easiest way to confirm this is to slice the data into dataframes that contain each subgroup, and then quickly visualize the survival rate of each subgroup with histograms.

2. Create a dataframe that contains all passengers that are female, and also contains all children (males included) ages 15 and under.  
     
   Additionally, create a dataframe that contains only adult male passengers over the age of 15.
   1. Now, you can use the matplotlib functionality built into the dataframe objects to quickly create visualizations of the Survived column for each DataFrame. Create a histogram visualization is of the Survived column for both dataframes.
3. Now, let's repeat the same process, but separating rich and poor passengers. Create one dataframe containing First Class passengers (Pclass == 1), and another dataframe containing everyone else.
   1. Now, we create histograms of the survival for each subgroup, just as above.

Slicing is a useful method for quickly getting DataFrames that contain only the examples we're looking for. It's a quick, easy method that feels intuitive in Python, since we can rely on the same conditional logic that we would if we were just writing if/else statements.

### [Part 3: Querying Dataframes](#dpPanel2)

Instead of slicing, you can also make use of the DataFrame's built-in .query() method. This method reads a bit more cleanly and allows us to pass in our arguments as a string.

4. Use the .query() method to slice a dataframe that contains only passengers who have a PassengerId greater than or equal to 500.

Just as with slicing, you can pass in queries with multiple conditions. One unique difference between using the .query() method and conditional slicing is that you can use and or & as well as or or | (for fun, try reading this last sentence out loud), while you are limited to the & and | symbols to denote and/or operations with conditional slicing.

Let's take a look at trying to reproduce the slicing from the previous question about females and children above but this time using the .query() method instead. Because it is based on query language it will inherently be faster computationally.

5. Use the query() method to return a dataframe that contains all female passengers and all children under the age of 15 (male and female).  
    *Hint: Although the entire query is a string, you'll still need to denote that female is also a string, within the string. You will want to make use of both single (') and double (") quotes (String-Ception?).*

### [Part 4: Eval Method](#dpPanel3)

A cousin of the query() method, eval() allows you to use the same string-filled syntax as querying for creating new columns and evaluating conditional expressions against a DataFrame. This method also allows the user to specify if the operation should be done in place or not, providing a quick, easy syntax for complex feature engineering based on python operators.

6. Use the dataframe's eval() method to add a new column called 'Age\_x\_Fare', that equals the 'Age' multiplied by the 'Fare' for each passenger. Save over the existing dataframe object.

### [Part 5: Querying Dataframes with SQL](#dpPanel4)

For this section of the assessment, you'll make use of the pandasql library. Pandasql is a library designed to make it easy to query DataFrames directly with SQL syntax, which was open-sourced by the company, Yhat, in late 2016.

In the first cell of the notebook we imported pandsql as sqldf for you to use.

pandasql allows you to pass in SQL queries in the form of a string to directly query your database. Each time you make a query, you need to pass an additional parameter that gives it access to the other variables in the session/environment. You can use a lambda function to pass locals() or globals() so that you don't have to type this every time.

7. Create a variable called pysqldf and define it as a lambda function that will return the passed globals and the query. Refer to the lesson and reading material if this is unclear.
8. Write a SQL query that returns the names of the first 10 passengers. Use the pysqldf object you just created above to read the string query, defined as query1, and return a dataframe.   
     
   *Hint: Consider the name of the table you need to select from here, remember that you are trying to query your DataFrame object.*
9. Query the dataframe for the names and fares of any male passengers that survived, limit the results to the first 30 rows.

This library is really powerful! This makes it easy for you to leverage all of your SQL knowledge to quickly query any DataFrame, especially when you only want to select certain columns. This saves you from having to slice/query the DataFrame and then slice the columns you want (or drop the ones you don't want).

Although it's outside the scope of this assessment, it's also worth noting that both pandas and pandasql provide built-in functionality for join operations, too!

### [Part 6: Compare Counts](#dpPanel5)

10. Create two separate DataFrames using pandasql. Your goal is to compare the different passenger class (Pclass) counts for all female passengers that survived against all female passengers that did not survive to see if class had an effect specifically on female survivorship.

Query3 should represent female passengers that survived and query4 should represent female passengers that did not survive.

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

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243850

Scraped At: 2026-05-14T21:17:02.702264
