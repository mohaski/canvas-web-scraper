# Technical Lesson: Assessing the Fit of a Line

# Technical Lesson: Assessing the Fit of a Line

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: Assessing the Fit of a Line

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In linear regression, understanding how well a model fits the data is critical to ensuring reliable predictions and meaningful insights. This process involves evaluating the model's ability to explain variability, diagnosing issues through residual analysis, and identifying data points that might disproportionately influence the regression results.

### Problem-Solving Approach

Imagine you are a data scientist tasked with predicting sales based on advertising spend for a marketing campaign. While your regression model may produce a fitted line and summary statistics, how do you know if it represents the data accurately? Are there outliers or influential points skewing your results? Does the model meet key assumptions?

To address these questions, you will follow a systematic approach to assess the fit of the regression model. This lesson provides technical steps to:

* Visualize data to uncover initial relationships and patterns.
* Fit a regression model and overlay the regression line with the correlation coefficient.
* Diagnose potential issues through **![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)**, residual analysis, and influential point detection

#### Key Parts of the Process

* **Compute
  ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
  :** Evaluate how much variability in the dependent variable is explained by the independent variable.  
  + **Challenge**: Misinterpreting **![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)** as a measure of prediction accuracy rather than variability explained.
* **Analyze Residuals:** Examine residual plots to ensure randomness and detect patterns.
  + **Challenge**: Identifying subtle patterns like non-linearity or heteroscedasticity that violate regression assumptions.
* **Identify Influential Observations:** Use diagnostics like Cook’s Distance to pinpoint data points that might disproportionately affect the model.  
  + **Challenge**: Balancing quantitative diagnostics with qualitative judgment to decide whether to retain or remove points.

By mastering this process, you will develop the skills to critically assess the performance of a regression model, ensuring its reliability and applicability in real-world scenarios. This structured approach transforms raw data into actionable insights while addressing specific challenges that arise during regression analysis.

### Video: Fitting Linear Models

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of assessing the fit of a line.

[VIDEO LINK](https://player.vimeo.com/video/1060371703?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Resources

* Jupyter Notebook and/or Integrated Development Environment (IDE) for Python like Colab VS Code.

### Instructions

#### Step 1. Import Required Libraries

**Action:** Import the necessary libraries for data manipulation, visualization, and regression analysis.

```
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
import statsmodels.api as sm
```

#### Step 2. Load and Inspect the Dataset

**Action:** Load the dataset and examine its structure to ensure it contains numeric variables suitable for regression analysis.

```
# Generate dataset: Advertising spend vs. sales  
np.random.seed(42)  # For reproducibility  
  
# Generate normal data  
advertising = np.random.rand(48) * 100  # Independent variable  
sales = 3 * advertising + np.random.normal(size=48, scale=10)  # Dependent variable  
  
# Introduce an outlier (large residual, near center of x-values)  
advertising = np.append(advertising, [50])  # Near the center of x  
sales = np.append(sales, [500])  # Very high y value (outlier)  
  
# Introduce an influential point (high leverage, near regression line)  
advertising = np.append(advertising, [200])  # Extreme x value  
sales = np.append(sales, [400])  # Close to the regression line  
  
   
  
# Create the DataFrame  
data = pd.DataFrame({'Advertising': advertising, 'Sales': sales})  
  
# Display the first few rows  
print(data.head())  
  
# Check data informat  
print(data.info())
```

**Output:**

```
Advertising       Sales  
0    37.454012   99.080175  
1    95.071431  287.182904  
2    73.199394  226.982848  
3    59.865848  181.311228  
4    15.601864   45.649109  
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 50 entries, 0 to 49  
Data columns (total 2 columns):  
 #   Column       Non-Null Count  Dtype    
---  ------       --------------  -----    
 0   Advertising  50 non-null     float64  
 1   Sales        50 non-null     float64  
dtypes: float64(2)  
memory usage: 928.0 bytes  
None
```

#### Step 3. Define Variables

**Action:** Assign the independent (*x*) and dependent (*y*) variables. Add a constant term for the regression.

```
# Define independent and dependent variables  
X = sm.add_constant(data['Advertising'])  # Add constant for intercept  
y = data['Sales']  
  
# Check dimensions  
print(f"X shape: {X.shape}")  
print(f"y shape: {y.shape}")
```

**Output:**

```
X shape: (50, 2)  
y shape: (50,)
```

#### Step 4. Create Scatterplot

**Action:** Visualize the relationship between the independent and dependent variables.

```
# Create scatterplot  
plt.scatter(data['Advertising'], data['Sales'], color='blue', label='Data Points')  
plt.title('Scatterplot: Advertising vs. Sales')  
plt.xlabel('Advertising Spend ($)')  
plt.ylabel('Sales ($)')  
plt.legend()  
plt.grid(True)  
plt.show()
```

**Output:**

![Scatterplot output of advertising vs. sales.](https://moringa.instructure.com/courses/1426/files/631878/download)

#### Step 5. Fit the Regression Model and Add Regression Line

**Action:** Fit the regression model, compute the regression line, calculate the correlation coefficient (*r*), and overlay the regression line on the scatterplot.

```
# Fit the regression model  
model = sm.OLS(y, X).fit()  
  
# Compute regression line  
y_pred = model.predict(X)  
  
# Calculate correlation coefficient (r)  
r = np.corrcoef(data['Advertising'], data['Sales'])[0, 1]  
  
# Scatterplot with regression line and r value  
plt.scatter(data['Advertising'], data['Sales'], color='blue', label='Data Points')  
plt.plot(data['Advertising'], y_pred, color='red', label='Regression Line')  
plt.title(f'Scatterplot: Advertising vs. Sales\nCorrelation Coefficient (r): {r:.2f}')  
plt.xlabel('Advertising Spend ($)')  
plt.ylabel('Sales ($)')  
plt.legend()  
plt.grid(True)  
plt.show()  
  
# Print the regression line equation  
b0 = model.params['const']  
b1 = model.params['Advertising']  
print(f"Regression Line: y = {b0:.2f} + {b1:.2f}x")
```

**Output:**

![Scatterplot output of advertising vs. sales with regression line.](https://moringa.instructure.com/courses/1426/files/631880/download)

```
Regression Line: y = 24.58 + 2.54x
```

#### Step 6. Compute **![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)**

**Action:** Compute **![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)** to evaluate the explanatory power of the model.

```
# Compute R-squared  
r_squared = model.rsquared  
print(f"R-squared: {r_squared:.2f}")
```

**Output:**

```
R-squared: 0.73
```

#### Step 7. Analyze Residuals

**Action:** Extract residuals and create a residual plot to check for randomness and adherence to assumptions.

```
# Extract residuals  
residuals = model.resid  
  
# Create a residual plot  
plt.scatter(model.fittedvalues, residuals, color='blue')  
plt.axhline(0, color='red', linestyle='--')  
plt.xlabel('Predicted Values')  
plt.ylabel('Residuals')  
plt.title('Residual Plot')  
plt.grid(True)  
plt.show()
```

**Output:**

![Residual plot output of predicted values.](https://moringa.instructure.com/courses/1426/files/631868/download)

#### Step 8: Identify Influential Observations

**Action:** Use Cook’s Distance to identify influential points.

```
# Compute Cook's Distance  
influence = model.get_influence()  
cooks_d = influence.cooks_distance[0]  
  
# Plot Cook's Distance  
plt.stem(np.arange(len(cooks_d)), cooks_d, basefmt=" ")  
plt.title("Cook's Distance")  
plt.xlabel("Observation Index")  
plt.ylabel("Cook's Distance")  
plt.axhline(1, color='red', linestyle='--')  # Threshold line  
plt.show()  
  
# Print observations with high Cook's Distance  
high_influence_points = np.where(cooks_d > 1)[0]  
print(f"High influence points: {high_influence_points}")
```

**Output:**

![Cook&#39;s Distance output](https://moringa.instructure.com/courses/1426/files/631882/download)

#### Step 9: Diagnose Outliers

**Action:** Identify data points that deviate significantly from the regression line.

```
# Extract standardized residuals  
standardized_residuals = influence.resid_studentized_internal  
  
# Plot standardized residuals  
plt.scatter(np.arange(len(standardized_residuals)), standardized_residuals, color='blue')  
plt.axhline(3, color='red', linestyle='--')  # Upper threshold  
plt.axhline(-3, color='red', linestyle='--')  # Lower threshold  
plt.title('Standardized Residuals')  
plt.xlabel('Observation Index')  
plt.ylabel('Standardized Residual')  
plt.grid(True)  
plt.show()  
  
# Print potential outliers  
outliers = np.where((standardized_residuals > 3) | (standardized_residuals < -3))[0]  
print(f"Potential outliers: {outliers}")
```

**Output:**

![Standardized residuals output.](https://moringa.instructure.com/courses/1426/files/631876/download)

### Common Challenges

#### Generating and Inspecting Data

* **Challenge:** Ensuring the dataset includes realistic data points, particularly for introducing outliers and influential points, can confuse learners who are new to these concepts.
* **Solution:** Clearly distinguish between points that are purely outliers, purely influential, or both. Use explicit examples to show their effects on the model.
* **Impact:** Misclassifying data points can lead to incorrect interpretations of regression diagnostics.
* **Pros:** Real-world examples enhance understanding of statistical anomalies.
* **Cons:** Adding such points may seem artificial or overly contrived if not properly contextualized.

#### Visualizing the Data

* **Challenge:** Learners may overlook the importance of visualizing the data with scatterplots before fitting the regression model.
* **Solution:** Emphasize the role of scatterplots in detecting potential non-linear patterns, clusters, or anomalies before proceeding to model fitting.
* **Impact:** Failing to create an initial scatterplot can result in incorrectly applying linear regression to non-linear relationships.
* **Pros:** Provides an intuitive understanding of data trends.
* **Cons:** Over-reliance on visual inspection may lead to missed subtleties in large or noisy datasets.

#### Adding and Interpreting Regression Lines

* **Challenge:** Displaying the correlation coefficient (*r*) alongside the regression line can confuse learners if they equate
  ![r](https://learning.flatironschool.com/equation\_images/r?scale=1)
  directly with model fit.
* **Solution:** Clarify the distinction between *r* (measuring the strength of linearity) and **![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)** (measuring explained variability). Use both metrics to reinforce complementary insights.
* **Impact:** Misinterpreting *r* or **![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)** can lead to overconfidence in weak models or dismissal of valid ones.
* **Pros:** Combining *r* and the regression line in one plot provides comprehensive insight.
* **Cons:** Additional explanation may be needed for learners to differentiate these concepts.

#### Residual Analysis

* **Challenge:** Identifying patterns in residual plots (e.g., heteroscedasticity or non-linearity) requires practice and may not be immediately intuitive.
* **Solution:** Provide examples of common residual patterns and their interpretations, such as funnel shapes (heteroscedasticity) or curves (non-linearity).
* **Impact:** Misinterpreting residual patterns can lead to unaddressed assumption violations, reducing the model’s validity.
* **Pros:** Visualizing residuals enhances the diagnostic process.
* **Cons:** Residual plots can be subjective without proper training or guidelines.

#### Identifying Influential Observations

* **Challenge:** Cook’s Distance threshold (e.g., >1) can seem arbitrary, and learners may default to removing flagged points without understanding their context.
* **Solution:** Encourage learners to investigate flagged points to determine whether they are valid, errors, or anomalies critical to the analysis.
* **Impact:** Blindly removing influential points may oversimplify the dataset or erase meaningful trends.
* **Pros:** Diagnostics like Cook’s Distance provide quantitative measures for identifying influential data.
* **Cons:** Learners may overlook the need for qualitative judgment alongside quantitative metrics.

#### Diagnosing Outliers

* **Challenge:** Learners may struggle to differentiate between outliers that are meaningful anomalies and those that result from data entry errors or measurement issues.
* **Solution:** Explain the importance of context in handling outliers, emphasizing that removing outliers should only occur if they are confirmed to be errors or irrelevant.
* **Impact:** Removing meaningful outliers can lead to biased or incomplete models.
* **Pros:** Highlighting outliers aids in understanding their potential impact on model fit.
* **Cons:** Overemphasis on removing outliers risks oversimplifying complex datasets.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248819

Scraped At: 2026-05-15T10:28:31.110330
