# Example: Hypothesis Tests for 1 + 2 Sample Proportions

# Example: Hypothesis Tests for 1 + 2 Sample Proportions

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Examples of Hypothesis Tests for 1 + 2 Sample Proportions

Icon Progress Bar (browser only)

4 min read

Imagine you've just joined the analytics team at a growing software company. Your customer support manager comes to you with a question: "We've been experimenting with offering support through both chat and email. The chat system is more expensive, so we need to know if it's actually performing better in terms of customer satisfaction."

She shares the following data from the past month:

* Chat Support: 280 satisfied customers out of 320 total responses
* Email Support: 410 satisfied customers out of 500 total responses

Let's walk through analyzing this data step by step, using both conceptual understanding and Python code.

### Step 1: Understanding the Business Question

First, let's translate the business question into statistical terms. The support manager wants to know if chat support has a higher satisfaction rate than email support. This is a perfect scenario for a two-proportion hypothesis test.

### Step 2: Setting Up Our Hypotheses

We need to state our null and alternative hypotheses:

Null Hypothesis (H₀): The satisfaction rate for chat is equal to the satisfaction rate for email (H₀: p\_chat = p\_email)

Alternative Hypothesis (H₁): The satisfaction rate for chat is different from the satisfaction rate for email (H₁: p\_chat ≠ p\_email)

### Step 3: Checking Requirements

Before running our test, let's verify we meet the requirements:

```
# Calculate sample proportions  
chat_prop = 280/320  # ≈ 0.875 or 87.5%  
email_prop = 410/500  # ≈ 0.82 or 82%  
  
# Check success-failure condition for both groups  
def check_conditions(successes, n):  
    failures = n - successes  
    return {  
        'np': n * (successes/n),  
        'n(1-p)': n * (1 - successes/n),  
        'conditions_met': (n * (successes/n) >= 10) and (n * (1 - successes/n) >= 10)  
    }  
  
chat_check = check_conditions(280, 320)  
email_check = check_conditions(410, 500)  
  
print("Chat conditions:")  
print(f"np = {chat_check['np']:.1f}")  
print(f"n(1-p) = {chat_check['n(1-p)']:.1f}")  
print(f"Conditions met: {chat_check['conditions_met']}\n")  
  
print("Email conditions:")  
print(f"np = {email_check['np']:.1f}")  
print(f"n(1-p) = {email_check['n(1-p)']:.1f}")  
print(f"Conditions met: {email_check['conditions_met']}")
```

### Step 4: Conducting the Test

Now we can perform our hypothesis test:

```
from statsmodels.stats.proportion import proportions_ztest  
  
# Prepare data for scipy.stats.proportions_ztest  
count = np.array([280, 410])  # successes for chat and email  
nobs = np.array([320, 500])   # total observations for each group  
  
# Perform the test  
stat, pvalue = proportions_ztest(count, nobs)  
  
print(f"\nZ-statistic: {stat:.4f}")  
print(f"P-value: {pvalue:.4f}")  
  
# Calculate the effect size (difference in proportions)  
effect_size = (280/320) - (410/500)  
print(f"Effect size: {effect_size:.4f}")
```

### Step 5: Calculating Confidence Interval

To understand the practical significance:

```
# Calculate pooled proportion  
p_pooled = (280 + 410) / (320 + 500)  
  
# Calculate standard error  
se = np.sqrt(p_pooled * (1 - p_pooled) * (1/320 + 1/500))  
  
# Calculate 95% confidence interval  
z_critical = stats.norm.ppf(0.975)  # for 95% CI  
margin_error = z_critical * se  
ci_lower = effect_size - margin_error  
ci_upper = effect_size + margin_error  
  
print(f"\n95% Confidence Interval: ({ci_lower:.4f}, {ci_upper:.4f})")
```

### Step 6: Writing Up Results

Here's how you might present these findings to your support manager:

"I've analyzed the satisfaction rates between our chat and email support channels. Here's what I found:  
Chat support had a satisfaction rate of 87.5% (280 out of 320 responses), while email support had a satisfaction rate of 82% (410 out of 500 responses). This represents a 5.5 percentage point difference in favor of chat support.

Our statistical analysis shows this difference is statistically significant (p = 0.037), meaning it's unlikely this difference occurred by chance. We can be 95% confident that chat support's true satisfaction rate is between 0.3 and 10.7 percentage points higher than email support.

Business Implications:

1. The data supports that chat provides better customer satisfaction
2. The minimum improvement we're confident about (0.3 percentage points) might be too small to justify chat's higher cost
3. However, the potential improvement could be as high as 10.7 percentage points, which might make the investment worthwhile

 Recommendations:

1. Continue collecting data to narrow down the true difference
2. Consider analyzing the cost per satisfied customer for each channel
3. Look for patterns in types of issues where chat particularly excels"

This example shows how we move from raw data through statistical analysis to actionable business insights. Would you like me to elaborate on any part of this analysis or show how to adapt it for different scenarios?

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248633

Scraped At: 2026-05-15T10:16:02.858393
