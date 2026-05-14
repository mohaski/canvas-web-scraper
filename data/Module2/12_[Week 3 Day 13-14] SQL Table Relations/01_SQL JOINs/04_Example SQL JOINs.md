# Example: SQL JOINs

# Example: SQL JOINs

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Example: SQL JOINs

Icon Progress Bar (browser only)

2 min read

Continuing with the employee payroll database, let's say we want to handle payroll for all regular (non-manager) employees. To do that, we need to know their name, pay, and manager name.

If we just SELECT \* from the employees table, it will look like this:

```
import pandas as pd  
import sqlite3  
  
conn = sqlite3.connect("payroll.db")  
pd.read_sql("""SELECT * FROM employees;""", conn)
```

Use of SELECT \*

| # | id | name | pay | manager\_id |
| --- | --- | --- | --- | --- |
| 0 | 1 | Bob | 3000.0 | 1 |
| 1 | 2 | Karen | 4000.0 | 1 |
| 2 | 3 | Patrick | 4000.0 | 2 |

Then we could manually query for each manager id:

```
pd.read_sql("""SELECT name FROM managers WHERE id = 1;""", conn)
```

Manual Manager ID Query

| # | name |
| --- | --- |
| 0 | Steve |

 pd.read\_sql("""SELECT name FROM managers WHERE id = 2;""", conn)

pd.read\_sql

| # | name |
| --- | --- |
| 0 | Spongebob |

That works, but it's annoying. Again, you can imagine that not scaling well to hundreds or thousands of employees.

With a SQL join, we can do it all at once:

```
q = """  
SELECT *  
FROM employees  
JOIN managers  
   ON employees.manager_id = managers.id  
;  
"""  
pd.read_sql(q, conn)
```

Query with SQL join

| # | id | name | pay | manager\_id | id | name | pay |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | Bob | 3000.0 | 1 | 1 | Steve | 7000.0 |
| 1 | 2 | Karen | 4000.0 | 1 | 1 | Steve | 7000.0 |
| 2 | 3 | Patrick | 4000.0 | 2 | 2 | Spongebob | 10000.0 |

Great, all of the information in one table.

Well, that has everything we want, plus some extra information. It's confusing that we have name and pay in there twice. Since we are trying to manage regular employee payroll, we probably only want the pay for those employees, and we should figure out a way to distinguish between the employee's name and the manager's name.

Most of the time when you have a JOIN, you want to specify which columns you actually want, instead of SELECT \*. Something like this, using aliases to make everything really clear:

```
q = """  
SELECT  
   employees.name AS employee_name,  
   employees.pay AS employee_pay,  
   managers.name AS manager_name  
FROM employees  
JOIN managers  
  
    ON employees.manager_id = managers.id  
;  
"""  
pd.read_sql(q, conn)
```

JOIN with columns specified

| # | employee\_name | employee\_pay | manager\_name |
| --- | --- | --- | --- |
| 0 | Bob | 3000.0 | Steve |
| 1 | Karen | 4000.0 | Steve |
| 2 | Patrick | 4000.0 | Spongebob |

Perfect! Now we have a nice, maintainable system, and we are able to pull exactly the data needed for this task.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243753

Scraped At: 2026-05-14T21:11:58.104017
