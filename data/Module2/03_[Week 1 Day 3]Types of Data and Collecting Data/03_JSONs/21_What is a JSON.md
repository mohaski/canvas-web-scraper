# What is a JSON?

# What is a JSON?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What is a JSON?

Icon Progress Bar (browser only)

3 min read

**JSON (JavaScript Object Notation)** is a human-readable data format that you will often encounter when:

* extracting data directly from the content of a web page through a process known as scraping
* via making data requests from Application Programming Interfaces (APIs). An API is a set of protocols and tools that allows you to programmatically access and interact with data from external sources.

### How Does it Work?

JSON (or Javascript Object Notation) is a web based format for structuring information.

The data is typically organized hierarchically in a manner that is very similar to Python nested data structures like nested dictionaries or lists of lists. However, when you grab data in JSON format from the web it is in a pure text format. The text might look something like this:

```
"first_name": Rajeev",  
  
"last_name": "Sharma",  
  
"email_address": "rajeev@ezeelive.com",  
  
"is_alive": true,  
  
"age": 30,  
  
"height_cm": 185.2,  
  
"billing_address": {  
  
"address": "502 Main Market, Evershine City, Evershine, Vasai East",  
  
"city": "Vasai Road, Palghar",  
  
"state": "Maharashtra",  
  
"postal_code": "401208"  
  
},  
  
"shipping_address": {  
  
"address": "Ezeelive Technologies, A-4, Station Road, Oripada, Dahisar East",  
  
"city": "Mumbai",  
  
"state": "Maharashtra",  
  
"postal_code": "400058"  
  
},
```

It is pretty easy to see that this looks a lot like a nested dictionary. However, the problem is that the data is actually text. We need to parse this text somehow.

Recall that we were able to parse CSVs without too much difficulty by splitting the text on newline characters, then by delimiter, and then finally converting strings to other types as necessary. This was possible because the structure of a CSV is strongly constrained and we knew that it had to come in rows and columns with values separated by a delimiter. Unfortunately, this is not going to work with JSONs. There is clearly structure in the above example – it is a dict of dicts. But writing a parser to load this structure into a Python data structure (i.e. a dictionary) would be painful. Fortunately, Python’s json module can do all of this parsing for us. In this topic, you’ll learn how to use the json module to load in this text and structure it appropriately in a Python data structure.

After this comes the tricky part. The data you need for your analysis is likely embedded deep within and also scattered widely across the parsed JSON data structure. You will need to understand how the data is organized and then navigate through and across a nested set of structures to get the specific pieces of information you need. You might employ techniques like iterating through nested structures using loops, filtering unwanted elements, and potentially creating a new data structure (like a list of dicts) with relevant information structured appropriately for your analysis task.

### Conceptualization: JSONs

There is a close correspondence to how data is encoded in JSON format and represented in Python:

JSON and Python Data structures with examples

| JSON Data Structure | Equivalent Python Data Structure | JSON Example | Python Example |
| --- | --- | --- | --- |
| Object | Dictionary | { "name": "Alice", "age": 30, "city": "New York" } | {"name": "Alice", "age": 30, "city": "New York"} |
| Array | List | [1, 2, 3, "apple", "banana"] | [1, 2, 3, "apple", "banana"] |
| String | String | "This is a string" | "This is a string" |
| Number | Integer or Float | 123 or 3.14 | 123 or 3.14 |
| Boolean | Boolean | true or false | True or False |
| Null | None | null | None |

Python explicitly uses this correspondence when parsing text files in JSON format into Python data structures and variable types. A large part of the wrangling process will then be to extract the data you need from the nested data structure and convert/transform data types accordingly.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243510

Scraped At: 2026-05-14T20:48:10.357168
