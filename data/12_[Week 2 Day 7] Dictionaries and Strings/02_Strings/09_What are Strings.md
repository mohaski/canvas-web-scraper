# What are Strings?

# What are Strings?

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) What are Strings?

Icon Progress Bar (browser only)

2 min read

A string is a sequence of characters enclosed in either single quotes (') or double quotes ("). These characters can be letters, numbers, symbols, or spaces. Here are some key concepts to remember about strings:

### Immutable

Once created, a string's content cannot be changed. You can't modify individual characters within a string, but you can create a new string based on the original.

### Ordered

The characters in a string have a specific order, starting from index 0. You can access individual characters using their index position within square brackets [].

The video below will guide you through each step of strings. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding.

[VIDEO LINK](https://player.vimeo.com/video/1003497468?h=a9e3d03f71)

### How Do Strings Work?

Strings behave like sequences, where each character has a designated position (index). Python keeps track of these characters and allows you to access, slice, or manipulate them using various methods. For instance, you can retrieve a specific character by its index, extract a portion of the string (slice), or combine strings using the + operator.

### Conceptualization: Parts of Strings

Parts of strings with definition and example

| Part of a String | Definition | Example |
| --- | --- | --- |
| Immutable | Once created, a string's content cannot be changed. You can't modify individual characters within a string, but you can create a new string based on the original. | ``` original = "hello" new_string = original + " world"  # new_string is "hello world" ``` |
| Ordered | The characters in a string have a specific order, starting from index 0. You can access individual characters using their index position within square brackets []. | ``` greeting = "hello"  first_letter = greeting[0]  # first_letter is 'h' ``` |
| Indexing | Accessing individual characters in a string using their position. | ``` word = "Python"  third_letter = word[2]  # third_letter is 't' ``` |
| Slicing | Extracting a portion of the string by specifying a range of indices. | ``` phrase = "Hello, World!"  substring = phrase[0:5]  # substring is 'Hello' ``` |
| Concatenation | Combining strings using the + operator. | ``` str1 = "Hello"  str2 = "World"  combined = str1 + " " + str2  # combined is 'Hello World' ``` |
| Length | The number of characters in a string, including spaces and symbols. | ``` message = "Hello, World!"  length = len(message)  # length is 13 ``` |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239280

Scraped At: 2026-05-14T15:57:45.806562
