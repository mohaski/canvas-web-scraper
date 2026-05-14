# Process: Python Operators

# Process: Python Operators

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Process: Python Operators

Icon Progress Bar (browser only)

5 min read

The following process for using Python operators is grounded by the [Software Development Life Cycle (SDLC) model](#dpPopup0Content). This process will help you outline how to efficiently and effectively execute operators and control-flow in a Python script. 

The SDLC is a structured framework that guides the development of software applications through distinct phases: planning, design, development, testing, deployment, and maintenance.

By following this process, you can effectively use if-elif-else statements and operators to make decisions and control the flow of your program based on specific conditions. Remember to choose the appropriate operators, structure the conditions logically, and test thoroughly to ensure the desired behavior is achieved.

### Step 1: Identify the Decision-Making Scenario

* Determine the specific decision or conditions you need to evaluate in your program.
* Understand the different possible outcomes based on the conditions.

### Step 2: Define the Conditions

* Identify the variables or expressions that will be used in the conditions.
* Choose the appropriate operators (comparison, logical, etc.) to express the conditions.
* Write the conditions using the selected operators and variables.

### Step 3: Construct the if-elif-else Statement

* Start with the if keyword followed by the first condition.
* If there are additional conditions to check, use elif (short for "else if") followed by the next condition.
* Optionally, include an else block to handle the case when none of the previous conditions are true.

### Step 4: Write the Code Blocks for Each Condition

* Indent the code block under each condition (if, elif, else).
* Write the code that should be executed when a particular condition is true.
* Ensure proper indentation to maintain the structure of the if-elif-else statement.

### Step 5: Test and Refine

* Run your program with different inputs and scenarios to test the behavior of the if-elif-else statement.
* Verify that the appropriate code blocks are executed based on the conditions.
* Make any necessary adjustments to the conditions, operators, or code blocks to achieve the desired outcome.

### Step 6: Document and Maintain

* Add comments to explain the purpose and functionality of the if-elif-else statement.
* Document any assumptions, constraints, or edge cases related to the conditions.
* Keep the code maintainable and readable for future reference or collaboration.

### Video: Loan Eligibility Scenario

In the following video, you will be introduced to a loan eligibility scenario and break down the process of working through an example with operators.

[VIDEO LINK](https://player.vimeo.com/video/1003497614?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Conceptualization: The Operator Process

The following compares the steps with specific actions and an example that aligns to scenario about the loan eligibility algorithm.

Step

Action

Example

**Step 1**: Identify the Decision-Making Scenario

* Determine the specific decision or conditions you need to evaluate in your program.
* Understand the different possible outcomes based on the conditions.

Determine loan eligibility based on credit score and income.

Possible outcomes: Eligible for loan, eligible for loan with higher income, not eligible for loan.

**Step 2**: Define the Conditions

* Identify the variables or expressions that will be used in the conditions.
* Choose the appropriate operators (comparison, logical, etc.) to express the conditions.
* Write the conditions using the selected operators and variables.

Conditions:

```
Credit score > 700 and annual income >= $50,000. 2. 600 <= credit score <= 700 and annual income > $75,000.
```

**Step 3**: Construct the if-elif-else Statement

* Start with the if keyword followed by the first condition.
* If there are additional conditions to check, use elif (short for "else if") followed by the next condition.
* Optionally, include an else block to handle the case when none of the previous conditions are true.

```
if credit_score > 700 and annual_income >= 50000:<br> return "Eligible for loan"<br>elif 600 <= credit_score <= 700 and annual_income > 75000:<br> return "Eligible for loan with higher income"<br>else:<br> return "Not eligible for loan"
```

**Step 4:**  Write the Code Blocks for Each Condition

* Indent the code block under each condition (if, elif, else).
* Write the code that should be executed when a particular condition is true.
* Ensure proper indentation to maintain the structure of the if-elif-else statement.

See the code block under Step 3 for each condition.

**Step 5**: Test and Refine

* Run your program with different inputs and scenarios to test the behavior of the if-elif-else statement.
* Verify that the appropriate code blocks are executed based on the conditions.
* Make any necessary adjustments to the conditions, operators, or code blocks to achieve the desired outcome.

Test the function with various credit scores and income levels to ensure correct eligibility determination.

Adjust conditions or operators if necessary based on test results.

**Step 6:** Document and Maintain

* Add comments to explain the purpose and functionality of the if-elif-else statement.
* Document any assumptions, constraints, or edge cases related to the conditions.
* Keep the code maintainable and readable for future reference or collaboration.

Add comments to the function explaining each condition and the corresponding eligibility outcome.

Document any assumptions about credit score ranges or income thresholds.

Keep the code well-structured and commented for easy understanding by other developers.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239151

Scraped At: 2026-05-14T15:19:46.018631
