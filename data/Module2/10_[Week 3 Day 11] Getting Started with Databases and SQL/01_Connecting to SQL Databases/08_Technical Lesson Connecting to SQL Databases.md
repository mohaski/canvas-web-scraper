# Technical Lesson: Connecting to SQL Databases

# Technical Lesson: Connecting to SQL Databases

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Technical Lesson: Connecting to SQL Databases

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

Now that you've gotten a brief introduction to SQL, it's time to go over connecting to a database and executing some queries. In this section, we will connect to a SQLite (one of the flavors of SQL databases) database using several methods. Databases seldom have easy direct interfaces with the scripting language we are planning to use, so we need some way to connect to those databases for analysis.

It is very rare that the data you’ll want to use lives in a flat csv file or spreadsheet. More likely, there will be a database file somewhere on the computer, a database existing somewhere on the network, or in the cloud. So, as data scientists, we need to be able to connect to these databases in a number of ways.

In this technical lesson, we will walk through how to:

1. Connect to a SQLite database through the sqlite3 Python library.
2. View information about database tables and column names.
3. Retrieve all information from a SQL table.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of connecting to SQL databases.

[VIDEO LINK](https://player.vimeo.com/video/1024509103?h=0096b4ae8a)

### Instructions

### Connecting to the Database

Use the `data.sqlite` file with the Python notebook `SQLM1P1.ipynb` in the **[Drive


Links to an external site.](https://drive.google.com/drive/folders/14cdZG7l8El7dOyDrmsWJFfE28KbXw79l)**.

We will use the sqlite3 module ([Python and SQLite3 documentation


Links to an external site.](https://docs.python.org/3/library/sqlite3.html)). This module works by opening a connection to the database with the sqlite3.connect() method:

```
import sqlite3   
conn = sqlite3.connect('data.sqlite')  
  
cur = conn.cursor()
```

We have created a connection object within our notebook and assigned it to ‘conn’. Let's continue and create a cursor so we can interact with connection.

A **cursor object** is what can actually execute SQL commands. You create it by calling .cursor() on the connection:`cur = conn.cursor()`

#### 1. Viewing the List of Tables

Let's use the cursor to find out what tables are contained in this database. This requires two steps:

1. Executing the query: .execute()
2. Fetching the results: .fetchone(), .fetchmany(), or .fetchall()

This is because some SQL commands (e.g. deleting data) do not require results to be fetched, just commands to be executed. So the interface only fetches the results if you ask for them.

```
# Execute the query  
  
# (This is a special query for finding the table names. You don't need to memorize it.)  
  
# SQLite databases all have a sqlite_master table that stores the schema information  
  
cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")  
  
# Fetch the result and store it in table_names  
  
table_names = cur.fetchall()  
  
table_names
```

```
[('orderdetails',),  
 ('payments',),  
 ('offices',),  
 ('customers',),  
 ('orders',),  
 ('productlines',),  
 ('products',),  
 ('employees',)]
```

#### 2. Selecting All Data from the offices Table

If we want to get all information about the offices table, we might do something like this (\* means all columns):

```
cur.execute("""SELECT * FROM offices;""")  
cur.fetchall()
```

```
[('1',  
  'San Francisco',  
  '+1 650 219 4782',  
  '100 Market Street',  
  'Suite 300',  
  'CA',  
  'USA',  
  '94080',  
  'NA'),  
 ('2',  
  'Boston',  
  '+1 215 837 0825',  
  '1550 Court Place',  
  'Suite 102',  
  'MA',  
  'USA',  
  '02107',  
  'NA'),  
 ('3',  
  'NYC',  
  '+1 212 555 3000',  
  '523 East 53rd Street',  
  'apt. 5A',  
  'NY',  
  'USA',  
  '10022',  
  'NA'),  
 ('4',  
  'Paris',  
  '+33 14 723 4404',  
  "43 Rue Jouffroy D'abbans",  
  '',  
  '',  
  'France',  
  '75017',  
  'EMEA'),  
 ('5',  
  'Tokyo',  
  '+81 33 224 5000',  
  '4-1 Kioicho',  
  '',  
  'Chiyoda-Ku',  
  'Japan',  
  '102-8578',  
  'Japan'),  
 ('6',  
  'Sydney',  
  '+61 2 9264 2451',  
  '5-11 Wentworth Avenue',  
  'Floor #2',  
  '',  
  'Australia',  
  'NSW 2010',  
  'APAC'),  
 ('7',  
  'London',  
  '+44 20 7877 2041',  
  '25 Old Broad Street',  
  'Level 7',  
  '',  
  'UK',  
  'EC2N 1HN',  
  'EMEA')]
```

Because .execute() returns the cursor object, it also possible to combine the previous two lines into one line, like so:

```
cur.execute("""SELECT * FROM offices;""").fetchall()
```

```
[('1',  
  'San Francisco',  
  '+1 650 219 4782',  
  '100 Market Street',  
  'Suite 300',  
  'CA',  
  'USA',  
  '94080',  
  'NA'),  
 ('2',  
  'Boston',  
  '+1 215 837 0825',  
  '1550 Court Place',  
  'Suite 102',  
  'MA',  
  'USA',  
  '02107',  
  'NA'),  
 ('3',  
  'NYC',  
  '+1 212 555 3000',  
  '523 East 53rd Street',  
  'apt. 5A',  
  'NY',  
  'USA',  
  '10022',  
  'NA'),  
 ('4',  
  'Paris',  
  '+33 14 723 4404',  
  "43 Rue Jouffroy D'abbans",  
  '',  
  '',  
  'France',  
  '75017',  
  'EMEA'),  
 ('5',  
  'Tokyo',  
  '+81 33 224 5000',  
  '4-1 Kioicho',  
  '',  
  'Chiyoda-Ku',  
  'Japan',  
  '102-8578',  
  'Japan'),  
 ('6',  
  'Sydney',  
  '+61 2 9264 2451',  
  '5-11 Wentworth Avenue',  
  'Floor #2',  
  '',  
  'Australia',  
  'NSW 2010',  
  'APAC'),  
 ('7',  
  'London',  
  '+44 20 7877 2041',  
  '25 Old Broad Street',  
  'Level 7',  
  '',  
  'UK',  
  'EC2N 1HN',  
  'EMEA')]
```

This data is useful, since it's a list of tuples rather than one giant string. If you wanted to select the phone number for the first office, for example, that would just be [0] [2] tacked on to the end of the previous Python statement.

#### 3. Viewing the Column Names from the offices Table

Information about the column names can be retrieved from the cursor. Since the most recent query was SELECT \* FROM offices; the cursor will contain information about the offices table:

```
cur.description
```

```
(('officeCode', None, None, None, None, None, None),  
 ('city', None, None, None, None, None, None),  
 ('phone', None, None, None, None, None, None),  
 ('addressLine1', None, None, None, None, None, None),  
 ('addressLine2', None, None, None, None, None, None),  
 ('state', None, None, None, None, None, None),  
 ('country', None, None, None, None, None, None),  
 ('postalCode', None, None, None, None, None, None),  
 ('territory', None, None, None, None, None, None))
```

If we wanted to combine the previous two steps together to make a dataframe with the right column names, that would look like this:

```
import pandas as pd  
  
pd.DataFrame(  
    data=cur.execute("""SELECT * FROM offices;""").fetchall(),  
    columns=[x[0] for x in cur.description]  
)
```

**Output:**

Data Output with SELECT column names

| # | officeCode | city | phone | addressLine1 | addressLine2 | state | country | postalCode | territory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | San Francisco | +1 650 219 4782 | 100 Market Street | Suite 300 | CA | USA | 94080 | NA |
| 1 | 2 | Boston | +1 215 837 0825 | 1550 Court Place | Suite 102 | MA | USA | 02107 | NA |
| 2 | 3 | NYC | +1 212 555 3000 | 523 East 53rd Street | apt. 5A | NY | USA | 10022 | NA |
| 3 | 4 | Paris | +33 14 723 4404 | 43 Rue Jouffroy D'abbans |  |  | France | 75017 | EMEA |
| 4 | 5 | Tokyo | +81 33 224 5000 | 4-1 Kioicho |  | Chiyoda-Ku | Japan | 102-8578 | Japan |
| 5 | 6 | Sydney | +61 2 9264 2451 | 5-11 Wentworth Avenue | Floor #2 |  | Australia | NSW 2010 | APAC |
| 6 | 7 | London | +44 20 7877 2041 | 25 Old Broad Street | Level 7 |  | UK | EC2N 1HN | EMEA |

### Disconnecting from the Database

Now that we have all of the information we need, we can close the connection to the database. It is always important to close out any connections when finished just like it is important to close any open files. We don’t want to accidentally manipulate/change/delete anything within the database.

```
conn.close()
```

### Connecting to a Database Using sqlite3 + pandas

This is the most straightforward technique for writing SQL queries within a Python context. We can skip over the use of the cursor via built-in pandas methods.

#### 4. Connecting to the Database

This is the same as the previous process, except you only need the connection, not the cursor. Pandas will read, execute, and fetch based on the provided query.

```
conn = sqlite3.connect("data.sqlite")
```

#### 5. Viewing the List of Tables

Now that we have the connection, we can use the pd.read\_sql method ([documentation here


Links to an external site.](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)). Instead of using the cursor, all you need is the connection variable and pandas will create a dataframe object based on the query:

```
df = pd.read_sql("""SELECT name FROM sqlite_master WHERE type = 'table';""", conn)  
df
```

List of Tables from query

| # | Name |
| --- | --- |
| 0 | orderdetails |
| 1 | payments |
| 2 | offices |
| 3 | customers |
| 4 | orders |
| 5 | productlines |
| 6 | products |
| 7 | employees |

```
type(df)  
pandas.core.frame.DataFrame
```

As you can see, this technique created a pandas dataframe as the result of the query, rather than a string or a collection of tuples. This tends to be very convenient for future analysis.

#### 6. Selecting All Data from the Offices Table and Viewing the Column Names from the Offices Table

Here we have combined two steps into one! pd.read\_sql automatically retrieves the relevant column names when you select data from a table.

```
pd.read_sql("SELECT * FROM offices;", conn)
```

Output of Query: Select Column Names

| # | officeCode | city | phone | addressLine1 | addressLine2 | state | country | postalCode | territory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | San Francisco | +1 650 219 4782 | 100 Market Street | Suite 300 | CA | USA | 94080 | NA |
| 1 | 2 | Boston | +1 215 837 0825 | 1550 Court Place | Suite 102 | MA | USA | 02107 | NA |
| 2 | 3 | NYC | +1 212 555 3000 | 523 East 53rd Street | apt. 5A | NY | USA | 10022 | NA |
| 3 | 4 | Paris | +33 14 723 4404 | 43 Rue Jouffroy D'abbans |  |  | France | 75017 | EMEA |
| 4 | 5 | Tokyo | +81 33 224 5000 | 4-1 Kioicho |  | Chiyoda-Ku | Japan | 102-8578 | Japan |
| 5 | 6 | Sydney | +61 2 9264 2451 | 5-11 Wentworth Avenue | Floor #2 |  | Australia | NSW 2010 | APAC |
| 6 | 7 | London | +44 20 7877 2041 | 25 Old Broad Street | Level 7 |  | UK | EC2N 1HN | EMEA |

It is still useful to be aware of the cursor construct in case you ever need to develop Python code that fetches one result at a time, or is a command other than SELECT. But in general if you know that the end result is creating a pandas dataframe to display the result, you don't really need to interface with the cursor directly.

#### 7. Disconnecting from the Database

This is the same as the process for using sqlite3 without pandas.

```
conn.close()
```

### Summary

#### Python sqlite3 Interface without pandas

Using Python to interface with SQL means that you can take advantage of your existing Python skills to craft a meaningful narrative with the results of a SQL query. The sqlite3 library is the simplest way to achieve this.  
If you ever need to use Python for tasks other than SELECT (e.g. inserting rows into a table), the sqlite3 library has flexible and powerful options available.

Two main downsides of using sqlite3 without pandas are the more-verbose syntax (i.e. you are writing more code, creating more opportunities to make a silly mistake) as well as the query result format (list of tuples). While a list of tuples is more usable than a long string, it can still be difficult to read, and navigating through the result requires numeric indexes rather than named labels like pandas has.

#### Python sqlite3 Interface with pandas

Adding pandas to sqlite3 means you can automatically display a table of query results in a tidy, visually-appealing way. You simply use pd.read\_sql and pass in a query string and a sqlite3 connection object.  
There are some tasks where pandas is not appropriate (e.g. inserting rows into a table), but in general it's the easiest approach for most tasks in this data science program.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243687

Scraped At: 2026-05-14T21:06:42.141793
