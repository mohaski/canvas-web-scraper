# Process: AIC and BIC for Model Selection

# Process: AIC and BIC for Model Selection

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Process: AIC and BIC for Model Selection

Icon Progress Bar (browser only)

2 min read

The process for AIC and BIC for model selection includes the following steps:

1. **Data Exploration and Preparation:** Understand the dataset and clean it for analysis.
2. **Fit the Full Model:** Build an initial model with all predictors and calculate AIC/BIC.
3. **Create Subset Models:** Develop models using smaller subsets of predictors.
4. **Compare Models:** Evaluate models systematically using AIC and BIC values.
5. **Select the Best Model:** Choose the model with the optimal balance of simplicity and fit.
6. **Validate and Interpret Results:** Ensure the selected model is robust and explainable.

### Conceptualize AIC and BIC for Model Selection

Conceptualization Table of AIC and BIC for Model Selection

| Term | Definition | Purpose | Formula | Key Considerations |
| --- | --- | --- | --- | --- |
| Akaike Information Criterion (AIC) | A metric for model selection that balances goodness-of-fit and complexity. | To identify the model with the best predictive performance while penalizing for extra predictors. | ![AIC equals 2 k minus 2 ln left parenthesis upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257BAIC%257D%2520%253D%25202k%2520-%25202%255Cln(%255Chat%257BL%257D)?scale=0.875)  Where:   * ![k](https://learning.flatironschool.com/equation\_images/k?scale=0.875)   : Number of parameters * ![upper L With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257BL%257D?scale=0.875)   : Log-likelihood | AIC favors models with better fit and may select more complex models. Ideal for prediction tasks. |
| Bayesian Information Criterion (BIC) | A stricter model selection criterion that penalizes complexity more heavily than AIC. | To select simpler models that balance goodness-of-fit and parsimony, especially for larger datasets. | ![BIC equals k ln left parenthesis n right parenthesis minus 2 ln left parenthesis upper L With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257BBIC%257D%2520%253D%2520k%2520%255Cln(n)%2520-%25202%255Cln(%255Chat%257BL%257D)?scale=0.875)  Where:   * ![k](https://learning.flatironschool.com/equation\_images/k?scale=0.875)   : Number of parameters * ![n](https://learning.flatironschool.com/equation\_images/n?scale=0.875)   : Number of observations * ![upper L With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257BL%257D?scale=0.875)   : Log-likelihood | BIC applies a stronger penalty for complexity. Tends to favor simpler models. Suitable for large datasets. |
| Adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=0.875) | A modification of ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=0.875) that penalizes for additional predictors to prevent overfitting. | To compare models based on variance explained, while accounting for model complexity. | ![Adjusted upper R squared equals 1 minus StartFraction left parenthesis 1 minus upper R squared right parenthesis left parenthesis n minus 1 right parenthesis Over n minus k minus 1 EndFraction](https://learning.flatironschool.com/equation\_images/%255Ctext%257BAdjusted%2520%257D%2520R%255E2%2520%253D%25201%2520-%2520%255Cfrac%257B(1%2520-%2520R%255E2)(n%2520-%25201)%257D%257Bn%2520-%2520k%2520-%25201%257D?scale=0.875)  Where:   * ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=0.875)   : Proportion of variance explained * ![n](https://learning.flatironschool.com/equation\_images/n?scale=0.875)   : Number of observations * ![k](https://learning.flatironschool.com/equation\_images/k?scale=0.875)   : Number of predictors | Adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=0.875)  is intuitive but does not incorporate likelihood directly. Best for simpler comparisons. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248889

Scraped At: 2026-05-15T10:36:50.831089
