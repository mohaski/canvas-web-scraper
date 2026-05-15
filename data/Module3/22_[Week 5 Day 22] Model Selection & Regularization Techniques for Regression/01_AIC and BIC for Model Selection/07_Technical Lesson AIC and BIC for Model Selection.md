# Technical Lesson: AIC and BIC for Model Selection

# Technical Lesson: AIC and BIC for Model Selection

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: AIC and BIC for Model Selection

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In this lesson, we focus on using AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion) for model selection in Multiple Linear Regression Models. AIC and BIC are key statistical metrics that help data scientists identify the best-fitting model while balancing predictive performance and model complexity.

To demonstrate this process, we use the well-known Boston Housing dataset. This dataset includes 506 rows and 14 variables, providing insights into the relationship between housing prices (medv, the response variable) and predictors such as:

* **CRIM:** Per capita crime rate by town.
* **RM:** Average number of rooms per dwelling.
* **LSTAT:** Percentage of lower-status population.
* **AGE:** Proportion of owner-occupied units built before 1940.
* **TAX:** Property tax rate.

The goal is to build and evaluate regression models to predict housing prices (medv) while systematically selecting the most effective predictors using AIC and BIC.

The Boston Housing dataset provides a **real-world example of regression modeling in the housing market**, which is applicable to industries like real estate, urban planning, and economic analysis. For instance:

* CRIM (crime rate) and LSTAT (lower-status percentage) may negatively affect housing prices.
* RM (average rooms per dwelling) and NOX (pollution levels) may have nonlinear relationships with medv.

By using AIC and BIC, we can identify a model that best explains housing price variation while avoiding overfitting caused by too many predictors. This structured process mirrors the problem-solving workflow of a data analyst tasked with building predictive models for real-world applications.

This process will equip you with the skills to perform model selection effectively, ensuring you can build robust regression models for complex, real-world datasets like the Boston Housing dataset.

### Video: Technical Lesson Guide

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of AIC and BIC for model selection.

[VIDEO LINK](https://player.vimeo.com/video/1060372568?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

### Step 1. Data Exploration and Setup

We will use the **"Boston Housing" dataset from rdatasets** for this example, which contains data on housing values and predictors.

```
#! pip install rdatasets  
  
import pandas as pd  
import statsmodels.api as sm  
from sklearn.model_selection import train_test_split  
from rdatasets import data as rdata  
  
  
# Load the dataset  
boston = rdata("MASS", "Boston")  
  
  
# Inspect data  
print(boston.head())  
print(boston.info())  
print(boston.describe())
```

**Output:**

```
rownames     crim    zn  indus  chas    nox     rm   age     dis  rad  tax  \  
0         1  0.00632  18.0   2.31     0  0.538  6.575  65.2  4.0900    1  296     
1         2  0.02731   0.0   7.07     0  0.469  6.421  78.9  4.9671    2  242     
2         3  0.02729   0.0   7.07     0  0.469  7.185  61.1  4.9671    2  242     
3         4  0.03237   0.0   2.18     0  0.458  6.998  45.8  6.0622    3  222     
4         5  0.06905   0.0   2.18     0  0.458  7.147  54.2  6.0622    3  222     
  
   ptratio   black  lstat  medv    
0     15.3  396.90   4.98  24.0    
1     17.8  396.90   9.14  21.6    
2     17.8  392.83   4.03  34.7    
3     18.7  394.63   2.94  33.4    
4     18.7  396.90   5.33  36.2    
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 506 entries, 0 to 505  
Data columns (total 15 columns):  
 #   Column    Non-Null Count  Dtype    
---  ------    --------------  -----    
 0   rownames  506 non-null    int64    
 1   crim      506 non-null    float64  
 2   zn        506 non-null    float64  
 3   indus     506 non-null    float64  
 4   chas      506 non-null    int64    
 5   nox       506 non-null    float64  
 6   rm        506 non-null    float64  
 7   age       506 non-null    float64  
 8   dis       506 non-null    float64  
 9   rad       506 non-null    int64    
 10  tax       506 non-null    int64    
 11  ptratio   506 non-null    float64  
 12  black     506 non-null    float64  
 13  lstat     506 non-null    float64  
 14  medv      506 non-null    float64  
dtypes: float64(11), int64(4)  
memory usage: 59.4 KB  
None  
         rownames        crim          zn       indus        chas         nox  \  
count  506.000000  506.000000  506.000000  506.000000  506.000000  506.000000     
mean   253.500000    3.613524   11.363636   11.136779    0.069170    0.554695     
std    146.213884    8.601545   23.322453    6.860353    0.253994    0.115878     
min      1.000000    0.006320    0.000000    0.460000    0.000000    0.385000     
25%    127.250000    0.082045    0.000000    5.190000    0.000000    0.449000     
50%    253.500000    0.256510    0.000000    9.690000    0.000000    0.538000     
75%    379.750000    3.677083   12.500000   18.100000    0.000000    0.624000     
max    506.000000   88.976200  100.000000   27.740000    1.000000    0.871000     
  
               rm         age         dis         rad         tax     ptratio  \  
count  506.000000  506.000000  506.000000  506.000000  506.000000  506.000000     
mean     6.284634   68.574901    3.795043    9.549407  408.237154   18.455534     
std      0.702617   28.148861    2.105710    8.707259  168.537116    2.164946     
min      3.561000    2.900000    1.129600    1.000000  187.000000   12.600000     
25%      5.885500   45.025000    2.100175    4.000000  279.000000   17.400000     
50%      6.208500   77.500000    3.207450    5.000000  330.000000   19.050000     
75%      6.623500   94.075000    5.188425   24.000000  666.000000   20.200000     
max      8.780000  100.000000   12.126500   24.000000  711.000000   22.000000     
  
            black       lstat        medv    
count  506.000000  506.000000  506.000000    
mean   356.674032   12.653063   22.532806    
std     91.294864    7.141062    9.197104    
min      0.320000    1.730000    5.000000    
25%    375.377500    6.950000   17.025000    
50%    391.440000   11.360000   21.200000    
75%    396.225000   16.955000   25.000000    
max    396.900000   37.970000   50.000000    
  
-
```

### Step 2. Fit a Full Model

The **response variable is medv** (median value of homes), and the predictors are all other numeric columns.

```
# Define response and predictor variables  
Y = boston['medv']  # Response variable  
X = boston.drop(columns=['medv'])  # All other predictors  
X = sm.add_constant(X)  # Add intercept  
  
# Fit the full model  
full_model = sm.OLS(Y, X).fit()  
  
# Print AIC and BIC  
print(f"Full Model AIC: {full_model.aic:.3f}")  
print(f"Full Model BIC: {full_model.bic:.3f}")
```

**Output:**

```
Full Model AIC: 3026.090  
Full Model BIC: 3089.488
```

### Step 3. Compare Models

We **compare smaller models** with different subsets of predictors.

```
# Subset models  
X1 = sm.add_constant(boston[['rm', 'lstat']])  # Model with 'rm' and 'lstat'  
X2 = sm.add_constant(boston[['rm', 'lstat', 'crim']])  # Add 'crim'  
  
# Fit models  
model1 = sm.OLS(Y, X1).fit()  
model2 = sm.OLS(Y, X2).fit()  
  
# Compare AIC and BIC  
print(f"Model 1 AIC: {model1.aic:.3f}, BIC: {model1.bic:.3f}")  
print(f"Model 2 AIC: {model2.aic:.3f}, BIC: {model2.bic:.3f}")  
print(f"Full Model AIC: {full_model.aic:.3f}, BIC: {full_model.bic:.3f}")
```

**Output:**

```
Model 1 AIC: 3171.542, BIC: 3184.222  
Model 2 AIC: 3163.232, BIC: 3180.138  
Full Model AIC: 3026.090, BIC: 3089.488
```

**Interpret Results:**

* AIC/BIC values help select the best model.
* The model with the lowest AIC/BIC is the preferred model, balancing fit and complexity.

### Considerations

Decision points and tradeoffs

| Decision Point | Pros | Cons |
| --- | --- | --- |
| Choosing AIC vs. BIC | AIC favors accuracy; BIC favors simplicity. | Can lead to different model selections. |
| Using All Predictors (Full Model) | Captures all possible relationships. | Increased complexity; risk of overfitting. |
| Removing Predictors | Reduces model complexity and improves AIC/BIC. | Risk of excluding meaningful predictors. |
| Automating Model Comparison | Faster and systematic model selection. | Automation may hide model assumptions/errors. |

* **Proper data exploration** and understanding of predictors are crucial for a meaningful full model.
* **AIC and BIC provide systematic ways to balance model fit and complexity**, but understanding their tradeoffs is key.
* **Iterative model comparisons** **(e.g., backward elimination) streamline the process**, but validating results through diagnostics is equally important.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248891

Scraped At: 2026-05-15T10:37:02.645252
