# Practice: For Loops

# Practice: For Loops

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: For Loops

Icon Progress Bar (browser only)

4 min read

In this lab, you'll work on a simple game development task that requires you to use for loops to iterate through lists and display messages. This practice is not graded, so feel free to experiment and learn from the process. If you get stuck, remember to refer back to your notes from the technical lesson and don't hesitate to use Python's documentation.

The skills you practice here are fundamental to many programming tasks, especially in game development where you often need to process lists of items, levels, or achievements. Let's get started!

### **Scenario**

Imagine you work for a mobile game company as a junior programmer. One of your tasks is to develop a simple achievement system for a new puzzle game. Players earn stars as they solve puzzles. You need to write a program that displays a message congratulating the player on reaching certain star milestones.

### **Problem-Solving Process**

1. **Define the problem:** Identify the specific star milestones and the corresponding congratulatory messages.
2. **Design the solution:** Use a for loop to iterate through the star milestones and print the appropriate message for each milestone.
3. **Implement the solution:** Write Python code to achieve the desired outcome.
4. **Test and refine:** Run the code and verify it works as expected. Make adjustments as necessary.

### Resources and Tools

* This practice builds upon the concepts covered in the for loop technical lesson.
* Code along using the Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Instructions

This practice will help you solidify your understanding of for loops in Python. Complete the following tasks:

### [Task 1: Define Star Milestones and Messages](#dpPanel0)

* Create a list called `star_milestones` with at least three milestone values (e.g., [10, 50, 100]).
* Create a corresponding list called `achievement_messages` with congratulatory messages for each milestone.

### [Task 2: Iterate Through Milestones](#dpPanel1)

Use a for loop to iterate through the list of star milestones.

### [Task 3: Print Achievement Messages](#dpPanel2)

* Inside the for loop, access the current star milestone and the corresponding message from their respective lists.
* Use the print function to display a message congratulating the player on reaching the current milestone.

### [Code Snippet](#dpPanel3)

Here's a code snippet to get you started. Replace the placeholders with your lists:

```
star_milestones = [PLACEHOLDER_LIST_OF_STAR_MILESTONES]  
achievement_messages = [PLACEHOLDER_LIST_OF_MESSAGES]  
  
for milestone in star_milestones:  
    # Find the corresponding message for the current milestone  
    # Hint: You can use the index() method or direct indexing  
      
    # Print the achievement message  
    # Your code here
```

### Solution

### [Select for Solution](#dpPanel4)

Once you've completed the practice lab, you can compare your solution to this example. Remember, there are often multiple ways to solve a problem in programming, so your solution might look different but still be correct.

```
# Task 1: Define Star Milestones and Messages  
star_milestones = [10, 50, 100]  
achievement_messages = [  
    "Great start! You've earned 10 stars!",  
    "Halfway there! 50 stars earned!",  
    "Wow! You're a star master with 100 stars!"  
]  
  
# Task 2 & 3: Iterate Through Milestones and Print Achievement Messages  
for milestone in star_milestones:  
    # Find the corresponding message for the current milestone  
    message_index = star_milestones.index(milestone)  
    current_message = achievement_messages[message_index]  
      
    # Print the achievement message  
    print(current_message)  
  
# Optional: Display total number of milestones  
print(f"\nCongratulations! You've reached {len(star_milestones)} milestones in total!")
```

### [Explanation of Solution](#dpPanel5)

Explanation of this sample solution:

1. We start by defining two lists: `star_milestones` for the milestone values and `achievement_messages` for the corresponding messages.
2. The `for` loop iterates through each milestone in the `star_milestones` list.
3. Inside the loop, we use the `index()` method to find the position of the current milestone in the `star_milestones` list. This index is then used to access the corresponding message from the `achievement_messages` list.
4. We print each achievement message as the loop progresses through the milestones.
5. After the loop, we print a final message showing the total number of milestones reached, demonstrating how we can use the `len()` function with our list.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239206

Scraped At: 2026-05-14T15:52:06.036797
