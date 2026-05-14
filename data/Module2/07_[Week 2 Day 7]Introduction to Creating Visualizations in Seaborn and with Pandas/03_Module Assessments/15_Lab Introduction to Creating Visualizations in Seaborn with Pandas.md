# Lab: Introduction to Creating Visualizations in Seaborn with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/625182/preview?) Lab: Introduction to Creating Visualizations in Seaborn and with Pandas

In this lab, you will use what you have learned in this lesson about the advanced visualization library Seaborn to generate plots that provide insight into the popular tips dataset.

In this lab, you will do the following:

* Create a boxplot using Seaborn.
* Label plots with appropriate axis labels and titles.
* Create data visualizations with Pandas.

### Tools and Resources

* [GitHub repository- Creating Visualizations in Seaborn with Pandas


  Links to an external site.](https://github.com/learn-co-curriculum/DS_Course0_Week1_Module6_SeabornPandas)
* Jupyter Notebook
* CodeGrade (for assignment submission)

### Instructions

### [Part 1: Seaborn](#dpPanel0)

We will use a randomly generated data set to practice using Seaborn. Begin by running the below code without change.

```
import numpy as np  
import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt  
%matplotlib inline  
  
# The seed must be 42 for the data to replicate  
seed = 42  
  
# Data  
data = np.random.normal(size=(20, 10)) + np.arange(10) / 2
```

#### Step 1

Create a boxplot and store the object returned in the variable boxplot1.

```
# CodeGrade step1  
# Replace None with your code  
  
boxplot1 = None
```

#### Step 2

Repeat Step 1 creating another boxplot, but now also call the boxplot object's set() method in order to set the title and axis labels as follows:

* X axis should be labeled 'X Label'
* Y axis should be labeled 'Y Label'
* Title should be labeled 'Example Boxplot'

```
# CodeGrade step2  
# Replace None with your code  
  
boxplot2 = None  
boxplot2.set(None)
```

#### Step 3

**Repeat Step 2**, this time also utilizing Seaborn to set the style to be 'darkgrid'. Still include title and axis labels.

```
# CodeGrade step3  
# Replace None with your code  
  
# Set style  
None  
  
# Plot  
boxplot3 = None  
boxplot3.set(None)
```

#### Step 4

Recreate the labeled boxplot that we made in Step 3:

* Utilizing Seaborn's context setting, adjust the size and font style of text so that it is more legible for presentations and large screen format.
* Use 'poster' from Seaborn's preconfigured options.

```
# CodeGrade step4  
# Replace None with your code  
  
# Context  
None  
  
# Plot  
boxplot4 = None  
boxplot4.set(None)
```

#### Step 5

You are now going to take a look at the canonical Seaborn Penguins dataset. This dataset contains biometric measurements and categorical information regarding three species of penguins.

Run this code without change:

```
# CodeGrade step0  
# Run this cell without changes  
  
penguins = pd.read_csv("penguins.csv")  
penguins.head()
```

Now use Seaborn to create a histogram of the 'body\_mass\_g' column with the following parameters:

* Context is set to 'talk'
* Color of the bars should distinguish male and female from each other
* The labels should be:  
  + **X Axis:** 'Body Mass (g)'
  + **Y Axis:** 'Number of Penguins'
  + **Title:** 'Penguin Mass Distribution by Sex'

```
# CodeGrade step5  
# Replace None with your code  
  
# Context  
None  
  
#Plot  
histplot1 = None  
histplot1.set(None)
```

#### Step 6

Create a scatter plot of the bill length (horizontal axis) vs. the bill depth (vertical axis), with:

* The context set to paper.
* Have the points color represent the sex.
* Have the points shape represent the species.
* Name the horizontal axis 'Bill Length (mm)', the vertical axis is 'Bill Depth, where the title is 'Scatterplot of Penguin Bill Sizes'.

```
sns.set_context('paper')  
scatterplot1 = sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="sex", style="species")  
scatterplot1.set(xlabel = 'Bill Length (mm)', ylabel='Bill Depth (mm)', title='Scatterplot of Penguin Bill Sizes')
```

```
# CodeGrade step6  
# Replace None with your code  
  
# Context  
None  
  
# Plot  
scatterplot1 = None  
scatterplot1.set(None)
```

### [Part 2: Pandas](#dpPanel1)

You are now going to take a look at the canonical iris dataset. This dataset is a classic multivariate dataset, which includes the sepal length, sepal width, petal length, and petal width for hundreds of samples of three species of the iris flower.

Begin by loading in the iris dataset. Run the cell without changes.

```
# CodeGrade step0  
# Run this cell without changes  
  
iris = pd.read_csv("iris.csv")  
iris.head()
```

#### Step 7

A primary question you might ask regarding this data is if there is any difference in average measurements across species? You can help answer this via a simple bar chart visual. In order to do so you must first create your aggregated data. You are interested in seeing how much the mean sepal width differs across the three species.

* X Axis should be labeled as 'Species'
* Y Axis should be labeled as 'Mean Sepal Width'
* Title should be labeled as 'Distribution of Sepal Width'

```
# CodeGrade step7  
# Replace None with your code  
  
# Create your grouped by means, should be a pandas series  
species_mean_sepal_width = iris.groupby('species').mean()['sepal_width']  
  
# Plot from the species_mean_width series  
barplot1 = species_mean_sepal_width.plot(kind='bar', title='Distribution of Sepal Width', ylabel='Mean Sepal Width')
```

#### Step 8

Utilize pandas plotting (.plot) to create a histogram plot to show the distribution of the 'sepal\_length' column separated and grouped by 'species'. You should end up with a chart showing three histograms, one on top of the other. You can accomplish this with one .plot() call.

```
# CodeGrade step8  
# Replace None with your code  
  
# Plot  
histplot2 = None
```

### Submission and Grading Criteria

1. Review the rubric below as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
3. When you are ready to submit, launch CodeGrade.
   * Click on + Create Submission. Upload your Jupyter notebook file for this lab.
   * For additional information on submitting assignments in CodeGrade: [Getting Started in CanvasLinks to an external site.


     Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
   * You can review your submission in CodeGrade and see your score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243633

Scraped At: 2026-05-14T21:01:10.874159
