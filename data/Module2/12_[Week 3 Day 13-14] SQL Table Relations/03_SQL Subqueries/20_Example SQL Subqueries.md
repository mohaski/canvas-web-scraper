# Example: SQL Subqueries

# Example: SQL Subqueries

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Example: SQL Subqueries

Icon Progress Bar (browser only)

2 min read

![Phone, tablet, and desktop computer together displaying a products page for an online shop](https://moringa.instructure.com/courses/1406/files/625344/download)
Jordan is a junior data analyst at an online retailer. They have been tasked with finding out which products have been ordered more than 50 times in total and get the names and prices of all these products. The useful tables are:

* Products: Contains information about each product  
  + Columns: ProductID, ProductName, Price
* OrderDetails: Contains information about the details of each order  
  + Columns: OrderID, ProductID, Quantity

Given these two tables, Jordan realizes that their task is in two parts: they need the total quantity ordered for every product, and they need the details for products that have been ordered more than 50 times from that list. This is an ideal situation for a subquery as building a join to answer this question is likely to make the code less legible.

First, Jordan writes the subquery to find the products that have been ordered more than 50 times. (This is the smaller question.)

```
SELECT ProductID  
FROM OrderDetails  
GROUP BY ProductID  
HAVING SUM(Quantity) > 50
```

Then, Jordan incorporates the subquery into the larger query:

```
SELECT ProductName, Price  
FROM Products  
WHERE ProductID IN (  
    SELECT ProductID  
    FROM OrderDetails  
    GROUP BY ProductID  
    HAVING SUM(Quantity) > 50  
);
```

Finally, Jordan evaluates the results of the whole query and makes sure that they have gotten the names and details for all the products that have sold more than 50 items.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243790

Scraped At: 2026-05-14T21:14:00.131686
