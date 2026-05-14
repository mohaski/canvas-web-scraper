# Technical Lesson: Input Validation

# Technical Lesson: Input Validation

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Technical Lesson: Input Validation

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time: 1 hour**

In this lesson, we will explore the process of data conversion and input validation in Python. Data conversion involves transforming data from one type to another, while input validation ensures that user input meets specific criteria. By mastering these concepts, you'll be able to handle user input effectively, prevent errors, and maintain data integrity in your Python programs.

In the following lesson and video we'll focus on the key steps of the input validation process, including identifying input fields, defining validation criteria, implementing validation functions, prompting for user input, and handling validation errors.

By the end, you'll have a solid understanding of how to apply data conversion and input validation techniques in your Python code.

Let's consider a simple registration form that asks for a user's name, age, and email address.

### Resources

* Lesson content about input validation and regular expression (regex).

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Instructions

The following video and steps will outline how to complete the code in the lesson to:

* Work with dictionaries to effectively store and retrieve data.
* Access and update dictionary values using keys.
* Utilize string operations to process product names and information.
* Apply problem-solving skills to design a user-friendly inventory management system.

[VIDEO LINK](https://player.vimeo.com/video/1003497440?h=a04880b562)

### Task 1: Identify the Input Fields

Determine which input fields require validation in your program.

* Name, Age, and Email

```
def validate_name(name):  
  
def validate_age(age):  
  
def validate_email(email):
```

### Task 2: Implement Validation Functions

* Create a separate validation function for each input field.
* Use appropriate techniques like type checking, range checking, and regular expressions to validate the input.
* Raise exceptions or return error messages when validation fails.

+ raise ValueError()

```
def validate_name(name):  
    if not name:  
        raise ValueError("Name cannot be empty.")  
    if not name.isalpha():  
        raise ValueError("Name can only contain letters and spaces.")  
  
def validate_age(age):  
    if not age.isdigit():  
        raise ValueError("Age must be a positive integer.")  
    age = int(age)  
    if age <= 0:  
        raise ValueError("Age must be a positive integer.")  
  
def validate_email(email):  
    if not email:  
        raise ValueError("Email cannot be empty.")  
    if "@" not in email:  
        raise ValueError("Invalid email format.")
```

### Task 3: Prompt for User Input

* Use the input() function to prompt the user for each input field.
* Provide clear instructions or examples to guide the user on the expected input format.

```
name = input("Enter your name: ")  
age = input("Enter your age: ")  
email = input("Enter your email address: ")
```

### Task 4: Validate and Handle Input

* Call the respective validation functions for each input field.
* Handle validation exceptions or errors gracefully using a try-except block.
* Provide meaningful feedback to the user when validation fails, indicating the specific issue.
* If validation passes, proceed with further processing or storage of the validated data.

```
try:  
    validate_name(name)  
    validate_age(age)  
    validate_email(email)  
    print("Registration successful!")  
    # Further processing or storage of validated data  
except ValueError as e:  
    print("Validation error:", str(e))
```

### Task 5: Test and Refine

* Run your program and test various input scenarios, including valid and invalid inputs.
* Verify that the validation functions correctly identify and handle invalid inputs.
* Refine your validation criteria and error messages if needed to provide a better user experience.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239340

Scraped At: 2026-05-14T16:01:56.575017
