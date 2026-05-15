# Technical Lesson: Statistical Inference on the Slope

# Technical Lesson: Statistical Inference on the Slope

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: Statistical Inference on the Slope

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In regression analysis, understanding and validating the relationship between an independent variable (*x*) and a dependent variable (*y*) is critical for making accurate predictions and informed decisions. This lesson focuses on statistical inference on the slope, a process that evaluates whether the slope (
![b 1](https://learning.flatironschool.com/equation\_images/b\_1?scale=1)
​) is statistically significant and quantifies the uncertainty surrounding its value.

To guide you through this process, we will use the mtcars dataset, predicting miles per gallon (mpg) based on horsepower (hp). This practical example demonstrates how to apply hypothesis tests and confidence intervals to assess the reliability of your regression model.

### Why Perform a Hypothesis Test?

The hypothesis test ensures that the relationship between *x* (horsepower) and *y* (mpg) is not due to random chance. A significant p-value (
![p less than 0.05](https://learning.flatironschool.com/equation\_images/p%2520%253C%25200.05?scale=1)
) confirms this relationship.

### Why Calculate a Confidence Interval?

The confidence interval quantifies uncertainty, providing stakeholders with a range for the true slope, which enhances trust in the model's predictions.

### Video: Technical Lesson Guide

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of statistical inference on the slope.

[VIDEO LINK](https://player.vimeo.com/video/1061119452?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Resources

* We will use the **"mtcars" dataset** from the statsmodels library, which contains advertising expenditure data and corresponding sales figures. This dataset is a commonly used example for regression analysis.

### Instructions

#### Step 1. Import Required Libraries

**Action:** Import the required libraries for data analysis and modeling.

```
# Install the necessary R package if you haven't already  
# !pip install rdatasets  
  
  
import pandas as pd  
import statsmodels.api as sm  
import matplotlib.pyplot as plt  
# Import the rdatasets package  
from rdatasets import data as rdata
```

#### Step 2. Load the Dataset

**Action:** Load the dataset and inspect its structure.

```
data = sm.datasets.get_rdataset("mtcars", "datasets").data  
  
  
# Display the info  
print(data.info())
```

**Decision Point:** Confirm that the dataset contains numeric columns suitable for regression.

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

#### Step 3. Define the Variables

Let’s use the mtcars dataset, which is a widely used dataset containing information about 32 cars, including variables like miles per gallon (mpg), horsepower (hp), and weight (wt). This dataset is well-suited for demonstrating regression analysis. The goal will be to predict miles per gallon (mpg) based on horsepower (hp).

```
# Define variables  
X = sm.add_constant(data['hp'])  # Add constant for intercept  
y = data['mpg']  
  
  
# Ensure that x and y have consistent dimensions.  
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
  
# Print the summary to verify the model's parameters.  
  
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
Time:                        20:55:42   Log-Likelihood:                -87.619  
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

#### Step 5. Perform Hypothesis Test for the Slope

**Action:** Extract the slope (
![b 1](https://learning.flatironschool.com/equation\_images/b\_1?scale=1)
), standard error (
![SE left parenthesis b 1 right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSE%257D(b\_1)?scale=1)
), *t*-statistic, and *p*-value from the model.

```
# Extract slope and related statistics  
slope = model.params['hp']  
std_error = model.bse['hp']  
t_statistic = model.tvalues['hp']  
p_value = model.pvalues['hp']  
  
print(f"Slope (b1): {slope}")  
print(f"Standard Error: {std_error}")  
print(f"t-Statistic: {t_statistic}")  
print(f"p-Value: {p_value}")  
  
 
```

**Output:**

```
Slope (b1): -0.0682282780715637  
Standard Error: 0.010119303810422772  
t-Statistic: -6.742388542706794  
p-Value: 1.7878352541210495e-07
```

**Interpretation:**

* The null hypothesis is
  ![upper H 0 colon beta 1 equals 0](https://learning.flatironschool.com/equation\_images/H\_0%253A%2520%255Cbeta\_1%2520%253D%25200?scale=1)
  .
* A *p*-value less than
  ![0.05](https://learning.flatironschool.com/equation\_images/0.05?scale=1)
  suggests that the slope is statistically significant.

#### Step 6. Construct a Confidence Interval for the Slope

**Action:** Calculate the 95% confidence interval for the slope ($b\_1$).

```
# Calculate confidence interval  
conf_int = model.conf_int(alpha=0.05).loc['hp']  
print(f"95% Confidence Interval for the slope: {conf_int}")
```

**Output:**

```
95% Confidence Interval for the slope: 0   -0.088895  
1   -0.047562  
Name: hp, dtype: float64
```

**Interpretation:**

* The confidence interval provides a range of plausible values for the true slope (
  ![beta 1](https://learning.flatironschool.com/equation\_images/%255Cbeta\_1?scale=1)
  ).
* If the interval does not include
  ![0](https://learning.flatironschool.com/equation\_images/0?scale=1)
  , the slope is statistically significant.

#### Step 7. Visualize the Regression Line

**Action:** Plot the data, the regression line, and annotate the slope.

```
# Predicted values  
data['Predicted_mpg'] = model.predict(X)  
  
# Scatterplot with regression line  
plt.scatter(data['hp'], data['mpg'], label='Data')  
plt.plot(data['hp'], data['Predicted_mpg'], color='red', label=f'Regression Line (Slope = {slope:.2f})')  
plt.title('Regression Analysis: Horsepower vs. MPG')  
plt.xlabel('Horsepower (hp)')  
plt.ylabel('Miles Per Gallon (mpg)')  
plt.legend()  
plt.show()
```

**Output:**

![Regression analysis output of horsepower vs mpg.](https://moringa.instructure.com/courses/1426/files/631845/download)

##### **Interpret Results: Findings Summary**

* **Slope (
  ![b 1](https://learning.flatironschool.com/equation\_images/b\_1?scale=1)
  ):** Indicates the average change in mpg for a one-unit increase in horsepower.
* **Confidence Interval:** Provides the range of plausible values for **![b 1](https://learning.flatironschool.com/equation\_images/b\_1?scale=1)**.
* **Hypothesis Test:** A *p*-value less than
  ![0.05](https://learning.flatironschool.com/equation\_images/0.05?scale=1)
  confirms a statistically significant relationship.

### Considerations

* **Data Suitability:** Ensure data cleanliness and numeric compatibility for regression.
* **Assumptions:** Validate model assumptions to ensure reliable results.
* **Outliers:** Identify and address influential points that distort regression outputs.
* **Confidence Intervals:** Clearly interpret intervals to avoid confusion.
* **Communication:** Balance statistical significance with practical relevance.
* **Visualization:** Use clear and informative plots to present results effectively.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248837

Scraped At: 2026-05-15T10:30:42.540274
