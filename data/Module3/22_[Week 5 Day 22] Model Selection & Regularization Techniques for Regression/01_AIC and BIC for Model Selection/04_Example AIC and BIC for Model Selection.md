# Example: AIC and BIC for Model Selection

# Example: AIC and BIC for Model Selection

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Example: AIC and BIC for Model Selection

Icon Progress Bar (browser only)

4 min read

![](https://moringa.instructure.com/courses/1426/files/631805/download)
As a junior data analyst at a real estate analytics company, your task is to develop a model to predict housing prices using available housing features. The company requires a model that strikes a balance between accuracy and simplicity, ensuring that it can be deployed efficiently for quick, actionable insights.

The dataset provided is the Boston Housing dataset, which includes various predictors such as:

* The per capita crime rate by town (**CRIM**)
* The average number of rooms per dwelling (**RM**)
* The percentage of lower-status population (**LSTAT**)
* The property tax rate (**TAX**)

Your challenge is to build and compare multiple regression models using **AIC (Akaike Information Criterion)** and **BIC (Bayesian Information Criterion)** to determine the best model while avoiding overfitting or unnecessary complexity.

### Steps to Determine the Best Model

* **Explore the Dataset**Before building a model, it is essential to explore the dataset. This involves **checking its structure, identifying the target variable (medv, representing median home values), and understanding the potential predictors.** A thorough review helps identify any missing values or inconsistencies, ensuring that the dataset is suitable for analysis. Understanding the data also allows you to determine which variables might be most relevant for predicting housing prices.
* **Fit the Full Model and Create Subset Models**A **full regression model is built** using all available predictors as a baseline for comparison. While this model provides a comprehensive view of the data, it may include unnecessary predictors, leading to increased complexity. To assess the model’s quality, AIC and BIC values are calculated. AIC measures how well a model fits the data while penalizing unnecessary complexity, with lower values indicating a better model. Similarly, BIC applies an even stricter penalty for including too many predictors, making it useful for selecting a simpler model that still provides strong predictive performance. While the full model typically achieves the lowest AIC and BIC, it may not be the most practical choice for deployment, as excessive complexity can reduce interpretability and computational efficiency.
* **Compare Models**  
    
  To find a more efficient model, you **test simplified versions using subsets of predictors**. One model includes RM (average rooms per dwelling) and LSTAT (lower-status percentage), capturing key factors affecting housing prices. Another model builds on this by adding CRIM (crime rate), introducing an additional explanatory variable. Comparing these models’ AIC and BIC values reveals how much predictive power is lost or gained with each modification. A model with too few predictors may oversimplify the problem and miss important patterns, while a model with too many predictors risks overfitting to the training data. The goal is to find a model that maintains high predictive accuracy without unnecessary complexity.
* **Select Best Model**  
  After evaluating the results, the **model including RM, LSTAT, and CRIM emerges as the best choice**. It has the lowest AIC and BIC among the subset models, striking a balance between simplicity and performance. While the full model technically has lower AIC and BIC, its added complexity does not justify the marginal improvement in fit. The selected model remains interpretable, allowing stakeholders to understand how housing prices are influenced by room size, socioeconomic status, and crime rates: factors that can directly inform business decisions in real estate analytics.
* **Validate and Interpret Results**  
  Model selection using AIC and BIC is particularly valuable in real-world applications. It **ensures predictive accuracy by optimizing model fit while discouraging unnecessary complexity**. Additionally, an interpretable model allows businesses to explain key drivers of housing prices, supporting data-driven decision-making. Finally, a simpler model is computationally efficient, making it easier to deploy for daily operations.

By applying AIC and BIC, you have systematically selected a model that balances accuracy and complexity. This approach is a critical skill in data analysis, ensuring that models are not only statistically sound but also practical for real-world applications.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248888

Scraped At: 2026-05-15T10:36:45.547237
