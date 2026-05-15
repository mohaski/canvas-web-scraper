# Summative Lab: Evaluating Customer Behavior with Inferential Statistics

## ![](https://moringa.instructure.com/courses/1426/files/631644/preview?) Summative Lab- Evaluating Customer Behavior

This summative lab bridges the concepts and techniques learned throughout the course with their practical application to a real-world industry scenario.

You will step into the role of a junior data analyst for a retail company and apply your skills to evaluate customer behavior, satisfaction, and promotional impacts.

By completing this lab, you will have:

* Practiced designing and executing statistical analyses in a real-world scenario.
* Reinforced your understanding of test selection and assumptions.

### [Understand the Scenario and Objectives](#dpPanel0)

* Review the scenario
* Identify the two primary business questions
* Reflect on how this analysis can guide marketing and operational strategies

### [Plan the Analysis (Experimental Design)](#dpPanel1)

* Formulate hypotheses
* Determine the types of data and the right tests
* Assess the dataset for adequacy

### [Explore and Prepare the Data](#dpPanel2)

* Load the dataset and review its structure (e.g., variables, sample size, missing data).
* Summarize key metrics (e.g., average spending, satisfaction ratings).
* Visualize data distributions (e.g., histograms, boxplots) to understand patterns and check for outliers.
* Test assumptions for parametric tests

### [Perform the Statistical Tests](#dpPanel3)

* Execute the selected tests step by step:
* For each test, report the statistical results (e.g., p-values, test statistics) and interpret their significance.

### [Interpret Results and Make Recommendations](#dpPanel4)

* Summarize the findings for each analysis:

+ Highlight key differences (e.g., spending is higher in City Center).
+ Discuss practical implications (e.g., allocating more promotional efforts to rural locations).

* Create visualizations to communicate insights effectively
* Relate the results back to the original business questions and provide actionable recommendations.

### [Reflect on the Process](#dpPanel5)

* Discuss the importance of experimental design in ensuring meaningful and valid results.
* Evaluate the sufficiency of the dataset and any limitations
* Suggest ways to improve the analysis or collect additional data in the future.

### [Document and Present Your Work](#dpPanel6)

Compile your findings into a concise technical report notebook, ensuring that the analysis is clear and reproducible.

### Overview Video: Inferential Statistics

The video below will guide you through each step of the Evaluating Customer Behavior Lab with Inferential Statistics. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Evaluating Customer Behavior Lab with Inferential Statistics.

[VIDEO LINK](https://player.vimeo.com/video/1061406176?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Business Scenario

Imagine you are a junior data analyst working for a retail company that operates stores in three distinct regions: City Center, Suburb, and Rural. Your manager has tasked you with analyzing customer behavior and preferences across these locations. The goal is to help the company answer two key questions:

* Do customer spending patterns, satisfaction levels, and product preferences differ across store locations?
* Do promotional periods result in significantly higher spending compared to non-promotional periods?

* [Spending Across Location](#dpPanel7Content)
* [Ratings Across Locations](#dpPanel8Content)
* [Promotional Spending](#dpPanel9Content)

### Spending Across Location

**Business-relevant MDE:** Relative difference in spending of 10$ or more

**Justification:** This represents enough of a difference to warrant location-specific strategies (inventory, staffing, etc.)

### Ratings Across Locations

**Business-relevant MDE:** 1.0 point difference between locations

**Justification:** On a 10-point scale, a one point difference is noticeable and actionable for customer service improvements

### Promotional Spending

**Business-relevant MDE:** A $15 increase from non-promotional periods

**Justification:** Promotional costs typically reduce margins by ~15-20%. Need at least 25% increase in spending to justify promotional costs. This aligns with industry standards for promotional ROI

Your task involves designing and conducting an analysis using the provided dataset to derive actionable insights. You will apply statistical concepts and techniques such as experimental design, test selection, hypothesis testing, and result interpretation. This process mimics real-world industry scenarios where junior analysts evaluate business performance using data.

The study focuses on four variables:

1. Amount spent by customers (in dollars).
2. Customer satisfaction ratings (scale of 1 to 10).
3. Product category preferences (Electronics, Clothing, Groceries).
4. Purchase type (Promotional vs. Non-Promotional).

Your analysis will inform decision-making around marketing strategies, store operations, and promotional campaigns.

### Tools and Resources

* [Jupyter Notebook: Evaluating Customer Behavior with Inferential Statistics


  Links to an external site.](https://drive.google.com/file/d/1iYCaNfV-NRVUDpQ9yQXDyDC3rccxYeE0/view)
* Provided Datasets: [retailstorecustomerdata.csv


  Links to an external site.](https://drive.google.com/file/d/1BT38CqHiQFiRLx6BsxxjpF-duIH_OJ7b/view)
* PythonLinks to an external site. (3.7 or higher)
* Required Libraries
  + [Pandas for Python


    Links to an external site.](https://pandas.pydata.org/)
  + [Matplotlib](https://matplotlib.org/)
  + [SciPy](https://scipy.org/ "Link")
  + [Seaborn](https://seaborn.pydata.org/ "Link")

### Instructions

By following the outlined process, you will gain experience in experimental design, statistical testing, and actionable decision-making. Your task is not only to conduct the analysis but also to reflect on how these techniques help solve real-world problems that businesses face daily.

* [Part 1: Experimental Design](#dpPanel10Content)
* [Part 2: Data Exploration](#dpPanel11Content)
* [Part 3: Hypothesis Testing](#dpPanel12Content)
* [Part 4: Interpretation and Reporting](#dpPanel13Content)
* [Part 5: Conclusion, Reflection and Lessons Learned](#dpPanel14Content)

### Part 1: Experimental Design

**Define the Hypotheses:** Clearly state the null and alternative hypotheses for each of the following:

* Differences in spending across store locations.
* Differences in customer satisfaction across store locations.
* Differences in spending between promotional and non-promotional periods.
* Relationship between product category preferences and store location.

### Part 2: Data Exploration

1. **Load and examine the dataset:**

1. * Check for missing values or inconsistencies.
   * Summarize the key statistics of each variable.
2. **Visualize the distribution of spending and satisfaction ratings across locations.**
3. **Assess the assumptions for each test:**
   * For parametric tests, test for normality (e.g., Shapiro-Wilk test) and homogeneity of variance (e.g., Levene’s test)
   * Discuss the implications if these assumptions are violated
4. **Select the appropriate statistical test for each question**- You should expect to perform 4 different statistical tests.

### Part 3: Hypothesis Testing

1. Setup your data correctly in order to conduct the appropriate statistical tests
2. Perform Parametric Tests
3. Perform Non-Parametric Tests

* If assumptions for parametric tests are violated, use a non-parametric test.

### Part 4: Interpretation and Reporting

1. Summarize the results of your analysis:
   * Clearly state whether the null hypotheses were rejected or not. Frame this in the business question context.
   * Use effect sizes (e.g., Cohen’s d, eta squared) to contextualize the significance of your results.
2. Explain the practical implications of the results:
   * What should the company do based on your findings about spending, satisfaction, or product preferences?
3. Create visualizations to support your conclusions (e.g., bar charts for categorical variables, boxplots for continuous variables).

### Part 5: Conclusion, Reflection and Lessons Learned

1. Reflect on the importance of experimental design and sufficient sample size in conducting a robust analysis.
2. Identify any limitations in the dataset or analysis (e.g., potential biases, unmeasured variables).
3. Suggest additional data the company could collect to improve future analyses.

### Submission and Grading Criteria

* Refer to the rubric below for the grading criteria for this part of your lab.
* Submit the completed analysis as a single notebook (ipynb) file. The notebook should contain:  
  + All relevant code
  + Markdown and analysis of the data
  + Visuals to represent EDA and recommendations
  + Results of the statistical tests
  + Your reflection in Part 5 at the end of notebook as a conclusion
* When you are ready, submit your Jupyter Notebook project file. Click *Start Assignment* and upload your file below.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248770

Scraped At: 2026-05-15T10:25:14.111892
