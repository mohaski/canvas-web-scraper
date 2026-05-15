# How does Probability Distributions work?

# How does Probability Distributions work?

## ![](https://moringa.instructure.com/courses/1426/files/631696/preview) How do Probability Distributions work?

Icon Progress Bar (browser only)

11 min read

A **statistical distribution** is a representation of the frequencies of potential events or the percentage of time each event occurs.

This may feel pretty vague, so let's use two examples to clarify:

* [Rolling a Dice Distribution](#dpPanel0Content)
* [Weather Distribution](#dpPanel1Content)

### Rolling a Dice Distribution

Let's return to the example of rolling a dice. You know that when rolling dice once, you will obtain a number between 1 and 6. Each number has the same chance of occurring, as denoted in this table:

Distribution of Dice Roll

| Outcome | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Probability | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 |

You can also represent this graphically as a probability distribution using the probability mass function as follows:

[![graph of equal probability of dice rolls for 6 numbers .16](https://moringa.instructure.com/courses/1426/files/631646/preview)](https://moringa.instructure.com/courses/1426/files/631646/preview "Graph noting the of equal probability of dice rolls for 6 numbers, .16")


*Graph noting the of equal probability of dice rolls for 6 numbers, .16*

**Note how**, with a fair die, the chance of throwing each number is exactly 1/6 (or 0.1666). The number of outcomes is finite and the outcome is a set of values. In this case, you are dealing with a **discrete distribution**. Think of it as a histogram but instead of showing counts it shows probabilities.

### Weather Distribution

Let's look at another situation. Let's think about the distribution of the temperature in New York on June 1st. You could say that the temperature would generally range between 65 and 95 Degrees (more extreme values would be exceptional), with the average around 80 Degrees Fahrenheit.

A potential distribution looks like this:

[![pdf temperatures in June 1, continuous distribution 80 degrees, of 80.5 degrees, of 80.0034 degrees, etc.](https://moringa.instructure.com/courses/1426/files/631734/preview)](https://moringa.instructure.com/courses/1426/files/631734/preview "Our distribution is a continuous distribution because temperature is a continuous value.")


Our distribution is a continuous distribution because temperature is a continuous value.

Instead of bars, which we had for the dice example, we have continuous lines here. Our distribution is a continuous distribution because temperature is a **continuous value** (we can have a temperature of 80 degrees, of 80.5 degrees, of 80.0034 degrees, etc.).

### Discrete vs Continuous Distributions

When dealing with **discrete** data you use a **Probability Mass Function (PMF)** (as in our dice example). When dealing with **continuous** data, you use a **Probability Density Function (PDF)** (see our weather example).

Based on the variation of their attributes, data distributions can take many shapes and forms. Very often, distributions are described using their statistical mean (or **expected value**) and variance of the data, but this is not always the case. You'll see more on this in the next few sections.

In the following image, you can see the general shapes of some common distributions. 

[![common distributions shapes in graph format](https://moringa.instructure.com/courses/1426/files/631619/preview)](https://moringa.instructure.com/courses/1426/files/631619/preview "The horizontal axis in each chart represents the set of possible numeric outcomes. The vertical axis describes the probability of the respective outcomes. Note the range of common distributions shapes in graph format")


The horizontal axis in each chart represents the set of possible numeric outcomes. The vertical axis describes the probability of the respective outcomes. Note the range of common distributions shapes in graph format

#### How to Describe Distributions: Center, Spread and Shape

To fully understand a dataset, it’s essential to look beyond just individual values and consider how the values are distributed. We describe distributions using three key characteristics, **center**, **spread**, and **shape**, each offering unique insight into the data’s overall pattern and variability.

* **Center** refers loosely to the middle values of a distribution and is measured more precisely by the mean, median, and mode.
* **Spread** refers loosely to how much the data varies or how far values are from the center. It helps you understand whether the data is tightly clustered or widely scattered and is measured by range and interquartile range; it is more precisely measured by the standard deviation, which shows how far, on average, each value is from the mean.
* **Shape** refers loosely how the data shows up when visualized graphically. It can help you identify patterns, including symmetry (both sides of distribution mirror each other) or skew (whether the data is pull more to one side), as well as the number of peaks (high points) in the distribution.

#### Center and Spread of Probability Distribution

[![probability distribution graph with 3 curves, mean, narrow distribution, and broad distribution](https://moringa.instructure.com/courses/1426/files/631601/preview)](https://moringa.instructure.com/courses/1426/files/631601/preview "Images sourced from Emory Department of Mathematics and Computer Science")


Images sourced from Emory Department of Mathematics and Computer Science

* A narrow distribution (red) has low spread, meaning data points are tightly clustered around the mean.
* A broad distribution (green) has high spread, meaning data points vary widely from the mean.
* Despite different spreads, all three distributions have the same center (mean).

#### Shape and Spread of Probability Distribution

[![3 graphs noting probability distribution with mean median and mode, are reversed, and not reversed ](https://moringa.instructure.com/courses/1426/files/631603/preview)](https://moringa.instructure.com/courses/1426/files/631603/preview "Images sourced from Emory Department of Mathematics and Computer Science")


Images sourced from Emory Department of Mathematics and Computer Science

* **Left Graph (Right-Skewed)**: The distribution has a long right tail (**right-skewed shape**) with a wider spread on the higher values.
* **Middle Graph (Symmetric/Normal)**: The distribution is **bell-shaped and symmetric**, with an even spread on both sides of the center.
* **Right Graph (Left-Skewed)**: The distribution has a long left tail (**left-skewed shape**) with a wider spread on the lower values.

### Examples of Discrete Distributions

To give you an initial idea of some applications, we'll give you a quick overview of discrete and continuous distributions. 

* [The Bernoulli Distribution](#dpPanel2Content)
* [The Binomial Distribution](#dpPanel3Content)
* [The Poisson Distribution](#dpPanel4Content)
* [The Uniform Distribution](#dpPanel5Content)

### The Bernoulli Distribution

The Bernoulli distribution represents the **probability of success** for a certain experiment (the outcome being "success or not", so there are two possible outcomes).

**Example:** A coin toss is a classic example of a Bernoulli experiment with a probability of success 0.5 or 50%, but a Bernoulli experiment can have any probability of success between 0 and 1.

### The Binomial Distribution

Binomial distribution represents the **probability of observing a specific number of successes** (Bernoulli trials) in a specific number of trials.

**Example:** The number of defects found from a 100-random sample from the production line.

#### The Poisson Distribution

The Poisson distribution represents the **probability of *n* events in a given time period when the overall rate of occurrence is constant.**

**Example:** A typical example is pieces of mail. If your overall mail received is constant, the number of items received on a single day (or month) follows a Poisson distribution. Other examples might include visitors to a website, or customers arriving at a store, or clients waiting to be served in a queue.

### The Uniform Distribution

The uniform distribution occurs when **all possible outcomes are equally likely**.

**Example:** The dice example shown before follows a uniform distribution with equal probabilities for throwing values from 1 to 6. The dice example follows a discrete uniform distribution, but continuous uniform distributions exist as well.

### Examples of Continuous Distributions

* [The Normal or Gaussian Distribution](#dpPanel6Content)
* [The Chi-squared Distribution](#dpPanel7Content)
* [The F-Distribution](#dpPanel8Content)

### The Normal or Gaussian Distribution

A normal distribution is the single most important distribution, and you'll come across it in many aspects of life. The normal distribution **follows a bell shape and is a foundational distribution for many models and theories** in statistics and data science.

**Example:** A normal distribution turns up very often when dealing with real-world data including heights, weights of different people, errors in some measurement or grades on a test. Our previous temperature example follows a normal distribution as well!

#### The Chi-squared Distribution

Think of the chi-squared distribution as a way to measure how different our observed data is from what we expected, when dealing with frequency or proportion data. The shape of a chi-squared distribution depends on its "degrees of freedom", a number that relates to how many independent pieces of information we're working with.

Unlike the symmetrical bell shape of the normal distribution, the **chi-squared distribution is always positive and often appears skewed to the right**, looking somewhat like a mountain with a long tail stretching to the right.

### The F-Distribution

While the normal distribution helps us understand single measurements and chi-squared distributions help us understand variance, the **F-distribution helps us compare variances between different groups**. It's named after the statistician Sir Ronald Fisher, who developed it.

You might use the F-distribution when you're comparing the performance of different machine learning models, or when you're trying to determine if different groups in your data (like users from different countries) show significantly different patterns of behavior.

It's particularly useful in A/B testing scenarios where you want to compare the variability between different test groups.

Like the chi-squared distribution, **the F-distribution is always positive and tends to be right-skewed, but it's shaped by two parameters: degrees of freedom for both numerator and denominator**. Think of it as comparing two chi-squared distributions at once.

### Probability Functions

Think of probability functions as mathematical tools that help us measure and predict uncertainty. There are **four key types of probability functions that work together**, each serving a different purpose in understanding random events:

#### [Probability Mass Function (PMF)](#dpPanel9)

This function **handles discrete events, or things we can count**.

**Example:**

Imagine you're tracking the number of support tickets a software company receives per hour. The PMF would tell you the exact probability of receiving 0, 1, 2, or any specific number of tickets.

Let's see this in code:

```
from scipy import stats  
import numpy as np  
  
# Let's model support tickets per hour using a Poisson distribution  
lambda_rate = 5  # Average 5 tickets per hour  
  
# Calculate probability of exactly k tickets in an hour  
def ticket_probability(k):  
    return stats.poisson.pmf(k, lambda_rate)  
  
# Probability of exactly 3 tickets  
print(f"Probability of exactly 3 tickets: {ticket_probability(3):.3f}")
```

**Output:** Probability of exactly 3 tickets: 0.140

#### [Probability Density Function (PDF)](#dpPanel10)

The **PDF handles continuous values, or measurements that can take any value within a range**, like response times or download speeds. Unlike the PMF, which gives exact probabilities, the PDF gives us relative likelihood.

Here's how we might use it:

```
from scipy import stats  
  
# Model response times using a normal distribution  
mean_response = 100  # milliseconds  
std_dev = 15  
  
# Calculate relative likelihood of different response times  
def response_likelihood(x):  
    return stats.norm.pdf(x, mean_response, std_dev)  
  
# Compare likelihood of different response times  
print(f"Likelihood at 100ms: {response_likelihood(100):.4f}")  
print(f"Likelihood at 130ms: {response_likelihood(130):.4f}")
```

**Output:**

* Likelihood at 100ms: 0.0266
* Likelihood at 130ms: 0.0036

#### [Cumulative Distribution Function (CDF)](#dpPanel11)

The CDF tells us the **probability of a value being less than or equal to a specific point**. It's particularly useful for setting thresholds and service level agreements.

Here's how we might use it:

```
from scipy import stats  
  
# Model response times using a normal distribution  
mean_response = 100  # milliseconds  
std_dev = 15  
  
# Calculate probability of response time being under a threshold  
def probability_under_threshold(threshold):  
    return stats.norm.cdf(threshold, mean_response, std_dev)  
  
# Probability of response time under 120ms  
print(f"Probability of response < 120ms: {probability_under_threshold(120):.3f}")
```

**Output:** Probability of response < 120ms: 0.909

#### [Quantile Function or Point Percentile Function (Inverse CDF/PPF)](#dpPanel12)

This function works backwards from the CDF: **given a probability, it tells us the corresponding value**. This is invaluable for capacity planning and setting performance targets.

In code:

```
from scipy import stats  
  
# Model response times using a normal distribution  
mean_response = 100  # milliseconds  
std_dev = 15  
  
# Find the response time threshold for a given percentile  
def find_response_threshold(percentile):  
    return stats.norm.ppf(percentile, mean_response, std_dev)  
  
# Find 95th percentile response time  
print(f"95th percentile response time: {find_response_threshold(0.95):.1f}ms")
```

**Output:**

* 95th percentile response time: 124.7ms
* -95% of all response times are 124.7ms or less

#### [Relating These Functions](#dpPanel13)

The key to understanding these functions is seeing how they relate:

* The **PDF/PMF** tells us about likelihood at specific points
* The **CDF** accumulates these probabilities to tell us about ranges
* The **Quantile Function** helps us work backwards from probabilities to values

In practice, we often use these functions together:

* The **PDF/PMF** tells us about likelihood at specific points
* The **CDF** accumulates these probabilities to tell us about ranges
* The **Quantile Function** helps us work backwards from probabilities to values

### Conceptualization of Probability Distributions

**Distribution Type**

**Definition**

**Real-World Example**

**Key Uses**

Normal (Gaussian)

A symmetric, bell-shaped distribution centered around a mean value, with values more likely to occur near the mean and less likely as they get farther away.

Heights of people in a population, measurement errors in scientific experiments, test scores in a large class.

Performance metrics, natural phenomena, aggregated random variables, quality control measurements

Exponential

Describes the time between events in a process where events occur continuously and independently at a constant average rate.

Time between customer arrivals at a store, duration between system failures, length of phone calls.

Service times, wait times, lifetime analysis, failure prediction

Poisson

Models the number of events occurring within a fixed interval of time or space, assuming events occur independently.

Number of visitors to a website per hour, defects per unit area, bugs found per code review.

Event counting, rare event modeling, quality control, traffic analysis

Uniform

Every value within a specified range has an equal probability of occurring.

Random number generation, simulation of dice rolls, random sampling from a range.

Random selection, simulation baselines, testing scenarios, A/B test assignment

Binomial

Models the number of successes in a fixed number of independent yes/no trials.

Number of successful email deliveries out of total sent, conversion counts in A/B tests.

Success/failure scenarios, conversion analysis, quality testing

Chi-squared

Measures how much observed values deviate from expected values. Used heavily in hypothesis testing.

Testing independence of variables, validating model fit, feature selection in machine learning.

Goodness-of-fit tests, independence tests, variance analysis

F-distribution

Used to compare variances between different groups or populations.

Comparing variability between different machine learning models, ANOVA tests.

Variance comparisons, ANOVA, model selection, feature importance testing

Beta

Models probabilities or proportions between 0 and 1, often used in Bayesian statistics.

Click-through rates, conversion rates, probability estimation.

Rate modeling, probability estimation, Bayesian updating

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248518

Scraped At: 2026-05-15T10:09:11.296292
