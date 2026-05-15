# What is Binary Logistic Regression?

# What is Binary Logistic Regression?

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) What is Binary Logistic Regression?

Icon Progress Bar (browser only)

6 min read

Logistic regression models the probability of a binary outcome. Unlike linear regression, which predicts continuous values, **logistic regression predicts probabilities** that are mapped to class labels using the **sigmoid curve**.

![Sigmoid curve](https://moringa.instructure.com/courses/1426/files/631828/download)

### Logit (Log-Odds) Transformation

**The formula:**

![logit left parenthesis p right parenthesis equals ln left parenthesis StartFraction p Over 1 minus p EndFraction right parenthesis equals beta 0 plus beta 1 x 1 plus beta 2 x 2 plus ellipsis plus beta Subscript n Baseline x Subscript n Baseline](https://learning.flatironschool.com/equation\_images/%255Ctext%257Blogit%257D(p)%2520%253D%2520%255Cln%255Cleft(%255Cfrac%257Bp%257D%257B1-p%257D%255Cright)%2520%253D%2520%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cbeta\_2%2520x\_2%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n?scale=1)

describes the logistic regression model in terms of the logit function.

![Logit Function: Relationship between probability and log-odds.](https://moringa.instructure.com/courses/1426/files/631830/download)

#### Breaking Down the Formula

Here's what it means:

1. **The Logit Function (
   ![logit left parenthesis p right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257Blogit%257D(p)?scale=1)**):
   * The logit function transforms the probability
     ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
     (of the binary outcome being 1) into the log-odds:
     ![ln left parenthesis StartFraction p Over 1 minus p EndFraction right parenthesis](https://learning.flatironschool.com/equation\_images/%255Cln%255Cleft(%255Cfrac%257Bp%257D%257B1-p%257D%255Cright)?scale=1)
   * ![StartFraction p Over 1 minus p EndFraction](https://learning.flatironschool.com/equation\_images/%255Cfrac%257Bp%257D%257B1-p%257D?scale=1)
     is the odds of the event occurring. The logarithm of the odds (log-odds) linearizes the relationship between predictors (
     ![x Subscript i](https://learning.flatironschool.com/equation\_images/x\_i?scale=1)
     ) and the outcome.
2. **The Right-Hand Side** (Linear Predictor):
   * ![beta 0 plus beta 1 x 1 plus beta 2 x 2 plus ellipsis plus beta Subscript n Baseline x Subscript n](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cbeta\_2%2520x\_2%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n?scale=1)
     is the linear combination of predictors:
     + ![beta 0](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0?scale=1)
       : The intercept, representing the baseline log-odds when all predictors are 0.
     + ![beta 1 comma beta 2 comma ellipsis comma beta Subscript n Baseline](https://learning.flatironschool.com/equation\_images/%255Cbeta\_1%252C%2520%255Cbeta\_2%252C%2520%255Cdots%252C%2520%255Cbeta\_n?scale=1)
       : The coefficients associated with predictors
       ![x 1 comma x 2 comma ellipsis comma x Subscript n Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520x\_2%252C%2520%255Cdots%252C%2520x\_n?scale=1)
       , quantifying their effect on the log-odds of the outcome.
3. **Interpretation**:
   * The logit of the probability (
     ![logit left parenthesis p right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257Blogit%257D(p)?scale=1)
     ) is modeled as a linear function of the predictors (
     ![x 1 comma x 2 comma ellipsis comma x Subscript n Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520x\_2%252C%2520%255Cdots%252C%2520x\_n?scale=1)
     ).
   * Each
     ![beta Subscript i](https://learning.flatironschool.com/equation\_images/%255Cbeta\_i?scale=1)
     coefficient represents the change in the log-odds of the outcome for a one-unit increase in
     ![x Subscript i](https://learning.flatironschool.com/equation\_images/x\_i?scale=1)
     , holding other predictors constant.

#### Why Use the Logit Function?

* The logit function ensures that the model's output,
  ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
  , is always a valid probability between 0 and 1.
* By modeling the log-odds, logistic regression extends linear regression to classification problems, linking a linear predictor to probabilities.

##### Example

Suppose:
![logit left parenthesis p right parenthesis equals ln left parenthesis StartFraction p Over 1 minus p EndFraction right parenthesis equals negative 3 plus 2 x 1 minus 0.5 x 2](https://learning.flatironschool.com/equation\_images/%255Ctext%257Blogit%257D(p)%2520%253D%2520%255Cln%255Cleft(%255Cfrac%257Bp%257D%257B1-p%257D%255Cright)%2520%253D%2520-3%2520%252B%25202x\_1%2520-%25200.5x\_2?scale=1)

* For
  ![x 1 equals 1](https://learning.flatironschool.com/equation\_images/x\_1%2520%253D%25201?scale=1)
  and
  ![x 2 equals 0](https://learning.flatironschool.com/equation\_images/x\_2%2520%253D%25200?scale=1)
  :
  ![logit left parenthesis p right parenthesis equals negative 3 plus 2 left parenthesis 1 right parenthesis minus 0.5 left parenthesis 0 right parenthesis equals negative 1](https://learning.flatironschool.com/equation\_images/%255Ctext%257Blogit%257D(p)%2520%253D%2520-3%2520%252B%25202(1)%2520-%25200.5(0)%2520%253D%2520-1?scale=1)
* The odds of the event occurring are:
  ![StartFraction p Over 1 minus p EndFraction equals e Superscript negative 1 Baseline almost equals 0.367](https://learning.flatironschool.com/equation\_images/%255Cfrac%257Bp%257D%257B1-p%257D%2520%253D%2520e%255E%257B-1%257D%2520%255Capprox%25200.367?scale=1)
* Converting to probability:
  ![p equals StartFraction e Superscript negative 1 Baseline Over 1 plus e Superscript negative 1 Baseline EndFraction almost equals 0.27](https://learning.flatironschool.com/equation\_images/p%2520%253D%2520%255Cfrac%257Be%255E%257B-1%257D%257D%257B1%2520%252B%2520e%255E%257B-1%257D%257D%2520%255Capprox%25200.27?scale=1)

This example shows how the logit function links predictors to probabilities, allowing us to predict outcomes based on the values of
![x 1](https://learning.flatironschool.com/equation\_images/x\_1?scale=1)
and
![x 2](https://learning.flatironschool.com/equation\_images/x\_2?scale=1)
.

### Transforming Log-Odds to Probability

**The formula:**

![p equals StartFraction 1 Over 1 plus e Superscript minus left parenthesis beta 0 plus beta 1 x 1 plus ellipsis plus beta Super Subscript n Superscript x Super Subscript n Superscript right parenthesis Baseline EndFraction](https://learning.flatironschool.com/equation\_images/p%2520%253D%2520%255Cfrac%257B1%257D%257B1%2520%252B%2520e%255E%257B-(%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n)%257D%257D?scale=1)

is used to transform log-odds back into a probability.

![Log-Odds to Probability Transformation](https://moringa.instructure.com/courses/1426/files/631847/download)

#### Breaking Down the Formula

Here's what it means:

1. **Log-Odds to Probability Conversion:**
   * The term
     ![beta 0 plus beta 1 x 1 plus ellipsis plus beta Subscript n Baseline x Subscript n](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n?scale=1)
     represents the log-odds of the binary outcome (i.e., the result of the logistic regression equation before applying the sigmoid function).
   * This formula uses the exponential function
     ![e Superscript minus left parenthesis ellipsis right parenthesis](https://learning.flatironschool.com/equation\_images/e%255E%257B-(%255Cdots)%257D?scale=1)
     to transform the log-odds into a probability
     ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
     , ensuring that the output is always between 0 and 1.
2. **Exponential Term (
   ![e Superscript minus left parenthesis beta 0 plus beta 1 x 1 plus ellipsis plus beta Super Subscript n Superscript x Super Subscript n Superscript right parenthesis](https://learning.flatironschool.com/equation\_images/e%255E%257B-(%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n)%257D?scale=1)
   ):**
   * This term controls how strongly the predictors influence the probability.
   * Large positive log-odds (e.g., when
     ![beta 0 plus beta 1 x 1 plus ellipsis plus beta Subscript n Baseline x Subscript n](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n?scale=1)
     is positive) lead to
     ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
     approaching 1.
   * Large negative log-odds (e.g., when
     ![beta 0 plus beta 1 x 1 plus ellipsis plus beta Subscript n Baseline x Subscript n](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n?scale=1)
     is negative) lead to
     ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
     approaching 0.
3. **Sigmoid Transformation:**
   * The formula is the sigmoid function, which maps any real-valued input (log-odds) to a probability between 0 and 1.
   * The sigmoid ensures that:
     + When
       ![beta 0 plus beta 1 x 1 plus ellipsis plus beta Subscript n Baseline x Subscript n Baseline equals 0](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n%2520%253D%25200?scale=1)
       ,
       ![p equals 0.5](https://learning.flatironschool.com/equation\_images/p%2520%253D%25200.5?scale=1)
       (equal odds).
     + Positive values make
       ![p greater than 0.5](https://learning.flatironschool.com/equation\_images/p%2520%253E%25200.5?scale=1)
       .
     + Negative values make
       ![p less than 0.5](https://learning.flatironschool.com/equation\_images/p%2520%253C%25200.5?scale=1)
       .
4. **Probability (
   ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
   ):**
   * The output
     ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
     represents the likelihood that the binary outcome is 1 (e.g., "success").

#### Key Points

* This formula ensures that logistic regression predictions are valid probabilities between 0 and 1.
* By applying the sigmoid function, the linear relationship in the log-odds is converted into a nonlinear relationship for probabilities.
* This transformation is crucial for binary classification tasks, where outcomes must be interpreted as probabilities.

##### Example

Suppose:
![beta 0 equals negative 2](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0%2520%253D%2520-2?scale=1)
,
![beta 1 equals 1.5](https://learning.flatironschool.com/equation\_images/%255Cbeta\_1%2520%253D%25201.5?scale=1)
, and
![x 1 equals 3](https://learning.flatironschool.com/equation\_images/x\_1%2520%253D%25203?scale=1)
. Then:

![beta 0 plus beta 1 x 1 equals negative 2 plus 1.5 left parenthesis 3 right parenthesis equals 2.5](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%253D%2520-2%2520%252B%25201.5(3)%2520%253D%25202.5?scale=1)

**Substitute into the formula:**

![p equals StartFraction 1 Over 1 plus e Superscript negative 2.5 Baseline EndFraction](https://learning.flatironschool.com/equation\_images/p%2520%253D%2520%255Cfrac%257B1%257D%257B1%2520%252B%2520e%255E%257B-2.5%257D%257D?scale=1)

**Simplify:**

![p almost equals StartFraction 1 Over 1 plus 0.082 EndFraction almost equals 0.92](https://learning.flatironschool.com/equation\_images/p%2520%255Capprox%2520%255Cfrac%257B1%257D%257B1%2520%252B%25200.082%257D%2520%255Capprox%25200.92?scale=1)

This means the probability of the event occurring is approximately
![92 percent sign](https://learning.flatironschool.com/equation\_images/92%2525?scale=1)
.

### Binary Logistic Regression

**Binary logistic regression** is a special case of logistic regression where the dependent variable has exactly two possible outcomes (e.g., 0 or 1, success or failure, yes or no). This method is widely used in classification tasks, such as predicting disease presence, customer churn, or fraud detection. It **provides a robust way to model the relationship between predictor variables and the likelihood of a binary outcome.**

The formulas and graphs already provided are tailored for binary logistic regression, so no additional changes are required to the existing formulas or graphs in the context of binary logistic regression. However, here are some points to highlight to reinforce their applicability to binary logistic regression:

1. **Formulas:** Both the logit transformation formula
   ![logit left parenthesis p right parenthesis equals ln left parenthesis StartFraction p Over 1 minus p EndFraction right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257Blogit%257D(p)%2520%253D%2520%255Cln%255Cleft(%255Cfrac%257Bp%257D%257B1-p%257D%255Cright)?scale=1)
   and the probability formula
   ![p equals StartFraction 1 Over 1 plus e Superscript minus left parenthesis beta 0 plus beta 1 x 1 plus midline horizontal ellipsis plus beta Super Subscript n Superscript x Super Subscript n Superscript right parenthesis Baseline EndFraction](https://learning.flatironschool.com/equation\_images/p%2520%253D%2520%255Cfrac%257B1%257D%257B1%2520%252B%2520e%255E%257B-(%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Ccdots%2520%252B%2520%255Cbeta\_n%2520x\_n)%257D%257D?scale=1)
   are specifically for binary outcomes. They work under the assumption that
   ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
   represents the probability of the positive class (e.g., 1 or "success").
2. **Graphs:** The logistic regression graph showing the sigmoid curve is appropriate for binary outcomes. In these cases:
   * The ***y*-axis** represents the probability (
     ![p](https://learning.flatironschool.com/equation\_images/p?scale=1)
     ) of the positive outcome.
   * The ***x*-axis** represents the predictor or the linear combination of predictors (
     ![beta 0 plus beta 1 x 1 plus midline horizontal ellipsis plus beta Subscript n Baseline x Subscript n](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Ccdots%2520%252B%2520%255Cbeta\_n%2520x\_n?scale=1)
     ).
   * The **curve** transitions smoothly from 0 to 1, reflecting probabilities for the binary outcome.
3. **No Changes Needed:** These formulas and the sigmoid curve are inherently binary in nature because they are designed to predict a single probability pp for the occurrence of one of two outcomes (e.g.,
   ![y equals 1](https://learning.flatironschool.com/equation\_images/y%2520%253D%25201?scale=1)
   ).

### How Does Binary Logistic Regression Work?

Logistic regression is a powerful statistical method used for binary classification, where the **goal is to predict the probability of an outcome belonging to one of two categories**. Unlike linear regression, which predicts continuous values, logistic regression predicts probabilities that are constrained between 0 and 1 using the logit transformation and the sigmoid function. Here's how it works:

#### The Logit Function and Probability Transformation

**Logistic regression models the log-odds** (logarithm of the odds ratio) of the binary outcome as a linear combination of predictors:

![logit left parenthesis p right parenthesis equals ln left parenthesis StartFraction p Over 1 minus p EndFraction right parenthesis equals beta 0 plus beta 1 x 1 plus ellipsis plus beta Subscript n Baseline x Subscript n Baseline](https://learning.flatironschool.com/equation\_images/%255Ctext%257Blogit%257D(p)%2520%253D%2520%255Cln%255Cleft(%255Cfrac%257Bp%257D%257B1-p%257D%255Cright)%2520%253D%2520%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n?scale=1)

* ![logit left parenthesis p right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257Blogit%257D(p)?scale=1)
  : Represents the log-odds of the event occurring.
* ![beta 0](https://learning.flatironschool.com/equation\_images/%255Cbeta\_0?scale=1)
  : The intercept, indicating the baseline log-odds when all predictors are zero.
* ![beta 1 comma ellipsis comma beta Subscript n Baseline](https://learning.flatironschool.com/equation\_images/%255Cbeta\_1%252C%2520%255Cdots%252C%2520%255Cbeta\_n?scale=1)
  : Coefficients representing the influence of each predictor (
  ![x 1 comma ellipsis comma x Subscript n Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520%255Cdots%252C%2520x\_n?scale=1)
  ) on the log-odds.

To convert log-odds back to a probability, the **sigmoid function** is applied:

![p equals StartFraction 1 Over 1 plus e Superscript minus left parenthesis beta 0 plus beta 1 x 1 plus ellipsis plus beta Super Subscript n Superscript x Super Subscript n Superscript right parenthesis Baseline EndFraction](https://learning.flatironschool.com/equation\_images/p%2520%253D%2520%255Cfrac%257B1%257D%257B1%2520%252B%2520e%255E%257B-(%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n)%257D%257D?scale=1)

This transformation ensures that the output is always a valid probability between 0 and 1.

**For example:**

* If
  ![z equals beta 0 plus beta 1 x 1 plus ellipsis plus beta Subscript n Baseline x Subscript n Baseline equals 0](https://learning.flatironschool.com/equation\_images/z%2520%253D%2520%255Cbeta\_0%2520%252B%2520%255Cbeta\_1%2520x\_1%2520%252B%2520%255Cdots%2520%252B%2520%255Cbeta\_n%2520x\_n%2520%253D%25200?scale=1)
  , then
  ![p equals 0.5](https://learning.flatironschool.com/equation\_images/p%2520%253D%25200.5?scale=1)
  .
* As
  ![z right arrow Number infinity](https://learning.flatironschool.com/equation\_images/z%2520%255Cto%2520%255Cinfty?scale=1)
  ,
  ![p right arrow 1](https://learning.flatironschool.com/equation\_images/p%2520%255Cto%25201?scale=1)
  .
* As
  ![z right arrow negative Number infinity](https://learning.flatironschool.com/equation\_images/z%2520%255Cto%2520-%255Cinfty?scale=1)
  ,
  ![p right arrow 0](https://learning.flatironschool.com/equation\_images/p%2520%255Cto%25200?scale=1)
  .

#### Significance in Data Science

Logistic regression is a cornerstone of data science due to its simplicity, interpretability, and applicability to a wide range of classification problems. Its significance lies in its ability to:

* **Provide Probabilistic Predictions:** The output probabilities can be used to make informed decisions, such as setting thresholds for classification.
* **Interpret Coefficients:** The coefficients explain how each predictor impacts the odds of the outcome, making the model highly interpretable.
* **Work with Linear Relationships in Log-Odds:** While flexible, it assumes a linear relationship between predictors and the log-odds, making it suitable for problems with clear relationships.

#### Relevance of Logistic Regression Terms

* **Odds and Log-Odds:** Help quantify the likelihood of an event and linearize the relationship between predictors and the target.
* **Sigmoid Function:** Ensures probabilities are valid and interpretable.
* **Coefficients (
  ![beta 1 comma ellipsis comma beta Subscript n Baseline](https://learning.flatironschool.com/equation\_images/%255Cbeta\_1%252C%2520%255Cdots%252C%2520%255Cbeta\_n?scale=1)
  ):** Indicate the relative importance and direction of influence of predictors.

#### Key Takeaways for Binary Logistic Regression

* **Bridges Linear Models and Classification:** Binary logistic regression connects the simplicity of linear models with the flexibility of classification tasks. It predicts probabilities constrained between 0 and 1, making it a natural choice for binary outcomes.
* **Interpretability and Simplicity:** Logistic regression remains a cornerstone of data science due to its interpretable coefficients, which explain how each predictor influences the odds of the outcome.
* **Probabilistic Outputs:** The use of the sigmoid function ensures that predictions are probabilistic, allowing for threshold-based classification and nuanced decision-making.
* **Applicability Across Industries:** Logistic regression is widely used in diverse fields such as:
  + Healthcare: Predicting disease risk and identifying key contributing factors.
  + Finance: Assessing loan default probabilities and fraud detection.
  + Marketing: Forecasting customer churn and optimizing retention strategies.
* **Comparison to Other Models:**
  + Compared to linear regression, logistic regression is tailored for binary targets, ensuring valid probability predictions.
  + Compared to more advanced models (e.g., neural networks), logistic regression is robust, interpretable, and effective with limited data or clear linear relationships.

By understanding the mechanics, assumptions, and practical applications of binary logistic regression, data scientists can develop actionable models to address critical classification problems in real-world scenarios.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248905

Scraped At: 2026-05-15T10:38:48.052984
