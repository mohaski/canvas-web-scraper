# Technical Lesson: Multiple Linear Regression

# Technical Lesson: Multiple Linear Regression

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: Multiple Linear Regression

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In this lesson, you will learn how to implement Multiple Linear Regression to analyze the relationship between a dependent variable and multiple independent variables. Specifically, we will use the galapagos dataset from the faraway package, which provides ecological data for islands in the Galapagos archipelago.

The goal is to predict the number of plant species (Species) on each island using key ecological factors:

* **Area:** The size of the island (in square kilometers).
* **Elevation:** The highest point on the island (in meters).
* **Nearest:** The distance to the nearest island (in kilometers).

As a junior data scientist, you may often be tasked with identifying the key factors that influence a particular outcome, such as predicting ecological patterns, forecasting sales, or analyzing customer behavior.

This example will guide you step-by-step to:

1. **Build a multiple linear regression model** that includes multiple predictors (independent variables).
2. **Interpret the model output**, including coefficients, p-values, and
   ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
   , to understand which predictors significantly impact the response variable.
3. **Diagnose the model** to ensure its assumptions (linearity, independence, normality, and equal variance) are satisfied.
4. **Make predictions** for new scenarios, applying the model to unseen data.

### Video: Technical Lesson Guide

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of multiple linear regression.

[VIDEO LINK](https://player.vimeo.com/video/1061119301?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

#### Step 1. Import Libraries and Load the Dataset

**Action:**

* **Import necessary libraries** for data manipulation, analysis, and modeling.
* **Load the galapagos dataset** and inspect its structure.

```
# ! pip install faraway  
  
# packages  
  
  
import pandas as pd  
import statsmodels.api as sm  
import matplotlib.pyplot as plt  
import seaborn as sns  
from faraway.datasets import galapagos  
  
  
# Load the galapagos dataset  
data = galapagos.load()  
  
  
# Display the first few rows  
print(data.head())  
  
  
# Display the column names and data types  
print(data.info())
```

**Output:**

```
     Species   Area  Elevation  Nearest  Scruz  Adjacent  
Baltra          58  25.09        346      0.6    0.6      1.84  
Bartolome       31   1.24        109      0.6   26.3    572.33  
Caldwell         3   0.21        114      2.8   58.7      0.78  
Champion        25   0.10         46      1.9   47.4      0.18  
Coamano          2   0.05         77      1.9    1.9    903.82  
<class 'pandas.core.frame.DataFrame'>  
Index: 30 entries, Baltra to Wolf  
Data columns (total 6 columns):  
 #   Column     Non-Null Count  Dtype    
---  ------     --------------  -----    
 0   Species    30 non-null     int64    
 1   Area       30 non-null     float64  
 2   Elevation  30 non-null     int64    
 3   Nearest    30 non-null     float64  
 4   Scruz      30 non-null     float64  
 5   Adjacent   30 non-null     float64  
dtypes: float64(4), int64(2)  
memory usage: 1.6+ KB  
None
```

#### Step 2. Define the Variables

**Action:**

* Identify the dependent variable (*y*) and independent variables (
  ![x 1 comma x 2 comma ellipsis comma x Subscript p Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520x\_2%252C%2520%255Cdots%252C%2520x\_p?scale=1)
  ).  
  + **Dependent Variable:** Species (number of plant species on the island).
  + **Independent Variables:** Area, Elevation, and Nearest.
* Prepare the variables for regression.

```
# Define the independent variables (predictors) and add a constant  
X = data[['Area', 'Elevation', 'Nearest']]  
X = sm.add_constant(X)  # Adds a constant for the intercept  
  
# Define the dependent variable  
y = data['Species']  
  
# Verify the shapes of X and y  
print(X.shape, y.shape)
```

**Output:**

```
(30, 4) (30,)
```

#### Step 3. Fit the Multiple Linear Regression Model

**Action:** Use the **statsmodels library** to fit the regression model.

```
# Fit the Multiple Linear Regression model  
model = sm.OLS(y, X).fit()  
  
# Print the model summary  
print(model.summary())
```

**Output:**

```
  OLS Regression Results                              
==============================================================================  
Dep. Variable:                Species   R-squared:                       0.554  
Model:                            OLS   Adj. R-squared:                  0.503  
Method:                 Least Squares   F-statistic:                     10.77  
Date:                Tue, 17 Dec 2024   Prob (F-statistic):           8.82e-05  
Time:                        14:36:26   Log-Likelihood:                -172.20  
No. Observations:                  30   AIC:                             352.4  
Df Residuals:                      26   BIC:                             358.0  
Df Model:                           3                                           
Covariance Type:            nonrobust                                           
==============================================================================  
                 coef    std err          t      P>|t|      [0.025      0.975]  
------------------------------------------------------------------------------  
const         16.4647     23.389      0.704      0.488     -31.612      64.541  
Area           0.0191      0.027      0.713      0.482      -0.036       0.074  
Elevation      0.1713      0.055      3.143      0.004       0.059       0.283  
Nearest        0.0712      1.065      0.067      0.947      -2.118       2.260  
==============================================================================  
Omnibus:                       18.125   Durbin-Watson:                   1.901  
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               30.695  
Skew:                           1.280   Prob(JB):                     2.16e-07  
Kurtosis:                       7.243   Cond. No.                     1.57e+03  
==============================================================================  
  
Notes:  
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.  
[2] The condition number is large, 1.57e+03. This might indicate that there are  
strong multicollinearity or other numerical problems.
```

##### **Analyze the Model Output**

**Action:** Review the key results from the model summary.

###### **Model Performance**

* **Adjusted
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  : 0.503**  
  + Adjusted
    ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
    accounts for the number of predictors in the model, penalizing unnecessary predictors.
  + While
    ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
    indicates that 55.4% of the variation in Species is explained by the model, the Adjusted
    ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
    of 0.503 suggests that some predictors may not add significant value and the model explains about 50.3% of the variability after accounting for the number of predictors.
* **F-statistic: 10.77 (p-value = 8.82e-05)**  
  + The F-statistic tests the overall significance of the model. A small p-value (< 0.05) indicates that the predictors, as a group, explain a statistically significant proportion of the variability in Species.

###### **Analysis of Coefficients**

Analysis of Coefficients

| Predictor | Coefficient (*b*) | Std Error | t-statistic | p-value | 95% Confidence Interval | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Intercept | 16.4647 | 23.389 | 0.704 | 0.488 | (-31.612, 64.541) | Baseline value for Species when all predictors are 0. Not significant. |
| Area | 0.0191 | 0.027 | 0.713 | 0.482 | (-0.036, 0.074) | Area has a small positive relationship with Species, but is not statistically significant. |
| Elevation | 0.1713 | 0.055 | 3.143 | 0.004 | (0.059, 0.283) | Elevation is statistically significant. For every 1-unit increase in elevation, the number of species increases by 0.1713. |
| Nearest | 0.0712 | 1.065 | 0.067 | 0.947 | (-2.118, 2.260) | Distance to the nearest island has no significant effect on the number of species. |

###### **Key Takeaways:**

* **Elevation** is the only statistically significant predictor (
  ![p equals 0.004](https://learning.flatironschool.com/equation\_images/p%2520%253D%25200.004?scale=1)
  ), indicating that islands with higher elevation tend to have more plant species.
* **Area and Nearest** are not significant (
  ![p greater than 0.05](https://learning.flatironschool.com/equation\_images/p%2520%253E%25200.05?scale=1)
  ), suggesting they do not explain the variation in Species after accounting for Elevation.

#### Step 4. Check for Multicollinearity

##### Part A: Check for Multicollinearity

* **Action:** Check for multicollinearity among predictors to ensure they are not highly correlated.

```
# Calculate the correlation matrix  
correlation_matrix = data[['Area', 'Elevation', 'Nearest']].corr()  
print(correlation_matrix)  
  
# Visualize the correlation matrix  
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')  
plt.title('Correlation Matrix of Predictors')  
plt.show()
```

* **Output:**

```
              Area  Elevation   Nearest  
Area       1.000000   0.753735 -0.111103  
Elevation  0.753735   1.000000 -0.011077  
Nearest   -0.111103  -0.011077  1.000000
```

![Correlation matrix output of predictors](https://moringa.instructure.com/courses/1426/files/631850/download)

The correlation matrix and corresponding heatmap above summarize the relationships between the predictor variables: Area, Elevation, and Nearest.

Here is the detailed breakdown and interpretation.

###### **What is a Correlation Matrix?**

A correlation matrix is a table that shows the Pearson correlation coefficients between pairs of variables. Each value ranges between -1 and +1:

* **+1:** Perfect positive correlation.
* **-1:** Perfect negative correlation.
* **0:** No linear relationship.

In this table:

* The diagonal values are 1, as each variable is perfectly correlated with itself.
* Off-diagonal values show the pairwise correlations between predictors.

###### **What is the Heatmap?**

The heatmap is a visual representation of the correlation matrix.

**Colors** represent the magnitude and direction of the correlation:

* **Red:** Strong positive correlation (close to +1).
* **Blue:** Negative correlation (close to -1).
* **Lighter shades:** Weak or no correlation.

**Numeric values** within the heatmap provide the exact correlation coefficients.

###### **Interpreting the Results**

Results Interpretation

| Variable Pair | Correlation Coefficient | Interpretation |
| --- | --- | --- |
| Area & Elevation | 0.75 | Strong positive correlation: As Area increases, Elevation also tends to increase. |
| Area & Nearest | -0.11 | Weak negative correlation: Area and Nearest are almost uncorrelated. |
| Elevation & Nearest | -0.01 | Very weak negative correlation: Essentially no relationship. |

##### Key Observations:

1. **Area and Elevation (0.75):**  
   * There is a strong positive correlation between Area and Elevation.
   * This could indicate multicollinearity, as these two predictors share significant linear relationships.
   * Multicollinearity inflates standard errors, making it harder to determine the independent effect of each predictor.
2. **Area and Nearest (-0.11):**  
   * There is a weak negative correlation, which suggests these two predictors do not influence each other strongly.
3. **Elevation and Nearest (-0.01):**  
   * These variables are almost uncorrelated, meaning changes in Elevation have no linear relationship with Nearest.

##### Why Multicollinearity is a Concern

The strong correlation (0.75) between Area and Elevation suggests potential multicollinearity:

* Multicollinearity occurs when predictor variables are highly correlated.
* It inflates the variance of the regression coefficients, leading to:  
  + Unstable estimates for the coefficients.
  + Increased standard errors.
  + Difficulty determining which predictor is significant.

##### Part B: Check for Multicollinearity Using VIF

To further investigate the multicollinearity observed between Area and Elevation in Step 5a, we will compute the Variance Inflation Factor (VIF) for each predictor.

##### What is VIF?

The **Variance Inflation Factor (VIF)** measures how much the variance of a regression coefficient is inflated due to multicollinearity with other predictors. Specifically:

![VIF Subscript j Baseline equals StartFraction 1 Over 1 minus upper R Subscript j Superscript 2 Baseline EndFraction](https://learning.flatironschool.com/equation\_images/%255Ctext%257BVIF%257D\_j%2520%253D%2520%255Cfrac%257B1%257D%257B1%2520-%2520R\_j%255E2%257D?scale=1)

Where:

* ![upper R Subscript j Superscript 2](https://learning.flatironschool.com/equation\_images/R\_j%255E2?scale=1)
  is the
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  value obtained when predictor
  ![x Subscript j](https://learning.flatironschool.com/equation\_images/x\_j?scale=1)
  ​ is regressed on all other predictors.
* A higher
  ![upper R Subscript j Superscript 2](https://learning.flatironschool.com/equation\_images/R\_j%255E2?scale=1)
  ​ means stronger multicollinearity.

Interpreting VIF:

* **VIF = 1:** No multicollinearity.
* **VIF between 1 and 5:** Moderate multicollinearity.
* **VIF > 5:** High multicollinearity, which should be addressed.
* **VIF > 10:** Severe multicollinearity; predictors are highly redundant.

```
from statsmodels.stats.outliers_influence import variance_inflation_factor  
  
# Define predictors (excluding the dependent variable 'Species')  
X = data[['Area', 'Elevation', 'Nearest']]  
X = sm.add_constant(X)  # Add constant for intercept  
  
# Calculate VIF for each predictor  
vif_data = pd.DataFrame()  
vif_data['Variable'] = X.columns  
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]  
  
print(vif_data)
```

**Output:**

```
   Variable       VIF  
0      const  2.511156  
1       Area  2.373470  
2  Elevation  2.344460  
3    Nearest  1.025189
```

###### **Analysis of Each Predictor**

1. **Area (VIF = 2.37) and Elevation (VIF = 2.34):**  
   * Both predictors show low to moderate multicollinearity (VIF < 5).
   * This indicates that Area and Elevation are correlated, which aligns with the correlation matrix results where their correlation was 0.75.
   * While not severe, the moderate multicollinearity could slightly inflate the standard errors of their coefficients. However, it is still within an acceptable range, so no immediate corrective action is needed.
2. **Nearest (VIF = 1.03):**  
   * This variable has a very low VIF, indicating no multicollinearity with the other predictors.
   * It can be confidently included in the model without concerns of redundancy.
3. **Constant Term (const, VIF = 2.51):**  
   * The intercept has a moderate VIF value. This is typical and does not directly impact the interpretation of the predictor variables. It simply reflects the scaling and centering of the predictors.

The **VIF values for all predictors are below 5**, meaning that multicollinearity is not severe and does not pose a significant threat to the regression model.

While **Area and Elevation are moderately correlated**, they can remain in the model unless further analysis reveals problems (e.g., inflated p-values or large standard errors).

**No predictor has a VIF > 10,** so the model does not suffer from severe redundancy among predictors.

#### Step 5. Visualize Residuals

**Action:** Check for assumptions of the model by plotting residuals.

1. **Residuals vs. Fitted Plot:** To assess homoscedasticity (constant variance of residuals).
2. **Histogram of Residuals:** To assess normality of residuals.

```
import matplotlib.pyplot as plt  
  
  
# Get the residuals  
residuals = model.resid  
  
  
# Create a 2x1 grid for the plots  
fig, axes = plt.subplots(1, 2, figsize=(8, 10))  # 2 rows, 1 column  
  
  
# Plot 1: Residuals vs Fitted Values  
axes[0].scatter(model.fittedvalues, residuals, color='blue')  
axes[0].axhline(0, color='red', linestyle='--')  
axes[0].set_title('Residuals vs Fitted Values')  
axes[0].set_xlabel('Fitted Values')  
axes[0].set_ylabel('Residuals')  
  
  
# Plot 2: Histogram of Residuals  
axes[1].hist(residuals, bins=10, edgecolor='black')  
axes[1].set_title('Histogram of Residuals')  
axes[1].set_xlabel('Residuals')  
axes[1].set_ylabel('Frequency')  
  
  
# Adjust layout  
plt.tight_layout()  
  
  
# Show the plots  
plt.show()
```

**Output:**

![Side-by-side output of Residuals vs Fitted Values scatterplot and Histogram of Residuals.](https://moringa.instructure.com/courses/1426/files/631776/download)

##### Residuals vs. Fitted Values Plot (Left)

**Purpose:** This plot is used to assess the assumption of homoscedasticity (constant variance of residuals) and check for any patterns in residuals.

**Analysis:**

* In the plot, the residuals appear scattered unevenly around the red horizontal line at zero, with a few noticeable outliers far from the center.
* There is a concentration of residuals near lower fitted values and larger spread in higher fitted values. This suggests possible heteroscedasticity (non-constant variance).
* A few points are significantly distant from the zero line, which may indicate outliers or influential observations that could disproportionately affect the regression results.

**Conclusion:** The lack of even scatter and potential funneling of residuals indicates a violation of the homoscedasticity assumption, which should be addressed through further diagnostics, transformations, or robust regression methods.

##### Histogram of Residuals (Right)

**Purpose:** This histogram checks whether the residuals are approximately normally distributed, which is essential for valid statistical inferences (e.g., hypothesis tests, confidence intervals).

**Analysis:**

* The histogram of residuals is not perfectly symmetric and exhibits a right-skewed distribution, with a notable cluster of residuals near zero and some extreme residuals at both ends.
* This deviation from normality suggests that the residuals are not centered around zero in a bell-curve shape, which violates the normality of residuals assumption.

**Conclusion:** Non-normal residuals indicate that the regression model may not fully capture the variability in the data, potentially leading to inaccurate p-values or confidence intervals.

#### Step 6. Make Predictions

**Action:** Use the model to predict the number of plant species for new islands with given ecological features.

```
# Define new data for prediction  
new_data = pd.DataFrame({'const': [1], 'Area': [10], 'Elevation': [100], 'Nearest': [1.5]})  
  
# Predict the number of species  
prediction = model.predict(new_data)  
print(f"Predicted number of species: {prediction[0]:.2f}")
```

**Output:**

```
Predicted number of species: 33.90
```

* The model estimates the number of species using the fitted regression equation:  
  ![y With caret equals b 0 plus b 1 dot Area plus b 2 dot Elevation plus b 3 dot Nearest](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1%2520%255Ccdot%2520%255Ctext%257BArea%257D%2520%252B%2520b\_2%2520%255Ccdot%2520%255Ctext%257BElevation%257D%2520%252B%2520b\_3%2520%255Ccdot%2520%255Ctext%257BNearest%257D?scale=1)
* So when the above values are substituted in as in the code, then the output 33.90.

### Summary of Findings

Key Insights from the Multiple Linear Regression Analysis on the Galapagos Dataset:

1. **Model Performance:**

* The model explains approximately 55.4% of the variation in the number of species based on the predictors (Area, Elevation, Nearest).
* Adjusted
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  is 0.503, accounting for the number of predictors and indicating the model’s performance after penalizing unnecessary predictors.

1. **Significant Predictor** among the predictors:

* Elevation has a statistically significant positive effect (
  ![p equals 0.004](https://learning.flatironschool.com/equation\_images/p%2520%253D%25200.004?scale=1)
  ). For every unit increase in Elevation, the number of species increases by approximately 0.17.
* Area and Nearest are not significant (
  ![p greater than 0.05](https://learning.flatironschool.com/equation\_images/p%2520%253E%25200.05?scale=1)
  ), meaning they do not contribute meaningfully to predicting the number of species after considering Elevation.

1. **Multicollinearity:**

* Correlation analysis showed a strong relationship (
  ![r equals 0.75](https://learning.flatironschool.com/equation\_images/r%2520%253D%25200.75?scale=1)
  ) between Area and Elevation.
* VIF values for Area (2.37) and Elevation (2.34) confirmed moderate multicollinearity but within acceptable limits (
  ![VIF less than 5](https://learning.flatironschool.com/equation\_images/%255Ctext%257BVIF%257D%2520%253C%25205?scale=1)
  ).

1. **Residual Diagnostics:**

* **Residuals vs. Fitted Plot:** Indications of heteroscedasticity were observed, as the residuals are unevenly scattered, particularly at higher fitted values.
* **Histogram of Residuals**: Residuals are right-skewed and deviate from normality, which may affect the validity of statistical inferences.

1. **Prediction:**

* Using the model, we predicted that a new island with an **Area = 10, Elevation = 100, and Nearest = 1.5 will have approximately 33.90 species.**
* This prediction is based on the fitted regression equation and is a useful estimate for ecological planning or prioritizing islands for conservation.

#### Final Recommendations

While Elevation is significant and useful for predictions, the lack of normality and heteroscedasticity in residuals suggests that improvements can be made to the model.

##### **Next Steps:**

* Address heteroscedasticity by transforming predictors or responses (e.g., log transformation).
* Investigate the inclusion of other ecological variables that may better explain species richness.
* Consider robust regression methods if influential outliers persist.

By summarizing these findings, you can see how to assess model results critically, identify limitations, and propose actionable improvements in real-world data science workflows.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248855

Scraped At: 2026-05-15T10:32:47.956180
