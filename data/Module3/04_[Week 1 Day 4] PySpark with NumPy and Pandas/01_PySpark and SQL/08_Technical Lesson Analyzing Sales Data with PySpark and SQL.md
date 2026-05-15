# Technical Lesson: Analyzing Sales Data with PySpark and SQL

# Technical Lesson: Analyzing Sales Data with PySpark and SQL

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: Analyzing Sales Data with PySpark and SQL

* [Page: Introduction: PySpark with NumPy, Pandas, & SQL (1 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248305 "Page: Introduction: PySpark with NumPy, Pandas, & SQL (1 of 18)")
* [Page: Introduction to PySpark and SQL (2 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248309 "Page: Introduction to PySpark and SQL (2 of 18)")
* [Page: What is PySpark and SQL Integration? (3 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248311 "Page: What is PySpark and SQL Integration?  (3 of 18)")
* [Page: Example: Using PySpark and SQL for Purchase Data Analysis (4 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248313 "Page: Example: Using PySpark and SQL for Purchase Data Analysis (4 of 18)")
* [Page: Process: Integrating PySpark and SQL (5 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248315 "Page: Process: Integrating PySpark and SQL (5 of 18)")
* [Page: Summary: PySpark and SQL (6 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248317 "Page: Summary: PySpark and SQL (6 of 18)")
* [Page: Check for Understanding: PySpark and SQL (7 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248319 "Page: Check for Understanding: PySpark and SQL (7 of 18)")
* [Page: Current: Technical Lesson: Analyzing Sales Data with PySpark and SQL (8 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248321 "Page: Current: Technical Lesson: Analyzing Sales Data with PySpark and SQL (8 of 18)")
* [Page: Introduction to PySpark, Pandas, and SQL (9 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248325 "Page: Introduction to PySpark, Pandas, and SQL (9 of 18)")
* [Page: Defining PySpark, Pandas, & SQL (10 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248327 "Page: Defining PySpark, Pandas, & SQL (10 of 18)")
* [Page: Example: PySpark, Pandas, and SQL Integration (11 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248329 "Page: Example: PySpark, Pandas, and SQL Integration (11 of 18)")
* [Page: Process: Integrating PySpark, Pandas, and SQL (12 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248331 "Page: Process: Integrating PySpark, Pandas, and SQL (12 of 18)")
* [Page: Summary: PySpark, Pandas, and SQL (13 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248333 "Page: Summary: PySpark, Pandas, and SQL (13 of 18)")
* [Page: Check for Understanding: PySpark, Pandas, and SQL (14 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248335 "Page: Check for Understanding: PySpark, Pandas, and SQL (14 of 18)")
* [Page: Technical Lesson: Integrating PySpark, Pandas, and SQL (15 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248337 "Page: Technical Lesson: Integrating PySpark, Pandas, and SQL (15 of 18)")
* [Page: Practice: Integrating PySpark, Pandas and SQL (16 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248339 "Page: Practice: Integrating PySpark, Pandas and SQL (16 of 18)")
* [Lab: PySpark with NumPy and Pandas (17 of 18), Assignment](https://moringa.instructure.com/courses/1426/modules/items/248343 "Lab: PySpark with NumPy and Pandas (17 of 18), Assignment")
* [Quiz: PySpark, Pandas, and SQL (18 of 18)](https://moringa.instructure.com/courses/1426/modules/items/248345 "Quiz: PySpark, Pandas, and SQL (18 of 18)")

*​*

**Estimated Completion Time:** 1 hour

This technical lesson provides a complete worked example on how to analyze sales data by integrating PySpark and SQL. It focuses on applying a structured, problem-solving approach to process and extract actionable insights from raw data. The lesson is designed to guide you step-by-step, addressing common challenges such as handling diverse data formats, cleaning datasets, and performing aggregations using SQL queries within PySpark.

By following this process, you'll gain practical experience in:

* **Data Ingestion:** Loading and structuring raw data into a PySpark DataFrame.
* **Data Inspection:** Exploring and understanding the data's structure and data types.
* **Data Cleaning:** Applying logical filters to remove invalid or null entries from critical columns.
* **SQL Integration:** Registering the DataFrame as a temporary SQL table to leverage SQL for complex queries and transformations.
* **Data Aggregation:** Generating meaningful statistics such as total sales revenue per product through SQL queries.
* **Data Visualization:** (Optional) Using Python’s matplotlib to visualize the results for better communication of insights.

Each step clarifies key actions to overcome specific challenges in the analysis process, ensuring you build confidence in handling real-world datasets. This lesson equips you with a robust workflow that combines the power of PySpark's distributed computing with SQL's intuitive querying capabilities, offering scalability and ease of implementation.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of PySpark and SQL.

[VIDEO LINK](https://player.vimeo.com/video/1058081138?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

* [Step 1. Load Data into PySpark DataFrame](#dpPanel0Content)
* [Step 2. Inspect Data Types and Structure](#dpPanel1Content)
* [Step 3. Clean the Data by Filtering Out Null Values](#dpPanel2Content)
* [Step 4. Register the Cleaned DataFrame as a Temporary SQL Table](#dpPanel3Content)
* [Step 5. Use SQL Queries to Perform Data Aggregation](#dpPanel4Content)
* [Step 6. Visualize the Results Using Python's Matplotlib](#dpPanel5Content)

### Step 1. Load Data into PySpark DataFrame

```
# initialize a SparkSession  
from pyspark.sql import SparkSession  
spark = SparkSession.builder.appName("Sales Data Analysis").getOrCreate()  
  
# Load the sales data into a PySpark DataFrame  
sales_df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)
```

**Decision Point:** If the data is stored in another format (e.g., JSON, Parquet), modify the .read method accordingly.

### Step 2. Inspect Data Types and Structure

```
# Display the first few records and the schema  
sales_df.show(5)  
sales_df.printSchema()
```

**Output:**

```
|customer_id|customer_name|
     
   customer_email|product_id|
   
  product_name|product_price|sale_id|quantity|
  sale_date|  
+-----------+-------------+--------------------+----------+---------------+-------------+-------+--------+----------+  
|
        1001|   John
  Smith|john.smith@email.com|  
     1234|T-Shirt (Large)|
         19.99|
   98765|      
  2|2024-05-14|  
|    
    1002|     Jane Doe|
   jane.doe@email.com|  
     4567|    
      Laptop|    
    899.99|  12345|  
      1|2024-05-13|  
|
        1003|
   Michael
  Lee|michael.lee@email...|  
     7890|    
  Coffee Mug|      
    7.99|  54321|  
      3|2024-05-12|  
|
        1004|  Alice
  Jones|alice.jones@email...|  
     9871|    
  Headphones|      
   49.99|  78901|  
      2|2024-05-11|  
|
        1005|  
   David Lee| david.lee@email.com|
       2345|  
         Mouse|
         14.99|
   34567|      
  1|2024-05-10|  
+-----------+-------------+--------------------+----------+---------------+-------------+-------+--------+----------+  
only
  showing top 5 rows  

    
root  
 |-- customer_id:
  integer (nullable = true)  
 |--
  customer_name: string (nullable =
  true)  
 |-- customer_email:
  string (nullable = true)  
 |--
  product_id: integer (nullable =
  true)  
 |-- product_name:
  string (nullable = true)  
 |--
  product_price: double (nullable =
  true)  
 |-- sale_id: integer
  (nullable = true)  
 |--
  quantity: integer (nullable =
  true)  
 |-- sale_date: date
  (nullable = true)>
```

### Step 3. Clean the Data by Filtering Out Null Values

```
# Filter rows with null values in critical columns  
  
cleaned_df = sales_df.filter(sales_df["customer_id"].isNotNull() & sales_df["product_id"].isNotNull())
```

If other columns require filtering based on business logic (e.g., non-negative prices or quantities), include additional conditions.

### Step 4. Register the Cleaned DataFrame as a Temporary SQL Table

```
# Create a temporary SQL table for the DataFrame  
  
cleaned_df.createOrReplaceTempView("sales_table")
```

If the DataFrame changes later (e.g., further cleaned or transformed), re-register the DataFrame using `createOrReplaceTempView` again.

### Step 5. Use SQL Queries to Perform Data Aggregation

```
# Run an SQL query to calculate total sales revenue per product  
  
sales_summary = spark.sql("""  
    SELECT product_name, SUM(product_price * quantity) AS total_revenue  
    FROM sales_table  
    GROUP BY product_name  
    ORDER BY total_revenue DESC  
""")  
  
# Display the result  
sales_summary.show()
```

**Output:**

```
+-------------------+------------------+  
|       product_name|     total_revenue|  
+-------------------+------------------+  
|             Laptop|            899.99|  
|        Camera Lens|            899.97|  
|             Tablet|            749.97|  
|          Projector|            699.98|  
|              Watch|            599.97|  
|         Smartwatch|            399.98|  
|       Air Purifier|            389.97|  
|     Gaming Headset|299.96999999999997|  
|Wireless Headphones|            299.96|  
|           Backpack|            249.95|  
|       Gaming Mouse|            149.97|  
|     Protein Powder|            124.75|  
|    Fitness Tracker|            119.97|  
|           Yoga Mat|            104.97|  
|         Headphones|             99.98|  
|          Desk Lamp|             99.96|  
|   Portable Charger| 99.94999999999999|  
|   Wireless Speaker|             79.99|  
|         Travel Mug|             77.94|  
|            Journal|             69.93|  
+-------------------+------------------+  
only showing top 20 rows
```

Modify the SQL query as needed to perform additional transformations, filters, or aggregations based on business requirements.

### Step 6. Visualize the Results Using Python's Matplotlib

```
# Select top 10 products by total revenue  
top_10_summary = sales_summary.limit(10)  
  
# Collect data for visualization  
  
products = top_10_summary.select("product_name").rdd.flatMap(lambda x: x).collect()  
revenues = top_10_summary.select("total_revenue").rdd.flatMap(lambda x: x).collect()  
  
# Generate a bar chart to visualize total revenue by product, for top 10 sales  
import matplotlib.pyplot as plt  
plt.figure(figsize=(12, 6))  
plt.bar(products, revenues, color='lightblue')  
plt.xlabel("Product Name")  
plt.ylabel("Total Revenue")  
plt.title("Total Sales Revenue by Product")  
plt.xticks(rotation=45)  
plt.show()
```

**Output:**

[![Bar chart of total sales revenue by prduct.](https://moringa.instructure.com/courses/1426/files/631436/download)](https://moringa.instructure.com/courses/1426/files/631436/download "Bar chart of total sales revenue by prduct.")

If a different visualization is desired, use a suitable plot type (e.g., line chart, scatter plot) to better illustrate insights.

### Common Issues and Challenges

#### **Data Management and Preparation**

* [Challenges](#dpPanel6Content)
* [Solutions](#dpPanel7Content)

### Challenges

* Schema inference (inferSchema=True) may misidentify data types in complex datasets.
* Null or missing values can disrupt analysis and lead to errors.

### Solutions

* Explicitly define schemas with StructType and StructField for accuracy.
* Use .filter(), .fillna(), or .dropna() to clean data carefully, balancing quality and dataset size.

#### **Performance Optimization and Transformation Approaches**

* [Challenges](#dpPanel8Content)
* [Solutions](#dpPanel9Content)

### Challenges

* Large datasets can cause slow transformations and queries if not optimized.
* Choosing between DataFrame API and SQL can impact code readability, performance, and flexibility.

### Solutions

* Cache reusable DataFrames, filter data early, and limit data for visualization to improve efficiency.
* Use SQL for complex joins and aggregations, and the DataFrame API for iterative, Pythonic operations. Combining these approaches strategically ensures both flexibility and scalability.

#### **Data Aggregation, Grouping, and Visualization**

* [Challenges](#dpPanel10Content)
* [Solutions](#dpPanel11Content)

### Challenges

* Grouping choices affect the granularity and interpretability of results.
* Visualizing large datasets can strain memory and lose detail when reducing the dataset.

### Solutions

* Group by relevant fields (e.g., product\_name) for actionable insights, avoiding overly granular or broad groupings.
* Reduce data to manageable subsets using .limit() for efficient visualizations, balancing interpretability with dataset representation.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248321

Scraped At: 2026-05-15T09:57:16.686430
