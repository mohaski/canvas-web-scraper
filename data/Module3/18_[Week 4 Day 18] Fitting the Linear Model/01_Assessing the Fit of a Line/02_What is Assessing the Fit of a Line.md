# What is Assessing the Fit of a Line?

# What is Assessing the Fit of a Line?

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) What is Assessing the Fit of a Line?

Icon Progress Bar (browser only)

16 min read

Understanding how well a regression model fits the data is fundamental to interpreting and applying its results. In this topic, you will learn to evaluate the performance of linear regression models using key diagnostic tools, ensuring their insights are both accurate and actionable.

### Key Terms and Concepts

#### Coefficient of Determination

**Coefficient of Determination (
![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
):** Measures the proportion of variance in the dependent variable explained by the independent variable(s).

##### Understanding ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1.25) : Quantifying Model Variability

The coefficient of determination (**![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)**) is a statistical measure that quantifies how well a regression model explains the variability in the dependent variable (*y*). It is a value between 0 and 1, where:

* ![LaTeX: r^2=1](https://learning.flatironschool.com/equation\_images/r%255E2%253D1?scale=1)
  : The model explains all the variability in *y*.
* ![r squared equals 0](https://learning.flatironschool.com/equation\_images/r%255E2%253D0?scale=1)
  : The model explains none of the variability, meaning it performs no better than simply predicting the mean of *y* for all observations.
* **Intermediate values:** Indicate the proportion of variability explained by the model. For example,
  ![r squared equals 0.75](https://learning.flatironschool.com/equation\_images/r%255E2%2520%253D%25200.75?scale=1)
  means the model explains 75% of the variability in *y*.

---

##### Formula for ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1.25)

The **formula for
![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)** is derived from the sum of squares:

![r squared equals 1 minus StartFraction SS Subscript residual Baseline Over SS Subscript total Baseline EndFraction](https://learning.flatironschool.com/equation\_images/r%255E2%2520%253D%25201%2520-%2520%255Cfrac%257B%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D%257D%257B%255Ctext%257BSS%257D\_%257B%255Ctext%257Btotal%257D%257D%257D?scale=1)

Where:

###### **Total Sum of Squares**

###### **( ![SS Subscript total](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Btotal%257D%257D?scale=1) ):**

![LaTeX: \text{SS}\_{\text{total}} = \sum (y\_i - \bar{y})^2](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Btotal%257D%257D%2520%253D%2520%255Csum%2520(y\_i%2520-%2520%255Cbar%257By%257D)%255E2?scale=1)

This measures the total variability in the observed data.

###### **Residual Sum of Squares**

###### **(****![SS Subscript residual](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D?scale=1) ):**

![SS Subscript residual Baseline equals sigma summation left parenthesis y Subscript i Baseline minus ModifyingAbove y With caret right parenthesis squared](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D%2520%253D%2520%255Csum%2520(y\_i%2520-%2520%255Chat%257By%257D)%255E2?scale=1)

This measures the variability in *y* that is not explained by the model (i.e., the error).

* ![LaTeX: y\_i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
  : Observed values.
* ![ModifyingAbove y With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D?scale=1)
  ​: Predicted values from the regression model.
* ![y overbar](https://learning.flatironschool.com/equation\_images/%255Cbar%257By%257D?scale=1)
  ​: Mean of the observed values.

The value of
![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
increases as the model explains more variability in *y* and decreases as the residual errors grow larger.

---

##### Conditions of  ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)

* **Interpretability:**
  ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
  only applies to linear relationships. For non-linear relationships, 
  ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
  can be misleading or low even if the model captures patterns in the data.
* **Dataset Sensitivity:** Adding irrelevant independent variables to the model can artificially inflate
  ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
  , even if the variables don’t contribute meaningfully to prediction.
* **Assumptions:** The validity of 
  ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
  relies on the model adhering to key regression assumptions like linearity and homoscedasticity.
* **Range:** is bounded between 0 and 1 inclusively, i.e.
  ![0 less than or equals r squared less than or equals 1](https://learning.flatironschool.com/equation\_images/0%2520%255Cleq%2520r%255E2%2520%255Cleq%25201%2520?scale=1)

---

##### Code to Calculate  ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)

```
# Using statsmodels  
  
# Fit the regression model  
# Add intercept  
X = sm.add_constant(x)  
# Model  
model = sm.OLS(y, X).fit()  
  
# Extract r-squared  
r_squared = model.rsquared  
  
  
# Using numpy  
  
# Predicted values  
y_pred = model.predict(X)  
  
# Compute r-squared manually  
# Total sum of squares  
ss_total = np.sum((y - np.mean(y)) ** 2)  
# Residual sum of squares   
ss_residual = np.sum((y - y_pred) ** 2)  
  
r_squared_manual = 1 - (ss_residual / ss_total)
```

We can see that using statsmodes, model.rsquared gives this value automatically after fitting the model, whereas with numpy it has to be calculated “by hand”.

#### Residuals

**Residuals:** The differences between observed and predicted values of the dependent variable.

##### Residuals: The Differences Between Observed and Predicted Values

Residuals are a fundamental concept in regression analysis. A residual is the difference between an observed value (
![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
) and its corresponding predicted value (
![ModifyingAbove y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
​) from the regression model. Mathematically, the residual for each data point is expressed as:

![e Subscript i Baseline equals y Subscript i Baseline minus ModifyingAbove y With caret Subscript i](https://learning.flatironschool.com/equation\_images/e\_i%2520%253D%2520y\_i%2520-%2520%255Chat%257By%257D\_i?scale=1)

Where:

* ![e Subscript i](https://learning.flatironschool.com/equation\_images/e\_i?scale=1)
  ​: The **residual (or error**) for the i-th observation.
* ![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
  ​: The **observed value** of the dependent variable.
* ![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
  ​: The **predicted value** of the dependent variable based on the regression line.

Residuals are the errors in the model’s predictions, and their analysis is critical for assessing the quality of the regression model.

---

##### Residuals and Ordinary Least Squares (OLS)

The **Ordinary Least Squares (OLS)** method was first formalized by **Carl Friedrich Gauss** in the early 19th century as a technique for estimating unknown parameters in linear equations. OLS originated as a solution to astronomical problems, particularly in fitting orbits, and has since become a cornerstone of statistical modeling.

The OLS method guarantees that the line fitted to the data is the best-fit line, meaning it minimizes the total squared error between the observed values and the predicted values:

![LaTeX: \text{SS}\_{\text{residual}} = \sum (y\_i - \hat{y}\_i)^2](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D%2520%253D%2520%255Csum%2520(y\_i%2520-%2520%255Chat%257By%257D\_i)%255E2?scale=1)

This property makes OLS the most widely used method for linear regression, ensuring the smallest possible residuals in the squared sense. (The proof of this is beyond the scope of this module.)

---

##### Why Residuals Are Important

* **Measure of Error:** Residuals quantify the difference between what the model predicts (
  ![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
  ​) and what is actually observed (*y*).
* **Assessing Model Fit:** The smaller the residuals, the better the model fits the data. If the residuals are large, it suggests that the model is not accurately predicting the dependent variable.
* **Diagnostics:** Analyzing residuals helps check whether the assumptions of linear regression (e.g., linearity, homoscedasticity, independence) are satisfied.

---

##### Code to Calculate Residuals

Here’s how you can calculate residuals and visualize them using Python with statsmodels.

```
import statsmodels.api as sm  
  
# Fit the regression model  
X = sm.add_constant(x)  # Add intercept  
model = sm.OLS(y, X).fit()  
  
# Compute residuals  
residuals = model.resid  
  
# Display residuals  
print(residuals.head())
```

Let’s look at **two sample residuals as they are on the scatter plot with the regression line.** The graph visually illustrates the concept of residuals in regression analysis. Each residual represents the difference between the observed value (
![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
​) and its corresponding predicted value (
![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
​) on the regression line.

 
![Graph of residuals scatter plot with regression line.](https://moringa.instructure.com/courses/1426/files/631821/download)

###### **Key Observations**

1. **Regression Line (Red Line):**  
   * The red line represents the best-fit regression line obtained using Ordinary Least Squares (OLS).
   * This line minimizes the sum of squared residuals
     ![LaTeX: \sum (y\_i - \hat{y}\_i)^2](https://learning.flatironschool.com/equation\_images/%255Csum%2520(y\_i%2520-%2520%255Chat%257By%257D\_i)%255E2?scale=1)
      to provide the most accurate predictions.
2. **Data Points (Blue Dots):**  
   * Each blue dot represents an observation in the dataset
     ![LaTeX: (x\_i, y\_i​)](https://learning.flatironschool.com/equation\_images/(x\_i%252C%2520y\_i%25E2%2580%258B)?scale=1)
     .
   * The vertical distance between the blue dots (observed values) and the regression line (predicted values) represents the residual (
     ![e Subscript i](https://learning.flatironschool.com/equation\_images/e\_i?scale=1)
     ​).
3. **Residuals:** Residuals represent the vertical difference or vertical distance between the observed values (
   ![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
   ​) and the predicted values (
   ![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
   ​) calculated using the regression line
   ![ModifyingAbove y With caret equals 2.4 x minus 2.31](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%25202.4x%2520-%25202.31?scale=1)
   .  
   * **Positive Residuals (Green Dashed Lines):** A positive residual occurs when the observed value (
     ![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
     ) is above the predicted value (
     ![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
     ​). For example:  
     + At
       ![x equals 2](https://learning.flatironschool.com/equation\_images/x%2520%253D%25202?scale=1)
       :  
       - Predicted value:
         ![y With caret equals 2.4 left parenthesis 2 right parenthesis minus 2.31 equals 4.80 minus 2.31 equals 2.49](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%25202.4(2)%2520-%25202.31%2520%253D%25204.80%2520-%25202.31%2520%253D2.49?scale=1)
         .
       - Observed value:
         ![y equals 3.60](https://learning.flatironschool.com/equation\_images/y%2520%253D%25203.60?scale=1)
         .
       - Residual:
         ![e Subscript i Baseline equals 3.60 minus 2.49 equals 1.11](https://learning.flatironschool.com/equation\_images/e\_i%2520%253D%25203.60%2520-%25202.49%2520%253D%25201.11?scale=1)
         (positive residual).
   * **Negative Residuals (Orange Dashed Lines):** A negative residual occurs when the observed value (
     ![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
     ​) is below the predicted value (
     ![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
     ​). For example:
     + At
       ![x equals 9](https://learning.flatironschool.com/equation\_images/x%2520%253D%25209?scale=1)
       :
       - Predicted value:
         ![y With caret equals 2.4 left parenthesis 9 right parenthesis minus 2.31 equals 21.6 minus 2.31 equals 19.29](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%25202.4(9)%2520-%25202.31%2520%253D%252021.6%2520-%25202.31%2520%253D%252019.29?scale=1)
         .
       - Observed value:
         ![y equals 14.11](https://learning.flatironschool.com/equation\_images/y%2520%253D%252014.11?scale=1)
         .
       - Residual:
         ![e Subscript i Baseline equals 14.11 minus 19.29 equals negative 5.18](https://learning.flatironschool.com/equation\_images/e\_i%253D%252014.11%2520-%252019.29%2520%253D%2520-5.18?scale=1)
         (negative residual).
4. **Magnitude of Residuals:** Larger vertical gaps indicate larger residuals (errors). Smaller gaps suggest that the regression line is closely predicting the observed values.

#### Residual Plot

**Residual Plot:** A scatterplot of residuals used to detect patterns or deviations from assumptions.

A residual plot is a graphical tool used in regression analysis to visualize the residuals (
![e Subscript i](https://learning.flatironschool.com/equation\_images/e\_i?scale=1)
​) of a model. It is a scatterplot where the residuals (
![e Subscript i Baseline equals y Subscript i Baseline minus ModifyingAbove y With caret Subscript i](https://learning.flatironschool.com/equation\_images/e\_i%2520%253D%2520y\_i%2520-%2520%255Chat%257By%257D\_i?scale=1)
​) are plotted on the *y*-axis and the corresponding predicted values (
![LaTeX: \hat{y}](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D?scale=1)
) are plotted on the *x*-axis. This plot is essential for diagnosing the quality of a regression model and checking whether its assumptions are satisfied.

---

##### Importance of Residual Plots

1. **Assessing Model Fit:** Residual plots help determine whether the regression model captures the underlying patterns in the data. If the residuals are randomly scattered around zero, the model likely fits the data well.
2. **Detecting Patterns:** Patterns in the residual plot (e.g., a curve or a funnel shape) suggest that the model may not meet key assumptions of linear regression, such as linearity or homoscedasticity.
3. **Identifying Outliers:** Residual plots can highlight data points with unusually large residuals (outliers) that might unduly influence the model.
4. **Verifying Assumptions:** The residual plot is used to check for the following, which are in a subsequent topic:  
   * **Linearity:** Residuals should have no clear pattern.
   * **Homoscedasticity:** Residuals should have constant variance (no funnel shape).
   * **Independence:** Residuals should not exhibit autocorrelation (no systematic trends).

---

##### Code to Generate a Residual Plot

Here’s how to **create a residual plot in Python** using statsmodels.

```
import matplotlib.pyplot as plt  
# Fit the regression model  
X = sm.add_constant(x)  # Add intercept  
model = sm.OLS(y, X).fit()  
  
# Compute residuals and predicted values  
residuals = model.resid  
y_pred = model.predict(X)  
  
# Residual plot  
plt.scatter(y_pred, residuals, color='blue', alpha=0.7)  
plt.axhline(0, color='red', linestyle='--', linewidth=1)  
plt.title('Residual Plot')  
plt.xlabel('Predicted Values ($\hat{y}$)')  
plt.ylabel('Residuals ($e_i$)')  
plt.grid(True)  
plt.show()
```

---

##### Interpreting the Residual Plot

1. **Random Scatter:** If the residuals are randomly scattered around the horizontal axis (
   ![LaTeX: e\_i \approx 0](https://learning.flatironschool.com/equation\_images/e\_i%2520%255Capprox%25200?scale=1)
   ), the regression model likely fits the data well, and the assumptions of linear regression are satisfied.
2. **Curvature:** A curved pattern in the residual plot suggests a violation of the linearity assumption. This may indicate that the relationship between the variables is not linear and another type of model (e.g., polynomial regression) may be more appropriate.
3. **Funnel Shape:** If the residuals exhibit a funnel shape, where the variance of residuals increases or decreases as predicted values increase, the assumption of homoscedasticity (constant variance) is violated. This often requires transformations of the dependent variable or alternative modeling techniques.
4. **Outliers:** Residuals that lie far from the horizontal line (
   ![LaTeX: e\_i \ne 0](https://learning.flatironschool.com/equation\_images/e\_i%2520%255Cne%25200?scale=1)
   ) indicate outliers that may have a disproportionate impact on the regression line. Some of these points, known as influential points, exert a strong influence on the regression model by significantly altering the slope or intercept. Investigating these points can help improve the model's performance and reliability. These concepts, including the identification of influential points, will be investigated in more detail next.

![Four residual plots with different regression scenarios.](https://moringa.instructure.com/courses/1426/files/631842/download)

**The image displays four residual plots, each showcasing different regression scenarios**:

* **Linear, No Outliers/Influence (Top-Left):** This residual plot shows a random scatter of residuals around the horizontal line at y=0, which indicates that the linear regression model is appropriate. There are no visible patterns, outliers, or influential points, and the variance of residuals appears constant, satisfying the assumptions of linear regression.   
    
  **Random Scatter:** Indicates a well-fitted linear model.
* **Linear, With Outliers/Influence (Top-Right):** In this plot, the residuals are mostly close to zero, but a few extreme residuals are present. These points suggest outliers or influential values that could disproportionately affect the regression line. These points must be investigated further to determine their cause and whether they should be removed or adjusted.   
    
  **Outliers/Influence:** Outliers distort the model and need investigation.
* **No Correlation,
  ![r equals 0](https://learning.flatironschool.com/equation\_images/r%2520%253D%25200?scale=1)
  (Bottom-Left):** This residual plot has no discernible pattern, but the residuals are widely scattered with no clear trend. This suggests that there is no linear relationship between *x* and *y*. Here, the linear regression model fails to capture any meaningful relationship.   
    
  **No Correlation:** Suggests no linear relationship.
* **Nonlinear Regression (Bottom-Right):** The residuals display a distinct curved pattern, indicating that the relationship between *x* and *y* is non-linear. The linear regression model is inappropriate for this data, as it fails to capture the curvature. A more suitable model, such as a polynomial regression, should be considered.   
    
  **Nonlinearity:** Curvature in residuals requires a non-linear model.

This analysis highlights the importance of residual plots in diagnosing issues like outliers, non-linearity, and poor model fit.

#### Influential Values

**Influential Values:** Data points that disproportionately affect the regression line.

Influential values are **specific data points in a dataset that have a significant impact on the regression line**. These points can disproportionately influence the slope, intercept, or overall fit of the regression model. While outliers are points with large residuals (errors), influential values may or may not have large residuals. Instead, they are characterized by their ability to shift the regression line due to their extreme position relative to the rest of the data.

##### Key Concepts of Influential Values

* **Leverage:** Influential points often have high leverage, meaning they are far from the means of the independent variables (*x*).
* **Impact on Fit:** Even a small vertical deviation for a high-leverage point can strongly influence the slope and intercept of the regression line.
* **Detection:** Influential values are identified using diagnostic tools like Cook’s Distance or leverage statistics.

---

##### Cook’s Distance

**Cook’s Distance** is one of the most widely used measures to identify influential values. It combines the **residual size** and the **leverage** of a point to quantify its overall influence on the regression model.

The **formula for Cook’s Distance (**
![upper D Subscript i](https://learning.flatironschool.com/equation\_images/D\_i?scale=1)
) is:

![LaTeX: D\_i = \frac{\sum\_{j=1}^n \left( \hat{y}\_j - \hat{y}\_{j(-i)} \right)^2}{p \cdot \text{MSE}}](https://learning.flatironschool.com/equation\_images/D\_i%2520%253D%2520%255Cfrac%257B%255Csum\_%257Bj%253D1%257D%255En%2520%255Cleft(%2520%255Chat%257By%257D\_j%2520-%2520%255Chat%257By%257D\_%257Bj(-i)%257D%2520%255Cright)%255E2%257D%257Bp%2520%255Ccdot%2520%255Ctext%257BMSE%257D%257D?scale=1)

Where:

* ![upper D Subscript i](https://learning.flatironschool.com/equation\_images/D\_i?scale=1)
  ​: Cook's Distance for the i-th observation.
* ![y With caret Subscript j](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_j?scale=1)
  ​: Predicted value with all data points included.
* ![y With caret Subscript j left parenthesis negative i right parenthesis](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_%257Bj(-i)%257D?scale=1)
  ​: Predicted value when the i-th observation is excluded from model training/fitting
* *p*: Number of parameters in the model.
* **MSE:** Mean Squared Error of the model.

**Rule of Thumb**:
![upper D Subscript i Baseline greater than 1](https://learning.flatironschool.com/equation\_images/D\_i%2520%253E%25201?scale=1)
: Indicates a highly influential point that warrants further investigation.

---

##### Why Are Influential Points Important?

* **Model Distortion:** Influential points can distort the regression model, leading to inaccurate predictions and misleading results.
* **Identifying Issues:** They often indicate data entry errors, incorrect measurements, or genuine but extreme observations.
* **Improving Model Fit:** Investigating and appropriately handling influential points (e.g., removing, transforming, or separating them) can improve model accuracy.

---

##### Code to Identify Influential Points Using Cook’s Distance

Here’s an example of **how to identify influential points using Cook’s Distance in Python** with statsmodels.

```
import statsmodels.api as sm  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
  
import statsmodels.api as sm  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
  
# Generate example data  
np.random.seed(42)  
x = np.random.rand(50) * 100  # Independent variable  
y = 2.5 * x + np.random.normal(size=50, scale=10)  # Dependent variable  
  
# Add an influential point  
x = np.append(x, 150)  # High leverage  
y = np.append(y, 50)   # Low y value relative to x  
  
# Fit the regression model  
X = sm.add_constant(x)  
model = sm.OLS(y, X).fit()  
  
# Compute Cook's Distance  
influence = model.get_influence()  
cooks_d = influence.cooks_distance[0]  
  
# Plot Cook's Distance  
plt.stem(np.arange(len(cooks_d)), cooks_d, basefmt=" ")  
plt.axhline(1, color='red', linestyle='--', linewidth=1, label="Threshold (D > 1)")  
plt.title("Cook's Distance")  
plt.xlabel("Observation Index")  
plt.ylabel("Cook's Distance")  
plt.legend()  
plt.show()  
  
# Print influential points  
influential_points = np.where(cooks_d > 1)[0]  
print(f"Influential Points: {influential_points}")
```

![Cook&#39;s Distance plot](https://moringa.instructure.com/courses/1426/files/631840/download)

**Interpreting the Output**

1. **Cook’s Distance Plot:**

* Data points with Cook's Distance > 1 are flagged as influential points.
* These points have a disproportionately large impact on the regression model.

1. **Identified Influential Points:** If any points are identified, they should be investigated to determine whether they are valid data points or errors.

---

##### Key Takeaways

* Influential values are data points that significantly affect the regression model by altering the slope, intercept, or overall fit. **Cook’s Distance is a key diagnostic tool for identifying these points**.
* Influential points may or may not be outliers; their defining characteristic is their ability to disproportionately influence the regression line.
* Proper identification and handling of influential points are critical to ensure the accuracy and reliability of the regression model.
* By visualizing and analyzing influential values, you can assess their impact on the regression line and make informed decisions to refine your model.

#### Outliers

**Outliers:** Observations that deviate significantly from the fitted regression line.

Outliers are **observations in a dataset that lie far from the fitted regression line,** meaning their residuals (
![e Subscript i](https://learning.flatironschool.com/equation\_images/e\_i?scale=1)
​) are unusually large. These points deviate significantly from the pattern established by the majority of the data and can impact the regression model's accuracy and reliability. Recall from our descriptive statistics for univariate numeric or quantitative variables, that we used the upper and lower fences in conjunction with a boxplot to identify outliers.

---

##### Key Concepts of Outliers

* **Definition:** An outlier is a data point where the observed value
  ![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
  ​ is far from the predicted value
  ![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
  ​, resulting in a large residual:
  ![e Subscript i Baseline equals y Subscript i Baseline minus ModifyingAbove y With caret Subscript i](https://learning.flatironschool.com/equation\_images/e\_i%2520%253D%2520y\_i%2520-%2520%255Chat%257By%257D\_i?scale=1)
* **Impact of Outliers:**  
  + Outliers can inflate residuals and distort the slope and intercept of the regression line.
  + They can reduce the overall goodness of fit and lower the
    ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
    value of the model.
  + While not all outliers are influential, they can still highlight issues such as data entry errors, incorrect measurements, or genuine but extreme data points
* **Detection:**
  + Outliers are identified through residual analysis.
  + Data points with large absolute residuals are potential outliers.

**Residual plots are an effective tool for identifying outliers.** Points far from the horizontal line (
![e Subscript i Baseline equals 0](https://learning.flatironschool.com/equation\_images/e\_i%2520%253D%25200?scale=1)
) are potential outliers.

---

##### Code to Detect and Visualize Outliers

The following example demonstrates how to identify outliers by analyzing residuals in Python.

```
import statsmodels.api as sm  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
  
# Generate example data  
np.random.seed(42)  
x = np.random.rand(50) * 100  # Independent variable  
y = 2.5 * x + np.random.normal(size=50, scale=10)  # Dependent variable  
  
# Add an outlier  
x = np.append(x, 150)  # Extreme x value  
y = np.append(y, -250)  # Large negative y value  
  
# Fit the regression model  
X = sm.add_constant(x)  # Add intercept  
model = sm.OLS(y, X).fit()  
  
# Compute residuals and predicted values  
residuals = model.resid  
y_pred = model.predict(X)  
  
# Plot Residuals  
plt.scatter(y_pred, residuals, color='blue', alpha=0.7)  
plt.axhline(0, color='red', linestyle='--', linewidth=1)  
plt.title('Residual Plot: Identifying Outliers')  
plt.xlabel('Predicted Values ($\hat{y}$)')  
plt.ylabel('Residuals ($e_i$)')  
plt.show()  
  
# Identify potential outliers  
threshold = 3 * np.std(residuals)  # Common threshold for outliers  
outliers = np.where(np.abs(residuals) > threshold)[0]  
print(f"Outliers detected at indices: {outliers}")
```

![Output of residual plot: identifying outliers.](https://moringa.instructure.com/courses/1426/files/631879/download)

**Key Observations:**

* The residual plot clearly identifies an outlier with a large negative residual.
* Outliers can arise from data errors, measurement inconsistencies, or natural variability in the data.
* While an outlier might not be influential (affecting the slope or intercept), it still distorts the model’s performance and should be investigated.

---

##### How to Handle Outliers

* **Investigate:** Verify if the outlier is due to a data entry error or a measurement issue.
* **Remove or Adjust:** If the outlier is an error, remove or correct it. If it is a legitimate value, assess its impact on the model.
* **Robust Regression:** Use techniques like robust regression to minimize the impact of outliers.

---

##### Key Takeaways

* Outliers are data points with large residuals (
  ![StartAbsoluteValue e Subscript i Baseline EndAbsoluteValue](https://learning.flatironschool.com/equation\_images/%257Ce\_i%257C%2520?scale=1)
  ) that deviate significantly from the regression line.
* They are identified using residual plots and statistical thresholds such as
  ![3 dot standard deviation](https://learning.flatironschool.com/equation\_images/3%255Ccdot%2520%255Ctext%257Bstandard%2520deviation%257D%2520?scale=1)
  .
* Proper identification and handling of outliers are essential to ensure the regression model's accuracy and reliability.

By detecting and addressing outliers, you can refine your regression model and improve its performance on the remaining data.

### How Does Assessing the Fit of a Line Work?

Assessing the fit of a regression line involves evaluating how well the model represents the data and whether the assumptions of linear regression are satisfied. In data science workflows, this process ensures that the model is both accurate and interpretable, making it a cornerstone of effective data-driven decision-making. By analyzing metrics like
![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
, residual plots, and diagnostics such as Cook’s Distance, data scientists can refine models to produce reliable predictions and actionable insights.

#### Significance in Data Science Workflow

##### **Quantifying Model Performance with ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)**

The coefficient of determination, measures the proportion of variability in the dependent variable (y) that is explained by the independent variable (x).

**Why It Matters:** A high value indicates that the model captures a substantial portion of the data's variability, making it a strong predictor. Conversely, a low  suggests that the model does not explain much of the variation, requiring further refinement or alternative approaches.

**Example in Data Science:** In predicting house prices based on square footage, an  of 0.85 means that 85% of the variability in house prices is explained by the model, providing confidence in its predictive power.

##### **Residual Plots to Detect Assumption Violations**

Residual plots are scatterplots of residuals (errors) against predicted values or independent variables. They help identify deviations from regression assumptions like linearity, independence of errors, and homoscedasticity.

**Why It Matters:** Residual plots ensure the validity of the linear regression model. For instance, a curved pattern in the residuals indicates non-linearity, while a "funnel" shape suggests heteroscedasticity (unequal variance).

**Example in Data Science:** A data scientist working on customer churn analysis might find a residual plot showing a pattern, indicating the need for a non-linear model or variable transformation to improve accuracy.

##### **Identifying Influential Observations with Cook’s Distance**

Cook’s Distance measures the influence of individual data points on the regression model. High values indicate points that disproportionately affect the fitted line.

**Why It Matters:** Identifying and investigating influential points helps improve model reliability. Removing or adjusting for these points can prevent them from skewing results.

**Example in Data Science:** In financial modeling, an outlier such as a single extremely high transaction could disproportionately impact the relationship between income and spending. Cook’s Distance helps flag such points for further analysis.

#### Relevance to Data Science

**Refining Predictive Models:** Assessing the fit of a line ensures that models are robust and align with the underlying data. For example, in a marketing campaign analysis,
![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
 validates how well ad spend predicts revenue, while residual plots ensure no assumptions are violated.

**Communicating Insights:** Evaluating the model's fit helps communicate its reliability to stakeholders. For instance, explaining that
![r squared equals 0.9](https://learning.flatironschool.com/equation\_images/r%255E2%2520%253D%25200.9?scale=1)
 and no assumption violations were detected builds trust in the model's outcomes.

**Iterative Model Development:** Diagnostics like Cook’s Distance support iterative refinement of models by identifying outliers and influential points, leading to more reliable and interpretable results.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248815

Scraped At: 2026-05-15T10:28:06.394403
