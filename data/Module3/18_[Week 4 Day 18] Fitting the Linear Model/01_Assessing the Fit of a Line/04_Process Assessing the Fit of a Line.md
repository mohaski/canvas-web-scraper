# Process: Assessing the Fit of a Line

# Process: Assessing the Fit of a Line

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Process: Assessing the Fit of a Line

Icon Progress Bar (browser only)

2 min read

Review the following process for assessing the fit of a line:

1. **Verify Data Suitability:** Ensure the data consists of two quantitative/numeric variables suitable for simple linear regression. Confirm there is no major violation of assumptions, such as extreme outliers or a non-linear relationship.
2. **Define the Variables:** Identify the independent variable (*x*) and dependent variable (*y*), clarifying their roles in the analysis.
3. **Scatterplot:** Visualize the relationship to detect trends and assess linearity.
4. **Compute the Regression Line and *r*:** If the scatterplot suggests linearity, calculate the regression line (
   ![ModifyingAbove y With caret equals b 0 plus b 1 x](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1x?scale=1)
   ) and correlation coefficient (*r*).
5. **Compute
   ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
   :** Quantify the model’s explanatory power.
6. **Analyze Residuals:** Check for randomness and adherence to assumptions.
7. **Identify Influential Observations:** Use Cook’s Distance or leverage statistics.
8. **Refine the Model:** Address violations or outliers to improve fit.
9. **Interpret Results:** Report on steps 3 - 8 for actionable insights.

### Conceptualize Assessing the Fit of a Line

Conceptualization Table for Assessing the Fit of a Line

| Term | Definition | Example |
| --- | --- | --- |
| Coefficient of Determination ( ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=0.875) ) | Proportion of variance in the dependent variable explained by the independent variable. | An ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=0.875)  of 0.85 means 85% of the variability in sales is explained by advertising spend. |
| Residuals | Differences between observed and predicted values. | If the observed value is 100 and the predicted value is 95, the residual is 5. |
| Residual Plot | Scatterplot of residuals used to detect assumption violations. | A residual plot shows random scatter if the model assumptions are met. |
| Influential Values | Data points that disproportionately affect the regression line. | Cook’s Distance identifies a single outlier that shifts the slope of the regression significantly. |
| Outliers | Observations that deviate significantly from the regression line. | A point far from the regression line on a scatterplot is flagged as an outlier |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248817

Scraped At: 2026-05-15T10:28:16.964691
