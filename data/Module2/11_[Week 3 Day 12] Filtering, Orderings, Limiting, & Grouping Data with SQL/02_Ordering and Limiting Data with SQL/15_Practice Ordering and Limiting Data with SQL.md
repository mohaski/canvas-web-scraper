# Practice: Ordering and Limiting Data with SQL

# Practice: Ordering and Limiting Data with SQL

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: Ordering and Limiting Data with SQL

Icon Progress Bar (browser only)

*​*

**Estimated completion time:** 30-60 minutes

In this scenario, you are working for a toy model company as as data scientist.  Your boss asks you to analyze the toy model company's database where you are required to give both general answers in the beginning steps, and more complex queries to answer very specific questions in the last steps.

For this practice with ordering and limiting data with SQL, you'll use queries that demonstrates a progression from broad product overview to specific pricing analysis within a particular toy model product line, showcasing various SQL techniques including selection, calculation, ordering, filtering, and limiting results.

### Resources

* [GitHub Repository (practice 2)


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

1. Order the data by product code in descending order.
2. Select the product code, product name, product line, and product vendor.
   1. Sort by product line and then product name.
3. Now count how many distinct product lines there are.
4. Select the product name, quantity in stock, the MSRP, the buy price, and find the difference between the MSRP and buy price.
   1. Call this difference "difference."
   2. Order by the difference from the greatest to the least and then by quantity in stock from least to greatest.
5. Select the product name, product line, the MSRP, the buy price.
   1. Find the difference between the buy price and MSRP, but use the absolute value to make the difference positive.
   2. Call this difference "abs\_difference."
   3. Order by the difference from the greatest to the least.
   4. Only select the "Classic Cars" product line.
   5. Limit the results to top 10.

### Solution

### [Select for Solution](#dpPanel0)

#### Initial Output

Product Data Set

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
# Ordering product code  
  
  
pd.read_sql("""  
SELECT *  
 FROM products  
ORDER BY productCode DESC;  
""", conn)
```

**Expected Output:**

Product Data Set with Ordering by productCode applied

| # | productCode | productName | productLine | productScale | productVendor | productDescription | quantityInStock | buyPrice | MSRP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | S72\_3212 | Pont Yacht | Ships | 1:72 | Unimax Art Galleries | Measures 38 inches Long x 33 3/4 inches High. ... | 414 | 33.30 | 54.60 |
| 1 | S72\_1253 | Boeing X-32A JSF | Planes | 1:72 | Motor City Art Classics | 10" Wingspan with retractable landing gears.Co... | 4857 | 32.77 | 49.66 |
| 2 | S700\_4002 | American Airlines: MD-11S | Planes | 1:700 | Second Gear Diecast | Polished finish. Exact replia with official lo... | 8820 | 36.27 | 74.03 |
| 3 | S700\_3962 | The Queen Mary | Ships | 1:700 | Welly Diecast Productions | Exact replica. Wood and Metal. Many extras inc... | 5088 | 53.63 | 99.31 |
| 4 | S700\_3505 | The Titanic | Ships | 1:700 | Carousel DieCast Legends | Completed model measures 19 1/2 inches long, 9... | 1956 | 51.09 | 100.17 |
| 105 | S10\_4757 | 1972 Alfa Romeo GTA | Classic Cars | 1:10 | Motor City Art Classics | Features include: Turnable front wheels; steer... | 3252 | 85.68 | 136.00 |
| 106 | S10\_4698 | 2003 Harley-Davidson Eagle Drag Bike | Motorcycles | 1:10 | Red Start Diecast | Model features, official Harley Davidson logos... | 5582 | 91.02 | 193.66 |
| 107 | S10\_2016 | 1996 Moto Guzzi 1100i | Motorcycles | 1:10 | Highway 66 Mini Classics | Official Moto Guzzi logos and insignias, saddl... | 6625 | 68.99 | 118.94 |
| 108 | S10\_1949 | 1952 Alpine Renault 1300 | Classic Cars | 1:10 | Classic Metal Creations | Turnable front wheels; steering function; deta... | 7305 | 98.58 | 214.30 |
| 109 | S10\_1678 | 1969 Harley Davidson Ultimate Chopper | Motorcycles | 1:10 | Min Lin Diecast | This replica features working kickstand, front... | 7933 | 48.81 | 95.70 |

110 rows × 9 columns

#### Step 2

```
pd.read_sql("""  
SELECT productCode, productLine, productName, productVendor  
 FROM products  
ORDER BY productLine, productName;  
""", conn)
```

**Expected Output:**

Product Data Set using SELECT and ORDER BY

| # | productCode | productLine | productName | productVendor |
| --- | --- | --- | --- | --- |
| 0 | S18\_1889 | Classic Cars | 1948 Porsche 356-A Roadster | Gearbox Collectibles |
| 1 | S18\_3685 | Classic Cars | 1948 Porsche Type 356 Roadster | Gearbox Collectibles |
| 2 | S24\_2766 | Classic Cars | 1949 Jaguar XK 120 | Classic Metal Creations |
| 3 | S10\_1949 | Classic Cars | 1952 Alpine Renault 1300 | Classic Metal Creations |
| 4 | S24\_2887 | Classic Cars | 1952 Citroen-15CV | Exoto Designs |
| ... | ... | ... | ... | ... |
| 105 | S24\_2022 | Vintage Cars | 1938 Cadillac V-16 Presidential Limousine | Classic Metal Creations |
| 106 | S18\_4668 | Vintage Cars | 1939 Cadillac Limousine | Studio M Art Models |
| 107 | S24\_1937 | Vintage Cars | 1939 Chevrolet Deluxe Coupe | Motor City Art Classics |
| 108 | S24\_3816 | Vintage Cars | 1940 Ford Delivery Sedan | Carousel DieCast Legends |
| 109 | S18\_3856 | Vintage Cars | 1941 Chevrolet Special Deluxe Cabriolet | Exoto Designs |

110 rows × 4 columns

#### Step 3

```
# Count  
  
  
pd.read_sql("""  
SELECT COUNT(DISTINCT productLine) AS productLineCount  
 FROM products  
""", conn)
```

**Expected Output:**

Expected Data Output from SELECT COUNT

| # | productlineCount |
| --- | --- |
| 0 | 7 |

#### Step 4

```
# Query  
  
  
pd.read_sql("""  
SELECT productName, quantityInStock, MSRP, buyPrice, MSRP - buyPrice AS difference  
 FROM products  
ORDER BY difference DESC, CAST(quantityInStock AS INTEGER) ASC;  
""", conn)
```

**Expected Output:**

Product Data Set (SELECT quantityInStock, MSRP, buyPrice, difference)

| # | productName | quantityInStock | MSRP | buyPrice | difference |
| --- | --- | --- | --- | --- | --- |
| 0 | 1952 Alpine Renault 1300 | 7305 | 214.30 | 98.58 | 115.72 |
| 1 | 2001 Ferrari Enzo | 3619 | 207.80 | 95.59 | 112.21 |
| 2 | 2003 Harley-Davidson Eagle Drag Bike | 5582 | 193.66 | 91.02 | 102.64 |
| 3 | 1968 Ford Mustang | 68 | 194.57 | 95.34 | 99.23 |
| 4 | 1928 Mercedes-Benz SSK | 548 | 168.75 | 72.56 | 96.19 |
| ... | ... | ... | ... | ... | ... |
| 105 | 1936 Mercedes Benz 500k Roadster | 2081 | 41.03 | 21.75 | 19.28 |
| 106 | Boeing X-32A JSF | 4857 | 49.66 | 32.77 | 16.89 |
| 107 | 1930 Buick Marquette Phaeton | 7062 | 43.64 | 27.06 | 16.58 |
| 108 | 1982 Ducati 996 R | 9241 | 40.23 | 24.14 | 16.09 |
| 109 | 1939 Chevrolet Deluxe Coupe | 7332 | 33.19 | 22.57 | 10.62 |

#### Step 5

```
# Query  
  
  
pd.read_sql("""  
SELECT productName, productLine, MSRP, buyPrice, abs(buyPrice - MSRP) AS abs_difference  
 FROM products  
 WHERE productLine ="Classic Cars"  
ORDER BY abs_difference DESC  
LIMIT 10;  
""", conn)  
  
 
```

**Expected Output:**

Product Data Set SELECT columns by productLine

| # | productName | productLine | MSRP | buyPrice | abs\_difference |
| --- | --- | --- | --- | --- | --- |
| 0 | 1952 Alpine Renault 1300 | Classic Cars | 214.30 | 98.58 | 115.72 |
| 1 | 2001 Ferrari Enzo | Classic Cars | 207.80 | 95.59 | 112.21 |
| 2 | 1968 Ford Mustang | Classic Cars | 194.57 | 95.34 | 99.23 |
| 3 | 1992 Ferrari 360 Spider red | Classic Cars | 169.34 | 77.90 | 91.44 |
| 4 | 1969 Ford Falcon | Classic Cars | 173.02 | 83.05 | 89.97 |
| 5 | 1948 Porsche Type 356 Roadster | Classic Cars | 141.28 | 62.16 | 79.12 |
| 6 | 1957 Corvette Convertible | Classic Cars | 148.80 | 69.93 | 78.87 |
| 7 | 1999 Indy 500 Monte Carlo SS | Classic Cars | 132.00 | 56.76 | 75.24 |
| 8 | 1976 Ford Gran Torino | Classic Cars | 146.99 | 73.49 | 73.50 |
| 9 | 1998 Chrysler Plymouth Prowler | Classic Cars | 163.73 | 101.51 | 62.2 |

```
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243721

Scraped At: 2026-05-14T21:10:01.362467
