# Technical Lesson: Integrated Development Environment

# Technical Lesson: Integrated Development Environment

## ![](https://moringa.instructure.com/courses/1391/files/620171/preview) Technical Lesson: Integrated Development Environment

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 60 min.

Let's look closer at the primary IDE we will be using: VS Code. IDEs are comprehensive tools that significantly enhance the coding experience by combining a variety of functionalities in a single platform. Most IDEs feature a source code editor, built-in debuggers, and numerous other utilities designed to streamline the coding process. These tools not only speed up the writing and management of code but also play a crucial role in ensuring better code quality and security.

Debuggers in IDEs are particularly powerful, offering the ability to analyze code execution, inspect variables, and monitor memory usage in real-time. This makes it easier to understand how your program operates and to identify and fix issues efficiently. With such capabilities, IDEs simplify complex tasks and make the development process more intuitive, allowing you to focus on creating robust and secure software.

By the end of this lab, you should be able to:

* Open and launch files in VS Code using terminal command `code`.
* Write and run basic Python scripts in VS Code.
* Use the major components of VS Code, including the Python Debugger.

### Resources

To get started, ensure you have the following:

* **IDE:** An application that includes autocompletion, debugging, graphical elements, and other components to aid in software or script development.
* **[VS Code:


  Links to an external site.](https://code.visualstudio.com/docs/python/python-quick-start)** Microsoft's feature-rich IDE that integrates seamlessly with various tools and languages, including Python.

### Tools

* **Tools Required:** Python and VS Code should be installed on your computer. Refer to the previous steps in this lesson for installation, if needed.

### Instructions

### Task 1: Setting Up the VS Code Terminal

1. **Open VS Code:**

* Open VS Code from the Start menu (Windows), Applications folder (macOS), or application launcher (Linux).

1. **Check if the `code` Command is Already Installed:**

* Open your **terminal** (Command Prompt on Windows, Terminal on macOS/Linux).
* Type `code --version` and press Enter.
  + **If you see a version number**, you're all set! You can skip the next step and go to step 4.
  + **If you see an error like `command not found` or `'code' is not recognized`**, follow Step 3 to install it.

1. **Install the `code` Command in VS Code:**

* Click on the search bar at the top center of VS Code (magnifying glass icon) and type `>`.
* Start typing **Shell Command: Install 'code' command in PATH** in the command palette that appears. It should appear in the dropdown.

![shell command screenshot](https://moringa.instructure.com/courses/1391/files/620130/preview)

* Select it from the dropdown to install the command.

1. **Use the `code` Command to Open Files:**

* Open your terminal or command prompt.
* Navigate to the directory where your file or project is located.
* Type `code
  <filename>`  to open a specific file or `code
  .` to open the entire directory in VS Code.

### Task 2: Navigating the VS Code User Interface

When you launch VS Code, you will see a main window with various elements that aid in development. Read through the [Quick Start Guide for Python in VS Code


Links to an external site.](https://code.visualstudio.com/docs/python/python-quick-start) for an overview of these elements.

**The User Interface**

* **Main Editor Area:** This is where you will write and edit your code. Initially, it displays the Welcome page or and open file.
* **Sidebar:**Located on the left, it contains icons for different views like file explorer, search, version control, debugging, and extensions.

### Task 3: Getting Started with Files

1. **Open the Explorer View:**

* Click on the Explorer icon at the top of the sidebar.

1. **Create or Open a Folder:**

* Click Open Folder or Add Folder to Workspace
* For this lab, create and Example folder in your Documents directory and open it.

1. **Create a New File:**

* Click the New File icon in the Explorer.
* Type example.py to name the file and indicate it is a Python script.
* You will now see the new file in your Example folder.

### Task 4: Running Python Code in VS Code

To run your Python scripts in VS Code, you need to select the appropriate Python Interpreter: 

1. **Install the Python package from Microsoft:**

* Navigate to the Extensions tab on the left side of VSCode.
* Type "Python" in the search bar.
* Find the package called "Python" by Microsoft and select "Install."

![python package by Microsoft in the Visual Studio Code extension tab.](https://moringa.instructure.com/courses/1391/files/620153/preview)

1. **Once the package is installed, select the Python Interpreter:**

* Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS) to open the command palette.
* Type `Python: Select Interpreter` and choose the path where Python is installed.

1. **Running Your Code:**

* **Line by Line:** Enter the code below in your example.py file terminal window. Press Shift+Enter to run both lines and see the output in the integrated terminal.

```
myvar = 5  
print(myvar * 25)
```

* **Entire Script:** Click the play button (Right arrow symbol) in the upper right corner to execute the whole script. This is similar to running `python3 example.py` in the terminal.

### Task 5: Debugging Python Code

Debugging is a critical part of development, and VS Code offers robust tools to make it easier.

**What are Breakpoints?**

Breakpoints are intentional pausing points placed in your code that allow you to halt the execution of your program at specific lines or conditions. When the program reaches a breakpoint during execution, it stops, and the debugger takes control, allowing you to examine the program's state, variables, and flow at that particular point. Breakpoints are essential tools for debugging because they enable you to:

* **Pause the program execution:** When a breakpoint is hit, the program stops running, giving you a chance to inspect its state and behavior.
* **Examine variables:** While paused at a breakpoint, you can view the values of variables, objects, and expressions at that specific point in the program's execution. This helps you understand how data is being processed and also helps identify any unexpected values.
* **Step through code:** Once paused at a breakpoint, you can use debugging commands to step through the code line by line, allowing you to follow the program's flow and understand how it reaches a particular state or condition.
* **Identify logic errors:** By strategically placing breakpoints at critical points in your code, such as inside conditional statements or loops, you can examine the program's behavior and identify logic errors or unexpected paths of execution.
* **Modify variable values:** Some debuggers allow you to modify the values of variables while paused at a breakpoint, enabling you to test different scenarios or fix incorrect values on the fly.

1. **Set Breakpoints**

* Click on the gutter next to the line numbers
* Alternatively, you can use debugging commands or keyboard shortcuts to set breakpoints programmatically.

1. **Start Debugging**

When you start debugging your program, the debugger will pause the execution when it reaches a breakpoint. Use debugging commands from the toolbar to control the program's execution.

* Go to the Run and Debug icon in the sidebar or press F5.
* Select the Python debugger and start debugging

1. **Using Debugging Controls:**

* **Continue (F5):**Resume execution until the next breakpoint or the end.
* **Step Over (F10):** Execute the next line of code but do not step into functions.
* **Step Into (F11):** Step into the function calls to see their execution.
* **Step Out (Shift+F11):** Complete the current function and return to the caller.
* **Restart and Stop:** Restart or stop the debugging session.

1. **Inspecting Variables and State:**

* While debugging, view the values of variables and expressions in the “Variables” section.
* Modify variable values during a pause to test different scenarios.

### Task 6: Example Debugging Session

1. **Create a Complex Script:**

* Create a new file in VSCode and name it **debug\_example.py**.
* Copy and paste the code below into the file.

```
def calculate_sum(a, b):  
    return a + b  
  
def calculate_product(a, b):  
    return a * b  
  
def main():  
    x = 5  
    y = 0  # This will cause a division by zero error  
    sum_result = calculate_sum(x, y)  
    print(f"Sum: {sum_result}")  
  
    product_result = calculate_product(x, y)  
    print(f"Product: {product_result}")  
  
if __name__ == "__main__":  
    main()
```

1. **Set a Breakpoint:**

* Place a breakpoint on the line sum\_result = calculate\_sum(x, y).

1. **Run the Debugger:**

* Use the Run and Debug button and observe how the code pauses at the breakpoint.

1. **Step Through the Code:**

* Use the debugging controls to step through the code and observe the behavior and variable values.

### Task 7: Resources

VS Code is equipped with many other features that will be useful as you advance in your programming journey.

* **Git/Version Control:** Easily manage your code versions and collaborate with others.
* **Virtual Environments:** Use and manage different Python environments for various projects.
* **Extensions:** Enhance VS Code's functionality with thousands of available extensions.

**Explore Further:**

* [VS Code Documentation


  Links to an external site.](https://code.visualstudio.com/docs)
* [Python Extension Docs


  Links to an external site.](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [VS Code Debugging


  Links to an external site.](https://code.visualstudio.com/docs/editor/debugging)
* [Python Debugging


  Links to an external site.](https://code.visualstudio.com/docs/python/debugging)

By following this walkthrough, you’ve learned how to set up and use VS Code for Python development, run scripts, and debug code effectively. These skills are fundamental for enhancing your coding efficiency and understanding. Continue to explore VS Code’s features and practice regularly to become proficient in using this powerful IDE.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239127

Scraped At: 2026-05-14T15:17:17.635278
