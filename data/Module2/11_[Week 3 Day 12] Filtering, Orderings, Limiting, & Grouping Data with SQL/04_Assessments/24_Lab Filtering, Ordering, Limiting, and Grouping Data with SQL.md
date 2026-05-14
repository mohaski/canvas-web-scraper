# Lab: Filtering, Ordering, Limiting, and Grouping Data with SQL

## ![](https://moringa.instructure.com/courses/1406/files/625319/preview) Lab: Filtering, Ordering, Limiting, and Grouping Data with SQL

In this lab assessment, you will explore writing more advanced SQL queries aimed at analyzing data on a more granular level. You will be working with 3 different databases throughout the assessment.

* planets.db: Contains data pertaining to planets in our solar system
* dogs.db: Contains data pertaining to famous fictional dog characters
* babe\_ruth.db: Contains data pertaining to Babe Ruth's baseball career statistics

SQL (Structured Query Language) provides powerful tools for manipulating and analyzing data in relational databases. Four key operations for working with data are filtering, ordering, limiting, and grouping. These operations can be combined in a single query to perform complex data analysis and extraction tasks, allowing for powerful and flexible data manipulation.

You will be able to:

* Retrieve a subset of records from a table using a WHERE clause.
* Filter results using conditional operators.
* Apply an aggregate function to the result of a query.
* Order the results of your queries by using ORDER BY (ASC & DESC).
* Limit the number of records returned by a query using LIMIT.
* Use Group BY statements in SQL to apply aggregate functions.

### Tools and Resources

* [GitHub repository: SQLQueries


  Links to an external site.](https://github.com/learn-co-curriculum/DS_Course1_Week1_Module2_SQLQueries)

### Instructions

You will begin by looking at the planets data to perform some basic filtering queries.

```
# Run this cell without changes  
  
import pandas as pd  
import sqlite3  
  
# Create the connection  
# Note the connect is 'conn1' since there will be multiple .db used  
conn1 = sqlite3.connect('planets.db')  
  
# Select all  
pd.read_sql("""SELECT * FROM planets; """, conn1)
```

### [Part 1: Basic Filtering](#dpPanel0)

1. Return all the columns for planets that have 0 moons.
2. Return the name and mass of each planet that has a name with exactly 7 letters. Avoid hard coding this filter subset as much as possible.

### [Part 2: Advanced Filtering](#dpPanel1)

3. Return the name and mass for each planet that has a mass that is less than or equal to 1.00.
4. Return all the columns for planets that have at least one moon and a mass less than 1.00.
5. Return the name and color of planets that have a color containing the string "blue".

### [Part 3: Ordering and Limiting](#dpPanel2)

This database has some fictional, yet generally famous, dogs.

```
# Run this cell without changes  
  
# Create a connection  
# Note the connect is 'conn2' since they will be multiple .db used  
conn2 = sqlite3.connect('dogs.db')  
  
# Select all  
pd.read_sql("SELECT * FROM dogs;", conn2)
```

6. Return the name, age, and breed of all dogs that are hungry (binary flag of 1) and sort them from youngest to oldest.
7. Return the name, age, and hungry columns for hungry dogs between the ages of two and seven. This query should also sort these dogs in alphabetical order.
8. Return the name, age, and breed for the 4 oldest dogs. Sort the result alphabetically based on the breed.

### [Part 4: Aggregation](#dpPanel3)

In the next few parts, you'll query data from a table populated with Babe Ruth's career hitting statistics. You'll use aggregate functions to pull interesting information from the table that basic queries cannot track.

```
# Run this cell without changes  
  
# Create a connection  
# Note the connect is 'conn3' since they will be multiple .db used  
conn3 = sqlite3.connect('babe_ruth.db')  
  
# Select all  
pd.read_sql("""  
SELECT * FROM babe_ruth_stats; """, conn3)
```

9. Return the total number of years that Babe Ruth played professional baseball.
10. Return the total number of home runs hit by Babe Ruth during his career.

### [Part 5: Grouping and Aggregation](#dpPanel4)

11. For each team that Babe Ruth has played on, return the team name and the number of years he played on that team, aliased as 'number\_years'.
12. For each team that Babe Ruth played on and averged over 200 at bats with, return the team name and average number of at bats, aliased as 'average\_at\_bats'.
13. Close the connections.

### Submission and Grading Criteria

1. Review the rubric below as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
3. When you are ready to submit, launch CodeGrade.
   * Click on + Create Submission. Upload your Jupyter notebook file for this lab.
   * For additional information on submitting assignments in CodeGrade: [Getting Started in CanvasLinks to an external site.


     Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
   * You can review your submission in CodeGrade and see your score in your Canvas gradebook

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243740

Scraped At: 2026-05-14T21:11:25.591952
