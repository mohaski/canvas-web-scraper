# Practice: Algorithms

# Practice: Algorithms

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Algorithms

Icon Progress Bar (browser only)

5 min read

Let's consider a real-world scenario and break it down using the SDLC approach and pseudocode without actual coding. You will walk through the first two SDLC phases, focusing on requirements gathering, analysis, and design by creating pseudocode.

**The Scenario:** A library management system needs to automate the process of borrowing and returning books. The system should allow librarians to manage the library's inventory, search for books, track borrowed books, and generate reports on borrowed and overdue books.

By following the SDLC approach and using pseudocode, you can effectively break down the development of a library management system into smaller, manageable steps. The pseudocode provides a high-level overview of the main functionalities without delving into the actual coding details. This allows for better planning, communication, and understanding of the system's requirements before proceeding with the implementation phase.

### Instructions

Use the following steps to guide you through the first two phases of the SDLC process.

### Task 1: Requirements Gathering and Analysis

1. Identify the main functionalities of the library management system.

* Think about what needs to be done to accomplish the goals below.
* The system should allow librarians to:
  + manage the library's inventory
  + track borrowed books
  + generate reports

1. Define the input and output requirements for each functionality.
2. Identify any constraints or limitations.

### Task 2: Design

**Action:** Create pseudocode for the main functionalities of the library management system.

1. Add new books and be set as available

* + **Input:** Book id
  + **Output:** Update book status as available

1. Search for books based on criteria

* + **Input:** Search Criteria (genre/author/length….)
  + **Output:** Books ids for matching books

1. Borrow/checkout a book to a person if available

* + **Inputs:**
  + Book id
  + Borrower id
  + **Outputs:**
  + Update book status as borrowed/unavailable
  + Record borrower information
  + Set due date for return

1. Needs a way for books to be returned

* + **Input:** Book id
  + **Outputs:**
  + Update book status as available
  + Remove borrower information

1. Needs to be able to generate reports on what books are currently borrowed or overdue

* + **Inputs:**
  + Report type
  + Date
  + **Output:** Book ids that are overdue (past due date) or still borrowed

### Solution

### Select for Pseudocode Algorithm Solution

#### Full Pseudocode for Library Management

`Function addBook(book):  
    Add book to the inventory database  
    Update the book's status as available  
  
Function searchBook(searchCriteria):  
    Search for books in the inventory based on searchCriteria  
    Return the list of matching books  
  
Function borrowBook(book, borrower):  
    If book is available:  
        Record the borrower information  
        Update the book's status as borrowed  
        Set the due date for return  
    Else:  
        Display a message that the book is not available  
  
Function returnBook(book):  
    Update the book's status as available  
    Remove the borrower information  
  
Function generateReport(reportType, date):  
    If reportType is "borrowed":  
        Generate a report of all currently borrowed books  
    Else if reportType is "overdue":  
 Compare date to return dates for borrowed books  
        Generate a report of overdue books (date > due date)  
    Else:  
        Display an error message for invalid report type`

#### Detailed Solution with Decisions Explained

To guide learners through the process, the solution is detailed, explaining each decision and step.

**Function: addBook(book)**

```
# This function is responsible for adding a new book to the inventory.  
  
# It takes the book object as input.  
  
# The function updates the book's status to available.  
  
Add book to the inventory database  
  
Update the book's status as available
```

**Function: searchBook(searchCriteria)**

```
# This function searches for books based on the provided criteria.  
# It takes searchCriteria as input, which could be genre, author, etc.  
# It returns a list of books that match the criteria.  
Search for books in the inventory based on searchCriteria  
Return the list of matching books
```

**Function: borrowBook(book, borrower)**

```
# This function handles the borrowing process.  
# It takes the book object and the borrower object as inputs.  
# If the book is available, it records the borrower's information, updates the book's status, and sets a due date.  
# If the book is not available, it informs the user that the book cannot be borrowed.  
If book is available:  
    Record the borrower information  
    Update the book's status as borrowed  
    Set the due date for return  
Else:  
    Display a message that the book is not available
```

**Function: returnBook(book)**

```
# This function handles the return process.  
# It takes the book object as input.  
# It updates the book's status to available and removes the borrower's information.  
Update the book's status as available  
Remove the borrower information
```

**Function: generateReport(reportType, date)**

```
# This function generates reports based on the type and date provided.  
# It takes reportType and date as inputs.  
# If the reportType is "borrowed," it generates a report of all currently borrowed books.  
# If the reportType is "overdue," it compares the current date to the due dates of borrowed books and generates a report of overdue books.  
# If an invalid report type is provided, it displays an error message.  
If reportType is "borrowed":  
    Generate a report of all currently borrowed books  
Else if reportType is "overdue":  
    Compare date to return dates for borrowed books  
    Generate a report of overdue books (date > due date)  
Else:  
    Display an error message for invalid report type
```

### Summary

This practice helped you step through the early phases of the SDLC, focusing on gathering requirements, analyzing them, and designing a system using pseudocode. By breaking down a library management system into manageable pieces, you learned how to organize your thoughts and plan out your code before jumping into actual Python programming.

Moving forward, you can use this approach to tackle new projects, ensuring you have a clear plan and understanding before you start coding.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239119

Scraped At: 2026-05-14T15:16:38.480172
