# Introduction to Finding Patterns in Bivariate Data

# Introduction to Finding Patterns in Bivariate Data

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Introduction to Finding Patterns in Bivariate Data

Icon Progress Bar (browser only)

6 min read

In organizations, data scientists often encounter situations where they must analyze relationships between two numeric variables. This is known as bivariate data analysis. For instance, understanding how the amount of advertising spending affects sales, or how a patient's age influences recovery time, requires uncovering patterns in data.

### Why Theory Matters

To detect and describe these patterns, we rely on linear regression models, which provide a theoretical framework to quantify and visualize the relationship between two numeric variables. The goal is to identify whether changes in one variable systematically correspond to changes in another. This relationship is often expressed  mathematically through a straight line, defined by the equation:

![y With caret equals b 0 plus b 1 x](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1x?scale=1)

Where

* ![y With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D?scale=1)
  is the **predicted value of the dependent variable** (response).
* ![b 0](https://learning.flatironschool.com/equation\_images/b\_0?scale=1)
  ​is the **intercept** (value of *y* when
  ![x equals 0](https://learning.flatironschool.com/equation\_images/x%253D0?scale=1)
  ).
* ![b 1](https://learning.flatironschool.com/equation\_images/b\_1?scale=1)
  is the **slope**, representing the rate of change in *y* for a unit change in *x*.
* *x* is the **independent variable** (predictor).

### Practical Context: Why Bivariate Analysis is Essential

**Consider this scenario:** A junior data scientist at an e-commerce company is tasked with analyzing the impact of marketing campaigns. They have data on ad spending (independent variable) and sales (dependent variable). The company wants to understand if increasing ad spending will lead to higher sales, and by how much.

Using linear regression, they can:

* **Model the Relationship:** Establish whether ad spending predicts sales.
* **Quantify the Effect:** Measure the exact impact of spending increases.
* **Inform Decisions:** Provide data-driven recommendations on budget allocation.

### Scatterplot Visualization

A scatterplot is a key tool for visualizing bivariate data and assessing whether a linear relationship exists.

Here’s how to create a scatterplot for **ad spending vs. sales**:

```
import matplotlib.pyplot as plt  
  
# Example data  
ad_spending = [21, 24, 31, 44, 57]  # Ad spending in $1000s  
sales = [136, 153, 180, 221, 300]   # Sales in $1000s  
  
# Create scatterplot  
plt.scatter(ad_spending, sales, color='blue', label='Data Points')  
plt.title('Scatterplot: Ad Spending vs Sales')  
plt.xlabel('Ad Spending ($1000s)')  
plt.ylabel('Sales ($1000s)')  
plt.legend()  
plt.grid(True)  
plt.show()
```

![Scatterplot of ad spending vs sales.](https://moringa.instructure.com/courses/1426/files/631835/download)

We can see that if we were to draw a line of the graph to “best fit” the data points on the scatter plot, then it would be increasing from left to right, i.e. as we called it in algebra, it would have a positive slope. In which case, the graph would look like this with the updated code.

```
import matplotlib.pyplot as plt  
import numpy as np  
  
# Example data  
ad_spending = [21, 24, 31, 44, 57]  # Ad spending in $1000s  
sales = [136, 153, 180, 221, 300]   # Sales in $1000s  
  
# Calculate the linear regression line  
m, b = np.polyfit(ad_spending, sales, 1)  # Fit linear regression (y = mx + b)  
  
# Create scatterplot  
plt.scatter(ad_spending, sales, color='blue', label='Data Points')  
  
# Plot the linear regression line  
x_vals = np.linspace(min(ad_spending), max(ad_spending), 100)  
y_vals = m * x_vals + b  
plt.plot(x_vals, y_vals, color='red', linestyle='--', label=f'Regression Line: y = {m:.2f}x + {b:.2f}')  
  
# Add title, labels, and legend  
plt.title('Scatterplot: Ad Spending vs Sales')  
plt.xlabel('Ad Spending ($1000s)')  
plt.ylabel('Sales ($1000s)')  
plt.legend()  
plt.grid(True)  
  
# Show the plot  
plt.show()
```

![Scatterplot of ad spending vs sales with regression line.](https://moringa.instructure.com/courses/1426/files/631858/download)

While we are holding off on computing the regression line until the next topic, we can describe it.

#### Description of the Regression Line:

1. **Equation of the Line:**  
   * The regression line is represented by the equation y=4.33x+44.67y = 4.33x + 44.67y=4.33x+44.67, where:  
     + 4.334.334.33 is the slope of the line.
     + 44.6744.6744.67 is the y-intercept.
2. **Interpretation of the Slope:**  
   * For every additional $1000 spent on advertising, sales increase by approximately $4330. This indicates a strong positive relationship between ad spending and sales.  
     + We focus on the intercept since it is the most meaningful and robust descriptive statistic from the regression line equation.
3. **Interpretation of the Intercept:**  
   * When ad spending is $0 (hypothetically), the model predicts that sales would be $44,670. While this may not be realistic, it provides a baseline for the linear relationship.  
     + Since, as in this case, the y-intercept is often not interpretable, we don’t focus on it, but we do need it for the graph of the linear regression line.
4. **Fit of the Line:**  
   * The regression line passes through the overall trend of the data points, illustrating a clear linear relationship between ad spending and sales. The alignment suggests the data fits well with the linear model.

### More Scatterplot Visualizations

Let’s consider some other possibilities for our scatter plots by using this code.

```
import matplotlib.pyplot as plt  
import numpy as np  
  
# Create a 2x3 grid of subplots  
fig, axes = plt.subplots(2, 3, figsize=(18, 12))  
  
# Data for different relationships  
np.random.seed(0)  
n_samples = 50  
  
# Strong positive linear relationship  
x1 = np.random.rand(n_samples)  
y1 = 2 * x1 + np.random.normal(0, 0.2, n_samples)  
axes[0, 0].scatter(x1, y1)  
axes[0, 0].set_title('Strong Positive Relationship')  
  
# Weak positive linear relationship  
x2 = np.random.rand(n_samples)  
y2 = 0.5 * x2 + np.random.normal(0, 1, n_samples)  
axes[0, 1].scatter(x2, y2)  
axes[0, 1].set_title('Weak Positive Relationship')  
  
# Weak negative linear relationship  
x3 = np.random.rand(n_samples)  
y3 = -0.5 * x3 + np.random.normal(0, 1, n_samples)  
axes[0, 2].scatter(x3, y3)  
axes[0, 2].set_title('Weak Negative Relationship')  
  
# Strong negative linear relationship  
x4 = np.random.rand(n_samples)  
y4 = -2 * x4 + np.random.normal(0, 0.2, n_samples)  
axes[1, 0].scatter(x4, y4)  
axes[1, 0].set_title('Strong Negative Relationship')  
  
# No relationship (truly random)  
x5 = np.random.rand(n_samples)  
y5 = np.random.rand(n_samples)  
axes[1, 1].scatter(x5, y5)  
axes[1, 1].set_title('No Relationship')  
  
# Nonlinear relationship  
x6 = np.linspace(0, 10, n_samples)  
y6 = np.sin(x6) + np.random.normal(0, 0.3, n_samples)  
axes[1, 2].scatter(x6, y6)  
axes[1, 2].set_title('Nonlinear Relationship')  
  
# Adjust layout and display the plot  
plt.tight_layout()  
plt.show()
```

 
![Scatterplots showing relationships: Strong Positive, Weak Positive, Weak Negative, Strong Negative, None, and Nonlinear.](https://moringa.instructure.com/courses/1426/files/631818/download)

Beginning with the next topic, we’ll be able to assign a descriptive statistic to the relationship between the two variables, but for now, in general, we have:

* Positive linear relationship
* Negative linear relationship
* No linear relationship

As well as a nonlinear relationship, where this means that there is an algebraic graph that can describe the relationship, but it is not a line. While we’ll learn about nonlinear relationships later in this module, we’ll remain focused on linear relationships for now.

#### Key Concepts

##### Response or Predicted Variable

---

The outcome we aim to predict or explain. In our example, this is sales.

##### Explanatory or Predictor Variable

---

The input or predictor that influences the dependent variable. Here, it’s ad spending.

##### Pattern Detection

---

Linear regression helps determine whether a relationship is positive, negative, or non-existent. A scatterplot is used to visualize this relationship and observe trends.

**Many terms for two variables**

There are a number of different terms for the response and explanatory variables, and we’ll follow the common practice of using them interchangeably, but sometimes where the choice of one is based on the application or point of emphasis.

Here is a summary of the terms:

Summary of terms

| *x*-variable | *y*-variable |
| --- | --- |
| Predictor Variable | Predicted Variable |
| Explanatory Variable | Response Variable |
| Input Variable | Outcome Variable |
| Feature | Target Variable |
| Covariate | Explained Variable |

#### Real-World Example

A company like Netflix might analyze the relationship between the number of new subscribers (dependent variable) and the amount spent on promotional campaigns (independent variable). By leveraging linear regression, Netflix can determine the return on investment for its marketing efforts, guiding future budget decisions.

By understanding the theoretical basis of linear regression, you’ll be equipped to interpret and uncover meaningful patterns in bivariate data, setting the stage for practical application and visualization in the next topic.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248783

Scraped At: 2026-05-15T10:25:57.300246
