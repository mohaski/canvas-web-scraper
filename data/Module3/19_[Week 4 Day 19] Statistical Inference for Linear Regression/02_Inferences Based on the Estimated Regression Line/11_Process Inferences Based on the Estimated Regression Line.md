# Process: Inferences Based on the Estimated Regression Line

# Process: Inferences Based on the Estimated Regression Line

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Process: Inferences Based on the Estimated Regression Line

Icon Progress Bar (browser only)

3 min read

### 1. Fit the Regression Model

Begin by fitting a linear regression model to estimate the relationship between the independent variable (*x*) and the dependent variable (*y*). This step establishes the regression line:

![y With caret equals b 0 plus b 1 x](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1x?scale=1)

* **Purpose:** Provides the foundation for making predictions and estimating intervals.
* **Relevance:** Ensures you can calculate both predicted values and residuals accurately.

### 2. Define the Target *x* Value(s)

Identify the specific value(s) of *x* for which you want to compute inferences.

* **Purpose:** Focuses the analysis on a specific point or set of points of interest (e.g., horsepower of 150 in the mtcars dataset).
* **Relevance:** These target *x* values will determine the predicted *y* values and their intervals.

### 3. Calculate Predicted Values ( ![y With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D?scale=0.875) )

For the given *x* values, calculate the predicted *y* values based on the regression model:

![y With caret equals b 0 plus b 1 x](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1x?scale=1)

* **Purpose:** Establishes the central point around which confidence and prediction intervals will be constructed.
* **Relevance:** Predicted values are necessary for constructing intervals.

### 4. Compute Confidence Interval for the Mean *y* Value

Using the regression model, calculate the confidence interval for the average *y* value at the given *x* value(s).

* **Purpose:** Provides a range that quantifies the uncertainty in the estimated mean *y* for a specific *x*.
* **Relevance:** Useful for group-level predictions and decision-making based on averages.

### 5. Compute Prediction Interval for a Single *y* Value

For the same *x* value(s), calculate the prediction interval for individual *y* observations.

* **Purpose:** Provides a range that accounts for variability in individual outcomes:  
    
  ![y With caret plus or minus t Superscript asterisk Baseline dot StartRoot Var left parenthesis ModifyingAbove y With caret right parenthesis plus sigma squared EndRoot](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%255Cpm%2520t%255E\*%2520%255Ccdot%2520%255Csqrt%257B%255Ctext%257BVar%257D(%255Chat%257By%257D)%2520%252B%2520%255Csigma%255E2%257D?scale=1)
    
    
  Where
  ![Var left parenthesis ModifyingAbove y With caret right parenthesis](https://learning.flatironschool.com/equation\_images/%255Ctext%257BVar%257D(%255Chat%257By%257D)?scale=1)
   is the variance of the predicted mean and 
  ![sigma squared](https://learning.flatironschool.com/equation\_images/%255Csigma%255E2?scale=1)
   accounts for residual variance.

* **Relevance:** Essential for scenarios requiring individual-level predictions.

### 6. Validate Assumptions

Check the assumptions of linear regression, linearity, normality, equal variance, and independence, using residual plots and other diagnostics.

* **Purpose:** Ensures the validity of the model and the computed intervals.
* **Relevance:** Prevents misinterpretation and ensures the intervals are reliable.

### 7. Interpret and Communicate Results

Summarize the results for stakeholders, clearly distinguishing between confidence intervals (for means) and prediction intervals (for individuals).

* **Purpose:** Translate statistical findings into actionable insights.
* **Relevance:** Builds trust in the model by communicating both predictions and their associated uncertainty.

### Conceptualize Inferences Based on the Estimated Regression Line

Conceptualization Table for Inferences Based on the Estimated Regression Line

| Inference | Definition | Formula | Python Code |
| --- | --- | --- | --- |
| Confidence Interval for Mean *y* Value | Provides a range for the average predicted *y* value at a specific *x* value. | ![ModifyingAbove y With caret plus or minus t Superscript asterisk Baseline dot StartRoot Var left parenthesis ModifyingAbove y With caret right parenthesis EndRoot](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%255Cpm%2520t%255E\*%2520%255Ccdot%2520%255Csqrt%257B%255Ctext%257BVar%257D(%255Chat%257By%257D)%257D?scale=0.875) where  ![Var left parenthesis ModifyingAbove y With caret right parenthesis equals StartFraction sigma squared Over n EndFraction plus StartFraction left parenthesis x minus x overbar right parenthesis squared Over sigma summation left parenthesis x Subscript i Baseline minus x overbar right parenthesis squared EndFraction](https://learning.flatironschool.com/equation\_images/%255Ctext%257BVar%257D(%255Chat%257By%257D)%2520%253D%2520%255Cfrac%257B%255Csigma%255E2%257D%257Bn%257D%2520%252B%2520%255Cfrac%257B(x%2520-%2520%255Cbar%257Bx%257D)%255E2%257D%257B%255Csum%2520(x\_i%2520-%2520%255Cbar%257Bx%257D)%255E2%257D?scale=0.875) | ``` # Calculate confidence interval predicted_mean = model.get_prediction(target_x).summary_frame(alpha=0.05) print(predicted_mean[['mean_ci_lower', 'mean_ci_upper']]) ``` |
| Prediction Interval for Single *y* Value | Provides a range for the predicted *y* value for an individual observation at a specific *x* value. | ![y With caret plus or minus t Superscript asterisk Baseline dot StartRoot Var left parenthesis ModifyingAbove y With caret right parenthesis plus sigma squared EndRoot](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%255Cpm%2520t%255E\*%2520%255Ccdot%2520%255Csqrt%257B%255Ctext%257BVar%257D(%255Chat%257By%257D)%2520%252B%2520%255Csigma%255E2%257D?scale=0.875)  Where ![sigma squared](https://learning.flatironschool.com/equation\_images/%255Csigma%255E2?scale=0.875) is the residual variance. | ``` # Calculate prediction interval<br>predicted_individual = model.get_prediction(target_x).summary_frame(alpha=0.05)  print(predicted_individual[['obs_ci_lower','obs_ci_upper']]) ``` |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248842

Scraped At: 2026-05-15T10:31:10.352167
