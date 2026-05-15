# Example of the Normal and Standard Normal Distribution

# Example of the Normal and Standard Normal Distribution

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Example of the Normal and Standard Normal Distribution

Icon Progress Bar (browser only)

3 min read

Imagine you've just started as a junior data analyst at a company that manufactures smartphone screens. Your first assignment is to help the quality control team analyze their production process.

The Scenario

Your team produces touchscreen displays with a target thickness of 0.5mm. Customer specifications allow for a small variation in thickness, but screens that are too thick won't fit in the phone housing, and screens that are too thin might break easily.

Let's analyze this real-world situation step by step:

### Initial Data Analysis

Understanding how the Normal Distribution applies will help:

* Set quality control limits
* Predict defect rates
* Make recommendations for process improvements

```
import numpy as np  
import scipy.stats as stats  
import matplotlib.pyplot as plt  
  
# Sample measurements from the production line (500 screens)  
measurements = np.random.normal(loc=0.5, scale=0.02, size=500)  
  
# Calculate basic statistics  
mean_thickness = np.mean(measurements)  
std_thickness = np.std(measurements)  
  
print(f"Mean thickness: {mean_thickness:.3f}mm")  
print(f"Standard deviation: {std_thickness:.3f}mm")
```

#### Output

* **Mean thickness:** 0.499mm
* **Standard deviation**: 0.020mm

### Quality Control Limits Using the Empirical Rule

```
# Calculate boundaries using the 68-95-99.7 rule  
one_sigma = (mean_thickness - std_thickness, mean_thickness + std_thickness)  
two_sigma = (mean_thickness - 2*std_thickness, mean_thickness + 2*std_thickness)  
three_sigma = (mean_thickness - 3*std_thickness, mean_thickness + 3*std_thickness)  
  
print("\nQuality Control Boundaries:")  
print(f"68% of screens between: {one_sigma[0]:.3f}mm and {one_sigma[1]:.3f}mm")  
print(f"95% of screens between: {two_sigma[0]:.3f}mm and {two_sigma[1]:.3f}mm")  
print(f"99.7% of screens between: {three_sigma[0]:.3f}mm and {three_sigma[1]:.3f}mm")
```

#### Quality Control Boundaries Output

* 68% of screens between: 0.479mm and 0.519mm
* 95% of screens between: 0.459mm and 0.540mm
* 99.7% of screens between: 0.438mm and 0.560mm

### Process Capability Analysis

Your team needs to know if the current process can meet customer specifications. The customer requires screens between 0.45mm and 0.55mm.

```
def analyze_process_capability(data, lower_spec, upper_spec):  
    # Convert measurements to z-scores relative to specifications  
    mean = np.mean(data)  
    std = np.std(data)  
      
    z_lower = (lower_spec - mean) / std  
    z_upper = (upper_spec - mean) / std  
      
    # Calculate probability of defects  
    prob_below = stats.norm.cdf(z_lower)  
    prob_above = 1 - stats.norm.cdf(z_upper)  
    total_defect_rate = (prob_below + prob_above) * 100  
      
    return total_defect_rate  
  
defect_rate = analyze_process_capability(  
    measurements,   
    lower_spec=0.45,   
    upper_spec=0.55  
)  
  
print(f"\nPredicted defect rate: {defect_rate:.2f}%")
```

#### Output

* Predicted defect rate: 1.35%

### Using the t-Distribution for Small Batch Analysis

Sometimes you need to analyze small batches of screens from new production runs:

```
def analyze_small_batch(measurements, confidence=0.95):  
    n = len(measurements)  
    mean = np.mean(measurements)  
    std_error = stats.sem(measurements)  
      
    # Use t-distribution for small sample  
    confidence_interval = stats.t.interval(  
        confidence,   
        df=n-1,   
        loc=mean,   
        scale=std_error  
    )  
      
    return confidence_interval  
  
# Analyze a small batch of 10 screens  
small_batch = measurements[:10]  
ci = analyze_small_batch(small_batch)  
print(f"\nSmall Batch Analysis:")  
print(f"95% Confidence Interval: {ci[0]:.3f}mm to {ci[1]:.3f}mm")
```

### Analysis Summary

**Real-World Impact:** Based on this analysis, you might recommend:

1. **If the defect rate is too high,** suggest adjusting the machine settings to center the process better.
2. **If the variation (standard deviation) is too large**, investigate factors causing inconsistency.
3. Use the t-distribution confidence intervals when testing new process adjustments with small samples.

**Writing Your Report:**

"Based on our analysis of 1000 screen measurements, our process is centered at 0.5mm with a standard deviation of 0.02mm. Using the Empirical Rule, we expect:

* 68% of screens to fall between 0.48mm and 0.52mm
* 95% of screens to fall between 0.46mm and 0.54mm
* 99.7% of screens to fall between 0.44mm and 0.56mm

Our current predicted defect rate is [X]%, which could be improved by [your recommendations]."

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248533

Scraped At: 2026-05-15T10:09:55.157091
