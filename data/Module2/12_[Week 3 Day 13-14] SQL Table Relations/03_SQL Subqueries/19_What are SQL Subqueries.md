# What are SQL Subqueries?

# What are SQL Subqueries?

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) What are SQL Subqueries?

Icon Progress Bar (browser only)

2 min read

SQL queries can get complex, especially as the number of tables increases. A subquery, also called a nested query, enables us to decompose a complicated query into smaller parts.

* **Query:** the code written in SQL to extract data from a database
* **Subquery:** a query inside another query
* **Main query:** the query that contains a subquery
* **Nested query:** another term for subquery
* **Inner query:** another term for subquery
* **Outer query:** another term for main query

### How Do SQL Subqueries Work?

Subqueries, in some ways, reverse the normal order of human thinking. We typically start from the big and refine our way down to the small. With subqueries, we are asking a smaller question and using that smaller question to refine the bigger question–the main query.

Let’s say that we want to find the names of customers who have spent more than $1000 with our company for a special loyalty reward. Given a pair of tables:

* Customers: Contains customer information.  
  + Columns: CustomerID, CustomerName
* Orders: Contains order information.  
  + Columns: OrderID, CustomerID, TotalAmount

We first write the subquery to find customers that have spent more than $1000:

```
SELECT CustomerID  
FROM Orders  
GROUP BY CustomerID  
HAVING SUM(TotalAmount) > 1000
```

We then wrap that query up inside of the main query:

```
SELECT CustomerName  
FROM Customers  
WHERE CustomerID IN (  
    SELECT CustomerID  
    FROM Orders  
    GROUP BY CustomerID  
    HAVING SUM(TotalAmount) > 1000  
);
```

### Conceptualization: SQL Subqueries

Terms with SQL Queries: Defined with Examples

| Term | Definition | SQLite in Python Pseudocode |
| --- | --- | --- |
| Query | The code written in SQL to extract data from a database. | ``` # Example of a basic query  SELECT * FROM Customers WHERE Country = 'USA'; ``` |
| Subquery | A query inside another query. | ``` # Example of a subquery  SELECT ProductName FROM Products WHERE ProductID IN (SELECT ProductID FROM OrderDetails WHERE OrderID = 10248); ``` |
| Main Query | The query that contains a subquery. | ``` # Example of a main query with a subquery  SELECT ProductName FROM Products WHERE ProductID IN (SELECT ProductID FROM OrderDetails WHERE OrderID = 10248); ``` |
| Nested Query | Another term for subquery. | ``` # Example of a nested query  SELECT CustomerID FROM Orders WHERE CustomerID = (SELECT CustomerID FROM Customers WHERE Country = 'USA') ``` |
| Inner Query | Another term for subquery. | ``` #Example of an inner query  SELECT * FROM Employees WHERE EmployeeID IN (SELECT ManagerID FROM Departments) ``` |
| Outer Query | Another term for main query. | ``` # Example of an outer query with a subquery  SELECT Name FROM Customers WHERE CustomerID = (SELECT CustomerID FROM Orders WHERE OrderID = 10248); ``` |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243788

Scraped At: 2026-05-14T21:13:54.869126
