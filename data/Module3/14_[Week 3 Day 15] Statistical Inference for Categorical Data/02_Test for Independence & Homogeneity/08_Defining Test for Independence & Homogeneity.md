# Defining Test for Independence & Homogeneity

# Defining Test for Independence & Homogeneity

## ![](https://learning.flatironschool.com/courses/8021/files/4346282/preview) What is Testing for Independence & Homogeneity?

Icon Progress Bar (browser only)

12 min read

The chi-squared test of independence and homogeneity are two powerful statistical tools that help us understand patterns in categorical data. Think of them as detectives looking for different kinds of relationships in our data, but using similar methods to reach their conclusions.

The chi-squared test of independence investigates whether two categorical variables are related to each other within a single population. Imagine you're curious whether students' choice of major is related to their preferred study time (morning vs. evening). This test would tell you if these choices are connected or if they occur independently of each other.

The chi-squared test of homogeneity, while mathematically similar, answers a different question: do different populations share the same distribution of a categorical variable? For instance, you might wonder if the distribution of study habits (solo, group, or mixed) is the same between first-year and senior students. This test helps us understand if different groups behave similarly or if they show distinct patterns.

### Chi-squared Test of Independence

This test determines whether there is a significant relationship between two categorical variables within a single population. The key question is: "Are these two variables independent of each other?"

### Chi-squared Test of Homogeneity

This test compares the distribution of a categorical variable across different populations or groups. The key question is: "Do different populations have the same distribution of responses?"

### Contingency Table

A two-way table that organizes data about two categorical variables, showing the frequency counts for each combination of categories. For example, if we're studying patient age groups and treatment responses, each cell shows how many patients in each age group had each type of response. Think of it as a grid where the rows and columns represent different categories, and the numbers inside tell us how often each combination occurs.

### Independence

Two categorical variables are independent if knowing the value of one variable doesn't give us any information about the value of the other. For instance, if treatment response is independent of gender, then knowing a patient's gender wouldn't help us predict their treatment response. Independence means the proportions in one variable stay consistent regardless of the category in the other variable.

### Test of Independence

A statistical method that helps us determine whether two categorical variables are truly independent or have a meaningful relationship. This test examines whether the observed frequencies in our contingency table differ significantly from what we'd expect if the variables were independent. We use this when we have a single sample and want to understand if two characteristics are related.

### Homogeneity

Homogeneity means that different populations or groups share the same distribution of a categorical variable. For example, if the distribution of treatment preferences is homogeneous across different age groups, each age group would show similar proportions of patients preferring each treatment option.

### Test of Homogeneity

A statistical procedure that determines whether multiple populations have the same distribution of a single categorical variable. Unlike the independence test, we use this when we have separate samples from different populations and want to compare them. For example, comparing if the distribution of treatment preferences is the same across different geographic regions.

### Expected Frequencies

The frequency counts we would expect to see in each cell of our contingency table if the null hypothesis (independence or homogeneity) were true. We calculate these using the row and column totals of our observed data. These expected values serve as our baseline for comparison.

### Chi-Square Statistic

A numerical value that measures how far our observed frequencies deviate from our expected frequencies. Larger values indicate bigger differences between observed and expected frequencies. This statistic helps us determine whether differences are statistically significant or could have occurred by chance.

### Degrees of Freedom

A number that tells us how many values in our contingency table can vary freely after we've fixed the row and column totals. For a table with r rows and c columns, the degrees of freedom is (r-1)(c-1). This number is crucial for determining the critical value and p-value of our test.

Remember, while these tests use similar calculations, they answer different questions:

* **Independence Test asks:** "Are these two variables related?" (one sample, two variables)
* **Homogeneity Test asks:** "Do these groups show the same pattern?" (multiple samples, one variable)

Understanding these distinctions helps ensure you choose the right test for your specific research question and interpret the results correctly.

### How does Chi-Square Test for Independence and Homogenity work?

### Chi-Square Test for Independence

The chi-square test for independence is an important tool for scientific experimental design, where both the hypothesized independent and dependent variables are categorical rather than numeric.

Returning to our Super Bowl data, let's hypothesize a causal connection between two variables. We hypothesize that winning the coin toss is an independent variable, and winning the game is a dependent variable. In other words, winning the coin toss and winning the game are not independent variables.

The null hypothesis is the opposite of this, that winning the coin toss and winning the game are independent variables and neither is dependent on the other.

One other way to phrase this as a research question is: is winning the game related to winning the coin toss, or are these unrelated (independent) variables?

Let's begin by aggregating the data — conveniently pandas has a crosstab function ([documentation here


Links to an external site.](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)) that will set this up for us automatically:

```
independence_table = pd.crosstab(sb_data["Coin Toss Winner"], sb_data["Game Winner"])  
independence_table
```

Superbowl Winner- Coin Toss

| Game Winner | Away Team | Home Team |
| --- | --- | --- |
| **Coin Toss Winner** |  |  |
| Away Team | 15 | 15 |
| Home Team | 16 | 9 |

We observe that there is a slight imbalance here, where the Home and Away team seem to win equally often when the Away team is the coin toss winner, but the Home team wins the game less often when the Home team is the coin toss winner.  
(This aligns with a superstition/fan theory that winning the coin toss causes a game loss. As of this writing, the coin toss winner had not won the game for the past 7 Super Bowls!)

But, is the difference statistically significant?

Because we have the data set up as a contingency table, we can use the chi2\_contingency function instead of chisquare:

```
chi2, p, dof, ex = stats.chi2_contingency(independence_table)  
  
print("Chi-square statistic:", chi2)  
print("p-value:", p)  
  
Chi-square statistic: 0.5920138888888885  
p-value: 0.44164141533080714
```

The results are a little different, but we have our familiar chi-square statistic and p-value.

(The other two values returned are dof, the degree of freedom and ex, the expected frequencies calculated along the way.) The core idea behind calculating expected frequencies is to determine what we would expect to see if there was no relationship between our variables.

Think of it like this: if two variables are completely independent, then knowing the value of one variable shouldn't give us any information about the other.

Again assuming
![LaTeX: \alpha = 0.01](https://learning.flatironschool.com/equation\_images/%255Calpha%2520%253D%25200.01?scale=1)
, we once again fail to reject the null hypothesis (that the variables are independent) because
![LaTeX: p \nless \alpha](https://learning.flatironschool.com/equation\_images/p%2520%255Cnless%2520%255Calpha?scale=1)
. We did not find statistically significant evidence that winning the coin toss and winning the game are dependent on each other.

### Chi-Square Test for Homogeneity

One other way we can use a chi-square test is a test for homogeneity. It is very subtly different from the previous test of independence in terms of the framing, but the code is very similar.

Whereas the independence test is about the factors (e.g. winning the coin toss vs. winning the game), homogeneity is about the labels (values) themselves. Similar to two-sample t-tests, the goal is comparing the distributions of two population samples, to understand whether their underlying populations follow the same distribution.

Let’s analyze this Super Bowl data using a test of homogeneity to examine the relationship between coin toss outcomes and game winners. This is a perfect application for a homogeneity test since we want to determine if the distribution of game winners (Home/Away) is the same across different coin toss outcomes (Heads/Tails). Note the different framing of this question as opposed to the test of independence above.

```
import numpy as np  
import pandas as pd  
from scipy.stats import chi2_contingency  
import seaborn as sns  
import matplotlib.pyplot as plt  
  
def analyze_superbowl_outcomes(data):  
    """  
    Analyzes the relationship between coin toss outcomes and game winners  
    using a chi-square test of homogeneity.  
    """  
    # Create a contingency table between coin toss and game winners  
    contingency_table = pd.crosstab(data['Coin Toss Outcome'], data['Game Winner'])  
      
    print("Contingency Table of Outcomes:")  
    print("============================")  
    print(contingency_table)  
    print("\n")  
      
    # Perform chi-square test of homogeneity  
    chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)  
      
    # Create visualization  
    plt.figure(figsize=(12, 5))  
      
    # Plot observed frequencies  
    plt.subplot(1, 2, 1)  
    sns.heatmap(contingency_table, annot=True, fmt='d', cmap='YlOrRd',  
                cbar_kws={'label': 'Number of Games'})  
    plt.title('Observed Game Outcomes\nby Coin Toss Result')  
      
    # Plot expected frequencies  
    plt.subplot(1, 2, 2)  
    sns.heatmap(pd.DataFrame(expected,   
                            index=contingency_table.index,  
                            columns=contingency_table.columns),  
                annot=True, fmt='.2f', cmap='YlOrRd',  
                cbar_kws={'label': 'Expected Number of Games'})  
    plt.title('Expected Game Outcomes\nUnder Homogeneity')  
      
    plt.tight_layout()  
      
    # Calculate proportions for each coin toss outcome  
    proportions = contingency_table.div(contingency_table.sum(axis=1), axis=0)  
      
    print("Win Proportions by Coin Toss Outcome:")  
    print("================================")  
    print(proportions.round(3))  
    print("\n")  
      
    print("Chi-Square Test of Homogeneity Results:")  
    print("================================")  
    print(f"Chi-square statistic: {chi2_stat:.3f}")  
    print(f"Degrees of freedom: {dof}")  
    print(f"P-value: {p_value:.3f}")  
      
    # Calculate and display standardized residuals  
    residuals = (contingency_table - expected) / np.sqrt(expected)  
    print("\nStandardized Residuals:")  
    print("(Values > |1.96| indicate significant deviations)")  
    print("================================")  
    print(residuals.round(3))  
  
# Run the analysis  
analyze_superbowl_outcomes(sb_data)
```

#### Output

```
Contingency Table of Outcomes:  
============================  
Game Winner        Away Team  Home Team  
Coin Toss Outcome                        
Heads                     13         13  
Tails                     18         11  
  
  
Win Proportions by Coin Toss Outcome:  
================================  
Game Winner        Away Team  Home Team  
Coin Toss Outcome                        
Heads                  0.500      0.500  
Tails                  0.621      0.379  
  
  
Chi-Square Test of Homogeneity Results:  
================================  
Chi-square statistic: 0.395  
Degrees of freedom: 1  
P-value: 0.530  
  
Standardized Residuals:  
(Values > |1.96| indicate significant deviations)  
================================  
Game Winner        Away Team  Home Team  
Coin Toss Outcome                        
Heads                 -0.432      0.491  
Tails                  0.409     -0.465
```

![2 box plots of coin toss outcomes](https://moringa.instructure.com/courses/1426/files/631572/preview)

What this analysis tells us about Super Bowl outcomes:

* The Contingency Table shows how many times each combination of coin toss outcome and game winner occurred. This gives us our raw data for comparison.
* Expected Frequencies show what we would expect to see if there was no relationship between coin toss outcomes and game winners (the homogeneity assumption).
* The Chi-Square Test helps us determine if any differences we see between coin toss outcomes are statistically significant or could have occurred by chance.
* The Proportions Table shows us the win rates for home and away teams under each coin toss outcome, making it easier to spot patterns.

Some important notes about interpreting these results:

* The standardized residuals help us identify which specific combinations of coin toss and game outcome differ most from what we'd expect under homogeneity.
* Even if we find statistical significance, we should consider the practical significance - is any difference we observe large enough to matter for prediction or decision-making?

This type of analysis could be valuable for:

* Understanding if coin toss outcomes have any relationship with game outcomes
* Identifying potential patterns in Super Bowl results
* Providing insights for sports analysts and commentators

### Conceptualize the Chi Squared Test- Test for Independence & Homogeneity

Understanding these terms and their relationships helps us:

* Choose the appropriate test for our research question
* Correctly interpret test results
* Identify specific patterns driving significant results
* Make informed decisions based on our findings

Conceptualize the Chi Squared Test- Test for Independence & Homogeneity

| Term | Definition | Example |
| --- | --- | --- |
| Test of Independence | A statistical method that examines whether two categorical variables are related to each other within a single population. Tests if knowing the value of one variable provides information about the other. | Testing if a patient's age group (young, middle, elderly) is related to their preferred appointment time (morning, afternoon, evening) at a medical clinic. |
| Test of Homogeneity | A statistical method that compares the distribution of a single categorical variable across different populations or groups. Tests if multiple groups show the same pattern of responses. | Comparing if the distribution of treatment outcomes (success, partial success, failure) is the same across different hospitals in a healthcare network. |
| Contingency Table | A two-dimensional table showing the frequency distribution of observations for two categorical variables. Rows represent one variable's categories, columns represent the other's. | A table showing how many patients from each age group (rows) chose each type of treatment (columns), with the count in each cell. |
| Expected Frequency | The number of observations we would expect in each cell of the contingency table if there were no relationship between the variables (independence) or if all groups had the same distribution (homogeneity). | In a clinic seeing 100 patients daily with two equally staffed shifts, we would expect 50 patients per shift if timing doesn't affect patient preferences. |
| Degrees of Freedom | The number of independent values that are free to vary in the contingency table. Calculated as (rows-1) × (columns-1). Used to determine critical values and p-values. | In a 3×4 table comparing age groups (3 rows) and treatment preferences (4 columns), degrees of freedom = (3-1)×(4-1) = 6 |
| Null Hypothesis (H₀) | The default assumption that there is no relationship between variables (independence) or that all populations have the same distribution (homogeneity). | H₀: Patient satisfaction levels are distributed the same way across all hospital departments. |
| Alternative Hypothesis (H₁) | The claim that there is a relationship between variables (independence) or that populations have different distributions (homogeneity). | H₁: Different hospital departments show different patterns of patient satisfaction levels. |
| Chi-Square Statistic | A numerical measure of how much the observed frequencies differ from expected frequencies. Larger values indicate bigger differences. | If χ² = 25.3 when comparing treatment outcomes across hospitals, this number represents the total accumulated differences between observed and expected frequencies. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248718

Scraped At: 2026-05-15T10:21:50.877904
