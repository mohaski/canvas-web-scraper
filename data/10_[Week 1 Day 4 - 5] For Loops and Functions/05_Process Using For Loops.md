# Process: Using For Loops

# Process: Using For Loops

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Process: Using For Loops

* [Page: Introduction to For Loops and Functions (1 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239191 "Page: Introduction to For Loops and Functions (1 of 18)")
* [Page: What are For Loops? (2 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239194 "Page: What are For Loops? (2 of 18)")
* [Page: For Loops: An Example (3 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239196 "Page: For Loops: An Example (3 of 18)")
* [Page: Current: Process: Using For Loops (4 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239197 "Page: Current: Process: Using For Loops  (4 of 18)")
* [Page: Summary: For Loops (5 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239199 "Page: Summary: For Loops (5 of 18)")
* [Page: Considering While Loops and For Loops (6 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239201 "Page: Considering While Loops and For Loops  (6 of 18)")
* [Page: Check for Understanding: For Loops (7 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239203 "Page: Check for Understanding: For Loops (7 of 18)")
* [Page: Technical Lesson: For Loops (8 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239205 "Page: Technical Lesson: For Loops  (8 of 18)")
* [Page: Practice: For Loops (9 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239206 "Page: Practice: For Loops  (9 of 18)")
* [Page: Introduction to Functions (10 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239210 "Page: Introduction to Functions  (10 of 18)")
* [Page: What are Functions? (11 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239211 "Page: What are Functions? (11 of 18)")
* [Page: Process: Using Functions (12 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239213 "Page: Process: Using Functions (12 of 18)")
* [Page: Summary: Functions (13 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239215 "Page: Summary: Functions (13 of 18)")
* [Page: Check for Understanding: Functions (14 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239217 "Page: Check for Understanding: Functions (14 of 18)")
* [Discussion: For Loops (15 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239220 "Discussion: For Loops (15 of 18)")
* [Lab: Coding with Functions (16 of 18), Assignment](https://moringa.instructure.com/courses/1391/modules/items/239222 "Lab: Coding with Functions (16 of 18), Assignment")
* [Lab: Coding with For Loops (17 of 18), Assignment](https://moringa.instructure.com/courses/1391/modules/items/239224 "Lab: Coding with For Loops (17 of 18), Assignment")
* [Quiz: For Loops and Functions (18 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239226 "Quiz: For Loops and Functions (18 of 18)")

2 min read

Imagine you're a junior developer at a tech company and have been tasked with manipulating a list of numbers. Your goal is to square each number in the list and print the result.

Here's a breakdown of the steps involved in using a for loop in Python:

### [1. Define the Sequence](#dpPanel0)

* Prepare the iterable object you want to iterate through. This could be a list, tuple, string, dictionary (for keys), or set.
* Make sure the elements in the sequence are arranged in a way that makes sense for your loop's purpose.

```
numbers = [1, 2, 3, 4, 5]
```

### [2. Set Up the Loop](#dpPanel1)

Use the `for` keyword followed by a loop variable and the `in` keyword.

* **Loop Variable:** Choose a descriptive name for this variable as it will represent the current element during each iteration.
* **`in` Keyword:** This specifies that the loop will iterate over the elements in the sequence you defined.

```
for number in numbers:
```

### [3. Create the Loop Body](#dpPanel2)

* Indent the code block that you want to execute for each element in the sequence. This is where the actual processing or manipulation of the elements happens.
* You can access the current element using the loop variable within the loop body.

```
squared_number = number * number
```

### [4. Access the Element (Optional)](#dpPanel3)

* Inside the loop body, use the loop variable to refer to the current element you're working with in each iteration.

```
print(squared_number)
```

### For Loop: Example Code

Review the following example with all parts pulled together:

```
numbers = [1, 2, 3, 4, 5]  
  
# Loop to square each number  
for number in numbers:  
  squared_number = number * number  # Access and manipulate the element  
  print(squared_number)
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239197

Scraped At: 2026-05-14T00:32:41.397616
