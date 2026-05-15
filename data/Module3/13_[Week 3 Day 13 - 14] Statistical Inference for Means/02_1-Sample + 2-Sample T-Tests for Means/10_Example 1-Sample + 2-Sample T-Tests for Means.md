# Example: 1-Sample + 2-Sample T-Tests for Means

# Example: 1-Sample + 2-Sample T-Tests for Means

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Example: 1-Sample + 2-Sample T-Tests for Means

Icon Progress Bar (browser only)

4 min read

### Scenario: Mobile App Performance Analysis

Background: You've joined the analytics team at ShopQuick, an e-commerce company. The mobile development team has been working on optimizing the app's performance, and you've been asked to analyze if their recent changes have made a meaningful difference.

#### Situation 1: One-Sample T-Test

The product team has set a target load time of 2.5 seconds for the app's home screen. Your first task is to determine if the current version meets this specification.

```
import numpy as np  
from scipy import stats  
  
# Load times collected from 30 test runs (in seconds)  
load_times = np.array([2.8, 2.3, 2.6, 2.4, 2.7, 2.5, 2.6, 2.4, 2.8, 2.3,  
                      2.5, 2.4, 2.6, 2.7, 2.5, 2.4, 2.6, 2.5, 2.7, 2.4,  
                      2.6, 2.5, 2.7, 2.4, 2.6, 2.5, 2.8, 2.4, 2.6, 2.5])  
  
# Perform one-sample t-test against target of 2.5 seconds  
t_stat, p_value = stats.ttest_1samp(load_times, 2.5)  
  
print(f"Average load time: {np.mean(load_times):.2f} seconds")  
print(f"Standard deviation: {np.std(load_times, ddof=1):.2f} seconds")  
print(f"t-statistic: {t_stat:.3f}")  
print(f"p-value: {p_value:.3f}")
```

Interpretation for Stakeholders: "Our analysis shows that the average load time is 2.55 seconds, which is slightly above our target of 2.5 seconds. However, with a p-value of 0.089 and an alpha at .05, we don't have strong enough evidence to conclude that we're significantly missing our target. That said, since we're running slightly above target, I recommend continued monitoring and optimization."

#### Situation 2: Two-Sample Independent T-Test

The team has implemented a new caching system, and you need to compare load times between users with and without the new cache.

```
# Load times with old and new caching system  
old_cache = np.array([2.8, 2.6, 2.7, 2.5, 2.8, 2.6, 2.7, 2.5, 2.8, 2.6])  
new_cache = np.array([2.3, 2.2, 2.4, 2.1, 2.3, 2.2, 2.4, 2.1, 2.3, 2.2])  
  
# Perform independent t-test  
t_stat, p_value = stats.ttest_ind(old_cache, new_cache)  
  
print(f"Old cache average: {np.mean(old_cache):.2f} seconds")  
print(f"New cache average: {np.mean(new_cache):.2f} seconds")  
print(f"Difference: {np.mean(old_cache) - np.mean(new_cache):.2f} seconds")  
print(f"t-statistic: {t_stat:.3f}")  
print(f"p-value: {p_value:.3f}")
```

#### Situation 3: Paired T-Test

To evaluate the effectiveness of a performance optimization, you measure the same set of user actions before and after the update.

```
# Same users' load times before and after optimization  
before_opt = np.array([3.1, 2.9, 3.0, 2.8, 3.2, 2.9, 3.1, 2.8, 3.0, 2.9])  
after_opt = np.array([2.7, 2.5, 2.6, 2.4, 2.8, 2.5, 2.7, 2.4, 2.6, 2.5])  
  
# Perform paired t-test  
t_stat, p_value = stats.ttest_rel(before_opt, after_opt)  
  
print(f"Average improvement: {np.mean(before_opt - after_opt):.2f} seconds")  
print(f"t-statistic: {t_stat:.3f}")  
print(f"p-value: {p_value:.3f}")
```

 Writing Your Analysis Report: "Based on our analysis of the recent performance optimizations:

1. Baseline Performance (One-Sample Test): Our current average load time is 2.55 seconds, slightly above our 2.5-second target. While this difference isn't statistically significant (p = 0.089), it suggests room for improvement.
2. Caching System Impact (Independent T-Test): The new caching system shows promising results, reducing average load times by 0.4 seconds (from 2.67 to 2.25 seconds). This improvement is statistically significant (p < 0.001), suggesting the new system is genuinely more effective.
3. Optimization Results (Paired T-Test): Testing the same user actions before and after optimization showed an average improvement of 0.4 seconds. This consistent improvement across all test cases is statistically significant (p < 0.001), indicating successful optimization.

 Recommendations:

1. Roll out the new caching system to all users
2. Document the optimization techniques that led to the 0.4-second improvement
3. Continue monitoring load times to ensure sustained performance

This scenario shows how different t-tests help us make data-driven decisions about product improvements, each telling us something slightly different about our system's performance."

This example demonstrates how t-tests move beyond pure statistics to become practical tools for business decision-making. Each type of t-test serves a specific purpose, helping us answer different questions about our product's performance and guide development decisions.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248669

Scraped At: 2026-05-15T10:19:15.970622
