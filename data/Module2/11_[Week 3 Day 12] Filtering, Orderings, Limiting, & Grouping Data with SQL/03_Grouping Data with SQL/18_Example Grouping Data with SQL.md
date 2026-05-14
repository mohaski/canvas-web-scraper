# Example: Grouping Data with SQL

# Example: Grouping Data with SQL

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Example: Grouping Data with SQL

Icon Progress Bar (browser only)

1 min read

![](https://moringa.instructure.com/courses/1406/files/625325/download)
Samantha is a data analyst at a coffee shop chain. Her manager wants to understand which locations have customers who spend the most on average per visit.

Samantha needs to find the average spend per visit for each location and identify locations where the average spend is greater than $10. The sales database contains information on the location, total bill amount, and the date of each sale.

To accomplish this, Samantha uses the SQL GROUP BY and HAVING statements and writes the following query:

```
SELECT location, AVG(total_bill) AS average_spend  
FROM sales  
GROUP BY location  
HAVING AVG(total_bill) > 10;
```

Let’s unpack Samantha’s query:

* SELECT location, AVG(total\_bill) AS average\_spend: Selects the location and calculates the average total bill for each location.
* FROM sales: Specifies the sales table as the source of data.
* GROUP BY location: Groups the results by location to calculate the average spend per location.
* HAVING AVG(total\_bill) > 10: Filters the results to include only those locations where the average total bill is greater than $10.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243727

Scraped At: 2026-05-14T21:10:17.461174
