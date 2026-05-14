# Defining Python Commands

# Defining Python Commands

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Defining Python Commands

Icon Progress Bar (browser only)[Snippet]

6 min read

Building on your understanding of algorithms and the use of IDEs, the next steps for building your Python skills is learning about how to use variables. Variables are fundamental to building your programming skills. 

In Python, variables are used to store and refer to values in a program. A variable is essentially a name that you give a piece of data, allowing you to access and manipulate that data throughout your code.

Variables in Python provide a way to store and manipulate data in your programs. They allow you to assign values, perform calculations, make decisions based on their values, and pass them around your code. Understanding variables is fundamental to writing effective and dynamic Python programs.

Here are some key points about variables in Python:

### Dynamic Typing

* Python is a dynamically-typed language, which means you don't need to declare the type of a variable explicitly.
* The type of a variable is determined by the value assigned to it, and it can change during the execution of a program.

### Variable Assignment

* To create a variable, you simply choose a name and assign a value to it using the assignment operator `=`
* The syntax for variable assignment is: `variable_name = value'`
* For example: `age = 25` assigns the integer value 25 to the variable named `age`

### Variable Naming Conventions

* Variable names should be meaningful and descriptive, indicating the purpose or content of the variable.
* Variable names should follow certain naming conventions:
  + Start with a letter or an underscore
  + Contain letters, digits, and underscores
  + Case-sensitive, meaning `age` and `Age` are considered different variables
* It's recommended to use lowercase letters and underscores for variable names (`snake_case`).

### Variable Types

Variables in Python can hold values of different types, such as numbers, strings, lists, dictionaries, and more. The type of a variable is determined by the value assigned to it. Some common variable types include:

* `int`: Represents integers, e.g., age = 25 `age = 25`
* `float`: Represents floating-point numbers, e.g., `height = 1.75`
* `str`: Represents strings, e.g., `name = "John"`
* `bool`: Represents Boolean values (True or False), e.g., `is_student = True`
* `list`: Represents an ordered collection of items, e.g., `fruits = ["apple", "banana", "orange"]`

### Variable Reassignment

* In Python, you can reassign a new value to an existing variable.
* When you assign a new value to a variable, the previous value is overwritten.
* For example: `age = 25` and then `age = 30` will update the value of age to 30.

### Variable Usage

* Once a variable is assigned a value, you can use that variable throughout your code to refer to the stored value.
* You can perform operations on variables, pass them as arguments to functions, and use them in expressions and statements.
* For example: `print(age)`will display the value stored in the age variable.

### Python Data Structures

With a solid understanding of variables, we can now explore how to manage collections of data using lists, tuples, and dictionaries in Python. Each of these **data structures** has its own properties, use cases, and methods for manipulation and accessing elements. Lists and tuples are useful for storing and iterating over collections of elements, while dictionaries are ideal for fast lookup and retrieval of values based on keys. Understanding and utilizing these data structures effectively is crucial for organizing and manipulating data in Python programs.

### Lists

**Definition**: Ordered, mutable sequences that allow duplicate elements and are accessed by index.

**Syntax**: Defined using square brackets [].

**Properties**:

* Can contain elements of different types.
* Elements can be accessed using their index, starting from 0.
* Support various operations such as appending, removing, and slicing.

**Example**:

```
fruits = ["apple", "banana", "orange"]  
print(fruits[0])  # Output: "apple"  
fruits.append("grape")  
print(fruits)  # Output: ["apple", "banana", "orange", "grape"]
```

### Tuples

**Definition**: Ordered, immutable sequences that allow duplicate elements and are accessed by index.

**Syntax**: Defined using parentheses ().

**Properties**:

* Can contain elements of different types.
* Elements can be accessed using their index, starting from 0.
* Immutable, meaning once created, their elements cannot be modified.

**Example**:

```
point = (3, 4)  
print(point[0])  # Output: 3  
x, y = point  # Tuple unpacking  
print(x)  # Output: 3  
print(y)  # Output: 4
```

### Dictionaries

**Definition**: Unordered, mutable mappings of key-value pairs, where keys are unique and used for accessing values.

**Syntax**: Defined using curly braces {}.

**Properties**:

* Keys must be unique and immutable (e.g., strings or numbers).
* Values can be of any type.
* Provide fast lookup and retrieval of values based on their keys.

**Example**:

```
person = {"name": "John", "age": 25, "city": "New York"}  
print(person["name"])  # Output: "John"  
person["age"] = 30  
print(person)  # Output: {"name": "John", "age": 30, "city": "New York"}
```

### Python Data Types

Understanding these data structures sets the stage for exploring the various data types in Python, which are fundamental to effectively working with and manipulating data within your programs.

### Data Types

Python has several built-in data types, including:

* Numeric types: `int` (integers), `float` (floating-point numbers)
* Sequence types: `list`, `tuple`, `range`
* Text type: `str` (strings)
* Mapping type: `dict` (dictionaries)
* Set types: `set`, `frozenset`
* Boolean type: `bool`(True or False)

### String Conversions

Python provides functions to convert other data types to strings:

* `str()` Converts a value to a string representation
* `repr()` Returns a string representation of an object, typically used for debugging
* `format()` Allows formatting of strings using placeholders and variable substitution

```
num = 42
  
str_num = str(num)  # Converts the integer 42 to the string "42"
  
formatted_str = "The answer is {}".format(num)  # Formatted string
```

### Integer Conversions

Python provides functions to convert strings or floating-point numbers to integers:

* `int()`: Converts a value to an integer
* `float()`: Converts a value to a floating-point number

```
str_num = "42"  
num = int(str_num)  # Converts the string "42" to the integer 42  
float_num = 3.14  
int_num = int(float_num)  # Converts the float 3.14 to the integer 3
```

### Basic Math

Python provides various arithmetic operators for performing mathematical operations:

* `+`: Addition
* `-`: Subtraction
* `*`: Multiplication
* `/`: Division (returns a float)
* `//`: Floor division (returns an integer)
* `%`: Modulo (remainder)

```
result = 10 + 5  # Addition  
result = 10 - 3  # Subtraction  
result = 4 * 6  # Multiplication  
result = 10 / 3  # Division (returns 3.3333333333333335)  
result = 10 // 3  # Floor division (returns 3)  
result = 10 % 3  # Modulo (returns 1)  
result = 2 ** 3  # Exponentiation (returns 8)
```

### Boolean Fundamentals

* Boolean values in Python are represented by True and False.
* Comparison operators such as `==`, `!=`, `<`, `>`, `<=`,  `>=`return Boolean values.
* Logical operators and, or, and not are used to combine or negate Boolean values.

```
is_equal = (5 == 5)  # True  
is_greater = (10 > 20)  # False  
result = (5 < 10) and (10 < 15)  # True  
result = (5 < 10) or (10 > 15)  # True  
result = not (5 == 5)  # False
```

### Print Function

* The `print()`function is used to display output to the console.
* This function takes one or more arguments, which can be of different data types, and prints them to the console.

```
print("Hello, World!")  # Prints a string  
name = "Alice"  
print("My name is", name)  # Prints multiple arguments  
age = 25  
print(f"I am {age} years old")  # Prints a formatted string
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239132

Scraped At: 2026-05-14T15:17:35.043997
