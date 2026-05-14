# Technical Lesson: Seaborn

# Technical Lesson: Seaborn

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Seaborn

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

In this lesson, we'll create a bar chart for qualitative data, a histogram for continuous data, and a scatter plot for two discrete variables. If you have completed our Data Visualizations with Python module, these datasets will look familiar!

Here is a video walkthrough of the technical lesson steps that follow:

[VIDEO LINK](https://player.vimeo.com/video/1006093502?h=c907952f2b)

### Visualizations with Seaborn

* [Part 1: Bar Chart for Qualitative Data](#dpPanel0Content)
* [Part 2: Histogram for Continuous Data](#dpPanel1Content)
* [Part 3: Scatter Plot for Two Discrete Variables](#dpPanel2Content)

### Part 1: Bar Chart for Qualitative Data

Suppose we have data on the favorite fruits of a group of people. Let's create a bar chart to visualize this qualitative data.

```
# Libraries  
import seaborn as sns  
import matplotlib.pyplot as plt  
  
# Data  
fruits = ['Apple', 'Banana', 'Orange', 'Grape']  
counts = [25, 20, 15, 10]  
  
# Create a bar chart  
sns.set(style="whitegrid")  
ax = sns.barplot(x=fruits, y=counts)  
  
# Add labels and title  
ax.set(xlabel='Fruit', ylabel='Count', title='Favorite Fruits')  
  
# Display the chart  
plt.show()
```

**Output:**

**![Bar chart with seaborn of favorite fruits](https://moringa.instructure.com/courses/1406/files/624809/download)**

**Explanation:**

* We set the style of the plot using sns.set(style="whitegrid") to have a white background with gridlines.
* We use sns.barplot() to create a bar chart, passing the fruits and counts data as the x and y parameters, respectively.
* We add labels for the x-axis, y-axis, and title using the set() method of the plot object.
* Finally, we display the chart using plt.show().

### Part 2: Histogram for Continuous Data

Let's create a histogram to visualize the distribution of a continuous variable, such as the heights of students in a class.

```
# Generate random height data  
heights = np.random.normal(170, 10, 100)  
  
# Create a histogram  
sns.set(style="darkgrid")  
ax = sns.histplot(heights, kde=True)  
  
# Add labels and title  
ax.set(xlabel='Height (cm)', ylabel='Frequency', title='Distribution of Student Heights')  
  
# Display the histogram  
plt.show()
```

**Output:**

![Histogram with seaborn of the distribution of student heights](https://moringa.instructure.com/courses/1406/files/624822/download)

**Explanation:**

* We generate random height data using np.random.normal(), specifying the mean (170), standard deviation (10), and the number of samples (100).
* We set the style of the plot using sns.set(style="darkgrid") to have a dark background with gridlines.
* We use sns.histplot() to create a histogram, passing the heights data and setting kde=True to overlay a kernel density estimate.
* We add labels and a title using the set() method of the plot object.
* Finally, we display the histogram using plt.show().

### Part 3: Scatter Plot for Two Discrete Variables

Let's create a scatter plot to visualize the relationship between two discrete variables, such as the number of hours studied and the corresponding test scores.

```
# Data  
hours_studied = [2, 3, 5, 1, 4, 2, 6, 3, 4, 5]  
test_scores = [85, 92, 98, 78, 95, 88, 100, 90, 96, 99]  
  
# Create a scatter plot  
sns.set(style="whitegrid")  
ax = sns.scatterplot(x=hours_studied, y=test_scores)  
  
# Add labels and title  
ax.set(xlabel='Hours Studied', ylabel='Test Score', title='Hours Studied vs. Test Score')  
  
# Display the scatter plot  
plt.show()
```

**Output:**

![Scatter plot with seaborn of hours studied versus test scores](https://moringa.instructure.com/courses/1406/files/625138/download)

**Explanation:**

* We define the hours\_studied and test\_scores lists containing the data for each variable.
* We set the style of the plot using sns.set(style="whitegrid") to have a white background with gridlines.
* We use sns.scatterplot() to create a scatter plot, passing hours\_studied and test\_scores as the x and y parameters, respectively.
* We add labels and a title using the set() method of the plot object.
* Finally, we display the scatter plot using plt.show().

### Summary

These examples demonstrate how to use Seaborn to create different types of plots for various data types. Seaborn provides a simple and intuitive interface for creating visually appealing and informative visualizations.

Remember to explore the Seaborn documentation and examples to learn more about the extensive customization options and additional plot types available in the library.

The main challenges with using Seaborn for data visualization in Python would be understanding the different types of plots available and when to use them, as well as navigating the various customization options to create effective and visually appealing plots that clearly communicate the insights from the data. With data visualizations, unless otherwise stated, there is a lot of latitude on which parameters one decided to change (e.g., the color scheme).

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243621

Scraped At: 2026-05-14T21:00:00.947928
