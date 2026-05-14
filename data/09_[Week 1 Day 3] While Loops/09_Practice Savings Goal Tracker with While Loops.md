# Practice: Savings Goal Tracker with While Loops

# Practice: Savings Goal Tracker with While Loops

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Savings Goal Tracker with While Loops

* [Page: Introduction to While Loops (1 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239166 "Page: Introduction to While Loops (1 of 11)")
* [Page: What are While Loops? (2 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239170 "Page: What are While Loops? (2 of 11)")
* [Page: Examples: While Loops (3 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239171 "Page: Examples: While Loops (3 of 11)")
* [Page: Process: While Loops (4 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239173 "Page: Process: While Loops (4 of 11)")
* [Page: Summary: While Loops (5 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239175 "Page: Summary: While Loops (5 of 11)")
* [Page: Check for Understanding: While Loops (6 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239178 "Page: Check for Understanding: While Loops  (6 of 11)")
* [Page: Technical Lesson: While Loops (7 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239179 "Page: Technical Lesson: While Loops (7 of 11)")
* [Page: Current: Practice: Savings Goal Tracker with While Loops (8 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239181 "Page: Current: Practice: Savings Goal Tracker with While Loops (8 of 11)")
* [Discussion: While Loops (9 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239184 "Discussion: While Loops (9 of 11)")
* [Lab: Coding with While Loops (10 of 11), Assignment](https://moringa.instructure.com/courses/1391/modules/items/239186 "Lab: Coding with While Loops (10 of 11), Assignment")
* [Quiz: While Loops (11 of 11)](https://moringa.instructure.com/courses/1391/modules/items/239188 "Quiz: While Loops (11 of 11)")

5 min read

Imagine you're a junior programmer for a personal finance app company. The app helps users track their savings progress towards a specific goal. You're tasked with creating a program that motivates users to keep saving by displaying encouraging messages until they reach their savings goal.

### Instructions

### [Step 1: Define](#dpPanel0)

Create a program that:

* Sets a savings goal for the user
* Tracks the user's current savings
* Motivates the user with encouraging messages until they reach their goal
* Congratulates the user when they reach their goal

### [Step 2: Design](#dpPanel1)

Design the solution using a while loop to continuously check if the user has reached their goal and display motivational messages until they do.

* Task 1: Define Variables (savings goal and current savings)
* Task 2: Implement a While Loop
* Task 3: Integrate Input and Outcome
* Task 4: Display Results

### [Step 3: Develop](#dpPanel2)

### [Task 1: Define Variables](#dpPanel3)

Define the `savings_goal` as a variable and prompt the user for their initial `current_savings`.

### [Task 2: Implement a While Loop](#dpPanel4)

Use a while loop to iterate as long as the `current_savings` are less than the `savings_goal`.

### [Task 3: Integrate Input and Outcome](#dpPanel5)

Inside the loop:

* Display a motivational message encouraging the user to keep saving.
* Prompt the user to enter their additional savings amount.
* Update the `current_savings` variable with the new amount.

### [Task 4: Display Results](#dpPanel6)

Once the loop finishes (user reaches the goal), print a congratulatory message.

Here's a basic structure to get you started:

```
savings_goal = 1000  # Example goal, you can change this or ask the user to input it  
current_savings = float(input("Enter your current savings amount: $"))  
  
while current_savings < savings_goal:  
    # Your code here:   
    # 1. Print motivational message  
    # 2. Ask for additional savings amount  
    # 3. Update current_savings  
  
# Your code here: Print congratulatory message
```

### [Step 4: Test and Refine](#dpPanel7)

* Run your program with different starting amounts and savings goals.
* Verify that the appropriate messages are displayed based on the user's progress.
* Make any necessary adjustments to the while loop or code blocks to achieve the desired outcome.

### [Step 5: Document and Maintain](#dpPanel8)

* **Version Control**: Use version control to track changes; allowing for easy updates, collaborative editing, and the ability to revert to previous versions if necessary.
* **Regular Updates and Reviews**: Schedule regular reviews and updates for code ensure content remains relevant, accurate, and aligned with the latest Python developments and industry practices,
* **Documentation and Examples Repository**: Maintain a centralized repository containing all lab documents, example code, and solutions.

### Resources

* Refer to the technical lesson on while loops for a refresher.

### Tools

* Use the Python IDE or [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code") to write and test your code.
* Refer to the technical lesson on while loops if you need a refresher.

### Solution

### [Select for Solution](#dpPanel9)

Remember, the key to this exercise is correctly implementing the while loop to continue motivating the user until they reach their savings goal. Focus on getting the loop logic right before adding any extra features. Here is a sample of what your script could look like, with comments to explain each step.

```
# Task 1: Define Variables  
savings_goal = 1000  # Example savings goal  
current_savings = float(input("Enter your starting savings amount: $"))  
  
# Task 2: Implement a While Loop  
while current_savings < savings_goal:  
    # Task 3: Integrate Input and Outcome  
    print(f"Keep saving! You're ${savings_goal - current_savings:.2f} away from your goal.")  
    additional_savings = float(input("Enter the amount you've saved since last check: $"))  
    current_savings += additional_savings  
  
# Task 4: Display Results  
print("Congratulations! You've reached your savings goal!")  
  
# Step 4: Test and Refine  
# (Run the program with different inputs to verify it works as expected)  
  
# Step 5: Document and Maintain  
# Comments explaining the while loop:  
# The while loop continues as long as current_savings is less than savings_goal.  
# In each iteration, it calculates and displays the remaining amount to save,  
# prompts the user for additional savings, and updates the current_savings.  
# The loop exits when current_savings is no longer less than savings_goal.  
  
# Potential future enhancements:  
# - Allow user to set their own savings goal  
# - Track multiple savings goals  
# - Add a feature to visualize savings progress  
  
# Version control: Use git to track changes over time  
# Example commands:  
# git init  
# git add savings_tracker.py  
# git commit -m "Initial implementation of Savings Goal Tracker"  
  
# Explanation of the Solution:  
  
# 1. Variable Initialization:  
#    - We set savings_goal to 1000 as an example target.  
#    - We use input() to get the user's starting savings amount and convert it to a float.  
  
# 2. While Loop Implementation:  
#    - The condition 'current_savings < savings_goal' ensures the loop continues as long as  
#      the user hasn't reached their goal.  
#    - This is the core of our program, allowing repeated checks and updates.  
  
# 3. Inside the While Loop:  
#    - We calculate and display how much more the user needs to save.  
#    - The f-string allows us to format the output, showing the amount to two decimal places.  
#    - We prompt the user for their additional savings since the last check.  
#    - We update current_savings by adding the additional amount.  
#    - This process repeats with each loop iteration.  
  
# 4. Loop Termination:  
#    - The loop ends when current_savings is no longer less than savings_goal.  
#    - This occurs when the user has met or exceeded their savings target.  
  
# 5. Final Output:  
#    - Once the loop ends, we print a congratulatory message.  
  
# This solution demonstrates key aspects of while loops:  
# - Setting up a condition (current_savings < savings_goal)  
# - Repeatedly executing code while the condition is true  
# - Updating variables that affect the loop condition (current_savings)  
# - Automatically terminating when the condition becomes false
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239181

Scraped At: 2026-05-14T00:31:23.335832
