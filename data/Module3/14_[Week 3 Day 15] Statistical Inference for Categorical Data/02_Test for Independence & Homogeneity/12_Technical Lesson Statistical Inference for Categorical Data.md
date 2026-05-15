# Technical Lesson: Statistical Inference for Categorical Data

# Technical Lesson: Statistical Inference for Categorical Data

## ![Blue FS Logo](https://moringa.instructure.com/courses/1426/files/631704/preview) Technical Lesson: Independence and Homogeneity Tests

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

Imagine you are working for a healthcare clinic as a data analyst and have been tasked with investigating appointment scheduling in effort to improve patient satisfaction and attendance rate. We'll analyze sample data from a hypothetical healthcare clinic to understand patient appointment scheduling patterns and outcomes.

We'll use two types of chi-square tests to examine whether patients show preferences in scheduling times (goodness of fit) and whether scheduling methods are related to appointment attendance rates (independence).

### Video: Independence and Homogeneity Tests

The video below will guide you through each step of the Independence and Homogeneity Tests Technical Lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Independence and Homogeneity Tests.

[VIDEO LINK](https://player.vimeo.com/video/1060680787?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Resources & Tools

* Jupyter Notebook
* [PythonLinks to an external site.](https://www.python.org/) (3.7 or higher)
* **Required Libraries**
  + [NumPy](https://numpy.org/)
  + [Matplotlib](https://matplotlib.org/)
  + [SciPy


    Links to an external site.](https://scipy.org/ "Link")
  + [Seaborn


    Links to an external site.](https://seaborn.pydata.org/ "Link")

 [Links to an external site](https://numpy.org/)Links to an external si

### Instructions

### Step 1: Defining the Research Question's

Our investigation into patient appointment scheduling has two different avenues of exploration.

First, we want to understand if there is any preference for specific timeslots, which could help us plan volume and doctor availability in the future.

**This is an excellent opportunity and use case for a Goodness of Fit test**

* **Null:** There is no preference for timeslot (expected a even split)
* **Alternative:** There is a significant preference for timeslot

Second, we want to see if there is a relationship between the scheduling method and actual appointment attendance in the hopes of reducing our ‘no-show’ rates.

**This warrants a Test of Independence**

* **Null:** The scheduling method and attendance rate are independent and not related to each other
* **Alternative:** There is a significant relation between scheduling method and attendance rates. Attendance rates are dependent on the scheduling method.

### Step 2: Organize Data

We need to start by loading in our data and doing some very quick initial EDA.

```
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
  
# Read in the healthcare appointments data  
# Note: Replace 'clinic_appointments.csv' with your actual file path  
df = pd.read_csv('clinic_appointments.csv')  
  
  
# Let's first look at our data structure  
print("Basic Dataset Information:")  
print("-" * 30)  
print(df.info())  
  
  
# Check the first few rows to confirm data looks correct  
print("\nFirst Few Appointments:")  
print("-" * 30)  
print(df.head())  
  
  
# Get distribution of our key categorical variables  
print("\nDistribution of Time Slots:")  
print("-" * 30)  
time_dist = df['TimeSlot'].value_counts()  
print(time_dist)  
print("\nPercentage by Time Slot:")  
print((time_dist / len(df) * 100).round(1))  
  
  
print("\nDistribution of Booking Methods:")  
print("-" * 30)  
booking_dist = df['BookingMethod'].value_counts()  
print(booking_dist)  
print("\nPercentage by Booking Method:")  
print((booking_dist / len(df) * 100).round(1))  
  
  
# Create a cross-tabulation of booking methods and attendance  
print("\nBooking Method vs. Attendance:")  
print("-" * 30)  
booking_attendance = pd.crosstab(df['BookingMethod'], df['Attended'])  
print(booking_attendance)  
  
  
# Calculate attendance rates by booking method  
attendance_rates = (booking_attendance['Yes'] /  
                  booking_attendance.sum(axis=1) * 100).round(1)  
print("\nAttendance Rates by Booking Method (%):")  
print(attendance_rates)  
  
  
# Visualize key distributions  
plt.figure(figsize=(12, 4))  
  
  
# Time slot distribution  
plt.subplot(1, 3, 1)  
sns.countplot(data=df, x='TimeSlot', order=['Morning', 'Afternoon', 'Evening'])  
plt.title('Time Slot Distribution')  
plt.xticks(rotation=45)  
  
  
# Booking method distribution  
plt.subplot(1, 3, 2)  
sns.countplot(data=df, x='BookingMethod')  
plt.title('Booking Method Distribution')  
plt.xticks(rotation=45)  
  
  
# Attendance by booking method  
plt.subplot(1, 3, 3)  
sns.barplot(data=df, x='BookingMethod', y='Attended')  
plt.title('Attendance Rate by Booking Method')  
plt.xticks(rotation=45)  
  
  
plt.tight_layout()  
plt.show()  
  
  
# Check for any missing values  
print("\nMissing Values Check:")  
print("-" * 30)  
print(df.isnull().sum())  
  
  
# This initial EDA helps us:  
# 1. Confirm our data is loaded correctly  
# 2. See if we meet minimum frequency requirements for chi-square tests  
# 3. Get a preliminary view of potential patterns before formal testing
```

### Output

```
Basic Dataset Information:  
------------------------------  
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 1000 entries, 0 to 999  
Data columns (total 4 columns):  
 #   Column         Non-Null Count  Dtype   
---  ------         --------------  -----   
 0   Unnamed: 0     1000 non-null   int64   
 1   TimeSlot       1000 non-null   object  
 2   BookingMethod  1000 non-null   object  
 3   Attended       1000 non-null   object  
dtypes: int64(1), object(3)  
memory usage: 31.4+ KB  
None  
  
First Few Appointments:  
------------------------------  
   Unnamed: 0   TimeSlot BookingMethod Attended  
0           0    Morning         Phone      Yes  
1           1    Evening        Online      Yes  
2           2  Afternoon    Mobile App       No  
3           3  Afternoon        Online      Yes  
4           4    Morning    Mobile App      Yes  
  
Distribution of Time Slots:  
------------------------------  
TimeSlot  
Morning      461  
Afternoon    340  
Evening      199  
Name: count, dtype: int64  
  
Percentage by Time Slot:  
TimeSlot  
Morning      46.1  
Afternoon    34.0  
Evening      19.9  
Name: count, dtype: float64  
  
Distribution of Booking Methods:  
------------------------------  
BookingMethod  
Phone         385  
Online        357  
Mobile App    258  
Name: count, dtype: int64  
  
Percentage by Booking Method:  
BookingMethod  
Phone         38.5  
Online        35.7  
Mobile App    25.8  
Name: count, dtype: float64  
  
Booking Method vs. Attendance:  
------------------------------  
Attended       No  Yes  
BookingMethod           
Mobile App     30  228  
Online         34  323  
Phone          65  320  
  
Attendance Rates by Booking Method (%):  
BookingMethod  
Mobile App    88.4  
Online        90.5  
Phone         83.1  
dtype: float64  
  
Missing Values Check:  
------------------------------  
Unnamed: 0       0  
TimeSlot         0  
BookingMethod    0  
Attended         0  
dtype: int64
```

### Visualization

![3 distribution graphs noting time slot, booking, and attendance rate](https://moringa.instructure.com/courses/1426/files/631581/preview)

### Step 3: Calculate Expected Frequencies

For our Test of Independence the expected frequencies are calculated under the hood as part of the `scipy.stats.chi2_contingency`.

However for the Goodness of Fit test we need to determine what our expected frequencies will be and calculate them based on that information. In order to test the question, “are there preferences in time-slot?”, we need to consider the null hypothesis that there are no preferences. Based on ‘no preference’ we would expect the frequencies for each time-slot to be the same.

```
# Calculate expected frequencies (equal distribution)   
n_appointments = len(df)   
n_slots = 3 # Morning, Afternoon, Evening   
expected = np.array([n_appointments/n_slots] * n_slots)
```

### Step 4: Running the Tests

### Goodness of Fit Test

```
from scipy.stats import chisquare, chi2_contingency  
  
# Count observed frequencies   
observed = df['TimeSlot'].value_counts().values  
  
# Perform chi-square goodness of fit test   
stat, p_value = chisquare(observed, expected)  
print(f"P-value: {p_value}")  
  
slot_reuslts = {'observed': observed, 'expected': expected, 'statistic': stat, 'p_value': p_value}  
  
# Visualize the comparison   
plt.figure(figsize=(10, 6))   
slots = ['Morning', 'Afternoon', 'Evening']   
x = range(len(slots))   
  
plt.bar(x, observed, width=0.4, align='edge', label='Observed', color='skyblue')   
plt.bar([i+0.4 for i in x], expected, width=0.4, align='edge', alpha=0.7, label='Expected', color='lightgreen')   
plt.xticks([i+0.4 for i in x], slots)   
plt.ylabel('Number of Appointments')   
plt.title('Appointment Time Slot Distribution: Observed vs Expected')  
plt.legend()
```

P-value: 3.9608440197756407e-23

![graph compareing morning afternoon evening observed vs expected time slot](https://moringa.instructure.com/courses/1426/files/631653/download)

### Test of Independence

```
Panel 2 Content.# Create contingency table   
contingency = pd.crosstab(df['BookingMethod'], df['Attended'])  
   
# Perform chi-square test of independence   
stat, p_value_ind, dof, expected = chi2_contingency(contingency)  
print(f"P-value: {p_value_ind}")  
  
# Calculate proportions for visualization   
props = contingency.div(contingency.sum(axis=1), axis=0) * 100  
  
attendance_results = {'contingency_table': contingency, 'proportions': props, 'expected': expected, 'statistic': stat, 'p_value': p_value_ind, 'dof': dof }  
  
# Visualize the relationship   
plt.figure(figsize=(10, 6))   
props.plot(kind='bar', stacked=True)   
plt.title('Attendance Rates by Booking Method')   
plt.xlabel('Booking Method')   
plt.ylabel('Percentage')   
plt.legend(title='Attended')   
plt.tight_layout()
```

 P-value: 0.00896194221644184

 
![graph comparing attendance rates by booking methods](https://moringa.instructure.com/courses/1426/files/631661/download)

### Step 5: Assess Significance of Tests

Both tests resulted in p-values less than an alpha of 0.05, leading to significant conclusions. Patients appear to have a preference for morning time-slots over the other two and patients who booked online have higher attendance rates. The scheduling method had a significant effect on the attendance rate of patients. 

### Output

```
Healthcare Appointments Analysis Report  
==================================================  
  
1. Time Slot Preference Analysis  
----------------------------------------  
  
Observed Frequencies:  
Morning: 461  
Afternoon: 340  
Evening: 199  
  
Chi-square statistic: 103.166  
P-value: 0.0000  
  
Finding: There is significant evidence of time slot preferences  
Morning: +38.3% from expected  
Afternoon: +2.0% from expected  
Evening: -40.3% from expected  
  
2. Booking Method and Attendance Relationship  
----------------------------------------  
  
Attendance Rates by Booking Method:  
Attended         No   Yes  
BookingMethod              
Mobile App     11.6  88.4  
Online          9.5  90.5  
Phone          16.9  83.1  
  
Chi-square statistic: 9.430  
P-value: 0.0090  
  
Finding: There is a significant relationship between  
booking method and attendance rates  
Mobile App attendance rate: 88.4%  
Online attendance rate: 90.5%  
Phone attendance rate: 83.1%
```

### Step 6: Interpret Results

**Interpretation of Statistical Findings**

Our analysis revealed two significant patterns in our appointment data.

* First, the chi-square goodness of fit test showed that patients do not schedule appointments equally across all time slots, with a clear preference for morning appointments.
* Second, our test of independence demonstrated a significant relationship between booking methods and attendance rates, with digital booking methods associated with higher attendance rates.

Business Impact and Context

These findings tell us an important story about patient behavior and clinic operations. The time slot preferences suggest that our current scheduling system might not be optimally aligned with patient demand. With morning slots being consistently more popular, we're likely experiencing high competition for these appointments while having unused capacity in other periods. Meanwhile, the connection between booking methods and attendance rates indicates that our digital scheduling tools are not just convenient – they're actually helping improve patient compliance with appointments.

Based on these statistical insights, here are specific recommendations for improving clinic operations:

### Scheduling Optimization

1. Increase morning slot availability by adjusting staff schedules to match peak demand periods
2. Consider implementing incentives (like shorter wait times or reduced fees) for less popular time slots to help distribute demand more evenly
3. Review current scheduling templates to ensure they align with observed patient preferences

### Digital Transformation

1. Expand digital booking options, considering that patients who book digitally are more likely to attend their appointments
2. Gradually transition more appointments to online and mobile app booking systems
3. Develop a targeted communication strategy to promote digital booking options to patients who typically book by phone

### Operational Improvements

1. Implement an automated reminder system integrated with digital booking platforms
2. Consider overbooking less for digitally booked appointments given their higher attendance rates
3. Design different confirmation protocols based on booking method, with more intensive follow-up for phone bookings

### Resource Allocation

1. Adjust staffing levels to better match observed time slot preferences
2. Invest in improving and expanding digital booking infrastructure
3. Develop training programs to help staff assist patients in transitioning to digital booking methods

### Expected Outcomes

By implementing these recommendations, the clinic could expect:

* Improved patient satisfaction through better appointment availability
* Reduced no-show rates by promoting more reliable booking methods
* More efficient resource utilization by matching staffing to demand
* Enhanced operational efficiency through increased use of digital tools
* Better capacity management across all time slots

### Considerations

These considerations directly impact the reliability and utility of our analyses. For example, in our healthcare appointment analysis, choosing three time slots rather than hourly blocks allowed us to maintain adequate cell counts while still providing actionable insights for clinic scheduling. Similarly, our decision to separate mobile app bookings from other online bookings revealed important differences in attendance patterns that might have been masked with broader categorization.

##### Common Issues and Solutions

1. **Data Quality Considerations**

* Missing or incorrect timestamps
* Inconsistent booking method categorization
* Solution: Implement data validation and cleaning steps

2. **Sample Size Requirements**

* Monitor expected frequencies (should be ≥ 5)
* Consider combining categories if needed
* Validate assumptions before analysis

3. **Temporal Patterns**

* Time slot preferences might vary by season
* Consider analyzing subsets of data
* Account for holiday effects

##### Statistical Testing Decisions

**Setting Significance Level:** Using Standard α = 0.05 

**Pros:**

* Widely accepted in healthcare research
* Balances Type I and Type II errors
* Facilitates comparison with other studies

**Cons:**

* May be too liberal for high-stakes healthcare decisions
* Doesn't account for multiple testing issues
* Could lead to overconfidence in marginal results

##### Statistical Testing Decisions

**Setting Significance Level:** Handling Small Cell Counts. When considering category combinations: 

**Pros:**

* Maintains statistical validity of chi-square tests
* Reduces risk of false conclusions
* Simplifies interpretation

**Cons:**

* Loses granularity in the analysis
* May obscure meaningful differences between combined categories
* Could reduce practical utility of findings

##### Recommendations for Decision Making

**Category Definitions:**

* Start with broader categories and subdivide only if sample sizes permit
* Document category definitions clearly for reproducibility
* Consider practical significance alongside statistical significance

##### Recommendations for Decision Making

**Sample Size Planning:**

* Aim for minimum expected frequencies of 5 in all cells
* Calculate required sample sizes before data collection
* Plan for potential category combinations if needed

##### Recommendations for Decision Making

**Testing Strategy:**

* Consider adjusted significance levels for multiple tests
* Document all decision points in the analysis
* Validate results with alternative statistical approaches when appropriate

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248727

Scraped At: 2026-05-15T10:22:15.622852
