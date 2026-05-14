# What are Dictionaries?

# What are Dictionaries?

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) What are Dictionaries?

Icon Progress Bar (browser only)

6 min read

A dictionary is a fundamental data structure in Python that stores information in a collection of key-value pairs. Think of it like the list of contacts in your mobile phone. In your contacts, each name (**key**) has a corresponding phone number (**value**). Similarly, in a dictionary, you can associate unique labels (**keys**) with any data (**values**) you want to store.

### Components of Dictionaries

Let's look more closely at the primary components of dictionaties.

#### **Key**

This acts as a unique identifier for a specific piece of data within the dictionary. Keys must be immutable data types like strings, numbers, or tuples. This immutability ensures that keys can't be changed accidentally, allowing for reliable retrieval of values. Here's a breakdown of some key terms around the use of dictionaries in Python:

* **Examples of Valid Keys:** `"name"` , `42`, `("apple", "red"`, `(tuple)`
* **Examples of Invalid Keys:** Lists (mutable), dictionaries (mutable)

#### **Value**

This represents the actual data you want to store and can be of any data type, including strings, numbers, lists, or even other dictionaries. This flexibility allows dictionaries to hold a wide variety of information.

#### **Mutable**

Unlike some data structures like strings or numbers, dictionaries are mutable. This means you can modify the dictionary after it's created. You can add new key-value pairs, remove existing ones, or even change the values associated with specific keys. This mutability makes dictionaries highly versatile for storing and managing dynamic data.

Let's expand on the concept of immutability for keys. Imagine a dictionary where keys could be changed. If you change the name in your contact list entry `(key)`, finding the corresponding number `(value)` would become impossible. By keeping keys immutable, dictionaries ensure a reliable and consistent way to access data.

### How Do Dictionaries Work?

Unlike lists, where items are accessed by their order `(index)`, dictionaries rely on a special technique called hashing to efficiently retrieve values using keys. Imagine a dictionary as a giant warehouse filled with boxes. Each box has a unique label (key) that helps you identify what's inside (value).

### [Keys and Hashing](#dpPanel0)

When you add a key-value pair to a dictionary, Python performs a hashing operation on the key. Hashing essentially converts the key into a unique fixed length number `(hash value)`. This hash value is then used to determine the location (memory address) where the key-value pair is stored within the dictionary. Think of it as a complex code assigned to each box based on its label (key).

* **Collision Handling:** It's important to note that sometimes two different keys might generate the same hash value (collision). To handle these collisions, Python uses additional techniques to store the key-value pair in the appropriate location.

### [Retrieving Values](#dpPanel1)

When you try to access a value using a key, Python performs the same hashing operation on the key. If the hash value matches an existing key in the dictionary, Python retrieves the associated value stored at that location. Going back to the warehouse analogy, you provide the box label (key), and if the code (hash value) matches a box, you retrieve its contents (value).

### [Performance Advantage](#dpPanel2)

Hashing allows for very fast retrieval of values in dictionaries because Python can directly jump to the memory location based on the key's hash value. This is significantly faster than searching through a list, where you would need to compare each item's index with the desired position.

#### Key Points to Remember

* Hashing provides efficient lookups in dictionaries based on keys.
* Collisions can occur, but Python has mechanisms to handle them.
* Retrieving values using keys is much faster than using indexes in lists.

### Conceptualization: Dictionary Parts and Features

A dictionary in Python is a versatile data structure that stores information in key-value pairs. Its features of immutability for keys, mutability for the structure, and efficient hashing for retrieval make it ideal for fast and reliable data management. For instance, in the dictionary contact `= {"name": "Alice", "age": 30, "city": "New York"}`, you can efficiently store, access, and modify details about a person.

Python dictionary parts and features with examples

| Part and Definition | Feature | Example |
| --- | --- | --- |
| **Key:** This acts as a unique identifier for a specific piece of data within the dictionary. Keys must be immutable data types like strings, numbers, or tuples. | * Immutable (cannot be changed after creation) * Uniqueness ensures reliable retrieval of values | In the dictionary contact `= {"name": "Alice", "age": 30, "city": "New York"}`, "name", "age", and "city" are keys. |
| **Value:** This represents the actual data you want to store and can be of any data type, including strings, numbers, lists, or even other dictionaries. | * Can be any data type * Provides flexibility to store varied data | In contact `= {"name": "Alice", "age": 30, "city": "New York"}`, "Alice", 30, and "New York" are values. |
| **Mutable:** Dictionaries are mutable, meaning you can modify the dictionary after it's created. You can add new key-value pairs, remove existing ones, or change the values associated with specific keys. | * Add, remove, or modify key-value pairs * Highly versatile for dynamic data | In contact `= {"name": "Alice", "age": 30, "city": "New York"}`, you can change `"age": 30` to `"age": 301`, add `"phone":"123-456-7890"`, or remove `"city": "New York"`. |
| **Hashing:** Python performs a hashing operation on the key to convert it into a unique fixed-length number (hash value). This hash value determines the location where the key-value pair is stored within the dictionary. | * Provides efficient lookups * Handles collisions through additional techniques | In `contact = {"name": "Alice", "age": 30, "city": "New York"}`, the key "name" is hashed to store and retrieve the value "Alice" efficiently. |
| **Retrieving Values:** When you access a value using a key, Python performs the same hashing operation on the key and retrieves the value stored at the corresponding location if the hash value matches an existing key. | * Efficient retrieval using keys * Faster than searching through a list | Accessing `contact["name"]` retrieves "Alice" from `contact = {"name": "Alice", "age": 30, "city": "New York"}` |
| **Performance Advantage:** Hashing allows for very fast retrieval of values in dictionaries because Python can directly jump to the memory location based on the key's hash value, which is faster than searching through a list. | * Efficient lookups * Significantly faster retrieval than list indexing | Accessing `contact["name"]` is faster than searching through a list to find the element "Alice". |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239270

Scraped At: 2026-05-14T15:57:01.878676
