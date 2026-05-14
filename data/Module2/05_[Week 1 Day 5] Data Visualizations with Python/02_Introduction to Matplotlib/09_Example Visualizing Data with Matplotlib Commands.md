# Example: Visualizing Data with Matplotlib Commands

# Example: Visualizing Data with Matplotlib Commands

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Example: Visualizing Data with Matplotlib Commands

Icon Progress Bar (browser only)

5 min read

Let’s look at some examples of visualizing data using Matplotlib commands. We have looked at the basic syntax in creating a histogram and scatter plot. We will build on the basic syntax of both visuals in this section and introduce the syntax of two more visual types.

### Histograms

You can use the plt.hist() function in matplotlib to draw a histogram while passing in values from the required data variable. Histograms are best when visualizing one continuous numeric variable. The below code using plt.hist() to visualize the retirement ages of 200 people:

```
# import numpy and matplotlib  
import numpy as np  
import matplotlib.pyplot as plt   
  
# Set seed for reproducability  
np.random.seed(100)  
  
# Generate a data set of 200 retirement age values  
x = 5*np.random.randn(200) + 65  
  
#Plot the histogram with hist() function  
plt.hist(x, bins = 10, edgecolor='black')  
  
plt.xlabel('Retirement Age')  
plt.ylabel('Frequency of Values')  
plt.title('Histograms in Matplotlib')  
plt.show()
```

![Matplotlib histogram example showing retirement age and frequency of values](https://moringa.instructure.com/courses/1406/files/625119/download)

The y-axis tells you how often a certain range of numbers appears in the data set. From the histogram, you can see that there are a lot of people who retire around 65. There are significantly fewer people who retire at 75 and even fewer people who retire at 50.

**The bins Argument**

Say you want to change the range of values that define the groups of a histogram. You can optionally pass the bins argument to set the number of groups. In the plot above, the data have been separated into 10 groups. Check out what happens when you change the number of bins to 5:

```
plt.hist(x, bins=5, edgecolor='black')  
plt.xlabel('Retirement Age')  
plt.ylabel('Frequency of Values')  
plt.title('Histograms in Matplotlib')  
plt.show()
```

![Matplotlib histogram example showing retirement age and frequency of values with 5 bins](https://moringa.instructure.com/courses/1406/files/624726/download)

Note the scale of the y-axis and the width of the bars compared to the histogram using 10 bins. The granularity of the bins can be changed according to your specific analytical needs and the amount of data available. For example, if you had 50 data points, you would not want to use 500 bins.

### Scatter Plots

Let’s expand the data above to add another continuous variable, life\_expectancy, on the y-axis to create a scatter plot. Scatter plots are best when viewing to continuous numeric variables to get a relationship between them.

```
# Set seed for reproducability   
np.random.seed(100)   
# Generate retirement age and life expectancy data   
retirement_age = 5 * np.random.randn(200) + 65   
life_expectancy = np.random.randint(75, 101, size=200)   
  
# Plot the scatter plot   
plt.scatter(retirement_age, life_expectancy, c='blue', alpha=0.7) # c is color alpha is transparency   
  
# Add labels   
plt.xlabel('Retirement Age')   
plt.ylabel('Life Expectancy')   
plt.title('Relationship Between Retirement Age and Life Expectancy (Simulated Data)')  
plt.show()
```

 
![Matplotlib scatter plot example showing the relationship between retirement age and life expectancy](https://moringa.instructure.com/courses/1406/files/625129/download)

We can see that the two continuous variables, retirement\_age and life\_expectancy, have little to no relationship between each other meaning the age someone retires has no influence on their life expectancy. Scatter plots are beneficial in this way where we can see the relationship between two variables.

### Bar Charts

Bar charts (also called "bar graphs") are one of the most common plot types for showing comparisons across data. Bar graphs allow comparisons across categories by presenting categorical data as rectangular bars with heights or lengths proportional to the values that they represent. One axis of the graph shows the specific categories being compared and the other axis represents a value scale. The bars can be plotted vertically or horizontally. When the bars are plotted vertically, it is usually referred to as a "column graph." Some examples of bar graphs are shown below.

 
![Matplotlib example showing both vertical and horizontal bar chart formats](https://moringa.instructure.com/courses/1406/files/625194/download)

Matplotlib features a number of handy plotting functions. Matplotlib's .bar() and .barh() functions can be used to draw constant width vertical and constant height horizontal bar graphs for a simple sequence of x, y values.

Let’s look at the code for creating a vertical bar graph of website traffic data that occurs for each day of the week:

```
import matplotlib.pyplot as plt  
  
np.random.seed(100)  
  
# Simulate website traffic data for each day of the week  
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]  
website_traffic = [1000, 1200, 1500, 1800, 2000, 1300, 800]  
  
# Create the bar chart  
plt.bar(days_of_week, website_traffic)  
  
# Add labels and title  
plt.xlabel("Day of the Week")  
plt.ylabel("Website Traffic")  
plt.title("Website Traffic by Day of the Week (Simulated Data)")  
  
# Customize x-axis labels for better readability (optional)  
plt.xticks(rotation=45)  # Rotate x-axis labels for better viewing  
  
plt.show()
```

 
![Matplotlib example bar chart showing website traffic by day of the week](https://moringa.instructure.com/courses/1406/files/625088/download)

**The difference between bar charts and histograms**

It is important to distinguish bar graphs from histograms. Bar graphs show category-specific values and consist of two variables. Histograms show counts of how frequently a given range of values occurs in a data set. Take a look at the examples below and think about how they are different:

 
![Side-by-side comparison of a bar chart and a histogram](https://moringa.instructure.com/courses/1406/files/625123/download)

### Line Graphs

Line graphs are a staple visualization tool in Python, especially for data science and time series analysis. They're ideal for visualizing continuous numeric variables plotted against another variable (often numeric or categorical) to show trends or relationships over time. Let’s simulate website traffic over 20 weeks using the code below:

```
import matplotlib.pyplot as plt  
import numpy as np  
  
np.random.seed(100)  
  
# Simulate website traffic data for 30 weeks  
weeks = np.arange(1, 21)  # Create an array of weeks (1 to 20)  
website_traffic = np.random.randint(1000, 5000, size=20)  # Random traffic between 1000 and 5000  
  
# Create the line graph  
plt.plot(weeks, website_traffic)  
  
# Add labels and title  
plt.xlabel("Week Number")  
plt.ylabel("Website Traffic")  
plt.title("Website Traffic Over 20 Weeks (Simulated Data)")  
  
# Customize x and y-axis for better readability (optional)  
plt.xticks(np.arange(min(weeks), max(weeks)+1))  # Display all week numbers on x-axis  
plt.yticks(np.arange(min(website_traffic), max(website_traffic)+500, 1000))  # Adjust y-axis ticks with increments of 1000  
  
plt.grid(True)  # Add grid lines for better readability  
  
plt.show()
```

 
![Matplotlib line graph example showing website traffic over 20 weeks](https://moringa.instructure.com/courses/1406/files/625113/download)

By looking at this visual you can see that weeks 6 and 11 have the lowest website traffic compared to other weeks.

These are examples of the four main types of visuals. There are tons of visual types that can be explored by using the [Matplotlib online documentation


Links to an external site.](https://matplotlib.org/stable/index.html).

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243561

Scraped At: 2026-05-14T20:53:24.374532
