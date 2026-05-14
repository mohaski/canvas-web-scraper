# Practice: One-to-Many and Many-to-Many Relationships

# Practice: One-to-Many and Many-to-Many Relationships

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: One-to-Many and Many-to-Many Relationships

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

In this practice, you'll be working with Python and SQLite to explore different types of joins within a relational database, helping you understand how to combine data from multiple tables effectively.

First, you'll start by performing a one-to-one join between the Employees and Offices tables, where you'll select each employee's first and last name, along with the city and state of the office they work out of (if they have one). You'll include all employees in your query, ensuring the results are ordered by their first name and last name.

Next, you'll practice a one-to-many join by selecting customer contacts (first and last names) and linking them with their corresponding order details, such as order numbers, order dates, and statuses.

After that, you'll carry out another one-to-many join to link customer contacts with their payment details, retrieving payment amounts and dates, and sorting the results in descending order by payment amount to highlight the largest transactions.

Finally, you'll tackle a many-to-many join, where you'll combine data from customers, orders, and product details. Here, you'll select customer contacts along with the names of products they've ordered, the quantities ordered, and the dates of those orders, arranging the results in descending order by the order date.

Through these exercises, you'll gain hands-on experience with different types of joins, helping you to understand how to navigate and extract meaningful insights from complex relational databases.

We will use an existing database to demonstrate how to apply these concepts in SQL.

### Resources

* [GitHub Repository (practice 2)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c1w1m3)

### Instructions

Begin by importing the libraries and connecting to the database.

Include the relevant imports, then connect to the database located at data.sqlite.

```
# Run this code without change  
  
import sqlite3  
import pandas as pd  
  
conn = sqlite3.connect('data.sqlite')
```

1. Employees and Their Offices (a One-to-One Join): Select all of the employees including their first name and last name along with the city and state of the office that they work out of (if they have one). Include all employees and order them by their first name, then their last name.
2. Customers and Their Orders (a One-to-Many Join): Select all of the customer contacts (first and last names) along with details for each of the customers' order numbers, order dates, and statuses..
3. Customers and Their Payments (Another One-to-Many Join): Select all of the customer contacts (first and last names) along with details for each of the customers' payment amounts and date of payment. Sort these results in descending order by the payment amount.
4. Orders, Order Details, and Product Details (a Many-to-Many Join): Select all of the customer contacts (first and last names) along with the product names, quantities, and date ordered for each of the customers and each of their orders. Sort these in descending order by the order date.

### Solution

#### Select for Solution

##### Step 1

```
q = """  
SELECT firstName, lastName, city, state  
FROM employees  
JOIN offices  
    USING(officeCode)  
ORDER BY firstName, lastName  
;  
"""  
df = pd.read_sql(q, conn)  
print('Total number of results:', len(df))  
df.head()
```

**Expected Output:**

 Total number of results: 23

Data Output: Step 1

|  | firstName | lastName | city | state |
| --- | --- | --- | --- | --- |
| 0 | Andy | Fister | Sydney |  |
| 1 | Anthony | Bow | San Francisco | CA |
| 2 | Barry | Jones | London |  |
| 3 | Diane | Murphy | San Francisco | CA |
| 4 | Foon Yue | Tseng | NYC | NY |

##### Step 2

```
q = """  
SELECT  
    contactFirstName,  
    contactLastName,  
    orderNumber,  
    orderDate,  
    status  
FROM customers  
JOIN orders  
    USING(customerNumber)  
;  
"""  
df = pd.read_sql(q, conn)  
print('Total number of results:', len(df))  
df.head()
```

**Expected Output:**

Total number of results: 326

Data Output: Step 2

|  | contactFirstName | contactLastName | orderNumber | orderDate | status |
| --- | --- | --- | --- | --- | --- |
| 0 | Carine | Schmitt | 10123 | 2003-05-20 | Shipped |
| 1 | Carine | Schmitt | 10298 | 2004-09-27 | Shipped |
| 2 | Carine | Schmitt | 10345 | 2004-11-25 | Shipped |
| 3 | Jean | King | 10124 | 2003-05-21 | Shipped |
| 4 | Jean | King | 10278 | 2004-08-06 | Shipped |

##### Step 3

```
q = """  
SELECT  
    contactFirstName,  
    contactLastName,  
    amount,  
    paymentDate  
FROM customers  
JOIN payments  
    USING(customerNumber)  
ORDER BY amount DESC  
;  
"""  
df = pd.read_sql(q, conn)  
print('Total number of results:', len(df))  
df.head()
```

Expected Output:

Total number of results: 273

Data Output: Step 3

|  | contactFirstName | contactLastName | amount | paymentDate |
| --- | --- | --- | --- | --- |
| 0 | Diego | Freyre | 120166.58 | 2005-03-18 |
| 1 | Diego | Freyre | 116208.40 | 2004-12-31 |
| 2 | Susan | Nelson | 111654.40 | 2003-08-15 |
| 3 | Eric | Natividad | 105743.00 | 2003-12-26 |
| 4 | Susan | Nelson | 101244.59 | 2005-03-05 |

##### Step 4

```
q = """  
SELECT  
    contactFirstName,  
    contactLastName,  
    productName,  
    quantityOrdered,  
    orderDate  
FROM customers  
JOIN orders  
    USING(customerNumber)  
JOIN orderdetails  
    USING(orderNumber)  
JOIN products  
    USING (productCode)  
ORDER BY orderDate DESC  
;"""  
df = pd.read_sql(q, conn)  
print('Total number of results:', len(df))  
df.head()
```

**Expected Output:**

Total number of results: 2996

Data Output: Step 4

|  | contactFirstName | contactLastName | productName | quantityOrdered | orderDate |
| --- | --- | --- | --- | --- | --- |
| 0 | Janine | Labrune | 1962 LanciaA Delta 16V | 38 | 2005-05-31 |
| 1 | Janine | Labrune | 1957 Chevy Pickup | 33 | 2005-05-31 |
| 2 | Janine | Labrune | 1998 Chrysler Plymouth Prowler | 28 | 2005-05-31 |
| 3 | Janine | Labrune | 1964 Mercedes Tour Bus | 38 | 2005-05-31 |
| 4 | Janine | Labrune | 1926 Ford Fire Engine | 19 | 2005-05-31 |

```
# Remember to close the connection when you are done  
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243782

Scraped At: 2026-05-14T21:13:41.973655
