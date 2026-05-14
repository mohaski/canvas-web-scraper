# Technical Lesson: Data Visualization with Pandas

# Technical Lesson: Data Visualization with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Data Visualization with Pandas

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

Before we dive into the data visualization in Pandas part of the lesson, it would be a good idea to get a quick introduction to Matplotlib's style module. Matplotlib comes with a number of predefined styles to customize the plots. These styles generally change the look of plots by changing color maps, line styles, backgrounds etc. Because Pandas is built on Matplotlib for visualizations, this will change the style of our Pandas graphs as we'll see below.

The videos below will guide you through each step of the technical lesson. You can follow along with the videos to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Data Visualization with Pandas.

[VIDEO LINK](https://player.vimeo.com/video/1006093612?h=38786e3ec1)

[VIDEO LINK](https://player.vimeo.com/video/1006093703?h=7ab11cae83)

We can use plt.style.available to see a list of predefined styles available in Matplotlib.

```
import matplotlib.pyplot as plt  
%matplotlib inline  
plt.rcParams['figure.figsize'] = (10, 10)  
plt.style.available
```

**Output:**

```
['Solarize_Light2',  
 '_classic_test_patch',  
 'bmh',  
 'classic',  
 'dark_background',  
 'fast',  
 'fivethirtyeight',  
 'ggplot',  
 'grayscale',  
 'seaborn',  
 'seaborn-bright',  
 'seaborn-colorblind',  
 'seaborn-dark',  
 'seaborn-dark-palette',  
 'seaborn-darkgrid',  
 'seaborn-deep',  
 'seaborn-muted',  
 'seaborn-notebook',  
 'seaborn-paper',  
 'seaborn-pastel',  
 'seaborn-poster',  
 'seaborn-talk',  
 'seaborn-ticks',  
 'seaborn-white',  
 'seaborn-whitegrid',  
 'tableau-colorblind10']
```

So this provides us with a list of styles available. To use a style, we simply give the command plt.style.use(<style name>). Let's use ggplot for now and see how it changes the default style. Feel free to try other styles and see how they impact the look and feel of the plots.

```
plt.style.use('ggplot')
```

We’ll practice creating visualizations in Pandas using a randomly generated data set. The DataFrame.plot() method allows us to plot a number of different kinds of plots. We can select which plot we want to use by specifying the kind parameter. Here is a complete list from the [Pandas documentation


Links to an external site.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html):

**Output:**

```
kind : str  
  
‘line’ : line plot (default)  
‘bar’ : vertical bar plot  
‘barh’ : horizontal bar plot  
‘hist’ : histogram  
‘box’ : boxplot  
‘kde’ : Kernel Density Estimation plot  
‘density’ : same as ‘kde’  
‘area’ : area plot  
‘pie’ : pie plot  
‘scatter’ : scatter plot  
‘hexbin’ : hexbin plot
```

Now let's get to data visualization with Pandas.

* [Step 1: Building a Synthetic Temporal DataFrame](#dpPanel0Content)
* [Step 2: Inspecting the Data Visually](#dpPanel1Content)
* [Step 3: Creating a Scatter Plot](#dpPanel2Content)
* [Step 4: Choosing the Plot Kind](#dpPanel3Content)
* [Step 5: Performing Modifications](#dpPanel4Content)
* [Step 6: Creating a Box Plot](#dpPanel5Content)
* [Step 7: Creating a Histogram](#dpPanel6Content)
* [Step 8: Creating the Kernel Density Plot](#dpPanel7Content)

### Step 1: Building a Synthetic Temporal DataFrame

Let's build a synthetic temporal DataFrame with the following steps:

* Data frame with three columns A, B, and C
* For data in each column, we will use a random number generator to generate 365 numbers (to reflect days in a year) using np.random.randn()
* Using NumPy's .cumsum() (cumulative sum) method, we will cumulatively sum the generated random numbers in each column
* Offset column B by +25 and column C by -25 with respect to Column A, which will remain unchanged
* Using pd.date\_range(), set the index to be every day in 2018 (starting from 1st of January)

We'll also set a seed for controlling the randomization, allowing us to reproduce the data.

It is always a good idea to set a random seed when dealing with probabilistic outputs so that they can be replicated.

```
import pandas as pd  
import numpy as np  
  
np.random.seed(777)  
  
data = pd.DataFrame({'A':np.random.randn(365).cumsum(),  
                    'B':np.random.randn(365).cumsum() + 25,  
                    'C':np.random.randn(365).cumsum() - 25},   
                     index = pd.date_range('1/1/2018', periods = 365))  
data.head()
```

**Output:**

```
ABC2018-01-01-0.46820925.435990-22.9979432018-01-02-1.29103426.479220-22.6734042018-01-03-1.35641425.832356-21.6690272018-01-04-2.06977626.456703-21.4083102018-01-05-1.16342525.864281-22.685208
```

### Step 2: Inspecting the Data Visually

Now we have a dataset with three columns that we can call time-series. Let's inspect our data visually. To plot this data we can simply use the .plot() method on the DataFrame.

```
data.plot();
```

**Output:**

![Plot of the three columns of data from the dataset](https://moringa.instructure.com/courses/1406/files/624815/download)

 So, we didn't have to define our canvas, axes or labels etc. It automatically set the datetime index as the x axis and created a legend labeling the lines with the column names. This is where pandas really shines.

The DataFrame.plot() method is just a simple wrapper around plt.plot() that draws line plots. So when we call data.plot(), we get a line graph of all the columns in the data frame with labels.

Also, notice how this plot looks different in terms of look and feel. This is because of the style we used earlier.

### Step 3: Creating a Scatter Plot

Let's try and create a scatter plot that takes the A and B columns of data. We pass in 'scatter' to the kind parameter to change the plot type. Also note, putting a semicolon at the end of plotting function mutes any extra text out.

```
data.plot('A', 'B', kind='scatter');
```

**Output:**

![Scatter plot output of columns A and B of data.](https://moringa.instructure.com/courses/1406/files/624736/download)

### Step 4: Choosing the Plot Kind

We can also choose the plot kind by using the methods dataframe.plot.<kind> instead of passing the kind argument. We'll perform the following steps:Now create another scatter plot with points varying in color and size. We'll perform the following steps:

* Use df.plot.scatter() and pass in columns 'A' and 'C'.
* Set the color c and size s of the data points to change based on the value of column B.
* Choose the color palette by passing a string into the parameter colormap.

```
data.plot.scatter('A', 'C',   
                  c = 'B',  
                  s = data['B'],  
                  colormap = 'viridis');
```

**Output:**

![Scatter Plot output of columns A and C based on the value of column B using a colormap](https://moringa.instructure.com/courses/1406/files/624772/download)

Here, A and C columns plotted against one another with graduating color and changing the size and based on the values of the 'B' column.

### Step 5: Performing Modifications

df.plot.scatter() returns a matplotlib.axes.\_subplot object so we can perform modification on these objects just like we would do in Matplotlib plots. Here we'll change the aspect ratio for the scatter plot generated above but otherwise keep it the same, and add a title using axes properties.

* Set the aspect to ‘equal’
* Set the title to ‘Manipulating Pandas plot objects in Matplotlib

```
ax = data.plot.scatter('A', 'C',   
                        c = 'B',  
                        s = data['B'],  
                        colormap = 'viridis');  
ax.set_aspect('equal')  
ax.set_title('Manipulating Pandas plot objects in matplotlib');
```

**Output:**

**![Scatter Plot output with the aspect set to ‘equal’ and the title to ‘Manipulating Pandas plot objects in matplotlib&#34;](https://moringa.instructure.com/courses/1406/files/625024/download)**

Setting the aspect ratio to 'equal' allows the viewer to easily see that the range of series A (x axis) is smaller than the range of series C (y axis).

### Step 6: Creating a Box Plot

Now we'll create a boxplot of the three groups by simply using data.plot.box();.

```
# Box Plots  
data.plot.box();
```

**Output:**

 
![Box plot output of the three groups](https://moringa.instructure.com/courses/1406/files/624804/download)

### Step 7: Creating a Histogram

Next we'll create a histogram of the three groups, but set the alpha to 0.7 in order to inspect the distribution overlap.

```
# Histograms   
# Setting alpha level to inspect distribution overlap  
data.plot.hist(alpha = 0.7); 
```

**Output:**

![Histogram output of the three groups with alpha set to 0.7](https://moringa.instructure.com/courses/1406/files/624810/download)

### Step 8: Creating the Kernel Density Plot

Last, we'll create the Kernel Density plot of the three groups, where the title is ‘KDE with bandwidth estimator silverman’. N.B. ‘scott’ is the default bandwidth, so we’re changing it to ‘silverman’.

```
# Kernel Density Estimate plots  
# Useful for visualizing an estimate of a variable's probability density function with bw_method set to silverman   
ax = data.plot.kde(bw_method='silverman');  
ax.set_title('KDE with bandwith estimator silverman');
```

**Output:**

![Kernel density plot output of the three groups with the title as ‘KDE with bandwidth estimator silverman’.](https://moringa.instructure.com/courses/1406/files/624832/download)

#### Considerations

A common error is to try to use a plot that is not the correct one for that type of data. For example, a bar chart is used for qualitative or categorical data whereas a histogram is used for quantitative or numeric data.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243630

Scraped At: 2026-05-14T21:00:49.541906
