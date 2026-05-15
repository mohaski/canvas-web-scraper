# Technical Lesson: General Linear Regression Models

# Technical Lesson: General Linear Regression Models

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: General Linear Regression Models

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

This technical lesson focuses on understanding General Linear Regression Models (GLMs), where the goal is to explore how GLMs generalize multiple linear regression models. Unlike traditional regression with a single response variable, GLMs can handle multiple dependent variables simultaneously, providing a robust statistical framework to analyze complex relationships.

The **mtcars dataset** serves as the foundation for this example. The steps focus on:

1. Building a multivariate regression model using sklearn to predict multiple response variables.
2. Evaluating model performance with metrics such as R-squared and Adjusted R-squared.
3. Extending the base model by introducing interaction terms and assessing improvements.

This process aligns with real-world scenarios where analysts need to model multiple outcomes influenced by shared predictors. For example, in the automotive industry, understanding how weight (predictor) impacts both fuel efficiency (mpg) and engine power (hp) helps in optimizing vehicle design.

**Key challenges** include:

* Defining multiple response variables appropriately.
* Evaluating model accuracy for each dependent variable.
* Managing potential nonlinear relationships and interactions.

### Video: Lesson Guide

By following the outlined steps, you will develop skills to build, evaluate, and compare multivariate regression models effectively.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of general liner regression models.

[VIDEO LINK](https://player.vimeo.com/video/1060372670?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

### Step 1. Data Exploration and Setup

* Load the dataset and inspect its structure.
* Identify the response variables (dependent variables) and predictors (independent variables).

```
import pandas as pd  
import numpy as np  
import statsmodels.formula.api as smf  
import statsmodels.api as sm  
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import r2_score  
  
  
# Import the rdatasets package  
from rdatasets import data as rdata  
  
   
  
  
# Load the 'cars' dataset  
cars_data = sm.datasets.get_rdataset("mtcars", "datasets").data  
  
  
# Inspect the data  
print(cars_data.head())  
print(cars_data.info())  
print(cars_data.describe())
```

**Output:**

```
 mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \  
rownames                                                                       
Mazda RX4          21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     
Mazda RX4 Wag      21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     
Datsun 710         22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     
Hornet 4 Drive     21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     
Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     
  
                   carb    
rownames                   
Mazda RX4             4    
Mazda RX4 Wag         4    
Datsun 710            1    
Hornet 4 Drive        1    
Hornet Sportabout     2    
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
             mpg        cyl        disp          hp       drat         wt  \  
count  32.000000  32.000000   32.000000   32.000000  32.000000  32.000000     
mean   20.090625   6.187500  230.721875  146.687500   3.596563   3.217250     
std     6.026948   1.785922  123.938694   68.562868   0.534679   0.978457     
min    10.400000   4.000000   71.100000   52.000000   2.760000   1.513000     
25%    15.425000   4.000000  120.825000   96.500000   3.080000   2.581250     
50%    19.200000   6.000000  196.300000  123.000000   3.695000   3.325000     
75%    22.800000   8.000000  326.000000  180.000000   3.920000   3.610000     
max    33.900000   8.000000  472.000000  335.000000   4.930000   5.424000     
  
            qsec         vs         am       gear     carb    
count  32.000000  32.000000  32.000000  32.000000  32.0000    
mean   17.848750   0.437500   0.406250   3.687500   2.8125    
std     1.786943   0.504016   0.498991   0.737804   1.6152    
min    14.500000   0.000000   0.000000   3.000000   1.0000    
25%    16.892500   0.000000   0.000000   3.000000   2.0000    
50%    17.710000   0.000000   0.000000   4.000000   2.0000    
75%    18.900000   1.000000   1.000000   4.000000   4.0000    
max    22.900000   1.000000   1.000000   5.000000   8.0000  
```

### Step 2. Fit a Multivariate Regression Model

We will predict mpg (miles per gallon) and hp (horsepower) using the predictor wt (weight).

* Define the predictor (independent variable) and response variables (dependent variables).
* Use sklearn's LinearRegression to fit the model.

```
from sklearn.linear_model import LinearRegression  
  
# Define predictors (X) and response variables (Y)  
X = cars_data[['wt']]  # Predictor: weight of the car  
Y = cars_data[['mpg', 'hp']]  # Response variables: mpg and hp  
  
# Initialize and fit the multivariate regression model  
multi_reg = LinearRegression().fit(X, Y)  
  
# Extract coefficients and intercepts  
print("Intercepts:", multi_reg.intercept_)  
print("Coefficients:", multi_reg.coef_)
```

**Output:**

```
Intercepts: [37.28512617 -1.82092177]  
Coefficients: [[-5.34447157]  
 [46.16005028]]
```

**Output Interpretation:**

* The **intercepts** represent the baseline values for mpg and hp when wt is zero.
* The **coefficients** indicate how changes in wt affect mpg and hp.

### Step 3. Model Evaluation

To evaluate the model performance, calculate the R-squared value for each response variable.

```
from sklearn.metrics import r2_score  
  
# Predict the response variables  
Y_pred = multi_reg.predict(X)  
  
# Compute R-squared for each response variable  
r2_mpg = r2_score(Y['mpg'], Y_pred[:, 0])  # R-squared for mpg  
r2_hp = r2_score(Y['hp'], Y_pred[:, 1])  # R-squared for hp  
  
print(f"R-squared for mpg: {r2_mpg:.3f}")  
print(f"R-squared for hp: {r2_hp:.3f}")
```

**Output:**

```
R-squared for mpg: 0.753  
R-squared for hp: 0.434
```

**Output Interpretation:**

* **R-squared for mpg:** How well the predictor wt explains variation in mpg.
* **R-squared for hp:** How well the predictor wt explains variation in hp.

### Step 4. Add Quadratic Terms

**Introduce quadratic terms by including wt²** (weight squared) to capture potential nonlinear relationships.

* Create a new column for wt².
* Fit the updated multivariate regression model.

```
# Add quadratic term: weight squared  
cars_data['wt_squared'] = cars_data['wt'] ** 2  
  
  
# Update predictors  
X_quad = cars_data[['wt', 'wt_squared']]  
  
  
# Fit the updated model  
multi_reg_quad = LinearRegression().fit(X_interaction, Y)  
  
  
# Extract coefficients and intercepts  
print("Updated Intercepts:", multi_reg_quad.intercept_)  
print("Updated Coefficients:", multi_reg_quad.coef_)  
  
 
```

**Output:**

```
Updated Intercepts: [ 49.93081095 -76.73441384]  
Updated Coefficients: [[-13.38033708   1.17108689]  
 [ 93.76480697  -6.93756093]]
```

**Output Interpretation:**

* **Adding the wt² term** allows the model to capture curvature in the relationships between wt and the response variables (mpg, hp).
* **Compare the updated coefficients** to understand the effect of the quadractic term.

### Step 5. Model Comparison Using R-squared

To evaluate whether the quadractic term improves the model performance, we will **compute the R-squared values. R-squared accounts for the number of predictors** in the model and provides a better comparison between models with different numbers of features.

```
# Predict using the updated model  
Y_pred_quad = multi_reg_quad.predict(X_quad)  
  
# Compute R-squared for the updated model  
r2_mpg_quad = r2_score(Y['mpg'], Y_pred_quad[:, 0])  
r2_hp_quad = r2_score(Y['hp'], Y_pred_quad[:, 1])  
  
print(f"Updated R-squared for mpg: {r2_mpg_quad:.3f}")  
print(f"Updated R-squared for hp: {r2_hp_quad:.3f}")
```

**Output:**

```
Updated R-squared for mpg: 0.819  
Updated R-squared for hp: 0.452
```

**Output Interpretation:**

* **R-squared for Base Model:** Indicates the performance of the model using only wt as the predictor.
* **R-squared for Quadratic Model:** Measures the performance when the quadratic term (wt²) is included.

**Note:** If the R-squared values improve for the quadratic model, it suggests that the addition of the nonlinear term improves the model's explanatory power while accounting for model complexity.

### Step 6. Final Model and Recommendations

```
# Create a dictionary to store the values  
data = {  
   'Metric': ['R-squared for mpg', 'R-squared for hp'],  
   'GLM Model': [r2_mpg, r2_hp],  
   'Quadractic Model': [r2_mpg_quad, r2_hp_quad]  
}  
  
  
# Create a pandas DataFrame  
df = pd.DataFrame(data)  
  
  
# Display the DataFrame as a table  
print(df.to_markdown(index=False))
```

**Output:**

```
| Metric            |   GLM Model |   Quadractic Model |  
|:------------------|------------:|-------------------:|  
| R-squared for mpg |    0.752833 |           0.819061 |  
| R-squared for hp  |    0.433949 |           0.451908 |
```

### Pros and Cons of Multivariate Regression Models

Pros and Cons of Multivariate Regression Models

| Decision Point | Pros | Cons |
| --- | --- | --- |
| Using Multiple Response Variables | Simultaneously models correlated outcomes, saving computational resources. | Increased complexity in model interpretation. |
| Adding Interaction Terms | Captures nonlinear relationships for better accuracy. | Risk of multicollinearity; requires careful diagnostics. |
| Adjusted R-squared | Penalizes overfitting, making model comparison fairer. | Requires understanding of model degrees of freedom. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248880

Scraped At: 2026-05-15T10:35:33.641836
