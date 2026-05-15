# Defining Non-Parametric Tests

# Defining Non-Parametric Tests

## ![](https://learning.flatironschool.com/courses/8021/files/4346282/preview) What are non-parametric tests?

Icon Progress Bar (browser only)

9 min read

Understanding these methods is crucial for real-world data analysis where data often doesn't meet traditional statistical assumptions.

A non-parametric test is a statistical method that does not require assumptions about the underlying distribution of your data. Think of it like being able to measure the height of buildings without needing to assume they're all shaped like perfect rectangles - it works regardless of the building's shape.

Key Features of Non-Parametric Tests

Distribution-free approaches mean these tests don't assume your data follows any particular shape or pattern. Recall that parameters are how we have been defining these distributions, hence ‘non-parametric’. They typically work with ranks (ordering of values) rather than the actual values themselves.

For example, instead of comparing means like a t-test would, the Mann-Whitney U test compares whether one group tends to have higher values than another, regardless of the exact numeric differences.

Exact Tests

An exact test calculates precise probabilities based on the observed data rather than relying on approximate distributions. Imagine counting actual combinations of possible outcomes instead of using a mathematical approximation. While this seems like a no-brainer and you might ask why we don’t always do this, it quickly becomes very computationally expensive the more data and variables we have.

Fisher's Exact Test is a classic example - it calculates the exact probability of seeing your results under the null hypothesis, particularly useful when sample sizes are small and approximations might be unreliable.

Key Terms in Non-Parametric Statistics

**Ranks:** The position of a value when data is ordered from lowest to highest. Ranks form the basis of many non-parametric methods.

**Median:** The middle value when data is ordered. Non-parametric tests often use medians instead of means as measures of central tendency.

**Ordinal Data:** Data with a natural ordering but where differences between values aren't necessarily equal (like survey responses from "strongly disagree" to "strongly agree").

These methods become particularly valuable when:

* Your data is ordinal (like ratings or rankings)
* You have outliers that would overly influence parametric tests
* Your sample sizes are small
* The data is highly skewed or doesn't follow a normal distribution

Common Types of Non-Parametric Tests

* [Mann-Whitney U Test](#dpPanel0Content)
* [Wilcoxon Signed-Rank Test](#dpPanel1Content)
* [Kruskal-Wallis H Test](#dpPanel2Content)
* [Spearman's Rank Correlation](#dpPanel3Content)

### Mann-Whitney U Test

This test compares two independent groups, like comparing customer satisfaction between two different products. It's the non-parametric alternative to the independent t-test.

### Wilcoxon Signed-Rank Test

Used for paired comparisons, like measuring customer satisfaction before and after a product update. It's the non-parametric equivalent of a paired t-test.

### Kruskal-Wallis H Test

Compares three or more independent groups, similar to one-way ANOVA but without requiring normality or equal variances.

### Spearman's Rank Correlation

Measures the strength and direction of association between two variables without assuming a linear relationship. It works by converting values to ranks before calculating correlation.

#### How does non-parametric tests work?

Understanding the Mechanics Through Code

* [Rank Transformation Test](#dpPanel4Content)
* [Mann-Whitney U (Wilcoxon rank sum) Test](#dpPanel7Content)
* [Fishers Exact Test](#dpPanel10Content)

### Rank Transformation Test

Let's start with how rank-based tests work, since this is fundamental to many non-parametric methods. Rank Transformation is something most non-parametric tests do to convert raw values to ranks, which makes them resistant to outliers and non-normal distributions

### [Code](#dpPanel5)

```
data = [20, 23, 24, 28, 29, 32, 34, 36, 40]  
  
def demonstrate_ranking_process(data):  
    """  
    Shows how non-parametric tests convert raw data to ranks  
    """  
    import numpy as np  
    from scipy import stats  
      
    # Original data  
    print("Original data:", data)  
      
    # Convert to ranks  
    ranks = stats.rankdata(data)  
    print("\nRanked data:", ranks)  
      
    # Handle ties by averaging ranks  
    data_with_ties = np.array([1, 2, 2, 3, 4, 4, 5])  
    ranks_with_ties = stats.rankdata(data_with_ties)  
    print("\nData with ties:", data_with_ties)  
    print("Ranks with ties:", ranks_with_ties)  
      
    return ranks  
  
demonstrate_ranking_process(data)
```

### [Output](#dpPanel6)

```
Original data: [20, 23, 24, 28, 29, 32, 34, 36, 40]  
  
Ranked data: [1. 2. 3. 4. 5. 6. 7. 8. 9.]  
  
Data with ties: [1 2 2 3 4 4 5]  
Ranks with ties: [1.  2.5 2.5 4.  5.5 5.5 7. ]
```

### Mann-Whitney U (Wilcoxon rank sum) Test

Now let's implement a complete Mann-Whitney U (Wilcoxon rank sum) test to understand its inner workings. This is the non-parametric version of the 2-sample independent t test:

### [Code](#dpPanel8)

`# Scenario: Customer satisfaction ratings (1-5 scale) for old and new website  
# Simulating ordinal data where parametric tests wouldn't be appropriate  
import numpy as np  
from scipy import stats  
  
  
np.random.seed(42)  
satisfaction_old = np.random.choice([1, 2, 3, 4, 5], size=30,  
                                   p=[0.1, 0.2, 0.4, 0.2, 0.1])  
satisfaction_new = np.random.choice([1, 2, 3, 4, 5], size=30,  
                                   p=[0.05, 0.15, 0.3, 0.3, 0.2])  
  
def mann_whitney_detailed(group1, group2, alpha=0.05):  
    """  
    Implements Mann-Whitney U test with detailed explanation  
    """  
    # Step 1: Combine and rank all values  
    combined = np.concatenate([group1, group2])  
    ranks = stats.rankdata(combined)  
      
    # Step 2: Split ranks back into groups  
    n1, n2 = len(group1), len(group2)  
    rank_sum1 = np.sum(ranks[:n1])  
      
    # Step 3: Calculate U statistic  
    U1 = rank_sum1 - (n1 * (n1 + 1)) / 2  
    U2 = n1 * n2 - U1  
    U = min(U1, U2)  
      
    # Step 4: Calculate effect size  
    effect_size = 2 * (U - (n1 * n2)/2) / (n1 * n2)  
      
    # Perform the test using scipy for p-value (does the above for us)  
    stat, p_value = stats.mannwhitneyu(group1, group2, alternative='two-sided')  
      
    print("Mann-Whitney U Test Analysis")  
    print("-" * 30)  
    print(f"Group 1 n: {n1}")  
    print(f"Group 2 n: {n2}")  
    print(f"U statistic: {U}")  
    print(f"P-value: {p_value:.4f}")  
    print(f"Effect size: {effect_size:.3f}")  
      
    return {  
        'U': U,  
        'p_value': p_value,  
        'effect_size': effect_size,  
        'significant': p_value < alpha  
    }  
  
mann_whitney_detailed(satisfaction_old, satisfaction_new)`

### [Output](#dpPanel9)

```
Mann-Whitney U Test Analysis  
------------------------------  
Group 1 n: 30  
Group 2 n: 30  
U statistic: 329.0  
P-value: 0.0669  
Effect size: -0.269
```

### Fishers Exact Test

For exact tests, let's implement Fisher's exact test to understand how it calculates exact probabilities. Note that Fisher’s is used in lieu of a Chi-squared test of independence or homogeneity when any expected frequencies are less than 5.

The key steps in Fisher's Exact Test are:

* **Fixed Margins:** The test considers the row and column totals as fixed. In our A/B test example, this means we always have:
  + Total number of visitors in each group stays the same
  + Total number of conversions and non-conversions stays the same
* **Exact Probability:** For each possible arrangement of the data (keeping those margins fixed), the test calculates the exact probability using the hypergeometric distribution. This involves the use of factorials.
* **P-value Calculation:** The p-value is the sum of probabilities for all arrangements that are as extreme as or more extreme than what we observed.

### [Equation](#dpPanel11)

![LaTeX: \Large p = \frac{(a+b)!(c+d)!(a+c)!(b+d)!}{a!b!c!d!n!}](https://learning.flatironschool.com/equation\_images/%255CLarge%2520p%2520%253D%2520%255Cfrac%257B(a%252Bb)!(c%252Bd)!(a%252Bc)!(b%252Bd)!%257D%257Ba!b!c!d!n!%257D?scale=1.25)

These values a, b, c, and d are given by the frequencies of a contingency table, namely:

![LaTeX:
\begin{array}{c|cc}
& \text{Category 1, choice \#1} & \text{Category 1, choice \#2} \\
\hline
\text{Category 2, choice \#1} & a & b \\
\text{Category 2, choice \#2} & c & d \\
\end{array}
](https://learning.flatironschool.com/equation\_images/%250A%255Cbegin%257Barray%257D%257Bc%257Ccc%257D%250A%2520%2526%2520%255Ctext%257BCategory%25201%252C%2520choice%2520%255C%25231%257D%2520%2526%2520%255Ctext%257BCategory%25201%252C%2520choice%2520%255C%25232%257D%2520%255C%255C%250A%255Chline%250A%255Ctext%257BCategory%25202%252C%2520choice%2520%255C%25231%257D%2520%2526%2520a%2520%2526%2520b%2520%255C%255C%250A%255Ctext%257BCategory%25202%252C%2520choice%2520%255C%25232%257D%2520%2526%2520c%2520%2526%2520d%2520%255C%255C%250A%255Cend%257Barray%257D%250A%250A%250A%250A?scale=1.25)

### [Code](#dpPanel12)

```
def demonstrate_fishers_exact(table):  
    """  
    Demonstrates how Fisher's Exact Test calculates probabilities  
    using a clear step-by-step process  
    """  
    import numpy as np  
    from scipy.stats import fisher_exact  
    from math import factorial  
      
    # Step 1: Set up the contingency table  
    table = np.array(table)  
      
    # Step 2: Calculate row and column totals  
    row_sums = np.sum(table, axis=1)  
    col_sums = np.sum(table, axis=0)  
    total = np.sum(table)  
      
    # Step 3: Calculate the hypergeometric probability for one table  
    def calculate_table_probability(t):  
        """  
        Calculates the probability of observing this exact table arrangement  
        """  
        numerator = (factorial(row_sums[0]) * factorial(row_sums[1]) *   
                    factorial(col_sums[0]) * factorial(col_sums[1]))  
        denominator = (factorial(total) * factorial(t[0,0]) *   
                      factorial(t[0,1]) * factorial(t[1,0]) *   
                      factorial(t[1,1]))  
        return numerator / denominator  
      
    probability = calculate_table_probability(table)  
    # Repeat this for all possible tables that are as extreme or more OR  
      
    # Step 4: Calculate Fisher's exact test using scipy  
    odds_ratio, p_value = fisher_exact(table)  
      
    print("Fisher's Exact Test Analysis")  
    print("-" * 30)  
    print("\nContingency Table:")  
    print(table)  
    print("\nRow totals:", row_sums)  
    print("Column totals:", col_sums)  
    print("Total:", total)  
    print(f"\nProbability of this exact arrangement: {probability:.6f}")  
    print(f"Fisher's Exact Test p-value: {p_value:.6f}")  
      
    return odds_ratio, p_value  
  
# Example usage with a small dataset  
example_table = np.array([[5, 0],  
                         [1, 4]])  
  
demonstrate_fishers_exact(example_table)
```

### [Output](#dpPanel13)

```
Fisher's Exact Test Analysis  
------------------------------  
  
Contingency Table:  
[[5 0]  
 [1 4]]  
  
Row totals: [5 5]  
Column totals: [6 4]  
Total: 10  
  
Probability of this exact arrangement: 0.023810  
Fisher's Exact Test p-value: 0.047619
```

### Single Table Probability

This is the probability of seeing exactly the arrangement we observed

* It's calculated using the hypergeometric distribution
* It represents just one possible way the data could have arranged itself

### P-value

This is the sum of probabilities for all arrangements that are as extreme as or more extreme than what we observed

It includes our observed arrangement plus other arrangements that show similar or stronger evidence against the null hypothesis

This gives us the full picture of how unusual our results are under the null hypothesis

Think of it like this: If you're wondering how unusual it is to roll a total of 12 with two dice, you wouldn't just look at the probability of rolling 6+6. You'd also consider 5+7 and 4+8 because they're equally extreme outcomes. The single probability is like looking at just 6+6, while the p-value is like considering all ways to roll 12 or higher.

### Conceptualize Non-parametric Tests

Conceptualizing Non-parametric Tests

| Term | Definition | Example |
| --- | --- | --- |
| Mann-Whitney U Test | Compares two independent groups using ranks; alternative to t-test | Comparing customer ratings (1-5 scale) between two product versions |
| Wilcoxon Signed-Rank Test | Analyzes paired data by ranking differences; alternative to paired t-test | Measuring employee performance before/after training |
| Kruskal-Wallis Test | Compares three or more independent groups using ranks; alternative to ANOVA | Comparing satisfaction scores across multiple store locations |
| Spearman's Rank Correlation | Measures relationship strength between variables using ranks; alternative to Pearson correlation | Analyzing relationship between study time and test scores |
| Fisher's Exact Test | Calculates exact probabilities for categorical data; preferred for small samples | Testing if treatment response differs between small patient groups |
| Rank-Based Methods | Convert raw values to ranks before analysis | Converting raw scores to 1st, 2nd, 3rd, etc. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248751

Scraped At: 2026-05-15T10:23:49.726010
