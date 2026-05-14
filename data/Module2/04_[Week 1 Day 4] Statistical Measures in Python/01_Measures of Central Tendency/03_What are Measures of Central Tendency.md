# What are Measures of Central Tendency?

# What are Measures of Central Tendency?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What are Measures of Central Tendency?

Icon Progress Bar (browser only)

13 min read

Central tendency, also known as a measure of central tendency, is a statistical concept used to describe the typical value within a dataset. It aims to capture, with a single number, where most of the data points tend to cluster around within the distribution.

Imagine you have a collection of test scores. Central tendency wouldn't pinpoint a single score, but rather the area where the majority of scores fall. This provides a starting point for understanding the overall performance of the class.

There are different ways to calculate this "typical" value, each with its own advantages and limitations depending on the data:

* **The Mean (Arithmetic Average):** This familiar concept finds the center point by summing all the data values and dividing by the total number of data points. It is often a good choice for representing a value of central tendency. However, there are many notable exceptions which we will discuss. One example might be where the distribution of data is skewed by the presence of extreme values (e.g., there are a few really fat koalas roving about Northern Australia).
* **The Median:** The median is a point contained within the data, ordered from lowest to highest, in half. It's unaffected by extreme values, making it a robust choice for skewed distributions where the mean might be skewed towards the tail.
* **The Mode:** This measure identifies the most frequent value in the data. For quantitative numeric data, the mode measures the most commonly occurring value. This can coincide with a measure of central tendency but does not have to. The mode can also be used to characterize nominal categoricals. In this case, the mode represents a characteristic value: the type that occurs most frequently.

As we delve deeper into this topic and actually calculate these metrics for different data, we will see the strengths and weaknesses of each measure. Knowing which measure to use in a given situation is crucial. It allows you to choose the most appropriate one to represent the central tendency of your specific data.

### How Does Central Tendency Work?

### [Mean](#dpPanel0)

#### Calculating the Mean

Let us imagine that we have a collection of retirement ages for several individuals. This can be denotes as *X* and in Python we would naturally represent this as a list:

```
X = [54, 54, 54, 55, 56, 57, 57, 58, 58, 60, 60]
```

Each individual element of this collection can symbolically be represented as
![LaTeX: x\_i](https://bletchley.instructure.com/equation\_images/x\_i?scale=1)
 where the index denotes the *i*th value in the list. For example in this case
![LaTeX: x\_4  = 55](https://bletchley.instructure.com/equation\_images/x\_4%2520%25C2%25A0%253D%252055?scale=1)
. Then the mean value of this collection of retirement ages, denoted as
![LaTeX: \bar{X}](https://bletchley.instructure.com/equation\_images/%255Cbar%257BX%257D?scale=1)
 can be calculated as follows:

Adding all the values in X together:

```
54+54+54+55+56+57+57+58+58+60+60
```

Output:

```
623
```

And then dividing this sum by the numbers of observations in X:

```
623/11
```

Output:

```
56.6
```

The mean retirement age of individuals in *X* is 56.6 years. Programatically, this would be represented as:

```
X_bar = sum(X)/len(X)  
X_bar
```

Output:

```
56.6
```

This is symbolically represented as:

```
![LaTeX: \bar{X} = \frac{1}{N}\sum_{i=1}^{N} x_i](https://bletchley.instructure.com/equation_images/%255Cbar%257BX%257D%2520%253D%2520%255Cfrac%257B1%257D%257BN%257D%255Csum_%257Bi%253D1%257D%255E%257BN%257D%2520x_i?scale=0.875)
```

Where *N* is the number of observations and
![LaTeX: \Sigma](https://bletchley.instructure.com/equation\_images/%255CSigma?scale=1)
symbols denotes a sum running over the index *i* of all the values
![LaTeX: x\_i](https://bletchley.instructure.com/equation\_images/x\_i?scale=1)
 in the *X*.

So, the mean is just an arithmetic average of the numbers contained in *X*.

#### As a Measure of Central Tendency

Whether the mean of a collection of values measures central tendency depends heavily on how the data is distributed. This will often be true when the majority of values in the collection occur around a characteristic value and where observed values get less frequent the farther you get away from this characteristic value. We will take an example of 150 grades on some Precalculus midterm with grades ranging from 0-100.  A plot called a histogram is useful to see the distribution of data. Histograms display the counts occurring in discrete value ranges and can give you a sense of how the data is distributed. For our midterm data:

 
![Histogram plot example showing counts and exam grades](https://moringa.instructure.com/courses/1406/files/624959/download)

Some important observations are:

* A grade range ~80 is the most common or most frequent outcome.
* 80 lies smack dab in the center of the range of measured values.
* Values are clustered heavily around 80 in a range (70-90).
* The frequency of values tapers off on either side of a grade of 80 and this behavior is symmetric below and above 80.

Thus most of the observations are clustered near the value (i.e., 80) of the range of observed grades. These values of high frequency dominate the sum used to calculate the mean and suggest that the mean characterizes the value of central tendency (i.e., a probable value at the center of the range of values—in this case 80).

```
![LaTeX:  \bar{X} = \frac{1}{N}\sum_{i=1}^{N} x_i ](https://bletchley.instructure.com/equation_images/%2520%255Cbar%257BX%257D%2520%253D%2520%255Cfrac%257B1%257D%257BN%257D%255Csum_%257Bi%253D1%257D%255E%257BN%257D%2520x_i%2520?scale=0.875)
```

The fact that the distribution tapers off quickly from the characteristic value and is relativity symmetric implies that contributions to the mean from more extreme values average out to the value of central tendency.

It is under these rather strict conditions that the mean represents a good measure of probable value and central tendency. It turns out that these strict conditions are met often in nature (a fact whose explanation is rather subtle and profound). It is one reason why the mean is so often used as a measure of a characteristic value for numeric quantities.

There are cases where the mean does not reflect the most probable or central value of the distribution of values. Important examples are:

* Where your distribution is skewed (i.e., is not distributed symmetrically about the value of central tendency)
* Extreme values in the dataset

The median then might work better as a measure of central tendency.

### [Median](#dpPanel1)

The median offers another way to pinpoint a central value within a dataset. Unlike the mean (average), which sums all the values and divides by the total number, the median focuses on the **middle** value.

**Odd Number of Observations:**

Imagine you're tracking the test scores for a small class of five (5) students: 85, 72, 98, 67, and 88. Since there's an odd number (5) of scores, the median is simply the **middle value** when the data is arranged in ascending or descending order. In this case, the median score is **85**.

**Even Number of Observations:**

Now, let's consider the shoe sizes of six (6) friends: 8, 7.5, 9, 10, 8.5, and 9.5. Here, we have an even number (6) of observations. With even numbers, the median is calculated as the **average of the two middle values**. Arranging the sizes from smallest to largest, the two middle values are 8.5 and 9. So, the median shoe size would be (8.5 + 9) / 2 = **9**.

#### Why Use the Median? A Case of the Outliers

The choice between using the mean or median often depends on the presence of outliers —extreme values that significantly deviate from the bulk of the data. Here's where the median shines.

Let's consider the housing prices in a particular neighborhood:

* Price 1: $225,000
* Price 2: $230,000
* Price 3: $250,000
* Price 4: $275,000
* Price 5: $300,000
* Price 6: $375,000
* Price 7: $2,500,000 (a McMansion)

The median is simply the **middle value** when the data is arranged from lowest to highest. So, the median price would be **Price 4: $275,000**.

The **mean** price ($831,875) is skewed upwards by the McMansion and is thus not representative of the bulk of the housing prices in the neighborhood. The **median (House 3: $275,000)** provides a more realistic sense of the central value of the typical house price range in the neighborhood.

#### Why Use the Median? A Case of Skewed Distribution

##### Skewed Distributions

A non-symmetrical distribution is called a **skewed distribution**. We can see two examples below:

![Side-by-side examples of positive and negative skewed distribution for retirement age](https://moringa.instructure.com/courses/1406/files/625065/download)

For skewed distributions, the mean generally is shifted away from the value of central tendency in the direction of the tail exhibiting higher frequency. The median tends to remain more stable to this and closer to where the bulk of values are clustered (i.e., in a range of highest frequency).

### [Mode](#dpPanel2)

The mode is simply the most frequent value that appears in a dataset. It identifies the value that occurs more often than any other value.

#### Mode and Data Types

The mode is particularly useful for describing the central tendency of categorical data. Categorical data consists of non-numerical values or categories, such as colors (red, green, blue), types of cars (sedan, SUV, truck), or survey responses (excellent, good, fair, poor). Since you can't calculate an average for categories, the mode identifies the most common category within the data.

The mode can be useful for understanding discrete numeric data. For instance, if you're analyzing shoe sizes in a store and find that size 8 appears more often than any other size, then 8 would be the mode. This indicates that size 8 is the most popular shoe size among your customers.

The mode can also be used with continuous numerical data, but it is generally less useful than the mean or the median in this case. Continuous data often has many unique values, and it's less likely for a single value to appear most frequently.

#### When to Use the Mode (and When You Need to be Careful)

Here are some key points to consider when using the mode:

* The mode is useful when you want to know the **most common value or category** within your data.
* **Categorical data:** The mode is the go-to choice for summarizing the central tendency of categorical data.
* **Continuous data (use with caution):** While applicable to continuous data, the mode might not be the most informative measure of central tendency, especially for large datasets with many unique values.
* The mode picks the most frequent value—not a value that necessarily measures central tendency. This means that the mode will be sensitive to spikes in the distribution of values.

**Consider this case:**  
Imagine a class of 120 students taking another challenging precalculus exam. The professor, aiming for a high standard, set a difficult curve. Here's a histogram of the resultant grades (assume a grading scale from 0 to 100):

 
![Histogram of example grades for a precalculus exam](https://moringa.instructure.com/courses/1406/files/624945/download)

Let’s say that we are interested in which of the numeric bins above contain the most counts. We are asking which of the bins corresponds to a mode. The mode here is the  bin of grades ~ 92. There is a spike in the distribution here: it happens to correspond to a cadre of future Olympiads that are in this precalculus class. This bin clearly is not near where the bulk of the distribution clusters around. That value is the bin of grades ~ 65. While characterizing the grade bin with the highest frequency, the mode does not capture the characteristic bin measuring the central tendency of the bulk of the distribution.

In essence, the mode offers a quick way to identify the peak of your data. For categorical or discrete numeric data, this will give you the value of the category or value occuring most frequently in your data. This mode may be important to know —knowing the most common range of values (or value) could certainly be useful. In the case of our grade data, it helped us identify an interesting feature that was interpretable as a subgroup of students with very high mathematical skill levels. But careless attribution of the mode to a value characteristic of the dataset can lead to errors.

#### Sample Statistics and Population Parameters

Extracting a statistic like the mode, mean, or median from a set of data gives us a characteristic value about which the data clusters. But it is important to keep in mind that the data itself is usually a sample drawn from a larger population. Our end goal is usually not just to draw conclusions about the particular set of data that we collected but rather to infer something that is generally true about the population from which the data was drawn from. The main question is whether the summary statistics that we extract from a finite size sample have anything to do with parameters that govern the population as a whole.

To make this more concrete, let’s examine a case where we want to understand the average travel distance of a specific whale species that migrates vast distances across oceans. Directly tagging and tracking every whale is close to impossible. Researchers often rely on satellite tagging a sample of the whale population. While these tags provide valuable movement data, the collected data represents a small fraction of the entire whale population. We can calculate the mean travel distance from the tagged whales. However, this is a sample statistic
![LaTeX: \bar{d}](https://bletchley.instructure.com/equation\_images/%255Cbar%257Bd%257D?scale=1)
on the measured travel distances
![LaTeX: d\_i](https://bletchley.instructure.com/equation\_images/d\_i?scale=1)
 of each whale in the sample.

```
![LaTeX: \bar{d}_{whale} = \frac{1}{N_{sample}}\sum_{i=1}^{N_{sample}} d_i](https://bletchley.instructure.com/equation_images/%255Cbar%257Bd%257D_%257Bwhale%257D%2520%253D%2520%255Cfrac%257B1%257D%257BN_%257Bsample%257D%257D%255Csum_%257Bi%253D1%257D%255E%257BN_%257Bsample%257D%257D%2520d_i?scale=0.875)
```

This  wouldn't be the exact population mean of distance traveled for all whales in the species (usually denoted by the greek symbol
![LaTeX: \mu](https://bletchley.instructure.com/equation\_images/%255Cmu?scale=1)
). If we had access to all *N* extant whales then we could calculate the population mean over the entire species. The formula follows the same logic as extracting a mean from a sample:

```
![LaTeX: \mu_{whale} = \frac{1}{N}\sum_{i=1}^{N} d_i](https://bletchley.instructure.com/equation_images/%255Cmu_%257Bwhale%257D%2520%253D%2520%255Cfrac%257B1%257D%257BN%257D%255Csum_%257Bi%253D1%257D%255E%257BN%257D%2520d_i?scale=0.875)
```

The population mean
![LaTeX: \mu\_{whale}](https://bletchley.instructure.com/equation\_images/%255Cmu\_%257Bwhale%257D?scale=1)
is a measure of central tendency for the entire whale population. So, can we use our sample mean
![LaTeX: \bar{d}](https://bletchley.instructure.com/equation\_images/%255Cbar%257Bd%257D?scale=1)
to infer the value of central tendency
![LaTeX: \mu\_{whale}](https://bletchley.instructure.com/equation\_images/%255Cmu\_%257Bwhale%257D?scale=1)
 entire whale population?

The answer is yes, but with caution. We can use the sample mean as an estimate of the underlying population parameter—but we can only do so with a certain degree of certainty.

The smaller the sample size and the more challenging the data collection, the less certain we can be that the sample mean
![LaTeX: \bar{X}](https://bletchley.instructure.com/equation\_images/%255Cbar%257BX%257D?scale=1)
provides an accurate estimate of the population parameter
![LaTeX: \mu\_{whale}](https://bletchley.instructure.com/equation\_images/%255Cmu\_%257Bwhale%257D?scale=1)
 . In the whale case, this means our estimate of the population average travel distance might have a larger margin of error. A common rule of thumb suggests a sample size of at least 30 as a good starting point for estimating population means from the sample mean. However, the ideal sample size depends on several factors that include expected variability in your population or the degree of confidence you require in your estimate of the population mean. Higher degrees of intrinsic variability in the population and/or a requirement of a lower margin of error on your population mean estimate may mean that you may need a larger sample size.

### Conceptualization: Measures of Central Tendency

Measure of Central Tendency with description and how it is used

| Measure | Description | Calculation Method | Useful for Numeric or Categorical Data | Outliers Affected? |
| --- | --- | --- | --- | --- |
| Mean | Average of all values | Sum of all values divided by the number of values | Numeric | Yes |
| Median | Middle value when data is ordered | If odd number of values: [(n + 1) / 2]th term. <br> If even number of values: Average of (n / 2)th and [(n / 2) + 1]th term. | Numeric | Less affected |
| Mode | Most frequent value | Identify value that appears most often | Numeric or Categorical | No |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243530

Scraped At: 2026-05-14T20:50:20.310665
