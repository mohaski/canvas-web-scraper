# Example: Assumptions of Linear Regression

# Example: Assumptions of Linear Regression

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Example: Assumptions of Linear Regression

Icon Progress Bar (browser only)

3 min read

As a junior data scientist tasked with predicting weekly sales (*y*) based on advertising spend (*x*), validating the assumptions of linear regression is essential to ensure the model’s reliability and accuracy. Below is an explanation of the four assumptions with specific examples related to this task.

### Linearity

The relationship between advertising spend and sales must follow a straight-line trend.

* **For example**, when plotting advertising spend (*x*) against weekly sales (*y*), the scatterplot shows a clear upward linear relationship. The points closely cluster around the regression line, indicating that a linear model is appropriate.

**Why It Matters:** If the relationship is nonlinear, such as a curved trend where high advertising spend has diminishing returns on sales, the model will not capture the true relationship, leading to inaccurate predictions.

### Independence of Errors

Residuals (
![e Subscript i](https://learning.flatironschool.com/equation\_images/e\_i?scale=1)
​), the differences between observed and predicted sales, must not show systematic patterns relative to the fitted values.

* **For example**, in a Residuals vs. Fitted Values plot, the residuals appear randomly scattered around zero, with no waves, clusters, or cycles. This suggests the residuals are independent.

**Why It Matters:** If the errors were dependent, such as showing periodic spikes (e.g., seasonal sales trends), the model would violate the independence assumption. This could lead to biased standard errors and overly optimistic confidence intervals, particularly in time-sensitive predictions.

### Normality of Errors

Residuals should follow an approximately normal distribution.

* **For instance,** the histogram of residuals for this model shows a bell-shaped curve, and a Q-Q plot confirms that the residuals align closely with the diagonal line. This indicates that the residuals are approximately normally distributed around zero.

**Why It Matters:** If residuals were skewed (e.g., extremely high or low sales due to outliers or rare promotions), the p-values and confidence intervals would be invalid, undermining the credibility of the model's results.

### Equal Variances (Homoscedasticity)

Residuals should have consistent variance across all levels of advertising spend.

* In the Residuals vs. Fitted Values plot, the residuals for this model have a uniform spread around zero without showing funnel or bowtie shapes.

**Why It Matters:** If residuals had unequal variance (e.g., higher variability at higher advertising spend levels), the model would provide less reliable predictions for extreme budgets, potentially misguiding the allocation of marketing resources.

### Outcome

By validating all four assumptions:

1. **Linearity:** The scatterplot shows a linear trend between advertising spend and sales.
2. **Independence:** Residuals vs. Fitted Values plot reveals random scatter, confirming independence.
3. **Normality:** Histogram and Q-Q plot confirm that residuals are approximately normally distributed.
4. **Equal Variances:** Residuals vs. Fitted Values plot shows constant variance across advertising levels.

The regression model can now reliably predict weekly sales based on advertising spend. This validation ensures the business can confidently allocate advertising budgets to optimize sales and improve ROI. By thoroughly checking assumptions, the junior data scientist ensures actionable and trustworthy results, earning credibility within the organization.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248823

Scraped At: 2026-05-15T10:28:50.574700
