# What is Experimental Design and Statistical Testing?

# What is Experimental Design and Statistical Testing?

## ![](https://moringa.instructure.com/courses/1426/files/631696/preview) What is Experimental Design and Statistical Testing?

Icon Progress Bar (browser only)

18 min read

**Experimental Design** refers to the structured methodology of planning and conducting research studies to test hypotheses and examine cause-effect relationships. Think of it as creating a careful "recipe" for your experiment that will give you trustworthy results. Just as a chef carefully controls ingredients and cooking conditions to perfect a dish, we control variables and conditions to understand cause and effect relationships.

**Statistical Testing** is the framework we use to make decisions about our experimental results, helping us determine whether the patterns we see in our data are real or just due to chance. It's like being a detective, gathering evidence (data) and then determining if that evidence is strong enough to support our conclusions.

Let's examine the key terms and concepts that form the foundation:

### Experimental Design Terms

* **Control Group:** The baseline group that doesn't receive the treatment being tested.
* **Treatment/Experimental Group:** The group that receives the intervention being studied; there could be more than one.
* **Independent Variable:** The factor researchers manipulate during the experiment.
* **Dependent Variable:** The outcome being measured to assess the treatment's effect.
* **Confounding Variables:** External factors that might influence the relationship.
* **Randomization:** The process of randomly assigning participants to different group.

### Statistical Testing Terms

* **Null Hypothesis (H₀):** The default assumption that there's no effect or difference.
* **Alternative Hypothesis (H₁):** The claim we're investigating.
* **p-value:** The probability of seeing our results if the null hypothesis were true.
* **Significance Level (α):** Our threshold for rejecting the null hypothesis.
* **Type I Error:** Incorrectly rejecting a true null hypothesis (false positive).
* **Type II Error:** Failing to reject a false null hypothesis (false negative).
* **Statistical Power:** The probability of detecting a real effect when one exists.

### Two-sided Versus One-sided Tests

Let’s explain the subtle differences between one-sided and two-sided hypothesis tests, as this is a crucial concept that often causes confusion. First, let's understand what we mean by "sides" in hypothesis testing. The "sides" refer to the direction of the effect we're looking for and whether we care about differences in one particular direction or in either direction.

#### Two-Sided Tests

A **two-sided (also called two-tailed) test examines whether there's a difference in either direction**. We use these when we want to know if something is different, regardless of whether it's greater or less. For example, imagine we're testing whether a new medication affects heart rate:

* There is **not a significant difference** in the mean heart rate of users of the new versus old medication.
  + **Null Hypothesis (H₀)**: The medication has no effect on heart rate.
* There is **a significant difference** in the mean heart rate of users of the new medication.
  + **Alternative Hypothesis (H₁)**: The medication changes heart rate, either up or down.

#### One-Sided Tests

A one-sided (or one-tailed) test looks for differences in only one direction. We use these when we specifically care about whether something is greater or less, but not both. Let's say we're testing a new weight loss program:

* The mean weight of people in the new program **was not significantly less than** the old program but could be greater.
  + **Null Hypothesis (H₀):** The program does not reduce weight.
* The mean weight of people in the new program **was less than** the mean weight of people in the old program.
  + **Alternative Hypothesis (H₁):** The program reduces weight.

#### Key Differences

##### **Critical Region:**

* Two-sided tests split the α (significance level) between both tails of the distribution (greater or less than)
* One-sided tests put all of α in one tail

##### **Statistical Power:**

* One-sided tests have more power to detect an effect in the specified direction
* However, they completely miss effects in the opposite direction

##### **When choosing between one-sided and two-sided tests, ask yourself:**

1. Do you have a specific directional hypothesis?
2. Would an effect in the opposite direction be meaningful?
3. Is there any possibility of an effect in the opposite direction?

**If you're unsure, it's generally safer to use a two-sided test,** as it avoids missing unexpected effects in the opposite direction. One-sided tests should only be used when you have a strong theoretical or practical reason to only care about effects in one direction.

These concepts work together to create what we call internal validity (the confidence that changes in the dependent variable are actually caused by the independent variable) and external validity (the extent to which results can be generalized to other situations and populations).

Understanding these terms is crucial because they form the building blocks of proper experimental design and statistical testing. When researchers carefully consider and implement these elements, they can create experiments that produce reliable, meaningful results that advance our understanding of the world around us.

### How does Experimental Design and Statistical Testing work?

Experimental Design and Statistical Hypothesis Testing form the foundation for making rigorous, data-driven business decisions. These methodologies work together to **help us determine whether observed changes in our metrics represent genuine effects or mere random variation.**

When designing experiments, we carefully structure our approach to isolate the effect we want to measure while controlling for other variables. This might mean A/B testing a new website design, comparing different medical treatments, or evaluating customer responses to product changes. The key is that **our experimental design must account for the natural variation that exists in any real-world measurement**. This is where probability distributions enter the picture; they provide the mathematical framework to model and understand this inherent variation in our data.

**Statistical hypothesis testing then gives us a systematic way to analyze our experimental results**. We begin by stating a null hypothesis (H₀) that assumes no effect from our change, along with an alternative hypothesis (H₁) that represents the effect we're looking to detect.   
  
**The probability distribution of our measurements under the null hypothesis becomes our baseline**, allowing us to calculate how likely it would be to observe our experimental results if the null hypothesis were true. If our observed results would be very unlikely under the null hypothesis (typically using a threshold p-value of 0.05), we can reject it in favor of our alternative hypothesis and conclude that our experimental change had a genuine statistically significant effect.

This structured approach of careful experimental design followed by statistical hypothesis testing helps ensure that our business decisions are based on genuine insights rather than random fluctuations in our data. By understanding and accounting for natural variation through probability distributions, we can confidently identify when changes in our metrics represent meaningful effects that should inform our decision-making.

#### Experimental Design

First, we need to **clearly define what we're testing and how we'll measure success**. This is like creating a detailed blueprint before building a house. We ask ourselves:

* What exactly are we measuring?
* What changes do we expect to see?
* What might interfere with our measurements? (Time of day, seasonal effects, user demographics)

Next, we **set up our experiment structure.** This is similar to setting up laboratory conditions, but in our digital environment we need:

1. **Control Group:** Users who see no change
2. **Treatment Group**: Users who see the treatment

The key is that everything else about their experience should be identical. This isolation of our variable is crucial,  just as a scientist controls laboratory conditions, we need to control our digital environment.

Next we need to consider an appropriate sample size. You can think of sample size determination as answering the question "How many observations do I need to be confident in my results?"   
  
To determine sample size, we need to consider [**four key components**](#dpPopup0Content).

##### Four Key Components

**Effect Size:**

1. 1. First, we need to **decide what size of change would be meaningful for the business.** For example, maybe a 2% increase in click-through rate would justify the cost of the website redesign. This is our minimum detectable effect - the smallest change we care about being able to find if it exists.
   2. Once you have your practical minimum effect, **you need to standardize it.** The most common standardized effect size is Cohen's d, which expresses the difference in terms of standard deviations. Here's how to calculate it:

**Cohen's d = (μ₁ - μ₂) / σ Where:**

* μ₁ - μ₂ is your minimum desired difference
* σ is the population (or sample) standard deviation

Think of this like adjusting a microscope. If you're looking for large objects, you don't need as much magnification. But if you're trying to spot tiny differences, you need more powerful magnification (in our case, a larger sample size).

**Statistical Power:**

* **Power is our ability to detect a real effect when one exists.** The standard target is 80% power, meaning if there really is an effect of our specified size, we'll detect it 80% of the time.
* This is like setting the sensitivity of a metal detector. With higher power, we're less likely to miss something important, but we need more time (larger sample size) to scan thoroughly.

**Significance Level (α)**:

* This is **typically set at 5% (0.05) and represents our tolerance for false positives.** It's the probability we'll conclude there's an effect when there actually isn't one. In practice this value is set before conducting an experiment and can vary widely depending on the context and industry.
* Think of this like a smoke alarm's sensitivity. Set it too sensitive (high α), and you get false alarms. Set it too insensitive (low α), and you might miss real fires.

**Variance:**

* We need to **estimate** **how much natural variation exists in our metric.** For example, if conversion rates naturally fluctuate between 1% and 5%, we need a larger sample than if they typically stay between 2.9% and 3.1%.
* This is like trying to hear a specific voice in a crowd. The more background noise (variance), the more time you need to listen to be sure you're hearing the right voice.

#### Power Analysis brings these components together

1. **Start with Business Requirements**
   * What effect size would make the change worthwhile?
   * How confident do we need to be in our decision?
   * How much risk can we tolerate?
2. **Consider Practical Constraints**
   * How much time do we have?
   * How much traffic do we get?
   * What costs are involved?
3. **Calculate Required Sample Size**: The larger the sample size:
   * The smaller the effect we can detect.
   * The more confident we can be in our results.
   * The more power we have to detect real effects.

 But there's always a tradeoff. **While larger samples give better results, they also:**

* Take longer to collect
* Cost more to obtain
* May delay important decisions

There are a variety of **ways to conduct a power analysis in order to determine the appropriate sample size** for your experiments.

1. **Online calculators** that allow you to enter and adjust the power, the minimum detectable effect desired, and the significance level.

* [Statsig


  Links to an external site.](https://www.statsig.com/calculator)
* [Abtasty


  Links to an external site.](https://www.abtasty.com/sample-size-calculator/)
* [Evanmiller


  Links to an external site.](https://www.evanmiller.org/ab-testing/sample-size.html)

1. **[Python library for statistics


   Links to an external site.](https://www.statsmodels.org/dev/stats.html#power-and-sample-size-calculations).** The Statsmodels library for python has convenient functions to conduct power analysis for a wealth of different statistical tests.

#### Statistical Testing

Once we have our experiment designed we can **properly set up our hypothesis testing framework** in order to extract meaningful inference from the experiment and data collected.

* We **start with a null hypothesis (H₀)** - our default assumption, like "there's no difference between the old and new website designs." We then collect data to potentially disprove this null hypothesis in favor of our alternative hypothesis (H₁) - "the new design performs better."
* After defining our null and alternative and collecting the appropriate sample data we need to **select an appropriate statistical test** that matches with our data. The choice of statistical test depends on several key factors, which we can think about like a decision path.   
    
  Let's walk through these **[factors](#dpPopup1Content).**

1. **Type of Data:** In an e-commerce example, we might be looking at order values, which are continuous numerical data (they can take any value within a range). However, in your work, you might encounter different types of data:

* **Continuous Data:** Things like prices, temperatures, or times that can take any value within a range.
* **Categorical Data:** Categories like customer segments or product types
* **Count Data:** Whole numbers like number of purchases or website visits
* **Binary Data:** Yes/no outcomes like whether a customer made a purchase

1. **Number of Groups:** In our previous examples, we're comparing two groups: this is a two-sample test scenario. You might encounter:

* **One-sample tests:** Comparing one group to a known population value
* **Two-sample tests:** Comparing two groups
* **Multiple-sample tests:** Comparing three or more groups

1. **Independence and Pairing**: Are your samples independent or paired? In our email campaign example, they're likely independent - different customers in each group. However, if you were measuring order values before and after a change for the same customers, you'd have paired data. (More on this in a later module)
2. **Assumptions About the Data:** This is where your understanding of distributions becomes crucial. The most common statistical tests assume your data follows certain patterns:

* **Normal Distribution:** The famous bell curve
* **Equal Variances:** The spread of data is similar between groups
* **Independence:** One observation doesn't affect another

The specific statistical test chosen determines how the test statistic is calculated and what distribution is used to define the null hypothesis to compare against.

![decision tree for choosing a statistical test](https://moringa.instructure.com/courses/1426/files/631587/preview)

* Next, we can **conduct the actual statistical test** in order to determine significance based on a returned p-value. Just as we compared a person's height to the distribution of heights in the population, we can compare our test result to what we'd expect under the null hypothesis. We do this mathematically via the test statistic, null distribution, and a p-Value (probability):
  + The test statistic is our way of standardizing the observed difference between treatment groups. For example, in a t-test, we take the difference between groups and scale it based on the variability in our data. This is like converting a height from feet and inches into "standard deviations away from average" so we can make fair comparisons.  
      
    Here's how the process works:

1. First, we **calculate our test statistic from our data**. This single number captures how large the effect we observed is, taking into account both the size of the difference and the variability in our data. Test statistics for a variety of different tests follow a similar pattern/formula:  Measure of Difference / Measure of Total Variation.
2. This test statistic has a known probability distribution under the null hypothesis. For example, if the null hypothesis is true, a t-test statistic follows a t-distribution. Think of this as knowing what range of heights we'd normally expect to see based on the null hypothesis.
3. The p-value is then calculated by asking: "If the null hypothesis were true, what's the probability of seeing a test statistic as extreme as or more extreme than what we observed?" We find this by looking at the area in the tails of our probability distribution, using the CDF introduced in 1 module.

**Think of it like this:** if we measure someone who's 6'8" tall, we can calculate how many standard deviations above average this is (our test statistic), then use the normal distribution to find how rare this height is (our p-value). The same principle applies in statistical testing - we're just measuring how unusual our results are relative to what we'd expect by chance. We use the significance level as the cutoff/threshold for determining if the observed difference or effect is significant.

* Finally, after collecting data and running our test we can analyze the results to make our decision. If this probability (p-value) is very small (less than significance level), we reject the null hypothesis and conclude our treatment had a significant effect.   
    
  **“If the p-value is low (less than alpha) the null must go”**

Think about significance level (α) like a judge's standard for conviction. Setting α = 0.05 is like saying "we need to be 95% confident before we'll reject the null hypothesis." This helps control for Type I errors (false positives, or convicting an innocent person) but also affects our ability to detect real differences (Type II errors, or letting a guilty person go free). The significance level determines the test's critical value.

![hypothesis testing the data not being special](https://moringa.instructure.com/courses/1426/files/631590/preview)

A **critical value is like a statistical threshold** that helps us decide whether to reject or fail to reject our null hypothesis. Think of it as a boundary line that separates "normal" results we might see by chance from "unusual" results that suggest something real is happening. Just as a doctor might use a specific temperature threshold to determine if someone has a fever, we use critical values to determine if our statistical results are significant.

The **critical value is directly connected to our chosen significance level (α)**. For example, with a standard significance level of 0.05 in a two-tailed test using the normal distribution, our critical values would be -1.96 and +1.96. These numbers aren't arbitrary; they're chosen because exactly 5% of a normal distribution lies beyond these values (2.5% in each tail: think back to the empirical rule)

![critical values](https://moringa.instructure.com/courses/1426/files/631597/preview)

**Different tests use different critical values.** For example, t-tests use values from the t-distribution, which has heavier tails than the normal distribution and depends on our sample size. This accounts for the additional uncertainty when working with smaller sample sizes. Comparing test statistics to critical values is the same as comparing p-values to your significance levels (Two sides of the same coin).

* Here's a thought experiment to deepen understanding: Imagine testing a new medication. Which would be worse:
  + Falsely concluding it works when it doesn't (Type I error)?
  + Failing to detect that it works when it does (Type II error)?

This illustrates why we often need to balance these risks based on the real-world consequences of our decisions.

The beauty of this approach is that it brings scientific rigor to our technical decisions. Instead of relying on intuition or incomplete data, we can make confident, data-driven decisions about our systems and features.

### Conceptualize Experimental Design and Statistical Testing

Key Terms Experimental Design and Statistical Testing

| Term | Definition | Example |
| --- | --- | --- |
| Statistical Power | The probability of detecting a real effect when one exists | If power = 0.8, we have an 80% chance of detecting a true difference of our specified size |
| Effect Size | A standardized measure of the magnitude of an observed relationship or difference | A Cohen's d of 0.5 indicates a medium-sized difference between two groups |
| Control Group | The baseline group that receives no treatment or the current standard | Users who see the current version of the website |
| Treatment Group | The experimental group that receives the intervention being tested | Users who see the new version of the website |
| Confounding Variable | An external factor that could affect both the independent and dependent variables, potentially leading to misleading conclusions | Time of day affecting both user traffic and conversion rates |
| Sample Size | The number of observations needed to achieve desired statistical power | Needing 1000 users per group to detect a 2% difference in conversion rates |
| Randomization | The process of randomly assigning subjects to treatment conditions to eliminate bias | Randomly showing users either the old or new website version |
| Hypothesis Testing | A statistical method for making decisions about populations based on sample data, using probability to determine if a proposed statement about a population parameter is true | Testing whether a new medication is more effective than a placebo by comparing recovery rates between two groups |
| Null Hypothesis (H₀) | The default assumption of no effect or no difference between groups, which we assume true until evidence suggests otherwise | "There is no difference in average recovery time between patients taking the new medication and those taking the placebo" |
| Alternative Hypothesis (H₁) | The research claim that contradicts the null hypothesis, representing the effect we're looking for | "There is a difference in average recovery time between patients taking the new medication and those taking the placebo" |
| P-value | The probability of observing results as extreme as or more extreme than our sample data, assuming the null hypothesis is true | If p = 0.02, there's a 2% chance of seeing such extreme differences in recovery times if the medication truly had no effect |
| Significance Level (α) | The threshold probability below which we reject the null hypothesis, representing our tolerance for Type I errors | Setting α = 0.05 means we're willing to accept a 5% chance of falsely concluding the medication works when it doesn't |
| Type I Error | Rejecting a true null hypothesis (false positive), occurs with probability α | Concluding the medication works when it actually doesn't |
| Type II Error | Failing to reject a false null hypothesis (false negative), occurs with probability β | Failing to detect that the medication works when it actually does |
| Test Statistic | A standardized value calculated from sample data that we compare to critical values to make our decision | A t-statistic of 2.5 indicates our observed difference is 2.5 standard errors away from what we'd expect under the null hypothesis |
| One-tailed Test | A hypothesis test that looks for an effect in only one direction | Testing if the new medication reduces recovery time (not interested in if it increases time) |
| Two-tailed Test | A hypothesis test that looks for an effect in either direction | Testing if the new medication affects recovery time (could increase or decrease) |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248568

Scraped At: 2026-05-15T10:12:08.859614
