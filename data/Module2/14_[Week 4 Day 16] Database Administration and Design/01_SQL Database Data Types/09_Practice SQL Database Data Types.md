# Practice: SQL Database Data Types

# Practice: SQL Database Data Types

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: SQL Database Data Types

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

As an independent data science consultant tasked with designing and implementing a database for a school, your approach must balance practicality with strategic foresight. This task is not just about creating a database that functions correctly today, but about developing a system that will remain effective as the school grows and its needs evolve. The primary objective is to build a robust and flexible database that can seamlessly manage essential information, including student and staff contact details, academic records, class rosters, and attendance logs.

To achieve this, you'll need to carefully consider the structure and relationships of the data from the outset. The database should be normalized to avoid redundancy and ensure data integrity, which will make it easier to maintain, query, and scale in the future. The design process involves identifying the key entities (such as students, staff, courses, and grades) and mapping out how these entities will interact with one another within the database. This requires not only a strong understanding of the data itself but also foresight into how the data might need to be accessed, updated, and analyzed over time.

In this particular implementation, you are working within a Python environment, leveraging the `sqlite3` module to create and manipulate the database. SQLite is a powerful, lightweight, and self-contained SQL database engine that is well-suited for this task due to its simplicity and ease of integration with Python. It allows you to create a local database file (`school.sqlite`) that can be easily managed and queried directly from your Python scripts.

The process begins with setting up the database file and establishing a connection to it. This is followed by designing the schema, which involves creating tables to represent the different entities within the school’s ecosystem. Each table must be carefully structured with appropriate columns and data types to capture the necessary information. For instance, the `contactInfo` table should include columns for first names, last names, roles (indicating whether the person is a student or staff member), and address details. Each entry in the table is uniquely identified by a primary key, ensuring that records can be accurately referenced and related across different tables.

As you proceed with populating the tables, it's crucial to write efficient and secure SQL queries to insert, update, and retrieve data. This process often involves iterating over datasets (like lists of dictionaries) and carefully formatting SQL commands to prevent errors such as SQL injection or data corruption. Additionally, you must implement measures to handle potential issues, such as duplicate records or the need for data updates, ensuring the database remains accurate and reliable.

Beyond the immediate implementation, it's essential to keep in mind the future needs of the school. This includes designing the database to accommodate new features, such as additional tables for attendance tracking or extracurricular activities, and ensuring that it can handle increasing data volume as the school grows. Moreover, the database should be structured in a way that allows for easy integration with other systems, such as learning management systems or student information systems, which may be added in the future.

In summary, your role as a data science consultant involves not only the technical creation of the database but also strategic planning to ensure the system is scalable, secure, and able to meet the long-term needs of the school. By carefully designing the database schema, implementing best practices in SQL, and considering future expansions, you will create a robust foundation that supports the school’s operational and analytical requirements.

### Resources

* [GitHub Repository


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c1w1m5)

### Instructions

Try following the steps using Jupyter notebook. When you are finished, you can check your code and expected outputs in the Solution section.

1. **Creating the database:** Once you've put a little thought into how you might design your database, it's time to go ahead and create it! Start by import the necessary packages. Then, create a database called school.sqlite.
2. **Create a table for contact information:** Create a table called contactInfo to house contact information for both students and staff. Be sure to include columns for first name, last name, role (student/staff), telephone number, street, city, state, and zip code. Be sure to also create a primary key for the table.
3. **Populate the table:**

1. Below, code is provided for you in order to load a list of dictionaries. Briefly examine the list. Each dictionary in the list will serve as an entry for your contact info table. Once you've briefly investigated the structure of this data, write a for loop to iterate through the list and create an entry in your table for each person's contact info.
2. Afterwards, query the table to ensure it is populated.

```
# Load the list of dictionaries; just run this cell  
import pickle  
  
with open('contact_list.pickle', 'rb') as f:  
    contacts = pickle.load(f)
```

1. **Commit your changes to the database:** Persist your changes by committing them to the database.
2. **Create a table for Student Grades:** Create a new table in the database called "grades". In the table, include the following fields: userId, courseId, grade. \*\* This problem is a bit more tricky and will require a dual key. (A nuance you have yet to see.) Here's how to do that:

```
CREATE TABLE table_name(  
   column_1 INTEGER NOT NULL,  
   column_2 INTEGER NOT NULL,  
   ...  
   PRIMARY KEY(column_1,column_2,...)  
);  
  
# Create the grades table  
cur.execute("""CREATE TABLE grades (  
                                    userId INTEGER NOT NULL,  
                                    courseId INTEGER NOT NULL,  
                                    grade INTEGER,  
                                    PRIMARY KEY(userId, courseId)  
                                    );  
            """)
```

1. **Remove duplicates entries:** An analyst just realized that there is a duplicate entry in the contactInfo table! Find and remove it.
2. **Updating an address:** Ed Lyman just moved to 2910 Simpson Avenue York, PA 17403. Update his address accordingly.
3. **Commit your changes to the database:** Persist your changes by committing them to the database.

### Solution

#### [Select for Solution](#dpPanel0)

##### Step 1

```
# Import necessary packages  
import sqlite3  
import pandas as pd  
  
# Create the database school.sqlite  
conn = sqlite3.Connection('school.sqlite')
```

##### Step 2

```
cur = conn.cursor()  
cur.execute("""CREATE TABLE contactInfo (  
                                        userId INTEGER PRIMARY KEY,  
                                        firstName TEXT,  
                                        lastName TEXT,  
                                        role TEXT,  
                                        telephone INTEGER,  
                                        street TEXT,  
                                        city TEXT,  
                                        state TEXT,  
                                        zipcode TEXT  
                                        );  
            """)
```

##### Step 3

```
# Load the list of dictionaries; just run this cell  
import pickle  
  
with open('contact_list.pickle', 'rb') as f:  
    contacts = pickle.load(f)  
  
# Iterate over the contact list and populate the contactInfo table here  
for contact in contacts:  
    firstName = contact['firstName']  
    lastName = contact['lastName']  
    role = contact['role']  
    telephone  = contact['telephone ']  
    street = contact['street']  
    city = contact['city']  
    state = contact['state']  
    zipcode  = contact['zipcode ']  
    cur.execute("""INSERT INTO contactInfo (firstName, lastName, role, telephone, street, city, state, zipcode)   
                  VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');  
                """.format(firstName, lastName, role, telephone, street, city, state, zipcode) )
```

Query the Table to Ensure it is populated

```
cur.execute("""SELECT *   
               FROM contactInfo;""")  
df = pd.DataFrame(cur.fetchall())  
df.columns = [x[0] for x in cur.description]  
df
```

**Expected Output:**

Expected Output: Step 3

|  | userId | firstName | lastName | role | telephone | street | city | state | zipcode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | Christine | Holden | staff | 2035687697 | 1672 Whitman Court | Stamford | CT | 06995 |
| 1 | 2 | Christopher | Warren | student | 2175150957 | 1935 University Hill Road | Champaign | IL | 61938 |
| 2 | 3 | Linda | Jacobson | staff | 4049446441 | 479 Musgrave Street | Atlanta | GA | 30303 |
| 3 | 4 | Andrew | Stepp | student | 7866419252 | 2981 Lamberts Branch Road | Hialeah | FL | 33012 |
| 4 | 5 | Jane | Evans | student | 3259909290 | 1461 Briarhill Lane | Abilene | TX | 79602 |
| 5 | 6 | Jane | Evans | student | 3259909290 | 1461 Briarhill Lane | Abilene | TX | 79602 |
| 6 | 7 | Mary | Raines | student | 9075772295 | 3975 Jerry Toth Drive | Ninilchik | AK | 99639 |
| 7 | 8 | Ed | Lyman | student | 5179695576 | 3478 Be Sreet | Lansing | MI | 48933 |

##### Step 4

```
conn.commit()
```

##### Step 5

We want the SQL code to look like this:

```
CREATE TABLE table_name(  
   column_1 INTEGER NOT NULL,  
   column_2 INTEGER NOT NULL,  
   ...  
   PRIMARY KEY(column_1,column_2,...)  
);
```

```
# Create the grades table  
cur.execute("""CREATE TABLE grades (  
                                    userId INTEGER NOT NULL,  
                                    courseId INTEGER NOT NULL,  
                                    grade INTEGER,  
                                    PRIMARY KEY(userId, courseId)  
                                    );  
            """)
```

##### Step 6

```
# Find the duplicate entry  
cur.execute("""SELECT firstName, lastName, telephone, COUNT(*)   
               FROM contactInfo  
               GROUP BY firstName, lastName, telephone  
               HAVING COUNT(*) > 1;""").fetchall()
```

```
[('Jane', 'Evans', 3259909290, 2)]
```

```
# Delete the duplicate entry  
cur.execute("""DELETE FROM contactInfo   
               WHERE telephone = 3259909290;""")  
  
# Check that the duplicate entry was removed   
cur.execute("""SELECT firstName, lastName, telephone, COUNT(*)   
               FROM contactInfo  
               GROUP BY firstName, lastName, telephone  
               HAVING COUNT(*) > 1;""").fetchall()
```

```
[]
```

##### Step 7

```
# Update Ed's address  
cur.execute("""UPDATE contactInfo  
               SET street = "2910 Simpson Avenue",  
                   city = 'York',  
                   state = 'PA',  
                   zipcode = '17403'  
               WHERE firstName = "Ed" AND lastName = "Lyman";""")  
  
# Query the database to ensure the change was made  
cur.execute("""SELECT *   
               FROM contactInfo;""")  
df = pd.DataFrame(cur.fetchall())  
df.columns = [x[0] for x in cur.description]  
df
```

**Expected Output:**

Expected Output: Step 7

|  | userId | firstName | lastName | role | telephone | street | city | state | zipcode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | Christine | Holden | staff | 2035687697 | 1672 Whitman Court | Stamford | CT | 06995 |
| 1 | 2 | Christopher | Warren | student | 2175150957 | 1935 University Hill Road | Champaign | IL | 61938 |
| 2 | 3 | Linda | Jacobson | staff | 4049446441 | 479 Musgrave Street | Atlanta | GA | 30303 |
| 3 | 4 | Andrew | Stepp | student | 7866419252 | 2981 Lamberts Branch Road | Hialeah | FL | 33012 |
| 4 | 5 | Jane | Evans | student | 3259909290 | 1461 Briarhill Lane | Abilene | TX | 79602 |
| 5 | 6 | Jane | Evans | student | 3259909290 | 1461 Briarhill Lane | Abilene | TX | 79602 |
| 6 | 7 | Mary | Raines | student | 9075772295 | 3975 Jerry Toth Drive | Ninilchik | AK | 99639 |
| 7 | 8 | Ed | Lyman | student | 5179695576 | 2910 Simpson Avenue | York | PA | 17403 |

##### Step 8

```
conn.commit()
```

```
# Remember to close the connection when you are done  
conn.close()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243870

Scraped At: 2026-05-14T21:18:05.506251
