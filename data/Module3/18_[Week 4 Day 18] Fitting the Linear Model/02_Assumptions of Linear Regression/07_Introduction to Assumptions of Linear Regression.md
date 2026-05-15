# Introduction to Assumptions of Linear Regression

# Introduction to Assumptions of Linear Regression

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Introduction to Assumptions of Linear Regression

Icon Progress Bar (browser only)

3 min read

As a junior data scientist, ensuring that your linear regression model meets its core assumptions is a critical step before drawing insights or making predictions.

There are four essential assumptions:

* linearity
* independence of errors
* normality of errors
* equal variances

These assumptions are the backbone of linear regression analysis. If any of these assumptions are violated, the model may produce biased or misleading results, leading to poor decision-making in real-world scenarios.

Imagine you are analyzing the impact of advertising spend on weekly sales for a retail company. A failure to validate assumptions might lead to predictions that are either systematically biased (nonlinearity) or overly optimistic (heteroscedasticity). By using visual diagnostic tools like scatterplots, residual plots, histograms, and Q-Q plots, you can quickly identify issues and take corrective action to improve the model’s reliability and accuracy.

### The Essential Assumptions

This section explores each assumption in detail, explaining its importance, what can go wrong if violated, and how to diagnose and address potential issues.

* **1. Linearity: The Relationship Between *x* and *y* Must Be Linear**

Linearity ensures that the relationship between the independent variable (*x*) and the dependent variable (*y*) can be described by a straight line. If this assumption is violated (e.g., the data follows a curve), the model will not capture the true relationship, leading to biased predictions and systematic errors. This can be diagnosed using a scatterplot with the regression line overlaid to check for a linear trend.

* **2. Independence of Errors: Residuals Must Be Independent**

Independence of errors means that the residuals (eie\_iei​) are not correlated with each other or with the independent variable (*x*). If the errors show patterns or trends (e.g., in time-series data), it may indicate autocorrelation, which can invalidate confidence intervals and p-values. A Residuals vs. Fitted Values plot is typically used to check for randomness in residuals.

* **3. Normality of Errors: Residuals Should Follow a Normal Distribution**

The normality assumption states that residuals (
![e Subscript i](https://learning.flatironschool.com/equation\_images/e\_i?scale=1)
​) should be approximately normally distributed around zero. This assumption is important for making reliable statistical inferences, such as accurate hypothesis tests, p-values, and confidence intervals. A Histogram of Residuals and a Q-Q Plot are used to assess whether residuals align with a normal distribution.

* **4. Equal Variances (Homoscedasticity): Residuals Should Have Constant Variance**

Homoscedasticity requires that the variance of residuals remains constant across all levels of *x*. If the spread of residuals increases or decreases systematically (heteroscedasticity), predictions for certain ranges of *x* will be unreliable, and standard errors will be inaccurate. This can be detected using a Residuals vs. Fitted Values plot, where consistent spread indicates homoscedasticity, and funnel-like patterns suggest violations.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248821

Scraped At: 2026-05-15T10:28:38.243030
