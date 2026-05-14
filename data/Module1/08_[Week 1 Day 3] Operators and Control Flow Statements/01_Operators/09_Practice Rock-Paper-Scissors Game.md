# Practice: Rock-Paper-Scissors Game

# Practice: Rock-Paper-Scissors Game

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Rock-Paper-Scissors Game

Icon Progress Bar (browser only)

3 min read

In this practice lab, you'll create a simple Rock-Paper-Scissors game using Python that will be played between a human player and computer. You'll go through the entire development process, starting with pseudocode, then creating a flowchart, and finally implementing and testing your code.

### **Game Rules**

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock

### Tools Needed

* Python IDE or [Visual Studio Code


  Links to an external site.](https://code.visualstudio.com/ "Link") with Python extension

### Instructions

### Program Flow Diagram for Planning

Study the following flow diagram carefully. You will need a series of if-elif-else and the comparison to determine both the computer's random choice and the player's choice. The diagram outlines the logic for determining the winner in the Rock-Paper-Scissors game:

![Pseudocode for planning rock paper scissors game with python](https://moringa.instructure.com/courses/1391/files/620310/download)

In this diagram, P represents the player's choice and C represent the computer's.

### Step 1: Plan Your Outcome

Based on the flow diagram, plan out your game structure. Consider:

* How will you represent the choices (Rock, Paper, Scissors)?
* What conditions need to be checked to determine the winner?
* How will you handle ties?

### Step 2: Define the Conditions

Based on your planning:

* Define the possible choices (Rock, Paper, Scissors).
* Determine how you'll represent these choices in your code (e.g., numbers, strings).
* List out the winning conditions (e.g., Rock beats Scissors).

### Task 3: Construct Your Statement(s)

In your Python file:

1. Import the `random` module for the computer's choice.
2. Set up the basic structure of your if-elif-else statement.
3. Include conditions for:
   * Checking for a tie
   * Each possible winning scenario for the player
   * The computer winning (else condition)

### Task 4: Write the Code Blocks for Each Condition

For each condition in your if-elif-else statement:

1. Add the appropriate code block.
2. Ensure proper indentation.
3. Include print statements to display the result of each round.

### Task 5: Test and Refine

Run your program multiple times, testing different scenarios:

* Player wins
* Computer wins
* Tie game
* Invalid input

Make adjustments to your code as needed to handle all possible outcomes correctly.

### Task 6: Document and Maintain

Add comments to your code explaining:

* The purpose of each main section.
* Any complex logic.
* Assumptions made in your implementation.

### Solution

### Select for Solution

```
import random  
  
print("\n\t1: Rock")    #1 = Rock  
print("\t2: Paper")     #2 = Paper  
print("\t3: Scissors")  #3 = Scissors  
  
# Choose!  
computer = random.randint(1,3)  
player = int(input("Please choose 1, 2, or 3: "))  
# Note the int() around the input. If the user enters an  
# incorrect character, this will cause an error  
  
if player == computer:    
    print ("Tie! No winner.")
```

### Summary

By completing this lab, you've practiced implementing game logic using conditional statements and working with user input. Remember to test your code thoroughly and consider how you might expand on this basic game in the future!

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239155

Scraped At: 2026-05-14T15:20:19.537936
