# Example: Parametric Test Assumption

# Example: Parametric Test Assumption

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Example: Parametric Test Assumption

Icon Progress Bar (browser only)

4 min read

Scenario

You're a junior data analyst at an e-commerce company, and your marketing manager asks you to analyze the effectiveness of two different email campaign strategies (A and B) by comparing customer purchase amounts.

### Solution

**Initial Approach:** Your first instinct might be to jump straight into a t-test, but let's work through the proper analysis of assumptions:

### Code

```
import pandas as pd  
import numpy as np  
from scipy import stats  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
# Load the campaign data  
def analyze_campaign_data():  
    # Simulated campaign data  
    campaign_a = np.array([45, 42, 36, 39, 51, 44, 58, 35, 120, 40, 48, 37,   
                          46, 41, 43, 39, 250, 200, 150, 42])  
    campaign_b = np.array([52, 48, 42, 45, 48, 46, 49, 44, 45, 42, 41, 47,   
                          44, 40, 45, 43, 42, 44, 45, 46])  
      
    print("Step 1: Initial Data Exploration")  
    print("-" * 50)  
    print("Campaign A Summary:")  
    print(f"Mean: ${np.mean(campaign_a):.2f}")  
    print(f"Median: ${np.median(campaign_a):.2f}")  
    print(f"Standard Deviation: ${np.std(campaign_a):.2f}\n")  
      
    print("Campaign B Summary:")  
    print(f"Mean: ${np.mean(campaign_b):.2f}")  
    print(f"Median: ${np.median(campaign_b):.2f}")  
    print(f"Standard Deviation: ${np.std(campaign_b):.2f}\n")  
      
    # Check normality  
    print("Step 2: Testing Normality Assumption")  
    print("-" * 50)  
    _, p_value_a = stats.shapiro(campaign_a)  
    _, p_value_b = stats.shapiro(campaign_b)  
      
    print(f"Shapiro-Wilk test p-values:")  
    print(f"Campaign A: {p_value_a:.4f}")  
    print(f"Campaign B: {p_value_b:.4f}\n")  
      
    # Visual check of distributions  
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  
    sns.histplot(campaign_a, ax=ax1, bins=10)  
    ax1.set_title('Campaign A Distribution')  
    sns.histplot(campaign_b, ax=ax2, bins=10)  
    ax2.set_title('Campaign B Distribution')  
    plt.show()  
      
    # Check homogeneity of variance  
    print("Step 3: Testing Homogeneity of Variance")  
    print("-" * 50)  
    _, p_value_levene = stats.levene(campaign_a, campaign_b)  
    print(f"Levene's test p-value: {p_value_levene:.4f}\n")  
      
    # Handle violation of assumptions  
    if p_value_a < 0.05 or p_value_b < 0.05:  
        print("Step 4: Handling Non-normality")  
        print("-" * 50)  
        print("Normality assumption violated. Attempting log transformation...")  
          
        # Log transform the data  
        campaign_a_log = np.log(campaign_a)  
        campaign_b_log = np.log(campaign_b)  
          
        # Check normality of transformed data  
        _, p_value_a_log = stats.shapiro(campaign_a_log)  
        _, p_value_b_log = stats.shapiro(campaign_b_log)  
          
        print("\nShapiro-Wilk test after log transformation:")  
        print(f"Campaign A: {p_value_a_log:.4f}")  
        print(f"Campaign B: {p_value_b_log:.4f}")  
          
        if p_value_a_log < 0.05 or p_value_b_log < 0.05:  
            print("\nTransformation unsuccessful. Recommending non-parametric test.")  
            # Perform Mann-Whitney U test  
            stat, p_value = stats.mannwhitneyu(campaign_a, campaign_b,   
                                             alternative='two-sided')  
            print(f"\nMann-Whitney U test p-value: {p_value:.4f}")  
        else:  
            # Perform t-test on transformed data  
            stat, p_value = stats.ttest_ind(campaign_a_log, campaign_b_log)  
            print(f"\nt-test on transformed data p-value: {p_value:.4f}")  
    else:  
        # Perform regular t-test if assumptions are met  
        stat, p_value = stats.ttest_ind(campaign_a, campaign_b)  
        print("All assumptions met. Performing standard t-test.")  
        print(f"t-test p-value: {p_value:.4f}")  
  
# Run the analysis  
analyze_campaign_data()
```

### Output

![output of data exploration with python](https://moringa.instructure.com/courses/1426/files/631757/download)

### Communicating the Solution

Here's how you might communicate your findings to the marketing manager:  
"I've analyzed the performance of our two email campaigns, taking care to ensure our statistical approach is valid. Here's what I found:

* Our initial exploration showed that Campaign A had more variable results than Campaign B, with some unusually high purchase amounts that might warrant a follow-up analysis and closer look. This also raised a red flag about using standard statistical tests.
* When I tested the assumptions for a regular t-test, I found that:  
  Campaign A's data wasn't normally distributed (p < 0.05), likely due to those few very large purchases
* The variances between the campaigns were significantly different  
  To handle this situation, I first tried transforming the data using a log transformation to see if we could use standard statistical tests. When this didn't fully resolve the issues, I switched to a non-parametric test (Mann-Whitney U) which doesn't require these assumptions.

Based on this analysis, I found no significant difference in mean purchase amount between the two marketing campaigns (p > 0.05), however, there were several considerably large outlier purchase amounts for campaign A that warrant a further analysis into as special customer cases."

**NOTE:** The relatively small sample sizes of simulated data (for demonstration purposes) might not be enough to detect a significant difference at any meaningful level here but are useful in highlighting data that does not meet our necessary assumptions.

### Learning Points from This Example

**Real Data Often Violates Assumptions:** In this case, the presence of a few large purchases (perhaps from business customers) created a right-skewed distribution in Campaign A. This might warrant a closer look at those particular data points despite the ultimate test result not indicating a significant difference.

### Sequential Decision Making

Notice how each step informed the next:

* First, we looked at basic summaries
* Then we tested assumptions
  + When violations were found, we tried transformations
  + When transformations weren't sufficient, we switched to non-parametric methods

**Business Context Matters:** Understanding why the assumptions were violated (large purchases) helps in both the analysis and communication of results.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248744

Scraped At: 2026-05-15T10:23:26.173691
