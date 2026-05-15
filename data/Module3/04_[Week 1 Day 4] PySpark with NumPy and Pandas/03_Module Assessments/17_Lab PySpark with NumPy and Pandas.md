# Lab: PySpark with NumPy and Pandas

## ![](https://moringa.instructure.com/courses/1426/files/631398/preview?) Lab: PySpark with NumPy and Pandas

You are a data scientist at a healthcare startup. Your team is developing tools to improve breast cancer diagnosis. Accurate data analysis can help doctors make better decisions, just like gathering the right instruments ensures a successful procedure.

In this lab, you will work with PySpark, NumPy, and Pandas to analyze patient data efficiently. You will load data, compute key metrics, and visualize results, gaining critical skills for handling large-scale healthcare datasets. By the end, you will have explored key healthcare metrics, computed statistical relationships, and visualized data distributions, all while ensuring the Spark session's reliability and operational readiness.

### Tools and Resources

* [breast\_cancer.csv


  Links to an external site.](https://drive.google.com/file/d/1dPkqTtwjqE-7q1wNr-WTLF3ZQgFpf7MO/view?usp=drive_link)
* [PySpark with NumPy and Pandas notebook file


  Links to an external site.](https://drive.google.com/file/d/12w589YT5mKQ_dKEFyCbEsl7Iui4zCwiR/view?usp=drive_link)

### Instructions

* [Step 0: Import Libraries](#dpPanel0Content)
* [Step 1: Set Up Your PySpark Environment](#dpPanel1Content)
* [Step 2: Load and Explore the Dataset](#dpPanel2Content)
* [Step 3: Count Diagnoses](#dpPanel3Content)
* [Step 4: SQL Query for Diagnosis Counts](#dpPanel4Content)
* [Step 5: Visualize Diagnosis Distribution](#dpPanel5Content)
* [Step 6: Summary Statistics](#dpPanel6Content)
* [Step 7: Average Feature Values for Benign Cases](#dpPanel7Content)
* [Step 8: Radius-to-Perimeter Ratio for Malignant Cases](#dpPanel8Content)
* [Step 9: Sum of Standard Deviations](#dpPanel9Content)
* [Step 10: Close the Spark Session](#dpPanel10Content)

#### Step 0: Import Libraries

Import the necessary libraries to set up the Spark session.

#### Step 1: Set Up Your PySpark Environment

* Create a Spark session named "Breast Cancer Analysis"
* Verify the Spark session is running. The response should be "yes."

#### Step 2: Load and Explore the Dataset

* Load the dataset into a PySpark DataFrame.
* Display the first 5 rows.
* Show the data types of each column.
* Find the perimeter\_mean from the 77th row and assign it to a variable called perimeter\_mean\_value.

#### Step 3: Count Diagnoses

* Count the number of benign (B) and malignant (M) diagnoses.
* Calculate the difference (B - M).

#### Step 4: SQL Query for Diagnosis Counts

* Register the DataFrame as an SQL table using `df.createOrReplaceTempView()` to enable SQL-based computation.
* Write and execute a SQL query to get the counts of benign and malignant diagnoses.

#### Step 5: Visualize Diagnosis Distribution

* Using your SQL query from the previous step, create a new DataFrame called `diagnosis_counts`.
* Create a bar plot showing the distribution of benign and malignant cases.

#### Step 6: Summary Statistics

Use the `.describe()` function to examine statistics for each feature:

* The maximum of `compactness_mean`.
* The minimum of `smoothness_mean`.
* Calculate the difference between `max_compactness_mean` and `min_smoothness_mean`.

#### Step 7: Average Feature Values for Benign Cases

* Using an SQL query, calculate the average of `radius_mean`, `texture_mean`, and `perimeter_mean` for benign cases.
* Round to two decimal places.
* Return the product of these three rounded means.

#### Step 8: Radius-to-Perimeter Ratio for Malignant Cases

* Using an SQL query, calculate the average of the ratio of r`adius_mean` to `perimeter_mean` for malignant cases.
* Round to two decimal places.
* Store the result as `mean_radius_perimeter_ratio`.

#### Step 9: Sum of Standard Deviations

* Using an SQL query, compute the standard deviations of `symmetry_mean` and `fractal_dimension_mean`.
* Sum these two values and store the result as `sum_of_stddevs`.

#### Step 10: Close the Spark Session

* Close the Spark session.
* Ensure verification outputs "yes."

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

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248343

Scraped At: 2026-05-15T09:58:21.429738
