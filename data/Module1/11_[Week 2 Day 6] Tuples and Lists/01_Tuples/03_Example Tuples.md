# Example: Tuples

# Example: Tuples

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Example: Tuples

Icon Progress Bar (browser only)

1 min read

Imagine storing a person's contact information: name, phone number, and email. Since this data shouldn't be modified, a tuple is a suitable choice. Let's create a tuple to store someone's contact information:

```
contact_info = ("Alice", "1234567890", "alice@email.com")
```

**In this example:**

* We create a variable called `contact_info`
* We assign it a tuple containing three pieces of information:

* + `"Alice"`: A string representing the name "Alice"
  + `"1234567890"`: An integer, likely a phone number
  + `"Snippet"`: A string representing an email address

**The next part of the code demonstrates how to access individual elements within the tuple.**

* + Tuples use zero-based indexing, similar to lists. The first element has an index of 0, the second has an index of 1, and so on.
  + Here, `contact_info[0]` refers to the element at index 0 of the tuple `contact_info`.
  + The value `"Alice"` is stored at index 0, so it's assigned to the variable name.

```
contact_info = ("Alice", 1234567890, "alice@email.com")  
  
# Accessing elements  
name = contact_info[0]  # name will be "Alice
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239234

Scraped At: 2026-05-14T15:54:08.630534
