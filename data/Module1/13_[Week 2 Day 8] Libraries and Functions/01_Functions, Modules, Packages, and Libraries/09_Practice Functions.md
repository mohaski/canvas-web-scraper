# Practice: Functions

# Practice: Functions

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Functions

Icon Progress Bar (browser only)

4 min read

You are a junior software developer working for a company that specializes in creating educational software. Your task is to create a Python package called "mathtools" that provides modules for various mathematical operations. The package will be used by other developers in your team to build educational math applications.

By completing this practice exercise, you will gain hands-on experience in creating Python packages, organizing code into modules, and writing functions to perform specific mathematical operations. You will also learn how to use these modules in a main script to solve math-related problems.

### Instructions

Use the following steps to outline how to use functions to solve a business problem.

### Task 1: Define the Problem

Your task is to create a Python package called "mathtools" that provides modules for various mathematical operations. The package will be used by other developers in your team to build educational math applications.

### Task 2: Develop the Code

### Create Directories

Create a new Python file with a .py extension for each module.

1. Create a new directory/folder named "mathtools" for your package.
2. Inside the "mathtools" directory, create an empty file named "\_\_**init\_\_**.py" to mark it as a Python package.

### Create New Files

Define functions, classes, and variables related to a specific functionality within each module. You will need to create a Python package named "mathtools" with the following modules:

* "arithmetic.py": Contains functions for basic arithmetic operations (addition, subtraction, multiplication, division)
* "geometry.py": Contains functions for calculating the area and perimeter of common geometric shapes (circle, rectangle, triangle)
* "utils.py": Contains utility functions for checking if a number is prime and generating Fibonacci sequences

#### arithmetic.py

Create a new file named "arithmetic.py" inside the "mathtools" directory. Implement the following functions in this module:

* "add(a, b)": Returns the sum of two numbers
* "subtract(a, b)": Returns the difference between two numbers
* "multiply(a, b)": Returns the product of two numbers
* "divide(a, b)": Returns the division result of two numbers (handle division by zero)

#### geometry.py

Create a new file named "geometry.py" inside the "mathtools" directory. Implement the following functions in this module:

* "circle\_area(radius)": Returns the area of a circle given its radius
* "circle\_perimeter(radius)": Returns the perimeter (circumference) of a circle given its radius
* "rectangle\_area(length, width)": Returns the area of a rectangle given its length and width
* "rectangle\_perimeter(length, width)": Returns the perimeter of a rectangle given its length and width
* "triangle\_area(base, height)": Returns the area of a triangle given its base and height

#### utils.py

Create a new file named "utils.py" inside the "mathtools" directory. Implement the following functions in this module:

* "is\_prime(num)": Checks if a number is prime and returns True or False
* "fibonacci(n)": Generates a list of the first n Fibonacci numbers

### Test Validity

Run main.py and verify the expected results.

### Task 3: Test and Validate

Run main.py and verify the expected results:

```
Addition: 8  
Subtraction: 3  
Multiplication: 24  
Division: 5.0  
Circle area (radius=5): 78.53981633974483  
Circle perimeter (radius=5): 31.41592653589793  
Rectangle area (length=4, width=6): 24  
Rectangle perimeter (length=4, width=6): 20  
Triangle area (base=5, height=3): 7.5  
Is 17 prime? True  
First 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Task 4: Document and Maintain

* **Version Control**: Use version control to track changes; allowing for easy updates, collaborative editing, and the ability to revert to previous versions if necessary.
* **Regular Updates and Reviews**: Schedule regular reviews and updates for code ensure content remains relevant, accurate, and aligned with the latest Python developments and industry practices.
* **Documentation and Examples Repository**: Maintain a centralized repository containing all lab documents, example code, and solutions.

### Tools

* [VS Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code"), a Python IDE

### Solution

### Select for Solution

```
from mathtools.arithmetic import add, subtract, multiply, divide  
from mathtools.geometry import circle_area, circle_perimeter, rectangle_area, rectangle_perimeter, triangle_area  
from mathtools.utils import is_prime, fibonacci  
  
# Arithmetic operations  
print("Addition:", add(5, 3))  
print("Subtraction:", subtract(10, 7))  
print("Multiplication:", multiply(4, 6))  
print("Division:", divide(10, 2))  
  
# Geometry calculations  
print("Circle area (radius=5):", circle_area(5))  
print("Circle perimeter (radius=5):", circle_perimeter(5))  
print("Rectangle area (length=4, width=6):", rectangle_area(4, 6))  
print("Rectangle perimeter (length=4, width=6):", rectangle_perimeter(4, 6))  
print("Triangle area (base=5, height=3):", triangle_area(5, 3))  
  
# Utility functions  
print("Is 17 prime?", is_prime(17))  
print("First 10 Fibonacci numbers:", fibonacci(10))
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239327

Scraped At: 2026-05-14T16:01:09.687705
