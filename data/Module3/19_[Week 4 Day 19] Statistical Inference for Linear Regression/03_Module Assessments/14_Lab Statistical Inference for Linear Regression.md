# Lab: Statistical Inference for Linear Regression

## ![](https://moringa.instructure.com/courses/1426/files/631874/preview?) Lab: Statistical Inference for Linear Regression

Imagine you are a junior data scientist working for a real estate analytics firm. Your team is tasked with understanding how median income levels in different neighborhoods impact housing prices. The company is developing a pricing model to help real estate investors make data-driven decisions. As a first step, your manager asks you to analyze the relationship between Median Income (MedInc) and Median House Value (MedianHouseValue) using a simple linear regression model.

Understanding the relationship between income levels and housing prices is crucial in various industries, including real estate investment, urban planning, and mortgage risk assessment.

By completing this lab, you will gain hands-on experience in applying regression analysis to a real-world problem, strengthening your ability to build predictive models for business decision-making.

### Tools and Resources

* [cal\_housing.tgz


  Links to an external site.](https://drive.google.com/file/d/1zyUXnvyA51Yetu_HxV0sAvxPyozwPA3S/view?usp=drive_link)
* [Lab Jupyter Notebook


  Links to an external site.](https://drive.google.com/file/d/1aPLfeYgQxwZ6SSc_0URbfxsTHBprTeCY/view?usp=drive_link)

### Instructions

To prepare for this lab, start by loading the appropriate libraries and bringing in the data.

**Note:** we have to [run a script to get the California Housing dataset


Links to an external site.](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) to match as it is in scikit-learn. We cannot pull it directly from scikit-learn since CodeGrade cannot access the internet.

#### Step 1

* Create a copy of the data and call it df.
* Select the X variable to be MedInc and the y to be MedianHouseValue.
* Add the constant term and call it X\_const.
* Verify this by returning the shape of X\_const.

#### Step 2

* Fit the OLS model and call it model.
* Return the rounded model R2R^2 value to four decimal places.

#### Step 3

* Extract the slope and the related statistics for MedInc, calling them, respectively, slope, std\_error, t\_statistic, and p\_value.
* Return the following (do not round) to verify: slope, std\_error, t\_statistic, p\_value.

#### Step 4

* Calculate the confidence interval of MedInc at a 95% level of confidence and call this conf\_int.
* Return the confidence interval rounded to four decimal places.

#### Step 5

* Find the model predictions, calling them y\_pred.
* Return y\_pred.shape to verify.

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

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248846

Scraped At: 2026-05-15T10:31:36.876427
