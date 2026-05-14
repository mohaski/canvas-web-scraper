# Practice: Debugging With an Integrated Development Environment

# Practice: Debugging With an Integrated Development Environment

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Debugging with an Integrated Development Environment

Icon Progress Bar (browser only)

2 min read

Imagine you work for a retail company that sells products online. The company has a Python script that calculates the total cost of an order, including the subtotal, sales tax, and shipping charges. However, the script seems to have a bug, and you need to use VS Code to debug it.

For this lab, you will use what you have already learned in this lesson to create your Python file and copy in the code provided then. You will need to consider how to debug and step into, through, and over a script using the VS Code Python debugger in order to solve the problem.

### Tools and Resources

* Python and VS Code installed - with the Python extension for the debugger

### Instructions

### [Step 1: Getting Started](#dpPanel0)

1. Open VS Code and create a new Python file.
2. Copy the provided Python script into the file.

```
def calculate_total_cost(subtotal, state):  
    tax_rates = {  
        'CA': 0.08,  
        'NY': 0.07,  
        'TX': 0.0625  
    }  
  
    shipping_charges = 10.00  
  
    if state in tax_rates:  
        sales_tax = subtotal * tax_rates[state]  
    else:  
        sales_tax = 0.00  
  
    total_cost = subtotal + sales_tax + shipping_charges  
    return total_cost  
  
# Example usage  
subtotal = 100.00  
state = 'CA'  
  
total_cost = calculate_total_cost(subtotal, state)  
print(f"Subtotal: ${subtotal:.2f}")  
print(f"Shipping Charges: ${shipping_charges:.2f}")  
print(f"Total Cost: ${total_cost:.2f}")
```

### [Step 2: Step Through the Code](#dpPanel1)

1. Set a breakpoint on the line that calculates the total\_cost.
2. Run the script in debug mode.
3. Step through the code and observe the values of subtotal, `sales_tax`, and `shipping_charges`.

### [Task 3: Fix the Bug](#dpPanel2)

1. Identify the bug in the script.
2. Fix the bug and verify that the script now calculates the correct total cost.

### Solution

### [Select for Solution](#dpPanel3)

The bug in the script is that the variable shipping\_charges `shipping_charges` is not defined outside the scope of the `calculate_total_cost function`.

To fix the bug, assign `shipping_charges` as a variable outside of the  `calculate_total_cost function`.

For an even more Pythonic fix, we could also provide  `shipping_charges` as a parameter in the `calculate_total_cost function`.

```
def calculate_total_cost(subtotal, state):  
    tax_rates = {  
        'CA': 0.08,  
        'NY': 0.07,  
        'TX': 0.0625  
    }  
  
    if state in tax_rates:  
        sales_tax = subtotal * tax_rates[state]  
    else:  
        sales_tax = 0.00  
  
    total_cost = subtotal + sales_tax + shipping_charges  
    return total_cost  
  
# Example usage  
subtotal = 100.00  
state = 'CA'  
  
# THE BUG FIX  
shipping_charges = 10.00  
  
total_cost = calculate_total_cost(subtotal, state)  
print(f"Subtotal: ${subtotal:.2f}")  
print(f"Shipping Charges: ${shipping_charges:.2f}")  
print(f"Total Cost: ${total_cost:.2f}")
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239129

Scraped At: 2026-05-14T00:25:49.307121
