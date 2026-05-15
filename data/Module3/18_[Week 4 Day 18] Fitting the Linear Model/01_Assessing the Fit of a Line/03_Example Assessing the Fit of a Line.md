# Example: Assessing the Fit of a Line

# Example: Assessing the Fit of a Line

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Example: Assessing the Fit of a Line

Icon Progress Bar (browser only)

1 min read

An e-commerce company wants to predict daily sales based on advertising spend.

To ensure their model is reliable, they:

1. **Compute
   ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
   :** Evaluate how much variability in sales is explained by advertising spend.
2. **Generate Residual Plots:** Confirm that residuals are randomly distributed.
3. **Identify Influential Values:** Use Cook’s Distance to flag points impacting the model disproportionately.

```
import statsmodels.api as sm  
import matplotlib.pyplot as plt  
import numpy as np  
  
# Example data  
X = np.random.rand(50, 1) * 100  # Advertising spend  
y = 3 * X.flatten() + np.random.normal(size=50, scale=10)  # Daily sales  
  
# Fit model  
X_const = sm.add_constant(X)  
model = sm.OLS(y, X_const).fit()  
  
# Residuals  
residuals = model.resid  
  
# Residual plot  
plt.scatter(model.predict(X_const), residuals)  
plt.axhline(0, color='red', linestyle='--')  
plt.xlabel('Predicted Values')  
plt.ylabel('Residuals')  
plt.title('Residual Plot')  
plt.show()
```

![Residual plot chart of predicted values.](https://moringa.instructure.com/courses/1426/files/631856/download)

We’ll see how to do each one of these steps and interpret them as we continue.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248816

Scraped At: 2026-05-15T10:28:12.029764
