# Summary: SQL JOINs

# Summary: SQL JOINs

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Summary: SQL JOINs

Icon Progress Bar (browser only)

2 min read

Joins in SQL are essential tools for combining data from multiple tables based on a common attribute, such as an ID. The process of using JOIN statements allows you to create a result set that merges columns from these related tables.

### Terms Recap

* **INNER JOIN** returns only the records that have matching values in both tables. It is useful when you want to analyze data that exists in both tables, like retrieving a list of customers who have made at least one order.
* **LEFT JOIN (or LEFT OUTER JOIN)** returns all records from the left table (e.g., Customers) and the matched records from the right table (e.g., Orders). If there is no match, NULL values are returned for columns from the right table. This join is helpful when you want to see all customers, including those who haven't placed any orders.
* **RIGHT JOIN (or RIGHT OUTER JOIN)** is similar to LEFT JOIN, but it returns all records from the right table and matched records from the left table, filling in NULLs where there are no matches. This join is useful when you want to ensure all orders are included, even if they lack corresponding customer data.
* **FULL JOIN (or FULL OUTER JOIN)** returns all records when there is a match in either the left or right table. This join provides a comprehensive view of all data, showing all customers and all orders, even those without corresponding records in the other table.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243757

Scraped At: 2026-05-14T21:12:13.368133
