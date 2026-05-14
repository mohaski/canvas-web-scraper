# Process: While Loops

# Process: While Loops

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Process: While Loops

Icon Progress Bar (browser only)

5 min read

Imagine you are creating a simple coin toss simulator in Python. You want to simulate tossing a coin repeatedly until a specific outcome (heads or tails) appears a certain number of times (e.g., three times).

* The `while` loop keeps the simulation running until the desired outcome happens the specified number of times.
* The loop controls the repetitive task of simulating coin tosses.
* Counters track the total tosses and occurrences of the desired outcome.

Here are the steps to use a while loop to achieve this:

### Step 1: Define the Problem

For this problem, you will simulate tossing a coin repeatedly until a specific outcome (heads or tails) appears a certain number of times (e.g., three times).

### Step 2: Design - Determine the Design

To determine your design, you will need to do the following: 

1. Define the variables
2. Implement a loop
3. Integrate input
4. Implement the outcome
5. Display results

**Review the Pseudocode for the Coin Toss Simulation:**

```
# Define desired outcome and number of occurrences  
desired_outcome = "heads"  # Or "tails"  
num_occurrences = 3  
  
# Initialize counters  
total_tosses = 0  
occurrences = 0  
  
# Start the loop  
while occurrences < num_occurrences:  
  # Simulate coin toss (random choice)  
  toss_result = random.choice(["heads", "tails"])  
  total_tosses += 1  
  
  # Check if the toss matches the desired outcome  
  if toss_result == desired_outcome:  
    occurrences += 1  # Increment counter for desired outcome  
  
# Loop finishes when desired outcome happens enough times  
  
# Display results  
print("Total tosses:", total_tosses)  
print(desired_outcome, "occurred", occurrences, "times")
```

### Step 2: Development- Write the Code

### Define the Variables

1. Variable: Outcome and number of occurrences
   * `desired_outcome`: Set the side you want to see (e.g., "heads" or "tails").
   * `num_occurrences`: Define how many times you want to see that outcome.
2. Variable: Initialize counters
   * `total_tosses`: Tracks the total number of coin tosses.
   * `occurrences`: Counts the number of times the desired outcome appears.

**Review the Pseudocode for the Coin Toss Simulation:**

```
# Define desired outcome and number of occurrences  
desired_outcome = "heads"  # Or "tails"  
num_occurrences = 3  
  
# Initialize counters  
total_tosses = 0  
occurrences = 0
```

### Implement a Loop

The while loop will runs as long as occurrences is less than `num_occurrences`. Inside the loop, a coin toss is simulated using random choice. The total\_tosses `total_tosses` increment by 1. If the result of the toss (`toss_result`) matches `desired_outcome`, occurrences increment by 1.

```
# Define desired outcome and number of occurrences  
desired_outcome = "heads"  # Or "tails"  
num_occurrences = 3  
  
# Initialize counters  
total_tosses = 0  
occurrences = 0
```

### Integrate Input

Simulate coin toss (random.choice). Use random.choice(["heads", "tails"]) to randomly pick "heads" or "tails" for each toss. Increment total tosses, total\_tosses += 1 keeps track of the overall number of tosses.

```
# Define desired outcome and number of occurrences  
desired_outcome = "heads"  # Or "tails"  
num_occurrences = 3  
  
# Initialize counters  
total_tosses = 0  
occurrences = 0  
  
# Start the loop  
while occurrences < num_occurrences:  
  # Simulate coin toss (random choice)  
  toss_result = random.choice(["heads", "tails"])  
  total_tosses += 1  
  
  # Check if the toss matches the desired outcome  
  if toss_result == desired_outcome:  
    occurrences += 1  # Increment counter for desired outcome
```

### Implement the Outcome

Check for desired outcome `(if).` If `toss_result` matches `desired_outcome`, increment the occurrences counter.

```
# Define desired outcome and number of occurrences  
desired_outcome = "heads"  # Or "tails"  
num_occurrences = 3  
  
# Initialize counters  
total_tosses = 0  
occurrences = 0  
  
# Start the loop  
while occurrences < num_occurrences:  
  # Simulate coin toss (random choice)  
  toss_result = random.choice(["heads", "tails"])  
  total_tosses += 1  
  
  # Check if the toss matches the desired outcome  
  if toss_result == desired_outcome:  
    occurrences += 1  # Increment counter for desired outcome  
  
# Loop finishes when desired outcome happens enough times  
  
# Display results  
print("Total tosses:", total_tosses)  
print(desired_outcome, "occurred", occurrences, "times")
```

### Display Results

Display results (outside the loop):

* Print the total number of tosses and how many times the desired outcome occurred.

### Step 3: Test and Refine

* Run your program with different number of occurrences and parameters for the outcome to test the behavior of the while loop.
* Verify that the appropriate code blocks are executed based on the conditions.
* Make any necessary adjustments to the while loop or code blocks to achieve the desired outcome.

### Step 5: Document and Maintain

* Add comments to explain the purpose and functionality of the if-elif-else statement.
* Document any assumptions, constraints, or edge cases related to the conditions.
* Keep the code maintainable and readable for future reference or collaboration.

### Pseudocode

The following is an example of how to plan for while loops with a simulator.

```
# Define desired outcome and number of occurrences  
desired_outcome = "heads"  # Or "tails"  
num_occurrences = 3  
  
# Initialize counters  
total_tosses = 0  
occurrences = 0  
  
# Start the loop  
while occurrences < num_occurrences:  
  # Simulate coin toss (random choice)  
  toss_result = random.choice(["heads", "tails"])  
  total_tosses += 1  
  
  # Check if the toss matches the desired outcome  
  if toss_result == desired_outcome:  
    occurrences += 1  # Increment counter for desired outcome  
  
# Loop finishes when desired outcome happens enough times  
  
# Display results  
print("Total tosses:", total_tosses)  
print(desired_outcome, "occurred", occurrences, "times")
```

### Conceptualization: While Loops Process

Task

Pseudocode

Definition

1. Define Outcomes and Number of Occurrences

```
desired_outcome = "heads"<br>num_occurrences = 3
```

Set the side of the coin you want to see (e.g., "heads" or "tails") and define how many times you want that outcome to appear.

2. Initialize Counters

```
total_tosses = 0<br>occurrences = 0
```

Initialize two counters: `total_tosses` to track the total number of coin tosses, and occurrences to count how many times the desired outcome appears.

3. Start the Loop

`while occurrences < num_occurrences:`

Begin a while loop that continues as long as the number of occurrences of the desired outcome is less than the specified number.

4. Simulate Coin Toss

```
import random<br>toss_result = random.choice(["heads", "tails"])
```

Use the random module to simulate a coin toss by randomly choosing between "heads" and "tails".

5. Increment Total Tosses

```
total_tosses += 1
```

Increment the `total_tosses` counter by 1 each time a coin is tossed.

6. Check for Desired Outcome

```
if toss_result == desired_outcome:<br> occurrences += 1
```

Check if the result of the coin toss matches the desired outcome. If it does, increment the `occurrences` counter by 1.

7. Loop Continues

(Implicit in step 3)

The loop repeats Steps 4-6 as long as `occurrences` is less than `num_occurrences`.

8. Display Results

```
print("Total tosses:", total_tosses)<br>print(desired_outcome, "occurred", occurrences, "times")
```

After the loop finishes, print the total number of tosses and the number of times the desired outcome occurred.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239173

Scraped At: 2026-05-14T15:21:38.944269
