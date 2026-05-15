# What is Normal and Standard Normal Distribution?

# What is Normal and Standard Normal Distribution?

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) What is Normal and Standard Normal Distribution?

Icon Progress Bar (browser only)

9 min read

The **Normal Distribution** is a continuous probability distribution that describes how data is symmetrically spread out around a central value. This creates the famous "bell curve" shape.

Watch the video below to learn more about Normal and Standard Distribution.

[VIDEO LINK](https://player.vimeo.com/video/1060681675?badge=0&autopause=0&player\_id=0&app\_id=58479)

Let's break down the essential components:

### Mean (μ)

**Mean (μ)**: This is the center of the distribution – the peak of the bell curve. It represents the average or expected value.

*![two distributions differing in mean, same slope](https://moringa.instructure.com/courses/1426/files/631732/preview)*


*2 peaks of bell curve, representing the average or expected value*

### Standard Deviation (σ)

**Standard Deviation (σ):** This measures how spread out the values are from the mean. A larger standard deviation means the bell curve is wider and flatter, showing more variability. A smaller standard deviation creates a taller, narrower curve, indicating the values cluster more tightly around the mean.

![graph with 2 distributions differing in variance for standard deviation](https://moringa.instructure.com/courses/1426/files/631665/preview)

Graph with 2 distributions differing in variance for standard deviation.

### Standard Normal Deviation (Z Distribution)

The Standard Normal Distribution is **often referred to as the Z Distribution**. The Standard Normal Distribution is a special case of the Normal Distribution where:

* The mean is exactly 0.
* The standard deviation is exactly 1.

This standardized form is crucial because it allows us to compare different normal distributions on the same scale. Imagine converting all temperatures to Celsius – it gives us a standard way to discuss temperature regardless of whether someone usually thinks in Fahrenheit.

**Z-score:** When we convert a value from any Normal Distribution to its equivalent position in the Standard Normal Distribution, we get what's called a z-score.

The formula is:

 z = (x - μ) / σ

* x: original value
* μ: the mean
* σ: standard deviation

**Think of z-scores as a universal "how many standard deviations away from the mean" measure**. A z-score of 2 for a particular value means that the value is two standard deviations above the mean, regardless of the original scale.

*![graph of the standard normal distribution and z value](https://moringa.instructure.com/courses/1426/files/631672/preview)*


*Convert a value from any Normal Distribution to its equivalent position in the Standard Normal Distribution, for a z-score.*

### Distribution Properties

Properties that make these distributions special:

* **Symmetry:** The distribution is perfectly symmetric around the mean. Values equally far above and below the mean are just as likely.
* **The Empirical Rule:** In any Normal Distribution,
  + about 68% of values fall within one standard deviation of the mean.
  + about 95% fall within two standard deviations.
  + about 99.7% fall within three standard deviations.
* **Area Under the Curve:** The total area under any Normal Distribution curve equals 1, representing 100% of possible outcomes.

### How does Normal and Standard Normal Distribution work?

The Normal Distribution is fundamental in programming because it helps us model real-world phenomena and make statistical predictions. Think of it as a mathematical model that we can use to simulate and analyze natural variation in our data.

Let's walk through how we work with Normal Distributions in Python, starting with the basics and building up to more complex applications.

**Copy and run this code in a jupyter notebook to visualize concepts:**

```
import numpy as np  
import scipy.stats as stats  
import matplotlib.pyplot as plt  
  
def demonstrate_normal_distribution():  
    """  
    Demonstrates key concepts of Normal Distribution in programming contexts.  
    Shows generation, analysis, and visualization of normally distributed data.  
    """  
    # 1. Generating normally distributed data  
    # Generate 1000 samples with mean=100 and std=15  
    samples = np.random.normal(loc=100, scale=15, size=1000)  
      
    # 2. Analyzing the distribution  
    mean = np.mean(samples)  
    std = np.std(samples)  
      
    # 3. Calculate empirical rule boundaries  
    one_sigma = (mean - std, mean + std)  
    two_sigma = (mean - 2*std, mean + 2*std)  
    three_sigma = (mean - 3*std, mean + 3*std)  
      
    # 4. Calculate actual percentages within each boundary  
    within_one = np.mean(np.abs(samples - mean) <= std) * 100  
    within_two = np.mean(np.abs(samples - mean) <= 2 * std) * 100  
    within_three = np.mean(np.abs(samples - mean) <= 3 * std) * 100  
      
    # 5. Transform to standard normal (z-scores)  
    z_scores = stats.zscore(samples)  
      
    # 6. Calculate probabilities using cumulative distribution function (CDF)  
    # Example: Probability of value being less than mean + 1 std  
    prob_less_than_one_sigma = stats.norm.cdf(mean+std, loc=mean, scale=std)  
      
    # 7. Visualization  
    plt.figure(figsize=(12, 6))  
      
    # Create histogram of original data  
    plt.hist(samples, bins=30, density=True, alpha=0.7, color='skyblue')  
      
    # Add theoretical normal curve  
    x = np.linspace(mean - 4*std, mean + 4*std, 100)  
    plt.plot(x, stats.norm.pdf(x, mean, std), 'r-', lw=2,   
             label='Theoretical Normal')  
      
    # Add vertical lines for standard deviations  
    plt.axvline(mean, color='black', linestyle='--', label='Mean')  
    plt.axvline(one_sigma[0], color='green', linestyle=':')  
    plt.axvline(one_sigma[1], color='green', linestyle=':')  
      
    plt.title('Normal Distribution Analysis')  
    plt.xlabel('Value')  
    plt.ylabel('Density')  
    plt.legend()  
      
    return {  
        'mean': mean,  
        'std': std,  
        'within_one_sigma': within_one,  
        'within_two_sigma': within_two,  
        'within_three_sigma': within_three,  
        'prob_less_than_one_sigma': prob_less_than_one_sigma  
    }  
  
# Run the demonstration  
results = demonstrate_normal_distribution()  
  
# Print analysis results  
print(f"Distribution Analysis Results:")  
print(f"Mean: {results['mean']:.2f}")  
print(f"Standard Deviation: {results['std']:.2f}")  
print(f"Percentage within 1σ: {results['within_one_sigma']:.1f}%")  
print(f"Percentage within 2σ: {results['within_two_sigma']:.1f}%")  
print(f"Percentage within 3σ: {results['within_three_sigma']:.1f}%")  
print(f"Probability of value < μ + 1σ: {results['prob_less_than_one_sigma']:.3f}")
```

![Normally distributed data using random.normal() function](https://moringa.instructure.com/courses/1426/files/631709/preview)

We can create normally distributed data using NumPy's random.normal() function or SciPy’s stats.norm.rvs() function.

#### Normal Distribution Aspects

* Simulating real-world processes
* Testing statistical algorithms
* Creating sample data for modeling

#### Analysis Tools

Python's scientific libraries provide several ways to work with normal distributions:

* NumPy for basic statistical calculations
* SciPy for more advanced statistical functions
* Matplotlib for visualization

#### Power of Normal Distribution

* Model uncertainty and variation in data.
* Standardize different measurements for comparison.
* Make probabilistic predictions.
* Set reasonable bounds for quality control.
* Validate assumptions in statistical tests.

#### Key Operations-Standard Score Calculation (Z-score)

```
z_scores = (data - np.mean(data)) / np.std(data)  
# or using scipy  
z_scores = stats.zscore(data)
```

#### Key Operations- Probability Calculations

```
# Probability of value less than x  
probability = stats.norm.cdf(x, mean, std)  
  
# Probability between two values  
prob_between = stats.norm.cdf(x2, mean, std) - stats.norm.cdf(x1, mean, std)
```

### The Empirical Rule

The **Empirical Rule, also known as the 68-95-99.7 Rule or the Three-Sigma Rule is one of the most powerful and practical features of the Normal Distribution**. Think of the Empirical Rule as nature's way of organizing variation in a predictable pattern. It tells us exactly how data clusters around the mean in a Normal Distribution, working like a set of concentric rings, each capturing a specific percentage of all observations.

Let's break this down layer by layer:

#### First Layer (One Standard Deviation)

Imagine drawing lines one standard deviation above and below the mean. This central region captures approximately 68% of all observations. In practical terms, this means:

* If you're measuring adult male height with a mean of 5'10" and a standard deviation of 2 inches, about 68% of men will be between 5'8" and 6'0".
* In quality control, if you're manufacturing bolts with a target length of 10mm and a standard deviation of 0.1mm, roughly 68% will fall between 9.9mm and 10.1mm.

#### Second Layer (Two Standard Deviations)

When we expand our view to two standard deviations on either side of the mean we capture approximately 95% of all observations. This is particularly useful because:

* It forms the basis for many confidence intervals in statistics.
* It helps set practical quality control limits.
* It identifies what might be considered "unusual" (anything outside this range).

#### Third Layer (Three Standard Deviations)

At three standard deviations, we capture nearly all observations - 99.7%. This means:

* Only about 3 in 1000 observations fall outside this range.
* Values beyond this range are often considered statistical outliers.
* In quality control, these boundaries often represent specification limits.

 
![Graph with Data from Standard Deviation](https://moringa.instructure.com/courses/1426/files/631728/preview)

The real power of the Empirical Rule comes from its consistency. Whether you're looking at:

* Test scores in a classroom
* Manufacturing tolerances
* Financial returns
* Measurement error
* Natural phenomena

 The same percentages apply, making it a powerful tool for prediction and quality control across many fields.

### T-Distribution

Think of the t-distribution as the Normal Distribution's more cautious cousin. While they look similar, the **t-distribution accounts for the uncertainty that comes with small sample sizes and is particularly relevant for hypothesis testing**. Here's how they relate:

#### Shape and Properties

* Both distributions are symmetric and bell-shaped.
* The t-distribution has heavier "tails" than the Normal Distribution.
* As sample size increases, the t-distribution gets closer to the Normal Distribution.
* The t-distribution is defined by its degrees of freedom (df = sample size - 1).

#### When to Use Each

**Normal Distribution**

* You know the population standard deviation.
* You have a large sample size (n > 30).
* You're working with naturally normal data.

**t-Distribution**

* You don't know the population standard deviation.
* You have a small sample size (n < 30).
* You need to account for extra uncertainty.

#### Practical Differences

Let's say you're calculating a 95% confidence interval:

* Normal Distribution uses z ≈ 1.96.
* t-Distribution with df=9 uses t ≈ 2.262.
* This means t-distribution intervals are wider, reflecting greater uncertainty.

 
![2 graphs noting the differnce of slope between standard and z and t distribution](https://moringa.instructure.com/courses/1426/files/631592/preview)

The key takeaway is that the t-distribution provides a more conservative estimate when working with small samples. It's like adding a safety margin to account for the uncertainty that comes with limited data.

### Conceptualization of Normal and Standard Normal Distribution?

**Term**

**Definition**

**Example**

Normal Distribution

A continuous, symmetric probability distribution that forms a bell-shaped curve where data clusters around a central value and gradually spreads out to both sides. The total area under the curve equals 1.

If you measure the heights of 1000 adults, the measurements tend to cluster around an average height, with fewer people being very tall or very short.

Mean (μ)

The central value of the distribution that represents the peak of the bell curve and the average of all values. All other values are distributed symmetrically around this point.

In a manufacturing process producing bolts with target length 10mm, μ = 10mm is the intended center of all measurements.

Standard Deviation (σ)

A measure that quantifies how spread out values are from the mean. It determines the width of the bell curve and serves as a unit of measurement for variability.

If test scores have μ = 75 and σ = 5, then a score of 80 is one standard deviation above the mean.

Standard Normal Distribution

A specific version of the normal distribution where the mean is 0 and the standard deviation is 1. Used as a reference point for comparing different normal distributions.

Converting a test score of 80 (with μ = 75, σ = 5) to the standard normal gives a z-score of +1, meaning it's one standard deviation above average.

Z-Score

The number of standard deviations a value lies from the mean, calculated as (x - μ) / σ. Allows comparison of values from different normal distributions.

A student scoring 85 on a test with μ = 75 and σ = 5 has a z-score of +2, indicating they scored two standard deviations above average.

Empirical Rule

States that approximately 68% of data falls within ±1σ of the mean, 95% within ±2σ, and 99.7% within ±3σ.

For a manufacturing process with μ = 100mm and σ = 0.1mm: 68% of parts are between 99.9-100.1mm, 95% between 99.8-100.2mm, and 99.7% between 99.7-100.3mm.

t-Distribution

A probability distribution similar to the normal distribution but with heavier tails, used when sample sizes are small or population standard deviation is unknown.

When analyzing satisfaction scores from only 15 customers, the t-distribution provides wider confidence intervals than the normal distribution would, accounting for the uncertainty of the small sample.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248531

Scraped At: 2026-05-15T10:09:48.710637
