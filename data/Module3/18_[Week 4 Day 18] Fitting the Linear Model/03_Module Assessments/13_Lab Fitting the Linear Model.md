# Lab: Fitting the Linear Model

## ![](https://moringa.instructure.com/courses/1426/files/631874/preview?) Lab: Fitting the Linear Model

### Scenario: Analyzing Housing Prices for Market Predictions

In the real estate industry, understanding the factors that influence housing prices is essential for accurate market predictions and investment decisions. Junior data scientists working in real estate analytics firms or financial institutions often need to build predictive models to estimate housing prices based on economic and demographic factors. One key variable that significantly impacts home values is median income: households with higher incomes are more likely to afford higher-priced homes.

In this lab, you will step into the role of a data scientist at a real estate investment firm. Your team is analyzing housing prices in California to help investors make data-driven decisions. **The goal is to develop a simple linear regression model to determine how median household income affects median house value in different regions**. By identifying influential data points and examining model residuals, you will assess the reliability of your predictions and refine your approach.

Your company’s analysts have noticed inconsistencies in previous housing price predictions, potentially due to outlier effects. If these influential points are not identified and managed properly, they could skew investment decisions, leading to financial losses. Your task is to investigate whether certain neighborhoods or price anomalies are distorting the model’s accuracy and provide a data-driven recommendation for improving prediction reliability.

By the end of this lab, you will gain hands-on experience in regression modeling, residual analysis, and outlier detection, which are all valuable skills that apply across multiple industries, including finance, healthcare, and fraud detection.

### Problem-Solving Process

To tackle this problem, you will follow a structured approach:

* **Load and Prepare the Data:** You will bring in the California Housing dataset and select key variables for analysis.
* **Fit a Linear Model:** Using the statsmodels library, you will create a simple regression model to quantify the relationship between median income and housing prices.
* **Analyze Residuals:** Residuals (the difference between predicted and actual values) help assess model accuracy. You will investigate whether your model systematically underestimates or overestimates housing prices.
* **Detect Influential Data Points:** Not all data points contribute equally to model accuracy. Some outliers or high-leverage points may disproportionately affect predictions. You will compute Cook’s distance to detect these influential points.

### Tools and Resources

* [cal\_housing.tgz


  Links to an external site.](https://drive.google.com/file/d/1WBjIijTMLob1sL9Ed2yPSJHnMwWG6k71/view?usp=drive_link)
* [Lab Jupyter Notebook


  Links to an external site.](https://drive.google.com/file/d/11DVBeAb5g3jMI80_2d9CxTYIyw-eXPVN/view?usp=drive_link)

### Instructions

Load the appropriate libraries and bring in the data. Note that we have to [run a script to get the California Housing dataset


Links to an external site.](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) to match as it is in scikit-learn. We cannot pull it directly from scikit-learn since CodeGrade cannot access the internet.

#### Step 1

* Create a copy of the data and call it df.
* Select the X variable to be MedInc and the y to be MedianHouseValue.
* Return X.shape, y.shape to verify.

#### Step 2

Using statsmodels:

* Add the constant term and call it X\_const.
* Fit the OLS model and call it model.
* Extract the residuals and call them residuals.
* Count the number of positive and negative residuals, calling them positive\_residuals and negative\_residuals, respectively.
* Return positive\_residuals, negative\_residuals to verify.

#### Step 3

* Compute Cook's distance, where the model's get\_influence is called influence and the Cook's distance from this is called cooks\_d.
* Identify the influential points, calling them influential\_points.
* Verify this by returning influential\_points.shape.

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

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248828

Scraped At: 2026-05-15T10:29:20.787383
