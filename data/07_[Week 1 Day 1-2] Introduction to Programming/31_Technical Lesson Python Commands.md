# Technical Lesson: Python Commands

# Technical Lesson: Python Commands

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Technical Lesson: Python Commands

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time: 30 min.**

This lesson is designed to build on your initial introduction to Python commands and processes. By engaging with practical exercises and real-world examples, you will gain hands-on experience with Python commands, reinforcing your understanding and ability to apply them effectively in various scenarios.

Python is a versatile coding language widely used by cybersecurity professionals, software engineers, and data scientists to automate tasks, analyze data, and solve complex problems. This lesson focuses on foundational Python commands essential for writing efficient scripts. Understanding these basics will empower you to tackle simple or repetitive tasks with ease and set a solid foundation for more advanced programming concepts. In the following video, you will learn about the programming concepts and commands used to create a simple python script.

[VIDEO LINK](https://player.vimeo.com/video/986746279?h=5bedd4e673)

### **Key Concepts Covered**

1. **Variables:** Learn how to store and manipulate data using variables in Python.
2. **Conditional Statements:** Explore how to use if statements to control the flow of your code based on specific conditions.
3. **Outputting Information:** Understand how to use the print() function to display variable values and results.
4. **Code Documentation:** Discover the importance of using comments to document your code, making it easier to read and maintain.

### Learning Outcomes

After completing this lab, you should be able to:

* Create a basic Python script to automate tasks or perform basic operations.
* Use variables in a Python script to store and manage data within your script.
* Use `if` statements to execute different branches of code based on specified conditions.

### Resources

* Consider the [process identified](https://moringa.instructure.com/courses/1391/pages/process-python-variables "Python Commands Process") in this module for writing variable statements and the key components of basic Python commands.

### Tools

* Code along using the Python IDE, [Visual Studio Code.](https://code.visualstudio.com/ "Link")
* An add-on for Python that provides additional functionality. The use is import `<package>` and exposes code within that package that can be used in the current script (more on this is a further module).

### Instructions for Hello World

Hello World is a foundational script in programming that prints “Hello World” onto the screen. It’s a common starting point for new programmers to ensure their development environment is correctly set up and to understand the basic syntax and logical flow of their code. This simple yet powerful exercise will allows you to confirm you Python setup is functioning properly without the complexity of more advanced programs.

### Step 1: Plan Your Code

Before writing any code, it is essential to have a clear plan. Create a flow of what your code will do. This helps to structure your thoughts and provides a roadmap for your coding process.

![flow chart defining actions for simple hello world python script](https://moringa.instructure.com/courses/1391/files/620198/preview)

### Step 2: Create a File

1. **Create a File in VSCode**:

* Open the Visual Studio Code editor.
* Create a new file named hello.py.
* Save this file in a dedicated folder in your Documents for easy navigation.

1. **Add Code to the File:**

* In the file, type the following: `print("Hello World")`

### Step 3: Begin Coding

The outputs should be the same regardless of where the Python code is executed, but the method of running the script will be based on where it is running.

Let's look at a few different approaches to running your script:

#### Running the Script in VS Code

* Click the Right Arrow Symbol in the top right corner of VS Code.

![VSCode menu image](https://moringa.instructure.com/courses/1391/files/620205/preview)

* **You can also** open the terminal in VS Code and run `$ python hello.py`.

**![VSCode terminal window](https://moringa.instructure.com/courses/1391/files/620202/preview)**

#### Running the Script in Linux/macOS Terminal

We can also run `$ python hello.py` in an independent terminal.

1. If we have included a shebang in the python script, we can run via a shortcut but we first need to provide permission to execute it

```
#!/usr/bin/python3  
  
print("Hello World!")
```

* The #! is called a she-bang.  After the she-bang, the path and application listed tells Linux how to execute the code. In this case, /usr/bin/python3 is the path to the python executable in Linux.

1. We now need to give permission via the `chmod` command (short for change mode) which allows us to change permission for reading and writing and executing files.

**Note:** We won’t dive too deep into this in the python course.

* In a terminal window (this can be done from VSCode terminal), type `$ chmod 755 hello.py`
* We should now be able to run the script using `$ ./hello.py`

**![VSCode terminal window](https://moringa.instructure.com/courses/1391/files/620202/preview)**

* When using Mac or Linux, the chmod 755 command sets the read and execute permissions on the file. Verify this with an extended listing command (`ls -l`).

![chmod command screenshot](https://moringa.instructure.com/courses/1391/files/620186/preview)

#### Running the Script in Windows PowerShell

* Use the command `python .\hello.py` to execute the script.

![hello.py command in terminal](https://moringa.instructure.com/courses/1391/files/620192/preview)

#### Step 4: Add Code Documentation and Comments

**Comments** are a way to add descriptions on parts of the code or other information useful to coders.

##### **How to Add Single-line Comments**

* Use a hash-tag symbol (#) is a way to insert a single-line comment.
* This can also be done at the end of a line.
* Comments will not be run or operated on via the Python interpreter, allowing you to document your code with ease.

```
#!/usr/bin/python3  
  
# This is a comment on it's own line  
  
print("Hello World!")  # This is a comment in a line of code, this code will print out the string Hello World!
```

##### **How to Add Multi-line Comments**

* Three double quotes: """<comments>"""
* Three single quotes, '''<comments> '''

```
#!/usr/bin/python3  
  
""" This is a multline comment.  
This can be a good place to included detailed information about the code,  
things like the author, purpose, date of update, etc...  
"""  
  
print("Hello World!")  
  
''' Single triple quotes will also work as well,  
to provide multiline comments if you need further documentation  
'''
```

**How to Show a Comment on a Flow Chart**

* Before modifying the code it can be helpful to create a flow chart.  This symbol is used for comments:

![Comments symbol for flowchart](https://moringa.instructure.com/courses/1391/files/620115/preview)

* Here is an example of how to add comments to a flow chart.

![FlowChart with Comments](https://moringa.instructure.com/courses/1391/files/620196/preview)

* Modify the **hello.py** to include comments about the script and the code it runs.

```
#!/usr/bin/python3  
  
# Author: <put your name here>  
  
# Date: <put today's data here>  
  
# version: 1.1  
  
'''  
  
<Insert a general description of the program here>  
  
'''  
  
print("Hello World!")
```

#### Step 5: Test and Refine

**Save and run your Python script with the comments added.**

* The outcome will print Hello World.
* The comments should have no effect on the outcome of the script. They are only to aid anyone viewing the code.

#### Step 6: Add Variables

**Variables** can hold values, like numbers or strings (text), as well as more advanced data types. Let’s write a new script called **hello2.py.**

1. **Create a flowchart (or Pseudocode)** to help formulate your script before writing it in Python.

* Add a string (text) variable to it.

![Flowchart with variables](https://moringa.instructure.com/courses/1391/files/620165/preview)

**Add Variable to Script**

* Add the text variable to your script in VS Code and save it as a new file.

```
#!/usr/bin/python3  
  
# Author: <put your name here>  
  
# Date: <put today's data here>  
  
# version: 1.1  
  
'''  
  
<Insert a general description of the program here>  
  
'''  
  
text = "Hello World!"  
  
print(text)
```

* Run the script and note the same output as before.
* The variable text, with an assigned value of the string “Hello World!”, is printed to return the same result as previously.

By using a variable, it would be easy to change the text, when needed or to reference that same text in multiple places within the script. Using variables can help to make your code more efficient and ‘pythonic’ versus hard coding values.

#### Step 7: Add User Input

**The User Input Command:** The command `input()` requests input directly from the user. This input is then stored into a variable for use in the script.

Let's try this out:

1. Creating another script, `user.py` to get user input.
2. Add the following code to the script:

```
#!/usr/bin/python3  
  
# Author: <put your name here>  
  
# Date: <put today's data here>  
  
# version: 1.1  
  
'''  
  
<Insert a general description of the program here>  
  
'''  
# The text within the input will be what is prompted to the user  
username = input("What is your name? ")  
  
text = "Hello"  
  
print(text, username)
```

* The `input("What if your name?")`statement solicits, via the terminal, an input from the user. This input is a string by default, which is different from an integer.
* If you wanted a number to be assigned instead of a string, you would use the `int()` function with the input statement to change from a string to an integer.

1. Run this new script and input `Student` when prompted for the name.
2. You should see the following output:

![VS Code Terminal output](https://moringa.instructure.com/courses/1391/files/620109/preview)

#### Step 8: Add if Statement

##### Using if Statements in Python

To evaluate variables, we need to use the `if` statement. Here’s how to use if statements in Python:

1. **Structure of an** **if** **Statement**:

* Begin with the if keyword followed by a condition to evaluate.
* End the if statement line with a colon (:).
* Indent the block of code that should run if the condition is true. By Python standards, this indentation is 4 spaces, not a tab character.

1. **Indentation**:

* Most Integrated Development Environments (IDEs) like VS Code automatically convert tabs to 4 spaces. However, if you’re using another editor, ensure it uses 4 spaces for indentation to avoid syntax errors.
* Proper indentation is crucial because it defines the code block that belongs to the if statement.

1. **Execution Flow**:

* The code within the indented block will only execute if the condition in the if statement evaluates to true.
* If the condition is false, Python will skip the indented block of code.

1. **Using** **else** **Statements**:

* An else statement can be used to define a block of code to run if the if statement’s condition is false.
* The else statement also ends with a colon (:) and is followed by an indented block of code.

1. **Automatic Indentation in VS Code**:

* VS Code automatically indents the line after an if statement when formatted correctly with a colon. This helps ensure your code is properly formatted.

##### if Statement Example

1. **Create** a new file: `user2-py`.
2. **Add the following script** into the file:

```
#!/usr/bin/python3  
  
# Author: <put your name here>  
  
# Date: <put today's data here>  
  
# version: 1.1  
  
'''  
  
<Insert a general description of the program here>  
  
'''  
# The text within the input will be what is prompted to the user  
username = input("What is your name? ")  
  
# The if statement checks if the inputed username equals the string Student  
if username == "Student": # It uses the double equals operator (==) to do so  
print("Hello Flatiron Student!") # Note the indentation  
else: # When the username does not equal Student the else block will operate  
print("Hello random person!") # Note the identation
```

1. **Run the Script:**

* Save the user2.py file.
* Open the terminal in VS Code or any other terminal.
* Navigate to the directory where user2.py is saved.
* Run the script by typing `python user2.py`

1. **Test the Script**

* When prompted, enter **Student** as the name and observe the output.
* Run the script again and enter a different name to see the else block in action.

![VS Code Terminal output](https://moringa.instructure.com/courses/1391/files/620176/preview)

#### Step 9: Add Integers

In this step, we will explore how to use integers as variables by accepting user inputs. Additionally, we will learn how to include variables within strings using a special type of formatting called f-strings.

1. **Create a new Python script named** `int.py`.
2. **Write the Basic Addition Script**

Using the script below, we can create a simple addition program that takes two numbers as input from the user, adds them together, and displays the result. Type the following script into the `int.py` file.

**NOTE:** When accepting user input, it is important to convert the input from a string to an integer. This can be done using the `int()` function.

```
#!/usr/bin/python3  
  
# Author: <put your name here>  
  
# Date: <put today's date here>  
  
# version: 1.1  
  
a = int(input("Enter a number: ")) # Using int() to convert string input  
b = int(input("Enter another number: "))  
  
print(a + b) # We can use basic arithmetic operator (+) to add our two integers
```

1. **Enhance Output with f-Strings**

We can make our output more informative by displaying the entered numbers and the results using f-strings.  F-strings allow you to embed expressions inside string literals, using curly braces {}.

1. **Write the Enhanced Script**

Update the `int.py` script to include f-string formatting. 

```
#!/usr/bin/python3  
  
# Author: <put your name here>  
  
# Date: <put today's date here>  
  
# version: 1.1  
  
a = int(input("Enter a number: ")) # Using int() to convert string input  
b = int(input("Enter another number: "))  
  
result = a + b  
  
print(f"Simple addition script. You entered {a} + {b} resulting in {result}")
```

1. **Run the Enhanced Script**

* Save the updated `int.py` file.
* Run the script, as before.

1. **Expected Output**

The output should now be a formatted string showing the entered numbers and the result.

```
Enter a number: 5  
Enter another number: 3  
Simple addition script. You entered 5 + 3 resulting in 8
```

By following these steps, you can effectively use integers as variables and enhance your output using f-strings to create informative and user-friendly Python scripts.

### Considerations

When working with Python scripts, you may encounter several issues. Here are some common problems and how to address them:

#### General Troubleshooting

* **Error Messages:** If you encounter an error, try searching the error message along with the keyword "Python on Google. This often helps identify the cause and solution.

#### Common Issues with Copying and Pasting Code

**Smart Quotes**: When copying code from a Windows machine, the quotes may be Smart Quotes (“ ” or ‘ ’) instead of the standard straight quotes (” “ or ’ ’). Smart Quotes can cause issues with the Python interpreter.

* **Solution**: Use find-and-replace or a different text editor to replace Smart Quotes with straight quotes. Alternatively, use the “Paste as Plaintext” option when pasting code.

**End-of-Line Characters**: Windows and Linux use different characters for line endings (carriage return and line feed combinations), which can lead to errors like “invalid character in identifier.”

* **Solution**: Ensure your text editor is set to use Unix/Linux style line endings (LF) instead of Windows style (CRLF).

### Indentation Errors

**Importance of Indentation**: Python uses indentation to define code blocks, including the body of an if statement. Incorrect indentation can lead to syntax errors or unexpected behavior.

* **Solution**: Maintain consistent and proper indentation (usually 4 spaces) throughout your code.

### Comparison Operators

**Using Comparison Operators**: `if` statements often involve comparisons using operators like ==, !=, <, >, <=, and >=.

* **Common Mistake**: Using = instead of == for equality comparison is a frequent error.
* **Solution**: Ensure you use the correct comparison operator for your needs. The next module will explore common operators in more depth.

### Formatting f-strings

**Correct Syntax**: f-strings provide a convenient way to embed expressions and variables within string literals. However, using incorrect syntax or missing placeholders can lead to errors.

* **Solution**: Use the correct syntax for f-strings: `f"Your string {variable} here"`. Ensure all placeholders within curly braces {} match the variables or expressions you want to include.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239134

Scraped At: 2026-05-14T00:26:26.049150
