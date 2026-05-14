# What is Filtering Data with SQL?

# What is Filtering Data with SQL?

## ![20240930\_205312preview](https://moringa.instructure.com/courses/1406/files/625387/preview) What is Filtering Data with SQL?

Icon Progress Bar (browser only)

3 min read

**Filtering** is the process of assessing a group of items to eliminate unwanted ones. In SQL, it is how we ensure that our queries only return the data that we want. We perform this filtering *in the query itself*, rather than after we have gotten all the data, to save processing and compute time.

### How Does Filtering Data with SQL Work?

We are already familiar with the SELECT and FROM statements in SQL. These find specific columns (SELECT) on specific tables (FROM). But we generally don’t want all of the data from those tables. The **WHERE statement** enables us to set conditions on the data being returned. This means that we can have SQL parse and analyze (in a primitive way) the data for us and ensure that we only get the records we actually want to use.

### Example: Filtering Data with SQL

Emily is a data analyst working for a retail company that sells various products online. She has been tasked with analyzing sales data to identify trends and make data-driven recommendations to increase revenue.

The company has a large database containing detailed records of every sale made over the past ten years. This data includes information on the product name, category, sale date, price, quantity sold, customer region, and more. Emily's manager has asked her to generate a report showing the total sales for high-value electronics (items priced over $500) sold in the last quarter (Q4).

To accomplish this, Emily needs to filter the database to include only the relevant records. She uses the SQL WHERE statement to do this.

```
SELECT product_name, SUM(price * quantity) AS total_sales  
FROM sales  
WHERE category = 'Electronics'  
AND price > 500  
AND sale_date BETWEEN '2023-10-01' AND '2023-12-31'  
GROUP BY product_name;
```

We already know SELECT and FROM. WHERE (and to a lesser extent GROUP BY) is what we are interested in here. Let’s break down that query:

* category = 'Electronics': This ensures only electronic items are considered.
* price > 500: This filters for high-value items priced over $500.
* sale\_date BETWEEN '2023-10-01' AND '2023-12-31': This limits the data to sales made in Q4.
* SUM(price \* quantity) AS total\_sales: This calculates the total sales value for each product, and aliases the results for human readability.
* GROUP BY product\_name: This groups the results by product name to summarize total sales per product.

By using this query, Emily can generate a concise report highlighting the high-value electronics sold in the last quarter of 2023, providing valuable insights for her company to make informed business decisions.

### Conceptualize Filtering Data with SQL

[![Stepped diagram of how filtering data with SQL works using Where and select statements](https://moringa.instructure.com/courses/1406/files/625427/download)](https://moringa.instructure.com/courses/1406/files/625427/download "A simple filter implemented using the WHERE statement. The data being queried is on the left; the results of the query are on the right.")


A simple filter implemented using the WHERE statement. The data being queried is on the left; the results of the query are on the right.

*IMG SOURCE: [Software Carpentry github 


Links to an external site.](https://ucsbcarpentry.github.io/2021-11-04-ucsb-sql-online/06-filter/) copyright © Software Carpentry*

### Process of Filtering using SQL WHERE Statements

Going back to the example above, how did Emily write the query? Here's the process:

1. Emily identified the specific data she needed and the tables she needed it from. This came from her manager’s requirements. She needed:  
   1. “high-value sales” (>$500)
   2. in Electronics
   3. made in the last quarter of 2023
2. She selects product\_name and SUMs price\*quantity in the SELECT statement
3. She selects these FROM the sales table
4. Using a WHERE statement and several additional conditions (the ANDs), she   
   1. Filters all products down to just Electronics,
   2. Filters all the Electronics sales down to those greater than $500, and
   3. Limits her results to just the last three months of 2023

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243703

Scraped At: 2026-05-14T21:08:42.452168
