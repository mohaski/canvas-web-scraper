# Practice: Matplotlib

# Practice: Matplotlib

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Matplotlib

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

Suppose you are a junior data scientist working for a business and you are given a sales data set that has the following variables: date of sale, product category, quantity sold, and revenue. Your boss asks you to create visualizations for the data to better understand the company’s sales.

### Resources

* [GitHub Repository


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m4)

### Instructions

* [Step 1](#dpPanel0Content)
* [Step 2](#dpPanel1Content)
* [Step 3](#dpPanel2Content)
* [Step 4](#dpPanel3Content)
* [Step 5](#dpPanel4Content)

### Step 1

Import the appropriate libraries and create the data given below.

```
# import germane libraries  
  
# data  
data = pd.DataFrame({  
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05',  
             '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10',  
             '2022-01-11', '2022-01-12', '2022-01-13', '2022-01-14', '2022-01-15',  
             '2022-01-16', '2022-01-17', '2022-01-18', '2022-01-19', '2022-01-20'],  
    'Category': ['Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing',  
                 'Home', 'Electronics', 'Clothing', 'Home', 'Electronics',  
                 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home',  
                 'Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing'],  
    'Quantity': [10, 5, 8, 20, 7, 6, 9, 11, 4, 13, 6, 9, 8, 5, 7, 11, 9, 6, 10, 8],  
    'Revenue': [1000, 250, 600, 1200, 350, 450, 900, 550, 300, 1300, 300, 675, 800, 250, 525, 1100, 450, 450, 1000, 400]  
})
```

### Step 2

* Create a bar chart to visualize the revenue by product category.  
  + Label the axes and title appropriately.
  + Create a new variable called ‘category\_revenure’ using this code `category_revenue = data.groupby('Category')['Revenue'].sum()`.
  + Which of the product categories has the greatest amount of revenue?

### Step 3

* Create a histogram to visualize the distribution of revenue.  
  + Label the axes and title appropriately.
  + How would you describe the shape of the distribution?

### Step 4

* Create a scatter plot to visualize the relationship between quantity sold and revenue.  
  + Label the axes and title appropriately.
  + How would you describe the overall trend of the data?

### Step 5

* Create a boxplot to visualize the quantity sold.  
  + Label the axes and title appropriately.
  + Do you notice any extreme values (possible outliers)?

### Solution

### [Select for Solution](#dpPanel5)

#### Step 1

```
# import germane libraries  
import pandas as pd  
import matplotlib.pyplot as plt  
  
# data  
data = pd.DataFrame({  
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05',  
             '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10',  
             '2022-01-11', '2022-01-12', '2022-01-13', '2022-01-14', '2022-01-15',  
             '2022-01-16', '2022-01-17', '2022-01-18', '2022-01-19', '2022-01-20'],  
    'Category': ['Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing',  
                 'Home', 'Electronics', 'Clothing', 'Home', 'Electronics',  
                 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home',  
                 'Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing'],  
    'Quantity': [10, 5, 8, 20, 7, 6, 9, 11, 4, 13, 6, 9, 8, 5, 7, 11, 9, 6, 10, 8],  
    'Revenue': [1000, 250, 600, 1200, 350, 450, 900, 550, 300, 1300, 300, 675, 800, 250, 525, 1100, 450, 450, 1000, 400]  
})
```

#### Step 2

Create a bar chart to visualize the revenue by product category.

Which of the product categories has the greatest amount of revenue? **Electronics**

```
# new variable  
category_revenue = data.groupby('Category')['Revenue'].sum()  
  
# bar chart  
plt.figure(figsize=(8, 6))  
plt.bar(category_revenue.index, category_revenue.values)  
plt.xlabel('Product Category')  
plt.ylabel('Revenue')  
plt.title('Revenue by Product Category')  
plt.show()
```

 
![Bar chart of revenue by product category](https://moringa.instructure.com/courses/1406/files/625168/download)

#### Step 3

Create a histogram to visualize the distribution of revenue.

How would you describe the shape of the distribution? **Generally skewed right.**

```
# histogram  
plt.figure(figsize=(8, 6))  
plt.hist(data['Revenue'], bins=10, edgecolor='black')  
plt.xlabel('Revenue')  
plt.ylabel('Frequency')  
plt.title('Distribution of Revenue')  
plt.show()
```

 
![Histogram of distribution of revenue](https://moringa.instructure.com/courses/1406/files/625052/download)

#### Step 4

Create a scatter plot to visualize the relationship between quantity sold and revenue.

How would you describe the overall trend of the data? **Generally positive, increasing trend**

```
# scatterplot  
plt.figure(figsize=(8, 6))  
plt.scatter(data['Quantity'], data['Revenue'])  
plt.xlabel('Quantity Sold')  
plt.ylabel('Revenue')  
plt.title('Quantity Sold vs. Revenue')  
plt.show()
```

![Scatterplot of quality sold versus revenue](https://moringa.instructure.com/courses/1406/files/625059/download)

##### Step 5

Create a boxplot to visualize the quantity sold.

Do you notice any extreme values (possible outliers)? **Strong visual evidence for an extreme value (potential outlier) greater than the rest of the data**

```
# boxplot  
  
plt.figure(figsize=(8, 6))  
plt.boxplot(data['Quantity'])  
plt.xlabel('Quantity Sold')  
plt.title('Boxplot of Quantity Sold')  
plt.show()
```

 
![Boxplot of quantity sold](https://moringa.instructure.com/courses/1406/files/625041/download)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243566

Scraped At: 2026-05-14T20:53:55.954049
