# Practice: Grouping Data with SQL

# Practice: Grouping Data with SQL

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: Grouping Data with SQL

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

You are working for a model toy company and need to run SQL queries for your boss, and with the eventual goal of setting yourself up for success as a data scientist

The series of SQL queries in this practice demonstrate progressive analysis of product data, focusing on product lines and pricing. It begins with a simple count of products in each line, sorted to show the most populous categories. The analysis then shifts to pricing, calculating average prices per product line to identify higher-value categories. Next the student does some further exploration involving finding price ranges within product lines by determining minimum and maximum MSRPs. The queries then introduce filtering conditions, first by considering only products with an MSRP of $50 or more, and then by focusing on product lines with an average price exceeding $50. The final query combines several concepts, calculating both average buy price and MSRP for product lines, but only for products and categories meeting specific price thresholds.

Throughout these queries, GROUP BY is used to organize data by product line, while ORDER BY helps in presenting results meaningfully. This sequence showcases how SQL can be used to progressively refine analysis, moving from broad overviews to more specific insights about product pricing and categorization.

### Resources

* [GitHub Repository (practice 3)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c1w1m2)

### Instructions

Begin by importing the germane libraries and connecting to the database.

```
# Run this code  
  
  
import pandas as pd  
import sqlite3  
  
  
conn = sqlite3.connect('data.sqlite')  
pd.read_sql("""  
SELECT *  
 FROM products;  
""", conn)
```

1. Select the product line.
   1. Count the number of each product line.
   2. Give the count the alias "count."
   3. Sort descending by count.
2. Select the product line.  
   1. Determine the average by Price by product line.
   2. Give the average the alias "avgPrice."
   3. Sort descending by avgPrice.
3. Select the product line.  
   1. Find the minimum of the MSRP as minMSRP.
   2. Find the maximum of the MSRP as maxMSRP.
4. Repeat (3), but only select the rows where the MSRP is $50 or more.
5. Repeat (2), but only select the product lines with an average price greater than $50.
6. Select the product line.  
   1. Find the average buy price as 'buyPrice' and the average MSRP as 'avgMSRP'.
   2. Only select MSRP greater than equal to $50.
   3. Only select avgPrice greater than equal to $50.
   4. Group by by product line and order by the ascending average price.

### Solution

### [Select for Solution](#dpPanel0)

#### Initial Output

Product Data Set, Initial Output

| # | productCode | productName | productLine | productScale | productVendor | productDescription | quantityInStock | buyPrice | MSRP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | S10\_1678 | 1969 Harley Davidson Ultimate Chopper | Motorcycles | 1:10 | Min Lin Diecast | This replica features working kickstand, front... | 7933 | 48.81 | 95.70 |
| 1 | S10\_1949 | 1952 Alpine Renault 1300 | Classic Cars | 1:10 | Classic Metal Creations | Turnable front wheels; steering function; deta... | 7305 | 98.58 | 214.30 |
| 2 | S10\_2016 | 1996 Moto Guzzi 1100i | Motorcycles | 1:10 | Highway 66 Mini Classics | Official Moto Guzzi logos and insignias, saddl... | 6625 | 68.99 | 118.94 |
| 3 | S10\_4698 | 2003 Harley-Davidson Eagle Drag Bike | Motorcycles | 1:10 | Red Start Diecast | Model features, official Harley Davidson logos... | 5582 | 91.02 | 193.66 |
| 4 | S10\_4757 | 1972 Alfa Romeo GTA | Classic Cars | 1:10 | Motor City Art Classics | Features include: Turnable front wheels; steer... | 3252 | 85.68 | 136.00 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 105 | S700\_3505 | The Titanic | Ships | 1:700 | Carousel DieCast Legends | Completed model measures 19 1/2 inches long, 9... | 1956 | 51.09 | 100.17 |
| 106 | S700\_3962 | The Queen Mary | Ships | 1:700 | Welly Diecast Productions | Exact replica. Wood and Metal. Many extras inc... | 5088 | 53.63 | 99.31 |
| 107 | S700\_4002 | American Airlines: MD-11S | Planes | 1:700 | Second Gear Diecast | Polished finish. Exact replia with official lo... | 8820 | 36.27 | 74.03 |
| 108 | S72\_1253 | Boeing X-32A JSF | Planes | 1:72 | Motor City Art Classics | 10" Wingspan with retractable landing gears.Co... | 4857 | 32.77 | 49.66 |
| 109 | S72\_3212 | Pont Yacht | Ships | 1:72 | Unimax Art Galleries | Measures 38 inches Long x 33 3/4 inches High. ... | 414 | 33.30 | 54.60 |

 110 rows × 9 columns

#### Step 1

```
# Group by  
  
pd.read_sql("""  
SELECT productLine, COUNT(*) AS count  
 FROM products  
 GROUP BY productLine  
 ORDER By count DESC;  
""", conn)
```

**Expected Output:**

Product Data Set, SELECT with DESC ORDER BY

|  | productLine | count |
| --- | --- | --- |
| 0 | Classic Cars | 38 |
| 1 | Vintage Cars | 24 |
| 2 | Motorcycles | 13 |
| 3 | Planes | 12 |
| 4 | Trucks and Buses | 11 |
| 5 | Ships | 9 |
| 6 | Trains | 3 |

#### Step 2

```
# Group by  
  
pd.read_sql("""  
SELECT productLine, AVG(buyPrice) AS avgPrice  
 FROM products  
 GROUP BY productLine  
 ORDER By avgPrice DESC;  
""", conn)
```

**Expected Output:**

Product Data Set, SELECT, GROUP BY

| # | productLine | avgPrice |
| --- | --- | --- |
| 0 | Classic Cars | 64.446316 |
| 1 | Trucks and Buses | 56.329091 |
| 2 | Motorcycles | 50.685385 |
| 3 | Planes | 49.629167 |
| 4 | Ships | 47.007778 |
| 5 | Vintage Cars | 46.066250 |
| 6 | Trains | 43.923333 |

#### Step 3

```
# Group by  
  
pd.read_sql("""  
SELECT productLine, MIN(MSRP) AS minMSRP, MAX(MSRP) AS maxMSRP  
 FROM products  
 GROUP BY productLine  
""", conn)
```

**Expected Output:**

Product Data Set, GROUP BY

| # | productLine | minMSRP | maxMSRP |
| --- | --- | --- | --- |
| 0 | Classic Cars | 35.36 | 214.30 |
| 1 | Motorcycles | 40.23 | 193.66 |
| 2 | Planes | 49.66 | 157.69 |
| 3 | Ships | 54.60 | 122.89 |
| 4 | Trains | 58.58 | 100.84 |
| 5 | Trucks and Buses | 54.11 | 136.67 |
| 6 | Vintage Cars | 33.19 | 170.00 |

#### Step 4

```
# Group by & where  
  
pd.read_sql("""  
SELECT productLine, MIN(MSRP) AS minMSRP, MAX(MSRP) AS maxMSRP  
 FROM products  
 WHERE MSRP >= 50  
 GROUP BY productLine  
""", conn)
```

**Expected Output:**

Product Data Set, GROUP BY & WHERE

|  | productLine | minMSRP | maxMSRP |
| --- | --- | --- | --- |
| 0 | Classic Cars | 50.31 | 214.30 |
| 1 | Motorcycles | 60.57 | 193.66 |
| 2 | Planes | 68.24 | 157.69 |
| 3 | Ships | 54.60 | 122.89 |
| 4 | Trains | 58.58 | 100.84 |
| 5 | Trucks and Buses | 54.11 | 136.67 |
| 6 | Vintage Cars | 50.31 | 170.00 |

#### Step 5

```
# Group by & having  
  
pd.read_sql("""  
SELECT productLine, AVG(buyPrice) AS avgPrice  
 FROM products  
 GROUP BY productLine  
 HAVING avgPrice >= 50  
 ORDER By avgPrice DESC  
""", conn)
```

**Expected Output:**

Product Data Set, GROUP BY & HAVING

|  | productLine | avgPrice |
| --- | --- | --- |
| 0 | Classic Cars | 64.446316 |
| 1 | Trucks and Buses | 56.329091 |
| 2 | Motorcycles | 50.685385 |

#### Step 6

```
# Group by & where & having  
  
pd.read_sql("""  
SELECT productLine, AVG(buyPrice) AS avgPrice, AVG(MSRP) AS avgMSRP  
 FROM products  
 WHERE MSRP >= 50  
 GROUP BY productLine  
 HAVING avgPrice >= 50  
 ORDER By avgPrice ASC  
""", conn)
```

**Expected Output:**

Product Data Set, GROUP BY, WHERE, HAVING

| # | productLine | avgPrice | avgMSRP |
| --- | --- | --- | --- |
| 0 | Vintage Cars | 50.680000 | 96.382000 |
| 1 | Planes | 51.161818 | 93.139091 |
| 2 | Motorcycles | 52.897500 | 101.924167 |
| 3 | Trucks and Buses | 56.329091 | 103.183636 |
| 4 | Classic Cars | 67.133611 | 122.546667 |

```
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243733

Scraped At: 2026-05-14T21:10:43.246608
