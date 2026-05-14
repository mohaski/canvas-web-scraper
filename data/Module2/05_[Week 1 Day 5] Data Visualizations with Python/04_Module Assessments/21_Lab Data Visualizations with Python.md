# Lab: Data Visualizations with Python

## ![](https://moringa.instructure.com/courses/1406/files/625182/preview?) Lab: Data Visualizations with Python

In this lab you will apply your knowledge of Python and Matplotlib to create data visualizations. You will take on the role of a data analyst for a video store, and develop visualizations that communicate insights to the team.

You will be able to:

* Create a bar plot using Matplotlib
* Create a scatter plot using Matplotlib
* Create a histogram using Matplotlib
* Follow best practices when creating visual labels

### Tools and Resources

* [GitHub repository


  Links to an external site.](https://github.com/learn-co-curriculum/DS_Course1_Week1_Module4_VizLab)
* Jupyter Notebook
* CodeGrade (for assignment submission)

### Instructions

Run this cell first without changing the code cell:

```
# Run this cell without changes  
import numpy as np  
import matplotlib.pyplot as plt  
%matplotlib inline
```

### [Exercise 1: Create a Bar Chart](#dpPanel0)

Jim's Video Library contains 40 crime, 30 science fiction, 10 drama, 50 comedy, 25 action and 5 documentary movies. The goal is to make the bar chart you see below:

![Jimmy&#39;s video library bar chart showing number of movies and genres](https://moringa.instructure.com/courses/1406/files/625109/download?)

Using ax.bar() recreate the bar chart by following these steps:

1. “Hard-code” the numbers listed above into Python (there is no data file).
2. X and height must be iterables of numbers, so x should just be 6 evenly-spaced numbers.
3. To set the labels of “crime” etc. pass the labels into the .bar() function using the tick\_label argument.

```
# Replace None with appropriate code  
height = None  
x = None  
labels = None  
  
# Create the plot  
fig, ax = plt.subplots(figsize=(8, 6))  
  
# Plot vertical bars of fixed width by passing x and height values to .bar() function   
None  
  
# Give a title to the bar graph and label the axes  
None  
None  
None
```

### [Exercise 2: Create a Scatter Plot](#dpPanel1)

You are a data scientist working for a major car manufacturer. The company is aiming to improve the fuel efficiency of their car models. To analyze the relationship between car weight and miles per gallon (MPG), use the data provided to create the scatter plot in the image below.

![Scatter plot of consumer car weight versus miles per gallon](https://moringa.instructure.com/courses/1406/files/625202/download?)

Using ax.scatter()recreate the scatter plot by following these steps:

1. Set appropriate labels for axes.
2. Give a title to the plot.
3. Create a legend.

```
# Replace None with appropriate code  
  
weight = [2750, 3125, 2100, 4082, 2690, 3640, 4380, 2241, 2895, 3659]  
mpg = [29, 23, 33, 28, 20, 21, 14, 25, 31, 17]  
  
# Create the plot  
None  
  
# Plot with scatter()  
None  
  
# Set x and y axes labels, legend, and title  
None  
None  
None  
None
```

### [Exercise 3: Create a Histogram](#dpPanel2)

Joe is the branch manager at a bank. Recently, Joe has been receiving customer feedback saying that the waiting times for clients to be served by customer service representatives are too long. Joe decides to observe and write down the time spent waiting by each customer. Here are his findings from observing and writing down the wait times (in seconds), spent by 20 customers:

43.1, 35.6, 37.5, 36.5, 45.3, 43.4, 40.3, 50.2, 47.3, 31.2, 42.2, 45.5, 30.3, 31.4, 35.6, 45.2, 54.1, 45.6, 36.5, 43.1

Create a histogram of Joe’s data that looks like the image below:

![Histogram of customer waiting times ](https://moringa.instructure.com/courses/1406/files/625101/download?)

Using ax.hist()recreate the histogram by following these steps:

1. Pass in x and use bins=5 .
2. Plot, label and give the same title in image above.

```
# Replace None with appropriate code  
  
x = [43.1, 35.6, 37.5, 36.5, 45.3, 43.4,   
     40.3, 50.2, 47.3, 31.2, 42.2, 45.5,   
     30.3, 31.4, 35.6, 45.2, 54.1, 45.6,   
     36.5, 43.1]  
  
# Create the plot  
None  
  
# Plot the histogram with hist() function  
None  
  
# Label axes and set title  
None  
None  
None
```

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

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243576

Scraped At: 2026-05-14T20:55:08.141933
