# Technical Lesson: Measures of Dispersion

# Technical Lesson: Measures of Dispersion

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Measures of Dispersion

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

In this technical lesson, we will walk through calculating the standard deviation, mean absolute deviation, and IQR on a data sample using Python. We will be writing functions that take in a list or an array of values and then calculate the dispersion using these various measures. We will also go over how to use numpy’s methods to extract these measures without having to manually calculate them yourself.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of measures of dispersion.

[VIDEO LINK](https://player.vimeo.com/video/989668092?h=627dbdef88)

### Situation 1: Characteristic Range for Flower Petal Lengths

Let's revisit our list of petal lengths for members of the Iris Virginica subspecies. In a previous lesson, we computed measures of central tendency for this data (i.e., the mean and median). This data was symmetrically distributed without outliers and a clear value of central tendency. In this case, the all the measures of dispersion (standard deviation, MAD and IQR) should be on the same scale. However, as they measure different things it is unreasonable to expect they are all the same. Let's go ahead and calculate all of these.

### Step 1: Standard Deviation

#### Computing Standard Deviation

First, we start the variance—which we will use to compute the standard deviation:

```
virginica_petal_length = [6.0, 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1, 5.1, 5.3, 5.5, 5.0, 5.1, 5.3, 5.5, 6.7, 6.9, 5.0, 5.7, 4.9, 6.7, 4.9, 5.7, 6.0, 4.8, 4.9, 5.6, 5.8, 6.1, 6.4, 5.6, 5.1,  
5.6, 6.1, 5.6, 5.5, 4.8, 5.4, 5.6, 5.1, 5.1, 5.9, 5.7, 5.2, 5.0, 5.2, 5.4, 5.1]
```

We now write a function that takes a list of numbers as input and returns the variance of the sample as output. Using the corrected formula:

s2corr=∑Ni(xi−ˉx)2N−1

```
def get_variance(sample):  
  
  
    # First, calculate the sample mean  
    sample_mean = sum(sample)/len(sample)  
     
    sum_of_squares = 0  
    for length in sample:  
        # Now, calculate the sum of squares by subtracting the sample mean  
        # from each length, squaring the result, and adding it to the total  
        sum_of_squares += (length - sample_mean)**2  
         
    # Divide the sum of squares by the number of items in the sample -1 to calculate variance  
    variance = sum_of_squares/(len(sample)- 1)  
     
    return variance
```

Applying this function to our list of petal lengths:

```
get_variance(virginica_petal_length)
```

**Output:**

```
0.30458775510204084
```

##### Calculating variance with Numpy

The following can also be accomplished readily by using Numpy. The steps are:

* Make sure you have numpy imported.
* Convert the list into an array.
* Call the .var(ddof = 1) method on your array. This calculates the corrected sample variance. The ddof=1 argument is what provides the $N-1$ correction to the variance.

```
import numpy as np  
  
virginica_array = np.array(virginica_petal_length)  
virginica_array.var(ddof = 1)
```

**Output:**

```
0.30458775510204084
```

Now let's calculate the sample standard deviation. The corrected formula base off of the variance is:

s2corr=√∑Ni(xi−ˉx)2N−1

First, let's write a function that builds of our ≥tvariance function:

```
# write function for the standard deviation  
  
def get_stddev(sample):  
  
  
    stdev = (get_variance(sample))**0.5 # this takes the square root of the corrected sample variance  
  
  
    return stdev
```

Applying this function on our petal lengths yields our corrected sample standard deviation:

```
get_stddev(virginica_petal_length)
```

**Output:**

```
0.5518946956639834
```

Using Numpy is also fairly straightforward:  
just call the .std(ddof = 1) method on our petal length array

```
virginica_array.std(ddof = 1)
```

Output:

```
0.5518946956639834
```

### Step 2: Mean Absolute Deviation

#### Computing the Mean Absolute Deviation (MAD)

Now let us calculate the MAD:

MAD=∑Ni|xi−ˉx|N

We can write a function that takes on a form similar to our ≥tvariance function. You will need to use the Python abs() function for this:

```
def get_mad(sample):  
  
  
    # First, calculate the sample mean  
    sample_mean = sum(sample)/len(sample)  
     
    sum_of_devs = 0  
    for length in sample:  
        # find deviation by subtracting the sample mean  
        # ftake the absolute value of the deviation and adding it to the total  
        sum_of_devs += abs(length - sample_mean)  
         
    # Divide the sum of deviations by the number of items in the sample to calculate MAD    
    mad = sum_of_devs/(len(sample))  
     
    return mad
```

Extracting the MAD for our petal lengths:

```
get_mad(virginica_petal_length)
```

**Output:**

```
0.43999999999999995
```

This is a comparable value to the standard deviation.

### Step 3: Interquartile Range

#### Computing the Interquartile Range (IQR)

Now let's calculate the IQR. In principle, we could find a function that sorts the data, splits it into quarters and then extracts the range of the middle half. We are not going to take this route here. Instead we will show you two methods to extract the IQR using νmpy and scipy.

##### Method 1:

This relies on calculating the 25th and 75th percentiles (Q1 and Q3 respectively) using νmpy and subtracting them yielding the IQR:

IQR=Q3−Q1

The νmpy function np.percentile() is used to calculate percentiles as follows:

```
# calculating the 25th percentile (Q1)  
Q1 = np.percentile(virginica_petal_length , 25)  
Q1
```

**Output:**

```
5.1
```

We can do the same for the 75th percentile (Q3):

```
# calculating the 25th percentile (Q1)  
Q3 = np.percentile(virginica_petal_length , 75)  
Q3
```

**Output:**

```
5.875
```

The IQR then is:

```
IQR_petals = Q3 - Q1  
IQR_petals 
```

**Output:**

```
0.7750000000000004
```

##### Method 2:

This involves import scipy, a powerful scientific computing package built off of νmpy and using the IQR method from scipy's stats submodule:

```
from scipy.stats import iqr  
iqr(virginica_petal_length)
```

**Output:**

```
0.7750000000000004
```

Remember that the IQR is the \*characteristic range\* not just a measure of deviation from the value of central tendency. The IQR then seems to be in rough concordance with estimates from the MAD and standard deviation.

### Situation 2: Characteristic Range for Weekly Sales of Air Conditioner Units

Recall that this data contained large outliers. There were two weeks, in particular, where the store made considerably more on air conditioner sales than other weeks. We will now see how presence of outliers affect the different measures of dispersion:

```
from scipy.stats import iqr  
weekly_sales = [5333, 4211, 35204, 4409, 5884, 5100, 4964, 3786, 5494, 5344, 5233, 5713,  
                4481, 4325, 5105, 4167, 5011, 5088, 5732, 4623, 6217, 5492, 4189, 6435,  
                5270, 5720, 5437, 6572, 4203, 26110, 4105, 3993, 5546, 4751, 4139, 4431,  
                4271, 5537, 6177, 4439, 5394, 6525, 4512, 3940, 4078, 5430, 5112, 5255, 5379,  
                5493, 6659, 4826]
```

### Step 1: Standard Deviation

#### Computing the Standard Deviation

```
np.array(weekly_sales).std(ddof = 1)
```

**Output:**

```
5104.157200459102
```

### Step 2: Mean Absolute Deviation

#### Computing the MAD

As mentioned in the lesson, we need to first sort the numeric data. Then we need to check whether the number of elements are even or odd.

* If odd (tested by modulo 2 division on the data length), just get the middle element: this is the number of element floor divided by 2.
* If even (the only other case besides odd), then find the two elements in the middle and average them.

In base Python, you can write a function to do this:

```
def compute_median(data):  
  """  
  This function calculates the median of a list of numbers.  
  
  
  Args:  
      data: A list of numbers.  
  
  
  Returns:  
      The median of the data.  
  """  
  
  
  # Sort the data in ascending order.  
  sorted_data = sorted(data)  
  
  
  # Calculate the length of the data.  
  n = len(sorted_data)  
  
  
  # If the length is odd, the median is the middle element.  
  if n % 2 == 1:  
    return sorted_data[n // 2]  
  
  
  # If the length is even, the median is the average of the two middle elements.  
  else:  
    middle_index1 = n // 2  
    middle_index2 = middle_index1 - 1  
    return (sorted_data[middle_index1] + sorted_data[middle_index2]) / 2
```

Now use the defined function or our data to compute the median:

```
compute_median(weekly_sales)
```

**Output:**

```
5172.5
```

This median looks plausible as a central measure of the main part of the data (excluding outliers). Compare this with the mean whose value is clearly pushed up considerably by outliers from the median and lies closer to higher end of values for the main data.

```
sum(weekly_sales)/len(weekly_sales)
```

**Output:**

```
6054.692307692308
```

### Step 3: Interquartile Range

#### Computing the IQR

```
iqr(weekly_sales)
```

**Output:**

```
1113.75
```

### Step 4: Removing Outliers

#### Removing Outliers

There are pretty large differences here—particularly between the standard deviation and the rest of the measures of dispersion. It's useful to look at a histogram of weekly sales.

![Histogram of weekly sales](https://moringa.instructure.com/courses/1406/files/625019/download)

The standard deviation is influenced heavily by the outliers. An inspection of the main cluster of values shows that an estimation of the characteristic range at ~ 5100 is much too high. The MAD is more reasonable but still is a bit high as an estimate of characteristic deviation from the value of central tendency. This is due to the fact that MAD is still influenced by the outliers at high values. The IQR estimates the full characteristic range of the bulk of the data. The range of the IQR seems reasonable.

Now let us remove outliers and see what happens to the three measures of dispersion:

```
weekly_sales_no_outliers = [elem for elem in weekly_sales if elem < 20000]
```

##### Calculating the standard deviation with outliers removed:

```
np.array(weekly_sales_no_outliers).std(ddof = 1)
```

This is a substantial reduction in the standard deviation! It is certainly more characteristic of the dispersion about the mean than the previous value when outliers were included.

**Output:**

```
760.6934001157049
```

##### Calculating the MAD with outliers removed:

```
get_mad(weekly_sales_no_outliers)
```

```
627.9680000000001
```

The MAD (Mean Absolute Deviation) also sees a substantial drop from its previous value when outliers were included. This drop is not as drastic as in the case of the standard deviation. Note that now the MAD and standard deviation are fairly similar in value.

##### Calculating the IQR with outliers removed:

```
iqr(weekly_sales_no_outliers)
```

**Output:**

```
1079.25
```

The IQR remains pretty stable and doesn't change much at all. This jives with the notion that the IQR is largely insensitive to distribution outliers.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243545

Scraped At: 2026-05-14T20:51:43.286100
