# Technical Lesson: Probability and Distributions

# Technical Lesson: Probability and Distributions

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Technical Lesson: Probability and Distributions

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In this lesson, you will demonstrate how Normal Distribution concepts directly apply to real-world business decisions in call center operations

Scenario

You need to analyze customer service call duration data to establish appropriate staffing levels and service standards. We'll follow our established process for working with Normal Distributions to analyze the data, make predictions, and set evidence-based performance targets.

The video below will guide you through each step of the Probability and Distributions Technical Lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Probability and Distributions.

[VIDEO LINK](https://player.vimeo.com/video/1060681061?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Tools and Resources

* [PythonLinks to an external site.](https://www.python.org/)(3.8 or higher)
* Required libraries: [NumPyLinks to an external site.](https://numpy.org/),[SciPyLinks to an external site.](https://scipy.org/),[MatplotlibLinks to an external site.](https://matplotlib.org/)

### Instructions

#### 1. Data Preparation and Validation

* Import required libraries, [NumPyLinks to an external site.](https://numpy.org/), [SciPyLinks to an external site.](https://scipy.org/), [Matplotlib.](https://matplotlib.org/)
* Create or load your call duration data.
* Verify normal distribution assumption using visual methods (histogram and Q-Q plot).

#### 2. Basic Statistical Analysis

* Calculate mean and standard deviation of call durations.
* These form the basis for all subsequent analysis.
* Mean represents typical call length.
* Standard deviation shows variability.

#### 3. Distribution Analysis

* Apply the Empirical Rule to understand data spread.
* Calculate actual percentages within 1, 2, and 3 standard deviations.
* Compare with expected percentages (68-95-99.7 rule).

#### 4. Service Level Agreement (SLA) Analysis

* Set target duration (e.g., 10 minutes).
* Calculate z-score for target.
* Determine probability of exceeding target.
* Use results to set realistic SLA targets.

#### 5. Staffing Implications

* Use mean duration to calculate service rate.
* Consider call volume (calls per hour).
* Calculate minimum staff needed based on target occupancy.

#### Full Code Solution

```
import numpy as np  
import scipy.stats as stats  
import matplotlib.pyplot as plt  
from scipy import stats  
  
def analyze_call_durations(call_data, target_duration=None):  
    """  
    Analyze call center duration data assuming normal distribution  
      
    Parameters:  
    call_data: array-like, call durations in minutes  
    target_duration: float, optional target duration for SLA  
    """  
      
    # Step 1: Verify Normal Distribution Appropriateness  
    # Create Q-Q plot to check normality  
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))  
      
    # Histogram with normal curve overlay  
    hist_data = ax1.hist(call_data, bins=30, density=True, alpha=0.7)  
    # Normal curve overlay  
xmin, xmax = ax1.get_xlim()  
    x = np.linspace(xmin, xmax, 100)  
    p = stats.norm.pdf(x, np.mean(call_data), np.std(call_data))  
    ax1.plot(x, p, 'k', linewidth=2)  
    ax1.set_title('Distribution of Call Durations')  
    ax1.set_xlabel('Duration (minutes)')  
    ax1.set_ylabel('Frequency')  
      
    # Q-Q plot  
    stats.probplot(call_data, dist="norm", plot=ax2)  
    ax2.set_title('Q-Q Plot of Call Durations')  
      
    # Step 2: Characterize the Distribution  
    mean_duration = np.mean(call_data)  
    std_duration = np.std(call_data)  
      
    # Step 3: Calculate Key Statistics  
    results = {  
        'mean': mean_duration,  
        'std': std_duration,  
        'within_1_std': np.mean(np.abs(call_data - mean) <= std),  
        'within_2_std': np.mean(np.abs(call_data - mean) <= 2 * std),  
        'within_3_std': np.mean(np.abs(call_data - mean) <= 3 * std)  
    }  
      
    # Step 4: Calculate SLA Probabilities if target provided  
    if target_duration is not None:  
        z_score = (target_duration - mean_duration) / std_duration  
        prob_within_target = 1 - stats.norm.cdf(z_score)  
        results['probability_exceed_target'] = prob_within_target  
      
    return results  
  
# Generate sample call data (normally distributed)  
np.random.seed(42)  # For reproducibility  
call_durations = np.random.normal(loc=8, scale=2, size=1000)  # Mean 8 mins, SD 2 mins  
  
# Analyze the data with a target SLA of 10 minutes  
results = analyze_call_durations(call_durations, target_duration=10)  
  
# Print results  
print("\nCall Center Analysis Results:")  
print(f"Mean call duration: {results['mean']:.2f} minutes")  
print(f"Standard deviation: {results['std']:.2f} minutes")  
print(f"\nEmpirical Rule Verification:")  
print(f"Percentage within 1 SD: {results['within_1_std']*100:.1f}% (expected ~68%)")  
print(f"Percentage within 2 SD: {results['within_2_std']*100:.1f}% (expected ~95%)")  
print(f"Percentage within 3 SD: {results['within_3_std']*100:.1f}% (expected ~99.7%)")  
print(f"\nProbability of call exceeding 10 minutes: {results['probability_exceed_target']*100:.1f}%")  
  
# Step 5  
# Calculate staffing implications  
def calculate_staffing_needs(mean_duration, calls_per_hour, target_occupancy=0.85):  
    """Calculate required staff based on Erlang C formula simplified"""  
    service_rate = 60 / mean_duration  # calls per hour per agent  
    minimum_agents = np.ceil(calls_per_hour / (service_rate * target_occupancy))  
    return int(minimum_agents)  
  
calls_per_hour = 30  # example  
staff_needed = calculate_staffing_needs(results['mean'], calls_per_hour)  
print(f"\nStaffing Recommendation:")  
print(f"Minimum agents needed for {calls_per_hour} calls per hour: {staff_needed}")
```

#### Report and Visualization

##### **Call Center Analysis Results**

* Mean call duration: 8.04 minutes
* Standard deviation: 1.96 minutes

##### **Empirical Rule Verification**

* Percentage within 1 SD: 68.6% (expected ~68%)
* Percentage within 2 SD: 95.6% (expected ~95%)
* Percentage within 3 SD: 99.7% (expected ~99.7%)

##### **Call-time Probability**

* Probability of call exceeding 10 minutes: 15.8%

##### **Staffing Recommendation**

* Minimum agents needed for 30 calls per hour: 5

*![2 graph visualization of Call Distributions and Plot of Call Durations](https://moringa.instructure.com/courses/1426/files/631717/preview)*


*Visualization of Call Distributions and Plot of Call Durations*

### Considerations

#### Common Issues

* **Non-normal data:** Check Q-Q plot for significant deviations.
* **Outliers:** Consider whether to exclude extremely long calls.
* **Seasonal variations:** May need separate analyses for different time periods.

#### Decision Points

* **Setting Target:**
  + **Too strict (< mean + 1 SD)**: High failure rate
  + **Too loose (> mean + 3 SD)**: Inefficient resource use
  + **Recommended**: mean + 2 SD for ~95% compliance

* **Staffing Levels:**
  + **Higher occupancy**: More efficient but higher stress
  + **Lower occupancy**: Better service but higher cost
  + **Recommended**: 85% target occupancy

* **Data Cleaning:**
  + **Include abandoned calls**: More realistic but skews distribution
  + **Exclude outliers**: Cleaner distribution but may miss important patterns
  + **Recommended**: Start inclusive, remove only clear errors

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248541

Scraped At: 2026-05-15T10:10:20.129721
