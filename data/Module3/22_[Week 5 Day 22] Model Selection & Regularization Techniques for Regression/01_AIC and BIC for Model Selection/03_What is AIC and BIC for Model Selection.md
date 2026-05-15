# What is AIC and BIC for Model Selection?

# What is AIC and BIC for Model Selection?

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) What is AIC and BIC for Model Selection?

Icon Progress Bar (browser only)

6 min read

Model Selection is the process of identifying the best statistical model among a set of candidate models based on their performance and complexity. In the context of Multiple Linear Regression, the objective is to **balance the tradeoff** between:

* **Model Fit:** How well the model explains the data.
* **Model Complexity:** The number of predictors included.

Two widely used criteria for model selection are:

* Akaike Information Criterion (AIC)
* Bayesian Information Criterion (BIC)

Both metrics provide a quantitative way to compare models by considering their fit (via likelihood) and complexity (via the number of predictors).

### How Does AIC and BIC for Model Selection Work?

AIC and BIC are based on the **log-likelihood of a model**, which measures how well the model fits the data. However, adding more predictors can artificially improve the log-likelihood, leading to overfitting. To address this, both AIC and BIC penalize models for having too many predictors, ensuring a balance between accuracy and simplicity.

**Explanation of Log-Likelihood in this context:** In the context of AIC and BIC for model selection, the log-likelihood measures how well a statistical model fits the observed data. It quantifies the probability of the observed data given the model parameters.

#### What is Log-Likelihood?

While this is a deep and complex statistical topic, to properly understand how AIC and BIC work, we need to see a few words about log-likelihood without getting lost in the minutia.

The **likelihood LL** represents the probability of observing the data under a given model. The log-likelihood (
![ln left parenthesis ModifyingAbove upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Cln(%255Chat%257BL%257D)?scale=1)
) is simply the natural logarithm of the likelihood function:

![ln left parenthesis ModifyingAbove upper L With caret right parenthesis equals sigma summation Underscript i equals 1 Overscript n Endscripts ln left parenthesis f left parenthesis y Subscript i Baseline comma theta right parenthesis right parenthesis](https://learning.flatironschool.com/equation\_images/%255Cln(%255Chat%257BL%257D)%2520%253D%2520%255Csum\_%257Bi%253D1%257D%255En%2520%255Cln(f(y\_i%252C%2520%255Ctheta))?scale=1)

Where:

* ![f left parenthesis y Subscript i Baseline comma theta right parenthesis](https://learning.flatironschool.com/equation\_images/f(y\_i%252C%2520%255Ctheta)?scale=1)
  : The probability density function for the response variable yiy\_i given the model parameters θ\theta.
* *n*: Number of observations.

#### Why Use Log-Likelihood?

1. **Simplification:** The log transformation turns the product of probabilities into a sum, making calculations more manageable.
2. **Fit Quality:** A higher log-likelihood means the model fits the data better.
3. **Connection to AIC and BIC:** AIC and BIC incorporate the log-likelihood to measure model fit, penalizing for unnecessary complexity.

#### Log-Likelihood in AIC and BIC

* **In AIC and BIC formulas**:  
  + ![ln left parenthesis ModifyingAbove upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Cln(%255Chat%257BL%257D)?scale=1)
    represents how well the model explains the data.
  + A model with a higher
    ![ln left parenthesis ModifyingAbove upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Cln(%255Chat%257BL%257D)?scale=1)
    has a better fit but may risk overfitting.
* **AIC and BIC correct for overfitting** by adding penalties for the number of parameters kk:  
  + **AIC**:
    ![2 k minus 2 ln left parenthesis ModifyingAbove upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/2k%2520-%25202%255Cln(%255Chat%257BL%257D)?scale=1)
  + **BIC**:
    ![k ln left parenthesis n right parenthesis minus 2 ln left parenthesis ModifyingAbove upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/k%2520%255Cln(n)%2520-%25202%255Cln(%255Chat%257BL%257D)?scale=1)

The log-likelihood measures the fit of the model to the data. A higher log-likelihood indicates a better fit, but when used in AIC and BIC, it is adjusted for complexity to avoid overfitting. For students exploring further, understanding the likelihood function is key to appreciating how models are evaluated statistically.

### Formulas and Explanation of the Information Criteria

#### Akaike Information Criterion (AIC)

---

The **formula for AIC** is:

![AIC equals 2 k minus 2 ln left parenthesis ModifyingAbove upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257BAIC%257D%2520%253D%25202k%2520-%25202%255Cln(%255Chat%257BL%257D)?scale=1)

Where:

* *k* = number of parameters in the model (including the intercept).
* ![ModifyingAbove upper L With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257BL%257D?scale=1)
  = maximum value of the likelihood function of the model.

**Interpretation:**

* A smaller AIC value indicates a better model.
* AIC rewards models with a better fit (higher likelihood) but penalizes those with more parameters.

#### Bayesian Information Criterion (BIC)

---

The **formula for BIC** is:

![BIC equals k ln left parenthesis n right parenthesis minus 2 ln left parenthesis ModifyingAbove upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257BBIC%257D%2520%253D%2520k%2520%255Cln(n)%2520-%25202%255Cln(%255Chat%257BL%257D)?scale=1)

Where:

* *n* = number of observations in the dataset.
* *k* = number of parameters in the model.
* ![upper L With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257BL%257D?scale=1)
  = maximum likelihood estimate.

**Interpretation:**

* Like AIC, a smaller BIC value indicates a better model.
* BIC applies a stronger penalty for the number of parameters (
  ![k](https://learning.flatironschool.com/equation\_images/k?scale=1)
  ) due to the
  ![ln left parenthesis n right parenthesis](https://learning.flatironschool.com/equation\_images/%255Cln(n)?scale=1)
  term, which grows with sample size.
* This makes BIC more likely to favor simpler models than AIC, particularly when the dataset is large.

##### AIC vs. BIC

AIC vs BIC Comparison

| Criterion | Focus | Penalty for Complexity | Use Case |
| --- | --- | --- | --- |
| AIC | Prioritizes prediction accuracy | Penalizes ![2 k](https://learning.flatironschool.com/equation\_images/2k?scale=1) | Best when predictive performance is critical. |
| BIC | Balances fit and simplicity | Penalizes ![k ln left parenthesis n right parenthesis](https://learning.flatironschool.com/equation\_images/k%255Cln(n)?scale=1) | Best when interpretability is key or for larger datasets. |

**Key Comparison:**

* AIC tends to favor more complex models because it penalizes complexity less.
* BIC is stricter and leans toward simpler models, making it more conservative.

### How AIC and BIC Compare to Adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1.470375)

Adjusted
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
is another metric used for model selection. It modifies
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
(which measures how well the model explains the variance in the response variable) by penalizing the addition of unnecessary predictors.

**Formula for Adjusted
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
:**

![Adjusted upper R squared equals 1 minus StartFraction left parenthesis 1 minus upper R squared right parenthesis left parenthesis n minus 1 right parenthesis Over n minus k minus 1 EndFraction](https://learning.flatironschool.com/equation\_images/%255Ctext%257BAdjusted%2520%257D%2520R%255E2%2520%253D%25201%2520-%2520%255Cfrac%257B(1%2520-%2520R%255E2)(n%2520-%25201)%257D%257Bn%2520-%2520k%2520-%25201%257D?scale=1)

Where:

* ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  = regular R-squared value.
* *n* = number of observations.
* *k* = number of predictors.

#### **Comparison**

Comparison of AIC, BIC, and Adjusted
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)

| Metric | Purpose | Penalty for Complexity | Focus |
| --- | --- | --- | --- |
| AIC | Balances fit and complexity. | Penalizes based on ![2 k](https://learning.flatironschool.com/equation\_images/2k?scale=0.875) . | Prediction accuracy. |
| BIC | Balances fit and complexity (stronger). | Penalizes based on ![k ln left parenthesis n right parenthesis](https://learning.flatironschool.com/equation\_images/k%255Cln(n)?scale=1) . | Model simplicity and parsimony. |
| Adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1) | Adjusts ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1) for added predictors. | Based on sample size and predictors. | Explains variance while penalizing unnecessary predictors. |

**Key Insight:**

* Adjusted
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  works well for comparing models within a frequentist framework but does not directly use the likelihood like AIC and BIC.
* AIC and BIC offer a more comprehensive comparison of models by incorporating likelihood and explicitly penalizing complexity.

  ---

#### **Significance in Data Science**

In data science, selecting the best model is crucial for building accurate, interpretable, and deployable solutions.

* AIC is widely used in predictive modeling when the goal is accuracy, such as forecasting sales or predicting housing prices.
* BIC is preferred in situations where model interpretability matters, such as medical research or economic analysis.

### Why AIC and BIC Are Generally Better Than Adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1.470375)

1. **Likelihood-Based Comparison:**
   * AIC and BIC explicitly use the log-likelihood (
     ![ln left parenthesis upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Cln(%255Chat%257BL%257D)?scale=1)
     ) to evaluate model fit. This gives a more robust measure of how well the model explains the observed data.
   * Adjusted 
     ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
     focuses only on explaining variance and does not directly assess the likelihood of the data.
2. **Penalty for Complexity:**
   * Both AIC and BIC penalize model complexity by adding a term proportional to the number of parameters (*k*).
   * BIC applies an even stronger penalty, especially for large sample sizes (*n*), making it less likely to overfit.
   * Adjusted
     ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
     , while penalizing complexity, does not adapt as strongly to the sample size or likelihood.
3. **Flexibility in Context:**
   * AIC is preferred for situations where predictive accuracy is the primary goal.
   * BIC is ideal when the model needs to be interpretable, such as in scientific research or situations where simpler models are preferred.
   * Adjusted 
     ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
     works well for quick comparisons but does not offer the same depth of evaluation as AIC and BIC.

While Adjusted 
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
provides a useful measure for comparing models in simpler cases, AIC and BIC are generally more powerful tools for model selection because they account for both the likelihood of the data and model complexity.

* AIC is suitable when the focus is on prediction and accuracy.
* BIC is better for achieving simplicity and avoiding overfitting, particularly with larger datasets.

By understanding the strengths and trade-offs of AIC, BIC, and Adjusted
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
, you can make more informed decisions in selecting models that balance performance, complexity, and interpretability: critical skills in real-world data analysis.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248887

Scraped At: 2026-05-15T10:36:39.356882
