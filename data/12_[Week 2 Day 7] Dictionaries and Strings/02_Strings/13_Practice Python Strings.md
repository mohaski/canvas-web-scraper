# Practice: Python Strings

# Practice: Python Strings

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Python Strings

Icon Progress Bar (browser only)

3 min read

Imagine you're working as a developer for a social media platform. One of your tasks is to develop a program that helps users create strong and secure passwords. Strong passwords typically include a combination of uppercase letters, lowercase letters, numbers, and symbols.

In this scenario, strings can be used to:

* Store the password entered by the user.
* Check the password for various criteria (uppercase, lowercase, numbers, symbols).
* Provide feedback to the user on the strength of their password.

The objective of this practice is to gain hands-on experience with string manipulation and validation techniques in Python. You will have the opportunity to practice your skills in:

* Accessing and modifying characters in a string.
* Checking for the presence of specific characters (uppercase, lowercase, numbers, symbols).
* Using conditional statements to evaluate password strength.

### Instructions

### [Step 1: Get User Input](#dpPanel0)

Use the input function to prompt the user to enter their password and store it in a variable named password.

### [Step 2: Check Password Length](#dpPanel1)

* Use the `len` function to determine the password length and store it in a variable named `password_length`.
* Use an if statement to check if the password length is less than a minimum threshold (e.g., 8 characters). 
  + If it is, print a message suggesting a longer password.

### [Step 3: Validate Character Types](#dpPanel2)

* Initialize variables to track the presence of uppercase letters (`has_uppercase`), lowercase letters (`has_lowercase`), numbers (`has_number`), and symbols (`has_symbol`). Set them to False initially.
* Iterate through each character in the password using a for loop.
  + Inside the loop, use string methods like `isupper()`, `islower()`, `isdigit()`, and `isalnum()` (checks for alphanumeric characters) to check the character type.
  + Based on the checks, update the corresponding tracking variables (e.g., has\_uppercase = True if an uppercase letter is found).

### [Step 4: Evaluate Password Strength](#dpPanel3)

* Use another if statement to check if all tracking variables (`has_uppercase`, `has_lowercase`, `has_number`, `has_symbol`) are True.
  + If all conditions are met, the password likely contains a good mix of character types and is considered strong. Print a message congratulating the user.
  + If not all conditions are met, print a message suggesting improvements for a stronger password (e.g., include uppercase letters, numbers, or symbols).

### Resources

* The strings technical lesson from this topic.

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Solution

### [Select for Solution](#dpPanel4)

```
# Minimum password length  
min_length = 8  
  
# Get user input  
password = input("Enter your password: ")  
  
# Check password length  
password_length = len(password)  
if password_length < min_length:  
    print(f"Password is too short. Minimum length is {min_length} characters.")  
else:  
    # Initialize tracking variables  
    has_uppercase = False  
    has_lowercase = False  
    has_number = False  
    has_symbol = False  
  
    # Validate character types  
    for char in password:  
        if char.isupper():  
            has_uppercase = True  
        elif char.islower():  
            has_lowercase = True  
        elif char.isdigit():  
            has_number = True  
        elif not char.isalnum():  # Check for symbols (not alphanumeric)  
            has_symbol = True  
  
    # Evaluate password strength  
    if has_uppercase and has_lowercase and has_number and has_symbol:  
        print("Strong password! You're using a good mix of characters.")  
    else:  
        print("Password could be improved. Consider including:")  
        if not has_uppercase:  
            print("- Uppercase letters (A-Z)")  
        if not has_lowercase:  
            print("- Lowercase letters (a-z)")  
        if not has_number:  
            print("- Numbers (0-9)")  
        if not has_symbol:  
            print("- Symbols (e.g., !@#$%^&*)")
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239287

Scraped At: 2026-05-14T15:58:16.412984
