# Example: Marketing Campaign Analysis

# Example: Marketing Campaign Analysis

## ![](https://moringa.instructure.com/courses/1426/files/631843/preview) Example: Marketing Campaign Analysis

Icon Progress Bar (browser only)

2 min read

Imagine you’re a junior data scientist at an e-commerce company. Your manager has asked you to analyze the relationship between advertising spend (*x*) and monthly revenue (*y*). The goal is to determine if increasing advertising budgets will likely result in higher revenue and to quantify this relationship.

This task requires understanding and finding patterns in bivariate data to answer the question: "How does advertising spend influence revenue?"

### Define the Variables

* **Independent Variable (*x*):** Advertising spend, in thousands of dollars.
* **Dependent Variable (*y*):** Monthly revenue, in thousands of dollars.
* **Linear Relationship:** We hypothesize that higher advertising spend is associated with higher revenue, following a linear pattern.

#### How to Express the Relationship

The relationship can be expressed with a linear regression model
![y With caret equals b 0 plus b 1 x](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D%2520%253D%2520b\_0%2520%252B%2520b\_1x?scale=1)
, where in particular:

* ![y With caret](https://learning.flatironschool.com/equation\_images/%255Chat%257By%257D?scale=1)
  ​ is the predicted monthly revenue.
* ![b 0](https://learning.flatironschool.com/equation\_images/b\_0?scale=1)
  is the intercept, representing baseline revenue when no advertising budget is allocated (
  ![x equals 0](https://learning.flatironschool.com/equation\_images/x%253D0?scale=1)
  ).
* ![b 1](https://learning.flatironschool.com/equation\_images/b\_1?scale=1)
  ​ is the slope, representing the change in revenue for each additional thousand dollars spent on advertising.

### Theoretical Analysis

In theory, finding the pattern involves:

1. **Scatter Plot:** Visualizing the data to assess whether a linear relationship might exist.
2. **Descriptive statistics:** The regression line and other descriptive statistics of the relationship between the two variables.

### Practical Example

The dataset includes the following monthly data:

Monthly Data

| Advertising Spend (*x*) | Revenue (*y*) |
| --- | --- |
| 10 | 100 |
| 20 | 150 |
| 30 | 200 |
| 40 | 250 |
| 50 | 300 |

**Pattern:** Spend leads to a $50k increase in revenue. This indicates a **positive linear relationship**.

This example illustrates how linear regression theory is applied to solve real-world problems. By understanding the foundational concepts, you’re prepared to move to the practical implementation phase, where Python tools will simplify calculations and enable scalable, repeatable analysis.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248788

Scraped At: 2026-05-15T10:26:09.052994
