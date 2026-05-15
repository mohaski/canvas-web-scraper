# Technical Lesson: Assumptions of Linear Regression

# Technical Lesson: Assumptions of Linear Regression

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: Assumptions of Linear Regression

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

As a junior data scientist at a retail analytics firm, your manager tasks you with building a linear regression model to predict weekly sales (yyy) based on advertising spend (xxx). The company needs this model to help allocate advertising budgets more efficiently. Before presenting the model to stakeholders, you must ensure it meets all the assumptions of linear regression. If the assumptions are violated, the model's predictions could be inaccurate, leading to poor decision-making.

To approach this systematically, you’ll:

1. Fit the linear regression model.
2. Use diagnostic plots to verify that the four key assumptions (linearity, independence of errors, normality of errors, and equal variances) are satisfied.

### Video: Technical Lesson Guide

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of assumptions of linear regression.

[VIDEO LINK](https://player.vimeo.com/video/1060371440?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Resources

* Jupyter Notebook and/or Integrated Development Environment (IDE) for Python like Colab VS Code.

### Instructions

#### Step 1. Import Required Libraries

**Import the Python libraries** needed for this analysis. Tools like statsmodels and seaborn will help fit the regression model and generate diagnostic plots.

```
import numpy as np    
import pandas as pd    
import statsmodels.api as sm    
import matplotlib.pyplot as plt    
import seaborn as sns 
```

#### Step 2. Generate Example Data

For the analysis, **simulate weekly advertising spend (xxx) and weekly sales (yyy) for 100 weeks.** This synthetic data represents real-world patterns with random noise added to mimic variability.

```
np.random.seed(42)    
x = np.random.rand(100) * 10  # Advertising Spend (in $1000s)  
y = 2.5 * x + np.random.normal(size=100) * 3  # Sales with noise    
  
data = pd.DataFrame({'x': x, 'y': y}) 
```

#### Step 3. Fit the Linear Regression Model

**Fit the linear regression model** using the Ordinary Least Squares (OLS) method to determine the best-fit line.

```
X = sm.add_constant(data['x'])  # Adds an intercept term  
model = sm.OLS(data['y'], X).fit()    
data['y_pred'] = model.predict(X)  # Predicted values    
residuals = model.resid  # Residuals (errors)
```

#### Step 4. Check Assumptions

##### **Linearity**

* Does the relationship between advertising spend (xxx) and sales (yyy) appear linear?
* **Plot a scatterplot of the observed data** with the regression line to visually confirm linearity.

```
sns.scatterplot(x='x', y='y', data=data)    
plt.plot(data['x'], data['y_pred'], color='red', label='Regression Line')    
plt.title('Linearity Check: Scatterplot with Regression Line')    
plt.legend()  
plt.show()
```

**Output:**

![Scatterplot output of linearity check with regression](https://moringa.instructure.com/courses/1426/files/631854/download)

**Interpretation:** If the data points cluster closely around the regression line, the linearity assumption holds. Curves or systematic deviations indicate nonlinearity.

---

##### **Independence of Errors**

* Are the residuals randomly scattered, with no discernible patterns?
* **Create a Residuals vs. Fitted Values plot** to ensure no autocorrelation.

```
plt.scatter(data['y_pred'], residuals)    
plt.axhline(0, color='red', linestyle='--')    
plt.title('Residuals vs Fitted Values: Checking Independence of Errors')    
plt.xlabel('Fitted Values')    
plt.ylabel('Residuals')    
plt.show()
```

**Output:**

![Scatterplot output of residuals vs. fitted values.](https://moringa.instructure.com/courses/1426/files/631823/download)

**Interpretation:** If residuals are randomly distributed around zero with no patterns, the errors are independent. Clusters or trends may suggest autocorrelation.

---

##### **Normality of Errors**

* Do the residuals follow a normal distribution?
* **Use a Q-Q plot** to assess whether the residuals align with a normal distribution.

```
sm.qqplot(residuals, line='45')    
plt.title('Q-Q Plot for Normality of Residuals')    
plt.show()
```

**Output:**

![Q-Q plot output of normality of residuals.](https://moringa.instructure.com/courses/1426/files/631789/download)

**Interpretation:** If the residuals lie along the diagonal line in the Q-Q plot, the normality assumption is satisfied. Deviations at the tails suggest non-normality.

---

##### **Equal Variances (Homoscedasticity)**

* Is the variance of the residuals constant?
* **Plot the absolute residuals against the fitted values** to check for heteroscedasticity.

```
plt.scatter(data['y_pred'], np.abs(residuals))    
plt.title('Residuals vs Fitted Values: Checking Homoscedasticity')    
plt.xlabel('Fitted Values')    
plt.ylabel('Absolute Residuals')    
plt.show()
```

**Output:**

![Scatterplot outp checking homoscedasticity.](https://moringa.instructure.com/courses/1426/files/631852/download)

**Interpretation:** If the spread of residuals is constant across all fitted values, the assumption holds. A funnel or megaphone shape indicates heteroscedasticity.

#### Step 5. Interpret Results

At this stage, you review the diagnostics:

1. **Linearity:** The scatterplot should confirm a linear trend.
2. **Independence of Errors:** The residuals plot should show random scatter around zero.
3. **Normality of Errors:** The Q-Q plot should indicate normally distributed residuals.
4. **Equal Variances:** Residual spread should be consistent across all fitted values.

By carefully validating these assumptions, you ensure your advertising spend vs. sales model is reliable and robust. Imagine presenting a poorly validated model to the leadership team; it could lead to misallocated budgets and lost opportunities. By using diagnostic tools like scatterplots, residual plots, and Q-Q plots, you identify and address any violations early, building confidence in your predictions.

This workflow equips you, as a junior data scientist, to not only deliver accurate insights but also explain why your model works, making your analyses actionable and trustworthy.

### Common Challenges

1. **Non-linearity:** Curved patterns in the scatterplot suggest a nonlinear relationship.
   * **Solution:** Apply transformations (e.g., log or polynomial regression).
2. **Autocorrelation:** Patterns in residuals indicate dependence, common in time-series data.  
   * **Solution:** Use time-series models like ARIMA.
3. **Non-Normal Residuals:** Skewed or heavy-tailed residuals affect inference.  
   * **Solution:** Use robust regression or transformations.
4. **Heteroscedasticity:** Unequal variance can lead to unreliable confidence intervals.  
   * **Solution:** Apply weighted least squares or log transformations.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248826

Scraped At: 2026-05-15T10:29:06.786411
