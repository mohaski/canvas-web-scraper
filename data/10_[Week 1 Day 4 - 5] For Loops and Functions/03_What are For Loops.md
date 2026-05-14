# What are For Loops?

# What are For Loops?

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) What are For Loops?

* [Page: Introduction to For Loops and Functions (1 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239191 "Page: Introduction to For Loops and Functions (1 of 18)")
* [Page: Current: What are For Loops? (2 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239194 "Page: Current: What are For Loops? (2 of 18)")
* [Page: For Loops: An Example (3 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239196 "Page: For Loops: An Example (3 of 18)")
* [Page: Process: Using For Loops (4 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239197 "Page: Process: Using For Loops  (4 of 18)")
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

5 min read

In the world of programming, automation is key. Often, you'll need to perform the same task repeatedly on a list of items, update values, or iterate through a sequence of numbers. This is where for loops come in! They are powerful tools that allow you to execute a block of code a specific number of times or for each item in a sequence.

Imagine you're a data analyst working with a large dataset of customer names. You might need to clean the data by converting all names to uppercase or lowercase. A for loop can automate this process, saving you significant time and effort.

In Python programming, for loops are a fundamental tool that allow you to iterate (loop through) a sequence of elements in an automated way. They excel at processing collections of data efficiently, saving you time and effort compared to writing repetitive code for each element.

**Iterables** are special data structures in Python that you can loop through to access their elements one by one. Common iterables include lists, tuples, strings, dictionaries (for keys), and sets.

### How Do For Loops Work?

Review each of the following for loop features to learn more about how for loops work in Python:

### [Initialization](#dpPanel0)

* You define a loop variable using a descriptive name that reflects the purpose of the element it will hold during each iteration.
* This variable is not assigned a value initially, but it will be assigned the value of each element in the sequence as the loop progresses.

In the code block, `for` initiates the loop with the keyword:

```
for loop_variable in iterable_object:        
  # indented code block (loop body)
```

### [Implicit Condition](#dpPanel1)

* Unlike while loops, for loops don't have an explicit condition that needs to be True for the loop to continue. The loop's internal mechanism is designed to iterate through the entire sequence you provide.

The `loop_variable`  takes on the value of each element in the `iterable_object` during each iteration of the loop. Choose a descriptive name that reflects the element's purpose.

```
for loop_variable in iterable_object:        
  # indented code block (loop body)
```

### [Loop Body Execution](#dpPanel2)

* The indented block of code following the for line defines the actions you want to perform for each element in the sequence.
* Inside this block, you can access the current element using the loop variable you defined earlier.
* The code within the loop body can involve various operations like printing, manipulating the element, or performing calculations based on its value.

### [Automatic Increment (Implicit)](#dpPanel3)

* This is another key difference from while loops. After the loop body finishes executing for the current element, the loop variable is automatically assigned the value of the next element in the sequence.
* This happens implicitly without needing an explicit increment statement within the loop.
* The loop continues iterating through the sequence until it reaches the last element.

#### Example

For Loops code:

```
for loop_variable in iterable_object:        
  # indented code block (loop body)
```

#### Explanation

* Initiates the loop with the keyword `for`.
* **Implicit Condition** - The `loop_variable` takes on the value of each element in the `iterable_object` during each iteration of the loop. Choose a descriptive name that reflects the element's purpose.
* `in` **keyword****:** Specifies that the loop will iterate over the elements in the `iterable_object`.
* **Indented Code Block (Loop Body)****:** This block contains the code you want to execute for each element in the sequence. You can access the current element using the `loop_variable` within this block.

### Example: For Loop

Take a minute to review the following example of a for loop.

Imagine you have a box filled with cookies, and you want to eat them one by one. A for loop would be like having a special cookie picker that automatically does these things.

1. **Initializes:** It has a hand that's initially empty (no cookie yet).
2. **Implicit Condition (Always True):** As long as there are cookies in the box, the picker keeps working.
3. **Body:** It picks up the next cookie from the box.

* You (the programmer) decide what to do with the cookie in your code (loop body)*—*eat it (perform an action), count it (manipulate the element), etc.

4. **Automatic Increment:** After you're done with the current cookie, the picker automatically reaches for the next one in the box.
5. **Continual Process:** This process continues until all the cookies (elements) in the box (sequence) are gone.

### [For Loop Flowchart](#dpPanel4)

Here is an example of how the cookie scenario could be mapped out with a flowchart.

![For Loop flowchart for cookie analogy](https://moringa.instructure.com/courses/1391/files/620173/preview)


This flow chart is how to create a while loop about eating cookies.

### Conceptualization: For Loop

* **Initialization**: The loop variable is set to hold each element from the sequence.
* **Implicit Condition:** The loop continues to iterate through the entire sequence.
* **Loop Body Execution:** The indented code block performs actions on each element.
* **Automatic Increment:** The loop variable automatically moves to the next element.

conceptualize for loop

| For Loop Section | Definition | Code Block | Example |
| --- | --- | --- | --- |
| Initialization | Define a loop variable to hold each element in the sequence during each iteration. | ``` for item in iterable: ``` | Here, cookie is the loop variable that will take on the value of each element in `'box_of_cookies'` |
| Implicit Condition | The loop iterates through the entire sequence provided without needing an explicit condition. The loop stops when all elements are processed. | ``` for item in iterable: ``` | The loop continues until all cookies in `'box_of_cookies'` are picked. |
| Loop Body Execution | The indented block of code that performs actions on each element in the sequence. The loop variable can be used within this block. | ``` # code block (loop body) ``` | This prints a statement for each cookie, simulating the action of eating each cookie. |
| Automatic Increment (Implicit) | After the loop body executes for the current element, the loop variable is automatically assigned the next element in the sequence. | ``` # code block (loop body) ``` | Automatically moves to the next cookie after printing. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239194

Scraped At: 2026-05-14T00:32:18.451538
