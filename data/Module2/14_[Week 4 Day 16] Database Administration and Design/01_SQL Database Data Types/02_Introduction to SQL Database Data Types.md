# Introduction to SQL Database Data Types

# Introduction to SQL Database Data Types

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Introduction to SQL Database Data Types

Icon Progress Bar (browser only)

3 min read

You've seen that when you create a table, you need to include a name for it as well as define at least one column. You define columns in a CREATE statement by including a name and a data type to let SQLite know the kind of data you will be storing there. The practice of explicitly declaring a type is known as "typing."

Why is it important that you use typing in our database? Simply put, typing allows us to exercise some level of control over our data. Typing not only informs our database of the kind of data you plan to store in a column but it also restricts it. For instance, look at the age column below in our cats table. What do you mean by age? What if you had this:

Database Example: Age Column

| name | breed | age |
| --- | --- | --- |
| Maru | Scottish Fold | 3 |
| Hannah | Tabby | two |
| Lil' Bub | American Shorthair | 5.5 |

Did you intend age to be represented as a whole-number, a word, or a decimal? If you were asked to add up the ages of all the cats you could simply convert the 'two' to 2 in your head, but your database can't do that. It doesn't have that ability because the logic involved in converting a word into a number would be dense and inefficient. What about different languages? What about different spellings? Capitalization, typos, or different hyphenation conventions? These are just some reasons this might start to get overwhelming. In other words, because databases are designed to store large amounts of data, they are very concerned with storing, accessing, and acting upon that data as efficiently as possible, which requires typing of columns.

Typing gives us the ability to perform all kinds of operations with predictable results. For instance, the ability to perform math operations like SUM (i.e. summing integers). If you tried, for example, to SUM all of the cats in the above table, SQLite would actually attempt to convert, or cast, their type to something it can SUM. It would try to convert anything it can to an INTEGER and ignore alpha characters. This can lead to real problems. Without typing, our data might get complicated and messy, and it would be difficult to ask the database questions about large sets of data.

Simply put, it's important to adhere strictly to only storing data that fits with the data type you have given to a particular column. Once you have assigned a data type, most databases will actually throw errors rather than allowing the invalid data to be inserted.

Different database systems also have different data types available, which are important and useful to know whenever you are dealing with those systems. SQLite is a good starting point to learn about data types because it only has four basic categories of data types. They are:

* TEXT
* INTEGER
* REAL
* BLOB

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243859

Scraped At: 2026-05-14T21:17:15.132503
