# Example of Probability Distributions

# Example of Probability Distributions

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Example of Probability

Icon Progress Bar (browser only)

4 min read

### Scenario: Student Homework Analysis

Imagine you're a junior data scientist working at an online learning platform. A teacher comes to you with a question: "I want to understand how long my students typically spend on homework assignments. This will help me design better assignments and give students realistic expectations."

This is much more useful than just knowing the average time, because it helps us understand the full range of student experiences. The power of using probability distributions here is that they help us:

* Describe typical behavior
* Account for natural variation
* Make predictions about future students
* Set realistic expectations

 The following code models a realistic homework scenario:

```
from scipy import stats  
import matplotlib.pyplot as plt  
  
# Generate homework completion times (in minutes)  
# We'll use lognormal since time spent often has a longer right tail   
# (some students take much longer than others)  
homework_times = stats.lognorm.rvs(s=0.5, scale=30, size=100)  
  
# First, let's understand what completion times are typical  
print("Understanding Homework Times:")  
print(f"Average completion time: {stats.tmean(homework_times):.1f} minutes")  
  
# Let's find how long we should tell students the homework will take  
# We'll use percentiles to give a realistic range  
time_ranges = stats.scoreatpercentile(homework_times, [25, 50, 75])  
print("\nTypical Time Ranges:")  
print(f"Quick students finish in: {time_ranges[0]:.1f} minutes")  
print(f"Typical students take: {time_ranges[1]:.1f} minutes")  
print(f"Slower students need: {time_ranges[2]:.1f} minutes")  
  
# What if we want to know the probability a student will finish in under 45 minutes?  
# We can fit a distribution to our data and use it to calculate this  
shape, loc, scale = stats.lognorm.fit(homework_times)  
prob_under_45 = stats.lognorm.cdf(45, shape, loc, scale)  
print(f"\nProbability of finishing under 45 minutes: {prob_under_45:.1%}")  
  
# Visualize the distribution of homework times  
plt.figure(figsize=(10, 6))  
plt.hist(homework_times, bins=20, density=True, alpha=0.7,   
         label='Actual Times')  
  
# Add markers for typical ranges  
for time in time_ranges:  
    plt.axvline(time, color='red', linestyle='--', alpha=0.5)  
  
plt.title('Distribution of Homework Completion Times')  
plt.xlabel('Time (minutes)')  
plt.ylabel('Density')  
plt.legend()
```

### Example Explanation

The code is modeling a realistic homework scenario where:

* Most students complete the work around 30 minutes (the scale parameter).
* There's some variation but not extreme (s=0.5 keeps it reasonable).
* A few students take longer (the natural right skew of log-normal captures this).

The parameters used in `stats.lognorm.rvs(s=.5, scale=30, size=100)`:

#### S Parameter

The parameter`s` (which is sigma or shape parameter) = 0.5 controls the shape of the log-normal distribution:

* A smaller s (like 0.5) creates a distribution that's less skewed and more concentrated
* A larger s would create a more spread out, heavily right-skewed distribution
* 0.5 was likely chosen here because homework completion times typically have some variation but aren't extremely spread out

#### Scale Parameter

The `scale` parameter = 30 determines the median of the distribution:

* In a log-normal distribution, scale is the median when you take e^(scale).
* 30 minutes represents a reasonable median time for homework completion.
* This means about half the students would finish before 30 minutes and half after

#### Size Parameter

The size parameter = 100 determines how many random variables are created for our sample data

*[![Graph of data for understanding homework time](https://moringa.instructure.com/courses/1426/files/631685/preview)](https://moringa.instructure.com/courses/1426/files/631685/preview "Graph distribution of data for understanding homework completion times. ")*


*Graph distribution of data for understanding homework completion times.*

### Summary

This analysis helps the teacher in several practical ways:

1. **Setting Expectations** Instead of just saying "this should take 30 minutes," we can give students a more realistic range: "Most students complete this in 20-40 minutes, but some may need up to an hour."
2. **Planning Assignments** If the teacher sees that typical completion times are longer than expected, they might need to adjust the assignment length or break it into smaller parts.
3. **Identifying Struggles Understanding** the typical range helps spot when a student might be struggling unusually with the material (taking much longer than the typical range).

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248520

Scraped At: 2026-05-15T10:09:18.057628
