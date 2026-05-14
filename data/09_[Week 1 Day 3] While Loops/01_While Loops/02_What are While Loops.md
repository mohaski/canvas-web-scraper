# What are While Loops?

# What are While Loops?

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) What are While Loops?

Icon Progress Bar (browser only)

4 min read

A while loop is a programming construct that repeatedly executes a block of code as long as a specified condition is true. It consists of three key parts:

1. **Condition:** This is a Boolean expression (evaluates to True or False) that determines whether the loop continues to execute.
2. **Loop Body:** This is the block of code that gets executed repeatedly as long as the condition is True. It can contain any valid Python statements.
3. **Loop Control:** While loops often involve modifying a variable within the loop body to eventually make the condition become False, causing the loop to terminate.

### How Do While Loops Work?

Imagine you want to bake a batch of 12 cookies. Take a minute to review this process, broken down into steps:

### [Step 1: Initialization (Assigning Values to Variables)](#dpPanel0)

* Before the loop starts, any necessary variables are initialized (assigned values).
* You know you need to bake 12 cookies, so you can initialize a variable  `num_cookies` with a value of 12.

### [Step 2: Condition Check (Checking If Baking Is Complete)](#dpPanel1)

* The loop's condition is evaluated. **If the condition is True**, the loop body executes.
* You'll use a loop to keep baking cookies until you have enough. The condition to check is whether you've reached the required number of cookies.

### [Step 3: Loop Body Execution (Baking a Cookie)](#dpPanel2)

* The statements within the loop body are executed sequentially.
* In each loop iteration, you'll simulate baking one cookie. You can print a message like "Baked one cookie!" to represent this.

### [Step 4: Condition Check (Again)](#dpPanel3)

* **If the condition is still True,** the loop body executes again (Steps 3 and 4 repeat). This creates the loop's repetitive behavior.
* After baking a cookie, you'll check again if you have enough (refer to Step 2).

### [Step 5: Iteration (Continuing to Bake)](#dpPanel4)

* If you don't have enough cookies yet, the loop will continue back to Step 3 to bake another one.

### [Step 6: Loop Termination (When Enough Cookies Are Baked)](#dpPanel5)

* **When the condition eventually becomes False,** the loop terminates, and the program continues executing the code after the loop.
* Once you've baked 12 cookies (the condition in Step 2 becomes False), the loop will terminate, and your program will move on to the next step, which might be taking the cookies out of the oven!

### [Python Solution](#dpPanel6)

```
# Step 1: Initialization  
num_cookies = 12  
baked_cookies = 0  # To keep track of how many cookies you've baked  
  
# Step 2: Condition Check (while loop)  
while baked_cookies < num_cookies:  
  # Step 3: Loop Body Execution  
  print("Baked one cookie!")  
  baked_cookies += 1  # Increment the number of baked cookies  
  
# Step 6: Loop Termination (after baking enough cookies)  
print("All cookies baked! Taking them out of the oven.")
```

### Conceptualization: While Loops

Imagine a revolving door with a sensor inside. The sensor detects someone (condition is True), so the door continues to revolve. Once the sensor no longer detects anyone walking through the door (condition becomes False), the revolving door stops.

Features of while loops with code and examples

| Feature | Coding Command | Analogy | Example |
| --- | --- | --- | --- |
| **Condition:**  Boolean expression (evaluates to True or False) that determines continual execution | `while` | Sensor detecting someone | A pet retailer might use the Boolean construction "(cat owners OR dog owners OR bird owners) AND Canada" to find customers who own cats, dogs, or birds and live in Canada. |
| **Loop Body:**  With the while loop we can execute a set of statements as long as a condition is true.  Execute a set of statements, once for each item in a list. | `for` | Walking through the door | A traffic light uses a loop to control the sequence of light colors. Change the light color to the next one in the sequence (red -> yellow -> green). Reset the timer for the new light duration. |
| **Loop Termination:**  Refers to the point where the loop stops executing and the program moves on to the next line of code after the loop. | Here, the loop terminates when count reaches 0 and becomes False in the condition count > 0.   ``` count = 5 while count > 0:   print(count)   count -= 1  # Decrementing the counter  print("Loop finished!") ``` | Sensor not detecting anyone | Imagine you're using a vending machine to buy a soda. The loop that controls the purchase process terminates based on user input and product availability. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239170

Scraped At: 2026-05-14T15:21:25.886062
