# Lab: Algorithms

## ![](https://moringa.instructure.com/courses/1391/files/620338/preview?) Lab: Algorithms

Now that you have had some practice with Python, let's pull everything together. Imagine you are a junior developer working for a financial technology company. Your team is tasked with developing a new feature for the company’s mobile banking app that enables users to set and track their savings goals.

Your specific responsibility is to develop the functionality for the savings goal tracking system. This system should be able to set new savings goals based on specific users and set dates to achieve said goals, as well as update the savings progress towards the goals. It should also include a user notification when a goal date is approaching and the savings has not been met.

In this lab, you will be writing pseudocode and defining basic programming commands needed to solve the problem. These tasks will help you structure your approach to solving this problem and improve your understanding of Python programming.

### Instructions

**Problem-Solving Process**

Let's break down this problem using the SDLC methodology and create pseudocode for the order tracking system.

**Step 1: Requirements Gathering and Analysis**

* Identify the main functionalities of the system.
  + Savings Goal
  + Savings Progress
  + Savings Goal Status
  + Savings Goal Notification
* Define the variables within the functionalities. This is information needed to make the functions work properly, this can be user input or complied from user input.
  + User ID
  + Target Amount
  + Target Date
  + Savings Goal
  + Amount Saved
* Define input and output requirements for each functionality of the system. Use the following verbs to describe the actions within the main functionalities.
  + Create
  + Store
  + Return
  + Update
  + Retrieve
  + Compose
  + Send

**Step 2: Design**

* Write the pseudocode for the system. Use the previously listed identifiers and process to develop an algorithm in pseudocode for the program.

### Submission and Grading Criteria

1. For this assignment, you will submit the following:

* + Pseudocode
  + Explanation of your thought process

1. Use the rubric below to ensure your submission meets all requirements.
2. When you're satisfied with your solution, submit all required pieces using one of the following methods:

* + Python text file and image
  + Media recording
  + Slide Deck
  + File Upload

### Solution

Once you have completed your assignment, review the solution below to check your work.

### [Select for Solution](#dpPanel0)

```
Function setSavingsGoal(userId, targetAmount, targetDate):  
    Create a new savings goal record with the provided userId, targetAmount, and targetDate  
    Store the savings goal record in the database  
    Return the unique identifier for the newly created savings goal  
  
Function updateSavingsProgress(userId, savingsGoalId, amountSaved):  
    Retrieve the savings goal record from the database using the savingsGoalId  
    Update the total amount saved by adding the amountSaved  
    Calculate the progress percentage based on the total amount saved and the target amount  
    Store the updated savings goal record in the database  
  
Function getSavingsGoalStatus(userId, savingsGoalId):  
    Retrieve the savings goal record from the database using the savingsGoalId  
    Return the current progress status of the savings goal  
  
Function sendSavingsGoalNotification(userId, savingsGoalId):  
    Retrieve the savings goal record from the database using the savingsGoalId  
    If the target date is approaching and the goal is not yet achieved:  
        Compose a notification message to remind the user about their savings goal  
        Send the notification to the user via push notification or email
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239137

Scraped At: 2026-05-14T00:26:46.859720
