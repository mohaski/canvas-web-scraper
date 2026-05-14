# Technical Lesson: For Loops

# Technical Lesson: For Loops

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Technical Lesson: For Loops

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

For loops are powerful tools in Python that allow you to execute a block of code repeatedly for each item in a sequence. This sequence can be a list, tuple, string, or any iterable object. In this lesson, we'll explore For loops through the context of a coin collection game.

**Scenario: Coin Collection Game**

Imagine you're a software developer designing a coin collection game. You need to implement a module that:

* Tracks the number of coins a player has collected
* Increments the coin count
* Checks if a milestone has been reached
* Displays congratulatory messages for reaching milestones

**Problem-Solving Process**

We'll follow this process to solve our problem:

1. **Define the sequence:** Identify the list of items you want to iterate through (e.g., coin milestones).
2. **Design the loop:** Use a for loop to access each item in the sequence.
3. **Perform actions:** Inside the loop, write the code you want to execute for each item (e.g., print congratulatory messages).

### Resources and Tools

* Before completing this technical lesson, be sure to review all the For Loops module content.
* Code along using the Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Video: Problem Solving Process with For Loops

Watch the following video to learn more about how to use the problem solving process when creating a script with for loops.

Sean: The code in this video shows a \*while\* loop, rather than a \*for\* loop. While loops were the previous module. It does not follow solution code and is not finished and runnable. I can redo this video if you want.

[VIDEO LINK](https://player.vimeo.com/video/1003497505?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

By following these steps and understanding the concept of for loops, you can automate repetitive tasks and iterate through sequences in your Python programs.

**Remember:** This is a basic example. You can modify the lists and the code within the loop to create more complex functionalities. Let's break down the steps to create a gaming program that congratulates players on reaching coin milestones:

### Step 1: Define the Problem

Our coin collection game needs to:

* Track collected coins
* Increment coin count
* Create milestones with congratulatory messages
* Check if a milestone has been reached

### Step 2: Design - Determine the Design

Build out your design before you write your code.

* **Task 1:** Define the variables by defining the milestones
* **Task 2:** Initialize the loop by iterating until milestones are achieved
* **Task 3:** Integrate user input determine between 2 different techniques for integrating input
* **Task 4:** Implement milestone output by defining the counters in this list
* **Task 5:** Display results and print congratulatory method

```
# Define variables with milestones  
Define list of coin_milestones  
Define list of congratulatory messages  
  
# Integrate input and implement milestone output by defining counters  
Define counter for tracking current coins  
  
# Initialize for loop  
For each milestone in coin_milestones:  
    # Integrate input (2 options: index or direct access)  
    Option 1: Find index of current milestone  
    Option 2: Directly access current milestone  
      
    Get corresponding message  
  
    # Display results  
    Print congratulatory message
```

### Step 3: Development - Write the Code

### Task 1: Define the Variables

We'll create two lists:

* `coin_milestones`: to store milestone values (e.g., 100, 500, 1000).

* `messages`: to store corresponding congratulatory messages (e.g., "Wow! You earned 100 coins!", "Excellent! You've reached 500 coins!", "Fantastic! You're a coin master!").

```
coin_milestones = [100, 500, 1000]  
messages = [...]
```

### Task 2: Initialize the for loop

We'll use a For loop to iterate through the `coin_milestones` list.

```
coin_milestones = [100, 500, 1000]  
messages = [...]  
  
for milestone in coin_milestones:
```

### Task 3: Implement milestone output

For this task, we'll explore two methods to access the current milestone and its corresponding message. These methods demonstrate different ways of integrating input within our For loop:

**Option 1:** Using index This method involves finding the position (index) of the current milestone within the `coin_milestones` list, and then using that index to access the corresponding message from the `messages` list.

```
coin_milestones = [100, 500, 1000]  
messages = [...]  
  
for milestone in coin_milestones:  
  # Option 1 (index)  
  current_message = messages[coin_milestones.index(milestone)]
```

Sean: Option 1 and Option 2 show the same code and are not different. I think I know what it was getting and and can change it if you want, but also we can just leave option 1 as the only solution

**Option 2:** Direct access This method directly accesses elements from both lists using a common index. It assumes that the `coin_milestones` and `messages` lists are in the same order and have the same length.

```
coin_milestones = [100, 500, 1000]  
messages = [...]  
  
for milestone in coin_milestones:# Option 2 (direct access)  
  current_message = messages[coin_milestones.index(milestone)]
```

Both of these options allow us to integrate the milestone (input) with its corresponding message (output). The choice between these methods depends on the specific requirements of your program and the structure of your data.

### Task 4: Implement milestone output

Now that we have our methods for integrating input, we can implement the milestone output.

The `messages` list that will also produce milestone output to the counters

* List two, `messages`, will hold the corresponding congratulatory messages (e.g., "Wow! You earned 100 coins!", "Excellent! You've reached 500 coins!", "Fantastic! You're a coin master!").

```
coin_milestones = [100, 500, 1000]  
messages = ["Wow! You earned 100 coins!",  "Excellent! You've reached 500 coins!", "Fantastic! You're a coin master!"]  
  
for milestone in coin_milestones:  
  # Option 1 (index)  
  current_message = messages[coin_milestones.index(milestone)]
```

### Task 5: Display results

Use the print function to print the congratulatory method.

```
coin_milestones = [100, 500, 1000]  
messages = ["Wow! You earned 100 coins!",  "Excellent! You've reached 500 coins!", "Fantastic! You're a coin master!"]  
  
for milestone in coin_milestones:  
  # Find the corresponding message for the current milestone (alternative approach)  
  current_message = messages[coin_milestones.index(milestone)]  
    
  # Print the congratulatory message  
  print(current_message)
```

### Step 4: Test and Refine

* Run your program with different number of occurrences and parameters to test the behavior of the for loop.
* Practice coding both index and direct access for loops
* Verify that the appropriate code blocks are executed based on the conditions.
* Make any necessary adjustments to the for loop or code blocks to achieve the desired outcome.

### Step 5: Document and Maintain

* **Version Control**: Use version control to track changes; allowing for easy updates, collaborative editing, and the ability to revert to previous versions if necessary.
* **Regular Updates and Reviews**: Schedule regular reviews and updates for code ensure content remains relevant, accurate, and aligned with the latest Python developments and industry practices,
* **Documentation and Examples Repository**: Maintain a centralized repository containing all lab documents, example code, and solutions.

### Considerations

For loops are a cornerstone of Python programming for iterating through sequences. Here are some key considerations around challenges and decisions to keep in mind:

#### Challenges

##### Index Errors

**Issue**

In Option 1 (using index), if a coin milestone doesn't exist in the `coin_milestones` list, trying to access the corresponding message using `messages[coin_milestones.index(milestone)]` will raise an IndexError.

**Solution**

**Validation:** Before accessing messages, check if the milestone exists in `coin_milestones` using `if milestone in coin_milestones:`.

**Default message:** Consider having a default message for milestones not explicitly listed.

##### Unequal List Lengths

**Issue**

If the `coin_milestones` and `messages` lists have different lengths, using Option 2 (direct access) can lead to errors if you try to access a message index that doesn't exist.

**Solution**

**Ensure equal lengths:** Maintain the same order and number of elements in both lists.

**Default message:** Similar to index errors, provide a default message for unmatched milestones.

##### Modifying Sequences During Iteration

**Issue**

Modifying the sequence you're iterating through within the loop can lead to unexpected behavior or errors.

**Solution**

**Copy the sequence:** Create a copy of the original sequence to iterate through and modify the copy if needed.

**Process after loop:** Defer modifications to the original sequence until after the loop completes.

#### Decisions

##### Accessing Elements (Index vs. Direct Access)

**Decision**

Choose between using the index  `(coin_milestones.index(milestone)` or direct access `(messages[coin_milestones.index(milestone)])` based on your list structure and preference.

**Impact**

**Index**offers more flexibility (e.g., handling missing milestones), but requires validation to avoid errors.

**Direct access** is simpler but relies on maintaining the same order and length in both lists.

##### Handling Unequal Lists:

**Decision**

Determine how to handle cases where the `coin_milestones` and messages lists might have different lengths.

**Impact**

**Validation** adds complexity but prevents errors.

**Default messages provide a fallback for unmatched milestones but require defining.**

##### Modifying Sequences

**Decision**

Decide if and how to modify the sequence you're iterating through within the loop.

**Impact**

Modifying the sequence during iteration can be tricky, so consider alternatives like copying or processing after the loop.

### Summary

This lesson has guided you through the process of using For loops in Python to solve a practical problem - tracking milestones in a coin collection game. By following the problem-solving steps and considering the challenges and decisions involved, you've gained valuable experience in applying For loops to real-world scenarios.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239205

Scraped At: 2026-05-14T15:51:58.575054
