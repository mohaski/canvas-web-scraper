# Summative Lab: Data Analysis Jet Airline Safety

## ![](https://moringa.instructure.com/courses/1406/files/625182/preview?) Summative Lab: Data Analysis Jet Airline Safety

* [Current: Summative Lab: Data Analysis Jet Airline Safety (1 of 2), Assignment](https://moringa.instructure.com/courses/1406/modules/items/243671 "Current: Summative Lab: Data Analysis Jet Airline Safety (1 of 2), Assignment")
* [Summative Quiz: Introduction to Data Science (2 of 2)](https://moringa.instructure.com/courses/1406/modules/items/243672 "Summative Quiz: Introduction to Data Science (2 of 2)")

*​*

**Estimated Completion Time:** 8 hours

![United Airlines plane on tarmac](https://moringa.instructure.com/courses/1406/files/625081/download?)

Imagine you are part of a consulting firm that is tasked to do an analysis of commercial and passenger jet airline safety. The client (an airline/airplane insurer) is interested in knowing what types of aircraft (makes/models) exhibit low rates of total destruction and low likelihood of fatal or serious passenger injuries in the event of an accident. They are also interested in any general variables/conditions that might be at play. Your analysis will be based on aviation accident data accumulated from the years 1948-2023.

Our client is only interested in airplane makes/models that are professional builds and could potentially still be active. Assume a max lifetime of 40 years for a make/model retirement and make sure to filter your data accordingly (i.e., from 1983 onwards). They would also like separate recommendations for small aircraft vs. larger passenger models. **In addition, make sure that claims that you make are statistically robust and that you have enough samples when making comparisons between groups.**

In this summative assessment you will demonstrate your ability to:

1. Use Pandas to load, inspect, and clean the dataset appropriately.
2. Transform relevant columns to create measures that address the problem at hand.
3. Conduct EDA: visualization and statistical measures to systematically understand the structure of the data.
4. Recommend a set of airplanes and makes conforming to the client's request and identify at least *two* factors contributing to airplane safety. You must provide supporting evidence (visuals, summary statistics, tables) for each claim you make.

The video below will guide you through each step of the lab. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of the lab.

[VIDEO LINK](https://player.vimeo.com/video/947024693?h=6b77be476b)

### Tools and Resources

* Terminal with learn-env conda environment
* [Github Repository with Jupyter Notebook


  Links to an external site.](https://github.com/flatiron-school/dsc-course0-m8-lab/tree/main)
  + For ease of accessibility, the data file has been added to the repo
* [link to the Airplane accident data


  Links to an external site.](https://www.kaggle.com/datasets/mos3santos/acidentes-de-aviao-at-2023); Kaggle link is different than the video but is the same data
  + [Link to the zip file (housed in Canvas)](https://moringa.instructure.com/courses/1406/files/624863?verifier=KDR3veOM0NaznsyTi1K6Z3df1ldnkb76l5c1j8vZ&wrap=1 "aviationData.zip")[Download Link to the zip file (housed in Canvas)](https://moringa.instructure.com/courses/1406/files/624863/download?verifier=KDR3veOM0NaznsyTi1K6Z3df1ldnkb76l5c1j8vZ&download_frd=1) in case there are issues with the link to Kaggle

### Lab Overview

1. **Fork** the assessment [repository


   Links to an external site.](https://github.com/flatiron-school/dsc-course0-m8-lab/tree/main) and **clone** it.
2. **Download the dataset** from Kaggle in a single .csv file. Place the file in the appropriate folder in the repository.
3. Complete all **data cleaning tasks** in the Aviations Accident Cleaning notebook. Pandas will be your primary tool, but you are free to use other base Python libraries and data structures.
4. Once cleaning is complete, move on to the Aviation Accident Data Analysis notebook. Complete any **exploratory data analysis** tasks and write short analysis summaries where prompted. Again, Pandas will be a primary tool, but you are free to use other base Python libraries when it is easier/appropriate. You should be making full use of statistical summary methods, the split-apply-combine paradigm for data aggregation across groups, and statistical visualization with the aid of Seaborn and Matplotlib.
5. Your submission must have make/model recommendations for small and large airplanes and analyze at least two factors potentially affecting injury/damage outcomes.
6. Ensure that your local and remote GitHub repository has documentation of the project (a README.md) that contains your short analysis summary and any key visualizations.
7. Finished assessment should be:
   1. A link to your GitHub repository
   2. Uploads of Cleaning and Data Analysis .ipynb files

### Lab Steps: Part One

For the first part of the assessment, you will address:

* Using Pandas to load, inspect, and clean the dataset appropriately.
* Transforming relevant columns to create measures that address the problem at hand.

* [Step1](#dpPanel0Content)
* [Step 2](#dpPanel1Content)
* [Step 3](#dpPanel2Content)
* [Step 4](#dpPanel3Content)
* [Step 5](#dpPanel4Content)
* [Step 6](#dpPanel5Content)
* [Step 7](#dpPanel6Content)
* [Step 8](#dpPanel7Content)
* [Step 9](#dpPanel8Content)

#### Make Relevant Library Imports

```
import numpy as np  
  
import pandas as pd  
  
import matplotlib.pyplot as plt  
  
import seaborn as sns
```

#### Data Loading and Inspection

Load in data from the relevant directory and inspect the dataframe.

* Inspect NaNs and datatypes
* Print out summary statistics

#### Data Cleaning

**Filtering aircraft and events**

We want to filter the dataset to include aircraft that the client is interested in an analysis of:

* Inspect relevant columns
* Figure out any reasonable imputations
* Filter the dataset

**Aircraft.Category**

* Client is only interested in airplanes

**Amateur.Built**

* Client is only interested in professional builds

**Event.Date**

* Removing all events older than 40 years ago

#### Cleaning and Constructing Key Measurables

Injuries and robustness to destruction are a key interest point for the client. Clean and impute relevant columns and then create derived fields that best quantifies what the client wishes to track. **Use commenting or markdown to explain any cleaning assumptions as well as any derived columns you create.**

1. Construct metric for fatal/serious injuries.

***Hint:**Estimate the total number of passengers on each flight. The likelihood of serious/fatal injury can be estimated as a fraction from this.*

1. Aircraft.Damage
   1. Identify and execute any cleaning tasks.
   2. Construct a derived column tracking whether an aircraft was destroyed or not.

#### Investigate the Make Column

* Identify cleaning tasks here.
* List cleaning tasks clearly in markdown.
* Execute the cleaning tasks.
* For your analysis, keep Makes with a reasonable number (put the threshold at 50).

#### Inspect Model Column

* Get rid of any NaNs.
* Inspect the column and counts for each model/make.
* Consider whether model labels are unique to each make. If not, create a derived column that is a unique identifier for a given plane type.

#### Cleaning Other Columns

There are other columns containing data that might be related to the outcome of an accident. We list a few here:

* Engine.Type
* Weather.Condition
* Number.of.Engines
* Purpose.of.flight
* Broad.phase.of.flight

Inspect and identify potential cleaning tasks in each of the columns. Execute those cleaning tasks.

***Hint:** Some things you might want to think about are values in numerical features that do not make sense or categories that contain too few examples. You might also want to treat values (for either categorical or numeric data) that might be placeholders for NaNs.*

**Note:** You do not necessarily need to impute or drop NaNs here.

#### Column Removal

Inspect the dataframe and drop any columns that have too many NaNs. For this exercise, keep all columns with more than 20,000 non-nulls.

#### Save DataFrame to csv

* Save cleaned data to a csv file. This clean data will be used in the other notebook for further analysis.

### Lab Steps: Part Two

For the second part of the assessment, you will:

* Conduct EDA: visualization and statistical measures to understand the structure of the data.
* Recommend a set of manufacturers to consider as well as specific airplanes conforming to the client's request.
* Discuss the relationship between serious injuries/airplane damage incurred and at least two factors at play in the incident. You must provide supporting evidence (visuals, summary statistics, tables) for each claim you make.

* [Step 1](#dpPanel9Content)
* [Step 2](#dpPanel10Content)
* [Step 3](#dpPanel11Content)

#### Load in the Cleaned Data

* Load the saved csv file from Part One.

#### Explore Safety Metrics Across Models/Makes

Remember that the client is interested in separate recommendations for smaller airplanes and larger airplanes. Choose a passenger threshold of 20 and separate the plane types.

1. **Analyzing Makes:** Explore the human injury risk profile for small and larger makes:  
   1. Choose the 15 makes for each group possessing the lowest mean fatal/seriously injured fraction.
   2. Plot the mean fatal/seriously injured fraction for each of these subgroups side-by-side.
2. **Distribution of injury rates:** small makes
   1. Use a violinplot to look at the distribution of the fraction of passengers serious/fatally injured for small airplane makes. Just display makes with the 10 lowest mean serious/fatal injury rates.
3. **Distribution of injury rates**: large makes
   1. Use a stripplot to look at the distribution of the fraction of passengers seriously/fatally injured for large airplane makes. Just display makes with the 10 lowest mean serious/fatal injury rates.
4. **Evaluate the rate of aircraft destruction** for both small and large aircraft by make. Sort your results and keep the lowest 15.
5. **Provide a short discussion** in markdown on your findings for your summary statistics and plots:
   1. Make any recommendations for makes here based off of the destroyed fraction and fraction fatally/seriously injured.
   2. Comment on the calculated statistics and any corresponding distributions you have visualized.
6. **Analyze plane types**
   1. Plot the mean fatal/seriously injured fraction for both small and larger planes.
   2. Also provide a distributional plot of your choice for the fatal/seriously injured fraction by airplane type (stripplot, violin, etc).
   3. Filter plane types, ensuring that you have at least 10 individual examples in each model/make to average over.
   4. For smaller planes, limit your plotted results to the makes with the 10 lowest mean serious/fatal injury fractions.
7. **Discussion of Specific Airplane Types:** Discuss in markdown what you have found regarding fatal/seriously injured fraction of passengers for both small and large airplane models.

#### Exploring Other Variables

Investigate how other variables affect aircraft damage and injury. You must choose two factors out of the following but are free to analyze more:

* Weather Condition
* Engine Type
* Number of Engines
* Phase of Flight
* Purpose of Flight

For each factor, provide a discussion in markdown explaining your analysis with appropriate visualization/data summaries and interpret your findings.

### Submission and Grading Criteria

1. Review the rubric below for the grading criteria before submitting your assignment.
2. When you are ready to submit, click Start Assignment.
3. Upload your Cleaning and Data Analysis .ipynb files. Share a link to your GitHub repository in the comments section.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243671

Scraped At: 2026-05-14T21:05:14.888261
