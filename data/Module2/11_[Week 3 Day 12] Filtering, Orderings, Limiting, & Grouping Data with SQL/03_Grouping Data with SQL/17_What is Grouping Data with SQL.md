# What is Grouping Data with SQL?

# What is Grouping Data with SQL?

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) What is Grouping Data with SQL?

Icon Progress Bar (browser only)

3 min read

Sometimes you may wish to find the mean, median, minimum, or maximum of a column feature. For example, there could be a customer relational database that you've been working with and you may wonder if there are differences in overall sales across offices or regions. We can use aggregate functions in SQL to assist with performing these analyses.

### How Does Grouping Data with SQL Work?

SQL grouping with HAVING works as follows:

1. The GROUP BY clause is used to group rows that have the same values in specified columns.
2. After grouping, aggregate functions (like AVG, COUNT, MAX, MIN, SUM) can be applied to each group.
3. The HAVING clause is then used to filter these groups based on the results of aggregate functions.

In the context of your prompt about customer sales across offices or regions, you might use GROUP BY to group sales data by office or region. Then, you could apply aggregate functions to calculate total sales, average sales, or other metrics for each group. Finally, the HAVING clause would allow you to filter these groups based on the aggregated results.

For example, you could:

1. Group sales by region
2. Calculate the total sales for each region
3. Use HAVING to filter out regions with total sales below a certain threshold

This process allows you to answer questions like "Which regions have total sales over $1 million?" or "Which offices have an average sale value higher than the company average?"

The key difference between WHERE and HAVING is that WHERE filters individual rows before grouping, while HAVING filters groups after the GROUP BY has been applied. This makes HAVING particularly useful for conditions involving aggregate functions, which can't be used with WHERE.

### Conceptualization: Grouping Data with SQL

Grouping Data with SQL: concepts described with examples

| Concept | Description | Example |
| --- | --- | --- |
| **GROUP BY Clause** | The GROUP BY clause is used to group rows that have the same values in specified columns. | Grouping sales data by salesperson to analyze total sales per person. |
| **Aggregate Functions** | After grouping, aggregate functions (like AVG, COUNT, MAX, MIN, SUM) can be applied to each group to calculate summary statistics. | Calculating the total (SUM), average (AVG), or maximum (MAX) sales for each salesperson. |
| **HAVING Clause** | The HAVING clause is used to filter these groups based on the results of aggregate functions. It is applied after the groups have been formed and aggregated. | Filtering out salespersons whose total sales (SUM) are below a certain threshold. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243725

Scraped At: 2026-05-14T21:10:12.319551
