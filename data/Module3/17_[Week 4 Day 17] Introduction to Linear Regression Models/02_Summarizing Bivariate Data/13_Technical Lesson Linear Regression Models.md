# Technical Lesson: Linear Regression Models

# Technical Lesson: Linear Regression Models

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: Linear Regression Models

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

The Gala Islands dataset from the faraway package provides ecological data on islands in the Galapagos archipelago. This dataset includes information on various geographic and ecological attributes, making it ideal for exploring relationships between environmental factors and biodiversity.

### Data Context

The Galapagos Islands are known for their unique and diverse ecosystems. This dataset captures how factors such as island size, proximity to other islands, and elevation influence the number of species observed. The dataset provides a meaningful context for studying ecological principles, such as island biogeography.

#### Variables in the Dataset

1. **Independent Variable (*x*):**  
   * **Area:** The size of the island, measured in square kilometers.
   * **Role:** Larger islands typically support more species due to greater habitat diversity, which makes this variable a logical predictor of species richness.
2. **Dependent Variable (*y*):**  
   * **Species:** The total number of observed species on the island.
   * **Role:** This variable reflects the biodiversity of each island and serves as the outcome of interest in this analysis.
3. **Other Variables in the Dataset:** While not used in this specific analysis, the dataset also includes:  
   * **Elevation:** The maximum elevation of the island (meters).
   * **Nearest:** Distance to the nearest island (kilometers).
   * **Scruz:** Distance to Santa Cruz Island (kilometers).
   * **Adjacent:** Area of adjacent islands within 50 km (square kilometers).

#### Relevance of the Data

This dataset is particularly valuable for exploring ecological patterns such as the **species-area relationship**, which suggests that larger areas typically harbor greater biodiversity. By analyzing the relationship between island area and species richness, we can better understand ecological dynamics and test hypotheses related to island biogeography.

#### Use in This Walkthrough

For this lesson, we focus on:

* **Independent Variable (*x*):** Island area (Area)
* **Dependent Variable (*y*):** Number of species observed (Species)

This straightforward bivariate relationship allows us to apply and interpret linear regression and correlation analysis effectively. The insights from this dataset also extend to real-world applications in ecology, conservation planning, and environmental decision-making.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of linear regression models.

[VIDEO LINK](https://player.vimeo.com/video/1060371620?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Resources

* [Functions and Datasets


  Links to an external site.](https://pypi.org/project/faraway)

### Instructions

* [Step 1. Import Necessary Libraries](#dpPanel0Content)
* [Step 2. Load and Inspect the Dataset](#dpPanel1Content)
* [Step 3. Verify Data Suitability](#dpPanel2Content)
* [Step 4. Define the Variables](#dpPanel3Content)
* [Step 5. Add a Constant Term for the Regression](#dpPanel4Content)
* [Step 6. Create a Scatterplot](#dpPanel5Content)
* [Step 7. Fit the Linear Regression Model](#dpPanel6Content)
* [Step 8: Add the Regression Line to the Scatterplot](#dpPanel7Content)

### Step 1. Import Necessary Libraries

**Action:** Import libraries for data manipulation, visualization, and computation. If you have not used the faraway datasets before, then you need to install the library.

```
! pip install faraway  
  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
import statsmodels.api as sm  
from faraway.datasets import galapagos
```

### Step 2. Load and Inspect the Dataset

**Action:** Load the dataset and inspect its structure.

```
# Load the gala dataset  
data = galapagos.load()  
  
# Display the first few rows  
print(data.head())  
  
# Check dataset information  
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

### Step 3. Verify Data Suitability

**Action:** Ensure the data contains two numeric variables suitable for bivariate analysis.

**Decision Point:** Confirm that the variables Area (independent variable) and Species (dependent variable) are numeric.

```
# Check data types  
print(data.dtypes)  
  
# Ensure no missing values  
print(data.isnull().sum())
```

**Output:**

```
Species        int64  
Area         float64  
Elevation      int64  
Nearest      float64  
Scruz        float64  
Adjacent     float64  
dtype: object  
Species      0  
Area         0  
Elevation    0  
Nearest      0  
Scruz        0  
Adjacent     0  
dtype: int64
```

### Step 4. Define the Variables

**Action:** Assign the independent variable (*x*) and dependent variable (*y*). Check their dimensions to ensure they are consistent and suitable for the regression model.

```
# Define variables  
X = data[['Area']]  # Independent variable (Area of the island)  
y = data['Species']  # Dependent variable (Number of species)  
  
# Check the dimensions  
print(f"X shape: {X.shape}")  
print(f"y shape: {y.shape}")
```

**Output:**

```
X shape: (30, 1)  
y shape: (30,)
```

What to Look For:

* ***X***: Should have two dimensions (e.g., (n, 1)), where *n* is the number of data points. This is because sklearn's LinearRegression expects a 2D array for the independent variable.
* ***y***: Should have one dimension (e.g., (n,)), corresponding to the number of data points.

### Step 5. Add a Constant Term for the Regression

**Action:** Add a constant term to the independent variable for the intercept (
![b 0](https://learning.flatironschool.com/equation\_images/b\_0?scale=1)
b0), and verify that it worked.

```
# Add constant term to X  
X = sm.add_constant(X)  
  
# Inspect the first few rows of X to verify the constant column was added  
print(X.head())  
  
# Check the dimensions of X to ensure an additional column was added  
print(f"X shape: {X.shape}")
```

**Output:**

```
          const   Area  
Baltra       1.0  25.09  
Bartolome    1.0   1.24  
Caldwell     1.0   0.21  
Champion     1.0   0.10  
Coamano      1.0   0.05  
X shape: (30, 2)
```

### Step 6. Create a Scatterplot

**Action:** Visualize the relationship between *x* and *y* using a scatterplot.

```
# Create scatterplot  
sns.scatterplot(x=data['Area'], y=data['Species'])  
plt.title('Scatterplot: Area vs Species')  
plt.xlabel('Island Area (sq km)')  
plt.ylabel('Number of Species')  
plt.grid(True)  
plt.show()
```

**Output:**

[![Scatterplot of Island Area vs Species](https://moringa.instructure.com/courses/1426/files/631791/download)](https://moringa.instructure.com/courses/1426/files/631791/download "Scatterplot of Island Area vs Species")

### Step 7. Fit the Linear Regression Model

**Action:** Fit a simple linear regression model using statsmodels. Make sure to print the regression line and linear correlation coefficient.

```
# Fit the regression model  
model = sm.OLS(y, X).fit()  
  
# Get regression coefficients  
b0 = model.params['const']  # Intercept  
b1 = model.params['Area']  # Slope  
  
  
# Compute the correlation coefficient  
r = np.corrcoef(data['Area'], data['Species'])[0, 1]  
  
  
# Print the regression line equation and correlation coefficient  
print(f"Regression Line: y = {b0:.2f} + {b1:.2f}x")  
print(f"Correlation Coefficient (r): {r:.2f}")  
  
  
# Print the model summary for additional details  
print(model.summary())
```

**Output:**

```
Regression Line: y = 63.78 + 0.08x  
Correlation Coefficient (r): 0.62  
                            OLS Regression Results                              
==============================================================================  
Dep. Variable:                Species   R-squared:                       0.382  
Model:                            OLS   Adj. R-squared:                  0.360  
Method:                 Least Squares   F-statistic:                     17.29  
Date:                Fri, 13 Dec 2024   Prob (F-statistic):           0.000275  
Time:                        21:54:15   Log-Likelihood:                -177.10  
No. Observations:                  30   AIC:                             358.2  
Df Residuals:                      28   BIC:                             361.0  
Df Model:                           1                                           
Covariance Type:            nonrobust                                           
==============================================================================  
                 coef    std err          t      P>|t|      [0.025      0.975]  
------------------------------------------------------------------------------  
const         63.7829     17.524      3.640      0.001      27.886      99.680  
Area           0.0820      0.020      4.158      0.000       0.042       0.122  
==============================================================================  
Omnibus:                       23.768   Durbin-Watson:                   1.303  
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               34.880  
Skew:                           1.995   Prob(JB):                     2.67e-08  
Kurtosis:                       6.461   Cond. No.                         930.  
==============================================================================  
  
Notes:  
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

There is way more output than we need.

### Step 8: Add the Regression Line to the Scatterplot

**Action:** Visualize the regression line on the scatterplot.

```
# Generate predicted values  
y_pred = model.predict(X)  
  
# Plot scatterplot with regression line  
plt.scatter(data['Area'], data['Species'], color='blue', label='Data Points')  
plt.plot(data['Area'], y_pred, color='red', label='Regression Line')  
plt.title('Scatterplot with Regression Line')  
plt.xlabel('Island Area (sq km)')  
plt.ylabel('Number of Species')  
plt.legend()  
plt.grid(True)  
plt.show()
```

**Output:**

[![Scatterplot with Regression Line of Island Area vs Species. ](https://moringa.instructure.com/courses/1426/files/631866/download)](https://moringa.instructure.com/courses/1426/files/631866/download "Scatterplot with Regression Line of Island Area vs Species. ")

### Considerations

When summarizing bivariate data, it’s essential to ensure the dataset is suitable for analysis by confirming variables are numeric and free of missing values.

* **Adding a constant term (
  ![b 0](https://learning.flatironschool.com/equation\_images/b\_0?scale=1)
  b0) for the intercept** is crucial for accurate regression modeling, as omitting it forces the regression line through the origin, which may not reflect the data accurately.
* **Scatterplots** are a powerful tool to visualize relationships, but they can be misleading if the data contains noise, outliers, or non-linear patterns.
* The **regression coefficients (
  ![b 0](https://learning.flatironschool.com/equation\_images/b\_0?scale=1)
  b0 and
  ![b 1](https://learning.flatironschool.com/equation\_images/b\_1?scale=1)
  b1) and the correlation coefficient (*r*)** provide critical insights, but their interpretation must align with the data's context. For example,
  ![b 0](https://learning.flatironschool.com/equation\_images/b\_0?scale=1)
  b0 might not be meaningful if
  ![x equals 0](https://learning.flatironschool.com/equation\_images/x%2520%253D%25200?scale=1)
  x=0 is outside the observed range.
* Additionally, while ***r*** measures the strength and direction of a linear relationship, it does not capture non-linear patterns.

Understanding these potential challenges and decision points ensures learners can confidently summarize bivariate data and draw meaningful conclusions.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248806

Scraped At: 2026-05-15T10:27:08.755373
