# Practice: Filtering Data with SQL

# Practice: Filtering Data with SQL

## ![20240930\_205312preview](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: Filtering Data with SQL

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

For this practice, you’ll begin by connecting to a SQLite database using Python and then work through a series of increasingly complex SQL tasks. These exercises cover basic filtering, column selection, string manipulation, date filtering, pattern matching with LIKE, and simple aggregations. By working with the Northwind database and various query types, you will gain practical experience in extracting and analyzing data from databases and honing your filtering skills.

### Resources

* [GitHub Repository (practice 1)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c1w1m2)

### Instructions

* [Part 1](#dpPanel0Content)
* [Part 2](#dpPanel1Content)

### Part 1

1. Import the germane libraries and connect to the database

```
# Run this code  
  
import pandas as pd  
import sqlite3  
  
conn = sqlite3.connect('data.sqlite')  
pd.read_sql("""  
SELECT *  
 FROM employees;  
""", conn)
```

1. Select all of the employees with first name "Leslie"
2. For the employees named Leslie, give the first name, last name, and job title.
3. Select all employees that have a last name less than 5. Using inequalities, do this in two different ways using conditionals.

### Part 2

1. Connect the orderDetails database.

```
# Run this code  
  
conn = sqlite3.connect('data.sqlite')  
pd.read_sql("""  
SELECT *  
FROM orderDetails;  
""", conn)
```

1. Round the price as an integer.
2. Let's look at the orders database.

```
conn = sqlite3.connect('data.sqlite')  
pd.read_sql("""  
SELECT *  
 FROM orders;  
""", conn)
```

1. Find all orders placed in the year 2005 in the orders database.
2. Going back to the employees database, use LIKE to find all of those who have sale or sales in their job title.
3. Find out how many items are priced at least $200 in the orderDetails database.

### Solution

### [Select for Solution](#dpPanel2)

#### Part 1

1. **Step 1** **Expected Output:**

```
employeeNumberlastNamefirstNameextensionemailofficeCodereportsTojobTitle01002MurphyDianex5800dmurphy@classicmodelcars.com1President11056PattersonMaryx4611mpatterso@classicmodelcars.com11002VP Sales21076FirrelliJeffx9273jfirrelli@classicmodelcars.com11002VP Marketing31088PattersonWilliamx4871wpatterson@classicmodelcars.com61056Sales Manager (APAC)41102BondurGerardx5408gbondur@classicmodelcars.com41056Sale Manager (EMEA)51143BowAnthonyx5428abow@classicmodelcars.com11056Sales Manager (NA)61165JenningsLesliex3291ljennings@classicmodelcars.com11143Sales Rep71166ThompsonLesliex4065lthompson@classicmodelcars.com11143Sales Rep81188FirrelliJuliex2173jfirrelli@classicmodelcars.com21143Sales Rep91216PattersonStevex4334spatterson@classicmodelcars.com21143Sales Rep101286TsengFoon Yuex2248ftseng@classicmodelcars.com31143Sales Rep111323VanaufGeorgex4102gvanauf@classicmodelcars.com31143Sales Rep121337BondurLouix6493lbondur@classicmodelcars.com41102Sales Rep131370HernandezGerardx2028ghernande@classicmodelcars.com41102Sales Rep141401CastilloPamelax2759pcastillo@classicmodelcars.com41102Sales Rep151501BottLarryx2311lbott@classicmodelcars.com71102Sales Rep161504JonesBarryx102bjones@classicmodelcars.com71102Sales Rep171611FixterAndyx101afixter@classicmodelcars.com61088Sales Rep181612MarshPeterx102pmarsh@classicmodelcars.com61088Sales Rep191619KingTomx103tking@classicmodelcars.com61088Sales Rep201621NishiMamix101mnishi@classicmodelcars.com51056Sales Rep211625KatoYoshimix102ykato@classicmodelcars.com51621Sales Rep221702GerardMartinx2312mgerard@classicmodelcars.com41102Sales Rep
```

1. **Step 2**

```
# Fist name Leslie  
pd.read_sql("""  
SELECT *  
 FROM employees  
WHERE firstName = "Leslie";  
""", conn)
```

**Expected Output:**

Data output: first name Leslie

| # | employeeNumber | lastName | firstName | extension | email | officeCode | reportsTo | jobTitle |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1165 | Jennings | Leslie | x3291 | ljennings@classicmodelcars.com | 1 | 1143 | Sales Rep |
| 1 | 1166 | Thompson | Leslie | x4865 | lthompson@classicmodelcars.com | 1 | 1143 | Sales Rep |

1. **Step 3**

```
# First name Leslie, with last name and title  
  
  
pd.read_sql("""  
SELECT firstName, lastName, jobTitle  
 FROM employees  
WHERE firstName = "Leslie";  
""", conn)
```

**Expected Output:**

Data Output: Employee Name "Leslie"

| # | firstName | lastName |
| --- | --- | --- |
| 0 | Leslie | Jennings |
| 1 | Leslie | Thompson |

1. **Step 4**

```
# Strictly less than 5  
pd.read_sql("""  
SELECT *, length(lastName) AS name_length  
 FROM employees  
WHERE name_length < 5;  
""", conn)  
  
# OR  
  
# Less than or equal to 4.  
pd.read_sql("""  
SELECT *, length(lastName) AS name_length  
 FROM employees  
WHERE name_length <= 4;  
""", conn)
```

**Expected Output:**

Data Output: Employees with less than 5 letters last name

| # | employeeNumber | lastName | firstName | extension | email | officeCode | reportsTo | jobTitle | name\_length |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1143 | Bow | Anthony | x5428 | abow@classicmodelcars.com | 1 | 1056 | Sales Manager (NA) | 3 |
| 1 | 1501 | Bott | Larry | x2311 | lbott@classicmodelcars.com | 7 | 1102 | Sales Rep | 4 |
| 2 | 1619 | King | Tom | x103 | tking@classicmodelcars.com | 6 | 1088 | Sales Rep | 4 |
| 3 | 1625 | Kato | Yoshimi | x102 | ykato@classicmodelcars.com | 5 | 1621 | Sales Rep | 4 |

Data Output: Employees with less than 4 letters last name

| # | employeeNumber | lastName | firstName | extension | email | officeCode | reportsTo | jobTitle | name\_length |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1143 | Bow | Anthony | x5428 | abow@classicmodelcars.com | 1 | 1056 | Sales Manager (NA) | 3 |
| 1 | 1501 | Bott | Larry | x2311 | lbott@classicmodelcars.com | 7 | 1102 | Sales Rep | 4 |
| 2 | 1619 | King | Tom | x103 | tking@classicmodelcars.com | 6 | 1088 | Sales Rep | 4 |
| 3 | 1625 | Kato | Yoshimi | x102 | ykato@classicmodelcars.com | 5 | 1621 | Sales Rep | 4 |

#### Part 2

1. **Step 1**

```
# Run this code  
  
  
conn = sqlite3.connect('data.sqlite')  
pd.read_sql("""  
SELECT *  
 FROM orderDetails;  
""", conn)
```

**Expected Output:**

Data Output: partial view of SELECT \* orderDetails

| # | orderNumber | productCode | quantityOrdered | priceEach | orderLineNumber |
| --- | --- | --- | --- | --- | --- |
| 0 | 10100 | S18\_1749 | 30 | 136.00 | 3 |
| 1 | 10100 | S18\_2248 | 50 | 55.09 | 2 |
| 2 | 10100 | S18\_4409 | 22 | 75.46 | 4 |
| 3 | 10100 | S24\_3969 | 49 | 35.29 | 1 |
| 4 | 10101 | S18\_2325 | 25 | 108.06 | 4 |
| ... | ... | ... | ... | ... | ... |
| 2991 | 10425 | S24\_2300 | 49 | 127.79 | 9 |
| 2992 | 10425 | S24\_2840 | 31 | 31.82 | 5 |
| 2993 | 10425 | S32\_1268 | 41 | 83.79 | 11 |
| 2994 | 10425 | S32\_2509 | 11 | 50.32 | 6 |
| 2995 | 10425 | S50\_1392 | 18 | 94.92 | 2 |

Output showing: 2996 rows × 5 columns

1. **Step 2**

```
# Rounding the price  
  
  
pd.read_sql("""  
SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int  
 FROM orderDetails  
WHERE rounded_price_int >= 100;  
""", conn)
```

**Expected Output:**

Partial Data Output: Query for rounded orderDetails price above 100

| # | orderNumber | productCode | quantityOrdered | priceEach | orderLineNumber | rounded\_price\_int |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 10100 | S18\_1749 | 30 | 136.00 | 3 | 136 |
| 1 | 10101 | S18\_2325 | 25 | 108.06 | 4 | 108 |
| 2 | 10101 | S18\_2795 | 26 | 167.06 | 1 | 167 |
| 3 | 10103 | S10\_1949 | 26 | 214.30 | 11 | 214 |
| 4 | 10103 | S10\_4962 | 42 | 119.67 | 4 | 120 |
| ... | ... | ... | ... | ... | ... | ... |
| 1105 | 10425 | S18\_2238 | 28 | 147.36 | 3 | 147 |
| 1106 | 10425 | S18\_2319 | 38 | 117.82 | 7 | 118 |
| 1107 | 10425 | S18\_3232 | 28 | 140.55 | 8 | 141 |
| 1108 | 10425 | S18\_4600 | 38 | 107.76 | 13 | 108 |
| 1109 | 10425 | S24\_2300 | 49 | 127.79 | 9 | 128 |

Output showing: 1110 rows × 6 columns

1. **Step 3**

```
conn = sqlite3.connect('data.sqlite')  
pd.read_sql("""  
SELECT *  
 FROM orders;  
""", conn)
```

**Expected Output:**

Partial view of Data Output: orders

| # | orderNumber | orderDate | requiredDate | shippedDate | status | comments | customerNumber |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10100 | 2003-01-06 | 2003-01-13 | 2003-01-10 | Shipped |  | 363 |
| 1 | 10101 | 2003-01-09 | 2003-01-18 | 2003-01-11 | Shipped | Check on availability. | 128 |
| 2 | 10102 | 2003-01-10 | 2003-01-18 | 2003-01-14 | Shipped |  | 181 |
| 3 | 10103 | 2003-01-29 | 2003-02-07 | 2003-02-02 | Shipped |  | 121 |
| 4 | 10104 | 2003-01-31 | 2003-02-09 | 2003-02-01 | Shipped |  | 141 |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 321 | 10421 | 2005-05-29 | 2005-06-06 |  | In Process | Custom shipping instructions were sent to ware... | 124 |
| 322 | 10422 | 2005-05-30 | 2005-06-11 |  | In Process |  | 157 |
| 323 | 10423 | 2005-05-30 | 2005-06-05 |  | In Process |  | 314 |
| 324 | 10424 | 2005-05-31 | 2005-06-08 |  | In Process |  | 141 |
| 325 | 10425 | 2005-05-31 | 2005-06-07 |  | In Process |  | 119 |

Output showing: 326 rows × 7 columns

1. **Step 4**

```
# Just 2005  
  
  
pd.read_sql("""  
SELECT *, strftime("%Y", orderDate) AS year  
 FROM orders  
WHERE year = "2005";  
""", conn)
```

**Expected Output:**

Partial view, data output order placed in 2005

| # | orderNumber | orderDate | requiredDate | shippedDate | status | comments | customerNumber | year |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10362 | 2005-01-05 | 2005-01-16 | 2005-01-10 | Shipped |  | 161 | 2005 |
| 1 | 10363 | 2005-01-06 | 2005-01-12 | 2005-01-10 | Shipped |  | 334 | 2005 |
| 2 | 10364 | 2005-01-06 | 2005-01-17 | 2005-01-09 | Shipped |  | 350 | 2005 |
| 3 | 10365 | 2005-01-07 | 2005-01-18 | 2005-01-11 | Shipped |  | 320 | 2005 |
| 4 | 10366 | 2005-01-10 | 2005-01-19 | 2005-01-12 | Shipped |  | 381 | 2005 |
| ... | ... | ... | ... | ... | ... | ... | ... | 2005 |
| 59 | 10421 | 2005-05-29 | 2005-06-06 |  | In Process | Custom shipping instructions were sent to ware... | 124 | 2005 |
| 60 | 10422 | 2005-05-30 | 2005-06-11 |  | In Process |  | 157 | 2005 |
| 61 | 10423 | 2005-05-30 | 2005-06-05 |  | In Process |  | 314 | 2005 |
| 62 | 10424 | 2005-05-31 | 2005-06-08 |  | In Process |  | 141 | 2005 |
| 63 | 10425 | 2005-05-31 | 2005-06-07 |  | In Process |  | 119 | 2005 |

Output showing: 64 rows × 8 columns

1. **Step 5**

```
# Using sales with wildcard  
  
  
pd.read_sql("""  
SELECT *  
 FROM employees  
WHERE jobTitle LIKE "Sale%";  
""", conn)
```

**Expected Output:**

Data Output, using LIKE to find all of those who have sale or sales in their job title.

| # | employeeNumber | lastName | firstName | extension | email | officeCode | reportsTo | jobTitle |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1088 | Patterson | William | x4871 | wpatterson@classicmodelcars.com | 6 | 1056 | Sales Manager (APAC) |
| 1 | 1102 | Bondur | Gerard | x5408 | gbondur@classicmodelcars.com | 4 | 1056 | Sale Manager (EMEA) |
| 2 | 1143 | Bow | Anthony | x5428 | abow@classicmodelcars.com | 1 | 1056 | Sales Manager (NA) |
| 3 | 1165 | Jennings | Leslie | x3291 | ljennings@classicmodelcars.com | 1 | 1143 | Sales Rep |
| 4 | 1166 | Thompson | Leslie | x4065 | lthompson@classicmodelcars.com | 1 | 1143 | Sales Rep |
| 5 | 1188 | Firrelli | Julie | x2173 | jfirrelli@classicmodelcars.com | 2 | 1143 | Sales Rep |
| 6 | 1216 | Patterson | Steve | x4334 | spatterson@classicmodelcars.com | 2 | 1143 | Sales Rep |
| 7 | 1286 | Tseung | Foon Yue | x2248 | ftseng@classicmodelcars.com | 3 | 1143 | Sales Rep |
| 8 | 1323 | Vanauf | George | x4102 | gvanauf@classicmodelcars.com | 3 | 1143 | Sales Rep |
| 9 | 1337 | Bondur | Loui | x6493 | lbondur@classicmodelcars.com | 4 | 1102 | Sales Rep |
| 10 | 1370 | Hernandex | Gerard | x2028 | ghernande@classicmodelcars.com | 4 | 1102 | Sales Rep |
| 11 | 1401 | Castillo | Pamela | x2759 | pcastillo@classicmodelcars.com | 4 | 1102 | Sales Rep |
| 12 | 1501 | Bott | Larry | x2311 | lbott@classicmodelcars.com | 7 | 1102 | Sales Rep |
| 13 | 1504 | Jones | Barry | x102 | bjones@classicmodelcars.com | 7 | 1102 | Sales Rep |
| 14 | 1611 | Fixter | Andy | x101 | afixter@classicmodelcars.com | 6 | 1088 | Sales Rep |
| 15 | 1612 | Marsh | Peter | x102 | pmarsh@classicmodelcars.com | 6 | 1088 | Sales Rep |
| 16 | 1610 | King | Tom | x103 | tking@classicmodelcars.com | 6 | 1088 | Sales Rep |
| 17 | 1621 | Nishi | Mami | x101 | mnishi@classicmodelcars.com | 5 | 1056 | Sales Rep |
| 18 | 1625 | Kato | Yoshimi | x102 | ykato@classicmodelcars.com | 5 | 1621 | Sales Rep |
| 19 | 1702 | Gerard | Martin | x2312 | mgerard@classicmodelcars.com | 4 | 1102 | Sales Rep |

1. **Step 6**

```
# Count each  
  
  
pd.read_sql("""  
SELECT COUNT(priceEach)  
 FROM orderDetails  
WHERE priceEach >=200;  
""", conn)
```

**Expected Output:**

Data output, count of items with price >=200

| # | COUNT(priceEach) |
| --- | --- |
| 0 | 20 |

```
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243709

Scraped At: 2026-05-14T21:09:16.842109
