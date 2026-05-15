# What is Multiple Linear Regression and How Does it Work?

# What is Multiple Linear Regression and How Does it Work?

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) What is Multiple Linear Regression and How Does it Work?

Icon Progress Bar (browser only)

4 min read

Multiple Linear Regression (MLR) is a **statistical technique that models the relationship between a single dependent variable (*y*) and two or more independent (predictor) variables** (
![x 1 comma x 2 comma ellipsis comma x Subscript p Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520x\_2%252C%2520%255Cdots%252C%2520x\_p?scale=1)
). It extends simple linear regression, which uses only one predictor, to allow for multiple factors to explain or predict an outcome.

### Key Terms and Concepts

#### Dependent Variable (*y*)

The outcome variable you are trying to predict or explain (e.g., sales revenue, house price, patient recovery time).

#### Independent Variables ( ![x 1 comma x 2 comma ellipsis comma x Subscript p Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520x\_2%252C%2520%255Cdots%252C%2520x\_p?scale=1.125) )

The predictors or features that influence the dependent variable (e.g., advertising spend, square footage, age of the house).

#### Regression Equation

The general form of the Multiple Linear Regression equation is:

![y With caret equals b 0 plus b 1 x 1 plus b 2 x 2 plus ellipsis plus b Subscript p Baseline x Subscript p](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1%2520x\_1%2520%252B%2520b\_2%2520x\_2%2520%252B%2520%255Cdots%2520%252B%2520b\_p%2520x\_p?scale=1)

Where:

* ![y With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D?scale=1)
  : Predicted value of the dependent variable.
* ![b 0](https://learning.flatironschool.com/equation\_images/b\_0?scale=1)
  : Intercept (the value of
  ![y With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D?scale=1)
  when all predictors are 0).
* ![b 1 comma b 2 comma ellipsis comma b Subscript p Baseline](https://learning.flatironschool.com/equation\_images/b\_1%252C%2520b\_2%252C%2520%255Cdots%252C%2520b\_p?scale=1)
  : Coefficients that measure the effect of each predictor
  ![x 1 comma x 2 comma ellipsis comma x Subscript p Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520x\_2%252C%2520%255Cdots%252C%2520x\_p?scale=1)
  on the dependent variable.
* ![x 1 comma x 2 comma ellipsis comma x Subscript p Baseline](https://learning.flatironschool.com/equation\_images/x\_1%252C%2520x\_2%252C%2520%255Cdots%252C%2520x\_p?scale=1)
  : Independent variables.

#### Coefficients ( ![b 1 comma b 2 comma ellipsis comma b Subscript p Baseline](https://learning.flatironschool.com/equation\_images/b\_1%252C%2520b\_2%252C%2520%255Cdots%252C%2520b\_p?scale=1.125) )

Each coefficient quantifies the effect of a one-unit increase in its corresponding predictor variable on the dependent variable, assuming all other predictors are held constant.

#### Residuals (*e*)

The difference between the observed value (
![y Subscript i](https://learning.flatironschool.com/equation\_images/y\_i?scale=1)
) and the predicted value (
![y With caret Subscript i](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D\_i?scale=1)
):
![e Subscript i Baseline equals y Subscript i Baseline minus ModifyingAbove y With caret Subscript i](https://learning.flatironschool.com/equation\_images/e\_i%2520%253D%2520y\_i%2520-%2520%255Chat%257By%257D\_i?scale=1)

Residuals are **used to assess the goodness of fit** of the model.

#### adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1.125)

adjusted
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
is a modification of the
![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
statistic that accounts for the number of predictors (independent variables) in a regression model. While
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
measures the proportion of variance in the dependent variable (*y*) explained by the predictors, it can be artificially inflated by adding unnecessary predictors, even if they have no true explanatory power.

adjusted
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
addresses this issue by introducing a penalty for the number of predictors in the model. Like
![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
, adjusted
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
is bound between 0 and 1.

##### Details on adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)

![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)

The standard
![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
(coefficient of determination) is given by:

![r squared equals 1 minus StartFraction SS Subscript residual Baseline Over SS Subscript total Baseline EndFraction](https://learning.flatironschool.com/equation\_images/r%255E2%2520%253D%25201%2520-%2520%255Cfrac%257B%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D%257D%257B%255Ctext%257BSS%257D\_%257B%255Ctext%257Btotal%257D%257D%257D?scale=1)

Where:

* ![SS Subscript residual Baseline equals sigma summation left parenthesis y Subscript i Baseline minus ModifyingAbove y With caret Subscript i Baseline right parenthesis squared](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D%2520%253D%2520%255Csum%2520(y\_i%2520-%2520%255Chat%257By%257D\_i)%255E2?scale=1)
  : The sum of squared residuals (errors).
* ![SS Subscript total Baseline equals sigma summation left parenthesis y Subscript i Baseline minus y overbar right parenthesis squared](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Btotal%257D%257D%2520%253D%2520%255Csum%2520(y\_i%2520-%2520%255Cbar%257By%257D)%255E2?scale=1)
  : The total sum of squares (variability in the observed *y*).  
  adjusted $R^2$

The adjusted
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
formula introduces a penalty to the
![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
formula for adding more predictors:

![adjusted upper R squared equals 1 minus left parenthesis StartFraction SS Subscript residual Baseline divided by left parenthesis n minus p minus 1 right parenthesis Over SS Subscript total Baseline divided by left parenthesis n minus 1 right parenthesis EndFraction right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257Badjusted%2520%257D%2520R%255E2%2520%253D%25201%2520-%2520%255Cleft(%2520%255Cfrac%257B%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D%2520%252F%2520(n%2520-%2520p%2520-%25201)%257D%257B%255Ctext%257BSS%257D\_%257B%255Ctext%257Btotal%257D%257D%2520%252F%2520(n%2520-%25201)%257D%2520%255Cright)?scale=1)

Where:

* *n*: Number of observations (sample size).
* *p*: Number of predictors in the model.
* ![SS Subscript residual](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D?scale=1)
  : Sum of squared residuals.
* ![SS Subscript total](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Btotal%257D%257D?scale=1)
  : Total sum of squares.

##### How adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1) Penalizes Additional Predictors

* **Understanding the Penalty:**
  + In the standard
    ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
     calculation, adding more predictors always decreases 
    ![SS Subscript residual](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D?scale=1)
    , thereby increasing 
    ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
    .
  + adjusted
    ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
    , however, divides 
    ![SS Subscript residual](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D?scale=1)
     by 
    ![left parenthesis n minus p minus 1 right parenthesis](https://learning.flatironschool.com/equation\_images/(n%2520-%2520p%2520-%25201)?scale=1)
    , where *p* is the number of predictors.
  + As *p* increases, the denominator 
    ![left parenthesis n minus p minus 1 right parenthesis](https://learning.flatironschool.com/equation\_images/(n%2520-%2520p%2520-%25201)?scale=1)
     decreases, which increases the penalty and lowers adjusted 
    ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
     unless the new predictor meaningfully reduces the residual sum of squares.

* **Why It Matters:**
  + adjusted
    ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
    prevents overfitting by discouraging the inclusion of irrelevant predictors.
  + Where “overfitting” means that the model can only fit the given data well, but not other data of the same type.
  + If a new predictor does not improve the model significantly, adjusted
    ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
    will decrease instead of artificially increasing.

##### Illustration of adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1.25) Behavior

* If a predictor adds substantial explanatory power (reduces
  ![SS Subscript residual](https://learning.flatironschool.com/equation\_images/%255Ctext%257BSS%257D\_%257B%255Ctext%257Bresidual%257D%257D?scale=1)
  significantly), adjusted
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  increases.
* If a predictor is irrelevant (adds noise or has minimal effect), adjusted
  ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
  decreases because of the penalty for adding unnecessary variables.

##### Why adjusted ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1.25) is Critical

1. **Avoid Overfitting:** Adding too many predictors can lead to overfitting, where the model performs well on the training data but poorly on unseen data. adjusted
   ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
   helps mitigate this issue.
2. **Model Comparison:** When comparing models with different numbers of predictors, adjusted
   ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
   provides a fairer metric than
   ![r squared](https://learning.flatironschool.com/equation\_images/r%255E2?scale=1)
   because it accounts for model complexity.
3. **Model Interpretation:** adjusted
   ![upper R squared](https://learning.flatironschool.com/equation\_images/R%255E2?scale=1)
   reflects the true explanatory power of the model by balancing accuracy (fit) with simplicity.

### Why is Multiple Linear Regression Important?

Multiple Linear Regression (MLR) allows you to:

* **Understand relationships:** Analyze how multiple factors affect the outcome variable.
* **Make predictions:** Forecast future outcomes using multiple predictors.
* **Quantify impacts:** Measure the effect of each predictor while controlling for others.
* **Identify key drivers:** Determine which variables are most influential in predicting the outcome.

By incorporating multiple variables, MLR provides a more comprehensive understanding of the data and enables data scientists to build more robust predictive models.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248851

Scraped At: 2026-05-15T10:32:25.251856
