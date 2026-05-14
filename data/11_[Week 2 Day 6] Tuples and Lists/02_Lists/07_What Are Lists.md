# What Are Lists?

# What Are Lists?

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) What Are Lists?

Icon Progress Bar (browser only)

3 min read

Lists are fundamental data structures in Python used to store ordered collections of elements. They are similar to tuples, which we learned about earlier, but with one key difference: lists are mutable, meaning their contents can be changed after creation.

### Key Characteristics of Lists

1. **Mutability**: Unlike tuples, elements within a list can be changed, added, or removed.
2. **Ordering**: Elements in a list maintain their order of insertion.
3. **Flexibility**: Lists can contain elements of different data types.

### Creating Lists

Lists are created using square brackets `[]`, with elements separated by commas. Elements within a list can be of different data types, similar to tuples.

```
fruits = ["apple", "banana", "cherry"]  
numbers = [1, 2, 3.14]  
mixed_list = ["hello", 42, True]
```

Let's break down the example:

1. `fruits = ["apple", "banana", "cherry"]`
   * This creates a list called `fruits`.
   * The equals sign `=` assigns the list on the right to the variable name on the left.
   * The square brackets `[]` indicate that we're creating a list.
   * Inside the brackets, we have three elements: 'apple', 'banana', and 'cherry'. These are all strings, separated by commas.
2. `numbers = [1, 2, 3.14]`
   * This creates a list called `numbers`.
   * It contains three elements: 1 and 2 (which are integers), and 3.14 (which is a float).
   * This example shows that lists can contain different numeric types.
3. `mixed_list = ["hello", 42, True]`
   * This creates a list called `mixed_list`.
   * It contains three elements of different types:
     + "hello" (a string)
     + 42 (an integer)
     + True (a boolean value)
   * This example demonstrates that lists can contain elements of completely different types.

These examples illustrate the flexibility of lists in Python. You can create lists that contain elements of the same type (like `fruits`), different numeric types (like `numbers`), or even completely different types (like `mixed_list`).

### How Do Lists Work?

Lists allow you to group and store data together in a flexible manner. You can modify the contents of a list throughout your program's execution, making them ideal for dynamic data manipulation.

#### When to Use Lists

Lists are preferred over tuples when:

* You need to modify the collection's contents after creation.
* Your data is likely to change during the program's execution.
* You need to frequently add or remove elements.

![Uploaded Image](https://moringa.instructure.com/courses/1391/files/620345/download)

#### Example

Imagine you're creating a shopping list. You might start with a few items, but as you plan your meals, you'll likely add or remove items from the list. A list is ideal for this scenario as it allows for these modifications.

### Conceptualization: Lists vs. Tuples

The following table summarizes the features of both lists and tuples:

Features of Lists and Tuples with Business Example

| Feature | Lists | Tuples | Example Use Case |
| --- | --- | --- | --- |
| **Ordering** | Elements maintain order of insertion | Elements maintain order of insertion | **Situation**  You are developing an e-commerce platform where the inventory of products is frequently updated. Each product has attributes like name, price, and quantity.  **Solution**  Use lists to store product attributes since lists are mutable, allowing for updates as inventory changes. |
| **Mutability** | Elements **can**be changed after creation | Elements cannotbe changed after creation | **Situation**  You need to store the coordinates of fixed landmarks on a map in a geographic information system (GIS) application. The coordinates (latitude, longitude) should remain unchanged once set.  **Solution**  Use tuples to store landmark coordinates as they are immutable and ensure data integrity. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239240

Scraped At: 2026-05-14T15:54:39.008304
