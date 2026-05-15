# Example: Confidence Intervals for Proportions

# Example: Confidence Intervals for Proportions

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Examples of Confidence Intervals for Proportions

Icon Progress Bar (browser only)

5 min read

**Scenario**

Digital Marketing Analysis Imagine you've just joined a digital marketing team, and your manager asks: "We launched a new email marketing campaign last month. Of our first 400 emails, 92 recipients clicked through to our website. I need to know what click-through rate we can expect long-term from this campaign to forecast our quarterly goals."

Let's work through this real situation, connecting each concept to practical application:

### Solution Code

```
import numpy as np  
from scipy import stats  
  
# Our campaign data  
clicks = 92        # Successes (click-throughs)  
emails = 400      # Total sample size  
confidence = 0.95  # We want 95% confidence  
  
# First, calculate our sample proportion  
p_hat = clicks / emails  
print(f"Sample proportion (p̂): {p_hat:.3f}")  
# This is 0.230 or 23.0% click-through rate  
  
# Before we proceed, let's verify our success-failure condition  
successes = emails * p_hat            # np̂  
failures = emails * (1 - p_hat)       # n(1-p̂)  
  
print("\nChecking success-failure condition:")  
print(f"Successes (np̂): {successes:.1f}")        # Need ≥ 10  
print(f"Failures (n(1-p̂)): {failures:.1f}")      # Need ≥ 10  
  
# Since both values exceed 10, we can proceed with our analysis  
# Now calculate standard error  
standard_error = np.sqrt((p_hat * (1 - p_hat)) / emails)  
print(f"\nStandard Error: {standard_error:.4f}")  
  
# Find critical value for 95% confidence  
z_critical = stats.norm.ppf((1 + confidence) / 2)  
print(f"Critical value (z*): {z_critical:.4f}")  
  
# Calculate margin of error  
margin_of_error = z_critical * standard_error  
print(f"Margin of Error: {margin_of_error:.4f}")  
  
# Calculate confidence interval  
ci_lower = p_hat - margin_of_error  
ci_upper = p_hat + margin_of_error  
  
print(f"\n95% Confidence Interval:")  
print(f"({ci_lower:.3f}, {ci_upper:.3f})")  
print(f"({ci_lower*100:.1f}%, {ci_upper*100:.1f}%)")
```

### Results

1. **Sample Proportion (Point Estimate):** Our observed click-through rate is 23.0% (92/400). This is our best single estimate, but we know it's not perfect. That's why we need a confidence interval.
2. **Success-Failure Condition:**
   * Successes: 92 (well above 10)
   * Failures: 308 (well above 10) This tells us our sample is large enough to use normal-based methods reliably.
3. **Standard Error:** We calculated a standard error of about 0.021, or 2.1 percentage points. This represents the typical amount our sample proportion might vary from sample to sample just by chance.
4. **Confidence Interval Construction**:
   * For 95% confidence, we use a z\* value of 1.96 (from the standard normal)
   * Our margin of error is about 4.1 percentage points (1.96 × 2.1%)
   * This gives us an interval from 18.9% to 27.1

### Communicating Results

**Writing the Analysis for Your Manager:**

"Based on our analysis of the first 400 emails, we can be 95% confident that the true long-term click-through rate for this campaign will fall between 18.9% and 27.1%.

Here's what this means for planning:

* Best estimate: 23.0% click-through rate
* Conservative estimate (lower bound): 18.9%
* Optimistic estimate (upper bound): 27.1%

For quarterly planning, I recommend:

1. Using 18.9% for conservative forecasts
2. Using 23.0% for typical forecasts
3. Using 27.1% for optimistic scenarios

The margin of error (±4.1 percentage points) gives us reasonable precision for planning. However, if we need more precise estimates, we could:

* Analyze more emails (doubling our sample size would reduce the margin of error by about 30%)
* Accept a lower confidence level (90% confidence would give us a narrower interval but less certainty)

**This example demonstrates how confidence intervals help us:**

* Move from a single point estimate to a range of plausible values
* Quantify the precision of our estimate
* Make data-driven decisions while acknowledging uncertainty
* Communicate results clearly to stakeholders

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248619

Scraped At: 2026-05-15T10:15:26.714962
