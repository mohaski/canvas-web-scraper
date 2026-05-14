# What are SQL Database Data Types?

# What are SQL Database Data Types?

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) What are SQL Database Data Types?

Icon Progress Bar (browser only)

4 min read

In SQL databases, data types define the kind of data that can be stored in each column of a table. Text is used for storing character strings, such as words or sentences, and can vary in length. Integer is used for storing whole numbers, both positive and negative, without any fractional component. Real is for storing floating-point numbers, which are numbers that can have a decimal point, representing fractions as well as whole numbers. Blob (Binary Large Object) is used for storing large binary data, such as images, videos, or any other multimedia content, in its raw format. These data types help ensure data integrity and optimize storage efficiency in SQL databases.

Let’s look at each of these in more detail.

### TEXT

Any alphanumeric characters which you want to represent as plain text. The body of this paragraph is text. Your name is text. Your email address is a piece of text. Your height, weight, and age, however, are probably not.

If you have meaningful leading zeroes (e.g. 02134, which you don't want to treat as equivalent to 2134), then it's better to store it as text.

This SQL data type roughly corresponds to the str data type in Python.

### INTEGER

Anything you want to represent as a whole number. If it's a number and contains no letter or special characters or decimal points then you should store it as an integer. If you use it to perform math or create a comparison between two different rows in our database, then you definitely want to store it as an integer.  
If it's a number that doesn't represent a quantity (e.g. an ID number or zip code), it depends on the context whether you should store it as an integer. You might never add two house address numbers together, but you might want to sort them numerically.

This SQL data type roughly corresponds to the int data type in Python.

### REAL

Anything that's a plain old decimal like 1.3 or 2.25. SQLite will store decimals up to 15 characters long. You can store 1.2345678912345 or 1234.5678912345, but 1.23456789123456789 would only store 1.2345678912345. In other database systems this is called 'double precision.'

This SQL data type roughly corresponds to the float data type in Python.

### BLOB

You may encounter the BLOB data type while you're Googling or doing any further reading on SQLite. For now, you will not use BLOB. It stands for "binary large object" and is generally used for holding binary data such as images or audio files. When we use those kinds of files in this course, we will generally just store them using the computer's file storage system (hard drive), rather than using databases.

### How Do SQL Database Data Types Work?

#### SQLite and Other SQL Implementations

To increase its compatibility with other database engines (e.g. mySQL or PostgreSQL), SQLite allows the programmer to use other common data types outside of the four mentioned above. This is why we are referring to TEXT, INTEGER, REAL, and BLOB as data type "categories". All other common data types are lumped into one of the four existing data types recognized by SQLite.

For example, INT is a common data type used outside of SQLite. SQLite won't complain if you define a column as an INT data type. It will simply lump it into the INTEGER category and store it as such. Similarly, if something is declared as VARCHAR, SQLite will treat it as TEXT.

To accommodate this, SQLite has a pretty complicated system of categorizing data types that involves Storage Classes, Type Affinities, and Datatypes. There is also a fifth data type category called NUMERIC that can actually contain any of TEXT, INTEGER, REAL, and BLOB types. This one mainly comes up for Python developers when you are working with BOOLEAN data (like True or False in Python), which becomes a NUMERIC column containing 0s and 1s rather than some separate boolean data type.

For a deeper dive, check out the [SQLite3 Documentation on Datatypes


Links to an external site.](http://www.sqlite.org/datatype3.html).

### Conceptualization: SQL Database Data Types

SQL Database Data Types with Examples

| Data Type | SQL Code | Example |
| --- | --- | --- |
| Text | VARCHAR(50) | ‘John Doe' |
| Text | TEXT | ‘This is a long text field that can store up to 65,535 characters.' |
| Integer | INT | 42 |
| Integer | BIGINT | 9223372036854775807 |
| Real | DECIMAL(10.2) | 3.14 |
| Real | FLOAT | 3.141592 |
| Binary (Blob) | BLOB | 0x504446 |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243861

Scraped At: 2026-05-14T21:17:21.843326
