# Practice: Python Commands

# Practice: Python Commands

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Python Commands

Icon Progress Bar (browser only)

4 min read

Let’s put your new knowledge and skills in Python commands into practice with a fun and practical exercise. This will help you solidify your understanding and become more comfortable with basic Python programming tasks.

Imagine you are a junior employee working for a car rental company. Your task is to create a Python script that calculates the total cost of a car rental based on the number of days the car is rented and the daily rental price. The script should prompt the user to enter the necessary information and display the calculated total cost using an f-string. Additionally, the company offers a special weekend promotion where the rental price is discounted by 10% for rentals that include a Saturday or Sunday.

**Problem-Solving Process:**

1. 1. Understand the problem
   2. Plan the solution
   3. Implement the solution
   4. Test and debug

By the end of this practice, you should be able to:

* Use the input() function to accept user input.
* Use an if statement to conditionally apply a discount based on whether the rental includes a weekend day.
* Perform basic arithmetic calculations.
* Use f-strings to format and display the output.

### Tools

* Python IDE
* [Visual Studio Code


  Links to an external site.](https://code.visualstudio.com/ "Link")

### Instructions

Use the steps below to guide your thinking through the process:

* [Step 1: Plan Your Outcome](#dpPanel0Content)
* [Step 2: Define the Conditions](#dpPanel1Content)
* [Step 3: Construct Your Statement(s)](#dpPanel2Content)
* [Step 4: Write the Code Blocks for Each Condition](#dpPanel3Content)
* [Step 5: Test and Refine](#dpPanel4Content)
* [Step 6: Document and Maintain](#dpPanel5Content)

### Step 1: Plan Your Outcome

* Consider the specific conditions to evaluate, the required inputs, and the resulting outcomes based on those conditions.
* Use the following program flow diagram to plan:

![Pseudocode for planning rock paper scissors game with python](https://moringa.instructure.com/courses/1391/files/620310/download)

### Step 2: Define the Conditions

Define the actual conditions and variables, including the user input.

### Step 3: Construct Your Statement(s)

Construct your `if-elif-else` statement in a Python file based on the possible conditions and outcomes.

### Step 4: Write the Code Blocks for Each Condition

Indent the code block under each condition (if, elif, else). Write the code that should be executed when a particular condition is true. Ensure proper indentation to maintain the structure of the `if-elif-else` statement.

### Step 5: Test and Refine

Run your program with different inputs and scenarios to test the behavior of the `if-elif-else` statement. Verify that the appropriate code blocks are executed based on the conditions. Make any necessary adjustments to achieve the desired outcome.

### Step 6: Document and Maintain

Add comments to explain the purpose and functionality of the `if-elif-else` statement. Document any assumptions, constraints, or edge cases related to the conditions. Keep the code maintainable and readable for future reference or collaboration.

### Solution

### [Select for Solution](#dpPanel6)

**Problem-Solving Process:**

1. **Understand the problem**:
   * Identify the inputs required: number of days, daily rental price, and whether the rental includes a weekend day.
   * Determine the output: total cost of the car rental, considering the weekend promotion if applicable.
2. **Plan the solution**:
   * Prompt the user to enter the number of days and daily rental price.
   * Prompt the user to indicate if the rental includes a weekend day (Saturday or Sunday).
   * Calculate the base cost by multiplying the number of days by the daily rental price.
   * Use an if statement to check if the rental includes a weekend day.
   * If the rental includes a weekend day, apply a 10% discount to the base cost.
   * Display the total cost using f-string formatting.
3. **Implement the solution**:
   * Write the Python script according to the planned solution.
4. **Test and debug**:
   * Run the script with different inputs to ensure it produces the correct output.
   * Test scenarios with and without weekend days to verify the discount is applied correctly.
   * Debug any issues that may arise during testing.

```
#!/usr/bin/python3  
  
# Author:   
  
# Date:  
  
'''  
This script takes in three inputs  
-Number of rental days : integer  
-Cost per day : integer  
-Includes weekend or not : (yes/no) string  
'''  
  
days = int(input("Enter the number of days the car will be rented for: "))  
cost = int(input("What is the current cost per day in dollars?: "))  
weekend = input("Does the rental period include a weekend day (yes/no): "))  
  
# Calculate base cost first  
base_cost = days * cost  
  
# Check if rental includes a weekend (yes) apply 10% discount  
if weekend == "yes":  
	total_cost = base_cost * .9  
	print(f"The total cost of the car rental for {days} days at ${cost} per day and with a 10% weekend discount comes to {total_cost}")  
else:  
	print(f"The total cost of the car rental for {days} days at ${cost} per day comes out to {base_cost}")
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239135

Scraped At: 2026-05-14T00:26:34.723474
