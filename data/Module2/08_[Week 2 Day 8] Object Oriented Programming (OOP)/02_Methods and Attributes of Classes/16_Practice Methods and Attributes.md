# Practice: Methods and Attributes

# Practice: Methods and Attributes

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Methods and Attributes

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

Imagine you are a junior software developer working on a student management system for a university. Your task is to create a Student class that represents students enrolled in the university. The Student class should have attributes such as name, student ID, major, year of study, and a dictionary of enrolled courses. You need to implement methods to display student information, add or remove courses, calculate the student's GPA, and determine the student's academic standing based on their GPA.

**Problem-Solving Process:**

1. 1. **Understand the problem:** Clearly identify the requirements for the Student class, including the necessary attributes and methods.
   2. **Plan the solution:** Break down the problem into smaller steps and determine the appropriate class structure and method implementations.
   3. **Implement the solution:** Write the code for the Student class, including the \_\_init\_\_ method and other required methods.
   4. **Test and debug:** Create instances of the Student class and test the implemented methods to ensure they work as expected. Debug any issues that arise.
   5. **Evaluate and refine:** Review your implementation and consider any potential improvements or optimizations.

**Objective:** By completing this practice exercise, you will gain experience in defining a class, initializing object attributes using the \_\_init\_\_ method, and implementing methods to interact with object instances. You will practice working with lists, performing calculations, and applying conditional logic within methods. This exercise will reinforce your understanding of OOP concepts and their practical application in a student management system.

### Resources

* GitHub repository is not needed for this practice.
* [Python documentation on classes and object-oriented programming


  Links to an external site.](https://docs.python.org/3/tutorial/classes.html)

### Instructions

Remember to implement the methods according to the provided instructions and test your code thoroughly. Feel free to add more attributes or methods to the Student class as needed, such as a method to update the student's major or year of study.

### Step 1

#### Define the Student class

Implement the \_\_init\_\_ method to initialize the attributes of a student: name, student ID, major, year of study, and an empty dictionary of enrolled courses and the students grade: {‘course\_name’:grade}

### Step 2

#### Implement the display\_info() method

* Define a method named display\_info() within the Student class.
* This method should print the student's name, student ID, major, year of study, and the list of enrolled courses.

### Step 3

#### Implement the add\_course() and remove\_course() methods

* Define methods named add\_course() and remove\_course() within the Student class.
* The add\_course() method should take a course name and a grade as a parameter and incorporate it into the dictionary.
* The remove\_course() method should take a course name as a parameter and remove it from the dictionary.

### Step 4

#### Implement the calculate\_gpa() method

* Define a method named calculate\_gpa() within the Student class.
* This method should calculate the student's GPA based on the grades received in their enrolled courses.
* Assume that the grades are stored as a dictionary where the course names are the keys and the grades (on a 4.0 scale) are the values.
* The method should return the calculated GPA.

### Step 5

#### Implement the academic\_standing() method

* Define a method named academic\_standing() within the Student class.This method should determine the student's academic standing based on their GPA.
* Use conditional statements to assign the appropriate standing (e.g., "Good Standing" for GPA >= 3.0, "Academic Probation" for GPA < 2.0).
* The method should return the academic standing.

### Step 6

#### Create instances of the Student class

* Create a few instances of the Student class, initializing them with appropriate attribute values.

### Step 7

#### Test the implemented methods

* Call the display\_info() method on each student instance to display their information.
* Use the add\_course() and remove\_course() methods to modify the enrolled courses for each student.
* Call the calculate\_gpa() method on each student instance and print their GPA. You will need to create grade dictionaries for each student.
* Call the academic\_standing() method on each student instance and print their academic standing.

### Step 8

#### Verify the results

* Check the output to ensure that the student information is displayed correctly, courses are added and removed accurately, GPA is calculated properly, and academic standing is determined based on the GPA.

### Solution

### Select for Solution

```
class Student:  
    def __init__(self, name, student_id, major, year_of_study):  
        self.name = name  
        self.student_id = student_id  
        self.major = major  
        self.year_of_study = year_of_study  
        self.courses = {}  
  
  
    def display_info(self):  
        print("Student Information:")  
        print("Name:", self.name)  
        print("Student ID:", self.student_id)  
        print("Major:", self.major)  
        print("Year of Study:", self.year_of_study)  
        print("Enrolled Courses:", self.courses)  
  
  
    def add_course(self, course, grade):  
        self.courses[course] = grade  
        print(f"Added course: {course}")  
  
  
    def remove_course(self, course):  
        if course in self.courses.keys():  
            del self.courses[course]  
            print(f"Removed course: {course}")  
        else:  
            print(f"Course {course} not found.")  
  
  
    def calculate_gpa(self):  
        total_grade_points = sum(self.courses.values())  
        total_credits = len(self.courses)  
        gpa = total_grade_points / total_credits  
        return round(gpa, 2)  
  
  
    def academic_standing(self, gpa):  
        if gpa >= 3.0:  
            return "Good Standing"  
        elif gpa >= 2.0:  
            return "Satisfactory"  
        else:  
            return "Academic Probation"  
  
# Create instances of the Student class  
student1 = Student("John Doe", "S001", "Computer Science", "Sophomore")  
student2 = Student("Jane Smith", "S002", "Business Administration", "Junior")  
  
# Test the methods  
student1.display_info()  
print()  
  
student1.add_course("Data Structures", 3.5)  
student1.add_course("Algorithms", 3.8)  
student1.display_info()  
print()  
  
student1.remove_course("Algorithms")  
student1.display_info()  
print()  
  
gpa1 = student1.calculate_gpa()  
print(f"GPA for {student1.name}: {gpa1}")  
print(f"Academic Standing for {student1.name}: {student1.academic_standing(gpa1)}")  
print()  
  
student2.display_info()  
print()  
  
student2.add_course("Financial Accounting", 3.2)  
student2.add_course("Marketing", 2.8)  
student2.display_info()  
print()  
  
gpa2 = student2.calculate_gpa()  
print(f"GPA for {student2.name}: {gpa2}")  
print(f"Academic Standing for {student2.name}: {student2.academic_standing(gpa2)}")
```

This solution implements the Student class with the requested attributes and methods. The \_\_init\_\_ method initializes the student's attributes, including an empty dictionary of courses:grades. The display\_info() method prints the student's information, including the enrolled courses.

The add\_course() and remove\_course() methods allow adding and removing courses from the student's list of enrolled courses. The calculate\_gpa() method calculates the student's GPA based on the grades received in their enrolled courses. The academic\_standing() method determines the student's academic standing based on their GPA.

The code also includes examples of creating instances of the Student class and testing the implemented methods. The output demonstrates the functionality of the class and its methods.

Feel free to modify and expand upon this solution based on your specific requirements and additional features you may want to include in the Student class.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243656

Scraped At: 2026-05-14T21:03:24.202902
