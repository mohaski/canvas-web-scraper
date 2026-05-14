# Defining Data Types

# Defining Data Types

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Defining Data Types

Icon Progress Bar (browser only)

4 min read

With some general knowledge of data types in data science, let's look closer at each and their significance in data science. By understanding these categories of data types and how Python represents them, we can better manipulate and analyze data in our data science tasks. In this section, we will define the common data types, differentiate between categorical and quantitative data, and introduce some useful Python methods for handling these data types.

### Data Types: Categories and Python Representations

Python uses specific variable types to represent different categories of data. Here’s a quick overview of the primary data types you will encounter:

Python data categories with definitions

| Numbers | Text | Logical |
| --- | --- | --- |
| `int`: Stores whole numbers (positive, negative, or zero)  `float`: Stores numbers with decimal points | `str`: Stores sequences of characters (letters, numbers, symbols) | **`bool`:** Stores True or False values |

### Categorical vs. Quantitative Data Types

A fundamental distinction in data science is between categorical data and quantitative data:

Characteristics of Quantitative and Categorical data

| **Categorical Data** | **Quantitative Data** |
| --- | --- |
| These variables denote membership in a group and include two major types:   * **Ordinal Categorical:** Categories that differ in degree (e.g., Bad, Neutral, Good in a survey). They are usually represented as strings but can also be encoded as integers to quantify magnitude/scale (e.g., Bad: -1, Neutral: 0, Good: +1). * **Nominal Categorical**: Categories that denote types within a general category (e.g., different species of Iris flowers). These are usually represented as strings and express categories distinguished by type, not by degree. * **Binary Categorical**: Categories with only two types, often represented as booleans. | These denote the amount or extent of a measurable and can come in discrete units or lie in a continuous range:   * **Discrete Quantitative Data**: This type of data consists of countable values. For example, the number of students in a class or the number of cars in a parking lot. Discrete data is typically represented using integers. Common methods to manipulate discrete data include basic arithmetic operations such as addition, subtraction, multiplication, and division.  * **Continuous Quantitative Data**: This type of data consists of measurable quantities that can take on any value within a range. Examples include height, weight, temperature, and time. Continuous data is usually represented using floats. Python’s math module provides several functions to work with continuous data, such as `math.sqrt` for square roots, `math.log` for logarithms, and `math.sin` for trigonometric calculations. |

### Useful Methods in Python

Python provides numerous methods to manipulate strings and perform arithmetic operations on quantitative data. Some key methods include:

#### **String Methods**

* **strip()** - Removes leading and trailing whitespaces (spaces, tabs, newlines) from the string.
* **replace(old, new, count)** - Replaces occurrences of a substring (`old`) with another substring (`new`) within the string. Optionally, you can specify the number of replacements (`count`).
* **lower()** - Converts all characters in the string to lowercase.
* **upper()** - Converts all characters in the string to uppercase.
* **split(sep)** - Splits the string into a list of substrings based on the specified separator (`sep`). If no separator is provided, whitespace is used by default.
* **join(iterable)** - Joins the elements of an iterable (like a list) into a string using a specified separator.

#### **Quantitative Data Methods**

**Arithmetic operators**

* \* (multiply)
* + (add)
* - (subtract)
* / (divide)
* \*\* (power)
* // (floor division)
* % (modulus)

**Functions in the Python math module**

* `math.sqrt`
* `math.log`
* `math.sin`

### Conceptualize Data Types

Types of data with definitions and examples

| Concept | Definition | Examples | Python Data Types |
| --- | --- | --- | --- |
| Integer Numeric | Discrete data representing whole numbers | Age, number of siblings, number of website visits | int |
| Continuous Numeric | Data representing measurable values that can take any value within a specific range, including decimals | Height, weight, temperature, time | float |
| Nominal Categorical | Qualitative data representing categories with no inherent order or ranking | Hair color (blonde, brunette, red), blood type (A, B, AB, O), political party affiliation (Democrat, Republican, Independent) | str |
| Ordinal Categorical | Qualitative data representing categories with a defined order or ranking | T-shirt size (S, M, L, XL), customer satisfaction rating (1-5 stars), education level (high school, bachelor's degree, graduate degree) | str (although numeric values could be used and mapped to order later) |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243488

Scraped At: 2026-05-14T20:46:12.203597
