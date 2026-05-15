# Defining Goodness of Fit

# Defining Goodness of Fit

## ![](https://learning.flatironschool.com/courses/8021/files/4346282/preview) What is Chi-Squared Goodness of Fit?

Icon Progress Bar (browser only)

11 min read

The Chi-Squared Goodness of Fit test is a statistical method that helps us determine whether observed frequencies in categorical data match expected frequencies or theoretical distributions. Let me break down the key terms and concepts to build a clear understanding.

### Chi-Squared Statistic

The chi-squared statistic (χ²) measures the total discrepancy between observed and expected frequencies across all categories. Think of it as a mathematical way to quantify how different your actual data is from what you expected to see. The larger this number becomes, the more evidence we have that the observed data doesn't match our expectations.

### Observed Frequencies

These are the actual counts we collect from our data. For example, if we survey 100 customers about their preferred payment method, we might observe 45 using credit cards, 30 using debit cards, and 25 using digital wallets. These numbers represent what actually happened in our sample/data.

### Expected Frequencies

These represent our theoretical predictions or hypothesized values for each category. Expected frequencies can come from historical data, theoretical models, or business assumptions. For instance, if we believe payment methods should be equally preferred, we would expect about 33 customers in each category out of our 100 respondents.

### Degrees of Freedom

This concept represents the number of independent values that are free to vary in our final calculation. For a goodness of fit test, it equals the number of categories minus one (k-1). Understanding degrees of freedom is crucial because it affects the critical values we use to make decisions about our data.

### Null Hypothesis (H₀)

This is our initial assumption that there is no significant difference between observed and expected frequencies. The null hypothesis essentially states that any differences we see are due to random chance rather than a real pattern.

### Alternative Hypothesis (H₁):

This represents the claim that there is a significant difference between observed and expected frequencies. If we reject the null hypothesis, we accept this alternative explanation that the differences we observe are meaningful. NOTE: Chi-squared tests are inherently “one-sided”.

These concepts work together in the following way: We collect our observed frequencies and compare them to our expected frequencies by calculating the chi-squared statistic. We then use the degrees of freedom and significance level to find our critical value. Finally, we make a decision based on comparing our calculated statistic to the critical value (or by examining the p-value).

### How does Chi-Squared Goodness of Fit work?

The Chi-Squared Goodness of Fit test helps us determine whether the frequencies we observe in our data match what we would expect based on some theory or historical pattern. Think of it like a quality control inspector comparing actual product measurements against design specifications. Just as the inspector needs to decide whether deviations from specifications are concerning or just normal variation, this test helps us make similar decisions about categorical data.

The test works by measuring the gap between what we observe and what we expect. For each category, we calculate how far our observed count strays from the expected count, but with a twist - we account for the fact that a difference of 5 items matters more when we expected 10 than when we expected 100. We combine all these differences into a single number (the chi-squared statistic) that tells us how well our data fits our expectations.

Let's see this in action with a real-world example, then implement it in Python:

The chi-square ($\chi^2$) test is applicable for \*\*discrete\*\* variables that can be represented by a \*\*probability mass function\*\*, which allows us to understand the data in terms of the \*\*frequencies\*\* of each outcome. There are several different kinds of chi-square tests depending on the question being asked, but we'll focus on \*Pearson's chi-square test\* and how it is applied for goodness of fit.

Let's start with a goodness of fit example. This is kind of like the one-sample t-test shown above, in that we are comparing sample data to a theoretical value. This time instead of comparing the sample mean to a theoretical mean, we will compare the frequencies of observed data to the expected frequencies.

### Coin Toss Example: Fair Coin?

For this example, let's use the coin toss at the Super Bowl (data through Super Bowl 55). We expect that this is a "fair" coin, meaning that we would expect it to produce Heads and Tails equally often.

### Data

```
# Data from sportsbettingdime.com  
sb_data = pd.read_csv("superbowl.csv")  
sb_data.tail()
```

Coin Toss Example: Fair Coin?

| Super Bowl | Coin Toss Outcome | Coin Toss Winner | **Game Winner** |
| --- | --- | --- | --- |
| 51 | Tails | Home Team | Away Team |
| 52 | Heads | Home Team | Away Team |
| 53 | Tails | Home Team | Away Team |
| 54 | Tails | Away Team | Home Team |
| 55 | Heads | Away Team | Home Team |

### Code

```
coin_toss_counts = sb_data["Coin Toss Outcome"].value_counts().sort_index()  
coin_toss_counts  
Heads    26  
Tails    29  
Name: Coin Toss Outcome, dtype: int64  
fig, ax = plt.subplots()  
  
# Extract observed counts  
fair_coin_observed = coin_toss_counts.values  
# Heads and tails each expected half the time  
fair_coin_expected = [sum(coin_toss_counts)/2, sum(coin_toss_counts)/2]  
  
# Placeholder data for display purposes; you can ignore these values  
x = np.array([0, 5])  
offset = 1  
bar_width = 2  
  
# Plot bars  
ax.bar(x-offset, fair_coin_observed, bar_width, label="Observed")  
ax.bar(x+offset, fair_coin_expected, bar_width, label="Expected")  
  
# Customize appearance  
ax.set_xticks(x)  
ax.set_xticklabels(["Heads", "Tails"])  
ax.set_ylabel("Count")  
ax.legend(loc="right")  
fig.suptitle("Super Bowl Coin Tosses")
```

### Output

![coin toss graph of observed vs expected results](https://moringa.instructure.com/courses/1426/files/631610/preview)

The orange bar shows a theoretical (expected) value and the blue shows what we actually observed from our sample.

The expected value is not a single line representing a parameter, it's a pair of orange bars showing how many times we would expect to see Heads and Tails outcomes.

As you can see, the coin toss at the Super Bowl has had slightly fewer Heads results and slightly more Tails results than we expected. But is that difference statistically significant?

### Coin Toss Solution: Goodness of Fit Test

As you can see, the coin toss at the Super Bowl has had slightly fewer Heads results and slightly more Tails results than we expected. But is that difference statistically significant?

To answer this, we'll need to perform a chi-square goodness of fitness test.

**A goodness of fit test:**

* Has null and alternative hypotheses about the frequencies of categorical data. For the example shown above, we'll use the null hypothesis that $P(\text{Heads}) = 0.5$ and $P(\text{Tails}) = 0.5$, i.e. that there is no significant difference between the observed and expected values. The alternative hypothesis is that there is a significant difference.
* Involves the calculation of a \*\*chi-square statistic\*\* (also just referred to as $\chi^2$) that represents a standardized version of the difference between the observed and expected values
* Compares this $\chi^2$ to the chi-square distribution (the shape of which varies depending on the degrees of freedom) in order to determine whether we can reject the null hypothesis at a given alpha level — i.e. to determine whether the difference between the data and the theoretical expectation is statistically significant

### Coin Toss Solution

Once again, the simplest way to do this is using [scipy.stats


Links to an external site.](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html). We will say that our alpha is 0.01.

### Running ChiSquare Code

```
fair_coin_result = stats.chisquare(fair_coin_observed, fair_coin_expected)  
fair_coin_result
```

### Code Output and Conclusion

```
Power_divergenceResult(statistic=0.16363636363636364, pvalue=0.6858304344516056)
```

Based on the results above, we fail to reject the null hypothesis at our desired significance level. This is because we found a p-value of 0.69, which is higher than our specified
![LaTeX: \alpha=0.01](https://learning.flatironschool.com/equation\_images/%255Calpha%253D0.01?scale=1)
.

In other words, we do not have statistically significant evidence that the coin used here is not a "fair" coin! This was an example of a "goodness of fit" application of chi-square.

### Chi-Square Test Calculations

In some cases, you will have extremely limited time for applying statistical tests, and will only have the bandwidth to learn how the null and alternative hypotheses are set up, and the code to execute the test. You'll need to be comfortable with some level of ambiguity, now that you're familiar with statistical tests in general!

But for now, let's break down the previous problem to understand what this statistical test is doing. How did it produce that p-value?

### Chi-Square Statistic

### Chi Square Statistics Formula

Here is the formula for
![LaTeX: \chi^2](https://learning.flatironschool.com/equation\_images/%255Cchi%255E2?scale=1)
:

![LaTeX: \chi^2=\sum\_{i=1}^{n} \frac{(O\_i - E\_i)^2}{E\_i}](https://learning.flatironschool.com/equation\_images/%255Cchi%255E2%253D%255Csum\_%257Bi%253D1%257D%255E%257Bn%257D%2520%255Cfrac%257B(O\_i%2520-%2520E\_i)%255E2%257D%257BE\_i%257D?scale=1)

Spelling this out, it means that we are finding the sum of the squared difference between the observed and expected values
![LaTeX: (O\_i - E\_i)^2](https://learning.flatironschool.com/equation\_images/(O\_i%2520-%2520E\_i)%255E2?scale=1)
divided by the expected values
![LaTeX: E\_i](https://learning.flatironschool.com/equation\_images/E\_i?scale=1)
for all categories
![LaTeX: i](https://learning.flatironschool.com/equation\_images/i?scale=1)
. Just like a t-statistic, it is representing the difference between values in a lower-dimensional way.

### Running ChiSquare statistics code

```
n = 2 # number of categories (Heads, Tails)  
chi_square = sum([((fair_coin_observed[i] - fair_coin_expected[i])**2)/fair_coin_expected[i] for i in range(n)])  
chi_square
```

### Code Output and Solution

Result of ChiSquare statistics code

`0.16363636363636364`

Note that this is the same as the statistic from when we called the chisquare function.

### Chi-Square Distribution

### Plotting Chi-Square Distribution

Plotting the relevant distribution for our current number of categories (degrees of freedom). Then we can find the critical value and plot that as well.

**Code Input:**

```
alpha = 0.01  
critical_value = stats.chi2.ppf(1-alpha, df=n-1)  
  
fig, ax = plt.subplots()  
  
ax.plot(x, y, color='darkblue', label=r"$\chi^2$ distribution PDF")  
ax.axvline(critical_value, color='green', linestyle="--", label=r"critical $\chi^2$")  
  
ax.legend();
```

**Output:**

![Chi-Square Distribution graph difference between relevant and critical distributions](https://moringa.instructure.com/courses/1426/files/631747/preview)

We won't actually plot the rejection region here because it is so small; just know that anywhere under the blue PDF line and to the right of the green line is the rejection region.

### Plotting Observed Chi-Square

Now we'll add our observed chi-square to this plot.

**Code Input:**

```
fig, ax = plt.subplots()  
  
  
ax.plot(x, y, color='darkblue', label=r"$\chi^2$ distribution PDF")  
ax.axvline(critical_value, color='green', linestyle="--", label=r"critical $\chi^2$")  
ax.axvline(chi_square, color='red', label=r"observed $\chi^2$")  
  
  
ax.legend();
```

**Output:**

![chi squared goodness fit graph fir distribution, critial and observed data ](https://moringa.instructure.com/courses/1426/files/631745/download)

To reject the null hypothesis, the observed chi-square would need to be to the right of the critical chi-square, but we can see that it is well to the left.

### Calculate p-value

Alternatively, we could calculate the p-value directly, this is the same value we got from the chisquare function:

**Code Input:**

```
stats.chi2.sf(chi_square, df=df)
```

**Output:**

```
0.6858304344516056
```

 The beauty of using scipy.stats is that it handles all the complex calculations while allowing us to focus on the business logic and interpretation. The chisquare function combines multiple mathematical steps into a single operation, making our code both more reliable and easier to maintain.

### Conceptualize the Chi-Squared Goodness of Fit

**Term**

**Definition**

**Example**

Null Hypothesis (H₀)

The default assumption that any differences between observed and expected frequencies are due to random chance

In a dice rolling experiment, H₀ would state that each number (1-6) has an equal probability of being rolled (1/6)

Alternative Hypothesis (H₁)

The claim that the differences between observed and expected frequencies are statistically significant

The dice is not fair, and some numbers appear more frequently than expected by chance

Observed Frequencies

The actual counts collected from your data

In 300 dice rolls: {1: 42, 2: 55, 3: 48, 4: 52, 5: 57, 6: 46}

Expected Frequencies

The theoretical or predicted counts based on your hypothesis

For fair dice with 300 rolls: {1: 50, 2: 50, 3: 50, 4: 50, 5: 50, 6: 50}

Chi-Squared Statistic (χ²)

A measure of the total discrepancy between observed and expected frequencies, calculated as Σ((O-E)²/E)

If χ² = 2.84 for our dice rolls, this represents the sum of squared differences between observed and expected counts, scaled by expected counts

Degrees of Freedom (df)

The number of categories minus one, representing independent values that are free to vary

For a six-sided die, df = 6 - 1 = 5

P-value

The probability of obtaining test results at least as extreme as those observed, assuming the null hypothesis is true

If p = 0.724, there's a 72.4% chance of seeing these or more extreme differences even with a fair die

Critical Value

The threshold value of χ² that determines whether to reject H₀, based on chosen significance level and degrees of freedom

For α = 0.05 and df = 5, the critical value is 11.07

Significance Level (α)

The threshold probability below which we reject the null hypothesis

Commonly set at 0.05, meaning we accept a 5% chance of incorrectly rejecting H₀

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248708

Scraped At: 2026-05-15T10:21:22.217265
