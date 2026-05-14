# Practice: SQL Subqueries

# Practice: SQL Subqueries

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: SQL Subqueries

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

Now that you’ve explored how subqueries function, it’s time to practice writing them. While not every query you’ll encounter will require a subquery, the exercises ahead will involve more complex scenarios that demand careful consideration of SQL concepts such as aggregates, grouping, ordering, filtering, joins, and subqueries. These challenges will help you apply what you’ve learned, pushing you to break down complex queries into manageable parts using subqueries where appropriate. As you work through these exercises, remember that the goal is to decompose complex queries into simpler components. By leveraging subqueries, you can enhance the clarity and efficiency of your SQL statements, making it easier to retrieve and analyze data even in intricate database structures. This practice will reinforce your understanding and improve your ability to handle real-world data challenges.

Management has tasked you with using the company's CRM database to conduct a detailed analysis of both the employees and the products sold by the company. Specifically, you will need to investigate the total number of orders for each product and identify the products that have attracted the highest number of unique customers. This analysis will include selecting the total number of orders associated with each product name and determining how many distinct individuals have placed orders for each product.

Additionally, you are asked to focus on the performance of employees, particularly those who have sold products that have been ordered by fewer than 20 customers. For these employees, you will need to extract details such as their employee number, first and last names, the city in which their office is located, and their office code. Lastly, the investigation extends to identifying employees whose customer base has an average credit limit exceeding $15,000. For these employees, you will provide their employee number, first and last names, and the number of customers they manage. This analysis will help management gain insights into product popularity and employee performance in relation to customer credit profiles.

### Resources

* [GitHub Repository (practice 3)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c1w1m3)

### Instructions

As usual, start by importing the necessary packages and connecting to the database.

```
import sqlite3  
import pandas as pd  
conn = sqlite3.Connection('data.sqlite')
```

1. Write an equivalent query using a subquery. The following query works using a JOIN. Rewrite it so that it uses a subquery instead.  

   ```
   SELECT  
       customerNumber,  
       contactLastName,  
       contactFirstName  
   FROM customers  
   JOIN orders   
       USING(customerNumber)  
   WHERE orderDate = '2003-01-31'  
   ;
   ```
2. Select the total number of orders for each product name. Sort the results by the total number of items sold for that product.
3. Select the product name and the total number of people who have ordered each product. Sort the results in descending order.  
     
   *A quick note on the SQL SELECT DISTINCT statement:* The SELECT DISTINCT statement is used to return only distinct values in the specified column. In other words, it removes the duplicate values in the column from the result set. Inside a table, a column often contains many duplicate values; and sometimes you only want to list the unique values. If you apply the DISTINCT clause to a column that has NULL, the DISTINCT clause will keep only one NULL and eliminates the other. In other words, the DISTINCT clause treats all NULL “values” as the same value.
4. Select the employee number, first name, last name, city (of the office), and office code of the employees who sold products that have been ordered by fewer than 20 people. *Hint:*  To start, think about how you might break the problem up. Be sure that your results only list each employee once.
5. Select the employee number, first name, last name, and number of customers for employees whose customers have an average credit limit over 15K.

### Solution

#### Select for Solution

##### Step 1

```
SELECT  
    customerNumber,  
    contactLastName,  
    contactFirstName  
FROM customers  
JOIN orders   
    USING(customerNumber)  
WHERE orderDate = '2003-01-31'  
;
```

```
q = """  
  
SELECT  
    customerNumber,  
    contactLastName,  
    contactFirstName  
FROM customers  
WHERE customerNumber IN (  
    SELECT customerNumber   
    FROM orders   
    WHERE orderDate = '2003-01-31'  
)  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Data Output: Step 1

|  | customerNumber | contactLastName | contactFirstName |
| --- | --- | --- | --- |
| 0 | 141 | Freyre | Diego |

##### Step 2

```
q = """  
SELECT  
    productName,  
    COUNT(orderNumber) AS numberOrders,  
    SUM(quantityOrdered) AS totalUnitsSold  
FROM products  
JOIN orderdetails  
    USING (productCode)  
GROUP BY productName  
ORDER BY totalUnitsSold DESC  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Data Output: Step 2

|  | productName | numberOrders | totalUnitsSold |
| --- | --- | --- | --- |
| 0 | 1992 Ferrari 360 Spider red | 53 | 1808 |
| 1 | 1937 Lincoln Berline | 28 | 1111 |
| 2 | American Airlines: MD-11S | 28 | 1085 |
| 3 | 1941 Chevrolet Special Deluxe Cabriolet | 28 | 1076 |
| 4 | 1930 Buick Marquette Phaeton | 28 | 1074 |
| ... | ... | ... | ... |
| 104 | 1999 Indy 500 Monte Carlo SS | 25 | 855 |
| 105 | 1911 Ford Town Car | 25 | 832 |
| 106 | 1936 Mercedes Benz 500k Roadster | 25 | 824 |
| 107 | 1970 Chevy Chevelle SS 454 | 25 | 803 |
| 108 | 1957 Ford Thunderbird | 24 | 767 |

 109 rows × 3 columns

##### Step 3

```
q = """  
SELECT productName, COUNT(DISTINCT customerNumber) AS numPurchasers  
FROM products  
JOIN orderdetails  
    USING(productCode)  
JOIN orders  
    USING(orderNumber)  
GROUP BY productName  
ORDER BY numPurchasers DESC  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Data Output: Step 3

|  | productName | numPurchases |
| --- | --- | --- |
| 0 | 1992 Ferrari 360 Spider red | 40 |
| 1 | Boeing X-32A JSF | 27 |
| 2 | 1972 Alfa Romeo GTA | 27 |
| 3 | 1952 Alpine Renault 1300 | 27 |
| 4 | 1934 Ford V8 Coupe | 27 |
| ... | ... | ... |
| 104 | 1958 Chevy Corvette Limited Edition | 19 |
| 105 | 2002 Chevy Corvette | 18 |
| 106 | 1969 Chevrolet Camaro Z28 | 18 |
| 107 | 1952 Citroen-15CV | 18 |
| 108 | 1949 Jaguar XK 120 | 18 |

##### Step 4

```
q = """  
SELECT  
    DISTINCT employeeNumber,  
    officeCode,  
    o.city,  
    firstName,  
    lastName  
FROM employees AS e  
JOIN offices AS o  
    USING(officeCode)  
JOIN customers AS c  
    ON e.employeeNumber = c.salesRepEmployeeNumber  
JOIN orders  
    USING(customerNumber)  
JOIN orderdetails  
    USING(orderNumber)  
WHERE productCode IN (  
    SELECT productCode  
    FROM products  
    JOIN orderdetails  
        USING(productCode)  
    JOIN orders  
        USING(orderNumber)  
    GROUP BY productCode  
    HAVING COUNT(DISTINCT customerNumber) < 20  
)  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Data Output: Step 4

|  | employeeNumber | officeCode | city | firstName | lastName |
| --- | --- | --- | --- | --- | --- |
| 0 | 1370 | 4 | Paris | Gerard | Hernandez |
| 1 | 1501 | 7 | London | Larry | Bott |
| 2 | 1337 | 4 | Paris | Loui | Bondur |
| 3 | 1166 | 1 | San Francisco | Leslie | Thompson |
| 4 | 1286 | 3 | NYC | Foon Yue | Tseng |
| ... |  |  |  | ... | ... |
| 13 | 1188 | 2 | Boston | Julie | Firrelli |
| 14 | 1504 | 7 | London | Barry | Jones |

  

##### Step 5

```
q = """  
SELECT  
    employeeNumber,  
    firstName,  
    lastName,  
    COUNT(customerNumber) AS numCustomers  
FROM employees AS e  
JOIN customers As c  
    ON e.employeeNumber = c.salesRepEmployeeNumber  
GROUP BY employeeNumber  
HAVING AVG(creditLimit) > 15000  
;  
"""  
pd.read_sql(q, conn)
```

**Expected Output:**

Data Output: Step 5

|  | employeeNumber | firstName | lastName | numCustomers |
| --- | --- | --- | --- | --- |
| 0 | 1165 | Leslie | Jennings | 6 |
| 1 | 1166 | Leslie | Thompson | 6 |
| 2 | 1188 | Julie | Firrelli | 6 |
| 3 | 1216 | Steve | Patterson | 6 |
| 4 | 1286 | Foon Yue | Tseng | 7 |
| ... |  |  | ... | ... |
| 13 | 1621 | Mami | Nishi | 5 |
| 14 | 1702 | Martin | Gerard | 6 |

```
# Remember to close the connection when you are done  
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243810

Scraped At: 2026-05-14T21:14:27.017138
