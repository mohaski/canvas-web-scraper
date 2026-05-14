# Technical Lesson: Operators

# Technical Lesson: Operators

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Technical Lesson: Operators

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In this lesson, we will explore the power of conditional statements and operators in Python. Conditional statements, such as if-elif-else, allow you to make decisions and control the flow of your program based on specific conditions. Operators, on the other hand, enable you to perform various operations on data, such as arithmetic calculations and comparisons. Adding robust comparison values brings out the power of branching usingif-elif-else statements. Combining multiple comparisons forms a complex logic and provides a means for writing advanced applications.

This lesson will cover the creation of an example guessing game and highlight some key considerations for using certain operators.

The Scenario

Imagine you are a junior developer and are tasked with developing an K-12 educational tech tool for a Learning Management System (LMS). The goal is to create an interactive guessing game (guessinggame.py) that provides various levels of feedback based on the user's input.

The game will prompt the user to guess a number between 1 and 100. Depending on the user's guess, the program will provide feedback such as:

* + "Too low!"
  + "Too high!"
  + "Correct! You've guessed the number!"

### Resources and Tools

* [Module Process: writing if-elif-else statements](https://moringa.instructure.com/courses/1391/pages/process-python-operators "Process of Operators")
* [Visual Studio Code](https://code.visualstudio.com/ "Link")

### Instructions

In this lesson you will be implementing control flow operators with if-elif-else statements. You will be combining multiple comparisons to form a complex logic and this will aid you in writing advanced applications. The following video and instructions will walk you through using operators for a technical lesson.

[VIDEO LINK](https://player.vimeo.com/video/986746146?h=55dafe3f88)

As you work through these steps in your own coding environment, the instructions and code comments will show you the parts of the code that have been added to the script.

### Step 1: Plan Your Outcomes

Based on the conditions, consider the specific conditions to be evaluated, what inputs are needed, and the resulting outcomes.

* Need the user to input a guess and convert to an integer
* Need to compare that guess to a random value (this will be handles using a special python import that is pre-existing)
* Need three outcomes
  + Guess was correct
  + Guess was too low
  + Guess was too high

### Step 2: Define Conditions and Variables

Define the actual conditions and variables, including the input.

* Define a **random value**: will be handled with the random package
  + value = ….
* Define a **user input guess**:solicit the user for a guess using input()
  + guess = ….
* Determine the **appropriate operator** to express the conditions:
  + When comparing two numbers, use arithmetic operators
  + Guess was correct: guess == value
  + Guess was too low: guess < value
  + Guess was too high: guess > value

```
# Package to generate a random number  
import random  
  
# Define the random value, integer between 0 and 10  
value = random.randint(0,10)  
  
# Define the user input guess and make it an integer  
guess = int(input(guess)) # input by default will return a string type
```

### Step 3: Construct Statements

Construct your **if-elif-else statement** in a python file based on the three possible conditions/outcomes.

```
# Package to generate a random number  
import random  
  
# Define the random value, integer between 0 and 10  
value = random.randint(0,10)  
  
# Define the user inputted guess and make it an integer  
guess = int(input(guess)) # input by default will return a string type  
  
# Construct the if-elif-else block  
if value == guess:  
	# Code here  
elif value < guess:  
	# Code here  
else: # Think about why we can get away with just else here  
	# Code here
```

### Step 4: Write Code Blocks for Condition

* Write the code blocks for each condition.
* Use the blocks for each matching condition. In practice this step is often combined with Step 3, as you write out the if-elif-else statements.

For our example we will keep it very simple and just print out the result. We will use f-string formatting (f”some string here {variable}”) to display the actual value as well.

```
# Package to generate a random number  
import random  
  
# Define the random value, integer between 0 and 10  
value = random.randint(0,10)  
  
# Define the user inputted guess and make it an integer  
guess = int(input("Please guess a number between 0 and 10: ")) # input by default will return a string type  
  
# Construct the if-elif-else block  
if guess == value:  
	print("You guessed correctly!")  
elif guess < value:  
	print(f"Your guess was too low, the actual number was {value}")  
else: # Use an else statement here  
	print(f"Your guess was too high, the actual number was {value}")
```

### Step 5: Test and Refine

* Test and refine if needed.
* Run the script from Step 4, testing out various inputs/guesses.

### Step 6: Document and Maintain

We were documenting by adding in code comments about what each code line will be doing.

The following highlighted code are code comments.

* Code comments are programmer-readable explanations or annotations in the source code of a computer program.
* Code comments helps developers understand what another developer's code was intended to do.

`# Package to generate a random number  
import random  
  
# Define the random value, integer between 0 and 10  
value = random.randint(0,10)  
  
# Define the user inputted guess and make it an integer  
guess = int(input("Please guess a number between 0 and 10: ")) # input by default will return a string type  
  
# Construct the if-elif-else block  
if guess == value:  
print("You guessed correctly!")  
elif guess < value:  
print(f"Your guess was too low, the actual number was {value}")  
else: # Use an else statement here  
print(f"Your guess was too high, the actual number was {value}")`

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239154

Scraped At: 2026-05-14T15:20:13.245781
