# Summary: Multiple Linear Regression

# Summary: Multiple Linear Regression

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Summary: Multiple Linear Regression

Icon Progress Bar (browser only)

2 min read

### Terms Recap

* **Dependent Variable (*y*):** The outcome variable you aim to predict or explain.
* **Independent Variables (
  ![x 1 comma x 2 comma ellipsis comma x Subscript p Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520x\_2%252C%2520%255Cdots%252C%2520x\_p?scale=1)
  ):** The predictors that explain variation in the dependent variable.
* **Regression Equation:** Describes the relationship between *y* and predictors:  
  ![y With caret equals b 0 plus b 1 x 1 plus b 2 x 2 plus ellipsis plus b Subscript p Baseline x Subscript p](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1x\_1%2520%252B%2520b\_2x\_2%2520%252B%2520%255Cdots%2520%252B%2520b\_px\_p?scale=1)
* **Coefficients (
  ![b 1 comma b 2 comma ellipsis comma b Subscript p Baseline](https://learning.flatironschool.com/equation\_images/b\_1%252C%2520b\_2%252C%2520%255Cdots%252C%2520b\_p?scale=1)
  ):** Measure the effect of each predictor on *y*.
* **Residuals (
  ![e Subscript i](https://learning.flatironschool.com/equation\_images/e\_i?scale=1)
  ):** The difference between observed and predicted values:  
  ![e Subscript i Baseline equals y Subscript i Baseline minus ModifyingAbove y With caret Subscript i](https://learning.flatironschool.com/equation\_images/e\_i%2520%253D%2520y\_i%2520-%2520%255Chat%257By%257D\_i?scale=1)
* **![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
  :** The proportion of variance in *y* explained by the predictors.
* As a rule, this should not be used for multiple linear regression
* **Adjusted
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  :** A version of
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  that adjusts for the number of predictors, preventing overfitting.
* **Multicollinearity:** When predictors are highly correlated, leading to unreliable coefficient estimates.

### Key Concepts

* **Incorporating Multiple Predictors:** Multiple Linear Regression models relationships between one dependent variable and multiple independent variables.
* **Quantifying Predictors' Impact:** The slope coefficients indicate how changes in predictors affect the outcome.
* **Evaluating Model Performance:** Use metrics like Adjusted
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  to assess fit and avoid overfitting.
* **Diagnosing Issues:** Check for multicollinearity, assumption violations, and influential data points.
* **Practical Applications:** Multiple Linear Regression is widely used to make predictions, understand relationships, and inform decisions in business, healthcare, and other fields.

### Brief Process Overview

1. **Import and Prepare Data:** Load and clean the dataset.
2. **Define Variables:** Identify the dependent and independent variables.
3. **Fit the Model:** Use tools like statsmodels to estimate the regression coefficients.
4. **Evaluate the Model:** Analyze Adjusted
   ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
   and p-values to assess the model's quality. You will learn more ways to evaluate regression models as you move forward in this course
5. **Visualize Results:** Plot relationships and predictions for a better understanding of the model.
6. **Make Predictions:** Use the model to predict outcomes for new data.

Each step builds on the previous one, providing a structured approach to implementing and interpreting Multiple Linear Regression.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248854

Scraped At: 2026-05-15T10:32:41.736262
