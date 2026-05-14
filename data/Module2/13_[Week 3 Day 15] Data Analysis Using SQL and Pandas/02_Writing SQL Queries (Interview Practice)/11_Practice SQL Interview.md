# Practice: SQL Interview

# Practice: SQL Interview

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: SQL Interview

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

In this practice, we'll see four different interview questions that test your SQL knowledge. We didn't write these questions -- instead, we found them out in the real-world. These are questions that have been used in the past by major technology companies such as Facebook, Amazon, and Twitter. Our goal here isn't to memorize the questions or anything like that -- after all, it's extremely unlikely that these questions are still in use, now that they've become publicly available on the interwebs. Instead, our goal is to treat these questions as if they are the real thing, and give us some insight into the types of questions we'll need to be able to answer in order pass an interview involving SQL.

If these questions seem hard to you, don't sweat it, they're supposed to be tough! These are meant to help you identify any areas of knowledge where you still need to grow! Use these questions as a way to see where your SQL knowledge is strong, and where it's a bit weak. Then, go study and practice in the areas where you still need work.

### Considerations

* Since these are interview questions, they'll almost always be posed as hypotheticals. This means that you won't have a real database to work with and test your code on. This also means that there are multiple different solutions to any given problem listed here. Be sure to double check the code you write for bugs and errors. It's much harder to write bug-free code when you aren't able to test it against a database!
* These are real questions that have been reported to online forums from job seekers at major companies. Obviously, it's unlikely that they're still in use at these companies, but they still represent a great way for us to test our skills against the kinds of questions we can expect to be asked in an interview!

### Instructions

1. Assume we have a table of employee information, which includes salary information. Write a query to find the names and salaries of the top 5 highest paid employees, in descending order.
2. Assume we have two SQL tables: authors and books. The authors table has a few million rows, and looks like this:  

   Authors Dataset Layout

   | author\_name | book\_name |
   | --- | --- |
   | author\_1 | book\_1 |
   | author\_2 | book\_2 |
   | author\_3 | book\_3 |
   | author\_4 | book\_4 |
   | author\_5 | book\_5 |
   | author\_6 | book\_6 |

     
   The books dataset also has a few million rows, and looks like this:  

   Books Dataset Layout

   | book\_name | copies\_sold |
   | --- | --- |
   | book\_1 | 10000 |
   | book\_2 | 2575 |
   | book\_3 | 60000 |
   | book\_4 | 98000 |
   | book\_5 | 5250 |
   | book\_6 | 19775 |

     
   Write a query that shows the top 3 authors who sold the most total books.
3. Assume you have two tables, customers and orders. Write a SQL query to select all customers who purchased at least 2 items on two separate days.
4. A company uses 2 data tables, Employee and Department, to store data about its employees and departments.  
   1. Table Name: Employee  
      Attributes:  
      ID Integer,  
      NAME String,  
      SALARY Integer,  
      DEPT\_ID Integer
   2. Table Name: Department  
      Attributes:  
      DEPT\_ID Integer,  
      NAME String,  
      LOCATION String

Write a query to print the respective Department Name and number of employees for all departments in the Department table (even unstaffed ones).

Sort your result in descending order of employees per department; if two or more departments have the same number of employees, then sort those departments alphabetically by Department Name.

### Solution

#### Select for Solution

##### Question 1

```
SELECT name, salary from Employees  
ORDER BY salary DESC  
LIMIT 5;
```

##### Question 2

```
SELECT a.author_name, SUM(b.copies_sold) as total_sold from Authors a  
JOIN Books b ON a.book_name = b.book_name  
GROUP BY a.author_name  
ORDER BY total_sold DESC  
LIMIT 3;
```

##### Question 3

```
SELECT c.name, COUNT(DISTINCT o.OrderDate) as NumOrderDates FROM (SELECT c.name, o.quantity FROM Customers c   
    JOIN Orders o ON c.orderNumber = o.OrderNumber  
    WHERE o.quantity > 1)  
WHERE NumOrderDates > 1
```

##### Question 4

```
SELECT d.name, COUNT(e.ID) as EmployeeCount   
FROM Department d   
LEFT JOIN Employee e on d.dept_id, = e.dept_id  
GROUP BY d.dept_id, d.name  
ORDER BY EmployeeCount DESC, d.name
```

### Additional SQL Practice Questions for Interviews

Here are 10 common SQL questions that are often asked in data science interviews, along with explanations for the correct answers.

These questions cover a range of SQL topics and concepts that are essential for data science roles, from joins and filtering to handling duplicates and understanding aggregate functions. Understanding the logic behind each answer is key to performing well in interviews.

1. What is the difference between `INNER JOIN` and `LEFT JOIN`?

#### Answer

**INNER JOIN:** Returns only the rows that have matching values in both tables. If there is no match, the result set will not include the rows from either table.

**LEFT JOIN (or LEFT OUTER JOIN):** Returns all the rows from the left table, along with the matching rows from the right table. If there is no match, the result will still include all rows from the left table, with NULLs for missing matches from the right table.

1. How would you find the second highest salary in a table named `employees` with a column `salary`?

#### Answer

```
```sql  
SELECT MAX(salary)   
FROM employees   
WHERE salary < (SELECT MAX(salary) FROM employees);  
```
```

**Explanation:** This query finds the maximum salary that is less than the highest salary. The subquery identifies the highest salary, and the main query then finds the maximum salary that is lower than that, effectively giving the second highest salary.

1. How do you retrieve the names of employees who have the same salary as another employee in the `employees` table?

#### Answer

```
```sql  
SELECT e1.name   
FROM employees e1  
JOIN employees e2 ON e1.salary = e2.salary   
AND e1.name <> e2.name;  
```
```

**Explanation:** This query joins the `employees` table to itself (a self-join), matching employees who have the same salary but different names.

1. Explain the difference between `GROUP BY` and `ORDER BY`.

#### Answer

**GROUP BY:** Groups rows that have the same values in specified columns into summary rows, such as aggregating data (e.g., SUM, COUNT) for each group.

**ORDER BY:** Sorts the result set of a query by one or more columns. `ORDER BY` doesn’t change the content of the result set; it just arranges the rows in a specified order.

1. How would you find all employees who have not made any sales in a `sales` table linked by `employee\_id`?

#### Answer

```
```sql  
SELECT name   
FROM employees e  
LEFT JOIN sales s ON e.employee_id = s.employee_id  
WHERE s.employee_id IS NULL;  
```
```

**Explanation:** This query uses a `LEFT JOIN` to include all employees and then filters out those who have made sales by checking for NULL in the `sales` table.

1. What is the difference between `HAVING` and `WHERE`?

#### Answer

**WHERE:** Is used to filter rows before any grouping is applied in the query. It is used with individual rows.

**HAVING:** Is used to filter groups after the `GROUP BY` clause has been applied. It is used with aggregated data.

1. Write a query to find the total number of orders placed by each customer, assuming you have an `orders` table with `customer\_id`.

#### Answer

```
```sql  
SELECT customer_id, COUNT(*) AS total_orders  
FROM orders  
GROUP BY customer_id;  
```
```

**Explanation:** This query counts the number of orders for each `customer\_id`, grouping the results by `customer\_id`.

1. How do you find duplicate records in a table with a column named `email`?

#### Answer

```
```sql  
SELECT email, COUNT(*)  
FROM users  
GROUP BY email  
HAVING COUNT(*) > 1;  
```
```

**Explanation:** This query groups the records by `email` and then uses the `HAVING` clause to filter groups that have more than one occurrence, indicating duplicates.

1. What is a `CROSS JOIN`, and when would you use it?

#### Answer

**CROSS JOIN:** Returns the Cartesian product of two tables, meaning it combines every row from the first table with every row from the second table.

It is rarely used deliberately because it can produce an extremely large result set. It might be used when you need to generate combinations of data, such as testing every possible pairing of two sets.

1. How would you delete duplicate rows in a table where there is no primary key?

#### Answer

```
```sql  
DELETE FROM employees   
WHERE rowid NOT IN (  
    SELECT MIN(rowid)   
    FROM employees   
    GROUP BY name, salary, department  
);  
```
```

**Explanation:** This query deletes rows where the `rowid` is not the minimum `rowid` for each group of duplicates (identified by `name`, `salary`, and `department`). It ensures that only one instance of each duplicate group remains.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243843

Scraped At: 2026-05-14T21:16:20.007571
