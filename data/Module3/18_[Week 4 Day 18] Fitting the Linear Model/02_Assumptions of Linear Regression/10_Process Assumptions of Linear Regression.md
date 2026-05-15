# Process: Assumptions of Linear Regression

# Process: Assumptions of Linear Regression

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Process: Assumptions of Linear Regression

Icon Progress Bar (browser only)

2 min read

1. **Plot the Scatterplot to Check Linearity:** Examine if the relationship between *x* and *y* is linear.
2. **Generate the Residuals vs. Fits Plot:** Verify the independence of residuals and assess homoscedasticity.
3. **Create a Histogram and Q-Q Plot for Residuals:** Check if residuals are approximately normally distributed.
4. **Interpret the Residual Spread:** Assess whether the variance of residuals remains constant across fitted values.
5. **Address Violations:** If violations occur, consider:

* **Nonlinearity:** Use transformations (e.g., log, polynomial regression).
* **Autocorrelation:** Use time-series models like ARIMA.
* **Heteroscedasticity:** Apply weighted least squares or robust regression.

### Conceptualize Assumptions of Linear Regression

Conceptualization Table for Assumptions of Linear Regression

| Assumption | Tool | Python Function | Check |
| --- | --- | --- | --- |
| Linearity | Scatterplot of *x* vs. *y* | `sns.scatterplot()` and `plt.plot()` | Data points should show a linear trend.  Curved or clustered patterns suggest nonlinearity. |
| Independence of Errors | Residuals vs. Fits plot | `plt.scatter()` | Residuals should display random scatter without patterns.  Serial correlation indicates dependence. |
| Normality of Errors | Histogram of residuals and Q-Q plot | `plt.hist()` and `sm.qqplot()` | Residuals should approximate a normal distribution and align with the diagonal in the Q-Q plot. |
| Equal Variances (Homoscedasticity) | Residuals vs. Fits plot | `plt.scatter()` | Residual spread should be consistent across all values of *x*.  Funnel or bowtie shapes indicate heteroscedasticity. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248824

Scraped At: 2026-05-15T10:28:55.462552
