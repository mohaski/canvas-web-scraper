# Practice: Data Visualization with Pandas

# Practice: Data Visualization with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Data Visualization with Pandas

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

In this practice, you will work on creating different types of data visualizations using pandas and the Iris dataset. You will create a bar chart, scatter plot, box plot, and histogram, and learn how to customize the plots using functions like set\_aspect, set\_title, and other modifications.

### Resources

* [GitHub Repository (Practice 2- Data Visualizations with Pandas)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m6)

### Instructions

1. **Import the necessary libraries**:  
   1. pandas as pd
   2. matplotlib.pyplot as plt
   3. seaborn as sns
2. **Load the Iris dataset into a pandas DataFrame**:
   1. Use the `sns.load\_dataset('iris')` function to load the dataset.
3. **Create a bar chart**:
   1. Use the `value\_counts()` function to count the number of samples for each species.
   2. Create a bar chart using the `plot(kind='bar')` function.
   3. Set the title of the plot using `set\_title('Number of Samples per Species')`.
   4. Label the x-axis as 'Species' and the y-axis as 'Count'.
   5. Rotate the x-tick labels by 45 degrees using `plt.xticks(rotation=45)`.
4. **Create a scatter plot**:
   1. Create a scatter plot using the `plot(kind='scatter', x='sepal\_length', y='sepal\_width')` function.
   2. Set the title of the plot using `set\_title('Sepal Length vs. Sepal Width')`.
   3. Label the x-axis as 'Sepal Length' and the y-axis as 'Sepal Width'.
   4. Use `set\_aspect('equal')` to set the aspect ratio of the plot to be equal.
5. **Create a box plot**:
   1. Create a box plot using the `boxplot(column=['sepal\_length', Projects 0 'sepal\_width', 'petal\_length', 'petal\_width'], by='species')` function.
   2. Set the title of the plot using `set\_title('Box Plot of Iris Measurements')`.
   3. Label the y-axis as 'Measurement (cm)'.
   4. Rotate the x-tick labels by 45 degrees using `plt.xticks(rotation=45)`.
6. **Create histograms**:
   1. Create a histogram for each feature (sepal\_length, sepal\_width, petal\_length, petal\_width) using the `hist()` function.
   2. Set the number of bins to 20 using the `bins` parameter.
   3. Set the title of each plot using `set\_title()` with an appropriate title for each feature.
   4. Label the x-axis with the feature name and the y-axis as 'Frequency'.
   5. Adjust the layout of the subplots using `plt.tight\_layout()`.
7. **Display all the plots using `plt.show()`**

### Solution

### [Select for Solution](#dpPanel0)

#### Step 1

```
Import necessary libraries  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns
```

#### Step 2

```
# Load the Iris dataset  
iris_data = sns.load_dataset('iris')
```

#### Step 3

```
# Create a bar chart  
species_counts = iris_data['species'].value_counts()  
species_counts.plot(kind='bar')  
plt.title('Number of Samples per Species')  
plt.xlabel('Species')  
plt.ylabel('Count')  
plt.xticks(rotation=45)  
plt.show()
```

**Expected Output:**

![Bar chart output of iris species](https://moringa.instructure.com/courses/1406/files/624767/download)

#### Step 4

```
# Create a scatter plot  
iris_data.plot(kind='scatter', x='sepal_length', y='sepal_width')  
plt.title('Sepal Length vs. Sepal Width')  
plt.xlabel('Sepal Length')  
plt.ylabel('Sepal Width')  
plt.gca().set_aspect('equal')  
plt.show()
```

**Expected Output:**

![Scatter plot output of iris sepal length versus sepal width](https://moringa.instructure.com/courses/1406/files/625137/download)

#### Step 5

```
# Create a box plot  
iris_data.boxplot(column=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], by='species')  
plt.title('Box Plot of Iris Measurements')  
plt.ylabel('Measurement (cm)')  
plt.xticks(rotation=45)  
plt.show()
```

**Expected Output:**

![Box plot output of iris data grouped by species](https://moringa.instructure.com/courses/1406/files/624800/download)

#### Steps 6 and 7

```
# Create histograms  
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  
axs = axs.flatten()  
  
for i, feature in enumerate(['sepal_length', 'sepal_width', 'petal_length', 'petal_width']):  
    axs[i].hist(iris_data[feature], bins=20)  
    axs[i].set_title(f'Histogram of {feature}')  
    axs[i].set_xlabel(feature)  
    axs[i].set_ylabel('Frequency')  
  
plt.tight_layout()  
plt.show()
```

**Expected Output:**

![Histogram outputs for each iris feature: sepal length, sepal width, petal length, and petal width](https://moringa.instructure.com/courses/1406/files/624715/download)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243631

Scraped At: 2026-05-14T21:00:57.315412
