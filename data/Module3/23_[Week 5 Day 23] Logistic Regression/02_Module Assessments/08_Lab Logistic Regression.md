# Lab: Logistic Regression

## ![](https://moringa.instructure.com/courses/1426/files/631874/preview?) Lab: Logistic Regression

### Scenario:

You are a junior data scientist working for a real estate investment firm that wants to classify neighborhoods into high-value and low-value housing markets. To help real estate developers and investors make strategic decisions, your team is building a logistic regression model to predict whether a house’s value is above or below the median.

By analyzing features such as Median Income (MedInc), Average Rooms (AveRooms), and Average Occupancy (AveOccup), the company aims to identify key indicators of high-value neighborhoods. **The goal is to create a model that can accurately classify homes and help stakeholders prioritize investment opportunities.**

In real-world real estate analytics, classification models play a crucial role in risk assessment, property valuation, and investment planning.

This lab will help you:

* Convert a continuous target into a binary classification problem, simulating real-world decision-making.
* Scale and preprocess data for better model performance.
* Fit and evaluate a logistic regression model, interpreting coefficients and predictions.
* Assess model performance using a confusion matrix and accuracy score.
* Analyze Variance Inflation Factors (VIFs) to check for multicollinearity in the predictor variables.

By completing this lab, you will gain practical experience in classification modeling, feature scaling, and multicollinearity analysis, which are essential skills in data-driven business applications.

### Tools and Resources

* [cal\_housing.tgz


  Links to an external site.](https://drive.google.com/file/d/1lZGb7yDgrx0OfzHfKQZz5TNgYHX9Uric/view?usp=drive_link)

### Instructions

Load the appropriate libraries and bring in the data. Note that we have to [run a script to get the California Housing dataset


Links to an external site.](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) to match as it is in scikit-learn. We cannot pull it directly from scikit-learn since CodeGrade cannot access the internet.

* [Step 1](#dpPanel0Content)
* [Step 2](#dpPanel1Content)
* [Step 3](#dpPanel2Content)
* [Step 4](#dpPanel3Content)
* [Step 5](#dpPanel4Content)
* [Step 6](#dpPanel5Content)
* [Step 7](#dpPanel6Content)
* [Step 8](#dpPanel7Content)
* [Step 9](#dpPanel8Content)

#### Step 1

* **Define threshold** as the median of MedianHouseValue.
* Create a **binary target value** called HighValue using the following code:  

  ```
  data['HighValue'] = (data['MedianHouseValue'] > threshold).astype(int)
  ```
* **Return an array** of the unique values in HighValue.

#### Step 2

* **Select MedInc, AveRoom, and AveOccup** as the variables for X, and let y be the variable HighValue.
* **Set seed** to 42.
* **Split the data** into X\_train, X\_test, y\_train, and y\_test, with a test size of 30% and a random state of 42.
* **Return the shapes** of these four arrays in the order: X\_train, X\_test, y\_train, y\_test.

#### Step 3

* **Use StandardScaler()** to scale the data:
* **Fit and transform X\_train**, calling it X\_train\_scaled.
* **Transform X\_test**, calling it X\_test\_scaled.
* Return the **shape of X\_test\_scaled**.

#### Step 4

* Return the model's intercept.

#### Step 5

* Return the model's coefficients.

#### Step 6

* **Using the model**:
  + Predict the probabilities of X\_test\_scaled, calling it y\_pred\_prob.
  + Predict the classes of X\_test\_scaled, calling it y\_pred\_class.
  + Return the first five elements of both arrays: y\_pred\_prob and y\_pred\_class.

#### Step 7

* Provide the confusion matrix of y\_test and y\_pred\_class.

#### Step 8

* Round to four decimal places and provide the accuracy score of y\_test and y\_pred\_class.

#### Step 9

* Round to three decimal places and provide the Variance Inflation Factors (VIFs) for each of the three columns of X\_train\_scaled.

### Submission and Grading Criteria

1. 1. Review the rubric below as a guide for how this lab is graded.
   2. Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
   3. When you are ready to submit, launch CodeGrade.
      * Click on + Create Submission. Upload your Jupyter notebook file for this lab.
      * For additional information on submitting assignments in CodeGrade: [Getting Started in Canvas.


        Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
      * You can review your submission in CodeGrade and see your score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248911

Scraped At: 2026-05-15T10:39:29.166710
