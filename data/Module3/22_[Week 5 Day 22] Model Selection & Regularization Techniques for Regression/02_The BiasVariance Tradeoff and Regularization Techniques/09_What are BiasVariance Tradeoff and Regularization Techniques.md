# What are Bias/Variance Tradeoff and Regularization Techniques?

# What are Bias/Variance Tradeoff and Regularization Techniques?

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) What are Bias/Variance Tradeoff and Regularization Techniques?

Icon Progress Bar (browser only)

4 min read

The bias/variance tradeoff and regularization techniques are fundamental concepts in machine learning and regression modeling. They address the challenges of model performance, particularly how well a model generalizes to unseen data.

### Key Terms and Concepts

#### Bias/Variance Tradeoff

The bias/variance tradeoff describes the balance between two sources of error in a model:

* **Bias (Underfitting):**
  + Bias refers to the error caused by oversimplifying the model, leading to underfitting.
  + A model with high bias fails to capture the underlying relationships in the data.
  + **Example:** A linear model applied to data with a complex, nonlinear pattern.
* **Variance (Overfitting):**
  + Variance refers to the error caused by overly complex models that capture noise in the training data instead of generalizable patterns.
  + A model with high variance performs well on training data but poorly on unseen test data.
  + **Example:** A polynomial regression model with a very high degree.

The **ideal model strikes a balance between bias and variance** to minimize the total prediction error.

#### Mean Squared Error (MSE)

The bias/variance tradeoff can be quantitatively analyzed using the **Mean Squared Error (MSE)**, which decomposes the total error into three components:

![Total Error equals Bias squared plus Variance plus Irreducible Error](https://learning.flatironschool.com/equation\_images/%255Ctext%257BTotal%2520Error%257D%2520%253D%2520%255Ctext%257BBias%257D%255E2%2520%252B%2520%255Ctext%257BVariance%257D%2520%252B%2520%255Ctext%257BIrreducible%2520Error%257D?scale=1)

* **Bias:** Measures the error introduced by approximating the real relationship with a simplified model.
* **Variance:** Measures how much the model's predictions vary for different training sets.
* **Irreducible Error:** Error caused by noise in the data that cannot be reduced regardless of the model's complexity.

The mathematical formula is:

![Total Error equals Bias squared plus Variance plus Irreducible Error](https://learning.flatironschool.com/equation\_images/%255Ctext%257BMSE%257D%2520%253D%2520%255Cfrac%257B1%257D%257Bn%257D%2520%255Csum\_%257Bi%253D1%257D%255En%2520%255Cleft(%2520y\_i%2520-%2520%255Chat%257By%257D\_i%2520%255Cright)%255E2?scale=1)

where

* ![n](https://learning.flatironschool.com/equation\_images/n?scale=1)
  : Number of data points (observations).
* ![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
  ​: Actual value of the iii-th observation.
* ![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
  ​: Predicted value of the iii-th observation.
* ![left parenthesis y Subscript i Baseline minus y With caret Subscript i Baseline right parenthesis squared](https://learning.flatironschool.com/equation\_images/%255Cleft(%2520y\_i%2520-%2520%255Chat%257By%257D\_i%2520%255Cright)%255E2?scale=1)
  : Squared difference between the actual and predicted values.

The **MSE measures the average of the squared errors**, indicating how close the predictions are to the actual values. Lower MSE values indicate better model performance.

##### Graphical Representation

The tradeoff between bias and variance can be visualized:

1. **Bias decreases** as the model becomes more complex and fits the training data better.
2. **Variance increases** because the model begins to overfit the training data.

The **optimal model lies where test error is minimized.**

![Bias-Variance Tradeoff graph.](https://moringa.instructure.com/courses/1426/files/631803/download)

#### Regularization Techniques

Regularization is a set of techniques used to reduce overfitting (high variance) by adding a penalty term to the loss function. This encourages simpler models with smaller coefficients, improving generalization.

The **two most common types of regularization** are:

1. **L1 Regularization:** Adds the absolute value of the coefficients as a penalty.
   * Encourages sparsity by shrinking some coefficients to exactly zero.
   * This technique is used in Lasso regression.
2. **L2 Regularization:** Adds the squared value of the coefficients as a penalty.
   * Shrinks coefficients towards zero, but not exactly zero.
   * This technique is used in Ridge regression.

### How Do Bias/Variance Tradeoff and Regularization Techniques Work?

The tradeoff between bias and variance can be visualized using error decomposition:

![Total Error equals Bias squared plus Variance plus Irreducible Error](https://learning.flatironschool.com/equation\_images/%255Ctext%257BTotal%2520Error%257D%2520%253D%2520%255Ctext%257BBias%257D%255E2%2520%252B%2520%255Ctext%257BVariance%257D%2520%252B%2520%255Ctext%257BIrreducible%2520Error%257D?scale=1)

* **Bias:** Measures the error introduced by approximating the real relationship with a simplified model.
* **Variance:** Measures how much the model's predictions vary for different training sets.

Regularization techniques, such as **Lasso (L1)** and **Ridge (L2)**, help control variance by shrinking model coefficients, thus improving generalization.

---

#### Bias/Variance Tradeoff Visualization

#### ![Three polynomial regression models: underfit, good fit, and overfit.](https://moringa.instructure.com/courses/1426/files/631815/download)

**Explanation:**

* As the **degree of the polynomial increases**:  
  + **Bias decreases** because the model becomes more complex and fits the training data better.
  + **Variance increases** because the model starts overfitting the training data.
* The **optimal model** is where the test error is minimized, which is the good fit above.

  ---

#### Lasso (L1) and Ridge (L2) Regularization

Both Lasso and Ridge regularization add a penalty term to the loss function, as shown below:

1. **Ridge Regression (L2 Regularization):** The Ridge penalty is the **sum of squared coefficients**:
   ![Loss Function equals RSS plus lamda sigma summation Underscript j equals 1 Overscript p Endscripts beta Subscript j Superscript 2](https://learning.flatironschool.com/equation\_images/%255Ctext%257BLoss%2520Function%257D%2520%253D%2520%255Ctext%257BRSS%257D%2520%252B%2520%255Clambda%2520%255Csum\_%257Bj%253D1%257D%255Ep%2520%255Cbeta\_j%255E2?scale=1)
   * ![lamda](https://learning.flatironschool.com/equation\_images/%255Clambda?scale=1)
     : Regularization strength (tuning parameter).
   * Ridge shrinks coefficients towards zero but does not make them exactly zero.
2. **Lasso Regression (L1 Regularization):** The Lasso penalty is the **sum of the absolute values** of the coefficients:   
   ![Loss Function equals RSS plus lamda sigma summation Underscript j equals 1 Overscript p Endscripts StartAbsoluteValue beta Subscript j Baseline EndAbsoluteValue](https://learning.flatironschool.com/equation\_images/%255Ctext%257BLoss%2520Function%257D%2520%253D%2520%255Ctext%257BRSS%257D%2520%252B%2520%255Clambda%2520%255Csum\_%257Bj%253D1%257D%255Ep%2520%257C%255Cbeta\_j%257C?scale=1)
     
   * ![lamda](https://learning.flatironschool.com/equation\_images/%255Clambda?scale=1)
     : Regularization strength.
   * Lasso can shrink coefficients to exactly zero, performing variable selection.

**Below is Python code** that gives you an idea of how Ridge and Lasso are implemented in sklearn:

```
from sklearn.linear_model import Ridge, Lasso  
  
# Ridge Regression  
ridge = Ridge(alpha=1.0)  
ridge.fit(X_train, y_train)  
ridge_coef = ridge.coef_  
print("Ridge Coefficients:", ridge_coef)  
  
# Lasso Regression  
lasso = Lasso(alpha=0.1)  
lasso.fit(X_train, y_train)  
lasso_coef = lasso.coef_  
print("Lasso Coefficients:", lasso_coef)
```

### Summary

* **Bias/Variance Tradeoff:** Balancing underfitting and overfitting to find the optimal model.
* **Mean Squared Error (MSE):** Measures prediction error and is decomposed into bias, variance, and irreducible error.
* **Regularization:** Reduces variance by penalizing large coefficients.
* **L1 (Lasso):** Shrinks coefficients to zero, performing feature selection.
* **L2 (Ridge):** Shrinks coefficients without eliminating predictors.
* **Significance:** Regularization techniques ensure models generalize well to unseen data while maintaining accuracy and interpretability.

By understanding the bias/variance tradeoff and applying regularization techniques like Lasso and Ridge, data scientists can develop models that are both robust and interpretable.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248894

Scraped At: 2026-05-15T10:37:15.449614
