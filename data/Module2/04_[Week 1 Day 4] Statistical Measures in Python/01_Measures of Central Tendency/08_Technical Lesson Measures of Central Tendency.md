# Technical Lesson: Measures of Central Tendency

# Technical Lesson: Measures of Central Tendency

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Measures of Central Tendency

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

Measures of central tendency form the basis of much of the statistical analysis that is used in data science. Without a firm understanding of these concepts, it is difficult to understand what comes later. We use the canonical iris data set to illustrate the measures of central tendency.

In this technical lesson, we will walk through examples of computing the mean, median, and mode in situations that are appropriate. We will follow a general pattern:

1. Understand the type of data you have and how it might be distributed.
2. Choose the appropriate statistic for quantifying central tendency.
3. Calculate that statistic.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of measures of central tendency.

[VIDEO LINK](https://player.vimeo.com/video/989668022?h=120327daab)

### Situation 1: Characteristic Value for Flower Petal Lengths

Many continuous physical measurements are often clustered in a symmetric fashion about a value of central tendency with extreme values being exceedingly unlikely.

Here, let us compute the characteristic value—or the value of central tendency—for the petal lengths of the Virginica subspecies of Iris flowers. A list of measured values have been given to you:

```
virginica_petal_length = [6.0, 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1, 5.1, 5.3, 5.5, 5.0, 5.1, 5.3, 5.5, 6.7, 6.9, 5.0, 5.7, 4.9, 6.7, 4.9, 5.7, 6.0, 4.8, 4.9, 5.6, 5.8, 6.1, 6.4, 5.6, 5.1,  
5.6, 6.1, 5.6, 5.5, 4.8, 5.4, 5.6, 5.1, 5.1, 5.9, 5.7, 5.2, 5.0, 5.2, 5.4, 5.1]
```

### Step 1

#### Choose the appropriate metric for this situation

The mean will be a good measure here.

### Step 2

#### Compute the mean

We can use base Python to compute the sum of values and then divide by the number of elements.

```
virginica_mean = sum(virginica_petal_length)/len(virginica_petal_length)  
virginica_mean
```

**Output:**

```
5.5520000000000005
```

### Using Numpy

#### Using Numpy

This can also be performed using a powerful numeric computation packed called Numpy. Numpy has a datatype called an array which is pretty similar to a list. However, the numpy array has a whole host of statistical and computational methods associated with it. This makes performing common mathematical operations on list type data a lot easier in Numpy with numpy arrays.

The process is as follows:

1. Make sure numpy is imported.
2. Convert Python list to numpy array.
3. Use .mean() method.

```
# step 1: library hasnt been imported yet  
import numpy as np
```

Numpy has been imported. `np` is a standard alias for `numpy`. 

```
# step 2  
virginica_petal_length_array = np.array(virginica_petal_length)  
print(type(virginica_petal_length_array))  
virginica_petal_length_array
```

**Output:**

```
<class 'numpy.ndarray'>  
  
array([6. , 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1, 5.1, 5.3, 5.5,  
       5. , 5.1, 5.3, 5.5, 6.7, 6.9, 5. , 5.7, 4.9, 6.7, 4.9, 5.7, 6. ,  
       4.8, 4.9, 5.6, 5.8, 6.1, 6.4, 5.6, 5.1, 5.6, 6.1, 5.6, 5.5, 4.8,  
       5.4, 5.6, 5.1, 5.1, 5.9, 5.7, 5.2, 5. , 5.2, 5.4, 5.1])
```

We have a numpy array —which is like a list. And now comes the magic.

```
# step 3  
virginica_petal_length_array.mean()
```

**Output:**

```
5.5520000000000005
```

We have the same result as before with a single method attached natively to the datatype.

### Situation 2: Characteristic Value for Weekly Sales of Air Conditioner Units

Financial and sales data can often have outliers. External events or holidays can lead to a sudden spike or dip in the measured quantity. While these outliers are part of the data, the bulk of data is clustered in a different location.

Here, let us compute the characteristic value—or the value of central tendency —for a store's weekly sales of refrigerators for the past year.

```
weekly_sales = [5333, 4211, 35204, 4409, 5884, 5100, 4964, 3786, 5494, 5344, 5233, 5713,  
                4481, 4325, 5105, 4167, 5011, 5088, 5732, 4623, 6217, 5492, 4189, 6435,  
                5270, 5720, 5437, 6572, 4203, 26110, 4105, 3993, 5546, 4751, 4139, 4431,  
                4271, 5537, 6177, 4439, 5394, 6525, 4512, 3940, 4078, 5430, 5112, 5255, 5379,  
                5493, 6659, 4826]
```

A quick perusal of the sales data shows that there are some outliers here. These are weeks where the store happens to have sold a lot of refrigerators—much more than the general expectation.

### Step 1

#### Choose the Appropriate Metric for This Situation

Based on the presence of outliers and the fact that the rest of the the bulk of the values lies in a similar range, the appropriate choice would be the median.

### Step 2

#### Compute the Median

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

### Using Numpy

* Convert to list to numpy array
* Use numpy's median function `np.median`

```
weekly_sales_array = np.array(weekly_sales)  
# use numpy's median function  
sales_median = np.median(weekly_sales_array)  
sales_median
```

Output:

```
5172.5
```

### Situation 3: Characteristic Value for the Type of Soda Picked at a Party

We may want to extract a characteristic value for nominal and/or certain kinds of ordinal categorical data.

There is a party with 30 people. They all choose to grab a soda bottle from the cooler. There are only 3 choices—Coke, Sunkist, and Sprite. The below list displays the choices that were made:

```
soda_data = ['Sprite', 'Sunkist', 'Sunkist', 'Coke', 'Coke', 'Coke', 'Coke', 'Coke', 'Coke', 'Coke', 'Coke',  
              'Coke', 'Coke', 'Coke', 'Coke', 'Coke', 'Coke', 'Coke', 'Coke', 'Coke',  
             'Sprite', 'Sprite', 'Sprite', 'Sprite', 'Sprite', 'Sprite', 'Sprite', 'Sprite', 'Sprite', 'Sunkist']
```

### Step 1

#### Choose the appropriate metric for this situation

The appropriate statistic is the mode. The characteristic statistic for categorical data should capture the most commonly occurring category.

### Step 2

#### Compute the mode

* The strategy here is to create a dictionary with keys being the unique categories.
* Then loop through the list and add a count to a particular key each time you encounter the corresponding category in the list. The result is a dictionary with {category: count} key/value pairs.
* The last step involves computing the maximum and then finding the key (or category) corresponding to this maximum count value.

```
def find_mode(data):  
  """  
  This function finds the mode(s) of a list.  
  
  
  Args:  
    data: A list of hashable elements.  
  
  
  Returns:  
    A list of modes. If there is no mode, returns an empty list.  
  """  
  # Initialize an empty dictionary to store element counts.  
  counts = {}  
  
  
  # Iterate through the list and count the occurrences of each element.  
  for element in data:  
    if element in counts:  
      counts[element] += 1  
    else:  
      counts[element] = 1  
  
  
  # Find the maximum count.  
  max_count = max(counts.values(), default=0)  
  
  
  # Find the elements with the maximum count.  
  modes = [element for element, count in counts.items() if count == max_count]  
  
  
  return modes
```

Use this function to return the mode:

```
find_mode(soda_data)
```

**Output:**

```
['Coke']
```

### The Counter object in the `collections` module

Writing the above function is not efficient nor is it generally required. Base Python has the very useful `collections` module that has the `Counter` object that is perfect for this task.  
In order to use `Counter` to compute the mode, you will need to:

1. Import Counter from collections
2. Create a Counter object
3. Use the .most\_common() method

Let's see this in action:

```
# 1. Import Counter  
from collections import Counter
```

**Output:**

```
['Coke']
```

```
# 2. Input the data into Counter's arguments  
cnt_obj = Counter(soda_data)  
cnt_obj
```

**Output:**

```
Counter({'Coke': 17, 'Sprite': 10, 'Sunkist': 3})
```

The Counter is a Python dictionary with some additional functionality. Now let’s use this added functionality to quickly extract the mode.

```
# 3. Input the data into Counter's arguments and get mode  
mode_val_pair = cnt_obj.most_common(1)  
mode_val_pair
```

**Output:**

```
[('Coke', 17)]
```

```
# Extracting the mode from this list of tuples:  
mode_val_pair[0][0]
```

**Output:**

```
'Coke'
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243535

Scraped At: 2026-05-14T20:50:48.079907
