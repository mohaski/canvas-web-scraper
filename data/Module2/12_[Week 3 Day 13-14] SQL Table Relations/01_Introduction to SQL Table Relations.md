# Introduction to SQL Table Relations

# Introduction to SQL Table Relations

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Introduction to SQL Table Relations

Icon Progress Bar (browser only)

5 min read

Now that you've learned the fundamentals of writing SQL queries, it's time to level up. One of the most powerful aspects of SQL and structured databases is their relational nature, meaning that they not only store data, they store relationships between different tables of data. In this section you will learn to use the JOIN clause and subquery concept to write queries that span multiple tables. Then at the end you will complete some SQL practice specifically intended to prepare you for the kinds of SQL questions you're likely to see in technical interviews.

Watch the video below to learn more about SQL table relations.

[VIDEO LINK](https://player.vimeo.com/video/1001740587?h=e565d742d8)

### Industry Example: Payroll Case Study

You have already seen this image several times:

![Entity relationship diagram of eight tables](https://moringa.instructure.com/courses/1406/files/625425/download)

We also previously described the idea that each table has a primary key (indicated in the diagram above using \*) and many tables have one or more foreign keys that link records in these tables to records in other tables.

But, why is it set up that way? What problem is it solving? Let's walk through a case study to understand this better.

#### Relational Databases

Let's say that you've been hired by a big and important company to handle the payroll for all of their employees. Every two weeks, you need to look up each and every employee and how much they get paid. You need to send them a check and send a notice of that check to their manager. (They have a very flat hierarchy, where everyone is either a manager or a regular employee. Managers do not have managers and regular employees do not manage anyone.)

In addition, let's say that managers get paid every month, instead of every two weeks. So, once a month we need to go through the list of employees again, find just the managers, and send them their checks.

In such a situation, we would need a place to store information about all of the managers and employees. Using a spreadsheet, your storage system might look something like this:

![Table showing employee names, pay, and if they have a manager](https://moringa.instructure.com/courses/1406/files/625401/download)

This tells you almost everything you need, since it would allow you to filter who is a manager and who isn't, plus the payment amounts. But it doesn't have enough information for you to be able to send notices to employees' managers, since it just says who is an employee and who is a manager, but not the relationships.

One idea we might have is to add another column, so that every employee record also lists the name of their manager:

![Table showing employee names, pay, if they have a manager, and the manager&#39;s name.](https://moringa.instructure.com/courses/1406/files/625364/download)

Now we technically have all of the information we need, but we can think of a few issues:

1. There is some redundancy and wasted space. We don't actually need the Manager? column, since we can just check whether there is a name in the Manager Name column...but maybe we don't want to remove that since accidentally putting a manager name in the wrong place could mark someone as a regular employee when they're actually a manager.
2. This is not a very robust system if anything changes. What if we get another manager who is also named Steve? Maybe you could enter the new Steve as "Steve H.", and you would just need to remember that "Steve" refers to the one who was there first.
3. Or, what if Steve decides he wants to rebrand himself and start going by Steven instead? (You can also think of other reasons why someone would change their legal name.) Then you would need to find all places in the spreadsheet that say "Steve" and replace them with "Steven".

If you really only had 5 total employees, it would be manageable to do this work "by hand" and just remember what you did. But if you had hundreds or thousands of employees, or you were working with a team of payroll professionals instead of by yourself, you can imagine how this system could get unmanageable pretty quickly!

#### The Relational Database Solution

We can use SQL to manage this information more effectively. First, we set up a managers table and an employees table with the following schemas:

![Managers table and employees table with id and manager\_id keys](https://moringa.instructure.com/courses/1406/files/625393/download)

Both the managers table and the employees table have primary keys (indicated by the key icon here) called id. Then employees have a foreign key called manager\_id that links to a record in the managers table.

The same data shown above is entered in like this:

![Two tables showing an id column for employees and a manager\_id column](https://moringa.instructure.com/courses/1406/files/625374/download)

Now, the issues described before are no longer issues:

1. There is no redundancy or extra space. You know whether someone is a regular employee or a manager based on which table they are in, and managers don't have an extra empty field for a manager name.
2. If we get another manager named Steve, we can just add another record to the managers table. It will have an id of 3 and will not be confused with this Steve, who has an id of 1.
3. If Steve changes his name to Steven, you only need to change one value in one place: the name column in Steve's record in the managers table. No need to hunt down the same information stored in multiple places in order to edit it!

### Learning Outcomes

After completing this lesson, you should be able to:

* Write SQL queries that make use of various types of JOIN statements (joins).
* Compare and contrast the various types of joins.
* Discuss how primary and foreign keys are used in SQL.
* Decide and perform whichever type of join is best for retrieving desired data.
* Explain one-to-many and many-to-many joins and relationships as well as implications for the size of query results.
* Query data using one-to-many and many-to-many joins.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243745

Scraped At: 2026-05-14T21:11:33.294053
