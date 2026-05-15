# Technical Lesson: Binary Logistic Regression

# Technical Lesson: Binary Logistic Regression

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Technical Lesson: Binary Logistic Regression

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

**Binary logistic regression** is a fundamental technique for modeling situations where the outcome variable has two categories, such as success/failure or presence/absence.

**This lesson demonstrates the use of binary logistic regression with the Galapagos Islands dataset, focusing on predicting whether an island is "isolated" or "connected"** based on its distance to the nearest neighboring island. By converting the Nearest variable into a binary format (Nearest\_Binary), the problem becomes a clear classification task. Specifically, islands with Nearest values greater than the median are classified as "isolated" (1), while those at or below the median are classified as "connected" (0). This transformation simplifies the analysis and aligns with the biological and ecological context of the data.

A junior data scientist might apply such a transformation to answer practical questions in conservation or ecology, such as determining how island isolation influences species distribution or ecological traits. **By creating a binary variable,** **the analysis can focus on comparing two distinct groups (isolated vs. connected islands), enabling actionable insights**. This approach not only enhances interpretability but also sets up a straightforward framework for logistic regression, where the coefficients will explain how predictors like area, elevation, and adjacency influence the likelihood of an island being classified as isolated. This process demonstrates the importance of defining clear research questions and preparing data in ways that provide meaningful answers.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of binary logistic regression.

[VIDEO LINK](https://player.vimeo.com/video/1060372138?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

#### [Step 1. Load, Explore, and Split the Data](#dpPanel0)

```
# ! pip install faraway  
  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  
from sklearn.linear_model import LogisticRegression  
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report  
from statsmodels.stats.outliers_influence import variance_inflation_factor  
  
# Data  
from faraway.datasets import galapagos
```

```
# Load the data  
data = galapagos.load()  
  
# Inspect the data  
print(data.head())  
print(data.info())  
  
# Define predictors and response variable  
X = data[['Area', 'Elevation', 'Nearest']]  # Example predictors  
y = data['Species']  # Response (binary outcome: presence/absence)  
  
# Split data into training and testing sets  
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**Output:**

```
        Species  Area  Elevation  Nearest  Scruz  Adjacent  
Baltra       58  25.09       346      0.6    0.6     1.84  
Bartolome    31   1.24       109      0.6   26.3   572.33  
Caldwell      3   0.21       114      2.8   58.7     0.78  
Champion     25   0.10        46      1.9   47.4     0.18  
Coamano       2   0.05        77      1.9    1.9   903.82  
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
```

```
# Create subplots  
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  
  
# Plot Species vs. Area  
axes[0, 0].scatter(data['Species'], data['Area'])  
axes[0, 0].set_xlabel('Species')  
axes[0, 0].set_ylabel('Area')  
axes[0, 0].set_title('Species vs. Area')  
axes[0,0].grid(alpha=0.3)  
  
# Plot Species vs. Elevation  
axes[0, 1].scatter(data['Species'], data['Elevation'])  
axes[0, 1].set_xlabel('Species')  
axes[0, 1].set_ylabel('Elevation')  
axes[0, 1].set_title('Species vs. Elevation')  
axes[0, 1].grid(alpha=0.3)  
  
  
# Plot Species vs. Nearest  
axes[1, 0].scatter(data['Species'], data['Nearest'])  
axes[1, 0].set_xlabel('Species')  
axes[1, 0].set_ylabel('Nearest')  
axes[1, 0].set_title('Species vs. Nearest')  
axes[1,0].grid(alpha=0.3)  
  
  
# Plot Species vs. Scruz  
axes[1, 1].scatter(data['Species'], data['Scruz'])  
axes[1, 1].set_xlabel('Species')  
axes[1, 1].set_ylabel('Scruz')  
axes[1, 1].set_title('Species vs. Scruz')  
axes[1,1].grid(alpha=0.3)  
  
  
plt.tight_layout()  # Adjust spacing between subplots  
plt.show()
```

**Output:**

[![Output of four plots: Species vs. Area, Species vs. Elevation, Species vs. Nearest, Species vs. Scruz.](https://moringa.instructure.com/courses/1426/files/631891/download)](https://moringa.instructure.com/courses/1426/files/631891/download "Output of four plots: Species vs. Area, Species vs. Elevation, Species vs. Nearest, Species vs. Scruz.")

```
# Define predictors and response variable  
X = data[['Area', 'Elevation', 'Adjacent']]  # Example predictors  
  
# Calculate the median of the Nearest column  
median_nearest = data['Nearest'].median()  
  
# Create the Nearest_Binary column  
y= data['Nearest_Binary'] = (data['Nearest'] > median_nearest).astype(int)  
  
# Inspect the new column  
print(data[['Nearest', 'Nearest_Binary']].head(8))
```

**Output:**

```
             Nearest  Nearest_Binary  
Baltra            0.6               0  
Bartolome         0.6               0  
Caldwell          2.8               0  
Champion          1.9               0  
Coamano           1.9               0  
Daphne.Major      8.0               1  
Daphne.Minor      6.0               1  
Darwin           34.1               1
```

```
# Count the occurrences of 0 and 1  
binary_counts = y.value_counts()  
  
# Print the counts  
print("Counts of 0 and 1 in Species_Binary:")  
print(binary_counts)
```

**Output:**

```
Counts of 0 and 1 in Species_Binary:  
Nearest  
0    15  
1    15  
Name: count, dtype: int64
```

```
# Split data into training and testing sets  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  
  
  
print("X_train dimensions:", X_train.shape)  
print("X_test dimensions:", X_test.shape)  
print("y_train dimensions:", y_train.shape)  
print("y_test dimensions:", y_test.shape)
```

**Output:**

```
X_train dimensions: (24, 3)  
X_test dimensions: (6, 3)  
y_train dimensions: (24,)  
y_test dimensions: (6,)
```

**Interpretation:** The dataset contains 30 records with six variables. The target variable, Species, represents a count that will later be transformed into a binary classification target. Predictors Area, Elevation, and Nearest are selected as independent variables. The data is successfully split into training (24 observations) and testing (6 observations) subsets.

#### [Step 2. Scale the Predictors](#dpPanel1)

```
# Scale the predictors  
scaler = StandardScaler()  
  
# Transform training and testing predictors  
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)  
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)  
  
# Get dimensions  
print("Dimensions of X_train_scaled:", X_train_scaled.shape)  
print("Dimensions of X_test_scaled:", X_test_scaled.shape)
```

**Output:**

```
Dimensions of X_train_scaled: (24, 3)  
Dimensions of X_test_scaled: (6, 3)
```

**Interpretation:** The predictors are scaled to standardize their range for better performance of logistic regression. The scaled training and testing datasets maintain the same dimensions as the original splits, ensuring no data is lost during preprocessing.

#### [Step 3. Fit the Logistic Regression Model](#dpPanel2)

```
# Fit logistic regression model on scaled data  
model = LogisticRegression(max_iter=1000)  
model.fit(X_train_scaled, y_train)  
  
# Output coefficients  
print("Intercept:", model.intercept_)  
print("Coefficients:", model.coef_)
```

**Output:**

```
Intercept: [0.36853881]  
Coefficients: [[-0.54318024  0.75656123  0.05697516]]
```

**Interpretation:** The logistic regression model has been trained. The intercept is approximately .36, and the coefficients indicate the influence of Area, Elevation, and Nearest on the log-odds of the binary response variable.

#### [Step 4: Make Predictions](#dpPanel3)

```
# Predict probabilities and classes  
y_pred_prob = model.predict_proba(X_test_scaled)[:, 1]  
y_pred_class = model.predict(X_test_scaled)  
  
# Display predictions  
print("Predicted Probabilities:", y_pred_prob[:5])  
print("Predicted Classes:", y_pred_class[:5])
```

**Output:**

```
Predicted Probabilities: [0.54407974 0.00074678 0.63293308 0.4764621  0.50250907]  
Predicted Classes: [1 0 1 0 1]
```

**Interpretation:** The predicted probabilities reflect the likelihood of each test observation belonging to the positive class. Predictions are converted into binary classes based on a default threshold of 0.5, correctly capturing the model's decision boundary.

#### [Step 5: Evaluate the Model](#dpPanel4)

```
# Evaluate model performance  
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_class))  
print("Accuracy Score:", accuracy_score(y_test, y_pred_class))  
print("Classification Report:\n", classification_report(y_test, y_pred_class))
```

**Output:**

```
Confusion Matrix:  
 [[1 4]  
 [1 0]]  
Accuracy Score: 0.16666666666666666  
Classification Report:  
               precision    recall  f1-score   support  
  
           0       0.50      0.20      0.29         5  
           1       0.00      0.00      0.00         1  
  
    accuracy                           0.17         6  
   macro avg       0.25      0.10      0.14         6  
weighted avg       0.42      0.17      0.24         6
```

**Interpretation:** The model achieves an accuracy of 17%. The confusion matrix highlights four misclassifications for the positive class.

#### [Step 6: Check Assumptions and Diagnostics](#dpPanel5)

```
# Check multicollinearity using VIF  
vif = pd.DataFrame()  
vif["Variable"] = X_train.columns  
vif["VIF"] = [variance_inflation_factor(X_train_scaled.values, i) for i in range(X_train_scaled.shape[1])]  
print(vif)
```

**Output:**

```
 Variable       VIF  
0       Area  2.814390  
1  Elevation  4.149119  
2   Adjacent  1.891136
```

**Interpretation:** Variance Inflation Factor (VIF) values for all predictors are below 5, indicating no severe multicollinearity issues. This ensures that each predictor contributes independently to the model.

### Considerations

When applying binary logistic regression to the Galapagos Islands dataset, **key challenges may arise in variable selection, scaling, and assumption validation.** Choosing predictors like Area, Elevation, and Nearest is critical, as their relevance directly impacts the model's interpretability and performance. A **potential issue is the inclusion of irrelevant predictors**, which may lead to overfitting or inflated multicollinearity. This was mitigated by calculating Variance Inflation Factor (VIF), confirming that multicollinearity is not severe in this dataset.

**Scaling the predictors ensures that the coefficients are on the same scale,** improving convergence and interpretability, but introduces additional preprocessing steps that must be consistently applied to training and testing sets. The binary transformation of the response variable (Species) highlights a decision-making point; you must ensure the response variable aligns with the research question.

For instance, defining species presence as Species > 0 provides a clear and biologically meaningful target. Understanding these steps and their implications is essential for robust and generalizable logistic regression models.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248909

Scraped At: 2026-05-15T10:39:14.814521
