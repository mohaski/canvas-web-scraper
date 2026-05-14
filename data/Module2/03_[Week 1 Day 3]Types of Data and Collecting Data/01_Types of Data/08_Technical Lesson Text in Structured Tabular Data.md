# Technical Lesson: Text in Structured Tabular Data

# Technical Lesson: Text in Structured Tabular Data

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Text in Structured Tabular Data

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[15-20 minutes]

Now that we have discussed the various types of data and their importance in data science, it’s time to look at how we can use that knowledge. In this technical lesson, we will guide you through handling text in structured tabular data. This lesson builds on your understanding of data types by applying Python’s built-in string methods to clean and preprocess textual data. You will learn how to manage inconsistencies in string formatting, remove special characters, and ensure data uniformity, which are essential skills for any data scientist.

Here is a video walkthrough of the technical lesson.

[VIDEO LINK](https://player.vimeo.com/video/989669183?h=f25ba79f8f)

### Why Common String Operations on Structured Data are Important

In data science, the quality of your data directly impacts the accuracy of your analysis and models. Text data, in particular, often comes with various inconsistencies and issues that need to be addressed before it can be used effectively. When dealing with structured data, such as tables, it’s common to encounter text fields that require cleaning and standardization. First, let's look at the fundamental string operations necessary to transform messy text data into a usable format. Understanding and applying these operations is crucial because they help you ensure data consistency, which leads to more reliable and valid results.

Strings are commonly encountered in both structured and unstructured data. Cleaning tasks and transformations are necessary to make this text data useful. These tasks include:

* Ensuring consistent string formatting and casing.
* Removing special characters and correcting typos.

You will use Python to perform these tasks on a sample dataset. The dataset contains people’s names, their age, current state of residence, and their college alma mater.

#### **Common String Operations on Structured Data**

Structured records (e.g., tables) often contain information like the names of people, locations, or the groups (or categories) that an observation belongs to. This data is stored in string format in Python.

In this lesson, we have a table containing people’s names, their age, current state of residence, and their college alma mater. The alma mater is a categorical feature that describes groups that each person belongs to. It is an example of a **nominal categorical**.

Data: Nominal Categorical Example

| Name | Age | State of Residence | Alma Mater |
| --- | --- | --- | --- |
| @Sarah Jones | 28 | NY | Columbia University |
| David Miller | 32 | NJ | New York University |
| Emily Li | 21 | CA | City University of New York |
| Michael Garcia | 42 | AZ | columbia university |
| Amanda Hernandez | 35 | NY | New York University |
| William Lee | 25 | PA | City University of New York |
| Olivia Brown | 40 | NY | COLUMBIA UNIVERSITY |
| Noah Patel | 30 | NJ | New York University |
| Sophia Chen | 23 | CA | City University of New York |
| Ethan Johnson | 45 | NY | Columbia University |
| Isabella Davis | 27 | PA | New York University |
| Lucas Ramirez | 38 | AZ | City University of New York |
| #Ava Wilson | 29 | CA | Columbia university |
| @Daniel Robinson | 43 | NJ | New York University |
| Mia Moore | 24 | PA | City University of New York |

Using common string operations, let’s clean up this data.

### Steps to Clean Text Data

* [Step 1: Check for String Inconsistencies](#dpPanel0Content)
* [Step 2: Remove Whitespace](#dpPanel1Content)
* [Step 3: Dealing with Case Inconsistencies](#dpPanel2Content)
* [Step 4: Removing Unwanted Characters](#dpPanel3Content)

### Step 1: Check for String Inconsistencies

First, we load the tabular dataset and extract the alma maters as a list. This step involves loading the data into Python and examining it for any inconsistencies.

**Instructions:**

1. Extract the ‘Alma Mater’ values into a list.

```
alma_mater_list = [x['Alma Mater'] for x in data]
```

1. Perform a type check on the elements of our list to ensure they are encoded as strings.

**Input:**

```
alma_dtype = []  
  
for elem in alma_mater_list:  
    alma_dtype.append(type(elem))  
  
alma_dtype
```

**Output:**

```
[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
```

1. Inspect the alma mater list for inconsistencies.

**Input:**

```
alma_mater_list
```

**Output:**

```
 ['Columbia University  ',  
 'New York University',  
 'City University of New York',  
 'columbia university  ',  
 'New York University',  
 'City University of New York',  
 'COLUMBIA UNIVERSITY',  
 'New York University',  
 'City University of New York',  
 'Columbia University',  
 'New York University',  
 'City University of New York',  
 'Columbia university',  
 'New York University',  
 'City University of New York']
```

Further inspection reveals some data quality issues. There are several variants of ‘Columbia University’ with trailing whitespace and different cases. We need to make sure that all strings signifying Columbia University are consistent. Let’s look at how to deal with whitespace issues and case consistency in Python.

#### Whitespace and the .strip() operation

Spaces after or preceding the actual text are a common problem in both structured and unstructured text. This is referred to as trailing or leading **whitespace** respectively. It is usually the result of formatting issues during the data entry process or issues during the text parsing process. Spaces are actual characters in Python and this means that a string like ‘Columbia University   ‘ is not the same as ‘Columbia University’.

1. Compare the first and tenth elements of the list of alma maters:

**Input:**

```
alma_mater_list[0] == alma_mater_list[9]
```

**Output:**

```
('Columbia University  ', 'Columbia University')
```

**Input:**

```
alma_mater_list[0] == alma_mater_list[9]
```

**Output:**

```
False
```

While these strings correspond to the same institution, the presence of whitespace leads Python to interpret them as inequivalent.

1. The string module’s .strip() method can take care of such trailing and leading whitespaces quite easily:

**Input:**

```
alma_mater_list[0]
```

**Output:**

```
 'Columbia University  '
```

**Input:**

```
alma_mater_list[0].strip()
```

**Output:**

```
'Columbia University'
```

1. Applying this to the whole list is easy with either a for loop, a map() operation, or a list comprehension.

**Input:**

```
alma_mater_list = [elem.strip() for elem in alma_mater_list]  
alma_mater_list
```

**Output:**

```
 ['Columbia University',  
 'New York University',  
 'City University of New York',  
 'columbia university',  
 'New York University',  
 'City University of New York',  
 'COLUMBIA UNIVERSITY',  
 'New York University',  
 'City University of New York',  
 'Columbia University',  
 'New York University',  
 'City University of New York',  
 'Columbia university',  
 'New York University',  
 'City University of New York']
```

Now that we have taken care of whitespaces with the .strip() method, let us turn our attention to case inconsistencies.

#### Dealing with Case Inconsistencies

A perusal of the list shows that there are casing inconsistencies in the entries for Columbia University. 

**Input:**

```
alma_mater_list[0], alma_mater_list[3], alma_mater_list[6]
```

**Output:**

```
 ('Columbia University', 'columbia university', 'COLUMBIA UNIVERSITY')
```

There are three main string methods that can be used to address casing inconsistencies like these.

**.upper()**: Converts all characters in the string to uppercase. Example: "Columbia University" becomes "COLUMBIA UNIVERSITY"

**.lower()**: Converts all characters in the string to lowercase. Example: "COLUMBIA UNIVERSITY" becomes "columbia university"

**.title()**: Converts the first letter of each word to uppercase and the rest to lowercase. Example: "columbia university" becomes "Columbia University" (no change in this case)

Which one you choose will depend on the particular situation you are faced with. In this case, we will pass the .title() method through the whole list to create a new cleaned list.

**Input:**

```
cleaned_list = []  
for elem in alma_mater_list:  
    cleaned_list.append(elem.title())  
  
cleaned_list
```

**Output:**

```
 ['Columbia University',  
 'New York University',  
 'City University Of New York',  
 'Columbia University',  
 'New York University',  
 'City University Of New York',  
 'Columbia University',  
 'New York University',  
 'City University Of New York',  
 'Columbia University',  
 'New York University',  
 'City University Of New York',  
 'Columbia University',  
 'New York University',  
 'City University Of New York']
```

#### Removing Unwanted Characters

##### The .replace() method

These are not the only string cleaning tasks that you will be confronted with. For example, you might need to remove certain characters appearing in names that were not appropriately filtered out during the data collection process. Hashtags ‘#’ or mentions ‘@’ would be an example of such special characters. Extracting the list of names from our table and inspecting a few of the elements, we can see these special characters appearing in front of names.

**Input:**

```
name_list = [x['Name'] for x in data]  
name_list  
  
  
name_list[0], name_list[-2], name_list[-3]
```

**Output:**

```
 ('@Sarah Jones', '@Daniel Robinson', '#Ava Wilson')
```

The .replace() method is used to find all examples of a given substring pattern and replace it with another. We can use this method to find all examples of ‘@’ for a given string and replace it with the empty string ‘’. The first two arguments of the function are, in order: the string pattern to find and replace, the string to replace the pattern with.

**Input:**

```
# .replace(string_to_replace, replacement)  
name_list[0].replace('@', '') # removing @ for Sarah Jones
```

**Output:**

```
'Sarah Jones'
```

We can do a similar thing for ‘#Ava Wilson’

**Input:**

```
print(name_list[-3]) # before  
print( name_list[-3].replace('#', '') )# after cleaning with .replace()
```

**Output:**

```
#Ava Wilson  
Ava Wilson
```

We can use method chaining to apply both cleaning operations through the entire names list.

**Input:**

```
cleaned_names = [elem.replace('@', '').replace('#', '') for elem in name_list]  
cleaned_names
```

**Output:**

```
['Sarah Jones',  
 'David Miller',  
 'Emily Li',  
 'Michael Garcia',  
 'Amanda Hernandez',  
 'William Lee',  
 'Olivia Brown',  
 'Noah Patel',  
 'Sophia Chen',  
 'Ethan Johnson',  
 'Isabella Davis',  
 'Lucas Ramirez',  
 'Ava Wilson',  
 'Daniel Robinson',  
 'Mia Moore']
```

### Summary

In this technical lesson, you were introduced to examples of text features in tabular data and their representation as Python strings embedded in nested data structures (e.g a list of dicts). There were various casing and formatting inconsistencies and common unwanted characters contained within the different text features. You saw how Python’s native string methods could be used to take care of each of these issues: in particular, the .lower(), .upper(), .title(), .strip(), and .replace() methods.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243494

Scraped At: 2026-05-14T20:46:45.268262
