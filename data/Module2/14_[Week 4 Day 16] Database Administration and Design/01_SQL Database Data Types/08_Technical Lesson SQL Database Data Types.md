# Technical Lesson: SQL Database Data Types

# Technical Lesson: SQL Database Data Types

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Technical Lesson: SQL Database Data Types

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

We can imagine a scenario where we work for a modest sized pet store chain and the database administrator is on vacation, but our manager tells us that we need to create a database, and it needs to be created today. Even though wea re a data scientist, we have enough knowledge about database administration to create a database.

Recall that the first step is to construct a brand new database to serve as a storage house for our information. Then, we know that we are supposed to create tables within this database, each one designed to hold a specific category of data. Once these tables are carefully designed, we can then populate them with rows of data. We want the database to be robust so as the data evolves and changes, we can modify existing entries to keep them accurate or remove outdated information entirely. Throughout this process, we know that we must not forget to commit changes, where committing changes means finalizing the updates we’ve made to the database, ensuring that they are permanently stored. Two of the key challenges in this process are using the correct code and properly identifying each type of data.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of SQL database data types.

[VIDEO LINK](https://player.vimeo.com/video/1009314954?h=b987b8e6a7)

### Instructions

#### [Step 1: Previewing Files in the Current Working Directory](#dpPanel0)

Remember that we can use the bash ls command to preview files and folders in the current working directory. We'll run the cell below to do just that. Note: Your working directory will likely look different.

```
!ls  
  
CONTRIBUTING.md  LICENSE.md       README.md        index.ipynb
```

**Output:**

`![Potential appearance of output depending on where the file is run.](https://moringa.instructure.com/courses/1406/files/625397/download)`

#### [Step 2: Creating a Database](#dpPanel1)

You've seen how to connect to a database, but did you know creating one is just as easy? All we have to do is create a connection to a non-existent database, and viola! The database will be created simply by establishing a connection.

Use the `pets_database.db` file with the Python notebook `SQLM5P1.ipynb` in the **[Drive


Links to an external site.](https://drive.google.com/drive/folders/12SoibkQ6-Gm-FyxM4hEvDzYxItl-3bsL)**.

```
import sqlite3   
conn = sqlite3.connect('pets_database.db')  
cur = conn.cursor()
```

##### Re-preview Files

If we use the ls command once again, we should now see the pets\_database.db file.

```
!ls  
  
CONTRIBUTING.md   README.md         pets_database.db  
LICENSE.md        index.ipynb
```

**Output:**

[![Potential output appearance depending on where the file is being run.](https://moringa.instructure.com/courses/1406/files/625381/download)](https://moringa.instructure.com/courses/1406/files/625381/download "Potential output appearance depending on where the file is being run.")

#### [Step 3: Creating Tables](#dpPanel2)

Now that we have a database, let's create our cats table along with columns for id, name, age, and breed. Remember that we use our cursor to execute these SQL statements, and that the statements must be wrapped in quotes ('''SQL statement goes here''' or """SQL statement goes here"""). Indenting portions of our queries can also make them much easier to read and debug.

```
#Creating the cats table  
cur.execute("""CREATE TABLE cats (  
                                id INTEGER PRIMARY KEY,  
                                name TEXT,  
                                age INTEGER,  
                                breed TEXT )            
            """)
```

#### [Step 4: Populating Tables](#dpPanel3)

In order to populate a table, we can use the INSERT INTO command, followed by the name of the table to which we want to add data. Then, in parentheses, we type the column names that we want to fill with data. This is followed by the VALUES keyword, which is accompanied by a parentheses enclosed list of the values that correspond to each column name.

**Important:** Note that we don't have to specify the "id" column name or value. Primary Key columns are auto-incrementing. Therefore, since the cats table has an "id" column whose type is INTEGER PRIMARY KEY, we don't have to specify the id column values when we insert data. As long as we have defined an id column with a data type of INTEGER PRIMARY KEY, a newly inserted row's id column will be automatically given the correct value.

A boilerplate INSERT INTO statement looks like this:

```
cur.execute('''INSERT INTO [table name] [(column1, columnN, ...)]  
                   VALUES [(value1, valueN, ...)]  
           ''')
```

Okay, let's start storing some data about different cats!

To insert a record with values, we type the following:

```
# insert Cats into the pet_database.db here  
cur.execute('''INSERT INTO cats (name, age, breed)  
                 VALUES ('Maru', 3, 'Scottish Fold'),  
                        ('Hannah', 5, 'Persian'),  
                        ('Bob', 7, 'Tabby'),  
                        ('Little Bub', 10, 'Maine Coon');  
           ''')
```

#### [Step 5: Changing a Table](#dpPanel4)

##### Altering a table

We can add new columns to an existing table like this:

```
cur.execute('''ALTER TABLE table_name   
ADD COLUMN column_name column_type;  
            ''')
```

##### Updating a Table

We use UPDATE keyword to change pre-existing rows within a table.

The UPDATE statement uses a WHERE clause to grab the row we want to update. It identifies the table name we are looking in and resets the data in a particular column to a new value.

A boilerplate UPDATE statement looks like this:

```
cur.execute('''UPDATE [table name]   
                  SET [column name] = [new value]  
                  WHERE [column name] = [value];  
            ''')
```

Let's update one of our cats. Turns out Maru's friend Hannah is actually Maru's friend Hana. Let's update that row to change the name to the correct spelling:

```
cur.execute('''UPDATE cats SET name = "Hana" WHERE name = "Hannah";''')  
  
# update hannah here  
cur.execute('''UPDATE cats SET name = "Hana" WHERE name = "Hannah";''')
```

#### [Step 6: Deleting Data](#dpPanel5)

We use the DELETE keyword to delete table rows.

Similar to the UPDATE keyword, the DELETE keyword uses a WHERE clause to select rows.

A boilerplate DELETE statement looks like this:

```
cur.execute('''DELETE FROM [table name] WHERE [column name] = [value];''')
```

Let's go ahead and delete Little Bub from our cats table (sorry big guy).

```
# DELETE record with name or id here  
cur.execute('''DELETE FROM cats  
                 WHERE name = 'Little Bub';  
           ''')
```

Notice that this time we selected the row to delete using the PRIMARY KEY column. Remember that every table row has a PRIMARY KEY column that is unique. Lil' Bub was the second row in the database and thus had an id of 2.

#### [Step 7: Saving Changes](#dpPanel6)

While everything may look well and good, if we were to connect to the database from another Jupyter notebook (or elsewhere) the database would appear blank! That is, while the changes are reflected in our current session connection to the database we have yet to commit those changes to the master database so that other users and connections can also view the updates.

Before we commit the changes, let's demonstrate this concept.

First, preview the results of the table:

```
#Preview the table via the current cursor/connection  
cur.execute("""SELECT * FROM cats;""").fetchall()
```

**Output:**

```
[(1, 'Maru', 3, 'Scottish Fold'),  
 (2, 'Hana', 5, 'Persian'),  
 (3, 'Bob', 7, 'Tabby')]
```

Now, to demonstrate that these changes aren't reflected to other connections to the database, we'll create a 2nd connection/cursor and run the same preview:

```
#Preview the table via a second current cursor/connection   
#Don't overwrite the previous connection: you'll lose all of your work!  
conn2 = sqlite3.connect('pets_database.db')  
cur2 = conn2.cursor()  
cur2.execute("""SELECT * FROM cats;""").fetchall()  
  
[]
```

As you can see, the second connection doesn't currently display any data in the cats table! To make the changes universally accessible, commit the changes.

In this case:

```
# Commit our changes to the databaase  
conn.commit()  
  
#Close connection  
conn.close()
```

Now, if we reload our second connection, we should see the updates reflected in the data.

```
#Preview the table via a reloaded second current cursor/connection   
conn2 = sqlite3.connect('pets_database.db')  
cur2 = conn2.cursor()  
cur2.execute("""SELECT * FROM cats;""").fetchall()
```

**Output:**

```
[(1, 'Maru', 3, 'Scottish Fold'),  
 (2, 'Hana', 5, 'Persian'),  
 (3, 'Bob', 7, 'Tabby')]
```

### Considerations

When a data scientist delves into basic database administration tasks, several challenges or common issues may arise:

* **Understanding SQL Syntax and Commands:** Data scientists often have a strong foundation in analytical skills, but may not be as familiar with the nuances of SQL syntax and commands. For instance, executing SQL statements like CREATE TABLE, INSERT INTO, UPDATE, and DELETE might seem straightforward, but ensuring correct syntax, understanding the implications of each command, and avoiding syntax errors can be challenging, especially when dealing with more complex queries.
* **Data Integrity and Constraints:** When creating or altering tables, data scientists must be cautious about maintaining data integrity. Issues can arise when defining primary keys, foreign keys, and ensuring that the correct data types are used for each column. For example, setting up auto-incrementing primary keys or managing relationships between tables requires careful planning to prevent data inconsistencies.
* **Transaction Management and Persistence:** A common pitfall is forgetting to commit changes to the database after performing operations like inserts, updates, or deletions. Without a commit statement, changes made during the session may not be saved, leading to confusion when the database appears unchanged upon reconnecting. Understanding transaction management, including when and how to commit changes, is crucial for ensuring that the database remains consistent and that all operations are properly recorded.

These challenges highlight the importance of a solid understanding of SQL and database management principles, even for data scientists who may primarily focus on data analysis and modeling.

However, this combination requires careful consideration of the challenges and trade-offs involved, including performance optimization, data integrity, and managing workflow complexity. By making informed choices, you can harness the full potential of SQL and Pandas to achieve superior analytical outcomes.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243868

Scraped At: 2026-05-14T21:17:56.817191
