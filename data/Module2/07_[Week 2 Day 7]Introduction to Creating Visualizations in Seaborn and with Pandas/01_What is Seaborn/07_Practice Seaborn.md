# Practice: Seaborn

# Practice: Seaborn

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Seaborn

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

In this practice, you will create three (3) scatterplots using the ‘penguins’ dataset. Each scatterplot will add more customizations to your visual to tell different stories.

### Resources

* [GitHub Repository (Seaborn Practice 1)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m6)

### Instructions

#### Step 1

Recreate the scatter plot image you see below using Seaborn. Use ‘flipper\_length\_mm’ on the x-axis and ‘body\_mass\_g’ on the y-axis. The dataset called ‘penguins’ has already been imported for you in the first cell.

![Scatter plot output of flipper length and body mass.](https://moringa.instructure.com/courses/1406/files/624802/download)

#### Step 2

Using the same code from Step 1, add an additional ‘hue’ argument and set that equal to the variable ‘species’.  You should get the image you see below displaying three distinct colors.

![Scatter plot output of flipper length and body mass with colors.](https://moringa.instructure.com/courses/1406/files/625253/download)

#### Step 3

Now add one more argument, ‘size’, and set it equal to the variable ‘bill\_length\_mm’.  Also, add an additional argument, ‘style’, and set that equal to the variable ‘species’.

### Solution

### Select for Solution

#### Step 1

```
# Import packages   
import matplotlib.pyplot as plt   
import seaborn as sns   
%matplotlib inline   
  
# Import data   
  
penguins = sns.load_dataset("penguins")  
  
# Create scatterplot   
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g')  
  
# Show the plot  
plt.show()
```

One nice thing about Seaborn is that many of their plots take the 'hue' argument, which effortlessly designates a category with colors.

#### Step 2

```
# Color by penguin species   
  
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species')  
  
# Show the plot  
plt.show()
```

#### Step 3

```
# Add size and style arguments to scatter plot    
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species',  
               size='bill_length_mm', style='species')  
  
# Show the plot  
plt.show()
```

**Expected Output:**

![Scatter plot output including size and style for species](https://moringa.instructure.com/courses/1406/files/624782/download)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243622

Scraped At: 2026-05-14T21:00:06.690258
