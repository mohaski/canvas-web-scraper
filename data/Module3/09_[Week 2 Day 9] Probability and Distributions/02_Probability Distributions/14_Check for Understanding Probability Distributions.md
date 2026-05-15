# Check for Understanding: Probability Distributions

# Check for Understanding: Probability Distributions

## ![](https://moringa.instructure.com/courses/1078/files/560252/preview)

## Probability Distributions

Icon Progress Bar (browser only)

Now is your opportunity to see how much you can recall from the topic! Take a moment to answer the questions below. These are not graded, but they will allow you to check how much you are putting together the content in this lesson and review before moving to a new topic. 

When analyzing customer service response times, which probability distribution would be most appropriate?

Normal distribution
:   Incorrect. This is incorrect because response times typically have a right-skewed distribution (many quick responses, fewer very long ones) and cannot be negative. The normal distribution is symmetric and allows for negative values, making it inappropriate for response times.

Exponential distribution
:   **Correct.**Response times follow an exponential distribution because:

    * They can't be negative (you can't respond before a request arrives)
    * Most responses happen relatively quickly (creating a right-skewed pattern)
    * The probability of longer wait times gradually decreases
    * It's good for modeling "time until event" scenarios. The normal distribution wouldn't work well here because it's symmetric and allows for negative values. The uniform distribution would suggest all response times are equally likely, which isn't realistic in customer service scenarios.

Uniform distribution
:   Incorrect. This is incorrect because it assumes all values within a range are equally likely to occur. In customer service, very short response times are typically more common than very long ones, and the probability decreases as time increases, making a uniform distribution unsuitable.

[Check Answer](#)

A data scientist notices their data is always positive and highly skewed right (with a long tail). Which distribution would likely be most appropriate?

Normal distribution
:   Incorrect. This is incorrect because the normal distribution is symmetric around its mean and allows for negative values. Since this data is highly skewed right and only contains positive values, a normal distribution would be a poor fit.

Uniform distribution
:   Incorrect. This is incorrect because a uniform distribution assumes all values within a range are equally likely to occur. This doesn't match the described data which has a skewed shape with a long tail, meaning some values are much more likely than others.

Lognormal distribution
:   **Correct.**The lognormal distribution is ideal here because:

    * It only allows positive values
    * It naturally creates a right-skewed shape
    * It's good for data where multiplicative effects are at play
    * Common examples include income distributions or asset prices.
    * The normal distribution wouldn't work because it's symmetric and allows negative values.
    * The uniform distribution wouldn't capture the skewed nature of the data. The lognormal is often used for quantities that are the product of many small factors, like salaries or market prices.

[Check Answer](#)

A manufacturing company wants to understand their daily production output. Their quality control team notes that the number of defective items per day seems to occur randomly but at a consistent rate. Which probability distribution would best model this scenario?

Beta distribution
:   Incorrect. This is incorrect because the beta distribution is used for modeling probabilities or proportions between 0 and 1. It's not appropriate for counting discrete events like the number of defective items occurring in a time period.

Poisson distribution
:   **Correct.**

    The Poisson distribution is perfect for this scenario because:

    * It models the number of events (defects) occurring in a fixed interval (one day)
    * It works well when events happen independently of each other
    * It's specifically designed for counting discrete occurrences
    * It requires only one parameter: the average rate of occurrence
    * It's ideal for rare events that occur at a constant average rate

Normal distribution
:   Incorrect. This is incorrect because while the normal distribution can approximate count data in some cases, it's continuous and allows for negative values. The Poisson distribution is specifically designed for modeling the number of events occurring in a fixed time period at a constant rate, making it more appropriate for counting defective items.

[Check Answer](#)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248526

Scraped At: 2026-05-15T10:09:36.184300
