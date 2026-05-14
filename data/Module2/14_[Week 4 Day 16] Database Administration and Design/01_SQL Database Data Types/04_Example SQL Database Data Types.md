# Example: SQL Database Data Types

# Example: SQL Database Data Types

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Example: SQL Database Data Types

Icon Progress Bar (browser only)

3 min read

Given that the management of your company, where all employees work remotely, has requested a database to store each employee's name and a brief biography, you should approach this task with both the current and future needs in mind. The initial database should be designed to handle the basic requirements of storing employee names and biographies. However, considering the company's goal of eventually leveraging data science tools to better serve its employees, the database should be scalable and flexible enough to incorporate additional employee-related data in the future.

You should start by defining the basic structure of the database. This might include creating a table with columns for employee ID, name, and biography. As the company plans to expand the database's functionality, it is important to consider what other information might be useful, such as job roles, skills, performance metrics, location, and work preferences. Therefore, the database schema should be designed with normalization in mind, ensuring that it can accommodate related tables for storing more detailed information like project assignments, employee feedback, and training history.

Here is some sample code with an explanation of it below.

```
CREATE TABLE users (  
  id INT PRIMARY KEY,  
  name VARCHAR(50),  
  bio TEXT  
);  
  
INSERT INTO users (id, name, bio) VALUES  
  (1, 'John Doe', 'This is a long text field that can store up to 65,535 characters.'),  
  (2, 'Jane Smith', 'A short bio for Jane.');
```

Here is the explanation of the code.

1. **CREATE TABLE users:** This line creates a new table named `users` in the database.
2. **(`id` INT PRIMARY KEY, `name` VARCHAR(50), `bio` TEXT):** This section defines the structure of the `users` table, including the following columns:
   * **`id`:** An integer data type that is set as the primary key. This means each row in the table will have a unique identifier.
   * **`name`:** A variable-length character string with a maximum length of 50 characters.
   * **`bio`:** A text data type that can store up to 65,535 characters.
3. **INSERT INTO users (id, name, bio) VALUES:** This line starts the insertion of data into the `users` table.
4. **(1, 'John Doe', 'This is a long text field that can store up to 65,535 characters.'):** This row inserts a new record into the `users` table with the following values:
   * **`id`:** 1
   * **`name`:** 'John Doe'
   * **`bio`:** 'This is a long text field that can store up to 65,535 characters.'
5. **(2, 'Jane Smith', 'A short bio for Jane.'):** This row inserts another new record into the `users` table with the following values:
   * **`id`:** 2
   * **`name`:** 'Jane Smith'
   * **`bio`:** 'A short bio for Jane'

In summary, this SQL code creates a new table called `users` with three columns: `id`, `name`, and `bio`. It then inserts two new records into the `users` table, one for 'John Doe' and one for 'Jane Smith', with their respective biographical information.

The `id` column is set as the primary key, which means each row in the table will have a unique identifier. The `name` column is a variable-length character string with a maximum length of 50 characters, and the `bio` column is a text data type that can store up to 65,535 characters.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243863

Scraped At: 2026-05-14T21:17:28.572907
