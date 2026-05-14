# Lab: Object-Oriented Programming (OOP)

## ![](https://moringa.instructure.com/courses/1406/files/625182/preview?) Lab: Object-Oriented Programming (OOP)

![Public library book aisle](https://moringa.instructure.com/courses/1406/files/625185/download?)
You are a junior software developer working on a library management system. The library has various types of items, such as books, magazines, and DVDs. Your task is to design a class hierarchy using inheritance to represent these different item types. The base class should be called "LibraryItem" and should contain common attributes and methods shared by all library items. You will then create derived classes for each specific item type (e.g., Book, Magazine, DVD) that inherit from the LibraryItem class and add any additional attributes or methods specific to that item type.

**Problem-Solving Process:**

1. **Understand the problem:** Identify the common attributes and behaviors among library items and determine the specific attributes and behaviors for each item type.
2. **Plan the solution:** Design the class hierarchy, deciding which attributes and methods should be placed in the base class and which ones should be in the derived classes.
3. **Implement the solution:** Write the code for the LibraryItem base class and the derived classes (Book, Magazine, DVD) using inheritance.
4. **Test and debug:** Create instances of each item type and test the implemented methods to ensure they work as expected. Debug any issues that arise.
5. **Evaluate and refine:** Review your implementation and consider any potential improvements or additional features that could be added.

By completing this lab, you will gain hands-on experience in applying OOP and inheritance concepts to design and implement a class hierarchy for a library management system. You will practice creating a base class, defining derived classes, and overriding methods to suit the specific needs of each item type. This lab reinforces your understanding of OOP and inheritance and its application in solving real-world problems.

### Tools and Resources

* [GitHub repository


  Links to an external site.](https://github.com/learn-co-curriculum/DS_Course0_Week1_Module7_OOPLab/tree/main)
* Jupyter Notebook
* CodeGrade (for assignment submission)

### Instructions

### [Step 1: Create the LibraryItem Base Class Using Init to Define the Attributes](#dpPanel0)

* Define the LibraryItem base class and implement the init method. It should set the following attributes:
  + title: The title of the library item (string)
  + author: The author of the library item (string)
  + publication\_year: The year the library item was published (integer)
  + is\_available: Indicates if the item is currently available for checkout should default to True (boolean)

### [Step 2: Implement the Methods in the LibraryItem Class](#dpPanel1)

* display\_info: Display the information of the library item
* checkout: Change the is\_available attribute to False when the item is checked out
* return\_item: Change the is\_available attribute to True when the item is returned

### [Step 3: Create the Book Derived Class](#dpPanel2)

* Create the Book derived class.
  + It should inherit from the LibraryItem class.
  + Implement a new init method to initialize the attributes of the Book instance, calling the base class constructor using super() and adapting to include new attributes as well. Add the following attributes specific to books:  
    - isbn: The ISBN number of the book (string)
    - publisher: The publisher of the book (string)
* Override the display\_info method to display the book-specific information along with the inherited attributes.

### [Step 4: Create the Magazine Derived Class](#dpPanel3)

* Define the Magazine class that inherits from the LibraryItem class.
  + Implement a new init method to initialize the attributes of the Magazine instance, calling the base class constructor using super() and adapting to include new attributes as well. Add the following attributes specific to magazines:  
    - issue\_number: The issue number of the magazine (integer)
    - publication\_month: The month of publication of the magazine (integer)
* Override the display\_info method to display the magazine-specific information along with the inherited attributes.

### [Step 5: Create the DVD Derived Class](#dpPanel4)

* Define the DVD class that inherits from the LibraryItem class
  + Implement a new init method to initialize the attributes of the DVD instance, calling the base class constructor using super() and adapting to include new attributes as well. Add the following attributes specific to DVDs:  
    - duration: The duration of the DVD in minutes (integer)
    - director: The director of the DVD (string)
    - genres: A set of genres for the DVD (set)
    - author: Set author default value to "N/A"
* Define a new method specific to the DVD class, add\_genre, that takes in a genre string (I.E. 'comedy') and adds it to the existing set. Don't forget to include self.

### [Step 6: Test the Implemented Classes](#dpPanel5)

* Test your implemented classes by instantiating different objects with the code provided.
  + Call the display\_info method on each instance to verify that the information is displayed correctly.
* Test the checkout and return\_item methods to ensure they update the is\_available attribute as expected.
* Test the add\_genre method for your DVD object to ensure it is adding the genre to your set as expected.

### [Step 7: Evaluate and Refine Your Code](#dpPanel6)

Review your implementation and consider any potential improvements or additional features that could be added to the library management system. Here are just a few potential examples and thoughts. You do not need to implement any of these for this assessment.

* It might make sense in the checkout method to include a check for if the item is currently available or not.
* Data validations and string standardization for specific attributes.
* Implement a database system to store all of our objects so that we can then search.
* How might you handle multiple copies of the same item?

Think about how you could further extend the class hierarchy to include more specific item types (e.g., Audiobook, Journal) or add additional methods for searching or sorting library items.

### Submission and Grading Criteria

1. Review the rubric below as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
3. When you are ready to submit, launch CodeGrade.
   * Click on + Create Submission. Upload your Jupyter notebook file for this lab.
   * For additional information on submitting assignments in CodeGrade: [Getting Started in CanvasLinks to an external site.


     Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
   * You can review your submission in CodeGrade and see your score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243669

Scraped At: 2026-05-14T21:04:30.121754
