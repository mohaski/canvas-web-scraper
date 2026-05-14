# Technical Lesson: Common String Operations on Unstructured Text Data

# Technical Lesson: Common String Operations on Unstructured Text Data

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Common String Operations on Unstructured Text Data

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[15-20 minutes]

Data in the form of free unstructured text is ubiquitous. You will likely encounter data in this form in any field that you might go into. Think of posts on social media platforms, customer reviews on e-commerce sites, legal briefs, doctor’s notes and written medical diagnoses, training manuals for a manufacturing company, academic research articles , etc.

There is potentially useful information contained in these documents and we want to extract this information and represent it in a way that can be used for pattern recognition and statistical learning tasks. For example, we might want to learn what words and semantic structures are likely to indicate whether a social media post is toxic. The very first step in such a task would involve removing any formatting issues or special characters from the free text that do not contribute relevant context to the task at hand, and chunking it into **tokens, or basic units of semantic meaning**. Tokens could be words or punctuation or could even be parts of words like word roots and contractions. Once these tokens are created, you’ll encounter a plethora of tasks – such as learning numeric representations of what these tokens mean in relationship to each other and in the context of a given sentence.

While the cleaning and token creation process typically involves language-specific chunking rules, there are many methods we have already covered ( .strip(), .replace(), .lower() ) as well as a few other new string methods (.split(), .join()) that are employed universally. In this lesson, we'll look at an example of the string cleaning and tokenization process on an example tweet that needs some initial string cleaning.

Here is a video walkthrough of the technical lesson.

[VIDEO LINK](https://player.vimeo.com/video/989669248?h=37d8c1c730)

### Instructions

Using the example tweet below, we will work on cleaning:

* Some erroneous numeric characters
* Tab (\t)
* New line special characters (\n)
* Leading white space

They provide formatting information, but are not semantically meaningful.

```
free_text = "\t       Mary had a littl0e lamb and th0en I ate it \n "  
print(free_text)  
free_text
```

```
Mary had a littl0e lamb and th0en I ate it  
'\t       Mary had a littl0e lamb and th0en I ate it \n'
```

### Step 1

#### Addressing Whitespace, Case Inconsistencies, and Unwanted Characters

One common operation is to make all casing consistent for further processing downstream. In this case, we will lower case everything. This ensures that a given word is represented by the same token regardless of how it was originally cased. In this lesson, we will lower case everything. Let's accomplish the removal of unnecessary characters and lower casing all at once by method chaining our various cleaning tasks.

**Input:**

```
cleaned_free_txt = free_text.strip().replace('0', '').lower()  
  
cleaned_free_txt
```

**Output:**

```
'mary had a little lamb and then i ate it'
```

### Step 2

#### Structuring Free Text

##### The .split() method

At this point the data while cleaned is still unstructured. It is just a string. The next step taken in structuring this data for further analysis is to segment or **tokenize** the sentence into semantically meaningful units. In this case, it just means separating this string into a list containing its constituent words.

The .split(sep) method takes a string and splits it on a given separator (sep) into a list of strings. The default separator is ‘\s’ which corresponds to spaces. Using this method on our string has the desired effect.

**Input:**

```
token_list = cleaned_free_txt.split()  
  
token_list
```

**Output:**

```
['mary', 'had', 'a', 'little', 'lamb', 'and', 'then', 'i', 'ate', 'it']
```

### Step 3

#### Reversing the Splitting Process (When Applicable)

##### The .join() method

Sometimes we want to reverse the splitting process. Typically, this is something you might do if you want the cleaned and case-normalized text  to file. You would take your processed list and convert it back to a string to save to text file. This is where the string join method can be really useful. The .join(iterable) method takes in an iterable like a tuple or a list of strings. It has the effect of joining all of the elements of the list separated by a specified string. Let us see this in action by reversing the splitting process we just performed. We join the list with a “ “ separator using the following syntax:

**Input:**

```
" ".join(token_list)
```

**Output:**

```
'mary had a little lamb and then i ate it'
```

Of course, this method is perfectly general. We could have used any string in there.

### Summary

This technical lesson walked you through important Python string commands for the cleaning and tokenization of unstructured text. These included string methods you had already seen before like .strip(), .replace(), and casing commands such as .lower(). We also introduced useful commands like .split() and .join() that were used for text tokenization and merging tokens back to contiguous strings to get ready for export of cleaned data to text file.

Before departing the subject, we point out that the .split() and .join() methods are generally useful and not just confined to dealing with free text. Any time you need to split a string on a specific delimiter, whether it be free text or a string value in a tabular dataset, then .split() will be of use to you. This goes similarly for .join(): concatenating strings that might be contained in multiple elements of a row is easily accomplished with the .join() method (e.g. joining [Title, First Name, Last Name, Suffix] in multiple columns to a single Name string).

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243495

Scraped At: 2026-05-14T20:46:51.155408
