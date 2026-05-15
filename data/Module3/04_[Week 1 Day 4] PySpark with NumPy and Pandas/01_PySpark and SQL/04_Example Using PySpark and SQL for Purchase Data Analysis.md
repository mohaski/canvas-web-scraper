# Example: Using PySpark and SQL for Purchase Data Analysis

# Example: Using PySpark and SQL for Purchase Data Analysis

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Example: Using PySpark and SQL for Purchase Data Analysis

Icon Progress Bar (browser only)

3 min read

A junior data scientist working for a retail company is tasked with analyzing customer purchase data to identify sales trends and customer behaviors. The data is stored in distributed files (CSV format), and the company uses PySpark for scalable data processing. The data needs cleaning, transformation, and aggregation to generate a sales summary report using both PySpark DataFrame operations and SQL queries. Let's look at how this is done:

* [Loading the Data](#dpPanel0Content)
* [Checking Data Types and Schema](#dpPanel1Content)
* [Data Cleaning with PySpark DataFrame Operations](#dpPanel2Content)
* [Registering the DataFrame as a Temporary SQL Table](#dpPanel3Content)
* [Using SQL Queries for Aggregation](#dpPanel4Content)
* [Visualizing the Results](#dpPanel5Content)

### Loading the Data

First, load the sales data stored in a CSV file into a PySpark DataFrame.

```
from pyspark.sql import SparkSession  
  
# Initialize a SparkSession  
spark = SparkSession.builder.appName("Retail Sales Analysis").getOrCreate()  
  
# Load the sales data into a DataFrame  
sales_df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)  
  
# Display the first few records  
sales_df.show(5)
```

### Checking Data Types and Schema

To understand the structure of the data, inspect its schema.

```
# Print schema of the DataFrame  
sales_df.printSchema()
```

### Data Cleaning with PySpark DataFrame Operations

Some rows contain null values in important columns, such as product\_id and sales\_amount.

Filter out these rows:

```
# Filter out rows with null values in critical columns  
cleaned_df = sales_df.filter(sales_df["product_id"].isNotNull() & sales_df["sales_amount"].isNotNull())
```

### Registering the DataFrame as a Temporary SQL Table

Register the cleaned DataFrame as a temporary SQL table to use SQL queries for exploring and analyzing the data.

```
# Register the DataFrame as a temporary view  
cleaned_df.createOrReplaceTempView("sales_table")
```

### Using SQL Queries for Aggregation

The manager requests a report on total sales revenue per product category. Use an SQL query to aggregate the data.

```
# Use SQL to calculate total sales revenue per product category  
sales_summary = spark.sql("""  
    SELECT category, SUM(sales_amount) AS total_revenue  
    FROM sales_table  
    GROUP BY category  
    ORDER BY total_revenue DESC  
""")  
# Display the results  
sales_summary.show()
```

### Visualizing the Results

Collect the results for visualization to better communicate insights.

```
# Collect data for visualization  
categories = sales_summary.select("category").rdd.flatMap(lambda x: x).collect()  
revenues = sales_summary.select("total_revenue").rdd.flatMap(lambda x: x).collect()  
  
import matplotlib.pyplot as plt  
  
# Plot the total revenue per category  
plt.figure(figsize=(10, 6))  
plt.bar(categories, revenues, color='skyblue')  
plt.xlabel("Product Category")  
plt.ylabel("Total Revenue")  
plt.title("Total Sales Revenue by Product Category")  
plt.xticks(rotation=45)  
plt.show()
```

In the workplace, it is common to encounter scenarios where you need to analyze large datasets stored across distributed environments. Using PySpark and SQL together allows you to perform data cleaning, transformations, and aggregations on big data while maintaining the flexibility to use SQL for more complex queries. This skillset is highly valued in roles where data size and performance are important considerations.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248313

Scraped At: 2026-05-15T09:56:22.493662
