# Lab: General Linear Regression and Statistical Inference

## ![](https://moringa.instructure.com/courses/1426/files/631874/preview?) Lab: General Linear Regression and Statistical Inference

You are a junior data scientist working for a real estate investment firm that wants to build a **predictive model** for California housing prices. Your team needs to understand which factors, such as median income, average number of rooms, and average occupancy, most strongly influence **Median House Value**.

Additionally, your manager is interested in whether adding non-linear terms (such as squared income) can improve the model’s accuracy. This analysis will help the company make data-driven investment decisions by identifying key predictors of home prices and refining pricing strategies for different market segments.

In real estate, multiple factors interact to determine property prices. A simple linear model may not always capture complex relationships, so testing for statistical significance and exploring non-linear effects is crucial. This lab will help you:

* Identify which factors significantly impact house prices.
* Assess the uncertainty of these estimates using confidence intervals.
* Compare the effectiveness of a linear vs. quadratic model using adjusted ²R².

By completing this lab, you will gain experience in **multivariate regression modeling, statistical inference, and model evaluation**, skills that are essential in predictive analytics for business decision-making.

### Tools and Resources

* [cal\_housing.tgz


  Links to an external site.](https://drive.google.com/file/d/1HTLRV1SWSGvtU8Jbd0p9dYH6Mx_SIuiq/view?usp=drive_link)

### Instructions

**Load the appropriate libraries and bring in the data.**

**Note:** Because CodeGrade is not accessing the Internet, the dataset cannot be pulled directly from scikit-learn. To match what is in scikit-learn, we must [run a script to get the California Housing dataset


Links to an external site.](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html).

#### Step 1

* Let X be the variables MedInc, AveRooms, and AveOccup, and add the constant for the intercept.
* Let y be MedianHouseValue.
* Fit the regression model, calling it **mlr\_model**.
* **Return the R2 value** of the model rounded to four decimal places.

#### Step 2

* Let **p\_values** be the model's p-values.
* **Return the four p-values** using .iloc[] from the first value to the fourth, in order, separated by commas. Round each to 5 decimal places.

#### Step 3

* Identify the significant predictors (strictly less than α=0.05\alpha=0.05), calling this **significant\_predictors**.
* **Return** the shape of significant\_predictors.

#### Step 4

* **Find the confidence intervals** of the model (at a 95% level of confidence), calling this conf\_intervals.
* Using .iloc[,] and rounding to 2 decimal places, **return the four confidence intervals** in the following order:  
  + First row and first column
  + First row and second column
  + Second row and first column
  + Second row and second column

#### Step 5

* **Add a quadratic term** to the model, calling the new model **quad\_model**, where a new term MedInc\_squared (the square of MedInc) is added to the data.
* **Return the R2 value** of the quadratic model rounded to four decimal places.

#### Step 6

* **Find the adjusted R2 for both models** and call them adjusted\_r2\_base and adjusted\_r2\_quad, respectively.
* **Return these two adjusted R2 values** rounded to four decimal places, separated by a comma.

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

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248882

Scraped At: 2026-05-15T10:35:49.404368
