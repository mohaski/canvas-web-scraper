# Process: Summarizing Bivariate Data

# Process: Summarizing Bivariate Data

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Process: Summarizing Bivariate Data

Icon Progress Bar (browser only)

5 min read

Summarizing bivariate data involves a structured approach to understanding and quantifying the relationship between two numeric variables. The process below provides a logical sequence of steps, building on foundational concepts to ensure clarity and actionable insights.

For the preceding topic we had the same first three steps, but now we add two more.

### 1. Verify Data Suitability

Ensure that the dataset contains **bivariate numeric data**: Confirm that both variables are numeric and measured on an interval or ratio scale.

### 2. Define the Variables

Clearly identify and define the roles of each variable:

* **Independent Variable (*x*):** The predictor or explanatory variable.
* **Dependent Variable (*y*):** The response or outcome variable.

### 3. Create a Scatterplot

Visualize the relationship between *x* and *y* using a scatterplot:

* Each point on the plot represents a pair of (*x*, *y*) values.
* Look for trends or patterns, such as a positive, negative, or non-linear relationship.

### 4. Compute the Linear Regression Line and Correlation Coefficient (*r*)

If the scatterplot suggests a **linear relationship**, calculate:

* **Linear Regression Line:** Represented by
  ![ModifyingAbove y With caret equals b 0 plus b 1 x](https://bletchley.instructure.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1x?scale=1)
  , where:  
  + ![b 0](https://bletchley.instructure.com/equation\_images/b\_0?scale=1)
    : Intercept of the regression line
  + ![b 1](https://bletchley.instructure.com/equation\_images/b\_1?scale=1)
    : Slope of the regression line
* **Correlation Coefficient (*r*):** Measures the strength and direction of the linear relationship:  
  + ![r greater than 0](https://bletchley.instructure.com/equation\_images/r%2520%253E%25200?scale=1)
    : Positive correlation
  + ![r less than 0](https://bletchley.instructure.com/equation\_images/r%2520%253C%25200?scale=1)
    : Negative correlation
  + ![r equals 0](https://bletchley.instructure.com/equation\_images/r%2520%253D%25200?scale=1)
    : No correlation

### 5. Interpret the Slope and Correlation Coefficient (r)

Analyze the results:

* **Slope (
  ![b 1](https://bletchley.instructure.com/equation\_images/b\_1?scale=1)
  ):** Indicates the rate of change in *y* for a one-unit change in *x*.  
  + Example: For every additional $1k spent on ads, sales increase by $5k.
* **Correlation Coefficient (*r)*:** Describes the strength and direction of the relationship.  
  + Example:
    ![r equals 0.95](https://bletchley.instructure.com/equation\_images/r%2520%253D%25200.95?scale=1)
     suggests a very strong positive correlation.

This structured process ensures that bivariate data is effectively summarized for predictive analysis and decision-making.

### Scatterplots (A Slight Return)

In the previous topic, we had six scatter plots where we described the relationships present in each. Now that we have more fully discussed the linear regression line and the correlation coefficient, let’s see these scatter plots again but with their linear regression lines and their *r*’s.

Again, we have included the code.

```
import matplotlib.pyplot as plt  
import numpy as np  
from numpy.polynomial.polynomial import Polynomial  
from scipy.stats import pearsonr  
  
  
# Create a 2x3 grid of subplots  
fig, axes = plt.subplots(2, 3, figsize=(18, 12))  
  
  
# Data for different relationships  
np.random.seed(0)  
n_samples = 50  
  
  
# Helper function to plot linear regression line  
def plot_linear_regression(ax, x, y):  
   m, b = np.polyfit(x, y, 1)  # Fit linear regression (y = mx + b)  
   x_vals = np.linspace(min(x), max(x), 100)  
   ax.plot(x_vals, m * x_vals + b, color="red", linestyle="--")  
  
  
# Helper function to display r-value  
def display_r_value(ax, x, y, fixed_r=None):  
   if fixed_r is not None:  
       r = fixed_r  
   else:  
       r, _ = pearsonr(x, y)  
   ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes,  
           fontsize=12, verticalalignment='top')  
  
  
# Strong positive linear relationship  
x1 = np.random.rand(n_samples)  
y1 = 2 * x1 + np.random.normal(0, 0.2, n_samples)  
axes[0, 0].scatter(x1, y1)  
axes[0, 0].set_title('Strong Positive Relationship')  
plot_linear_regression(axes[0, 0], x1, y1)  
display_r_value(axes[0, 0], x1, y1)  
  
  
# Weak positive linear relationship  
x2 = np.random.rand(n_samples)  
y2 = 0.5 * x2 + np.random.normal(0, 1, n_samples)  
axes[0, 1].scatter(x2, y2)  
axes[0, 1].set_title('Weak Positive Relationship')  
plot_linear_regression(axes[0, 1], x2, y2)  
display_r_value(axes[0, 1], x2, y2)  
  
  
# Weak negative linear relationship  
x3 = np.random.rand(n_samples)  
y3 = -0.5 * x3 + np.random.normal(0, 1, n_samples)  
axes[0, 2].scatter(x3, y3)  
axes[0, 2].set_title('Weak Negative Relationship')  
plot_linear_regression(axes[0, 2], x3, y3)  
display_r_value(axes[0, 2], x3, y3)  
  
  
# Strong negative linear relationship  
x4 = np.random.rand(n_samples)  
y4 = -2 * x4 + np.random.normal(0, 0.2, n_samples)  
axes[1, 0].scatter(x4, y4)  
axes[1, 0].set_title('Strong Negative Relationship')  
plot_linear_regression(axes[1, 0], x4, y4)  
display_r_value(axes[1, 0], x4, y4)  
  
  
# No relationship (truly random)  
x5 = np.random.rand(n_samples)  
y5 = np.random.rand(n_samples)  
axes[1, 1].scatter(x5, y5)  
axes[1, 1].set_title('No Relationship')  
axes[1, 1].axhline(y=np.mean(y5), color="red", linestyle="--")  # Horizontal line  
display_r_value(axes[1, 1], x5, y5, fixed_r=0)  # Force r = 0  
  
  
# Nonlinear relationship  
x6 = np.linspace(0, 10, n_samples)  
y6 = np.sin(x6) + np.random.normal(0, 0.3, n_samples)  
axes[1, 2].scatter(x6, y6)  
axes[1, 2].set_title('Nonlinear Relationship')  
  
  
# Fit and plot a nonlinear regression (degree 3 polynomial)  
p = Polynomial.fit(x6, y6, 3)  # Fit a cubic polynomial  
x_vals = np.linspace(min(x6), max(x6), 100)  
axes[1, 2].plot(x_vals, p(x_vals), color="red", linestyle="--")  
# Do not display r-value for the nonlinear graph  
  
  
# Adjust layout and display the plot  
plt.tight_layout()  
plt.show()
```

**Output:**

 
![Scatterplots output from the provided Python code.](https://moringa.instructure.com/courses/1426/files/631871/download)

**Notes:**

* The graph with no relationship has
  ![r equals 0](https://bletchley.instructure.com/equation\_images/r%253D0?scale=1)
  , since the slope is zero. In other words,
  ![b 1 equals 0](https://bletchley.instructure.com/equation\_images/b\_1%2520%253D%25200?scale=1)
   means that that there is no relationship or correlation between the two variables. This idea will be very important in the next module.
* We have left off *r* for the graph with the nonlinear relationship since here *r* the linear correlation coefficient.

### Conceptualize Summarizing Bivariate Data

Conceptualization Table of Summarizing Bivariate Data

| Term | Notation | Definition | Python Code |
| --- | --- | --- | --- |
| Simple Linear Regression Line | ![ModifyingAbove y With caret equals b 0 plus b 1 x](https://bletchley.instructure.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1x?scale=0.875) | The line that models the relationship between the independent variable (*x*) and the dependent variable (*y*). | from sklearn.linear\_model import LinearRegression |
| Predicted Value | ![ModifyingAbove y With caret](https://bletchley.instructure.com/equation\_images/%255Chat%257By%257D?scale=0.875) | The estimated value of the dependent variable (*y*) for a given value of the independent variable (*x*). | model.predict(X) |
| Intercept | ![b 0](https://bletchley.instructure.com/equation\_images/b\_0?scale=0.875) | The value of *y* when ![x equals 0](https://bletchley.instructure.com/equation\_images/x%2520%253D%25200?scale=0.875) ; the point where the regression line crosses the *y*-axis. | model.intercept\_ |
| Slope | ![b 1](https://bletchley.instructure.com/equation\_images/b\_1?scale=0.875) | The rate of change in *y* for a one-unit increase in *x*; indicates the direction and steepness of the line. | model.coef\_ |
| Independent Variable | *x* | The variable that predicts or explains changes in the dependent variable. | X = data[['x']] |
| Dependent Variable | *y* | The variable being predicted or explained by the independent variable. | y = data['y'] |
| Correlation Coefficient | *r* | A measure of the strength and direction of the linear relationship between *x* and *y* | np.corrcoef(x, y)[0, 1] |
| Scatterplot |  | A visual representation of the relationship between *x* and *y*, showing each pair of values as a point. | sns.scatterplot(x='x', y='y', data=data) |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248804

Scraped At: 2026-05-15T10:26:53.798220
