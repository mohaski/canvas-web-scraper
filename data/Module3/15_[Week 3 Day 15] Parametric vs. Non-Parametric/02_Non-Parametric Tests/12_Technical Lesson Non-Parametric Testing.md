# Technical Lesson: Non-Parametric Testing

# Technical Lesson: Non-Parametric Testing

## ![Blue FS Logo](https://moringa.instructure.com/courses/1426/files/631704/preview) Technical Lesson: Non-Parametric Testing

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time: 1 hour**

Medical research often presents unique statistical challenges that make it an ideal candidate for non-parametric and exact testing methods. In this lesson, we'll analyze a pain management treatment study using our comprehensive four-step approach to statistical analysis.

Our study examines two key aspects of a new pain treatment:

* Individual patient pain scores before and after treatment (paired data on a 0-10 scale)
* Treatment success rates between two independent patient groups (success being a reduction in pain)
  + Group A: Received pain management treatment
  + Group B: Placebo, did not receive actual pain management treatment

### Video: Parametric vs. Non-Parametric Testing

The video below will guide you through each step of the Parametric vs. Non-Parametric Testing. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Parametric vs. Non-Parametric Testing.

[VIDEO LINK](https://player.vimeo.com/video/1060681319?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Resources & Tools

* Jupyter Notebook
* [PythonLinks to an external site.](https://www.python.org/) (3.7 or higher)
* **Required Libraries**
  + [NumPy](https://numpy.org/)
  + [Matplotlib](https://matplotlib.org/)
  + [SciPyLinks to an external site.](https://scipy.org/ "Link")
  + [Seaborn](https://seaborn.pydata.org/ "Link")

### Instructions

### Step 1: Assessment Phase

* Examine the structure and characteristics of our pain score data
* Evaluate the distribution of before/after differences
* Assess the frequency and pattern of treatment responses
* Consider sample size implications for both analyses

This initial step is crucial because it shapes all subsequent analysis decisions. We're examining our data’s properties to understand what statistical approaches will be most appropriate.

```
# Load in both datasets  
df_pain = pd.read_csv('paired_pain.csv')  
df_response = pd.read_csv('response_outcome.csv')  
  
  
# Function to help with basic EDA  
def assess_data_characteristics(pain_data, response_data):  
   """  
   Evaluates characteristics of both pain scores and treatment response data  
   """  
   print("Step 1: Data Assessment")  
   print("-" * 50)  
    
   # Analyze pain scores  
   print("Pain Score Analysis:")  
   print(f"Number of patients: {len(pain_data)}")  
   print("Summary statistics:")  
   print(pain_data.describe())  
    
   # Check normality of differences  
   differences = pain_data['before'] - pain_data['after']  
   _, p_value = stats.shapiro(differences)  
   print(f"\nNormality test of differences p-value: {p_value:.4f}")  
    
   # Analyze treatment response  
   contingency_table = pd.crosstab(response_data['group'],  
                                 response_data['success'])  
   print("\nTreatment Response Contingency Table:")  
   print(contingency_table)  
  
  
assess_data_characteristics(df_pain, df_response) 
```

### Output

```
Step 1: Data Assessment  
--------------------------------------------------  
Pain Score Analysis:  
Number of patients: 50  
Summary statistics:  
       patient_id     before      after  
count    50.00000  50.000000  50.000000  
mean     24.50000   7.280000   5.243031  
std      14.57738   1.852081   2.032219  
min       0.00000   4.000000   0.929015  
25%      12.25000   6.000000   3.970540  
50%      24.50000   7.000000   5.183064  
75%      36.75000   9.000000   6.493707  
max      49.00000  10.000000   9.178334  
  
Normality test of differences p-value: 0.8648  
  
Treatment Response Contingency Table:  
success   0   1  
group            
A         7  43  
B        20  30
```

### Step 2: Selection Phase

* Choose appropriate tests based on data characteristics
* Consider the paired nature of pain scores
* Account for small sample sizes in treatment response data
* Balance statistical power with assumption requirements

Now we determine which specific tests to use based on our data characteristics. The selection phase focuses on matching our analytical tools to our data's characteristics. We're choosing non-parametric methods for the pain scores and an exact test for the treatment responses.

* Pain Scores: Wilcoxon signed-rank test
  + Rating data is ordinal hence non-parametric
  + Data is paired across treatments
* Treatment Response: Fisher's exact test
  + Small samples and low frequencies in contingency table
  + Fisher’s better than Chi-squared

### Step 3: Implementation Phase

* Apply selected statistical tests systematically
* Create informative visualizations
* Calculate effect sizes and confidence intervals
* Document all analytical steps

Here we actually perform our chosen statistical tests.

### Output

```
Step 3: Conducting Statistical Analysis  
--------------------------------------------------  
Pain Score Analysis Results:  
Wilcoxon test p-value: 0.0000  
  
Treatment Response Analysis Results:  
Fisher's exact test p-value: 0.0063  
Odds ratio: 0.24
```

 
![2 box plot graphs noting pain scores for treatment and groups](https://moringa.instructure.com/courses/1426/files/631680/download)

### Step 4: Interpretation Phase

* Translate statistical findings into clinical relevance
* Consider practical significance alongside statistical significance
* Provide context for healthcare decision-making
* Address limitations and uncertainties

Finally, we interpret our results in a clinically meaningful way.

**Pain Management Effectiveness:**

* Treatment significantly reduced pain scores
* Evidence supports treatment's pain management efficacy

**Treatment Response:**

* Group differences are statistically significant
* Group A shows 0.2x higher odds of success
* The Treatment group had a significantly higher success rate then the placebo group indicting the efficacy of the new treatment

**Clinical Recommendations:**

* New pain management treatment is effective at reducing pain levels significantly, implement for appropriate patients
* Monitor pain scores regularly during treatment as there is a wide range of scores both before and after, individuals might respond differently
* Document any adverse events or treatment modifications
* The new pain treatment warrants a follow-up comparison against other pain management treatments

### Considerations

When analyzing medical treatment data using non-parametric and exact tests, several important challenges and decision points require careful attention:

#### Critical Decision Points

Choice Between Wilcoxon Signed-Rank and Sign Test

**Pros of Wilcoxon:**

More powerful when assumptions are met

Uses magnitude of differences

Better for detecting subtle changes

**Pros of Sign Test:**

More robust to extreme values

Easier to interpret

Fewer assumptions required

#### Critical Decision Points

**Fisher's Exact Test vs. Chi-Square Decision**

Sample size considerations

Expected cell frequencies

Trade-off between exact calculations and asymptotic approximations

Computational limitations with larger samples

#### Critical Decision Points

**Effect Size Reporting**

Choice of effect size metrics for non-parametric tests

Clinical relevance thresholds

Communication to medical practitioners

Integration with existing medical literature

#### Common Challenges

**Missing Data Management**

Pain scores might be missing at follow-up visits

Patients may drop out of the study

Different missing data patterns between groups

Impact on paired analysis structure

#### Common Challenges

**Measurement Issues**

Pain scores are subjective and often clustered at certain values

Individual differences in pain perception

Potential ceiling and floor effects in pain scales

Variation in timing of measurements

#### Common Challenges

**Sample Size Limitations**

Medical studies often have smaller sample sizes due to recruitment challenges

Impact on statistical power

Balance between test sensitivity and assumption requirements

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248759

Scraped At: 2026-05-15T10:24:13.212177
