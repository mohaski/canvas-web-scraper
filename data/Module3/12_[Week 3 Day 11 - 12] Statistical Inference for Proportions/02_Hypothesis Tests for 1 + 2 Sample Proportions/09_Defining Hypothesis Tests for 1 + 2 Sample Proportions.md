# Defining Hypothesis Tests for 1 + 2 Sample Proportions

# Defining Hypothesis Tests for 1 + 2 Sample Proportions

## ![](https://learning.flatironschool.com/courses/8021/files/4346282/preview) What is Hypothesis Tests for 1 + 2 Sample Proportions?

Icon Progress Bar (browser only)

10 min read

### Types of Proportion Tests

### One-Sample Proportion Test

Used when comparing a single sample proportion to a fixed value or target. For instance, testing whether a manufacturing process meets a 99% quality standard. The hypotheses might look like:

* H₀: p = 0.99 (The process meets the standard)
* H₁: p < 0.99 (The process falls below the standard)

### Two-Sample Proportion Test

Used when comparing proportions between two independent groups. For example, comparing conversion rates between two email campaigns. The hypotheses might be:

* H₀: p₁ = p₂ (Both campaigns have equal conversion rates)
* H₁: p₁ ≠ p₂ (The campaigns have different conversion rates)

#### The Test Statistic

The test statistic measures how far our sample results are from what we'd expect if the null hypothesis were true. For proportions, we typically use the z-statistic, which shows us how many standard deviations our observed difference is from the null hypothesis expectation.

##### one-sample test

For a one-sample test, the formula is:

![LaTeX: z = (p̂ - p₀) / \sqrt{(p₀(1-p₀)/n}](https://learning.flatironschool.com/equation\_images/z%2520%253D%2520(p%25CC%2582%2520-%2520p%25E2%2582%2580)%2520%252F%2520%255Csqrt%257B(p%25E2%2582%2580(1-p%25E2%2582%2580)%252Fn%257D?scale=1)

* p̂ is our sample proportion
* p₀ is the null hypothesis proportion
* n is our sample size

##### two-sample z-test statistic

The two-sample z-test statistic for proportions is:

![LaTeX: z = (p̂₁ - p̂₂) / \sqrt{(p̂ₚ(1-p̂ₚ)(1/n₁ + 1/n₂)}](https://learning.flatironschool.com/equation\_images/z%2520%253D%2520(p%25CC%2582%25E2%2582%2581%2520-%2520p%25CC%2582%25E2%2582%2582)%2520%252F%2520%255Csqrt%257B(p%25CC%2582%25E2%2582%259A(1-p%25CC%2582%25E2%2582%259A)(1%252Fn%25E2%2582%2581%2520%252B%25201%252Fn%25E2%2582%2582)%257D?scale=1)

Where p̂ₚ is the pooled proportion, calculated as:

p̂ₚ = (x₁ + x₂)/(n₁ + n₂)

Where x₁ and x₂ are the number of successes for each sample respectively

#### Let's break down why each part of this formula matters:

### The Numerator (p̂₁ - p̂₂)

This is the observed difference between our sample proportions. It tells us how big the difference is, but alone doesn't tell us if it's significant.

### The Pooled Proportion (p̂ₚ)

Under the null hypothesis (that there's no real difference between the groups), we assume both groups have the same underlying proportion. We estimate this shared proportion by pooling our data:

This represents our best estimate of the overall conversion rate if there truly is no difference between versions.

### The Denominator (Standard Error)

![LaTeX: \sqrt{(p̂ₚ(1-p̂ₚ)(1/n₁ + 1/n₂)}](https://learning.flatironschool.com/equation\_images/%255Csqrt%257B(p%25CC%2582%25E2%2582%259A(1-p%25CC%2582%25E2%2582%259A)(1%252Fn%25E2%2582%2581%2520%252B%25201%252Fn%25E2%2582%2582)%257D?scale=1)
represents the standard error of the difference between proportions. It accounts for:

* The variability in our data (p̂ₚ(1-p̂ₚ))
* The sample sizes of both groups (1/n₁ + 1/n₂)

### Effect Size

The effect size for proportions is typically measured as the difference between proportions (p₁ - p₂) or as a ratio (p₁/p₂). Understanding effect size helps us determine if a statistically significant difference is also practically meaningful.

### Important Assumptions

Proportion tests rely on several key assumptions:

1. Random Sampling: Each observation must be independently selected from the population
2. Independence: Observations must not influence each other
3. Large Sample Size: Both np and n(1-p) should be at least 10 for each group
4. Binary Outcomes: Each observation must be classified into one of two categories

 Understanding these concepts allows us to:

* Design appropriate tests for our questions
* Collect sufficient data to make reliable conclusions
* Interpret results correctly
* Communicate findings effectively to stakeholders

This framework helps us make data-driven decisions while accounting for the role of chance in our observations. Whether we're analyzing A/B tests, quality control processes, or survey responses, these concepts provide the foundation for reliable statistical inference about proportions.

### How does Hypothesis Tests for 1 + 2 Sample Proportions work?

Think of hypothesis testing as a structured way to play "prove me wrong" with data. We start with a claim that there's nothing special going on - this is our null hypothesis.

For example, when comparing two marketing campaigns, our null hypothesis might be "both campaigns perform equally well." This is like saying "prove to me that Campaign B is actually different from Campaign A."

The beauty of this approach is that we can quantify exactly how strong our evidence needs to be to reject this initial claim. We do this by asking: "If there really were no difference between the campaigns, how likely would we be to see differences as large as what we observed in our data?"

Let's walk through how this works in practice. Imagine you're analyzing two email campaigns:

* Campaign A: 150 conversions from 1000 emails (15%)
* Campaign B: 210 conversions from 1200 emails (17.5%)

The process unfolds in several logical steps:

### Analyze The Raw Data

First, we calculate what we actually observed - a 2.5 percentage point difference between campaigns. But is this difference meaningful, or could it have happened by chance?

To answer this, we need to understand what "by chance" looks like. If both campaigns truly had the same conversion rate (our null hypothesis), we'd expect some random variation in our samples. This variation follows a predictable pattern - the sampling distribution of differences in proportions.

Think of it like this: If you flipped two fair coins many times, you wouldn't always get exactly 50% heads for both coins.

Sometimes one coin might show 55% heads while the other shows 45%. The sampling distribution tells us how common different sizes of differences are under the null hypothesis.

The z-statistic translates our observed difference into a standardized measure - how many "standard deviations away from expected" our result is. It's like asking, "How unusual is this difference compared to what we'd typically see by chance?"

### Plan the Testing

For our email campaigns:

1. We first pool our data to estimate what the "true" shared conversion rate might be if there really were no difference: (150 + 210)/(1000 + 1200) ≈ 16.4%
2. We then calculate how much random variation we'd expect to see in differences between samples of our sizes
3. Finally, we compare our actual observed difference to this expected variation

The p-value then tells us: "If there really were no difference between campaigns, what's the probability we'd see a difference this large or larger just by chance?" A small p-value (typically less than 0.05) suggests our observed difference is too large to easily explain as random chance.

The power of this approach lies in its ability to help us make decisions while explicitly accounting for uncertainty. Rather than just saying "Campaign B had a higher conversion rate," we can say "The difference we observed is (or isn't) larger than what we'd typically expect to see by chance."

### Code The Testing

The statsmodels.stats.proportion module provides the [proportions\_ztest


Links to an external site.](https://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportions_ztest.html) function, which handles both one-sample and two-sample proportion tests. This function:

* Automatically calculates the z-statistic and p-value
* Handles the mathematical complexity under the hood
* Provides reliable results that match standard statistical software
* Allows for one or two-sided tests

##### 1-Sample proportion z-test:

```
from statsmodels.stats.proportion import proportions_ztest  
count = 5  
nobs = 83  
value = .05  
stat, pval = proportions_ztest(count, nobs, value, prop_var=value)
```

#### 2-Sample proportion z-test:

```
import numpy as np  
from statsmodels.stats.proportion import proportions_ztest  
count = np.array([5, 12])  
nobs = np.array([83, 99])  
stat, pval = proportions_ztest(count, nobs)
```

### Conceptualize Hypothesis Tests for 1 + 2 Sample Proportions

**Term**

**Definition**

**Example**

Population Proportion

The true proportion of a characteristic in an entire population that we're trying to estimate; typically unknown in practice

The actual percentage of all Netflix users who watch documentaries. While we can't survey every user, this unknown value exists and is what we aim to estimate.

Sample Proportion

The observed proportion from our sample data, calculated as number of successes divided by sample size; serves as our estimate of the population proportion

If 280 out of 400 surveyed Netflix users watch documentaries, our sample proportion is 0.70 or 70%. This helps us estimate the true population proportion.

Standard Error

A measure of the variability in our sample proportion that tells us how precise our estimate is likely to be; calculated as √(p̂(1-p̂)/n)

With 400 surveyed users and a 70% viewing rate, our standard error would be √(0.70 \* 0.30 / 400) ≈ 0.023, meaning our estimate might typically vary by about 2.3 percentage points.

Success-Failure Condition

A requirement that we have at least 10 successes (np̂ ≥ 10) and 10 failures (n(1-p̂) ≥ 10) in our sample to use normal-based methods

In our Netflix survey with 280 documentary watchers and 120 non-watchers, both values exceed 10, so we can use our standard methods.

Null Hypothesis

The default assumption we start with, typically stating there is no effect or no difference between groups

When comparing two marketing campaigns, H₀: "There is no difference in conversion rates between campaigns" (p₁ = p₂).

Alternative Hypothesis

The claim we need evidence to support, stating there is an effect or difference between groups

H₁: "The new marketing campaign has a different conversion rate than the old one" (p₁ ≠ p₂).

P-value

The probability of observing results as extreme as ours if the null hypothesis were true; smaller values provide stronger evidence against the null hypothesis

If p = 0.03 when comparing marketing campaigns, we'd only expect to see differences this large about 3% of the time if the campaigns were truly equally effective.

Effect Size

The practical magnitude of the difference between groups or from a target value; helps determine if a statistically significant result is also meaningful in practice

A 5 percentage point increase in conversion rate (from 15% to 20%) represents the effect size. Even if statistically significant, we need to decide if this size improvement justifies any additional costs.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248630

Scraped At: 2026-05-15T10:15:56.853858
