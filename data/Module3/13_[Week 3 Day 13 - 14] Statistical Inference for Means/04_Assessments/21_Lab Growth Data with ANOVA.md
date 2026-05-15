# Lab: Growth Data with ANOVA

## ![](https://moringa.instructure.com/courses/1426/files/631644/preview?) Lab: Growth Data with ANOVA

As a research assistant at a marine biology research center, you're helping analyze data from a coral restoration project. The center has been growing different genotypes of staghorn coral (Acropora cervicornis) in their nursery to determine which genetic strains show the best growth potential for reef restoration.

The research team has collected growth data (measured in centimeters of linear extension) over 1 year for 6 different coral genotypes. Initial fragments sizes were within .05cm of each other and only single tip fragments were used. Within the nursery 10 fragments from each genotype were placed on each growout tree (60 fragments total) for a total of 50 trees. This was done to try and control for any variation within the nursery setting.

Your task is to determine if there are significant differences in growth rates between these genotypes, which will help inform which strains should be prioritized for future restoration efforts.

### Tools and Resources

* Data File: [coral\_growth.csv


  Links to an external site.](https://drive.google.com/file/d/1ShNe2Lwe2wAoEQjwwbNsvIx8jmQQhLGM/view "Link")
  + Contains columns:

    - Genotype (G1, G2, G3, G4, G5, G6)
    - Growth\_cm (linear extension in centimeters)
* [Python 


  Links to an external site.](https://www.python.org/)
* [statsmodel


  Links to an external site.](https://www.statsmodels.org/stable/index.html)
* [Jupyter Notebook: stats\_model\_infer\_mean.ipynb


  Links to an external site.](https://drive.google.com/file/d/1TDgEErk84vM-ghTeOuwjntuOt0HWQTrM/view)

### Instructions

### [Step 1: Defining your research question and planning your analysis](#dpPanel0)

Define Hypothesis: Select the appropriate null and alternative hypothesis

### [Step 2: Conducting initial data exploration](#dpPanel1)

Data Preparation and Exploration

* Load the coral growth data
* Calculate descriptive statistics for each genotype
* Create initial visualizations to understand the distribution of growth rates

### [Step 3: Examining data quality and checking assumptions](#dpPanel2)

Check ANOVA Assumptions

* Test for normality within each genotype
* Test for homogeneity of variances
* Document any violations and planned adjustments

### [Step 4: Performing the ANOVA test](#dpPanel3)

Conduct ANOVA Analysis

* Perform one-way ANOVA
* Document your findings

### [Step 5: Conducting post-hoc analysis when needed](#dpPanel4)

Post-hoc Analysis

* If ANOVA is significant, conduct Tukey's HSD test
* Create clear visualization of results

### [Step 6: Calculating and interpreting effect sizes](#dpPanel5)

Write Analysis Report

* Calculate effect size
* Summarize findings
* Make recommendations for the restoration program

### Submission and Grading Criteria

1. 1. Review the rubric below as a guide for how this lab is graded.
   2. Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
   3. When you are ready to submit, launch CodeGrade.
      * Click on + Create Submission. Upload your Jupyter notebook file for this lab.
      * For additional information on submitting assignments in CodeGrade: [Getting Started in CanvasLinks to an external site.


        Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
      * You can review your submission in CodeGrade and see your score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248695

Scraped At: 2026-05-15T10:20:34.575923
