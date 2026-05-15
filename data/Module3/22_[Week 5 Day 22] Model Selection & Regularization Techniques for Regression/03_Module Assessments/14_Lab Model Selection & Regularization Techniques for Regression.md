# Lab: Model Selection & Regularization Techniques for Regression

## ![](https://moringa.instructure.com/courses/1426/files/631874/preview?) Lab: Model Selection & Regularization Techniques for Regression

### **Scenario:**

You are a junior data scientist working for a real estate analytics firm that helps investors and property developers make data-driven pricing decisions. Your manager wants to compare different statistical models to determine the best approach for predicting Median House Value.

Specifically, your team is evaluating:

* **Model Selection Criteria (AIC & BIC):** To compare models with different predictor sets.
* **Regularization Techniques (Ridge & Lasso Regression):** To improve predictions by reducing overfitting.

Your task is to analyze these methods and recommend the best approach based on model performance.

In predictive modeling, choosing the right set of features and avoiding overfitting is crucial. This lab will help you:

* Understand Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) for model selection.
* Compare OLS, Ridge, and Lasso regression to balance model complexity and predictive accuracy.
* Evaluate mean squared error (MSE) to determine the effectiveness of different models.

By completing this lab, you will gain valuable skills in model evaluation, feature selection, and regularization techniques, which are essential for building robust predictive models in real-world business applications.

### Tools and Resources

* [cal\_housing.tgz


  Links to an external site.](https://drive.google.com/file/d/1EWrvmqXLNP83-VLS5uHkuhUW0gj7FCwY/view?usp=drive_link)

### Instructions

**Load the appropriate libraries and bring in the data.**

**Note**: we have to [run a script to get the California Housing dataset


Links to an external site.](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) to match as it is in scikit-learn. We cannot pull it directly from scikit-learn since CodeGrade cannot access the internet.

#### Step 1

* **Add a constant** **to X**, calling it X\_const.
* **Let full\_model be the OLS** model of y and X\_const.
* Rounding to the nearest whole number, **return the full model's AIC and BIC**, separated by a comma.

#### Step 2

* **Let subset1 be the OLS model fit** with MedInc and AveRooms, and subset2 be the OLS model fit with MedInc and AveOccup.
* Rounding to the nearest whole number, **provide the AIC and BIC** for the first subset, followed by the same two information criteria for the second subset. These four values should be separated by commas.

#### Step 3

* **Define ridge\_pred** as the prediction of X\_test and ridge\_mse as the mean squared error of y\_test and ridge\_pred.
* **Return ridge\_mse,** rounded to four decimal places.

#### Step 4

* **Return ridge.coef\_.**

#### Step 5

* **Define lasso\_pred** as the prediction of X\_test and lasso\_mse as the mean squared error of y\_test and lasso\_pred.
* **Return lasso\_mse,** rounded to four decimal places.

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

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248900

Scraped At: 2026-05-15T10:37:57.318545
