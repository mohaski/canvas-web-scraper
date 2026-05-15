# Technical Lesson: Integrating PySpark, Pandas, and SQL

# Technical Lesson: Integrating PySpark, Pandas, and SQL

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: Integrating PySpark, Pandas, and SQL

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In this lesson, we'll explore how to integrate PySpark, Pandas, and SQL for a common data science task. Imagine you are working with a sales dataset that is too big to be processed by Pandas alone due to memory constraints. We'll solve this problem by using PySpark for distributed data processing, leveraging SQL for querying, and integrating Pandas for exploratory analysis on sampled data.

We'll walk through a workflow that allows us to:

1. Load a sales dataset with PySpark.
2. Perform data transformations and filtering using SQL queries within PySpark.
3. Convert the Spark DataFrame to a Pandas DataFrame for detailed exploration and visualization.

**Key Challenge:** Handle large-scale data processing while retaining the flexibility of familiar Pandas operations, and SQL helps bridge the gap between data extraction and transformation.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of PySpark, Pandas, and SQL.

[VIDEO LINK](https://player.vimeo.com/video/1058080500?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

* [Step 1. Set Up the Environment](#dpPanel0Content)
* [Step 2. Load Data into PySpark](#dpPanel1Content)
* [Step 3. Perform SQL Operations with PySpark](#dpPanel2Content)
* [Step 4. Convert Spark DataFrame to Pandas DataFrame](#dpPanel3Content)
* [Step 5. Perform Exploratory Data Analysis with Pandas](#dpPanel4Content)

### Step 1. Set Up the Environment

* Import the required libraries. Import PySpark, Pandas, and other module.
* Create a SparkSession. The SparkSession is the entry point for working with PySpark:

```
from pyspark.sql import SparkSession  
import pandas as pd  
  
spark = SparkSession.builder.appName("PySpark_Pandas_SQL_Integration").getOrCreate()
```

### Step 2. Load Data into PySpark

* Load the sales dataset using PySpark. For this example, we'll use a CSV file named sales\_data.csv:

```
# Note: Replace "sales_data.csv" with the path to your dataset.  
  
df_spark = spark.read.csv("sales_data.csv", header=True, inferSchema=True)
```

### Step 3. Perform SQL Operations with PySpark

* Create a temporary view for SQL queries. This allows you to use SQL on the PySpark DataFrame:  

  ```
  df_spark.createOrReplaceTempView("sales_data")
  ```
* Write an SQL query to filter data. Use SQL to perform transformations or filtering. For example, filter sales greater than $100:  

  ```
  filtered_df = spark.sql("SELECT *   
           FROM sales_data  
           WHERE product_price > 100")
  ```
* **Decision Point:** You can modify the condition (product\_price > 100) to suit the specific filtering criteria for your dataset.

### Step 4. Convert Spark DataFrame to Pandas DataFrame

* Convert the filtered Spark DataFrame to a Pandas DataFrame for detailed analysis:

```
df_pandas = filtered_df.limit(1000).toPandas()
```

### Step 5. Perform Exploratory Data Analysis with Pandas

* Use Pandas to explore the data. Perform summary statistics and visualizations:

```
# Summary statistics  
print(df_pandas.describe())  
  
# Example visualization  
import matplotlib.pyplot as plt  
df_pandas['product_price'].hist()  
plt.xlabel('Product Price')  
plt.ylabel('Frequency')  
plt.title('Histogram of Product Price')  
plt.show()
```

**Output:**

```
 customer_id   product_id  product_price       sale_id   quantity  
count    12.000000    12.000000      12.000000     12.000000  12.000000  
mean   1026.333333  5197.500000     296.656667  44653.166667   1.416667  
std      14.797625  2594.892273     203.975637  22657.747841   0.514929  
min    1002.000000  1789.000000     129.990000  12345.000000   1.000000  
25%    1015.750000  2310.000000     199.990000  34619.500000   1.000000  
50%    1026.000000  5672.000000     249.990000  45499.500000   1.000000  
75%    1038.250000  7062.500000     312.490000  48687.500000   2.000000  
max    1047.000000  8901.000000     899.990000  89012.000000   2.000000
```

[![Histogram of product price](https://moringa.instructure.com/courses/1426/files/631525/download)](https://moringa.instructure.com/courses/1426/files/631525/download "Histogram of product price")

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248337

Scraped At: 2026-05-15T09:58:01.510311
