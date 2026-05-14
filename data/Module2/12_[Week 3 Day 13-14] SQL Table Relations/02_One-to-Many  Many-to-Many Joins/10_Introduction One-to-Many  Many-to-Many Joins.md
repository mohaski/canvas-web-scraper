# Introduction: One-to-Many / Many-to-Many Joins

# Introduction: One-to-Many / Many-to-Many Joins

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Introduction: One-to-Many / Many-to-Many Joins

Icon Progress Bar (browser only)

2 min read

Previously, you learned about the typical case where one joins on a primary or foreign key. In this section, you'll explore other types of joins using one-to-many and many-to-many relationships.

So far, you've seen a couple of different kinds of join statements: LEFT JOIN and INNER JOIN (aka, JOIN). Both of these refer to the way in which you would like to define your join based on the tables and their shared information. Another perspective on this is the number of matches between the tables based on your defined links with the keywords ON or USING.

You have also seen the typical case where one joins on a primary or foreign key. For example, when you join on customerID or employeeID, this value should be unique to that table. As such, your joins have been very similar to using a dictionary to find additional information associated with that record. In cases where there are multiple entries in either table for the field (column) you are joining on, you will similarly be given multiple rows in your resulting view, one for each of these entries.

In this section you'll learn:

* What one-to-many and many-to-many joins are, as well as implications for the size of query results.
* How to query data using one-to-many and many-to-many joins.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243768

Scraped At: 2026-05-14T21:12:49.640964
