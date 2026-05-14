# Technical Lesson: Matplotlib

# Technical Lesson: Matplotlib

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Matplotlib

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

This lesson will guide you through creating bar charts, histograms, and scatter plots using Python’s Matplotlib package. We'll break down the process step-by-step, making it easy for you to understand and apply these techniques to your own data analysis projects.

Throughout this lesson, we'll cover the following key topics:

1. **Bar chart** for qualitative data
2. **Histogram** for continuous data
3. **Scatter plot** for discrete data

When using Matplotlib for data visualization, you should keep the following considerations in mind:

1. Choosing the Appropriate Plot Type:
   * Consider the nature of your data and the insights you want to convey when selecting the plot type.
   * For qualitative or categorical variables, a bar chart is often suitable to compare and contrast different categories.
   * For a single continuous variable, a histogram is useful to visualize the distribution and identify patterns or anomalies.
   * For exploring the relationship between two continuous numeric variables, a scatter plot is commonly used.
   * Keep in mind that there are many other plot types available in Matplotlib, such as line plots, box plots, heatmaps, etc., which may be more appropriate depending on your specific data and analysis requirements.
2. Customization and Aesthetics:
   * Matplotlib provides a wide range of customization options to enhance the appearance and readability of your plots. Including but not limited to color, labels, line styles, font sizes, and more. Consultant the Matplotlib documentation for all customizations.
3. Interpretation and Insights:
   * After creating the plot, take time to interpret the visualization and extract meaningful insights from it. Is there a trend? pattern? outlier?

By keeping these considerations in mind, a student can effectively use Matplotlib to create informative and visually appealing plots, communicate insights effectively, and iterate on their visualizations to achieve the desired results.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Matplotlib.

[VIDEO LINK](https://player.vimeo.com/video/989668237?h=1bcf8dadc3)

### Instructions

### Part 1: Bar Chart for Qualitative Data

Suppose we have data on the favorite fruits of a group of people. Let's create a bar chart to visualize this qualitative data.

```
import matplotlib.pyplot as plt  
  
# Data  
fruits = ['Apple', 'Banana', 'Orange', 'Grape']  
counts = [25, 20, 15, 10]  
  
# Create a bar chart  
plt.figure(figsize=(6, 4))  
plt.bar(fruits, counts)  
  
# Add labels and title  
plt.xlabel('Fruit')  
plt.ylabel('Count')  
plt.title('Favorite Fruits')  
  
# Display the chart  
plt.show()
```

 
![Bar chart showing the count for favorite fruits](https://moringa.instructure.com/courses/1406/files/625124/download)

**Explanation:**

* We import the matplotlib.pyplot module and alias it as plt.
* We define the fruits list containing the categories and the counts list with the corresponding counts.
* We create a new figure with a specified size using plt.figure(figsize=(6, 4)).
* We create a bar chart using plt.bar(), passing the fruits and counts as arguments.
* We add labels for the x-axis and y-axis using plt.xlabel() and plt.ylabel(), respectively.
* We set a title for the chart using plt.title().
* Finally, we display the chart using plt.show().

### Part 2: Histogram for Continuous Data

Let's create a histogram to visualize the distribution of continuous data, such as the heights of students in a class.

```
import numpy as np  
import matplotlib.pyplot as plt  
  
# Generate random height data  
heights = np.random.normal(170, 10, 100)  
  
# Create a histogram  
plt.figure(figsize=(6, 4))  
plt.hist(heights, bins=20, edgecolor='black')  
  
# Add labels and title  
plt.xlabel('Height (cm)')  
plt.ylabel('Frequency')  
plt.title('Distribution of Student Heights')  
  
# Display the histogram  
plt.show()
```

 
![Histogram showing distribution of student heights](https://moringa.instructure.com/courses/1406/files/625198/download)

**Explanation:**

* We import the numpy module for generating random data and matplotlib.pyplot for plotting.
* We generate random height data using np.random.normal(), specifying the mean (170), standard deviation (10), and the number of samples (100).
* We create a new figure and use plt.hist() to create a histogram, passing the heights data and the number of bins (bins=20).
* We set the edgecolor to 'black' to outline the bins.
* We add labels and a title using plt.xlabel(), plt.ylabel(), and plt.title().
* We display the histogram using plt.show().

### Part 3: Scatter Plot for Two Discrete Variables

Let's create a scatter plot to visualize the relationship between two discrete variables, such as the number of hours studied and the corresponding test scores.

```
import matplotlib.pyplot as plt  
  
# Data  
hours_studied = [2, 3, 5, 1, 4, 2, 6, 3, 4, 5]  
test_scores = [85, 92, 98, 78, 95, 88, 100, 90, 96, 99]  
  
# Create a scatter plot  
plt.figure(figsize=(6, 4))  
plt.scatter(hours_studied, test_scores)  
  
# Add labels and title  
plt.xlabel('Hours Studied')  
plt.ylabel('Test Score')  
plt.title('Hours Studied vs. Test Score')  
  
# Display the scatter plot  
plt.show()
```

 
![Scatter plot showing hours studied versus test scores](https://moringa.instructure.com/courses/1406/files/625115/download)

**Explanation:**

* We define the hours\_studied and test\_scores lists containing the data for each variable.
* We create a new figure and use plt.scatter() to create a scatter plot, passing hours\_studied and test\_scores as arguments.
* We add labels for the x-axis and y-axis using plt.xlabel() and plt.ylabel(), respectively.
* We set a title for the scatter plot using plt.title().
* We display the scatter plot using plt.show().

### Summary

These examples demonstrate how to use Matplotlib to create different types of plots for various data types. You can customize the plots further by modifying colors, markers, font sizes, and other properties using the appropriate Matplotlib functions and parameters.

Remember to explore the Matplotlib documentation and examples to learn more about the extensive capabilities of the library for creating visualizations in Python.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243565

Scraped At: 2026-05-14T20:53:48.586442
