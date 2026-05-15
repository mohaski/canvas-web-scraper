# Lab: Predicting Housing Prices for Real Estate Investment

## ![](https://moringa.instructure.com/courses/1426/files/631874/preview?) Lab: Predicting Housing Prices for Real Estate Investment

For this lab, you are a junior data analyst working for a real estate investment firm. Your team specializes in evaluating housing markets to identify profitable investment opportunities. One of your tasks is to analyze historical housing data and build a simple predictive model to estimate median house values based on median income levels in different areas of California.

Since your company operates in a fast-paced industry, accurate and efficient predictive modeling is essential. Senior analysts need quick estimates of housing prices to inform investment decisions, and your role is to provide reliable insights using data science techniques.

### Problem-Solving Process

To tackle this challenge, you will:

1. **Load and Prepare the Data**
   * Work with a preprocessed version of the California Housing dataset.
   * Select relevant features for modeling.
2. **Build a Simple Predictive Model**
   * Use a linear regression model to understand the relationship between median income (MedInc) and median house value (MedianHouseValue).
3. **Evaluate Model Parameters and Predictions**
   * Extract key components such as the model’s intercept and slope.
   * Predict housing prices based on income levels.
4. **Assess Model Accuracy**
   * Calculate the correlation coefficient to measure how well the model captures the relationship between the chosen variables.

By following this process, you will develop a fundamental understanding of predictive modeling in real estate, which is a skill that is highly valuable in industries such as finance, property management, and urban planning.

### Tools and Resources

* [cal\_housing.tgz


  Links to an external site.](https://drive.google.com/file/d/1BSYSJEImhACVbJ8MNWh268BUJzQtiVKT/view?usp=drive_link)
* [Lab Jupyter Notebook


  Links to an external site.](https://drive.google.com/file/d/10kPFOSt1BYrgcMcw5OWmGDZXta7k3xoJ/view?usp=drive_link)

### Instructions

Load the appropriate libraries and bring in the data. Note that we have to [run a script to get the California Housing dataset


Links to an external site.](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) to match as it is in scikit-learn. We cannot pull it directly from scikit-learn since CodeGrade cannot access the internet.

#### Step 1

* Create a copy of the data and call it df.
* Select the X variable to be MedInc and the y to be MedianHouseValue.
* Return X.shape, y.shape to verify.

#### Step 2

* Find y\_pred by using the model to predict y given the argument of X.
* Return y\_pred.shape to verify.

#### Step 3

* Extract the intercept and slope of the model.
* Return intercept, slope to verify.

#### Step 4

* Calculate the correlation coefficient using pearsonr and call this r.
* Return only r, not the array, and round to two decimal places.

### Submission and Grading Criteria

* + Review the rubric below as a guide for how this lab is graded.
  + Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
  + When you are ready to submit, launch CodeGrade.
    - Click on + Create Submission. Upload your Jupyter notebook file for this lab.
    - For additional information on submitting assignments in CodeGrade: [Getting Started in Canvas.


      Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
  + You can review your submission in CodeGrade and see your score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248809

Scraped At: 2026-05-15T10:27:21.829749
