# Technical Lesson: Statistical Inference for Proportions

# Technical Lesson: Statistical Inference for Proportions

## ![Blue FS Logo](https://moringa.instructure.com/courses/1426/files/631704/preview) Technical Lesson - Statistical Inference for Proportions

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

Business Scenario: E-commerce Website Optimization

You're a junior data analyst at GreenCart, an online grocery delivery service. The company has been experiencing lower-than-desired conversion rates on their website, where a conversion is defined as a visitor proceeding from product browsing to adding items to their cart.

The marketing team has developed a new website design that they believe will improve conversion rates. They've been running an A/B test:

* Version A: Current website design
* Version B: New website design with simplified navigation and larger product images

 Your manager, Sarah, has asked you **two critical questions:**

1. "What's the current conversion rate for our website, and how confident can we be in that number?"
2. "Is the new design actually performing better, or are the differences we're seeing just random chance?"

 These questions perfectly align with our **two main tools:**

* Confidence intervals will help us estimate the true conversion rate
* Hypothesis testing will help us determine if the new design is significantly better

The Data

The A/B test has been running for two weeks, and you have:

**Version A (Current Design):**

* Total Visitors: 1000
* Conversions: 150 (users who added items to cart)

**Version B (New Design):**

* Total Visitors: 1200
* Conversions: 210 (users who added items to cart)

### Tools and Resources

* Jupyter Notebook
* [Python


  Links to an external site.](https://www.python.org/) (3.7 or higher)
* [Numpy


  Links to an external site.](https://numpy.org/) and [SciPy


  Links to an external site.](https://scipy.org/)

The video below will guide you through each step of the Statistical Inference for Proportions. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Statistical Inference for Proportions.

[VIDEO LINK](https://player.vimeo.com/video/1060682025?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

### Part 1: Estimating Current Performance with Confidence Intervals

Let's first address Sarah's question about the current website's performance. We'll use confidence intervals to estimate the true conversion rate with a measure of certainty.

```
import numpy as np  
from scipy import stats  
  
# Set up our data for the current website (Version A)  
conversions_a = 150    # Number of users who added items to cart  
visitors_a = 1000      # Total visitors to current design  
  
def analyze_conversion_rate(conversions, visitors, confidence_level=0.95):  
    """  
    Analyze conversion rate with confidence interval.  
      
    Parameters:  
        conversions: Number of successful conversions  
        visitors: Total number of visitors  
        confidence_level: Desired confidence level (default 95%)  
    """  
    # Step 1: Calculate sample proportion  
    p_hat = conversions / visitors  
    print(f"Current conversion rate: {p_hat:.1%}")  
  
    # Step 2: Verify we can use normal approximation  
    # We need at least 10 successes and 10 failures  
    successes = visitors * p_hat  
    failures = visitors * (1 - p_hat)  
      
    print("\nChecking requirements:")  
    print(f"Number of conversions: {successes:.1f} (need ≥ 10)")  
    print(f"Number of non-conversions: {failures:.1f} (need ≥ 10)")  
      
    if successes >= 10 and failures >= 10:  
        print("✓ Requirements met for reliable analysis")  
    else:  
        print("⚠ Warning: Need more data for reliable analysis")  
        return  
  
    # Step 3: Calculate standard error  
    # This tells us how much we expect our estimate to vary  
    std_error = np.sqrt((p_hat * (1 - p_hat)) / visitors)  
    print(f"\nStandard Error: {std_error:.4f}")  
  
    # Step 4: Find critical value and margin of error  
    z_critical = stats.norm.ppf((1 + confidence_level) / 2)  
    margin_error = z_critical * std_error  
    print(f"Margin of Error: {margin_error:.1%}")  
  
    # Step 5: Construct confidence interval  
    ci_lower = max(0, p_hat - margin_error)  # Can't go below 0%  
    ci_upper = min(1, p_hat + margin_error)  # Can't go above 100%  
      
    print(f"\n{confidence_level*100}% Confidence Interval:")  
    print(f"({ci_lower:.1%}, {ci_upper:.1%})")  
      
    return {  
        'point_estimate': p_hat,  
        'confidence_interval': (ci_lower, ci_upper),  
        'margin_error': margin_error  
    }  
  
# Analyze current website performance  
current_performance = analyze_conversion_rate(conversions_a, visitors_a)
```

### Part 2: Testing if the New Design is Better

Now let's address Sarah's second question about whether the new design is actually performing better. We'll use hypothesis testing to determine if the observed improvement is statistically significant.

```
def compare_designs(conversions_a, visitors_a, conversions_b, visitors_b, alpha=0.05):  
    """  
    Compare two website designs using hypothesis testing.  
      
    Parameters:  
        conversions_a: Conversions for current design  
        visitors_a: Visitors to current design  
        conversions_b: Conversions for new design  
        visitors_b: Visitors to new design  
        alpha: Significance level (default 5%)  
    """  
    # Step 1: Calculate observed proportions  
    p_a = conversions_a / visitors_a  
    p_b = conversions_b / visitors_b  
      
    print("Observed Conversion Rates:")  
    print(f"Current Design: {p_a:.1%}")  
    print(f"New Design: {p_b:.1%}")  
    print(f"Absolute Difference: {(p_b - p_a):.1%}")  
      
    # Step 2: Calculate pooled proportion (assuming null hypothesis is true)  
    p_pooled = (conversions_a + conversions_b) / (visitors_a + visitors_b)  
      
    # Step 3: Calculate standard error for difference in proportions  
    se_diff = np.sqrt(p_pooled * (1 - p_pooled) * (1/visitors_a + 1/visitors_b))  
      
    # Step 4: Calculate test statistic  
    z_stat = (p_b - p_a) / se_diff  
      
    # Step 5: Calculate p-value (two-sided test)  
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))  
      
    # You could also you the scipy proportion test function  
    print(f"\nTest Statistics:")  
    print(f"Z-statistic: {z_stat:.3f}")  
    print(f"P-value: {p_value:.4f}")  
      
    # Step 6: Make decision  
    print("\nDecision:")  
    if p_value < alpha:  
        print(f"✓ Statistically significant (p < {alpha})")  
        print("The difference between designs is unlikely to be due to chance.")  
    else:  
        print(f"× Not statistically significant (p > {alpha})")  
        print("We don't have enough evidence to conclude the designs are different.")  
      
    return {  
        'difference': p_b - p_a,  
        'p_value': p_value,  
        'z_statistic': z_stat  
    }  
  
# Compare the two designs  
visitors_b = 1200  
conversions_b = 210  
  
comparison_results = compare_designs(conversions_a, visitors_a,   
                                  conversions_b, visitors_b)  
  
# Prepare summary for Sarah  
def prepare_business_summary(current_perf, comparison):  
    """  
    Create a business-friendly summary of our analysis.  
    """  
    print("\nSummary for Sarah:")  
    print("-----------------")  
    print(f"Current Website Performance:")  
    print(f"• Conversion rate is between "  
          f"{current_perf['confidence_interval'][0]:.1%} and "  
          f"{current_perf['confidence_interval'][1]:.1%} "  
          f"(95% confidence)")  
      
    if comparison['p_value'] < 0.05:  
        print("\nNew Design Impact:")  
        print(f"• The new design shows a {abs(comparison['difference']):.1%} "  
              f"{'increase' if comparison['difference'] > 0 else 'decrease'} "  
              f"in conversion rate")  
        print("• This difference is statistically significant")  
    else:  
        print("\nNew Design Impact:")  
        print("• While we observe some differences, we need more data to be "  
              "confident they're not due to chance")  
      
    print("\nRecommendations:")  
    if comparison['p_value'] < 0.05 and comparison['difference'] > 0:  
        print("• Consider implementing the new design")  
        print("• Continue monitoring to ensure performance remains stable")  
    else:  
        print("• Continue testing to gather more data")  
        print("• Consider analyzing specific user segments where the new "  
              "design might be more effective")  
  
prepare_business_summary(current_performance, comparison_results)
```

 This code provides a complete analysis that:

* Estimates the current conversion rate with confidence
* Tests if the new design performs differently
* Presents results in a business-friendly format

Each function includes detailed comments explaining the statistical concepts and decisions being made. We've also included data validation and clear output formatting to make the results easily interpretable.

### Considerations

### Sample Size Requirements

* Always verify the success-failure condition (np̂ ≥ 10 and n(1-p̂) ≥ 10)
* Larger samples provide more precise estimates and more powerful tests
* When working near 0 or 1, larger samples may be needed

### Decision Points

1. Choosing Confidence Level
   * 99% for critical decisions
   * 90% when wider intervals are acceptable

* 95% is standard but consider:

2. One-sided vs Two-sided Tests

* Two-sided for general differences
* One-sided when direction matters
* One-sided tests have more power but can miss opposite effects

3. Significance Level

* Standard α = 0.05
* Consider α = 0.01 for critical decisions
* Balance Type I and Type II errors

### Common Issues

1. Boundary Problems

* Solution: Use Wilson score interval near 0 or 1
* Alternative: Transform data if possible

2. Small Sample Sizes

* Solution: Collect more data
* Alternative: Use exact methods

3. Independence Violations

* Check sampling method
* Consider clustering if needed

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248640

Scraped At: 2026-05-15T10:16:24.315825
