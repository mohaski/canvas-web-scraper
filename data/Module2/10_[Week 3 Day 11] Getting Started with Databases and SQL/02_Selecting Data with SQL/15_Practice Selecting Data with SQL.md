# Practice: Selecting Data with SQL

# Practice: Selecting Data with SQL

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: Selecting Data with SQL

Icon Progress Bar (browser only)

*​*

**Estimated completion time:** 30-60 minutes

As a data scientist, understanding how to select data with SQL is a crucial skill in data analysis and manipulation.

Imagine you're working with a large e-commerce database containing millions of customer transactions. Your task is to analyze customer purchasing behavior to inform marketing strategies. Using SQL's SELECT statement, you can efficiently extract specific information from this vast dataset. For instance, you might want to retrieve the total amount spent by each customer in the last quarter, focusing only on those who made purchases exceeding $500. SQL allows you to precisely define these criteria, filtering and aggregating data from various tables to obtain the exact insights you need.

This ability to select, filter, and summarize data is fundamental to deriving meaningful insights and forms the foundation for more complex data analysis tasks.

### Resources

* [GitHub Repository: Selecting Data with SQL 


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c1w1m1/tree/main)

### Instructions

Run the code below without change to get started.

```
# Connecting, Libraries, and Data  
  
import sqlite3  
conn = sqlite3.connect('data.sqlite')  
  
import pandas as pd  
  
pd.read_sql("""  
SELECT *  
  FROM products;  
""", conn)
```

* [Step 1](#dpPanel0Content)
* [Step 2](#dpPanel1Content)
* [Step 3](#dpPanel2Content)
* [Step 4](#dpPanel3Content)
* [Step 5](#dpPanel4Content)
* [Step 6](#dpPanel5Content)
* [Step 7](#dpPanel6Content)
* [Step 8](#dpPanel7Content)
* [Step 9](#dpPanel8Content)
* [Step 10](#dpPanel9Content)

### Step 1

* Select the product name and product code for the products.
* Show the last five products.

### Step 2

* Switch the order of the columns, i.e. show the product code first and then the product name.
* Show the last five products.

### Step 3

* Select the product name and product line.
  + When the product line is "Planes" keep it as "Planes", otherwise have it as "Not Planes."
  + Call this new column "Planes.”

### Step 4

* Find the length of the product description for each product.
  + Call this new column "description\_length."
  + Show the first five rows of data.

### Step 5

* Change the product vendor to all caps.
  + Call this new column "caps\_vendor."
  + Show the first five rows.

### Step 6

* Change the product name to all lowercase.
  + Use lower() as you did upper().
* Call this new column "lower\_name."
* Show the first five rows.

### Step 7

* Since all of the product scales are 1:xxx, we can take a substring of just the number following the colon.
* The first character following the colon is the third character.
* None of the scales are more than 1 to a three digit number.

### Step 8

* Create a new column "fullName" that has product vendor followed by the product name with a space between.
  + For example, Min Lin Diecast 1969 Harley Davidson Ultimate Chopper.

### Step 9

* Find the difference in price between the MSRP and the buy price.
* Round the difference to the nearest whole number, i.e. as an integer, not floating point.
* Call this new column "round\_diff."

**Hint:** These should all be positive values.

### Step 10

Close the connection when finished.

### Solution

### [**Select for Solution**](#dpPanel10)

Run the code below without change to get started:

```
# Connecting, Libraries, and Data  
  
import sqlite3  
conn = sqlite3.connect('data.sqlite')  
  
import pandas as pd  
  
pd.read_sql("""  
SELECT *  
  FROM products;  
""", conn)
```

**Expected Output:**

SQL output for products

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
pd.read_sql("""  
SELECT productName, productCode  
  FROM products;  
""", conn).tail()
```

**Expected Output:**

SQL output with productCode query

| # | productName | productCode |
| --- | --- | --- |
| 105 | The Titanic | S700\_3505 |
| 106 | The Queen Mary | S700\_3962 |
| 107 | American Airlines: MD-11S | S700\_4002 |
| 108 | Boeing X-32A JSF | S72\_1253 |
| 109 | Pont Yacht | S72\_3212 |

#### Step 2

```
pd.read_sql("""  
SELECT productCode, productName  
  FROM products;  
""", conn).tail()
```

**Expected Output:**

SQL output using SELECT, productCode and productName

| # | productCode | productName |
| --- | --- | --- |
| 105 | S700\_3505 | The Titanic |
| 106 | S700\_3962 | The Queen Mary |
| 107 | S700\_4002 | American Airlines: MD-11S |
| 108 | S72\_1253 | Boeing X-32A JSF |
| 109 | S72\_3212 | Pont Yacht |

#### Step 3

```
pd.read_sql("""  
SELECT productName, productLine,  
       CASE  
       WHEN productLine = "Planes" THEN "Planes"  
       ELSE "Not Planes"  
       END AS Planes  
  FROM products;  
""", conn)
```

**Expected Output:**

SQL output with "Not Planes" query

| # | productName | productLine | Planes |
| --- | --- | --- | --- |
| 0 | 1969 Harley Davidson Ultimate Chopper | Motorcycles | Not Planes |
| 1 | 1952 Alpine Renault 1300 | Classic Cars | Not Planes |
| 2 | 1996 Moto Guzzi 1100i | Motorcycles | Not Planes |
| 3 | 2003 Harley-Davidson Eagle Drag Bike | Motorcycles | Not Planes |
| 4 | 1972 Alfa Romeo GTA | Classic Cars | Not Planes |
| ... | ... | ... | ... |
| 105 | The Titanic | Ships | Not Planes |
| 106 | The Queen Mary | Ships | Not Planes |
| 107 | American Airlines: MD-11S | Planes | Planes |
| 108 | Boeing X-32A JSF | Planes | Planes |
| 109 | Pont Yacht | Ships | Not Planes |

#### Step 4

```
pd.read_sql("""  
SELECT length(productDescription) AS description_length  
  FROM products;  
""", conn).head()
```

**Expected Output:**

SQL query to SELECT length

| # | description\_length |
| --- | --- |
| 0 | 230 |
| 1 | 143 |
| 2 | 391 |
| 3 | 494 |
| 4 | 161 |

#### Step 5

```
pd.read_sql("""  
SELECT upper(productVendor) AS caps_vendor  
  FROM products;  
""", conn).head()
```

**Expected Output:**

SQL query to SELECT caps\_vendor

| # | caps\_vendor |
| --- | --- |
| 0 | MIN LIN DIECAST |
| 1 | CLASSIC METAL CREATIONS |
| 2 | HIGHWAY 66 MINI CLASSICS |
| 3 | RED START DIECAST |
| 4 | MOTOR CITY ART CLASSICS |

#### Step 6

```
pd.read_sql("""  
SELECT lower(productName) AS lower_name  
  FROM products;  
""", conn).head()  
  
 
```

**Expected Output:**

SQL query SELECT lower(productName)

|  | lower\_name |
| --- | --- |
| 0 | 1969 harley davidson ultimate chopper |
| 1 | 1952 alpine renault 1300 |
| 2 | 1966 moto guzzi 1100i |
| 3 | 2003 harley-davidson eagle drag bike |
| 4 | 1972 alfa romeo gta |

#### Step 7

```
pd.read_sql("""  
SELECT substr(productScale, 3,3) AS non  
  FROM products;  
""", conn)
```

**Expected Output:**

SQL query SELECT substr

| # | non |
| --- | --- |
| 0 | 10 |
| 1 | 10 |
| 2 | 10 |
| 3 | 10 |
| 4 | 10 |
| ... | ... |
| 105 | 700 |
| 106 | 700 |
| 107 | 700 |
| 108 | 72 |
| 109 | 72 |

110 rows × 1 columns

#### Step 8

```
pd.read_sql("""  
SELECT productVendor || " " || productName AS fullName  
  FROM products;  
""", conn)
```

**Expected Output:**

SQL SELECT productVendor fullName

| # | fullName |
| --- | --- |
| 0 | Min Lin Diecast 1969 Harley Davidson Ultimate ... |
| 1 | Classic Metal Creations 1952 Alpine Renault 1300 |
| 2 | Highway 66 Mini Classics 1996 Moto Guzzi 1100i |
| 3 | Red Start Diecast 2003 Harley-Davidson Eagle D... |
| 4 | Motor City Art Classics 1972 Alfa Romeo GTA |
| ... | ... |
| 105 | Carousel DieCast Legends The Titanic |
| 106 | Welly Diecast Productions The Queen Mary |
| 107 | Second Gear Diecast American Airlines: MD-11S |
| 108 | Motor City Art Classics Boeing X-32A JSF |
| 109 | Unimax Art Galleries Pont Yacht |

110 rows × 1 columns

#### Step 9

```
pd.read_sql("""  
SELECT CAST(round(MSRP - buyPrice) AS INTEGER) AS round_diff  
  FROM products;  
""", conn)
```

**Expected Output:**

SQL output using round\_diff

| # | round\_diff |
| --- | --- |
| 0 | 47 |
| 1 | 116 |
| 2 | 50 |
| 3 | 103 |
| 4 | 50 |
| ... | ... |
| 105 | 49 |
| 106 | 56 |
| 107 | 38 |
| 108 | 17 |
| 109 | 21 |

110 rows × 1 columns

#### Step 10

```
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243695

Scraped At: 2026-05-14T21:07:38.626118
