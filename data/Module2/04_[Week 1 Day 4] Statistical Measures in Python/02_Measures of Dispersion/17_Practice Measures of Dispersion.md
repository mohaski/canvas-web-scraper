# Practice: Measures of Dispersion

# Practice: Measures of Dispersion

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Measures of Dispersion

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

It is time to get some hands-on practice calculating measures of dispersion for a variety of cases. For this lab, you will be using the NHIS dataset that we used previously in the practice lab for measures which contain weights, heights, and some other attributes for a number of surveyed individuals.

Setup Instructions:

1. Fork the repository to your personal github.
2. Clone down the repo notebook locally.
3. Work in learn-env virtual environment.
4. Open notebook in code editor of choice and complete code.

### Resources

* [GitHub Repository (Practice 2 file)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m3)

### Instructions

* [Step 1](#dpPanel0Content)
* [Step 2](#dpPanel1Content)
* [Step 3](#dpPanel2Content)
* [Step 4](#dpPanel3Content)
* [Step 5](#dpPanel4Content)
* [Step 6](#dpPanel5Content)
* [Step 7](#dpPanel6Content)
* [Step 8](#dpPanel7Content)
* [Step 9](#dpPanel8Content)
* [Step 10](#dpPanel9Content)
* [Step 11](#dpPanel10Content)

### Step 1

Load in the relevant dataset using csv DictReader.

```
import csv  
  
# Your code here
```

### Step 2

Extract values for the the variable height and save to a Python list called `height\_list`.

### Step 3

We have plotted a histogram of the data. There are clearly outliers in the data.

![Histogram results for height](https://moringa.instructure.com/courses/1406/files/624769/download)

Calculate the sample mean of the heights.

### Step 4

Calculate the sample variance of the heights. Make sure that you are using the corrected variance.

### Step 5

Calculate the sample standard deviation of heights. Make sure that you are using the corrected standard deviation.

### Step 6

Calculate the IQR by calculating and subtracting relevant percentiles.

### Step 7

Calculate the IQR using scipy.

### Step 8

Clean all outliers from the height data. You can use the histogram of heights to help guide in your data filtering.

### Step 9

Compute the sample standard deviation on the cleaned data.

### Step 10

Compute the new IQR on the cleaned data.

### Step 11

Comment on how the standard deviation and IQR has changed between the original and cleaned heights.

### Solution

### [Select for Solution](#dpPanel11)

1. Load in the relevant dataset using csv DictReader. The path has been provided.

```
import csv  
path = './nhis.csv'  
# Or bring in the data file locally  
   
  
# Your code here  
with open(path, 'r') as f:  
    data = list(csv.DictReader(f))  
data[0]
```

**Expected Output:**

```
1079.25
```

1. Extract values for the the variable height and save to a Python list called `height\_list`:

```
#Your code here.  
height_list = [int(row['height']) for row in data]
```

We have plotted a histogram of the data. There are clearly outliers in the data.

![Histogram results for height](https://moringa.instructure.com/courses/1406/files/624769/download)

1. Calculate the sample mean of the heights.

```
# Your code here  
import numpy as np # import numpy  
  
height_array = np.array(height_list)  
height_mean = height_array.mean()  
height_mean
```

**Expected Output:**

```
69.57826541274817
```

1. Calculate the sample variance of the heights. Make sure that you are using the corrected variance.

```
# Your code here  
height_variance = height_array.var(ddof=1)  
height_variance
```

**Expected Output:**

```
87.74476162268516
```

1. Calculate the sample standard deviation of heights. Make sure that you are using the corrected standard deviation.

```
# Your code here  
height_std = height_array.std(ddof=1)  
height_std
```

**Expected Answer:**

```
9.367217389528502
```

1. Calculate the IQR by calculating and subtracting relevant percentiles.

```
# Your code here  
Q1 = np.percentile(height_array, 25)  
Q3 = np.percentile(height_array, 75)  
print(Q1, Q3)  
IQR_orig = Q3 - Q1  
print(IQR_orig)
```

**Expected Output:**

```
64.0 71.0  
  
7.0
```

1. Calculate the IQR using scipy.

```
# Your code here  
from scipy.stats import iqr  
  
iqr(height_array)
```

**Expected Output:**

```
7.0
```

1. Clean all outliers from the height data. You can use the histogram of heights to help guide in your data filtering.

```
# Your code here  
  
#filtering heights above 80 out of the dataset should do the trick.  
# we convert to numpy array for convenience  
heights_cleaned = np.array([height for height in height_list if height < 80 ])
```

1. Compute the sample standard deviation on the cleaned data.

```
# Your code here  
cleaned_std = heights_cleaned.std(ddof=1)  
cleaned_std
```

**Expected Output:**

```
3.910385485998152
```

1. Compute the new IQR on the cleaned data.

```
# Your code here  
Q1_cleaned = np.percentile(heights_cleaned, 25)  
Q3_cleaned = np.percentile(heights_cleaned, 75)  
  
print(Q1_cleaned, Q3_cleaned)  
iqr_cleaned = iqr(heights_cleaned)  
iqr_cleaned
```

**Expected Output:**

```
64.0 70.0  
  
6.0
```

1. Comment on how the standard deviation and IQR has changed between  the original and cleaned heights.

**Expected Answer:**

The standard deviation has reduced substantially—to a value that now reflects a deviation from the mean about which the bulk of the main height distribution lies. The IQR has reduced somewhat but is basically stable. The IQR now is commensurate with the characteristic range
![LaTeX: [ \bar{x} - s, \bar{x} + s]](https://bletchley.instructure.com/equation\_images/%255B%2520%255Cbar%257Bx%257D%2520-%2520s%252C%2520%255Cbar%257Bx%257D%2520%252B%2520s%255D?scale=1)
given by the sample standard deviation and mean.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243546

Scraped At: 2026-05-14T20:51:50.546711
