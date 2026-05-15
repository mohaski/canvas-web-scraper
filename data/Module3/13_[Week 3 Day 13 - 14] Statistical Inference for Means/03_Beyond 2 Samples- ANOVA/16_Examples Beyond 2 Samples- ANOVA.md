# Examples: Beyond 2 Samples- ANOVA

# Examples: Beyond 2 Samples- ANOVA

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Example: Beyond 2 Samples- ANOVA

Icon Progress Bar (browser only)

2 min read

Scenario: Mobile App Navigation Analysis

Imagine you've joined the analytics team at a popular fitness app company. The UX team has been experimenting with four different navigation layouts, and they need to know if these designs affect how long users spend finding specific features in the app. They've conducted a usability study with 40 participants (10 per design), measuring the time (in seconds) it takes users to find and start a new workout.

Let's analyze this data:

```
import numpy as np  
from scipy import stats  
from statsmodels.stats.multicomp import pairwise_tukeyhsd  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
# Time (in seconds) for users to find and start a workout  
design_A = np.array([15, 17, 14, 16, 15, 18, 16, 14, 17, 15])  # Traditional menu  
design_B = np.array([12, 13, 11, 14, 12, 13, 12, 11, 13, 12])  # Tab bar  
design_C = np.array([19, 21, 18, 20, 19, 22, 20, 18, 21, 19])  # Hamburger menu  
design_D = np.array([16, 18, 15, 17, 16, 19, 17, 15, 18, 16])  # Gesture-based  
  
# First, let's visualize our data  
plt.figure(figsize=(10, 6))  
sns.boxplot(data=[design_A, design_B, design_C, design_D])  
plt.xticks([0, 1, 2, 3], ['Traditional', 'Tab Bar', 'Hamburger', 'Gesture'])  
plt.ylabel('Time to Start Workout (seconds)')  
plt.title('Navigation Design Performance')  
  
# Perform one-way ANOVA  
f_statistic, p_value = stats.f_oneway(design_A, design_B, design_C, design_D)  
print(f"fstat: {f_statistic}, pvalue: {p_value})  
  
# If we find significant differences, perform post-hoc analysis  
all_data = np.concatenate([design_A, design_B, design_C, design_D])  
design_labels = np.repeat(['Traditional', 'Tab Bar', 'Hamburger', 'Gesture'], 10)  
  
tukey = pairwise_tukeyhsd(all_data, design_labels)  
tukey.summary()
```

 
![Table of results for multiple comparison of means](https://moringa.instructure.com/courses/1426/files/631755/preview)

![Histogram of navigation layouts for design performance](https://moringa.instructure.com/courses/1426/files/631743/preview)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248682

Scraped At: 2026-05-15T10:19:53.897630
