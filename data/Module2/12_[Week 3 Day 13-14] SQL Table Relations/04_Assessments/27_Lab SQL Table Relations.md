# Lab: SQL Table Relations

## ![](https://moringa.instructure.com/courses/1406/files/625319/preview?) Lab: SQL Table Relations

In this lab assessment, you'll practice your knowledge of JOIN statements and subqueries, using various types of joins and various methods for specifying the links between them. One of the main benefits of using a relational database is the table relations that define them which allow you to access and connect data together via shared columns. By writing more advanced SQL queries that utilize joins and subqueries you can provide a deeper and more granular level of analysis and data retrieval.

This assessment will continue looking at the familiar Northwind database that contains customer relationship management (CRM) data as well as employee and product data. You will take a deeper dive into this database in order to accomplish more advanced SQL queries that require you to access data from multiple tables at once.

Imagine that you are working in an analyst role for the sales rep team. They have collaborated with the customer relations and the product teams to take a comprehensive look at the employee to customer pipeline in an attempt to find areas of improvement and potential growth. You have been asked to provide some specific data and statistics regarding this project.

You will be able to:

* Write SQL queries that make use of various types of joins.
* Perform the best type of join for retrieving desired data.
* Write subqueries to decompose complex queries.
* Limit the number of records returned by a query using LIMIT.
* Use Group BY statements in SQL to apply aggregate functions.

### Tools and Resources

* [GitHub repository


  Links to an external site.](https://github.com/learn-co-curriculum/DS_Course1_Week1_Module2_SQLTables)

### Instructions

The database will be the customer relationship management (CRM) database, which has the following ERD.

[![ERD for the CRM database](https://moringa.instructure.com/courses/1406/files/625425/download?)](https://moringa.instructure.com/courses/1406/files/625425/download? "ERD for the CRM database")

You will begin by connecting to the database. In the block below, we have provided the code to import both pandas and sqlite3 as well as define and create the connection to the database you will use. Also displayed is the schema and table names from the database. Use this information in conjunction with the ERD image above to assist in creating your SQL Queries. *Major Hint: Look for the shared columns across tables you need to 'join' together.*

```
# Run this cell without changes  
  
# SQL Library and Pandas Library  
import sqlite3  
import pandas as pd  
  
# Connect to the database  
conn = sqlite3.connect('data.sqlite')  
  
pd.read_sql("""SELECT * FROM sqlite_master""", conn)
```

### [Part 1: Join and Filter](#dpPanel0)

1. The company would like to let Boston employees go remote but need to know more information about who is working in that office. Return the first and last names and the job titles for all employees in Boston.
2. Recent downsizing and employee attrition have caused some mixups in office tracking and the company is worried they are supporting a 'ghost' location. Are there any offices that have zero employees?

### [Part 2: Type of Join](#dpPanel1)

3. As a part of this larger analysis project the HR department is taking the time to audit employee records to make sure nothing is out of place and have asked you to produce a report of all employees. Return the employees first name and last name along with the city and state of the office that they work out of (if they have one). Include all employees and order them by their first name, then their last name.
4. The customer management and sales rep team know that they have several 'customers' in the system that have not placed any orders. They want to reach out to these customers with updated product catalogs to try and get them to place initial orders. Return all of the customer's contact information (first name, last name, and phone number) as well as their sales rep's employee number for any customer that has not placed an order. Sort the results alphabetically based on the contact's last name. There are several approaches you could take here, including a left join and filtering on null values or using a subquery to filter out customers who do have orders. In total there are 24 customers who have not placed an order.

### [Part 3: Built-In Function](#dpPanel2)

5. The accounting team is auditing their figures and wants to make sure all customer payments are in alignment, they have asked you to produce a report of all the customer contacts (first and last names) along with details for each of the customers' payment amounts and date of payment. They have asked that these results be sorted in descending order by the payment amount. *Hint: A member of their team mentioned that they are not sure the 'amount' column is being stored as the right datatype so keep this in mind when sorting.*

### [Part 4: Joining and Grouping](#dpPanel3)

6. The sales rep team has noticed several key team members that stand out as having trustworthy business relations with their customers, reflected by high credit limits indicating more potential for orders. The team wants you to identify these 4 individuals. Return the employee number, first name, last name, and number of customers for employees whose customers have an average credit limit over 90k. Sort by number of customers from high to low.
7. The product team is looking to create new model kits and wants to know which current products are selling the most in order to get an idea of what is popular. Return the product name and count the number of orders for each product as a column named 'numorders'. Also return a new column, 'totalunits', that sums up the total quantity of product sold (use the quantityOrdered column). Sort the results by the totalunits column, highest to lowest, to showcase the top selling products.

### [Part 5: Multiple Joins](#dpPanel4)

8. As a follow-up to the above question, the product team also wants to know how many different customers ordered each product to get an idea of market reach. Return the product name, code, and the total number of customers who have ordered each product, aliased as 'numpurchasers'. Sort the results by the highest number of purchasers. *Hint: You might need to join more than 2 tables. Use DISTINCT to return unique/different values.*
9. The custom relations team is worried they are not staffing locations properly to account for customer volume. They want to know how many customers there are per office. Return the count as a column named 'n\_customers'. Also return the office code and city.

### [Part 6: Subquery](#dpPanel5)

10. Having looked at the results from above, the product team is curious to dig into the underperforming products. They want to ask members of the team who have sold these products about what kind of messaging was successful in getting a customer to buy these specific products. Using a subquery or common table expression (CTE), select the employee number, first name, last name, city of the office, and the office code for employees who sold products that have been ordered by fewer than 20 customers. *Hint: Start with the subquery, find all the products that have been ordered by 19 or less customers, consider adapting one of your previous queries.*
11. Close the connection.

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

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243815

Scraped At: 2026-05-14T21:15:11.093923
