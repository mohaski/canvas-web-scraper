# Technical Lesson: Experimental Design and Statistical Testing

# Technical Lesson: Experimental Design and Statistical Testing

## ![](https://moringa.instructure.com/courses/1426/files/631704/preview) Technical Lesson: Experimental Design and Statistical Testing

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:  1 hour**

In this lesson you will use a problem solving process for experimental design and statistical testing. This walkthrough emphasizes proper setup and planning, which are crucial for valid hypothesis testing. The focus is on making and documenting clear decisions before any data analysis begins, ensuring a rigorous and defensible process.

### Scenario: Mobile App Performance Analysis

You're a data scientist at a mobile gaming company. The engineering team has developed a new content loading system they believe reduces app startup time. Before rolling this out to all users, you need to determine if the new system actually improves performance. Current load times have a known population mean of 2000ms with a standard deviation of 400ms.

### Video: Experimental Design and Statistical Testing

The video below will guide you through each step of the Experimental Design and Statistical Testing. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Experimental Design and Statistical Testing.

[VIDEO LINK](https://player.vimeo.com/video/1060682094?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

* [Step 1: Define Your Research Question](#dpPanel0Content)
* [Step 2: Experimental Framework](#dpPanel1Content)
* [Step 3: Determine the Decision Criteria](#dpPanel2Content)
* [Step 4: Collect and Explore Data](#dpPanel3Content)
* [Step 5: Analyze and Interpret](#dpPanel4Content)

#### Step 1: Define Your Research Question

**Research Question Documentation:** "Does the new content loading system significantly reduce the average app startup time compared to our current system?"

Key Components Defined:

* **Change:** New content loading system
* **Metric:** App startup time (measured in milliseconds)
* **Population:** Active app users
* **Direction:** Looking for a reduction in time (less than)

**Formulate Hypotheses:** Since we specifically want to test for improvement (reduction in time), this calls for a one-sided test.

* H₀ (null): μnew >= μcurrent (New system is not faster than current system)
* H₁ (alternative): μnew < μcurrent (New system is faster than current system)

#### Step 2: Experimental Framework

Now that we have the initial questions of our experimental test down we **need to consider possible variables that will need to be controlled for** in order to ensure our samples of users for both groups (new system versus current) are representative and non-biased.

* The users device type might have an effect on start-up times
  + Stratified sampling of users based on device type
* The app version might also have an effect
  + Only include users with the latest version in our experiment

The following is a **very general look at what data might be crucial to collect and monitor for this experiment.** We are not going to cover the actual data collection process here but note the basic python dictionary format that will allow us easy access to specific data. From there it is possible to create a DataFrame to store information or maybe even a SQL database.

```
import pandas as pd  
from datetime import datetime, timedelta  
  
# Define data collection parameters  
collection_plan = {  
    'metrics': ['startup_time_ms', 'device_type', 'app_version', 'network_type'],  
    'start_date': datetime.now(),  
    'duration_days': 14,  
    'control_variables': ['app_version', 'network_type'],  
    'exclusion_criteria': ['startup_time_ms > 10000', 'network_type == "offline"']  
}  
  
# Stratify Sampling  
def analyze_device_distribution(data_df):  
    """  
    Analyzes the current distribution of device types in our user base  
    Returns the proportion of each device type  
    """  
    device_counts = data_df['device_type'].value_counts()  
    total_users = len(data_df)  
    device_proportions = device_counts / total_users  
      
    print("Current device distribution:")  
    for device, proportion in device_proportions.items():  
        print(f"{device}: {proportion:.1%}")  
      
    return device_proportions  
  
def stratified_sample_allocation(user_df, group_size, device_proportions):  
    """  
    Allocates users to groups while maintaining device type proportions  
      
    Parameters:  
    user_df: DataFrame with user information  
    group_size: Desired size of each group  
    device_proportions: Target proportions for each device type  
      
    Returns: Dictionary with user IDs for each group  
    """  
    control_group = []  
    treatment_group = []  
      
    # Calculate target number of users for each device type  
    target_counts = {  
        device: int(group_size * proportion)  
        for device, proportion in device_proportions.items()  
    }  
      
    # Sample users for each device type  
    for device_type in target_counts:  
        device_users = user_df[user_df['device_type'] == device_type]  
          
        # Randomly sample users of this device type  
        sampled_users = device_users.sample(  
            n=target_counts[device_type] * 2  # Times 2 for both groups  
        )  
          
        # Split sampled users between groups  
        mid_point = len(sampled_users) // 2  
        control_group.extend(sampled_users.iloc[:mid_point].index)  
        treatment_group.extend(sampled_users.iloc[mid_point:].index)  
      
    return {  
        'control': control_group,  
        'treatment': treatment_group  
    }  
  
def collect_startup_time(user_id, group):  
    """  
    Collects startup time data for a single user session  
    Now includes stratification information  
    """  
    return {  
        'user_id': user_id,  
        'group': group,  
        'startup_time_ms': None,  # To be filled with actual measurement  
        'timestamp': datetime.now(),  
        'device_type': None,      # To be filled  
        'app_version': None       # To be filled  
    }  
  
# Example usage:  
def run_stratified_experiment(data_df, group_size=1000):  
    """  
    Sets up and runs a stratified experiment  
    """  
    # First, analyze current device distribution  
    device_props = analyze_device_distribution(data_df)  
      
    # Allocate users to groups maintaining device proportions  
    groups = stratified_sample_allocation(data_df, group_size, device_props)  
      
    # Verify stratification worked as expected  
    print("\nVerifying group distributions:")  
    for group_name, user_ids in groups.items():  
        group_df = data_df.loc[user_ids]  
        print(f"\n{group_name.title()} Group Device Distribution:")  
        device_dist = group_df['device_type'].value_counts(normalize=True)  
        for device, prop in device_dist.items():  
            print(f"{device}: {prop:.1%}")  
      
    return groups
```

#### Step 3: Determine the Decision Criteria

For this mobile app optimization project, we might set:

* **Statistical Significance:** α = 0.05
  + Standard alpha level, 95% confidence
* **Minimum Effect:** 100ms reduction in load time
  + What reduction in load time is worth the engineering cost of the new system?
  + Typically this is information that you need to ask for or are given based on industry domain knowledge
  + With a known population standard deviation of 400ms, this equates to an effect size of 0.25
* **Power:** 80%
  + Standard power level, see considerations below
* **Business Guards:** Secondary metrics to monitor
  + No more than 0.1% increase in error rates
  + Memory usage cannot increase by more than 5%
  + Battery impact must be negligible

We use this information to create a basic ‘decision making framework’. 

**Decision Framework:**

1. **Primary Success Criterion:**
   1. Statistically significant reduction in startup time (p < 0.05)
   2. Minimum improvement of 100ms
2. **Secondary Considerations:**
   1. No increase in crash rates
   2. No adverse impact on memory usage
   3. No adverse impact on battery/power usage
3. **Implementation Criteria:**
   1. If successful, gradual rollout over 1 week
   2. If unsuccessful, document learnings and iterate

Once we have determined our alpha, effect size, and power **we can conduct a necessary power analysis to determine the minimum sample sizes needed.** For this calculation I went ahead and used this website: [ClinCalc Sample Size Calculator 


Links to an external site.](https://clincalc.com/stats/samplesize.aspx)

[![continuous endpoint, 2 sample study (size and parameters)](https://moringa.instructure.com/courses/1426/files/631677/preview)](https://moringa.instructure.com/courses/1426/files/631677/preview "continuous endpoint, 2 sample study (size and parameters)")

#### Step 4: Collect and Explore Data

Based on the sample size calculation above, **we need at least 251 users for our control and experimental group respectively.** Our control group will receive no change to the startup system while our experimental group will experience the new system.

As part of the data collection we **ensure that our users are being appropriately stratified** to account for differences in device and network types. This can be validated by checking the distributions of each group/sample as the data is being collected.

Given a daily user volume of 1000 individuals, **we decide to run this experiment for 1 week, each day we randomly select 100 individuals for each group resulting in a total of 500 samples for each group,** well above the necessary minimum.

**Exploratory data analysis can then be conducted on the data collected** to understand basic statistics and distribution information in order to inform the next step. Data cleaning might also need to be conducted in this step to ensure appropriate format, structure, and relevance. This includes considerations of outlier data and its removal. A common tactic is to treat anything beyond 3 standard deviations from the mean as outliers and remove them from the data.

```
def clean_data(data_df):  
    """  
    Removes outliers and invalid data points  
    """  
    # Remove startup times > 3 standard deviations  
    mean = data_df['startup_time_ms'].mean()  
    std = data_df['startup_time_ms'].std()  
    return data_df[abs(data_df['startup_time_ms'] - mean) <= 3 * std]
```

#### Step 5: Analyze and Interpret

Here we are interested in analyzing differences in a continuous numerical response variable (start-up time) and have two groups or samples in which we have pulled data, our control and experiment, leading to a two-sample and one-sided test (based on hypothesis setup).

**NOTE:** We could consider/setup this experiment as a 1-sample test. Comparing the experimental startup times (new system) to the known population startup time (current system). However, we have the ability to sample a control group in order to get an actual value for comparison. This control startup time might have changed from when the known population value was reported and might even help account for unchecked seasonality or compounding factors.

After conducting the appropriate statistical test we find that:

* The mean startup time for our control group was 1,994 ms (just about in line with our previous known value).
* The mean startup time for our experimental group was 1,700 ms.
* This gives us a difference/reduction in startup time of 294ms on average, well above the practical threshold.
* Our statistical test returned a p-value of 0.001.

At a confidence level of 0.05 we reject our null hypothesis in favor of the alternative.

***“Our statistical test showed there was a significant reduction in app startup time for our new system when compared to the current one.”***

When looking at the actual difference, we see a reduction of almost 300ms on average in startup time for the new system. This equates to roughly a 15% decrease in startup times for our users.

This is where we step through the decision making framework determined earlier. If no secondary metrics are affected we would conclude that this change is warranted based on the significant result and the overall practical difference being enough to justify the engineering cost.

“Based on the results above, we would recommend implementing this new startup system across the entirety of our user base in the hopes of improving load times and customer satisfaction. Note that only the most updated version of our app was tested, users on older versions might experience different results, we should ensure that updates are pushed when this new system is implemented.”

### Considerations

#### Common Challenges

**Data Quality Issues**

* Missing values
* Outliers
* Inconsistent measurements

**Timeline Pressure**

* Balancing speed vs. reliability
* Handling incomplete data
* Managing stakeholder expectations

**Technical Constraints**

* Implementation limitations
* Measurement capabilities
* System dependencies

**When determining minimum effect size, consider:**

1. Implementation costs
2. Expected benefits
3. Natural variation in your metrics
4. Business context and scale
5. What level of confidence does the business need?
6. Directly effects the sample size calculation

#### Key Challenges

1. **Unclear Research Questions**

* **Impact:** Makes hypothesis formation and testing impossible
* **Solution:** Use SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)

2. **Confounding Variables**

* **Impact:** Can invalidate results
* **Solution:** Document potential confounders in advance and control for them in design

3. **Timeline Pressure**

* **Impact:** May lead to insufficient sample sizes
* **Solution:** Use power analysis to determine minimum required sample size and timeline

4. **Multiple Testing**

* **Impact:** Increases risk of false positives
* **Solution:** Plan all tests in advance and adjust significance levels if testing multiple hypotheses, or use a more appropriate test for multiple samples.

#### Decision Point Trade-offs

* **More Stringent (lower α):**
  + **Pro**: Fewer false positives
  + **Con**: Requires larger sample sizes

* **Less Stringent (higher α):**
  + **Pro:** Can detect effects with smaller samples
  + **Con:** More false positives
* **Industry standards often use:**
  + **α = 0.05** for general business decisions
  + **α = 0.01** for critical decisions involving safety or large financial impacts
  + **α = 0.10** for exploratory research or when false positives are less costly

#### Decision Point Trade-offs

**Sample Size Selection:**

* **Larger:**
  + **Pro:** More reliable results
  + **Con:** Takes longer, costs more
* **Smaller:**
  + **Pro:** Faster, cheaper
  + **Con**: May miss important effects

#### Practical Business Thresholds

Beyond statistical criteria, consider setting explicit business thresholds:

1. **Primary Success Criteria:** The main metric must improve by at least X%
2. **Secondary Guards**: No negative impact on related metrics beyond Y%
3. **Risk Tolerances:** Maximum acceptable degradation in any metric

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248577

Scraped At: 2026-05-15T10:12:41.309970
