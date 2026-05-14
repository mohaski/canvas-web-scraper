# Practice: SQL-Style Syntax with Pandas

# Practice: SQL-Style Syntax with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: SQL-Style Syntax with Pandas

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

As a data scientist at a toy model company, you've been tasked with analyzing the company's product database to gain insights into pricing strategies. Your manager wants you to focus on the relationship between buy prices, MSRPs, and product lines. You start by importing the products table into a Pandas DataFrame named 'df' and take a quick look at the first five rows to familiarize yourself with the data structure.

Next, you use Pandas' read\_sql() function to calculate the average MSRP for each product line, naming this calculated field 'avgMSRP'. You sort these results alphabetically by product line to make the information easily digestible for the marketing team.

To visualize the relationship between buy prices and MSRPs across all products, you create a scatter plot using matplotlib. This visualization helps identify any patterns or outliers in the company's pricing strategy.

Your manager is particularly interested in the profit margin for each product. You use the DataFrame's eval method to calculate the difference between MSRP and buy price, creating a new column called 'Price\_Difference'. After examining the first five rows of this updated DataFrame and noting the total number of products, you create a histogram of the Price\_Difference to visualize the distribution of potential profit margins.

Finally, to focus on high-margin products, you use slicing to create a new DataFrame called 'df\_50' that only includes products with a Price\_Difference of $50 or more. You compare the number of rows in this new DataFrame to the original df to determine what percentage of products fall into this high-margin category.

This analysis provides valuable insights into your company’s product pricing, helping the company make informed decisions about their pricing strategy and product mix.

### Resources

* [GitHub Repository


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c1w1m4)

### Instructions

Try following the steps using Jupyter notebook. When you are finished, you can check your code and expected outputs in the Solution section.

Begin by importing the required libraries and bringing in the data.

1. Read in the products table as a Pandas dataframe.  
   1. Call it ‘df’.
   2. Look at the first five rows.
2. Using read.sql() from Pandas:  
   1. Determine the average MSRP by product line.
   2. Give the average the alias of avgMSRP.
   3. Sort alphabetically A-Z by product line.
3. Using matplotlib, create a scatterplot that shows buyPrice vs MSRP.
4. Use the DataFrame eval method in place to find the difference of MSRP and the buy price.  
   1. Call this new column `Price\_Difference'.
   2. Look at the first five rows.
   3. Give the number of rows.
5. Using matplotlib, create a histogram of Price\_Difference.
6. Using slicing, create a DataFrame that contains 'Price\_Difference' that is greater than or equal to $50.  
   1. Call this `df\_50'.
   2. Look at the number of rows.  
      1. How does this number compare to the number of rows of df?

### Solution

#### Select for Solution

Import the required libraries and bring in the data

```
# Run this code without change  
  
import sqlite3  
import pandas as pd  
from pandasql import sqldf  
from matplotlib import pyplot as plt  
  
conn = sqlite3.Connection('data.sqlite')
```

##### Step 1

```
df = pd.read_sql("""  
SELECT *  
 FROM products;  
""", conn)  
  
df.head()
```

**Expected Output:**

Expected Output: Step 1

|  | Product Code | Product Name | Product Line | Product Scale | Product Vendor | Product Description | Quantity In Stock | Buy Price | MSRP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | S10\_1678 | 1969 Harley Davidson Ultimate Chopper | Motorcycles | 1:10 | Min Lin Diecast | This replica features working kickstand, front and rear suspension, and steering. | 7933 | 48.81 | 95.70 |
| 1 | S10\_1949 | 1952 Alpine Renault 1300 | Classic Cars | 1:10 | Classic Metal Creations | Turnable front wheels; steering function; detailed interior. | 7305 | 98.58 | 214.30 |
| 2 | S10\_2016 | 1996 Moto Guzzi 1100i | Motorcycles | 1:10 | Highway 66 Mini Classics | Official Moto Guzzi logos and insignias, saddlebags, and working rear suspension. | 6625 | 68.99 | 118.94 |
| 3 | S10\_4698 | 2003 Harley-Davidson Eagle Drag Bike | Motorcycles | 1:10 | Red Start Diecast | Model features official Harley Davidson logos and insignias, and free-rolling wheels. | 5582 | 91.02 | 193.66 |
| 4 | S10\_4757 | 1972 Alfa Romeo GTA | Classic Cars | 1:10 | Motor City Art Classics | Features include: Turnable front wheels; steering function; detailed interior. | 3252 | 85.68 | 136.00 |

##### Step 2

```
query = ("""  
SELECT productLine, AVG(MSRP) AS avgMSRP  
 FROM products  
 GROUP BY productLine  
 ORDER By productLine;  
""")  
  
df_query = pd.read_sql(query, conn)  
df_query.head()
```

**Expected Output:**

```
productLineavgMSRP0Classic Cars118.0210531Motorcycles97.1784622Planes89.5158333Ships86.5633334Trains73.853333
```

##### Step 3

```
df.plot(kind='scatter', x='buyPrice', y='MSRP', s=32, alpha=.8)  
plt.gca().spines[['top', 'right',]].set_visible(False)
```

**Expected Output:**

![Scatterplot output for the MSRP and buyPrice](https://moringa.instructure.com/courses/1406/files/625322/download)

##### Step 4

```
df = df.eval('Price_Difference = MSRP-buyPrice')  
df.head()
```

**Expected Output:**

```
productCodeproductNameproductLineproductScaleproductVendorproductDescriptionquantityInStockbuyPriceMSRPPrice_Difference0S10_16781969 Harley Davidson Ultimate ChopperMotorcycles1:10Min Lin DiecastThis replica features working kickstand, front...793348.8195.7046.891S10_19491952 Alpine Renault 1300Classic Cars1:10Classic Metal CreationsTurnable front wheels; steering function; deta...730598.58214.30115.722S10_20161996 Moto Guzzi 1100iMotorcycles1:10Highway 66 Mini ClassicsOfficial Moto Guzzi logos and insignias, saddl...662568.99118.9449.953S10_46982003 Harley-Davidson Eagle Drag BikeMotorcycles1:10Red Start DiecastModel features, official Harley Davidson logos...558291.02193.66102.644S10_47571972 Alfa Romeo GTAClassic Cars1:10Motor City Art ClassicsFeatures include: Turnable front wheels; steer...325285.68136.0050.32
```

```
len(df)
```

**Expected Output:**

```
110
```

##### Step 5

```
df['Price_Difference'].plot(kind='hist', bins=20, title='Price_Difference')  
plt.gca().spines[['top', 'right',]].set_visible(False)
```

**Expected Output:**

![Histogram output of Frequency and Price\_Difference](https://moringa.instructure.com/courses/1406/files/625355/download)

##### Step 6

```
df_50 = df[df['Price_Difference'] > 50]  
len(df_50)
```

**Expected Output:**

```
32
```

```
comparison = len(df)-len(df_50)  
comparison
```

**Expected Output:**

```
78
```

```
# Remember to close the connection when you are done  
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243835

Scraped At: 2026-05-14T21:16:00.081339
