# Lab: Task Management System

## ![](https://moringa.instructure.com/courses/1391/files/620140/preview?) Lab: Task Management System

You are a junior software developer working for a productivity app company. Your task is to create a Python program that allows users to manage their tasks and track their progress.

You will need to create a task management system that allows users to add tasks, mark tasks as complete, view pending tasks, and track their progress. You should format the structure to store tasks as a list of dictionaries, each dictionary representing one task.

By completing this lab exercise, you will gain practical experience in integrating functions, modules, packages, and data input validation to create a functional task management system. You will learn how to design and implement a modular and maintainable codebase that handles user input, data validation, and data processing.

### Tools and Resources

* Python IDE, [Visual Studio Code](https://code.visualstudio.com/ "Link")
* Download the three (3) following files that contain starter code for proper function and file naming. You should not change the file names or internal function names within.
  + [main.py file](https://moringa.instructure.com/courses/1391/files/620212?verifier=RdBtnjdjAGiGIKIO23wvPLufWOQfQM8NQhADgQM6&wrap=1)[Download main.py file](https://moringa.instructure.com/courses/1391/files/620212/download?verifier=RdBtnjdjAGiGIKIO23wvPLufWOQfQM8NQhADgQM6&download_frd=1)
  + [task\_utils.py](https://moringa.instructure.com/courses/1391/files/620213?verifier=dfiVwqOIbJaP8stPo74f51cbUIlwppLgE2EhT5DW&wrap=1)[Download task\_utils.py](https://moringa.instructure.com/courses/1391/files/620213/download?verifier=dfiVwqOIbJaP8stPo74f51cbUIlwppLgE2EhT5DW&download_frd=1)
  + [validation.py](https://moringa.instructure.com/courses/1391/files/620218?verifier=QMdlbGMPf8yXiVFtoG0Rr7emVaWJDgCEzUGqeK01&wrap=1)[Download validation.py](https://moringa.instructure.com/courses/1391/files/620218/download?verifier=QMdlbGMPf8yXiVFtoG0Rr7emVaWJDgCEzUGqeK01&download_frd=1)

### Instructions

### [Identify the Problem](#dpPanel0)

Create a Python program that allows users to manage their tasks and track their progress. The task management system should allow users to add tasks, mark tasks as complete, view pending tasks, and track their progress.

* **Task 1:** Define a dictionary structure to represent a task. You can use the structure below.
* **Task 2:** Implement functions for adding tasks.
* **Task 3:** Develop functions for validation.
* **Task 4:** Develop functions for marking tasks as complete and viewing pending tasks.
* **Task 5:** Create a main script to interact with the task management system.

### [Develop the Code](#dpPanel1)

### [Task 1: Define a dictionary structure](#dpPanel2)

Define a dictionary structure to represent a task. You can use the following:

```
task = {"title": "Groceries",  
 "description": "Shop at Market Basket for food",   
 "due_date": "2024-06-26",  
 "completed": True}
```

### [Task 2: Implement functions for adding tasks](#dpPanel3)

Create functions to encapsulate specific tasks and promote code reusability.

In the `validation.py` module, create functions to validate user input for task details such as title, description, and due date.

Function names: 

1. 1. `validate_task_title`
   2. `validate_task_description`
   3. `validate_due_date`

In the `task_utils.py` module, define functions for adding a task, marking a task as complete, viewing pending tasks, and calculating progress, making sure to consider validation.

Function names:

1. 1. `add_task`
   2. `mark_task_as_complete`
   3. `view_pending_tasks`
   4. `calculate_progress`

### [Task 3: Organize functions with modules](#dpPanel4)

Organize related functions into modules to improve code structure and maintainability:

* Create separate modules for task-related functions (`task_utils.py`) and data input validation functions (`validation.py`).

Group related modules into packages to create a hierarchical structure and enable better code organization:

* Create a package/folder called `task_manager` and organize the modules (`task_utils.py` and `validation.py`) within this package.

### [Task 4: Develop functions for validation](#dpPanel5)

Implement data input validation within functions and modules to ensure data integrity and prevent errors:

* In the `validation.py` module, implement functions to handle invalid input and provide appropriate error messages.
* Use the validation functions in the `task_utils.py` module to validate user input before adding tasks.

### [Task 5: Develop functions for marking tasks as complete and viewing pending tasks](#dpPanel6)

Create a main script to interact with the task management system. Use the functions, modules, and packages in the main script to solve the overall problem:

* + In the main.py script, create a menu-based interface for the user to interact with the task management system.
  + Use the functions from the `task_utils.py` module to perform operations such as adding tasks, marking tasks as complete, viewing pending tasks, and tracking progress.

Your main script needs to be on the same directory level as the package task\_manager.

### [Test and Refine](#dpPanel7)

* Run your program and test various input scenarios, including valid and invalid inputs.
* Verify that the validation functions correctly identify and handle invalid inputs.
* Refine your validation criteria and error messages if needed to provide a better user experience.

### Submission

* Click the L*oad Lab: Task Management System* button below to launch this assignment in CodeGrade.
* Upload your Python file to the *click here or add files to upload* field.
* For additional information on submitting assignments in CodeGrade: [Getting Started in Canvas.


  Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)

### Grading Criteria

* Use the rubric below as a guide for how this lab is graded.
* You submission will be automatically scored in CodeGrade.
* You can review your submission in CodeGrade and see your final score in your Canvas grades.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239346

Scraped At: 2026-05-14T16:02:17.448408
