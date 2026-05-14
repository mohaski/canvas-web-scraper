# Technical Lesson: Data Engineering with SQL

# Technical Lesson: Data Engineering with SQL

## ![20240930\_205312preview](https://moringa.instructure.com/courses/1406/files/625387/preview) Technical Lesson: Data Engineering with SQL

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In this technical lesson, we delve into the critical role of SQL within the data engineering lifecycle, particularly from the perspective of data scientists. SQL (Structured Query Language) is not just a tool for querying databases; it is a powerful and versatile language that serves as the backbone of data management in many organizations. For data scientists, mastering SQL is essential because it enables them to efficiently interact with relational databases, where much of the world's structured data resides.

Through SQL, data scientists can perform a wide range of tasks, from creating and modifying database schemas to executing complex queries that retrieve and transform data for analysis. Beyond simple data retrieval, SQL allows data scientists to manage the entire lifecycle of data—ensuring that the data is stored in an organized manner, cleaned of any inconsistencies, and transformed into a format that is optimal for analysis. This capability is crucial because the quality of the data directly impacts the insights that can be derived from it. Clean, well-structured data is the foundation of accurate analysis, predictive modeling, and data-driven decision-making.

We will see how SQL is integrated into each stage of the data engineering lifecycle, from the initial ingestion of data into a database to its final transformation and serving. By gaining a deeper understanding of SQL’s role in these processes, data scientists can enhance their ability to manage data effectively, ensuring that it is both reliable and actionable. Whether you are cleaning raw data, performing complex joins and aggregations, or preparing data for deployment in machine learning models, SQL is an indispensable tool in your data science toolkit.

In particular, in this lesson, we will apply the concepts of Data Engineering with SQL by working through a practical example involving customer data management. Imagine we are tasked with organizing and analyzing customer information for a global retail company. We will start by loading existing customer data from a CSV file into a Pandas DataFrame, simulating the initial data generation process. From there, we’ll move the data into a SQLite database, where we’ll define the structure and schema necessary to store this information in an organized way.

Once the data is securely stored, we’ll use SQL to ingest it into the database and perform essential transformations, such as removing duplicates, handling missing values, and aggregating data to derive meaningful insights like the average credit limit by city. Finally, we’ll learn how to serve this cleaned and transformed data, ensuring it is accessible for reporting and analysis.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of the data engineering with Python.

[VIDEO LINK](https://player.vimeo.com/video/1009315123?h=082ecc1611)

### Step 1: Generation

We are going to use existing data to 'generate' it via pandas DataFrame. Use the `customer_data.csv` file with the Python notebook `SQLM7P1.ipynb` in the **[Drive


Links to an external site.](https://drive.google.com/drive/folders/1UFePMt_hSsSVakrH9XExXQt9sxhiZRLM)**.

```
# Imports  
import pandas as pd  
import sqlite3  
  
# Read CSV into DataFrame  
df = pd.read_csv('customer_data.csv', index_col=0)  
df.head()
```

**Output:**

SQL Data Set: Customer Information

| Customer Number | Customer Name | Contact Last Name | Contact First Name | Phone | Address Line 1 | Address Line 2 | City | State | Postal Code | Country | Sales Rep Employee Number | Credit Limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 103 | Atelier graphique | Schmitt | Carine | 40.32.2555 | 54, rue Royale | NaN | Nantes | NaN | 44000 | France | 1370.0 | 21000.0 |
| 112 | Signal Gift Stores | King | Jean | 7025551838 | 8489 Strong St. | NaN | Las Vegas | NV | 83030 | USA | 1166.0 | 71800.0 |
| 114 | Australian Collectors, Co. | Ferguson | Peter | 03 9520 4555 | 636 St Kilda Road | Level 3 | Melbourne | Victoria | 3004 | Australia | 1611.0 | 117300.0 |
| 119 | La Rochelle Gifts | Labrune | Janine | 40.67.8555 | 67, rue des Cinquante Otages | NaN | Nantes | NaN | 44000 | France | 1370.0 | 118200.0 |
| 121 | Baane Mini Imports | Bergulfsen | Jonas | 07-98 9555 | Erling Skakkes gate 78 | NaN | Stavern | NaN | 4110 | Norway | 1504.0 | 81700.0 |

### Step 2: Store Data

In order to properly store the data contained in the above DataFrame we must first create our SQL database and subsequent table schema in order to ingest this data. Let's start by creating a new database via our connection call.

```
# 2. Create a connection to a new SQLite database thus creating it  
conn = sqlite3.connect('customer_database.db')  
c = conn.cursor()
```

We now need to create the table via executing a SQL query as we have done in previous modules. We need to keep track of columns and values so we can specify what datatypes SQL should store this information in.

```
# Create a table to store the customer data  
c.execute('''CREATE TABLE IF NOT EXISTS customers  
             (customerNumber INTEGER PRIMARY KEY,  
             customerName TEXT,  
             contactLastName TEXT,  
             contactFirstName TEXT,  
             phone TEXT,  
             addressLine1 TEXT,  
             addressLine2 TEXT,  
             city TEXT,  
             state TEXT,  
             postalCode INTEGER,  
             country TEXT,  
             saleRepEmployeeNumber INTEGER  
             creditLimit INTEGER)''')
```

**Output:**

```
<sqlite3.Cursor at 0x11ec534c0>
```

### Step 3: Ingest Data

Now that we have the table created and laid out with the appropriate schema we can ingest our data from the DataFrame into the SQL database and table. We could use INSERT INTO but that would require some reformatting of the data to extract it from the DataFrame. Pandas and SQL are built to work together and thus Pandas has a direct way to save information into a SQL tables via the to\_sql() method.

```
#### Load/store the data from the DataFrame into the database table  
df.to_sql('customers', conn, if_exists='replace', index=False)  
  
# Sanity Check  
pd.read_sql('''SELECT * FROM customers''', conn).head()
```

**Output:**

SQL Data Set: Customer Information (with 'None' values)

| Customer Number | Customer Name | Contact Last Name | Contact First Name | Phone | Address Line 1 | Address Line 2 | City | State | Postal Code | Country | Sales Rep Employee Number | Credit Limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 103 | Atelier graphique | Schmitt | Carine | 40.32.2555 | 54, rue Royale | None | Nantes | None | 44000 | France | 1370.0 | 21000.0 |
| 112 | Signal Gift Stores | King | Jean | 7025551838 | 8489 Strong St. | None | Las Vegas | NV | 83030 | USA | 1166.0 | 71800.0 |
| 114 | Australian Collectors, Co. | Ferguson | Peter | 03 9520 4555 | 636 St Kilda Road | Level 3 | Melbourne | Victoria | 3004 | Australia | 1611.0 | 117300.0 |
| 119 | La Rochelle Gifts | Labrune | Janine | 40.67.8555 | 67, rue des Cinquante Otages | None | Nantes | None | 44000 | France | 1370.0 | 118200.0 |
| 121 | Baane Mini Imports | Bergulfsen | Jonas | 07-98 9555 | Erling Skakkes gate 78 | None | Stavern | None | 4110 | Norway | 1504.0 | 81700.0 |

### Step 4: Transform Data

We can now use SQL to perform our data transformations directly including things like handling duplicate and null values as well as performing analysis via grouping and aggregating.

```
# Remove duplicates  
c.execute('''DELETE FROM customers  
            WHERE customerNumber NOT IN (  
                SELECT MIN(customerNumber)  
                FROM customers  
                GROUP BY customerName, phone, city)  
        ''')
```

**Output:**

```
<sqlite3.Cursor at 0x11ec534c0>
```

```
# Update missing values  
c.execute('''UPDATE customers SET state = "N/A"   
            WHERE state IS NULL''')
```

**Output:**

```
<sqlite3.Cursor at 0x11ec534c0>
```

```
# Aggregate data  
c.execute('''SELECT city, AVG(creditLimit) AS avg_credit_limit  
             FROM customers  
             GROUP BY city''')  
  
# Fetch the transformed data  
transformed_data = c.fetchall()  
transformed_data[0:10]
```

**Output:**

```
[('Aachen', 0.0),  
 ('Allentown', 100600.0),  
 ('Amsterdam', 0.0),  
 ('Auckland', 77700.0),  
 ('Auckland  ', 99000.0),  
 ('Barcelona', 60300.0),  
 ('Bergamo', 119600.0),  
 ('Bergen', 96800.0),  
 ('Berlin', 0.0),  
 ('Bern', 0.0)]
```

```
# Sanity Check with Pandas  
pd.read_sql('''SELECT city, AVG(creditLimit) AS avg_credit_limit  
             FROM customers  
             GROUP BY city''', conn)
```

**Output:**

SQL Data Set: City and Average Credit Limit

| Index | City | Average Credit Limit |
| --- | --- | --- |
| 0 | Aachen | 0.0 |
| 1 | Allentown | 100600.0 |
| 2 | Amsterdam | 0.0 |
| 3 | Auckland | 77700.0 |
| 4 | Auckland | 99000.0 |
| ... | ... | ... |
| 91 | Versailles | 77900.0 |
| 92 | Warszawa | 0.0 |
| 93 | Wellington | 86800.0 |
| 94 | White Plains | 102700.0 |
| 95 | Århus | 120800.0 |

96 rows × 2 columns

### Step 5: Serve Data

Need to make sure we commit and save our changes via the open connection object.

```
# Save and then close  
conn.commit()  
conn.close()
```

The final step would be to formulate a way to allow external access to this data. The simplest form would be to just publish a static table or visual, or send to the parties that need it. However there are much more advanced ways to serve data through the use of web API's, dashboarding tools, and deployment libraries. While we won't cover those here just know that there are a plethora of methods to 'serve' data and the method used highly depends on the use case of the data.

### Explanation of the Pseudocode

1. We use pandas to read the CSV file customer\_data.csv into a DataFrame called df.
2. We create a connection to a SQLite database named customer\_database.db using sqlite3. We also create a table named customers to store the customer data.
3. We use the to\_sql() function from pandas to load the data from the DataFrame into the customers table in the database. The if\_exists='replace' parameter ensures that the table is replaced if it already exists.
4. We perform data transformations using SQL queries:  
   * Remove duplicates: We use a DELETE statement with a subquery to remove duplicate rows based on the combination of columns.
   * Update missing values: We use an UPDATE statement to set the state to ‘N/A’ for rows where state is NULL.
   * Aggregate data: We use a SELECT statement with AVG() aggregate function and GROUP BY clause to calculate the average credit limit for each city.
   * We fetch the transformed data using c.fetchall() and store it in the transformed\_data variable.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243942

Scraped At: 2026-05-14T21:22:48.100819
