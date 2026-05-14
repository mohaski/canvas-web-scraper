# What is Selecting Data with SQL?

# What is Selecting Data with SQL?

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) What is Selecting Data with SQL?

Icon Progress Bar (browser only)

9 min read

Here are some key terms to know about selecting data with SQL:

* **SQL (Structured Query Language)**: The computer language used for getting data into and out of databases
* **Query**: The set of coded instructions for accessing data in a database
* **Database**: an organized collection of structured information, or data, typically stored electronically in a computer system. Databases come in many different ‘flavors’ like:  
  + **Relational**: The main type of database we will be starting off with. This stores creates and discovers relationships between tables in a database.
  + **NoSQL Databases:** These databases are designed to handle a wide variety of data models, including key-value, document, column-family, and graph formats. They are particularly useful for handling large sets of distributed data and are known for their flexibility, scalability, and performance in handling unstructured data.
  + **Object-Oriented Databases:** These databases store data in the form of objects, as used in object-oriented programming. They are designed to work well with object-oriented programming languages, providing a seamless integration between the application and the database.
  + **Graph Databases:** Designed specifically to handle relationships between data points, graph databases store entities as nodes and the relationships between them as edges. They excel in scenarios where relationships are as important as the data itself, such as social networks, fraud detection, and recommendation systems.
  + **Time Series Databases:** These are optimized for handling time-stamped data, such as logs, sensor data, and other time-based information. They are built to efficiently collect, store, and query sequences of data over time, making them ideal for monitoring, real-time analytics, and Internet of Things (IoT) applications. Examples include InfluxDB and TimescaleDB.
* **Table:** The basic organizational unit of a database is called a table, and databases contain one or more tables. Tables can be thought of as individual spreadsheets within a workbook.
* **Entity Relationship Diagram (ERD):** A visual representation of the relationships among the tables of a database.
* **Schema:** A formal definition that describes the organization of data in a database. It serves as a blueprint that outlines how the database is structured, including the tables, the fields within those tables, and the relationships between those tables.

### How Does Selecting Data with SQL Work?

### [The Structure of SQL Databases](#dpPanel0)

A SQL database is a high-level container holding one or more tables. The database can be a continuously-running server that receives requests and returns responses (MySQL, PostgreSQL) or it can be a specially-formatted file on disk (SQLite). We will primarily use SQLite in these lessons because it is lightweight and portable (and therefore useful for educational purposes), but it's important to know that other more "heavy duty" types of databases are available and used more often in industry settings.

A SQL table contains tabular data (data stored in rows and columns), similar to a CSV. Every table has a defined set of columns, and then we store any number of what we refer to as 'records' as rows in our database. A record is just information referring to one specific entity. For instance, if you had a table called "people" you could imagine a structure like this:

SQL table example with information about people

| id | name | age | email |
| --- | --- | --- | --- |
| 1 | Bob | 29 | bob@flatironschool.com |
| 2 | James | 28 | james@flatironschool.com |
| 3 | John | 28 | john@flatironschool.com |

Each column has a name, and each row contains the corresponding information about a person. Unlike a CSV, a SQL table can also enforce the data types of the columns, which are described in the table schema. The schema for this table might look something like this:

```
CREATE TABLE people (  
  id INTEGER PRIMARY KEY,  
  name TEXT,  
  age INTEGER,  
  email TEXT  
);
```

### [Connecting to and Querying SQL Databases](#dpPanel1)

As a data scientist, your primary use case of SQL will be querying data stored within databases. To do this, you connect to the database with some sort of tool.

* Most SQL databases have an associated command-line interface where you can write SQL queries without any additional languages or tools. For SQLite, this is called sqlite3 ([SQLite documentation


  Links to an external site.](https://sqlite.org/cli.html)).
* You can also connect through a different coding language such as Python. For SQLite, the Python module is called sqlite3 ([Python and SQLite documentation


  Links to an external site.](https://docs.python.org/3/library/sqlite3.html)).   
  + Yes, the command-line interface and Python module have the same name.
* One other approach is using a GUI ([graphical user interface SQLite browser


  Links to an external site.](https://sqlitebrowser.org/)) tool. For SQLite, a good one is DB Browser for SQLite ().

Once you're connected to the database, you can then read, write, update, and delete data from its tables. These commands are called queries and are written using the SQL language.

Similar to other kinds of file permissions, you might only have the ability to perform some of these actions but not others. For example, you might be able to read information from the database but not delete information.

To retrieve data from one or more tables you usually use a **SELECT statement** in your query. A simple query would look something like this:

```
SELECT col1, col2, col3  
FROM table  
WHERE records match criteria  
LIMIT 100;
```

Don't worry if this is confusing now, you'll soon learn what each line does. For now, just notice that:

* Queries start with the SELECT clause, followed by what you want to select. If selecting multiple columns, you separate them with a comma.
* Then you specify where that data is being retrieved from the using the FROM clause followed by the table name.
* Afterward, you can provide conditions such as filters or limits on the amount of data returned.

### [Relational Data](#dpPanel2)

Also unlike a CSV, a SQL database can contain multiple related SQL tables. To demonstrate, here is an outline of a database structure:

This kind of diagram is called an **entity relationship diagram (ERD)** because it shows the relationships between tables. It does not give us any information about the specific data stored in the database, but rather the metadata.

[![Entity-Relationship-Diagram](https://moringa.instructure.com/courses/1406/files/625425/preview)](https://moringa.instructure.com/courses/1406/files/625425/preview "Entity-Relationship-Diagram")

In the diagram, each rectangle is a table, with the table name listed at the top. In this case, we have 8 tables:

1. productlines
2. products
3. orderdetails
4. employees
5. offices
6. customers
7. orders
8. payments

Below each of the table names, we have a list of the various column names associated with that table. So for example, the productlines table has four columns: productLine, textDescription, htmlDescription and image.

In addition to the names of the tables and their column names, we have an indication of relationships. For example, data in the employees table has some relationship to data on the offices table, indicating that an employee may be associated with a specific office location. Likewise, certain orders are associated with certain customers. Lots of real world data is inherently related. For example, students have an association to a course, or ingredients are related to a recipe.

### [Primary Keys and Foreign Keys](#dpPanel3)

You may also note that some of these column names are preceded by an asterix (\*). This indicates that this is the primary key for the table. A primary key is a unique identifier for a table. That is, there can only be unique values for this column entry. lastName would not be a good choice for a primary key as it's common for people to have the same last names or even firstName + lastName pairings. For this reason it is typical for a primary key to have a name reflecting some kind of "number", "code", or "id" — something that is truly unique to that record, which may or may not have any meaning beyond the database itself.

If you look closely, you'll see that the columns that are the primary key for one table can also appear on other tables. This is known as a foreign key aka the primary key from a different ("foreign") table. This is the core idea of how data on different tables is associated in a relational database. If you were told a specific customerNumber, and then given a list of order data that included the customerNumber, you could determine which orders were placed by that customer by matching up the primary and foreign keys.

The lines, circles, arrows, and tick marks are showing different categorizations on exactly how this data is linked.

### Summary

In this lesson, you got a quick overview of what SQL is and saw an example SQL SELECT query and ERD. Remember that there are multiple SQL dialects all with particular differences, but the overall language is generally fairly similar and interchangeable. You also learned that knowledge of SQL is important for job interviews since data retrieval is a foundational part of the data science process.

### Conceptualization: Selecting Data with SQL

Selecting Data with SQL terms defined with use cases

| Term | Definition | Use Case |
| --- | --- | --- |
| Relational | The main type of database we will be starting off with. This stores creates and discovers relationships between tables in a database. | Relational databases are suitable for structured data with well-defined relationships, such as financial records, customer information, and inventory management systems. |
| NoSQL Databases | These databases are designed to handle a wide variety of data models, including key-value, document, column-family, and graph formats. They are particularly useful for handling large sets of distributed data and are known for their flexibility, scalability, and performance in handling unstructured data. | NoSQL databases are ideal for handling unstructured or semi-structured data, such as social media data, web analytics, content management systems, and real-time web applications. |
| Object-Oriented Databases | These databases store data in the form of objects, as used in object-oriented programming. They are designed to work well with object-oriented programming languages, providing a seamless integration between the application and the database. | Object-oriented databases are useful in complex software systems where data is tightly coupled with the application logic, such as computer-aided design (CAD) systems, multimedia applications, and telecommunications. |
| Graph Databases | Designed specifically to handle relationships between data points, graph databases store entities as nodes and the relationships between them as edges. They excel in scenarios where relationships are as important as the data itself, such as social networks, fraud detection, and recommendation systems. | Graph databases are well-suited for applications that heavily rely on complex relationships between data points, such as social networks, fraud detection systems, recommendation engines, and knowledge graph management. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243690

Scraped At: 2026-05-14T21:06:57.264281
