# What are One-to-Many and Many-to-Many Relationships?

# What are One-to-Many and Many-to-Many Relationships?

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) What are One-to-Many and Many-to-Many Relationships?

Icon Progress Bar (browser only)

3 min read

We’ve talked about much of the power of SQL and databases coming from the relationships among tables. But so far we have only used instances where one record in a table connects to just one record in another table. Think of employees and addresses, for example, in a payments database for HR. One employee is (probably) only going to have one address of record.

But what about situations like a customers table and an orders table for an e-commerce company? Hopefully, one customer has many orders. Or teachers in a school’s database: each teacher teaches multiple students, not just one. Continuing with schools, think about students and courses: a student can enroll in many courses, and any given course will (probably) have multiple students. We need ways to represent both of these kinds of relationships.

Keywords:

* **Database:** A collection of organized information that can be easily accessed, managed, and updated.
* **Table:** A set of data arranged in rows and columns, like a spreadsheet.
* **Relationship:** A connection between tables in a database.
* **Join:** A way to combine rows from two or more tables based on a related column.
* **One-to-Many:** A record in one table connects to multiple records in another table, like teachers and students.
* **Many-to-Many:** Many records in a table connect to many records in another table, like students and courses.

### How Do One-to-Many and Many-to-Many Relationships Work?

In SQL, specifically when using Python's SQLite, one-to-many and many-to-many relationships are fundamental concepts that help model real-world scenarios where entities are related to each other in various ways. Here's how these relationships work:

#### One-to-Many Relationship

A one-to-many relationship occurs when a record in one table is related to multiple records in another table. For example, consider a scenario where each customer can place multiple orders, but each order is linked to only one customer.

Example:

1. **Customers Table:**  
   * CustomerID (Primary Key)
   * Name
2. **Orders Table:**  
   * OrderID (Primary Key)
   * OrderDate
   * CustomerID (Foreign Key referring to Customers.CustomerID)

In this setup, the CustomerID in the Orders table acts as a foreign key, creating the one-to-many relationship. Each customer can have multiple orders, but each order is associated with only one customer.

#### Many-to-Many Relationship

A many-to-many relationship occurs when records in one table can relate to multiple records in another table, and vice versa. For example, consider a scenario where students can enroll in multiple courses, and each course can have multiple students.

Example:

1. **Students Table:**  
   * StudentID (Primary Key)
   * Name
2. **Courses Table:**  
   * CourseID (Primary Key)
   * CourseName
3. **Enrollments Table (Linking Table):**  
   * StudentID (Foreign Key referring to Students.StudentID)
   * CourseID (Foreign Key referring to Courses.CourseID)

The Enrollments table links students and courses, representing the many-to-many relationship.

### Conceptualization: One-to-Many and Many-to-Many Relationships

Type of Relationship Defined with Code Snippet

| Type of Relationship | Definition | Pseudocode Snippet |
| --- | --- | --- |
| One-to-Many Relationship | Involves a parent table and a child table where each record in the parent can relate to multiple records in the child. Implemented using a foreign key in the child table that references the primary key of the parent table. | ``` Create ParentTable (ParentID PRIMARY KEY)  Create ChildTable (ChildID PRIMARY KEY, ParentID FOREIGN KEY REFERENCES ParentTable) ``` |
| Many-to-Many Relationship | Involves two tables where records in each can relate to multiple records in the other. Implemented using a linking (junction) table that includes foreign keys referencing the primary keys of both related tables. | ``` Create TableA (AID PRIMARY KEY) Create TableB (BID PRIMARY KEY) Create LinkingTable (AID FOREIGN KEY REFERENCES TableA, BID FOREIGN KEY REFERENCES TableB) ``` |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243770

Scraped At: 2026-05-14T21:12:57.627804
