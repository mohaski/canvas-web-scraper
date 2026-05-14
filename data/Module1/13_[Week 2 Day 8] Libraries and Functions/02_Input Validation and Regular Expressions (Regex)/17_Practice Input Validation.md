# Practice: Input Validation

# Practice: Input Validation

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Input Validation

Icon Progress Bar (browser only)

3 min read

In this practice scenario, you'll apply your knowledge of data conversion and input validation in Python to a real-world problem. Imagine you're a junior developer working for a car rental company. Your task is to create a program that allows customers to enter their information when reserving a rental car.

The program should prompt the user to enter their email address, driver's license number, and rental duration in days. You need to validate the input to ensure that the email address is in a valid format, the driver's license number consists of only alphanumeric characters, and the rental duration is a positive integer. Additionally, you'll convert the rental duration to an integer for further processing.

By completing this practice activity, you'll strengthen your understanding of the input validation process and gain practical experience in applying data conversion and validation techniques to a real-world scenario.

### Instructions

* [Task 1: Define the Problem](#dpPanel0Content)
* [Task 2: Write the Code](#dpPanel1Content)
* [Task 3: Test and Refine](#dpPanel5Content)
* [Task 4: Document and Maintain](#dpPanel6Content)

### Task 1: Define the Problem

Create a program that allows customers to enter their information when reserving a rental car.

* Prompt the user to enter their email address, driver's license number, and rental duration in days.
* Validate the input to ensure that the email address is in a valid format, the driver's license number consists of only alphanumeric characters, and the rental duration is a positive integer.
* Convert the rental duration to an integer for further processing.

### Task 2: Write the Code

### [Identify the input fields](#dpPanel2)

* Email address
* Driver's license number
* Rental duration in days

### [Define validation criteria and prompt for user input](#dpPanel3)

* Email address: Should contain "@" and "." characters.
* Driver's license number: Should consist of only alphanumeric characters (letters and digits).
* Rental duration: Should be a positive integer.

Prompt for user input:

```
email = input("Enter your email address: ")  
license_number = input("Enter your driver's license number: ")  
rental_duration = input("Enter the rental duration in days: ")
```

### [Validate and handle input](#dpPanel4)

1. Call the respective validation functions for each input field.
2. Handle validation exceptions or errors gracefully using a try-except block.
3. Provide meaningful feedback to the user when validation fails, indicating the specific issue.
4. If validation passes, proceed with further processing or storage of the validated data.

### Task 3: Test and Refine

1. Run your program and test various input scenarios, including valid and invalid inputs.
2. Verify that the validation functions correctly identify and handle invalid inputs.
3. Refine your validation criteria and error messages if needed to provide a better user experience.

### Task 4: Document and Maintain

* **Version Control**: Use version control to track changes; allowing for easy updates, collaborative editing, and the ability to revert to previous versions if necessary.
* **Regular Updates and Reviews**: Schedule regular reviews and updates for code ensure content remains relevant, accurate, and aligned with the latest Python developments and industry practices,
* **Documentation and Examples Repository**: Maintain a centralized repository containing all lab documents, example code, and solutions.

### Tools

* [VS Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code"), a Python IDE

### Solution

### [Select for Solution](#dpPanel7)

```
def validate_email(email):  
    if "@" not in email or "." not in email:  
        raise ValueError("Invalid email address.")  
  
def validate_license_number(license_number):  
    if not license_number.isalnum():  
        raise ValueError("Driver's license number should only contain alphanumeric characters.")  
  
def validate_rental_duration(rental_duration):  
    if not rental_duration.isdigit() or int(rental_duration) <= 0:  
        raise ValueError("Rental duration should be a positive integer.")  
email = input("Enter your email address: ")  
license_number = input("Enter your driver's license number: ")  
rental_duration = input("Enter the rental duration in days: ")  
try:  
    validate_email(email)  
    validate_license_number(license_number)  
    validate_rental_duration(rental_duration)  
    rental_duration = int(rental_duration)  
    print("Reservation successful!")  
    # Further processing or storage of validated data  
except ValueError as e:  
    print("Validation error:", str(e))
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239342

Scraped At: 2026-05-14T16:02:03.786975
