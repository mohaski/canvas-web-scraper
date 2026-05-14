# Practice: Measures of Central Tendency

# Practice: Measures of Central Tendency

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Measures of Central Tendency

Icon Progress Bar (browser only)

7 min read

It is time to get some hands-on practice calculating measures of central tendency for a variety of cases. For this lab, you will be using a dataset which contains weights, heights, and some other attributes for a number of surveyed individuals. You will be extracting mean, median, and mode for the height of the surveyed individuals and you will see how each of these represent a value of central tendency for the entire group.

Setup Instructions:

1. Fork the repository to personal github.
2. Clone down the repo notebook locally.
3. Work in learn-env virtual environment.
4. Open notebook in code editor of choice and complete code.

### Resources

* [GitHub Repository (Practice 1 file)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m3)

### Instructions

### Step 1

Load in the relevant dataset using csv DictReader. The path has been provided.

```
import csv  
path = './nhis.csv'  
  
# Your code here
```

### Step 2

Extract values for the the variable height and save to a Python list called `height\_list`.

### Step 3

Calculate the mean of the height data by explicitly calculating the sum over values and dividing by the number of data points.

### Step 4

Calculate mean height using numpy.

### Step 5

We have plotted a histogram of the data. There are clearly outliers in the data.

![Histogram showing plotted results of individuals and height](https://moringa.instructure.com/courses/1406/files/625053/download)

Is the mean the best measure for central tendency given these outliers? Explain your answer.

### Step 6

Given knowledge of the distribution of the data and the presence of outliers, compute the relevant statistic (i.e., the mode or the median) reflecting central tendency. Use either the Counter object or numpy respectively for the statistic you have chosen.

### Step 7

There are cases where the extreme values are either erroneous data points or are not relevant to the aims of our analysis. Filtering outliers is useful in this case. Filter the heights\_list by removing any values greater than 80. This value is set by inspection of the histogram above. Save this to a new list called filtered\_heights\_list.

### Step 8

Compute the mean on the filtered\_heights\_list.

### Step 9

**Reflection Question:** How does the mean of the data with outliers removed compare to the mean of the original data? How do both means compare to the median?

### Step 10

Calculate the mode for height data. Complete the function below so that it returns a list of values—there may be more than one value—which have the highest frequency.

```
# Throughout this cell, replace None with appropriate code  
  
def get_mode(data):  
  
    # Create and populate frequency distribution  
    frequency_dict = {}  
      
    for height in data:  
        # If an element is not in the dict, add it to the dict with value 1  
        # If an element is already in the dict, +1 the value in place  
        None  
      
    # Find the frequency of the mode(s) by finding the largest  
    # value in frequency_dict  
    highest_freq = None  
      
    # Create a list for mode values  
    modes = []  
      
    # From the dictionary, add element(s) to the modes list with max frequency  
    for height, frequency in frequency_dict.items():  
        None  
  
    # Return the mode list   
    return modes
```

### Step 11

Use the above function to calculate the mode of the original height list.

### Step 12

Use the collections library and Counter object to extract the mode.

### Step 13

**Reflection Question:** Discuss the location of the mode relative to the mean and median. Could knowing the value of the mode independent of the mean and median be useful? Explain.

### Solution

### Select for Solution

1. Load in the relevant dataset using csv DictReader. The path has been provided.

```
import csv  
path = './nhis.csv'  
  
# Your code here
```

**Expected Output:**

```
data = list(csv.DictReader(f))  
data  
  
  
[{'HHX': '16',  
  'FMX': '1',  
  'FPX': '2',  
  'SEX': '1',  
  'BMI': '33.36',  
  'SLEEP': '8',  
  'educ': '16',  
  'height': '74',  
  'weight': '260'},  
 {'HHX': '20',  
  'FMX': '1',  
  'FPX': '1',  
  'SEX': '1',  
  'BMI': '26.54',  
  'SLEEP': '7',  
  'educ': '14',  
  'height': '70',  
  'weight': '185'},  
 {'HHX': '69',  
  'FMX': '1',  
  'FPX': '2',  
  'SEX': '2',  
  'BMI': '32.13',  
  'SLEEP': '7',  
  'educ': '9',  
  
...  
 'SLEEP': '8',  
  'educ': '16',  
  'height': '72',  
  'weight': '195'},  
 ...]
```

1. Extract values for the the variable height and save to a Python list called `height\_list`:

```
#Your code here.  
height_list = [int(row['height']) for row in data]
```

1. Calculate the mean of the height data by explicitly calculating the sum over values and dividing by the number of data points.

```
 # Your code here.  
height_mean = sum(height_list)/len(height_list)  
height_mean
```

**Expected Output:**

```
69.57826541274817
```

1. Calculate mean height using numpy.

```
# Your code here.   
import numpy as np  
  
height_numpy = np.array(height_list)  
height_numpy.mean()
```

**Expected Output:**

```
69.57826541274817
```

1. We have plotted a histogram of the data. There are clearly outliers in the data.

 Is the mean the best measure for central tendency given these outliers? Explain your answer.

**Expected Answer:**

The mean is not the best measure here. The outlier will pull the mean up from the central, most probable part of the main distribution.

1. Given knowledge of the distribution of the data and the presence of outliers, compute the relevant statistic (i.e., the mode or the median) reflecting central tendency. Use either the Counter object or numpy respectively for the statistic you have chosen.

```
# Your code here.  
  
# the median is the best statistic here and is much more stable to the outliers than the mean.  
median_stat = np.median(height_numpy)  
median_stat
```

**Expected Output:**

```
67.0
```

1. There are cases where the extreme values are either erroneous data points or are not relevant to the aims of our analysis. Filtering outliers is useful in this case. Filter the heights\_list by removing any values greater than 80. This value is set by inspection of the histogram above. Save this to a new list called filtered\_heights\_list.

```
# Your code here.   
  
filtered_height_list = [height for height in height_list if height < 80 ]
```

1. Compute the mean on the filtered\_heights\_list.

```
 # Your code here.  
filtered_heights_mean = np.array(filtered_height_list).mean()  
filtered_heights_mean
```

**Expected Output:**

```
 66.85231193926846
```

1. How does the mean of the data with outliers removed compare to the mean of the original data? How do both means compare to the median?

**Expected Answer:**

The mean on the filtered list is lower than the original mean. It lies close to the median on the original dataset. Quick inspection of the histogram shows that both the median of the original data and the mean of the data with outliers removed lie at the center of the main distribution of heights.

1. Calculate the mode for height data. Complete the function below so that it returns a list of values—there may be more than one value—which have the highest frequency.

```
# Your code here.  
  
  
# Throughout this cell, replace None with appropriate code  
  
  
def get_mode(data):  
  
  
    # Create and populate frequency distribution  
    frequency_dict = {}  
     
    for height in data:  
        # If an element is not in the dict, add it to the dict with value 1  
        # If an element is already in the dict, +1 the value in place  
        if height in frequency_dict.keys():  
            frequency_dict[height] += 1  
        else:  
            frequency_dict[height] = 1  
     
    # Find the frequency of the mode(s) by finding the largest  
    # value in frequency_dict  
    highest_freq = max(frequency_dict.values())  
     
    # Create a list for mode values  
    modes = []  
     
    # From the dictionary, add element(s) to the modes list with max frequency  
    for height, frequency in frequency_dict.items():  
        if frequency == highest_freq:  
            modes.append(height)  
  
  
    # Return the mode list  
    return modes
```

1. Use the above function to calculate the mode of the original height list.

```
 # Your code here  
find_mode(height_list)
```

**Expected Output:**

```
[64]
```

1. Use the collections library and Counter object to extract the mode.

```
# Your code here  
from collections import Counter  
  
  
# insert python height list into Counter object  
cnt_obj = Counter(height_list)  
  
  
# counter object most common method to extracr mode  
mode_counter = cnt_obj.most_common(1)[0][0]  
mode_counter
```

**Expected Output:**

```
 64
```

1. Discuss the location of the mode relative to the mean and median. Could knowing the value of the mode independent of the mean and median be useful? Explain.

**Expected Answer:**

 The mode is slightly lower than the mean and median values. It lies a little bit lower than the value of central tendency for the main part of the distribution.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243536

Scraped At: 2026-05-14T20:50:53.444122
