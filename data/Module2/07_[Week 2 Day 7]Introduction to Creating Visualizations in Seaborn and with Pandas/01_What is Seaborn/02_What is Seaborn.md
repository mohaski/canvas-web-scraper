# What is Seaborn?

# What is Seaborn?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What is Seaborn?

Icon Progress Bar (browser only)

6 min read

**Seaborn** is a popular Python data visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. Seaborn aims to make it easy to create complex visualizations with just a few lines of code, while still allowing for deep customization.

Watch the videos below to learn more about Seaborn.

### Part One: Features of Seaborn

[VIDEO LINK](https://player.vimeo.com/video/1006093359?h=f9873c62c3)

### Part Two: Seaborn vs. Matplotlib, Common Seaborn Commands

[VIDEO LINK](https://player.vimeo.com/video/1006093410?h=68c8bf7e27)

### Part Three: Examples of Visualizations with Seaborn

[VIDEO LINK](https://player.vimeo.com/video/1006093456?h=8c4a0cbc86)

### Key Features and Benefits of Seaborn

* **Built on Matplotlib with Beautiful Default Styles:** 
  + Seaborn is built on Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics. It comes with several built-in themes and color palettes that make creating visually appealing plots straightforward.
* **Statistical Functions and High-Level Abstraction:** 
  + It includes built-in statistical functions for creating complex visualizations and provides high-level functions for common plot types like bar plots, violin plots, and scatter plots, making it accessible for beginners and powerful for advanced users.
* **DataFrame Support and Faceted Plots:** 
  + Seaborn works seamlessly with Pandas DataFrames, allowing for direct plotting from DataFrames. It simplifies the creation of faceted plots, which show different subsets of data side by side, useful for comparing distributions across subsets.
* **Customizability and Integration with Matplotlib:** 
  + While Seaborn’s default settings are designed for quick and easy visualizations, it allows extensive customization. Seaborn plots can be fine-tuned using Matplotlib commands, providing additional flexibility.
* **User-Friendly and Practical:** 
  + Designed to be user-friendly, Seaborn’s features and functionalities are practical for everyday data analysis tasks, helping users uncover patterns and insights efficiently.

### Seaborn vs. Matplotlib

Below are some comparisons and differences between Matplotlib and Seaborn.

#### **Ease of Use and Aesthetics**

* **Seaborn:** Provides high-level interfaces and beautiful default styles, making it easier to create complex and aesthetically pleasing plots with less code.
* **Matplotlib:** Requires more code and customization to achieve the same level of aesthetics and complexity. It is more flexible but less intuitive for beginners.

#### **Statistical Plotting**

* **Seaborn:** Includes built-in support for statistical plots such as regression plots, box plots, and violin plots. It simplifies the process of visualizing statistical relationships.
* **Matplotlib:** Does not have built-in statistical plotting functions. Users need to manually create these plots, which can be more time-consuming and complex.

#### **Integration with Pandas DataFrames**

* **Seaborn:** Works seamlessly with Pandas DataFrames, allowing direct plotting from DataFrame columns. It is designed to handle data structures used in data analysis.
* **Matplotlib:** Requires data to be converted into NumPy arrays or lists for plotting, which can add extra steps when working with Pandas DataFrames.

Recall how to create a scatter plot using Matplotlib.  Below are two visuals, on the left a scatter plot of height vs weight created in Matplotlib and on the right the same visual using Seaborn.  Take note of the similarities and differences.

![Comparison of a scatterplot with Matplotlib versus Seaborn](https://moringa.instructure.com/courses/1406/files/624798/download)

### How Does Seaborn Work?

#### The Code Behind Seaborn

Seaborn is built on top of Matplotlib, leveraging its foundational capabilities to offer a higher-level, more intuitive interface for creating attractive and informative statistical graphics. To use Seaborn effectively, you need to import both Seaborn and Matplotlib packages. Seaborn’s documentation provides extensive information on various customizations and functionalities, allowing users to tailor their visualizations to specific needs and aesthetic preferences.

Below is the coding cell that imports both the Matplotlib and Seaborn packages.  Note that the industry standard alias for the Seaborn package is sns.

```
   import seaborn as sns  
   import matplotlib.pyplot as plt  
   %matplotlib inline
```

After importing the Seaborn package, you can refer to the table below to choose the right command based on the type of visual you are creating.

### Examples of Seaborn

The examples below use several built-in data frames that can be loaded within a Python notebook (you do not need to upload a data file!).

#### Simple Univariate Boxplot

Below is a boxplot of a single continuous numeric variable, total\_bill amount.  This visual can show the spread of the data within that column and a statistical summary (with the median being the center bold line).

```
import seaborn as sns  
  
tips = sns.load_dataset('tips') # Seaborn comes prepackaged with several different datasets that are great for visualizing!  
  
boxplot = sns.boxplot(data=tips["total_bill"])
```

![Boxplot of a single continuous numeric variable, total\_bill amount](https://moringa.instructure.com/courses/1406/files/624819/download)

#### Boxplot Grouped by Categorical Variable

This boxplot can further be broken down into a single boxplot for each day of the week.  What main takeaway do you gather about the total bill amount across each day of the week?

```
sns.boxplot(x="day", y="total_bill", data=tips)
```

![Data grouped by categorical variable and broken down into a single boxplot for each day of the week.](https://moringa.instructure.com/courses/1406/files/624785/download)

#### Scatter plot

Using the same tips dataset above let’s make a scatterplot.

```
import seaborn as sns  
import matplotlib.pyplot as plt  
  
# Load the built-in 'tips' dataset  
tips = sns.load_dataset('tips')  
  
# Create a scatter plot  
plt.figure(figsize=(10, 6))  
sns.scatterplot(data=tips, x='total_bill', y='tip')  
plt.title('Scatter Plot of Total Bill vs. Tip')  
plt.xlabel('Total Bill')  
plt.ylabel('Tip')  
plt.show()
```

![Seaborn scatterplot of total bill versus tip](https://moringa.instructure.com/courses/1406/files/624806/download)

### Conceptualization: Seaborn Commands

Seaborn plot type with description and command

| Plot Type | Seaborn Command | Description |
| --- | --- | --- |
| Scatter Plot | sns.scatterplot() | Creates a scatter plot to visualize the relationship between two continuous variables. |
| Line Plot | sns.lineplot() | Creates a line plot to visualize the trend of a continuous variable over a categorical variable. |
| Bar Plot | sns.barplot() | Creates a bar plot to compare categorical variables. |
| Count Plot | sns.countplot() | Creates a bar plot to show the count of observations in each category. |
| Box Plot | sns.boxplot() | Creates a box plot to visualize the distribution of a continuous variable across categories. |
| Violin Plot | sns.violinplot() | Creates a violin plot to visualize the distribution of a continuous variable across categories, showing the probability density. |
| Strip Plot | sns.stripplot() | Creates a scatter plot where one variable is categorical, showing the individual observations. |
| Swarm Plot | sns.swarmplot() | Similar to a strip plot, but the points are adjusted to avoid overlapping. |
| Histogram | sns.histplot() | Creates a histogram to visualize the distribution of a single continuous variable. |
| Kernel Density Estimation (KDE) Plot | sns.kdeplot() | Creates a smooth estimate of the univariate or bivariate distribution using kernel density estimation. |
| Heatmap | sns.heatmap() | Creates a heatmap to visualize a matrix of values as colors. |
| Pair Plot | sns.pairplot() | Creates a grid of scatter plots to visualize pairwise relationships in a dataset. |
| Joint Plot | sns.jointplot() | Creates a plot that combines a scatter plot and marginal univariate distributions (histogram or KDE). |
| Facet Grid | sns.FacetGrid() | Creates a grid of plots based on different subsets of the data, useful for visualizing relationships across multiple variables. |
| Regression Plot | sns.regplot() | Creates a scatter plot with a regression line to visualize the relationship between two variables. |
| Residual Plot | sns.residplot() | Creates a plot to visualize the residuals of a linear regression model. |
| Category Plot | sns.catplot() | A figure-level function that creates a grid of plots based on categorical variables, using various plot types (e.g., bar, box, violin). |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243616

Scraped At: 2026-05-14T20:59:34.231439
