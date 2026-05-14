# Example: Ordering and Limiting Data with SQL

# Example: Ordering and Limiting Data with SQL

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Example: Ordering and Limiting Data with SQL

Icon Progress Bar (browser only)

2 min read

John is a data analyst working for an e-commerce company. His boss wants to know which products are selling the most, so they can focus their marketing efforts on the most popular items.

John needs to find the top 5 best-selling products based on the quantity sold. The company has a large sales database with information on product names, quantities sold, and sale dates.

To find the top 5 best-selling products, he uses the SQL ORDER BY and LIMIT statements to sort and limit the results. He writes the following query:

```
SELECT product_name, SUM(quantity) AS total_quantity  
FROM sales  
WHERE sale_date >= '2023-01-01'  
GROUP BY product_name  
ORDER BY total_quantity DESC  
LIMIT 5;
```

Let’s unpack John’s query:

* SELECT product\_name, SUM(quantity) AS total\_quantity: Selects the product name and calculates the total quantity sold for each product.
* FROM sales: Specifies the sales table as the source of data.
* WHERE sale\_date >= '2023-01-01': Filters the data to include sales from January 1, 2023, onwards.
* GROUP BY product\_name: Groups the results by product name to aggregate the quantities.
* ORDER BY total\_quantity DESC: Sorts the results by total quantity in descending order, so the highest-selling products come first.
* LIMIT 5: Limits the results to the top 5 products.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243713

Scraped At: 2026-05-14T21:09:33.842771
