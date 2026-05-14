# For Loops: An Example

# For Loops: An Example

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) For Loops: An Example

Icon Progress Bar (browser only)

2 min read

Now that you have been introduced to for loops, let's walk through an example.

The code example below demonstrates a for loop in Python that iterates through a list of fruits, converting each fruit name to uppercase before printing it.

```
fruits = ["apple", "banana", "cherry"]  
  
for fruit in fruits:  
  print(fruit.upper())
```

### For Loops

Here's a breakdown of how it works:

### List Initialization

* `fruits = ["apple", "banana", "cherry"]`: Creates a list named `fruits` containing three string elements: `"apple"`, `"banana"` and `"cherry"`.

### For Loop Structure

* `for fruits in fruits`: Initiates the for loop.
* `fruit`: This is the loop variable that will take on the value of each element in the fruits list during each iteration of the loop.
* `in fruits`: This specifies the iterable object (the list fruits) that the loop will iterate over.

### Loop Body

* `print(fruit.upper))`: The indented block of code that executes for each element in the list.
* `fruit`: Within the loop body, fruit refers to the current element in the list during each iteration.
* `.upper()`: This is a method applied to the fruit string. The `.upper()` method converts the string to uppercase.
* `print()`: This function prints the result of the `.upper()` method call to the console.

### Conceptualization: For Loop Example

For Loop Part Defined with Code Example

| For Loop Part | Definition | Code |
| --- | --- | --- |
| List Initialization | * You define a loop variable using a descriptive name that reflects the purpose of the element it will hold during each iteration. * This variable is not assigned a value initially, but it will be assigned the value of each element in the sequence as the loop progresses. | ``` fruits = ["apple", "banana", "cherry"] ``` |
| Implicit Condition | * Unlike while loops, for loops don't have an explicit condition that needs to be True for the loop to continue. The loop's internal mechanism is designed to iterate through the entire sequence you provide. * However, the loop will terminate prematurely if you use a break statement within the loop body (discussed in more advanced lessons). | ``` for fruit in fruits: ``` |
| Loop Body Execution | * The indented block of code following the for line defines the actions you want to perform for each element in the sequence. * Inside this block, you can access the current element using the loop variable you defined earlier. * The code within the loop body can involve various operations like printing, manipulating the element, or performing calculations based on its value. | ``` print(fruit.upper()) ``` |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239196

Scraped At: 2026-05-14T15:51:24.728589
