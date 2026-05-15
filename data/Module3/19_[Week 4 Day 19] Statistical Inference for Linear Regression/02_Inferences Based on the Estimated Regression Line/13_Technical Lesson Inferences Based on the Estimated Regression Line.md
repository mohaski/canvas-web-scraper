# Technical Lesson: Inferences Based on the Estimated Regression Line

# Technical Lesson: Inferences Based on the Estimated Regression Line

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: Inferences Based on the Estimated Regression Line

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

This lesson focuses on confidence intervals for the mean *y* value and prediction intervals for a single *y* value, using the mtcars dataset to predict miles per gallon (mpg) based on horsepower (hp). Follow these steps to apply statistical inference and ensure the reliability of your predictions.

### Video: Lesson Guide

The video below will guide you through each step of this technical lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of inferences based on the estimated regression line.

[VIDEO LINK](https://player.vimeo.com/video/1061119530?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Resources

* We will use the "mtcars" dataset from the statsmodels library, which contains advertising expenditure data and corresponding sales figures. This dataset is a commonly used example for regression analysis.
* Jupyter Notebook and/or Integrated Development Environment (IDE) for Python like Colab VS Code.

### Instructions

#### Step 1. Import Required Libraries

**Action:** Import the libraries required for data manipulation, modeling, and visualization.

```
import pandas as pd  
import statsmodels.api as sm  
import matplotlib.pyplot as plt  
# Import the rdatasets package  
from rdatasets import data as rdata
```

#### Step 2. Load the Dataset

**Action:** Load the mtcars dataset and inspect its structure.

```
data = sm.datasets.get_rdataset("mtcars", "datasets").data  
  
# Display dataset information  
print(data.info())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>  
Index: 32 entries, Mazda RX4 to Volvo 142E  
Data columns (total 11 columns):  
 #   Column  Non-Null Count  Dtype    
---  ------  --------------  -----    
 0   mpg     32 non-null     float64  
 1   cyl     32 non-null     int64    
 2   disp    32 non-null     float64  
 3   hp      32 non-null     int64    
 4   drat    32 non-null     float64  
 5   wt      32 non-null     float64  
 6   qsec    32 non-null     float64  
 7   vs      32 non-null     int64    
 8   am      32 non-null     int64    
 9   gear    32 non-null     int64    
 10  carb    32 non-null     int64    
dtypes: float64(5), int64(6)  
memory usage: 3.0+ KB  
None
```

**Decision Point:** Confirm that the dataset contains numeric columns suitable for regression.

#### Step 3. Define the Variables

**Action:** Define the independent variable ($x$) as horsepower (hp) and the dependent variable ($y$) as miles per gallon (mpg).

```
X = sm.add_constant(data['hp'])  # Add constant for intercept  
y = data['mpg']  
  
# Ensure that X and y have consistent dimensions  
print(f"X shape: {X.shape}, y shape: {y.shape}")
```

**Output:**

```
X shape: (32, 2), y shape: (32,)
```

#### Step 4. Fit the Linear Regression Model

**Action:** Use Ordinary Least Squares (OLS) to fit the regression model.

```
# Fit the regression model  
model = sm.OLS(y, X).fit()  
  
# Print the model summary  
print(model.summary())
```

**Output:**

```
 OLS Regression Results                              
==============================================================================  
Dep. Variable:                    mpg   R-squared:                       0.602  
Model:                            OLS   Adj. R-squared:                  0.589  
Method:                 Least Squares   F-statistic:                     45.46  
Date:                Mon, 16 Dec 2024   Prob (F-statistic):           1.79e-07  
Time:                        22:01:16   Log-Likelihood:                -87.619  
No. Observations:                  32   AIC:                             179.2  
Df Residuals:                      30   BIC:                             182.2  
Df Model:                           1                                           
Covariance Type:            nonrobust                                           
==============================================================================  
                 coef    std err          t      P>|t|      [0.025      0.975]  
------------------------------------------------------------------------------  
const         30.0989      1.634     18.421      0.000      26.762      33.436  
hp            -0.0682      0.010     -6.742      0.000      -0.089      -0.048  
==============================================================================  
Omnibus:                        3.692   Durbin-Watson:                   1.134  
Prob(Omnibus):                  0.158   Jarque-Bera (JB):                2.984  
Skew:                           0.747   Prob(JB):                        0.225  
Kurtosis:                       2.935   Cond. No.                         386.  
==============================================================================  
  
Notes:  
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

#### Step 5. Calculate Confidence Interval for Mean ![y](https://learning.flatironschool.com/equation\_images/y?scale=0.875) Value

**Action:** For a specific horsepower value, calculate the confidence interval for the mean predicted mpg.

```
# Define the target horsepower value  
target_hp = 150  
# Create a DataFrame with the target horsepower and add a constant term  
target_X = pd.DataFrame({'hp': [target_hp]})  
target_X = sm.add_constant(target_X, has_constant='add')  # Explicitly add constant  
  
# Get the confidence interval for the mean predicted value  
mean_prediction = model.get_prediction(target_X).summary_frame(alpha=0.05)  
print(mean_prediction[['mean', 'mean_ci_lower', 'mean_ci_upper']])
```

**Output:**

```
 mean  mean_ci_lower  mean_ci_upper  
0  19.864619      18.468309      21.260928
```

#### Step 6. Calculate Prediction Interval for a Single *y* Value

**Action:** For the same horsepower value, calculate the prediction interval for the mpg of an individual car.

```
# Get the prediction interval for an individual observation  
prediction = model.get_prediction(target_X).summary_frame(alpha=0.05)  
print(prediction[['mean', 'obs_ci_lower', 'obs_ci_upper']])
```

**Output:**

```
mean  obs_ci_lower  obs_ci_upper  
0  19.864619     11.852784     27.876453
```

**Interpretation:** The prediction interval accounts for variability in individual cars, resulting in a broader range than the confidence interval.

**Important Note:** In the Example

1. **Confidence Interval for the Mean *y* Value:** The range (18.47 to 21.26) reflects the uncertainty in predicting the average mpg for cars with 150 horsepower.
2. **Prediction Interval for a Single *y* Value:** The range (11.85 to 27.88) is much wider because it accounts for the additional variability of an individual car's mpg around the regression line.

The confidence interval is narrower because it estimates the mean response, which has less variability compared to individual outcomes. The prediction interval is wider because it incorporates not only the uncertainty in the mean prediction but also the inherent randomness in individual observations. This distinction is always the case and essential in data science for interpreting predictions, whether you are predicting group-level trends (confidence interval) or individual outcomes (prediction interval).

#### Step 7. Visualize the Results

**Action:** Plot the scatter plot with the regression line side-by-side for each type of interval

```
#Scatterplot with confidence intervals  
axes[0].scatter(data['hp'], data['mpg'], label='Data', color='blue', alpha=0.7)  
axes[0].plot(data['hp'], data['Predicted_mpg'], color='red', label='Regression Line')  
axes[0].fill_between(data['hp'], data['mean_ci_lower'], data['mean_ci_upper'], color='gray', alpha=0.3, label='Confidence Interval (Mean)')  
axes[0].set_title('Confidence Intervals for the Mean')  
axes[0].set_xlabel('Horsepower (hp)')  
axes[0].set_ylabel('Miles Per Gallon (mpg)')  
axes[0].legend()  
  
  
# Scatterplot with prediction intervals  
axes[1].scatter(data['hp'], data['mpg'], label='Data', color='blue', alpha=0.7)  
axes[1].plot(data['hp'], data['Predicted_mpg'], color='red', label='Regression Line')  
axes[1].fill_between(data['hp'], data['obs_ci_lower'], data['obs_ci_upper'], color='orange', alpha=0.3, label='Prediction Interval')  
axes[1].set_title('Prediction Intervals for a Single Observation')  
axes[1].set_xlabel('Horsepower (hp)')  
axes[1].legend()  
  
  
plt.tight_layout()  
plt.show()
```

**Output:**

![Plot outputs for confidence and prediction intervals.](https://moringa.instructure.com/courses/1426/files/631889/download)

Again, we can see how the prediction intervals are wider than the confidence intervals.

#### Panel 8: Interpret Results

**Action:** Summarize the findings for stakeholders.

* **Confidence Interval:** Provides the range of plausible average mpg values for cars with 150 horsepower.
* **Prediction Interval:** Accounts for individual variability, offering a broader range for the mpg of a specific car.
* **Key Takeaway:** Confidence intervals are for group-level predictions, while prediction intervals address individual cases.

### Considerations

1. Clarify the distinction between confidence and prediction intervals.
2. Ensure linear regression assumptions are validated for accurate results.
3. Identify and handle outliers or influential data points to maintain model reliability.
4. Avoid extrapolating predictions beyond the range of observed *x* values.
5. Effectively communicate the results to stakeholders using both text and visualizations.

By addressing these considerations, you will develop a more rigorous understanding of statistical inferences, ensuring your predictions are both accurate and actionable in a data science context.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248844

Scraped At: 2026-05-15T10:31:22.055778
