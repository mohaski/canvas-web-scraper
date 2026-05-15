# Examples: Parametric Tests

# Examples: Parametric Tests

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Example of Parametric Testing

Icon Progress Bar (browser only)

6 min read

Scenario: E-commerce Website Redesign Analysis

Imagine you're a junior analyst at an e-commerce company. The UX team has implemented a new website design and needs to understand its impact on user behavior. You have data from three sources: user satisfaction ratings, time spent on site, and purchase completion rates.

**Understanding the Business Context**

In this scenario, we're trying to answer a crucial business question: "Did our website redesign actually help our users?" Just like a doctor wouldn't rely on a single vital sign, we're looking at three different metrics that tell us different parts of the story:

### User Satisfaction Ratings

These are like asking patients how they feel on a scale of 1-5. It's direct feedback from users, but it's ordinal data - meaning the difference between a 4 and a 5 might not be the same as between a 3 and a 4.

This is why we will use the Mann-Whitney U test instead of a t-test.

Think of it as comparing whether users tend to give higher ratings in one version versus the other, rather than comparing average ratings.

### Time on Site

This is like measuring how long patients spend in the waiting room. It's continuous data (measured in seconds), but it tends to be right-skewed (non-normal) - some users spend much longer than others, pulling the average up.

Just like medical waiting times, you rarely see negative times, and you often get a few very long times that skew the distribution.

Again, the Mann-Whitney U test helps us here because it's not affected by these extreme values like a t-test would be.

### Purchase Completion Rates

This is like tracking whether patients completed their treatment or not - a simple yes/no outcome.

Because we're dealing with counts in categories (completed vs. abandoned) and potentially small numbers,

Fisher's exact test is perfect here instead of a Chi-squared test. It's like calculating the exact probability of seeing this pattern of completions if the new design had no effect.

### Code Solution and Output

### Code Solution

```
import numpy as np  
import pandas as pd  
from scipy import stats  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
def analyze_website_redesign():  
    """  
    Comprehensive analysis of website redesign impact using non-parametric tests  
    """  
    # Generate realistic example data  
    np.random.seed(42)  
      
    # 1. User Satisfaction Ratings (1-5 scale, ordinal data)  
    old_ratings = np.random.choice([1, 2, 3, 4, 5], size=50,   
                                 p=[0.1, 0.2, 0.4, 0.2, 0.1])  
    new_ratings = np.random.choice([1, 2, 3, 4, 5], size=50,   
                                 p=[0.05, 0.15, 0.3, 0.3, 0.2])  
      
    # 2. Time on Site (right-skewed continuous data)  
    old_time = np.random.lognormal(3, 0.5, 50)  
    new_time = np.random.lognormal(2.8, 0.5, 50)  
      
    # 3. Purchase Completion (binary data)  
    old_purchases = np.array([[30, 70],  # Completed, Abandoned  
                             [40, 60]])  # Before, After  
      
    print("Website Redesign Analysis")  
    print("=" * 50)  
      
    # Analysis 1: User Satisfaction (Mann-Whitney U Test)  
    print("\n1. User Satisfaction Analysis")  
    print("-" * 30)  
    statistic, p_value = stats.mannwhitneyu(old_ratings, new_ratings,   
                                          alternative='two-sided')  
      
    print(f"Old design median rating: {np.median(old_ratings)}")  
    print(f"New design median rating: {np.median(new_ratings)}")  
    print(f"Mann-Whitney U test p-value: {p_value:.4f}")  
      
    # Visualization for satisfaction  
    plt.figure(figsize=(10, 5))  
    plt.subplot(1, 2, 1)  
    sns.boxplot(data=[old_ratings, new_ratings])  
    plt.xticks([0, 1], ['Old Design', 'New Design'])  
    plt.title('User Satisfaction Ratings')  
      
    # Analysis 2: Time on Site (Log-transform and compare)  
    print("\n2. Time on Site Analysis")  
    print("-" * 30)  
      
    # First, check if we should use non-parametric test  
    _, norm_p_old = stats.normaltest(old_time)  
    _, norm_p_new = stats.normaltest(new_time)  
      
    print(f"Normality test p-values: Old={norm_p_old:.4f}, New={norm_p_new:.4f}")  
    print("Using non-parametric test due to non-normal distribution")  
      
    statistic, p_value = stats.mannwhitneyu(old_time, new_time,   
                                          alternative='two-sided')  
      
    print(f"Old design median time: {np.median(old_time):.1f} seconds")  
    print(f"New design median time: {np.median(new_time):.1f} seconds")  
    print(f"Mann-Whitney U test p-value: {p_value:.4f}")  
      
    # Visualization for time  
    plt.subplot(1, 2, 2)  
    sns.boxplot(data=[old_time, new_time])  
    plt.xticks([0, 1], ['Old Design', 'New Design'])  
    plt.title('Time on Site (seconds)')  
    plt.tight_layout()  
    plt.show()  
      
    # Analysis 3: Purchase Completion (Fisher's Exact Test)  
    print("\n3. Purchase Completion Analysis")  
    print("-" * 30)  
      
    odds_ratio, p_value = stats.fisher_exact(old_purchases)  
      
    print("Purchase Completion Rates:")  
    print(f"Old design: {old_purchases[0,0]/(old_purchases[0,0]+old_purchases[0,1])*100:.1f}%")  
    print(f"New design: {old_purchases[1,0]/(old_purchases[1,0]+old_purchases[1,1])*100:.1f}%")  
    print(f"Fisher's exact test p-value: {p_value:.4f}")  
      
    # Prepare summary report  
    results = {  
        'satisfaction': {  
            'test': 'Mann-Whitney U',  
            'p_value': p_value,  
            'interpretation': 'Significant improvement' if p_value < 0.05 else 'No significant change'  
        },  
        'time_on_site': {  
            'test': 'Mann-Whitney U',  
            'p_value': p_value,  
            'interpretation': 'Significant reduction' if p_value < 0.05 else 'No significant change'  
        },  
        'purchase_completion': {  
            'test': "Fisher's Exact",  
            'p_value': p_value,  
            'interpretation': 'Significant improvement' if p_value < 0.05 else 'No significant change'  
        }  
    }  
      
    return results  
  
# Run the analysis  
results = analyze_website_redesign()  
  
# Create a business-friendly summary  
print("\nExecutive Summary")  
print("=" * 50)  
print("\nBased on our analysis of the website redesign:")  
  
for metric, result in results.items():  
    print(f"\n{metric.replace('_', ' ').title()}:")  
    print(f"- Test used: {result['test']}")  
    print(f"- Finding: {result['interpretation']}")  
    print(f"- Statistical significance: {'Yes' if result['p_value'] < 0.05 else 'No'}")
```

### Output

```
Website Redesign Analysis  
==================================================  
  
1. User Satisfaction Analysis  
------------------------------  
Old design median rating: 3.0  
New design median rating: 3.5  
Mann-Whitney U test p-value: 0.0168  
  
2. Time on Site Analysis  
------------------------------  
Normality test p-values: Old=0.0000, New=0.0023  
Using non-parametric test due to non-normal distribution  
Old design median time: 20.0 seconds  
New design median time: 18.2 seconds  
Mann-Whitney U test p-value: 0.0390  
3. Purchase Completion Analysis  
------------------------------  
Purchase Completion Rates:  
Old design: 30.0%  
New design: 40.0%  
Fisher's exact test p-value: 0.1819  
  
Executive Summary  
==================================================  
  
Based on our analysis of the website redesign:  
  
Satisfaction:  
- Test used: Mann-Whitney U  
- Finding: No significant change  
- Statistical significance: No  
  
Time On Site:  
- Test used: Mann-Whitney U  
- Finding: No significant change  
- Statistical significance: No  
  
Purchase Completion:  
- Test used: Fisher's Exact  
- Finding: No significant change  
- Statistical significance: No
```

![2 boxplot graphs of user satisfaction and time on site](https://moringa.instructure.com/courses/1426/files/631655/download)

### The Analysis Workflow

Think of our analysis like building a case in court, where we need multiple pieces of evidence:

* First, we examined user satisfaction. This test ranked all ratings together and checked if the new design's ratings tend to be higher than the old design's. It's like asking "Do users consistently rate one version higher than the other?" rather than just comparing averages.
* Then, we look at time on site. We first checked if the data is normal - like a doctor checking if vital signs follow expected patterns. When we see it's not normal (which is common with time data), we again use Mann-Whitney U test to compare the times without being misled by extreme values.
* Finally, we examined purchase completion. Fisher's exact test calculates the precise probability of seeing this pattern of completions by chance. It's particularly valuable because purchase completions might be relatively rare events, and we need to be very precise in our analysis.

#### Bringing It All Together

The power of this approach comes from how these tests complement each other:

* Satisfaction ratings tell us about user perception
* Time on site indicates user engagement
* Purchase completion shows actual behavior change

By using non-parametric tests, we're being appropriately cautious in our analysis. We're not making assumptions about our data being perfectly normal or well-behaved. Instead, we're using methods that work reliably even when data is messy or skewed, as it often is in real business situations.

The visualizations (box plots) help stakeholders see the differences intuitively, while the statistical tests provide rigorous evidence for our conclusions. Together, they tell a complete story about how the redesign affected user experience.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248753

Scraped At: 2026-05-15T10:23:55.741304
