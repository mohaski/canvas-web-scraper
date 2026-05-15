# Lab: Experimental Design and Statistical Testing

## ![](https://moringa.instructure.com/courses/1426/files/631644/preview?) Lab: Experimental Design and Statistical Testing

This lab will walk you through designing a hypothesis testing process for 2 scenarios for data analysis at Spotify. At each step, you'll analyze and reflect on the key decisions that need to be made as a part of the process.

Scenario

You are a data analyst at Spotify. The product team has developed a new personalized playlist algorithm they believe will increase user engagement. Before rolling this out globally, they want to test if the new algorithm actually improves weekly listening time compared to the current system.

### Instructions

#### [Part 1: Research Question Definition and Hypothesis Formation](#dpPanel0)

* Read the following context and answer the reflection questions. In this step you will need to define the research question. **Clear problem definition guides the entire investigation. Formulate the hypotheses and state both null and alternative hypotheses precisely.**

The product team says: "We think the new algorithm will make people listen more because it's better at finding music they'll like. Can you test if it works?"

**State both null and alternative hypotheses precisely.** Consider these potential hypotheses:

* **H₀:** The new algorithm does not increase listening time
* **H₁:** The new algorithm increases listening time

##### Reflection Questions

Reflection questions to for clear problem definition guides the entire investigation:

1. What makes this initial request problematic for hypothesis testing?
2. How would you refine this into a specific, measurable research question?
3. What additional information would you need from the product team?
4. Would a one-sided test or two-sided test be best in this scenario? Why?
5. What are the potential risks of choosing a one-sided test?

#### [Part 2: Experimental Design Framework](#dpPanel1)

* Read the following context and answer the reflection questions. In this step you will need to design the experimental framework. **Identify what variables need to be controlled. How sampling will be conducted.**

The platform has 100 million active users worldwide across different subscription types (free and premium). Given here is Spotify's user segmentation:

* **Premium subscribers:** 40% of user base
* **Free tier users:** 60% of user base
* **Geographic distribution:** 30% US, 40% Europe, 30% Rest of World
* **Device usage:** 70% mobile, 20% desktop, 10% other

##### Reflection Questions

1. What factors might affect listening time that need to be controlled for?
2. How would you ensure representative sampling across user segments?
3. What potential biases could emerge from improper sampling?

#### [Part 3: Setting Decision Criteria](#dpPanel2)

* Read the following context and answer the reflection questions. In this step you will need to set decision criteria. **Document your significance level. Determine sample size based on MDE**

The product team says implementing the new algorithm will require a lot of engineering resources and costs so the change must be significant.

##### Reflection Questions

1. How would the implementation cost affect your choice of:

* Significance level (α)
* Minimum effect size
* Required statistical power

2. What specific business metrics would you need to define "significant improvement"?
3. What secondary metrics could be monitored for potential negative impacts?

#### [Part 4: Data Collection](#dpPanel3)

* Read the following context and answer the reflection questions. In this step you will need to determine implementation and data collection. **Gather measurements and examine basic patterns. Ensure proper randomization and group assignment**

After running your experiment and collecting the appropriate data for one week you observe the following metrics:

* Weekly listening time (primary metric)
* **Control group (n=500,000):**
  + Mean: 118.5 minutes
  + Standard deviation: 44.2 minutes
  + 95% Confidence Interval: [117.8, 119.2] minutes

* **Treatment group (n=500,000):**
  + Mean: 122.3 minutes
  + Standard deviation: 43.8 minutes
  + 95% Confidence Interval: [121.6, 123.0] minutes

##### Reflection Questions

1. How would you interpret these confidence intervals in non-technical language
2. What does the overlap (or lack thereof) between confidence intervals tell us?

#### [Part 5: Analyze and Interpret](#dpPanel4)

* Read the following context and answer the reflection questions. In this step you will need to determine the analysis and interpretation. **Select and perform appropriate statistical analysis test. Evaluate statistical significance according to alpha and p\_value. Interpret in the context of your initial business question/s.**

**Scenario 1: Your test comparing the new and old playlist algorithms returns the following results:**

* p-value = 0.047
* Average listening time increase: 8 minutes per week
* Sample size: 500,000 users per group
* Test duration: 2 weeks

**Scenario 2: Your test results show:**

* p-value = 0.08 (above traditional 0.05 threshold)
* Effect size: 12 minutes increased listening time per week
* High variance in the data
* Strong positive trends in user satisfaction metrics

##### Scenario 1: Reflection Questions

1. How would you explain this p-value to non-technical stakeholders? What common misinterpretations should you help them avoid? What other factors might you include?
2. If running the same test with 5 million users per group returned a p-value of 0.001, but showed only a 2-minute increase in listening time, how would this change your interpretation?

##### Scenario 2: Reflection Questions

1. How would you approach making a recommendation in this case? What factors beyond the p-value would influence your decision?
2. How would you handle stakeholder pressure to make a definitive "yes/no" decision based solely on statistical significance?
3. What additional data or analyses might help provide more context for decision-making?

### Submission and Grading Criteria

1. Use the rubric below to review the grading criteria and expectations for this assessment.
2. When you are ready, submit this assignment by uploading a document below or writing directly in the text box included.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248580

Scraped At: 2026-05-15T10:12:57.785731
