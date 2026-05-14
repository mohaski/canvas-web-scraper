# Technical Lesson: SQL-Style Syntax with Pandas

# Technical Lesson: SQL-Style Syntax with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Technical Lesson: SQL-Style Syntax with Pandas

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

Data analysis using SQL and Pandas combines the power of relational databases with the flexibility of Python's data manipulation library. SQL (Structured Query Language) excels at querying and managing large datasets stored in databases, while Pandas provides a high-performance, easy-to-use data structure called DataFrame for in-memory analysis. Together, they form a robust toolkit for data professionals.

SQL is used to extract, filter, and aggregate data from databases, making it ideal for initial data preparation and complex queries. Pandas then takes this data and offers a wide range of functions for cleaning, transforming, and analyzing it within Python. This combination allows analysts to leverage SQL's efficiency for data retrieval and Pandas' rich ecosystem for advanced analysis, visualization, and machine learning integration.

We'll start with this familiar ERD, it represents a fictional trading company and contains tables for customers, orders, products, employees, and more. Using this dataset, we can showcase how SQL and Pandas work together for effective data analysis. In this overview we will showcase several different methods for querying a data frame as well as then showcase combining SQL and Pandas to analyze the top 5 products.

Use the `data.sqlite` file with the Python notebook `SQLM4P1.ipynb` in the **[Drive


Links to an external site.](https://drive.google.com/drive/folders/1Cqn0y_c1vhSrxzFoZTGEt3DwM7xwd2dH)**.

[![Entity relationship diagram between eight tables of company data](https://moringa.instructure.com/courses/1406/files/625425/download)](https://moringa.instructure.com/courses/1406/files/625425/download "Entity relationship diagram between eight tables of company data")

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of SQL-Style Syntax with Pandas.

[VIDEO LINK](https://player.vimeo.com/video/1006093154?h=b4225d9dd1)

### Instructions

#### [Step 1: Connecting to the Data](#dpPanel0)

In the cell below, we import sqlite and pandas with the standard alias. Then we create a connection to the database.

```
import sqlite3  
import pandas as pd  
conn = sqlite3.Connection('data.sqlite')
```

#### [Step 2: Creating Dataframe for Comparisons](#dpPanel1)

Here we create a Pandas DataFrame that contains the full products table from our database. We will use this to showcase and compare methods.

### Step 2: Creating dataframe for comparisons

```
products_df = pd.read_sql("""  
                          SELECT *  
                          FROM products  
                          """, conn)  
products_df.head()
```

Dataframe with all products

|  | productCode | productName | productLine | productScale | productVendor | productDescription | quantityInStock | buyPrice | MSRP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | S10\_1678 | 1969 Harley Davidson Ultimate Chopper | Motorcycles | 1:10 | Min Lin Diecast | This replica features working kickstand, front... | 7933 | 48.18 | 95.70 |
| 1 | S10\_1949 | 1952 Alpine Renault 1300 | Classic Cars | 1:10 | Classic Metal Creations | Turnable front wheels; steering function; deta... | 7305 | 98.58 | 214.30 |
| 2 | S10\_2016 | 1996 Moto Guzzi 1100i | Motorcycles | 1:10 | Highway 66 Mini Classics | Official Moto Guzzi logos and insignias, saddl... | 6625 | 68.99 | 118.94 |
| 3 | S10\_4698 | 2003 Harley-Davidson Eagle Drag Bike | Motorcycles | 1:10 | Red Start Diecast | Model features, official Harley Davidson logos... | 5582 | 91.02 | 193.66 |
| 4 | S10\_4757 | 1972 Alfa Romeo GTA | Motorcycles | 1:10 | Motor City Art Classics | Features include: Turnable front wheels; steer... | 3252 | 85.68 | 136.00 |

```
od_df = pd.read_sql("""  
                    SELECT *  
                    FROM orderDetails  
                    """, conn)
```

```
od_df.head()
```

DataFrame with orderDetails

|  | orderNumber | productCode | quantityOrder | priceEach | orderLineNumber |
| --- | --- | --- | --- | --- | --- |
| 0 | 10100 | S18\_1749 | 30 | 136.00 | 3 |
| 1 | 10100 | S18\_2248 | 50 | 55.09 | 2 |
| 2 | 10100 | S18\_4409 | 22 | 75.46 | 4 |
| 3 | 10100 | S24\_3969 | 49 | 35.29 | 1 |
| 4 | 10101 | S18\_2325 | 25 | 108.06 | 4 |

```
# Need to make buyPrice numeric  
products_df['buyPrice'] = products_df['buyPrice'].astype(float)
```

#### [Step 3: Pandas Query Method](#dpPanel2)

Pandas DataFrames come with a built-in query method, which allows you to get information from DataFrames quickly without using the cumbersome slicing syntax. Below we try to subset our data to just products that cost 50$ or more (buyPrice).

See the following examples:

```
# Getting Data using slicing syntax  
foo_df1 = products_df[products_df["buyPrice"] >= 50]
```

```
# Using The query method  
foo_df2 = products_df.query("buyPrice >= 50")
```

```
# These two lines are equivalent!  
print(foo_df1.shape, foo_df2.shape)
```

```
(62, 9) (62, 9)
```

```
foo_df1.head()
```

Slicing Syntax Query with products that cost 50$ or more (buyPrice)

| Index | Product Code | Product Name | Product Line | Product Scale | Product Vendor | Product Description | Quantity In Stock | Buy Price | MSRP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | S10\_4757 | 1972 Alfa Romeo GTA | Classic Cars | 1:10 | Motor City Art Classics | Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 3252 | 85.68 | 136.00 |
| 5 | S10\_4962 | 1962 Lancia Delta 16V | Classic Cars | 1:10 | Second Gear Diecast | Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 6791 | 103.42 | 147.74 |
| 3 | S10\_4698 | 2003 Harley-Davidson Eagle Drag Bike | Motorcycles | 1:10 | Red Start Diecast | Model features, official Harley Davidson logos and insignias, detachable rear wheelie bar, heavy diecast metal with resin parts, authentic multi-color tampo-printed graphics, separate engine drive belts, free-turning front fork, rotating tires and rear racing slick, certificate of authenticity, detailed engine, display stand, precision diecast replica, baked enamel finish, 1:10 scale model, removable fender, seat and tank cover piece for displaying the superior detail of the v-twin engine. | 5582 | 91.02 | 193.66 |
| 2 | S10\_2016 | 1996 Moto Guzzi 1100i | Motorcycles | 1:10 | Highway 66 Mini Classics | Official Moto Guzzi logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail, rotating wheels, working kick stand, diecast metal with plastic parts and baked enamel finish. | 6625 | 68.99 | 118.94 |
| 1 | S10\_1949 | 1952 Alpine Renault 1300 | Classic Cars | 1:10 | Classic Metal Creations | Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 7305 | 98.58 | 214.30 |

```
foo_df2.head()
```

Query method: products that cost 50$ or more (buyPrice)

| Index | Product Code | Product Name | Product Line | Product Scale | Product Vendor | Product Description | Quantity In Stock | Buy Price | MSRP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | S10\_4757 | 1972 Alfa Romeo GTA | Classic Cars | 1:10 | Motor City Art Classics | Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 3252 | 85.68 | 136.00 |
| 5 | S10\_4962 | 1962 Lancia Delta 16V | Classic Cars | 1:10 | Second Gear Diecast | Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 6791 | 103.42 | 147.74 |
| 3 | S10\_4698 | 2003 Harley-Davidson Eagle Drag Bike | Motorcycles | 1:10 | Red Start Diecast | Model features, official Harley Davidson logos and insignias, detachable rear wheelie bar, heavy diecast metal with resin parts, authentic multi-color tampo-printed graphics, separate engine drive belts, free-turning front fork, rotating tires and rear racing slick, certificate of authenticity, detailed engine, display stand, precision diecast replica, baked enamel finish, 1:10 scale model, removable fender, seat and tank cover piece for displaying the superior detail of the v-twin engine. | 5582 | 91.02 | 193.66 |
| 2 | S10\_2016 | 1996 Moto Guzzi 1100i | Motorcycles | 1:10 | Highway 66 Mini Classics | Official Moto Guzzi logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail, rotating wheels, working kick stand, diecast metal with plastic parts and baked enamel finish. | 6625 | 68.99 | 118.94 |
| 1 | S10\_1949 | 1952 Alpine Renault 1300 | Classic Cars | 1:10 | Classic Metal Creations | Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 7305 | 98.58 | 214.30 |

Note that if you want to use and and or statements with the .query() method, you'll need to use "&" and "|" instead because we are within Pandas.

#### [Step 4: Combining Conditionals](#dpPanel3)

Here we showcase how you can combine conditionals in Pandas to get only the classic car products that are 50$ or more.

```
foo_df = products_df.query("buyPrice >=50 & productLine == 'Classic Cars'")  
foo_df.head()
```

Combined conditionals in Pandas: only classic car products $50 or more

| Index | Product Code | Product Name | Product Line | Product Scale | Product Vendor | Product Description | Quantity In Stock | Buy Price | MSRP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | S10\_1949 | 1952 Alpine Renault 1300 | Classic Cars | 1:10 | Classic Metal Creations | Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 7305 | 98.58 | 214.30 |
| 4 | S10\_4757 | 1972 Alfa Romeo GTA | Classic Cars | 1:10 | Motor City Art Classics | Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 3252 | 85.68 | 136.00 |
| 5 | S10\_4962 | 1962 Lancia Delta 16V | Classic Cars | 1:10 | Second Gear Diecast | Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 6791 | 103.42 | 147.74 |
| 6 | S12\_1099 | 1968 Ford Mustang | Classic Cars | 1:12 | Autoart Studio Design | Hood, doors and trunk all open to reveal highly detailed interior features. Steering wheel actually turns the front wheels. Color dark green. | 68 | 95.34 | 194.57 |
| 7 | S12\_1108 | 2001 Ferrari Enzo | Classic Cars | 1:12 | Second Gear Diecast | Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 3619 | 95.59 | 207.80 |

#### [Step 5: Using SQL syntax with pandasql](#dpPanel4)

Since SQL is such a powerful, comfortable tool for Data Scientists, some people had the bright idea of creating a library that lets users query DataFrames using SQL-style syntax. This library is called pandasql.

We can install pandasql using the bash command pip install pandasql. However it has already been pre-provided to you via the learn-env coding environment.

In order to use pandasql, we need to start by importing sqldf pandasql.

Note: You may need to run

```
! pip install pandasql
```

if you don't already have it

```
from pandasql import sqldf
```

Next, it's helpful to write a lambda function that will make it quicker and easier to write queries. Normally, you would have to pass in the global variables every time we use this new object. In order to avoid doing this every time, here's how to write a lambda that does this for you:

```
pysqldf = lambda q: sqldf(q, globals())
```

Now, when you pass a query into pysqldf, the lambda will also pass along the globals, saving you that repetitive task.

#### [Step 6: Writing Queries](#dpPanel5)

To write a query, we just format it as a multi-line string, same as we have been doing previously.

Let's say you are a data analyst working for the Northwind Company on their product marketing team. You have been tasked with analyzing the top 5 products in order to create new customer promotional material highlighting key products for purchase.

We can start with creating a query to give us the top 5 products from our data.

```
# Query for Pandas  
top_5_query_pandas = """  
SELECT productCode, productName, SUM(quantityOrdered) as TotalOrdered  
    FROM products_df  
        JOIN od_df  
            USING(productCode)  
GROUP BY productCode  
ORDER BY TotalOrdered DESC  
Limit 5  
"""
```

```
# Query for SQL  
top_5_query_sql = """  
SELECT productCode, productName, SUM(quantityOrdered) as TotalOrdered  
    FROM products  
        JOIN orderDetails  
            USING(productCode)  
GROUP BY productCode  
ORDER BY TotalOrdered DESC  
Limit 5  
"""
```

#### [Step 7: Create Pandas DataFrame](#dpPanel6)

There are a number of options here in terms of achieving the requested data in a Pandas DataFrame.

We could query the products\_df and od\_df that we created earlier using pandasql.

In order to query DataFrames, we can just pass in the query string we've created to our sqldf object that we stored in pysqldf. This will return a DataFrame.

```
top_5 = pysqldf(top_5_query_pandas)  
top_5.head()
```

DataFrame returned from query string for sqldf object

|  | productCode | productName | totalOrdered |
| --- | --- | --- | --- |
| 0 | S18\_3232 | 1992 Ferrari 360 Spider red | 1808 |
| 1 | S18\_1342 | 1937 Lincoln Berline | 1111 |
| 2 | S700\_4002 | American Airlines: MD-11S | 1085 |
| 3 | S18\_3856 | 1941 Chevrolet Special Deluxe Cabriolet | 1076 |
| 4 | S50\_1341 | 1930 Buick Marquette Phaeton | 1074 |

There is a major downside here however, in that we had to have first queried the entire table for both products and orderDetails thus using more memory than needed by being required to load those into memory first. This is very inefficient and we can do better.

We could of course directly query the SQL database by creating a cursor using the connection and executing then fetching our results. However, this is also inefficient if we want a Pandas DataFrame because we would need to manually give our returned data result to pd.DataFrame().

#### [Step 8: Direct to Pandas](#dpPanel7)

Our best option is to use Pandas to directly read the query into a resulting data frame which we can then use for further analysis.

Note the difference in syntax with our two queries, the only thing that changed was the tables/data frames we are pulling information from.

```
# Use Pandas to read query  
top_5_best = pd.read_sql(top_5_query_sql, conn)  
top_5_best.head()
```

Use of Pandas to directly read the SQL query

|  | productCode | productName | totalOrdered |
| --- | --- | --- | --- |
| 0 | S18\_3232 | 1992 Ferrari 360 Spider red | 1808 |
| 1 | S18\_1342 | 1937 Lincoln Berline | 1111 |
| 2 | S700\_4002 | American Airlines: MD-11S | 1085 |
| 3 | S18\_3856 | 1941 Chevrolet Special Deluxe Cabriolet | 1076 |
| 4 | S50\_1341 | 1930 Buick Marquette Phaeton | 1074 |

```
# Should have same results  
top_5 == top_5_best
```

Use of Pandas to directly read the top\_5\_best.head() query

|  | productCode | productName | totalOrdered |
| --- | --- | --- | --- |
| 0 | True | True | True |
| 1 | True | True | True |
| 2 | True | True | True |
| 3 | True | True | True |
| 4 | True | True | True |

#### [Step 9: Further Analysis with Pandas](#dpPanel8)

Now that we have our top 5 products data in an easy to use format we can dive into performing more analysis on it.

```
# Easy summary statistics  
top_5_best.describe()
```

Summary Statistics on Top 5 Products Data

|  | totalOrdered |
| --- | --- |
| count | 5.000000 |
| mean | 1230.800000 |
| std | 323.001084 |
| min | 1074.000000 |
| 25% | 1076.000000 |
| 50% | 1085.000000 |
| 75% | 1111.000000 |
| max | 1808.000000 |

```
# Calculate the percentage of total sales for each product among the top 5  
total_sales = top_5_best['TotalOrdered'].sum()  
  
# Add as new column  
top_5_best['SalesPercentage'] = top_5_best['TotalOrdered'] / total_sales * 100  
  
top_5_best.head()
```

Percentage of Total Sales of Top 5 Total Sales

|  | productCode | productName | TotalOrdered | SalesPercentage |
| --- | --- | --- | --- | --- |
| 0 | S18\_3232 | 1992 Ferrari 360 Spider red | 1808 | 29.379266 |
| 1 | S18\_1342 | 1937 Lincoln Berline | 1111 | 18.053299 |
| 2 | S700\_4002 | American Airlines: MD-11S | 1085 | 17.630809 |
| 3 | S18\_3856 | 1941 Chevrolet Special Deluxe Cabriolet | 1076 | 17.484563 |
| 4 | S50\_1341 | 1930 Buick Marquette Phaeton | 1074 | 17.452064 |

#### [Step 10: Visualize](#dpPanel9)

Using this approach also allows us to easily visualize results using native Pandas plotting or Seaborn or Matplotlib.

```
import matplotlib.pyplot as plt  
  
# Create Bar chart  
top_5_best.plot(x='productName', y='SalesPercentage', kind='bar')  
plt.title('Sales Percentage of Top 5 Products')  
plt.ylabel('Percentage of Total Sales')  
plt.xlabel('Product Name')  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()
```

[![Bar chart of the sales percentage of the top 5 products](https://moringa.instructure.com/courses/1406/files/625335/download)](https://moringa.instructure.com/courses/1406/files/625335/download "Bar chart of the sales percentage of the top 5 products")

```
# Remember to close the connection when you are done  
conn.close()
```

### Considerations

As data analysts and data scientists, combining the power and functionality of both SQL and Pandas can significantly enhance the efficiency and effectiveness of our work. SQL excels at querying and retrieving large datasets directly from databases, allowing us to filter, aggregate, and join data in a highly efficient, database-optimized manner.

Pandas, on the other hand, offers powerful tools for in-memory data manipulation, enabling us to reshape, clean, and perform detailed analyses on the data once it has been retrieved. By leveraging the strengths of both tools, we can streamline our workflows, reduce the computational load, and achieve more granular or meta-level insights that would be challenging with either tool alone.

However, this combination requires careful consideration of the challenges and trade-offs involved, including performance optimization, data integrity, and managing workflow complexity. By making informed choices, you can harness the full potential of SQL and Pandas to achieve superior analytical outcomes.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243833

Scraped At: 2026-05-14T21:15:53.916245
