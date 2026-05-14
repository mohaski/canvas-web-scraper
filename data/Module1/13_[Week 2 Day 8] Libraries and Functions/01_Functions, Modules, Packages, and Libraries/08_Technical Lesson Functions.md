# Technical Lesson: Functions

# Technical Lesson: Functions

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Technical Lesson: Functions

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time: 1 hour**

In this technical lesson, we will explore the process of creating and using functions, modules, and packages in Python. Understanding these concepts is crucial for writing clean, modular, and reusable code. We will walk through the steps of defining functions, organizing code into modules, and structuring modules into packages. By following this established process, you will be able to create well-organized and maintainable Python projects.

The video below will guide you through each step of the functions, modules, and packages process. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding.

[VIDEO LINK](https://player.vimeo.com/video/1003497535?h=25607cd33e)

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Instructions

### Task 1: Defining Functions

* Define a function by using the def keyword followed by the function name and parentheses `()`.
* If the function accepts parameters, specify them within the parentheses.
* Add a colon : after the parentheses to indicate the start of the function block.
* Indent the code block inside the function (usually 4 spaces or a tab).
* Write the code that the function should execute.
* If the function needs to return a value, use the return keyword followed by the value to be returned.

**Example:** Let’s define a very simple function that can add two variables together.

```
def add(a, b):  
    return a + b
```

### Task 2: Calling Functions

* To use a function, you need to call it by its name followed by parentheses `()`.
* If the function requires arguments, provide them within the parentheses.
* The function will execute the code inside its block when called.

**Example:** We can use the defined add function to add numerical or string values in Python.

```
add(2, 5) # Output: 7  
  
add("string1", "string2") # Output: "string1string2"  
  
add(2, "string1") # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Task 3: Creating Modules

* Create a new Python file with a .py extension to define a module.
* Write functions, classes, or variables related to a specific functionality in the module file.
* Save the module file with a descriptive name that reflects its purpose.

**Example:** Let's create a basic calculator module that can add or subtract two values called `math_functions.py`

```
# math_functions.py  
  
def add(a, b):  
    return a + b  
  
def subtract(a, b):  
    return a - b
```

### Task 4:  Importing Modules

* To use functions, classes, or variables from a module, you need to import the module into your Python script.
* Use the import keyword followed by the module name (without the .py extension).
* You can then access the module's contents using the dot notation: `module_name.function_name()`.

**Example:** In a new Python file located next to the `math_functions.py` file we can import and call to those functions.

```
import math_functions  
  
result = math_functions.add(5, 3)  
print(result)  # Output: 8
```

### Task 5: Creating Packages

* Create a new directory with a descriptive name for your package.
* Inside the package directory, create an  `__init__.pyprint` file (which can be empty) to indicate that the directory is a package.
* Create module files within the package directory to organize related functionality.

**Example:** Let’s create a `directory/folder` called basic\_functions `basic_functions` and move the `math_functions.py` file into it. We could also add other modules if we had them.

```
basic_functions/  
    __init__.py  
    math_functions.py  
    module2.py  
    module3.py etc....
```

### Task 6:  Importing Packages

* To use modules from a package, you need to import the package or specific modules from it.
* Use the import keyword followed by the package name and the module name separated by a dot.
* You can then access the module's contents using the dot notation:  `package_name.module_name.function_name()`.

**Example:** We can now pull in our package and access the modules and contained functions as needed within a new python file.

```
# Import module  
import basic_functions.math_functions  
  
basic_functions.math_functions.add(2,3) # Output: 5  
  
# Import and use alias  
import basic_functions.math_functions as mf  
  
mf.add(2,3)  
  
# Import just the function  
from basic_functions.math_functions import add  
  
add(2,3)
```

### Task 7: Using Third-Party Packages

* Python has a vast ecosystem of third-party packages/libraries that provide additional functionality.
* To use a third-party package, you first need to install it using a package manager like pip.
* Open a terminal or command prompt and run the following command to install a package:

```
pip install package_name
```

### Solution Code

```
# Import module  
import basic_functions.math_functions  
  
basic_functions.math_functions.add(2,3) # Output: 5  
  
# Import and use alias  
import basic_functions.math_functions as mf  
  
mf.add(2,3)  
  
# Import just the function  
from basic_functions.math_functions import add  
  
add(2,3)
```

### Considerations

Once installed, you can import and use the package in your Python scripts just like you would with your own modules and packages.

By following these steps, you can create and use functions, modules, and packages in your Python projects. This modular approach helps in organizing code, promoting reusability, and maintaining a clean and structured codebase.

**Remember:** Choose meaningful names for your functions, modules, and packages, and document them appropriately using comments or docstrings to enhance code readability and understandability.

Practice creating your own functions, modules, and packages to solidify your understanding of these concepts. Explore the Python Standard Library and third-party packages to leverage existing functionality and speed up your development process.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239325

Scraped At: 2026-05-14T16:01:03.184222
