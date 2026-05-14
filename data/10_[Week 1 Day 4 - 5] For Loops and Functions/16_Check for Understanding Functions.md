# Check for Understanding: Functions

# Check for Understanding: Functions

## ![](https://moringa.instructure.com/courses/1391/files/620140/preview?) Check for Understanding: Functions

* [Page: Introduction to For Loops and Functions (1 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239191 "Page: Introduction to For Loops and Functions (1 of 18)")
* [Page: What are For Loops? (2 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239194 "Page: What are For Loops? (2 of 18)")
* [Page: For Loops: An Example (3 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239196 "Page: For Loops: An Example (3 of 18)")
* [Page: Process: Using For Loops (4 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239197 "Page: Process: Using For Loops  (4 of 18)")
* [Page: Summary: For Loops (5 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239199 "Page: Summary: For Loops (5 of 18)")
* [Page: Considering While Loops and For Loops (6 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239201 "Page: Considering While Loops and For Loops  (6 of 18)")
* [Page: Check for Understanding: For Loops (7 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239203 "Page: Check for Understanding: For Loops (7 of 18)")
* [Page: Technical Lesson: For Loops (8 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239205 "Page: Technical Lesson: For Loops  (8 of 18)")
* [Page: Practice: For Loops (9 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239206 "Page: Practice: For Loops  (9 of 18)")
* [Page: Introduction to Functions (10 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239210 "Page: Introduction to Functions  (10 of 18)")
* [Page: What are Functions? (11 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239211 "Page: What are Functions? (11 of 18)")
* [Page: Process: Using Functions (12 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239213 "Page: Process: Using Functions (12 of 18)")
* [Page: Summary: Functions (13 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239215 "Page: Summary: Functions (13 of 18)")
* [Page: Current: Check for Understanding: Functions (14 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239217 "Page: Current: Check for Understanding: Functions (14 of 18)")
* [Discussion: For Loops (15 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239220 "Discussion: For Loops (15 of 18)")
* [Lab: Coding with Functions (16 of 18), Assignment](https://moringa.instructure.com/courses/1391/modules/items/239222 "Lab: Coding with Functions (16 of 18), Assignment")
* [Lab: Coding with For Loops (17 of 18), Assignment](https://moringa.instructure.com/courses/1391/modules/items/239224 "Lab: Coding with For Loops (17 of 18), Assignment")
* [Quiz: For Loops and Functions (18 of 18)](https://moringa.instructure.com/courses/1391/modules/items/239226 "Quiz: For Loops and Functions (18 of 18)")

Now is your opportunity to see how much you can recall from the topic! Take a moment to answer the questions below. These are not graded, but they will allow you to check how much you are putting together the content in this lesson and review before moving to a new topic. 

### Quick Check: Total Cost

You are a junior developer working on a project that involves calculating the total cost of items in a shopping cart, including tax. To make the code more organized and reusable, you decide to write a function that performs this calculation. The function should take the price of an item, the quantity of the item, and the tax rate as input, and return the total cost for that item. Now, you need to call this function in your main code to calculate the total cost for different items.

Given the following code snippet, which of the following options correctly calls the `calculate_total_cost` function to calculate the total cost of an item priced at $20, with a quantity of 3, and a tax rate of 5%?

Here's the function you have written:

```
def calculate_total_cost(price, quantity, tax_rate):  
    subtotal = price * quantity  
    tax = subtotal * tax_rate  
    total_cost = subtotal + tax  
    return total_cost
```

**This question has multiple correct answers. Select all that are correct:**

---

``` total = calculate_total_cost(20, 3, 0.05) print("The total cost is:", total) ```
:   **Correct:** This is the correct way to call the function, providing all required parameters (`price`, `quantity`, and `tax_rate`) in the correct order.

``` total = calculate_total_cost(20, 3) print("The total cost is:", total) ```
:   This option is incorrect because it omits the `tax_rate` parameter, which is required by the function.

``` total = calculate_total_cost(price=20, quantity=3, tax_rate=0.05) print("The total cost is:", total) ```
:   **Correct:** This option is also correct as it uses keyword arguments to specify the values for `price`, `quantity`, and `tax_rate`.

``` total = calculate_total_cost(price=20, quantity=3) print("The total cost is:", total) ```
:   This option is incorrect because it omits the `tax_rate` parameter.

Check Answer

### Quick Check: Greeting Users

You are working on a project that involves greeting users by their names. To make your code more organized and reusable, you decide to create a function that generates a personalized greeting. You then assign this function to a variable and use that variable to call the function.

Here’s the function you defined:

```
def greet(name):  
    return f"Hello, {name}! Welcome to the program."
```

 You assign this function to a variable and call it as follows:

```
greeting_function = greet
```

Which of the following options correctly calls the `greeting_function` variable to greet a user named "Alice"?

**This question has multiple correct answers. Select all that are correct:**

---

``` greeting = greet("Alice") print(greeting) ```
:   **Incorrect,** not relevant to the question, as it directly calls the original `greet` function rather than using the `greeting_function` variable.

``` greeting = greeting_function("Alice") print(greeting) ```
:   **Correct:** it uses the `greeting_function` variable, which holds the memory location of the `greet` function, and calls it with the argument "Alice".

``` greeting = greeting_function() print(greeting) ```
:   **Incorrect, t**his option is incorrect because it attempts to call `greeting_function()` without passing the required `name` parameter.

``` greeting = greet print(greeting("Alice")) ```
:   **Correct:** This is correct but achieves the same result as the second option in a slightly different way. It assigns `greet` to `greeting` and then calls `greeting("Alice")`, which still directly invokes the original function rather than the variable.

Check Answer

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239217

Scraped At: 2026-05-14T00:34:28.501228
