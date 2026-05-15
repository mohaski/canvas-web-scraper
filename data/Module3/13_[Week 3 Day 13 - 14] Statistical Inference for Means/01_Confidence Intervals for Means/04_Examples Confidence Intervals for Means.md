# Examples: Confidence Intervals for Means

# Examples: Confidence Intervals for Means

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Example: Confidence Intervals for Means

Icon Progress Bar (browser only)

5 min read

Imagine you've just joined a streaming service as a junior data analyst. Your manager asks you to analyze video buffering times to ensure users are having a good experience. You can't measure every single video play (that would be your population), so you need to work with a sample and use confidence intervals to draw reliable conclusions.

Let's say you collect buffering times from 100 video plays (your sample) and find:

* Sample mean buffering time: 2.4 seconds
* Sample standard deviation: 0.6 seconds
* You want 95% confidence in your results

**Building Your Confidence Interval:** Think of building a confidence interval like creating a safety margin around your best estimate. Just as an architect doesn't design a bridge to hold exactly the expected weight but adds a safety margin, we add a margin of error around our sample mean.

Here's how the pieces fit together:

1. Your Best Estimate (Sample Mean): The sample mean of 2.4 seconds is like your "best guess" at the true average buffering time. It's your starting point, but you know it's probably not exactly right.
2. Understanding Uncertainty (Standard Error): The standard error tells you how much you expect sample means to bounce around. With your sample standard deviation of 0.6 seconds and sample size of 100, your standard error would be 0.06 seconds (0.6/√100). This is like knowing how steady your hand is when taking a measurement.
3. Setting Your Confidence Level (Critical Value): Choosing 95% confidence means you want to be right 95% of the time. This translates to a critical value of about 1.96 from the normal distribution. Think of this as deciding how wide to make your safety margin.
4. Calculating Your Margin of Error: Multiply your standard error by your critical value: 0.06 \* 1.96 = 0.12 seconds. This is like setting the "plus or minus" range around your estimate.

Your Final Interval: 2.4 ± 0.12 seconds, or [2.28, 2.52] seconds

### Code

```
import numpy as np  
from scipy import stats  
import matplotlib.pyplot as plt  
  
# Simulate 100 buffering times with mean 2.4 seconds and std dev 0.6 seconds  
# In reality, this would be your actual collected data  
np.random.seed(42)  # For reproducibility  
buffering_times = np.random.normal(loc=2.4, scale=0.6, size=100)  
  
# Calculate the basics  
sample_mean = np.mean(buffering_times)  
sample_std = np.std(buffering_times, ddof=1)  # ddof=1 for sample standard deviation  
sample_size = len(buffering_times)  
  
# Calculate 95% confidence interval using scipy.stats  
# The interval function handles all the t-distribution calculations for us  
confidence_level = 0.95  
ci = stats.t.interval(confidence_level,  
                     df=sample_size-1,  # Degrees of freedom  
                     loc=sample_mean,    # Center point (sample mean)  
                     scale=stats.sem(buffering_times))  # Standard error  
  
print(f"Sample Mean: {sample_mean:.2f} seconds")  
print(f"95% Confidence Interval: [{ci[0]:.2f}, {ci[1]:.2f}] seconds")  
  
# Let's visualize this to make it more intuitive  
plt.figure(figsize=(10, 6))  
  
# Plot the individual data points  
plt.plot(buffering_times, np.zeros_like(buffering_times), 'b.', alpha=0.2,  
         label='Individual measurements')  
  
# Plot the mean and confidence interval  
plt.vlines(sample_mean, -0.1, 0.1, colors='red', label='Sample mean')  
plt.hlines(0, ci[0], ci[1], colors='black', linewidth=2,  
          label='95% Confidence Interval')  
  
# Add labels and formatting  
plt.xlabel('Buffering Time (seconds)')  
plt.title('Video Buffering Times with 95% Confidence Interval')  
plt.legend()  
  
# Remove y-axis as it's not meaningful in this visualization  
plt.gca().get_yaxis().set_visible(False)  
  
plt.grid(True, axis='x')  
plt.show()
```

### Output

Sample Mean: 2.34 seconds  
95% Confidence Interval: [2.23, 2.45] seconds

![vgraph of video buffering time with 95% confidence interval](https://moringa.instructure.com/courses/1426/files/631632/preview)

#### Communicating the Solution

Now comes the important part - interpreting this for your manager:

"Based on our sample, we estimate that the true average buffering time for all video plays is between 2.28 and 2.52 seconds, and we're 95% confident in this range. This means:

* We're reasonably sure the true average lies in this range
* We're precise enough to detect changes of about 0.12 seconds
* If our buffering target is 3 seconds, we're comfortably meeting it
* If our target is 2 seconds, we need to improve our system"

**Factors Affecting Your Interval:**

1. Sample Size: If you had taken 400 samples instead of 100, your interval would be half as wide. This is like having a more precise measuring tool.
2. Variability: If buffering times were more consistent (smaller standard deviation), your interval would be narrower. This is like having more stable conditions for measurement.
3. Confidence Level: If you needed 99% confidence instead of 95%, your interval would be wider. This is like adding an extra safety margin.

**Understanding confidence intervals this way helps you:**

* Make informed decisions about how much data to collect
* Communicate uncertainty to stakeholders
* Set realistic performance targets
* Monitor system changes effectively

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248656

Scraped At: 2026-05-15T10:17:47.043429
