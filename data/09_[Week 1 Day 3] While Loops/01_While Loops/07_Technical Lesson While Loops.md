# Technical Lesson: While Loops

# Technical Lesson: While Loops

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Technical Lesson: While Loops

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

While loops are a fundamental control flow construct in Python that allow you to execute a block of code repeatedly as long as a certain condition remains true. This lesson will guide you through the essential steps of using while loops, employing a fitness app scenario to illustrate its practical application.

Imagine you're a junior programmer developing a fitness app that motivates users to reach their daily step goals. You need to create a program that prompts users for their current step count and keeps encouraging them to walk until they achieve their target.

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code")

### Instructions

The following video and steps will outline how to develop a script for the while loops.

[VIDEO LINK](https://player.vimeo.com/video/975473810?h=19820c030f)

### Step 1: Define the Problem

Imagine you're a junior programmer developing a fitness app that motivates users to reach their daily step goals.

You need to create a program that will prompts users for their current step count and encourages them to continue walking until they achieve their target.

### Step 2: Determine the Design

Determine the design. Establish the user's daily step goal (e.g., 10,000 steps) as the condition for the loop. Use a while loop to iterate as long as the user's current step count is less than the goal.

1. Define the variables (goal steps)
2. Integrate input and implement a loop
3. Implement the outcome
4. Display results

Develop pseudocode or programming flowchart for this program as part of your design.

### Step 3: Develop Code

### Task 1: Define the Variables

Define your outcome with setting a daily step goal. Define a variable, `goal_steps`, to store the user's daily step goal (e.g., `goal_steps = 10000`). 

```
goal_steps = 10000
```

### Task 2: Implement Input and Loop

Initialize current steps with a predefined count or prompt user for initial step. Start with a predefined step count, define a variable, `current_steps`, and assign a value (e.g., `current_steps = 0` ).

Implement prompting the user for their initial step count within the loop. Your script would look something like: 

```
goal_steps = 10000  
  
while True:  # Infinite loop (user exits with 'q' or 'quit')  
    current_steps = int(input("Enter your current step count (or 'q' to quit): "))  
  
    if current_steps < 0:
```

### Task 3: Implement the Conditions and Outcome

In this case, the condition is `current_steps` < `goal_steps`.

Display motivational message. Print an encouraging message to motivate the user to keep walking (e.g.,  `print("Keep going! You're almost there!")` .

Continue promoting the user to test the conditions and the ability of the loop.Use input to prompt the user for their current step count and store it in the `current_steps` variable (e.g., current\_steps `current_steps = int(input("Enter your current step count: "))`. Converting the input to an integer using int ensures proper comparison with the goal.

```
goal_steps = 10000  
  
while True:  # Infinite loop (user exits with 'q' or 'quit')  
    current_steps = int(input("Enter your current step count (or 'q' to quit): "))  
  
    if current_steps < 0:  
        print("Invalid input. Please enter a non-negative step count.")  
        continue  # Skip to the next iteration if input is invalid  
  
    if current_steps >= goal_steps:  
        print("Congratulations! You reached your daily step goal!")  
        break  # Exit the loop if goal is reached  
  
    print("Keep going! You're almost there!")
```

### Task 4: Display Result

Once the loop terminates because `current_steps` becomes greater than or equal to `goal_steps`, print a congratulatory message (e.g., `print("Keep going! You're almost there!")`).

```
goal_steps = 10000  
  
while True:  # Infinite loop (user exits with 'q' or 'quit')  
    current_steps = int(input("Enter your current step count (or 'q' to quit): "))  
  
    if current_steps < 0:  
        print("Invalid input. Please enter a non-negative step count.")  
        continue  # Skip to the next iteration if input is invalid  
  
    if current_steps >= goal_steps:  
        print("Congratulations! You reached your daily step goal!")  
        break  # Exit the loop if goal is reached  
  
    print("Keep going! You're almost there!")
```

### Step 4: Test and Refine

* Run your program with different number of occurrences and parameters for the outcome to test the behavior of the while loop.
* Practice coding both index and direct access for loops
* Verify that the appropriate code blocks are executed based on the conditions.
* Make any necessary adjustments to the while loop or code blocks to achieve the desired outcome.

### Step 5: Document and Maintain

* **Version Control**: Use version control to track changes; allowing for easy updates, collaborative editing, and the ability to revert to previous versions if necessary.
* **Regular Updates and Reviews**: Schedule regular reviews and updates for code ensure content remains relevant, accurate, and aligned with the latest Python developments and industry practices,
* **Documentation and Examples Repository**: Maintain a centralized repository containing all lab documents, example code, and solutions.

### Considerations

While loops are powerful tools for repetitive tasks, but there are some potential challenges and decision points to consider:

#### Infinite Loops

**Issue:** An incorrectly written while loop condition can lead to an infinite loop, where the loop never terminates.

**Solution:** Carefully design your loop condition to ensure it eventually becomes False, causing the loop to exit. In the fitness app example, we check if current\_steps is less than goal\_steps. Once the user reaches the goal, the condition becomes False, and the loop exits.

#### Input Validation

**Issue:** When updating a counter or condition variable within the loop, forgetting to increment or decrement by 1 can lead to unexpected behavior.

**Solution:** Double-check your calculations and variable updates within the loop. Consider using clear variable names and comments to improve readability.

#### Early Termination

**Issue**: In some cases, you might want to exit the loop prematurely based on a specific condition within the loop.

**Solution**: Use an if statement with a break statement to exit the loop when the desired condition is met. For example, you could add an option for the user to quit the program by entering 'q' or 'quit'.

#### Infinite Loops

**Decisions:** The loop condition determines how long the loop iterates.

**Impact:** Choosing the right condition is crucial. In the fitness app, we use current\_steps < goal\_steps to keep looping until the goal is reached. A different condition would lead to a different behavior.

#### Input Validation

**Decision:** You can choose to validate user input within the loop to ensure it meets certain criteria (e.g., non-negative step count).

**Impact:** Validation improves the user experience and prevents errors. In the example, we check for negative input and provide an error message.

#### Early Termination

**Decision:** We use an infinite loop (while True) with a way for the user to exit ('q' or 'quit').

**Impact:** This approach allows the program to keep prompting the user for steps until they explicitly choose to quit. An alternative would be to have a predefined number of iterations, but this wouldn't be as flexible for the fitness app scenario.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239179

Scraped At: 2026-05-14T15:22:00.550944
