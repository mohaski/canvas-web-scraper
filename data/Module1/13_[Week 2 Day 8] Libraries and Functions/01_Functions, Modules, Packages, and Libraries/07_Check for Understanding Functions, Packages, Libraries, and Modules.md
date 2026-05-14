# Check for Understanding: Functions, Packages, Libraries, and Modules

# Check for Understanding: Functions, Packages, Libraries, and Modules

## ![](https://moringa.instructure.com/courses/1391/files/620140/preview?) Check for Understanding: Functions, Packages, Libraries, and Modules

Icon Progress Bar (browser only)

Now is your opportunity to see how much you can recall from the topic! Take a moment to answer the questions below. These are not graded, but they will allow you to check how much you are putting together the content in this lesson and review before moving to a new topic. 

### Quick Check: Financial Application

You are a junior Python developer working on a project that involves building a modular, reusable Python library for a financial application. The application requires a currency conversion feature that can be used across different parts of the system. Your task is to create a well-organized library that includes functions for currency conversion, and you want to structure your code using modules and packages.

**Which of the following steps correctly describes the process of building a modular Python script that can be reused across different parts of your financial application?**

Write all the functions for currency conversion in a single Python script, then copy and paste this script into every part of the application that needs the conversion feature.
:   **Incorrect**, copying and pasting code across different parts of the application leads to redundancy and makes the code harder to maintain.

Create a single module with all your functions, then import this module directly into your main application script without organizing it into a package.
:   Incorrect, while creating a single module is a step in the right direction, this approach lacks the organization and scalability provided by using packages.

Define the currency conversion functions in a module named `converter.py`, organize this module within a package, and create an `__init__.py` file to make the package importable. Then, import the package into different parts of the application as needed.
:   **Correct:** Organizing the currency conversion functions into a module within a package ensures that your code is modular, reusable, and maintainable. This approach allows you to easily import the package into different parts of the application.

Develop the currency conversion functionality directly within the main application script, using inline code rather than functions or modules, to ensure that it is always available wherever needed.
:   Incorrect, writing the functionality directly within the main script without using functions, modules, or packages makes the code less organized and more difficult to manage or reuse.

[Check Answer](#)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239323

Scraped At: 2026-05-14T16:00:55.707281
