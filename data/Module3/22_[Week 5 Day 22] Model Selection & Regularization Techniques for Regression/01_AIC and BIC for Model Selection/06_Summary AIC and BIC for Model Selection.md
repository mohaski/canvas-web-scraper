# Summary: AIC and BIC for Model Selection

# Summary: AIC and BIC for Model Selection

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Summary: AIC and BIC for Model Selection

Icon Progress Bar (browser only)

3 min read

### Terms Recap

* **Model Selection** is the process of choosing the most appropriate statistical model from a set of candidate models based on specific criteria. In the context of Multiple Linear Regression, model selection aims to balance:  
  + **Model Fit:** How well the model explains the observed data.
  + **Model Complexity:** The number of predictors included in the model.

* **AIC (Akaike Information Criterion):**
  + Focuses on predictive accuracy.
  + Often selects more complex models by penalizing complexity lightly.
  + Ideal for tasks where the primary goal is accurate predictions, such as machine learning or forecasting.
* **BIC (Bayesian Information Criterion):**
  + Applies a stronger penalty for model complexity, particularly for large datasets.
  + Tends to favor simpler models that are easier to interpret.
  + Best suited for situations where model interpretability and parsimony are critical, such as scientific research or explainable AI.

### Key Concepts

Model selection is a fundamental process in regression analysis because:

* **Avoids Overfitting:** Prevents models from capturing noise in the data by limiting unnecessary predictors.
* **Improves Interpretability:** Ensures the model remains simple, making it easier to explain and apply.
* **Enhances Accuracy:** Balances complexity and performance, resulting in models that generalize well to unseen data.
* **Optimizes Efficiency:** Reduces computational costs and improves deployment speed, particularly in production systems.

**Takeaways**

* AIC prioritizes accuracy and often selects more complex models.
* BIC heavily penalizes complexity, favoring simpler models, especially with larger datasets.
* Adjusted
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  is simpler and works well for variance-based comparisons but lacks the likelihood-based robustness of AIC and BIC.
* Choosing the appropriate metric depends on the problem:  
  + Use AIC for accuracy-driven tasks.
  + Use BIC for simplicity and interpretability.
  + Use Adjusted 
    ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
    for quick, variance-focused comparisons.

### Brief Process Overview

1. **Data Exploration and Preparation:** Understand the dataset and clean it for analysis.
2. **Fit the Full Model:** Build an initial model with all predictors and calculate AIC/BIC.
3. **Create Subset Models:** Develop models using smaller subsets of predictors.
4. **Compare Models:** Evaluate models systematically using AIC and BIC values.
5. **Select the Best Model:** Choose the model with the optimal balance of simplicity and fit.
6. **Validate and Interpret Results:** Ensure the selected model is robust and explainable.

### Resources

* [Original AIC Paper: "A New Look at the Statistical Model Identification"


  Links to an external site.](https://link.springer.com/article/10.1007/BF02288367)
* [Original BIC Paper: "Bayesian Model Selection in Social Research"


  Links to an external site.](https://projecteuclid.org/euclid.aos/1176344136)
* [Python Libraries Statsmodels Documentation


  Links to an external site.](https://www.statsmodels.org/stable/index.html)
  + Use statsmodels.OLS for building regression models and extracting AIC/BIC values.
  + Ensure the following Python libraries are installed:  

    ```
    ! pip install pandas statsmodels rdatasets
    ```
* [Boston Housing Dataset


  Links to an external site.](https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248890

Scraped At: 2026-05-15T10:36:56.586018
