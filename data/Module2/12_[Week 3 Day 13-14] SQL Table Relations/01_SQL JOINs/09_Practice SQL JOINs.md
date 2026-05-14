# Practice: SQL JOINs

# Practice: SQL JOINs

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: SQL JOINs

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

Suppose you've been tasked by your manager to delve into the company's database to explore and analyze data with the goal of establishing a reward program for employees. This program would be based on the type and number of products each employee has sold. In addition, management has expressed interest in understanding the distribution of employees and customers across various office locations. To achieve these objectives, you would likely employ a combination of SQL queries and Python's sqlite3 library to interact with the database, extract relevant data, and perform necessary analyses.

Using Python with sqlite3, you can connect to the company's SQLite database and execute SQL queries that involve joining multiple tables to gather comprehensive insights. For instance, you would need to join tables that contain employee details, sales records, product information, and office locations. By doing so, you can identify which employees have sold the most products, categorize the sales by product type, and aggregate this information to determine who qualifies for the reward program.

Additionally, you can perform joins between employee and office tables to analyze the number of employees at each office, and between customer and office tables to understand the distribution of customers across locations. This analysis not only aids in the design of the reward program but also provides management with a clearer picture of how resources and clients are distributed across the company’s various offices.

The power of using sqlite3 in Python lies in its ability to seamlessly execute SQL commands and manage the resulting data within Python, allowing for further manipulation and analysis using Python’s data science libraries. By combining SQL joins with Python’s analytical capabilities, you can produce detailed reports and visualizations that inform strategic decisions regarding employee rewards and resource allocation across the company. This approach not only facilitates the immediate task of setting up the reward program but also equips the management with valuable insights for future business planning.

### Resources

* [GitHub Repository (practice 1)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c1w1m3)

### Instructions

Try finding the answers to following questions using Jupyter notebook. When you are finished, you can check your code and expected outputs in the Solution section.

1. Select the names of all employees in Boston.
2. Are there any offices that have zero employees?
3. How many customers are there per office?
4. Display the names of every individual product that each employee has sold as a dataframe.
5. Display the number of products each employee has sold.  
   1. Alphabetize the results by employee last name.
   2. Use the quantityOrdered column from orderDetails.
   3. Think about how to group the data when some employees might have the same first or last name.
6. Display the names of employees who have sold more than 200 different products.

### Solution

### [Select for Solution](#dpPanel0)

#### Step 1

```
conn = sqlite3.connect('data.sqlite')
```

```
q = """  
SELECT firstName, lastName  
FROM employees  
JOIN offices  
    USING(officeCode)  
WHERE city = 'Boston'  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Expected Output: Step 1

|  | firstName | lastName |
| --- | --- | --- |
| 0 | Julie | Firrelli |
| 1 | Steve | Patterson |

#### Step 2

```
# Note that COUNT(*) is not appropriate here because  
# we are trying to count the _employees_ in each group.  
# So instead we count by some attribute of an employee  
# record. The primary key (employeeNumber) is a   
# conventional way to do this  
q = """  
SELECT  
    o.officeCode,  
    o.city,  
    COUNT(e.employeeNumber) AS n_employees  
FROM offices AS o  
LEFT JOIN employees AS e  
    USING(officeCode)  
GROUP BY officeCode  
HAVING n_employees = 0  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Expected Output: Step 2

|  | officeCode | city | n\_employees |
| --- | --- | --- | --- |
| 0 | 27 | Boston | 0 |

#### Step 3

```
# how many  
  
q = """  
SELECT  
    o.officeCode,  
    o.city,  
    COUNT(c.customerNumber) AS n_customers  
FROM offices AS o  
JOIN employees AS e  
    USING(officeCode)  
JOIN customers AS c  
    ON e.employeeNumber = c.salesRepEmployeeNumber  
GROUP BY officeCode  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Expected Output: Step 3

|  | officeCode | city | n\_customers |
| --- | --- | --- | --- |
| 0 | 1 | San Francisco | 12 |
| 1 | 2 | Boston | 12 |
| 2 | 3 | NYC | 15 |
| 3 | 4 | Paris | 29 |
| 4 | 5 | Tokyo | 5 |
| 5 | 6 | Sydney | 10 |
| 6 | 7 | London | 17 |

#### Step 4

```
# We don't need to use aliases for the columns since they  
# are conveniently already labeled as different kinds of  
# names (firstName, lastName, productName)  
q = """  
SELECT firstName, lastName, productName  
FROM employees AS e  
JOIN customers AS c  
    ON e.employeeNumber = c.salesRepEmployeeNumber  
JOIN orders  
    USING(customerNumber)  
JOIN orderdetails  
    USING(orderNumber)  
JOIN products  
    USING(productCode)  
;  
"""  
df = pd.read_sql(q, conn)  
df
```

**Expected Output:**

Expected Output: Step 4

|  | firstName | lastName | productName |
| --- | --- | --- | --- |
| 0 | Leslie | Jennings | 1958 Setra Bus |
| 1 | Leslie | Jennings | 1940 Ford Pickup Truck |
| 2 | Leslie | Jennings | 1939 Cadillac Limousine |
| 3 | Leslie | Jennings | 1996 Peterbilt 379 Stake Bed with Outrigger |
| 4 | Leslie | Jennings | 1968 Ford Mustang |
| ... | ... | ... | ... |
| 2991 | Martin | Gerard | 1954 Greyhound Scenicruiser |
| 2992 | Martin | Gerard | 1950's Chicago Surface Lines Streetcar |
| 2993 | Martin | Gerard | Diamond T620 Semi-Skirted Tanker |
| 2994 | Martin | Gerard | 1911 Ford Town Car |
| 2995 | Martin | Gerard | 1936 Mercedes Benz 500k Roadster |

#### Step 5

```
q = """  
SELECT firstName, lastName, SUM(quantityOrdered) as total_products_sold  
FROM employees AS e  
JOIN customers AS c  
    ON e.employeeNumber = c.salesRepEmployeeNumber  
JOIN orders  
    USING(customerNumber)  
JOIN orderdetails  
    USING(orderNumber)  
GROUP BY firstName, lastName  
ORDER BY lastName  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

SQL Data Set: Salesperson Total Products Sold

| Index | First Name | Last Name | Total Products Sold |
| --- | --- | --- | --- |
| 0 | Loui | Bondur | 6186 |
| 1 | Larry | Bott | 8205 |
| 2 | Pamela | Castillo | 9290 |
| 3 | Julie | Firrelli | 4227 |
| 4 | Andy | Fixter | 6246 |
| 5 | Martin | Gerard | 4180 |
| 6 | Gerard | Hernandez | 14231 |
| 7 | Leslie | Jennings | 11854 |
| 8 | Barry | Jones | 7486 |
| 9 | Peter | Marsh | 6632 |
| 10 | Mami | Nishi | 4923 |
| 11 | Steve | Patterson | 5561 |
| 12 | Leslie | Thompson | 4056 |
| 13 | Foon Yue | Tseng | 5016 |
| 14 | George | Vanauf | 7423 |

#### Step 6

```
# Recall that HAVING is used for filtering after an aggregation  
q = """  
SELECT firstName, lastName, COUNT(productCode) as different_products_sold  
FROM employees AS e  
JOIN customers AS c  
    ON e.employeeNumber = c.salesRepEmployeeNumber  
JOIN orders  
    USING(customerNumber)  
JOIN orderdetails  
    USING(orderNumber)  
GROUP BY firstName, lastName  
HAVING different_products_sold > 200  
ORDER BY lastName  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Expected Output: Step 6

|  | firstName | lastName | different\_products\_sold |
| --- | --- | --- | --- |
| 0 | Larry | Bott | 236 |
| 1 | Pamela | Castillo | 272 |
| 2 | Gerard | Hernandez | 396 |
| 3 | Leslie | Jennings | 331 |
| 4 | Barry | Jones | 220 |
| 5 | George | Vanauf | 211 |

```
# Remember to close the connection when you are done  
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243764

Scraped At: 2026-05-14T21:12:42.914755
