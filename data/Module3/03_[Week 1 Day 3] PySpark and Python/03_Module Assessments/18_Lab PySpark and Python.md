# Lab: PySpark and Python

## ![](https://moringa.instructure.com/courses/1426/files/631398/preview?) Lab: PySpark and Python

In this lab, you’ll work with the Breast Cancer Wisconsin Diagnostic dataset, which contains information from clinical features that may indicate whether a tumor is malignant or benign. This scenario is ideal for beginners, as it covers foundational data exploration skills and introduces how to interpret medical datasets.

In this lab, you’ll learn to:

* **Explore the Data Structure:** Display records, understand the types of data, and visualize key features.
* **Visualize Data Distributions:** Create basic plots to explore data distribution and relationships between features.
* **Analyze Target Classes:** Review the target variable to understand class balance and explore patterns.

These tasks will give you a hands-on understanding of working with diagnostic data, an essential first step in any data science workflow. Explore our step-by-step problem-solving process for further guidance.

In this lab, you will demonstrate you ability to handle medical datasets, perform data exploration, and use visualizations to draw insights from healthcare data.

### Tools and Resources

* [breast\_cancer.csv


  Links to an external site.](https://drive.google.com/file/d/1X5nPyIY2VKDsRLev1QezSGRT96-aO8Dd/view?usp=sharing)
* [Module Lab Jupyter Notebook


  Links to an external site.](https://drive.google.com/file/d/1b4ZrPYz2or3lvw2hHhAOb3VEN-CT-SmF/view?usp=sharing)
  + **Note that this notebook has the steps that are needed for CodeGrade, where the directions below emphasize the process that you will be going through as you complete this lab.**

### Instructions

#### [Part 1: Initial Data Exploration](#dpPanel0)

1. **Import and Load Data**

* Import necessary libraries and read in the dataset as a DataFrame.

```
from pyspark.sql import SparkSession  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
  
# Create a spark session  
  
# Verify the spark session- named "Breast Cancer Analysis"- is running  
  
# Load the breast cancer data using spark.read.csv
```

1. **Display Records and Data Types**

* Display the first 5 records using .head().
* Use .info() to understand column types and check for missing values.

```
# Display records and data types  
df.head()  
df.info()
```

#### [Part 2: Basic Data Analysis](#dpPanel1)

1. Examine Unique Values in Diagnosis

* Use .value\_counts() to see how many cases are benign versus malignant.

```
# Check unique values in diagnosis  
df['diagnosis'].value_counts()
```

1. Calculate Summary Statistics

* Use .describe() to see statistics for each feature, which will help you understand the ranges and distributions of the data.

```
# Summary statistics  
df.describe()
```

#### [Part 3: Data Visualization](#dpPanel2)

1. Visualize Feature Distributions

* Create histograms for features like radius\_mean and texture\_mean to understand how they are distributed across the dataset.

```
import matplotlib.pyplot as plt  
  
# Plot feature distributions  
df['radius_mean'].hist(bins=20)  
plt.title("Distribution of Radius Mean")  
plt.xlabel("Radius Mean")  
plt.ylabel("Frequency")  
plt.show()
```

1. Plot Diagnosis Class Balance

* Create a bar plot to show the distribution of benign and malignant cases, helping you see if the dataset is balanced.

```
# Plot diagnosis class balance  
df['diagnosis'].value_counts().plot(kind='bar')  
plt.title("Diagnosis Class Balance")  
plt.xlabel("Diagnosis")  
plt.ylabel("Frequency")  
plt.show()
```

#### [Panel 4: Exploring Feature Relationships](#dpPanel3)

1. Visualize Relationship Between Radius and Texture

* Use a scatter plot to explore how radius\_mean and texture\_mean vary between benign and malignant cases.

```
# Scatter plot of radius_mean and texture_mean by diagnosis  
benign = df[df['diagnosis'] == 'B']  
malignant = df[df['diagnosis'] == 'M']  
plt.scatter(benign['radius_mean'], benign['texture_mean'], label="Benign", alpha=0.5)  
plt.scatter(malignant['radius_mean'], malignant['texture_mean'], label="Malignant", alpha=0.5)  
plt.xlabel("Radius Mean")  
plt.ylabel("Texture Mean")  
plt.legend()  
plt.title("Radius vs Texture by Diagnosis")  
plt.show()
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

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248298

Scraped At: 2026-05-15T09:55:25.033302
