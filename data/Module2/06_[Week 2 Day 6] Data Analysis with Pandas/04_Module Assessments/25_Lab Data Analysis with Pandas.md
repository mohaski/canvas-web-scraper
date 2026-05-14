# Lab: Data Analysis with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/625182/preview?) Lab: Data Analysis with Pandas

![Avengers action figures of Captain America, Iron Man, and Ant Man](https://moringa.instructure.com/courses/1406/files/625153/download?)
In this lab, you will make use of everything we have learned about pandas: data cleaning, reshaping, and joining. In order to complete this lab, you’ll have to import, clean, combine, reshape, and visualize data to answer questions provided, as well as your own questions.

In particular, you will go through the process of:

* Opening and inspecting the contents of CSVs using pandas dataframes
* Identifying and handling missing values
* Identifying and handling invalid values
* Cleaning text data by removing whitespace and fixing typos
* Joining multiple dataframes
* Aggregating data by groups
* Creating visualizations
* Using visualizations and summary statistics to answer business questions.

### Data Understanding

You will be working with a version of the comprehensive Superheroes Dataset, which can be found on Kaggle and was originally scraped from SuperHeroDb. We have modified the structure and contents of the dataset somewhat for the purposes of this lab.

The data is contained in two separate CSV files:

1. heroes\_information.csv: Each record represents a superhero, with attributes of that superhero (e.g., eye  
   color). Height is measured in centimeters, and weight is measured in pounds.
2. super\_hero\_powers.csv: Each record represents a superpower, then has True/False values representing  
   whether each superhero has that power.

### Business Understanding

The business questions you have been provided are:

1. What is the distribution of superheroes by publisher?
2. What is the relationship between height and number of superpowers? And does this differ based on gender?
3. What are the five (5) most common superpowers in Marvel Comics vs. DC Comics?

This lab also simulates something you are likely to encounter at some point or another in your career in data science: someone has given you access to a dataset, as well as a few questions, and has told you to find something interesting.

### Tools and Resources

* [GitHub repository


  Links to an external site.](https://github.com/flatiron-school/DS_Course0_Week1_Module5_DataPy/tree/main)
* Jupyter Notebook
* CodeGrade (for assignment submission)

### Instructions

* [Step 1](#dpPanel0Content)
* [Step 2](#dpPanel1Content)
* [Step 3](#dpPanel2Content)
* [Step 4](#dpPanel3Content)
* [Step 5](#dpPanel4Content)

### Step 1

* Load the Data with Pandas.
* Create a dataframes `heroes\_df` and `powers\_df` that represent the two CSV files. Use pandas methods to inspect the shape and other attributes of these dataframes.

### Step 2

* Perform Data Cleaning Required to Answer First Question.
* The first question is: \*What is the distribution of superheroes by publisher?\*
* To answer this question, you will need to:
  + Identify and handle missing values
  + Identify and handle text data requiring cleaning

### Step 3

* Perform Data Aggregation and Cleaning Required to Answer Second Question.
* The second question is: \*What is the relationship between height and number of superpowers? And does this differ based on gender?\*
* To answer this question, you will need to:
  + Join the dataframes together
  + Identify and handle invalid values

### Step 4

* Perform Data Aggregation Required to Answer Third Question.
* The third question is: \*What are the 5 most common superpowers in Marvel Comics vs. DC Comics?\*
* This should not require any additional data cleaning or joining of tables, but it will require some additional aggregation.

### Step 5

* Formulate and Answer Your Own Question.
* This part is fairly open-ended. Think of a question that can be answered with the available data, and perform any cleaning or aggregation required to answer that question.

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

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243611

Scraped At: 2026-05-14T20:58:50.100908
