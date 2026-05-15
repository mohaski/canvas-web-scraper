# Example: Bias/Variance Tradeoff and Regularization Techniques

# Example: Bias/Variance Tradeoff and Regularization Techniques

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Example: Bias/Variance Tradeoff and Regularization Techniques

Icon Progress Bar (browser only)

4 min read

![](https://moringa.instructure.com/courses/1426/files/631799/download)
As a junior data scientist at a healthcare analytics company, you are part of a team tasked with developing a model to predict patient hospital charges based on several key predictors, including age, BMI (body mass index), smoking status, and the number of medical conditions. The objective is to build a model that balances accuracy and interpretability, ensuring that it avoids both underfitting (high bias) and overfitting (high variance). Striking this balance is critical for producing reliable predictions that generalize well to new data.

To begin, **the dataset is explored** to understand its structure and the relationships between variables. The dataset includes a target variable (charges), which represents total hospital costs, and four predictor variables: age, BMI, smoking status (binary), and the number of medical conditions. Before building the model, the data is split into training and testing sets to ensure that the model can generalize beyond the data it was trained on. A common practice is to allocate 70-80% of the data for training and the remaining 20-30% for testing. This split prevents the model from being evaluated on the same data it was trained on, which would give an overly optimistic assessment of its performance.

With the data prepared, **models of increasing complexity are built to examine the bias-variance tradeoff**. Initially, a simple linear model (degree 1 polynomial) is tested, which assumes a straightforward relationship between predictors and hospital charges. However, this model is too simplistic, leading to high bias; it systematically underestimates the complexity of the data, failing to capture important relationships. To improve accuracy, polynomial regression models with increasing degrees (2, 3, and 4) are tested.

As complexity increases, the model captures more detailed patterns, but at a cost: while training error decreases, the gap between training and testing error widens, indicating that the model is memorizing the training data instead of learning general patterns. The highest-degree model exhibits overfitting (high variance), where it performs exceptionally well on training data but poorly on unseen data. The best-performing model is found at an intermediate level of complexity, where testing error is minimized, striking the right balance between bias and variance.

**To further refine the model and mitigate overfitting, regularization techniques are introduced.** Ridge regression (L2 regularization) and Lasso regression (L1 regularization) are applied to penalize large coefficients, encouraging simpler and more generalizable models. Ridge regression shrinks coefficients but does not eliminate any predictors, maintaining all features while reducing their influence to prevent overfitting. In contrast, Lasso regression performs feature selection by shrinking some coefficients to exactly zero, effectively removing less important variables. This makes Lasso particularly useful when model simplicity and interpretability are priorities.

**The results show that Ridge regression achieves lower test error than Lasso while keeping all predictors, making it a good choice** when predictive performance is the primary goal. Lasso, on the other hand, eliminates the number of medical conditions variable, suggesting that it contributes less to predicting hospital charges in this dataset. While Lasso simplifies the model, it comes at the cost of higher test error, showing that reducing complexity too much can also weaken predictive performance.

In real-world applications, the **choice between Ridge and Lasso depends on the specific objectives of the analysis.** If the goal is to retain all features and maximize predictive power, Ridge regression is preferable. However, if the goal is to create a more interpretable model by identifying the most important predictors, Lasso regression is a better option. Both techniques help address the bias-variance tradeoff by preventing overfitting while maintaining model interpretability.

By understanding the tradeoff between bias and variance and applying regularization techniques, you can build a predictive model that generalizes well to new data. In the context of healthcare analytics, this ensures more reliable cost predictions, enabling hospitals and insurers to make data-driven decisions on resource allocation and patient care management.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248895

Scraped At: 2026-05-15T10:37:21.562224
