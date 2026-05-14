# Technical Lesson Part 2: Filtering Data with SQL

# Technical Lesson Part 2: Filtering Data with SQL

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Technical Lesson Part 2: Filtering Data with SQL

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

### Video: Lesson Walkthrough

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of filtering data with SQL.

**Note:** This walkthrough video applies to both parts of the Technical Lesson.

Use the `data.sqlite` file and the `pets_database.db` with the Python notebook `SQLM2P1.ipynb` in the **[Drive


Links to an external site.](https://drive.google.com/drive/folders/1a1CMVmU1e46DcuosXgr21f2f8VgDPC0T)**.

[VIDEO LINK](https://player.vimeo.com/video/1001740304?h=4c5f33772b)

### Instructions

Now, we'll walk through executing a handful of common and handy SQL queries that use WHERE with conditional operators. We'll start with an example of what this type of query looks like, then type a query specifically related to the cats table.

For this section as the queries get more advanced we'll be using a simpler database called pets\_database.db containing a table called cats.

The cats table is populated with the following data:

Cats Table Dataset

| id | name | age | breed | owner\_id |
| --- | --- | --- | --- | --- |
| 1 | Maru | 3.0 | Scottish Fold | 1.0 |
| 2 | Hana | 1.0 | Tabby | 1.0 |
| 3 | Lil' Bub | 5.0 | American Shorthair | NaN |
| 4 | Moe | 10.0 | Tabby | NaN |
| 5 | Patches | 2.0 | Calico | NaN |
| 6 | None | NaN | Tabby | NaN |

Below we make a new database connection and read all of the data from this table:

```
conn = sqlite3.connect('pets_database.db')  
cursor = conn.cursor()  
pd.read_sql("SELECT * FROM cats;", conn)
```

**Output:**

Data Output using read\_sql

| # | id | name | age | breed | owner\_id |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | Maru | 3.0 | Scottish Fold | 1.0 |
| 1 | 2 | Hana | 1.0 | Tabby | 1.0 |
| 2 | 3 | Lil' Bub | 5.0 | American Shorthair | NaN |
| 3 | 4 | Moe | 10.0 | Tabby | NaN |
| 4 | 5 | Patches | 2.0 | Calico | NaN |
| 5 | 6 | None | NaN | Tabby | NaN |

### Step 1: WHERE with >=

For the =, !=, <, <=, >, and >= operators, the query looks like:

```
SELECT column/s  
 FROM table_name  
WHERE <column_name> <operator> <value>;
```

**Note:** The example above is not valid SQL, it is a template for how the queries are constructed.

We type the SQL query between the quotes to select all cats who are at least 5 years old:

```
pd.read_sql("""  
SELECT *  
 FROM cats  
WHERE age >= 5;  
""", conn)
```

This should return:

SQL query output: cats at least 5 y.o.

| id | name | age | breed | owner\_id |
| --- | --- | --- | --- | --- |
| 3 | Lil' Bub | 5.0 | American Shorthair | None |
| 4 | Moe | 10.0 | Tabby | None |

### Step 2: WHERE with BETWEEN

If we wanted to select all rows with values in a range, we could do this by combining the <= and AND operators. However, since this is such a common task in SQL, there is a shorter and more efficient command specifically for this purpose, called BETWEEN.

A typical query with BETWEEN looks like:

```
SELECT column_name(s)  
  FROM table_name  
 WHERE column_name BETWEEN value1 AND value2;
```

Note that BETWEEN is an inclusive range, so the returned values can match the boundary values (not like range() in Python).

Let's say we need to select the names of all of the cats whose age is between 1 and 3. We'll type the SQL query between the quotes below to select all cats who are in this age range:

```
pd.read_sql("""  
SELECT *  
  FROM cats  
 WHERE age BETWEEN 1 AND 3;  
""", conn)
```

This should return:

SQL query: cats 1-3 y.o.

| id | name | age | breed | owner\_id |
| --- | --- | --- | --- | --- |
| 1 | Maru | 3.0 | Scottish Fold | 1.0 |
| 2 | Hana | 1.0 | Tabby | 1.0 |
| 3 | Patches | 2.0 | Calico | NaN |

### Step 3: WHERE Column Is Not NULL

NULL in SQL represents missing data. It is similar to None in Python or NaN in NumPy or pandas. However, we use the IS operator to check if something is NULL, not the = operator (or IS NOT instead of !=).

To check if a value is NULL (or not), the query looks like:

```
SELECT column(s)  
  FROM table_name  
 WHERE column_name IS (NOT) NULL;
```

You might have noticed when we selected all rows of cats, some owner IDs were NaN, then in the above query they are None instead. This is a subtle difference where Python/pandas is converting SQL NULL values to NaN when there are numbers in other rows, and converting to None when all of the returned values are NULL. This is a subtle difference that you don't need to memorize; it is just highlighted to demonstrate that the operators we use in SQL are similar to Python operators, but not quite the same.

If we want to select all cats that don't currently belong to an owner, we want to select all cats where the owner\_id is NULL.

We'll type the SQL query between the quotes below to select all cats that don't currently belong to an owner:

```
pd.read_sql("""  
SELECT *  
  FROM cats  
WHERE owner_id IS NULL;  
""", conn)
```

This should return:

SQL query: cats without owner

| id | name | age | breed | owner\_id |
| --- | --- | --- | --- | --- |
| 3 | Lil' Bub | 5.0 | American Shorthair | None |
| 4 | Moe | 10.0 | Tabby | None |
| 5 | Patches | 2.0 | Calico | None |
| 6 | None | NaN | Tabby | None |

### Step 4: WHERE with LIKE

The LIKE operator is very helpful for writing SQL queries with messy data. It uses wildcards to specify which parts of the string query need to be an exact match and which parts can be variable.

When using LIKE, a query looks like:

```
SELECT column(s)  
  FROM table_name  
 WHERE column_name LIKE 'string_with_wildcards';
```

The most common wildcard you'll see is %. This is similar to the \* wildcard in Bash or regex: it means zero or more characters with any value can be in that position.

So for example, if we want all cats with names that start with "M", we could use a query containing M%. This means that we're looking for matches that start with one character "M" (or "m", since this is a case-insensitive query in SQLite) and then zero or more characters that can have any value.

We'll type the SQL query between the quotes below to select all cats with names that start with "M" (or "m"):

```
pd.read_sql("""  
SELECT *  
  FROM cats  
 WHERE name LIKE 'M%';  
""", conn)
```

This should return:

SQL query: cat names starting with "M"

| id | name | age | breed | owner\_id |
| --- | --- | --- | --- | --- |
| 1 | Maru | 3.0 | Scottish Fold | 1.0 |
| 4 | Moe | 10.0 | Tabby | NaN |

Note that we also could have used the substr SQL built-in function here to perform the same task:

```
pd.read_sql("""  
SELECT *  
  FROM cats  
 WHERE substr(name, 1, 1) = "M";  
""", conn)
```

Unlike in Python where:

> **There should be one-- and preferably only one --obvious way to do it. (Zen of Python)**

There will often be multiple valid approaches to writing the same SQL query. Sometimes one will be more efficient than the other, and sometimes the only difference will be a matter of preference.

The other wildcard used for comparing strings is \_, which means exactly one character, with any value.

For example, if we wanted to select all cats with four-letter names where the second letter was "a", we could use \_a\_\_.

We'll type the SQL query between the quotes below to select all cats with names where the second letter is "a" and the name is four letters long:

```
pd.read_sql("""  
SELECT *  
  FROM cats  
 WHERE name LIKE '_a__';  
""", conn)
```

This should return:

SQL query: cats with 2nd letter "a" in name

| id | name | age | breed | owner\_id |
| --- | --- | --- | --- | --- |
| 1 | Maru | 3 | Scottish Fold | 1 |
| 2 | Hana | 1 | Tabby | 1 |

Again, we could have done this using length and substr, although it would be much less concise:

```
pd.read_sql("""  
SELECT *  
  FROM cats  
 WHERE length(name) = 4 AND substr(name, 2, 1) = "a";  
""", conn)
```

These examples are a bit silly, but you can imagine how this technique would help to write queries between multiple datasets where the names don't quite match exactly. You can combine % and \_ in your string to narrow and expand your query results as needed.

### Step 5: Filter and Aggregate

Now, let's talk about the SQL aggregate function COUNT.

SQL aggregate functions are SQL statements that can get the average of a column's values, retrieve the minimum and maximum values from a column, sum values in a column, or count a number of records that meet certain conditions. You can learn more about these SQL aggregators here and here.

For now, we'll just focus on COUNT, which counts the number of records that meet a certain condition. Here's a standard SQL query using COUNT:

```
SELECT COUNT(column_name)  
  FROM table_name  
 WHERE conditional_statement;
```

Let's try it out and count the number of cats who have an owner\_id of 1. We'll type the SQL query between the quotes below:

```
pd.read_sql("""  
SELECT COUNT(owner_id)  
  FROM cats  
 WHERE owner_id = 1;  
""", conn)
```

This should return:

SQL Query: cats with owner\_id of 1

| # | COUNT(owner\_id) |
| --- | --- |
| 0 | 2 |

```
 conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243708

Scraped At: 2026-05-14T21:09:08.005519
