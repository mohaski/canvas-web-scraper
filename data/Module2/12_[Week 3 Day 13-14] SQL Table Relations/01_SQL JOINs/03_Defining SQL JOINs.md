# Defining SQL JOINs

# Defining SQL JOINs

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) What are SQL JOINs?

Icon Progress Bar (browser only)

5 min read

Joins are the primary mechanism for combining data from multiple tables. In order to do this, you define the common attribute(s) between tables in order for them to be combined.

The basic idea is:

* You have two or more tables with related data.
* These tables share a common column (like an ID).
* You use JOIN to create a result set that combines columns from these tables.

SQL recognizes many different kinds of JOIN, but a handful show up again and again in queries:

* **INNER JOIN:** Returns only the rows where there is a match in both tables. When you use an INNER JOIN, SQL compares the values in the specified columns from both tables, and only the rows with matching values in both tables are included in the result set. If no match is found, the rows are excluded. Use when you need only matching rows from both tables.
* **LEFT JOIN (or LEFT OUTER JOIN):** Returns all rows from the left table and the matched rows from the right table. If there is no match, the result will contain NULL values for columns from the right table. This allows you to see all the data from the left table, even if there are no corresponding rows in the right table. Use when you need all rows from the left table and matching rows from the right table.
* **Right JOIN (or RIGHT OUTER JOIN):** Returns all rows from the right table and the matched rows from the left table. If there is no match, NULL values will be returned for columns from the left table. This join is useful when you want to retain all records from the right table. Use when you need all rows from the right table and matching rows from the left table.
* **FULL JOIN (or FULL OUTER JOIN):** Returns all rows when there is a match in either the left or right table. If there is a match, the data from both tables will be displayed. If there is no match, the result will include NULL values for the columns from the table without the match. This type of join combines the results of both LEFT JOIN and RIGHT JOIN. Use when you need all rows from both tables, with or without matches.

### How Do SQL JOINs Work?

Imagine you have a "Customers" table and an "Orders" table. Each order is associated with a customer ID. A JOIN could let you create a result set showing customer names alongside their orders. Which would look like this in SQL pseudo-code:

```
SELECT Customers.Name, Orders.OrderID  
FROM Customers  
JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
```

This query combines data from the Customers and Orders tables, matching rows where the CustomerID is the same in both tables.

There are several types of JOINs (INNER, LEFT, RIGHT, FULL), each with different behaviors for handling matches and mismatches between tables that we’ll learn.

While working as a data scientist for a model toy company with tables in the database named `customers` and `orders`, understanding how to use different types of SQL joins is essential. Here's why you would need to use each type of join:

1. INNER JOIN
   * Use Case: You want to find data that exists in both the `customers` and `orders` tables.
   * Example: If you need to analyze the purchasing behavior of customers, you would use an `INNER JOIN` to retrieve a list of all customers who have made at least one order. This join would only return customers who have placed orders, excluding those who haven't.
2. LEFT JOIN (or LEFT OUTER JOIN)
   * Use Case: You want to find all customers, including those who may not have made an order.
   * Example: If you need to understand the full customer base and see which customers have never placed an order, you would use a `LEFT JOIN` from `customers` to `orders`. This would return all customers, with `NULL` values for customers who have not placed any orders.
3. \*\*RIGHT JOIN (or RIGHT OUTER JOIN)\*\*
   * Use Case: You want to focus on orders, ensuring that all orders are included, even if some do not have corresponding customer information.
   * Example: If there's a situation where you need to audit orders and check for any that might not have complete customer data (perhaps due to data entry errors), a `RIGHT JOIN` from `orders` to `customers` would be useful. This join returns all orders, with `NULL` values for orders that do not have a corresponding customer record.
4. \*\*FULL JOIN (or FULL OUTER JOIN)\*\*
   * Use Case: You want to combine both tables to see all customers and all orders, regardless of whether they have corresponding records in the other table.
   * Example: If you need a comprehensive view of all data, including all customers and all orders, regardless of whether a match exists between them, a `FULL JOIN` would be appropriate. This join would include all customers and orders, showing `NULL` where there are no corresponding records in the other table.

#### Summary

* INNER JOIN: Customers with orders.
* LEFT JOIN: All customers, including those without orders.
* RIGHT JOIN: All orders, including those without customer information.
* FULL JOIN: All customers and all orders, including those without corresponding records.

Each type of join helps you answer different business questions and understand the relationship between your customers and their orders.

### Conceptualize Filtering Data with SQL

[![SQL JOINs venn diagrams for seven common join statements](https://moringa.instructure.com/courses/1406/files/625316/download)](https://moringa.instructure.com/courses/1406/files/625316/download "SQL JOINs venn diagrams for seven common join statements")

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243751

Scraped At: 2026-05-14T21:11:50.259822
