# Example: Multiple Linear Regression

# Example: Multiple Linear Regression

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Example: Multiple Linear Regression

Icon Progress Bar (browser only)

4 min read

A junior data scientist at a real estate company is tasked with predicting house prices based on multiple factors. The company wants to understand how variables like square footage, number of bedrooms, and age of the house affect house prices. The data scientist decides to use Multiple Linear Regression to analyze the relationship.

The **objective is to predict house prices (*y*) based on three predictors**:

* ![x 1](https://learning.flatironschool.com/equation\_images/x\_1?scale=1)
  : Square footage (sqft)
* ![x 2](https://learning.flatironschool.com/equation\_images/x\_2?scale=1)
  : Number of bedrooms
* ![x 3](https://learning.flatironschool.com/equation\_images/x\_3?scale=1)
  : Age of the house

The **general regression equation** is:
![y With caret equals b 0 plus b 1 x 1 plus b 2 x 2 plus b 3 x 3](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1%2520x\_1%2520%252B%2520b\_2%2520x\_2%2520%252B%2520b\_3%2520x\_3?scale=1)

Where:

* ![y With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D?scale=1)
  is the predicted house price.
* ![b 0](https://learning.flatironschool.com/equation\_images/b\_0?scale=1)
  is the intercept.
* ![b 1 comma b 2 comma b 3](https://learning.flatironschool.com/equation\_images/b\_1%252C%2520b\_2%252C%2520b\_3?scale=1)
  are the coefficients of the predictor variables.

### Solution

#### Step 1: Import Necessary Libraries

**Action:** Import libraries for data handling, analysis, and modeling.

```
import pandas as pd  
import statsmodels.api as sm  
import matplotlib.pyplot as plt  
import seaborn as sns
```

#### Step 2: Load the Dataset

**Action:** Load a sample dataset containing house price data. For this example, we will create a fictional dataset.

```
# Create a sample dataset  
data = pd.DataFrame({  
    'square_footage': [1500, 1800, 2400, 3000, 3500, 4000, 4500, 2000, 2200, 3200],  
    'num_bedrooms': [3, 3, 4, 4, 5, 5, 6, 3, 3, 4],  
    'house_age': [10, 15, 20, 5, 8, 12, 25, 20, 18, 6],  
    'house_price': [300000, 350000, 500000, 600000, 650000, 700000, 750000, 400000, 420000, 580000]  
})  
  
# Display the first few rows  
print(data.head())
```

**Output:**

```
square_footage  num_bedrooms  house_age  house_price  
0            1500             3         10       300000  
1            1800             3         15       350000  
2            2400             4         20       500000  
3            3000             4          5       600000  
4            3500             5          8       650000
```

#### Step 3: Define the Variables

**Action:** Define the predictors ($x\_1, x\_2, x\_3$) and the dependent variable ($y$). Add a constant for the intercept.

```
# Define predictors (independent variables) and response (dependent variable)  
X = data[['square_footage', 'num_bedrooms', 'house_age']]  # Independent variables  
X = sm.add_constant(X)  # Add a constant for the intercept  
y = data['house_price']  # Dependent variable  
  
  
# Verify shape  
print(X.shape, y.shape)
```

**Output:**

```
(10, 4) (10,)
```

#### Step 4: Fit the Multiple Linear Regression Model

**Action:** Use the Ordinary Least Squares (OLS) method to fit the regression model.

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
Dep. Variable:            house_price   R-squared:                       0.975  
Model:                            OLS   Adj. R-squared:                  0.963  
Method:                 Least Squares   F-statistic:                     79.16  
Date:                Tue, 17 Dec 2024   Prob (F-statistic):           3.24e-05  
Time:                        13:18:26   Log-Likelihood:                -114.61  
No. Observations:                  10   AIC:                             237.2  
Df Residuals:                       6   BIC:                             238.4  
Df Model:                           3                                           
Covariance Type:            nonrobust                                           
==================================================================================  
                     coef    std err          t      P>|t|      [0.025      0.975]  
----------------------------------------------------------------------------------  
const            1.02e+05    4.8e+04      2.125      0.078   -1.54e+04    2.19e+05  
square_footage   140.5529     35.012      4.014      0.007      54.881     226.225  
num_bedrooms    1.263e+04   3.32e+04      0.381      0.716   -6.85e+04    9.38e+04  
house_age      -1615.4237   1523.778     -1.060      0.330   -5343.974    2113.126  
==============================================================================  
Omnibus:                        0.759   Durbin-Watson:                   1.221  
Prob(Omnibus):                  0.684   Jarque-Bera (JB):                0.619  
Skew:                           0.490   Prob(JB):                        0.734  
Kurtosis:                       2.274   Cond. No.                     1.71e+04  
==============================================================================  
  
Notes:  
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.  
[2] The condition number is large, 1.71e+04. This might indicate that there are  
strong multicollinearity or other numerical problems.  
/usr/local/lib/python3.10/dist-packages/scipy/stats/_axis_nan_policy.py:531: UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=10  
  res = hypotest_fun_out(*samples, **kwds)
```

#### Step 5: Analyze Results

**Action:** Interpret the model’s results

The model is used to predict house prices based on three predictors: square footage, number of bedrooms, and age of the house. Below is a breakdown of the results:

##### Key Metrics

1. **![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
   (R-squared): 0.975**  
   * This indicates that 97.5% of the variability in house prices is explained by the predictors in the model.
   * A high 
     ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
     suggests a strong fit of the regression model to the data.
2. **adjusted
   ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
   : 0.963**  
   * adjusted 
     ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
     accounts for the number of predictors in the model and penalizes overfitting.
   * The slight drop from 
     ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
     to adjusted 
     ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
     reflects the inclusion of predictors that might not add significant explanatory power.
3. **F-statistic: 79.16 (p-value = 3.24e-05)**  
   * The F-statistic tests the null hypothesis that all regression coefficients (
     ![b 1 comma b 2 comma ellipsis comma b Subscript p Baseline](https://learning.flatironschool.com/equation\_images/b\_1%252C%2520b\_2%252C%2520%255Cdots%252C%2520b\_p?scale=1)
     ) are zero.
   * A very small p-value (< 0.05) indicates that the model as a whole is statistically significant.

##### Interpretation of Coefficients

Interpretation of Coefficients

| Predictor | Coefficient (*b*) | Std Error | t-statistic | p-value | Interpretation |
| --- | --- | --- | --- | --- | --- |
| Intercept | ![1.02 times 10 Superscript 5](https://learning.flatironschool.com/equation\_images/1.02%2520%255Ctimes%252010%255E5?scale=1) | ![4.8 times 10 Superscript 4](https://learning.flatironschool.com/equation\_images/4.8%2520%255Ctimes%252010%255E4?scale=1) | 2.125 | 0.078 | Baseline price when all predictors are zero. Marginally insignificant ( ![p greater than 0.05](https://learning.flatironschool.com/equation\_images/p%2520%253E%25200.05?scale=1) ). |
| Square Footage | 140.55 | 35.01 | 4.014 | 0.007 | For each additional square foot, the house price increases by $140.55, holding other variables constant. Statistically significant. |
| Number of Bedrooms | ![1.263 times 10 Superscript 4](https://learning.flatironschool.com/equation\_images/1.263%2520%255Ctimes%252010%255E4?scale=1) | ![3.32 times 10 Superscript 4](https://learning.flatironschool.com/equation\_images/3.32%2520%255Ctimes%252010%255E4?scale=1) | 0.381 | 0.716 | Adding another bedroom increases the price by $12,630, but this effect is not statistically significant ( ![p greater than 0.05](https://learning.flatironschool.com/equation\_images/p%2520%253E%25200.05?scale=1) ). |
| House Age | -1615.42 | 1523.78 | -1.060 | 0.330 | Each additional year of house age reduces the price by $1,615.42, but this effect is not statistically significant. |

##### Statistical Significance

1. **Square Footage (
   ![p equals 0.007](https://learning.flatironschool.com/equation\_images/p%2520%253D%25200.007?scale=1)
   ):**  
   * Statistically significant. It is the most important predictor, as indicated by its strong t-statistic and small p-value.
   * This suggests that larger homes command higher prices, consistent with domain knowledge.
2. **Number of Bedrooms (
   ![p equals 0.716](https://learning.flatironschool.com/equation\_images/p%2520%253D%25200.716?scale=1)
   ):**  
   * Not statistically significant. Despite being intuitively relevant, the effect is weak after accounting for other predictors.
   * Multicollinearity may be a factor here, reducing its importance.
3. **House Age (
   ![p equals 0.330](https://learning.flatironschool.com/equation\_images/p%2520%253D%25200.330?scale=1)
   ):**  
   * Not statistically significant. Although house age has a negative coefficient (older houses decrease in value), the p-value is too high to conclude this effect confidently.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248852

Scraped At: 2026-05-15T10:32:30.903974
