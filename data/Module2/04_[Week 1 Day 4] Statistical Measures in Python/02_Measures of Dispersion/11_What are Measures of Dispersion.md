# What are Measures of Dispersion?

# What are Measures of Dispersion?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What are Measures of Dispersion?

Icon Progress Bar (browser only)

12 min read

The following are the measures of dispersion to know for this lesson:

**Mean Absolute Deviation (MAD):** This tells you the average distance each data point falls from the mean (average) of the data set. It's a good measure for understanding how spread out the data is without being influenced too heavily by extreme values (outliers).

**Variance:** This represents the average squared deviation from the mean. While it gives a sense of spread, variance can be difficult to interpret directly because it's in squared units. Outliers or observations at large deviation from the mean tend to be heavily weighted in the variance due to the computation involving the square of the deviation.

**Standard Deviation (SD):** This is the square root of the variance. It's expressed in the same units as the original data, making it easier to understand the spread compared to variance. A high SD indicates a larger spread of data points from the mean. However, similar to variance, SD can be sensitive to outliers because squaring the deviations from the mean gives more weight to extreme values.

**Interquartile Range (IQR):** This focuses on the middle 50% of the data. It represents the difference between the 75th percentile (Q3) and the 25th percentile (Q1) of the data set. IQR is a good measure for understanding spread when outliers might exist because it ignores the extreme values on either end.

### How Does Dispersion Work?

Understanding and being able to calculate measures of dispersion is crucial in data science for a few key reasons:

1. **Revealing the Spread of the Data:** Central tendency measures like mean or median only tell you where the center of the data is clustered. They don't tell you how spread out the data points are from that center. Measures of dispersion, like variance, standard deviation, and interquartile range, quantify this spread. This is vital for understanding the data's variability and how representative the central tendency value might be.
2. **Identifying Outliers:** High dispersion can indicate the presence of outliers in your data. Outliers are data points that fall far outside the typical range. By understanding the spread through measures of dispersion, you can identify potential outliers that might require further investigation or exclusion (depending on the context).
3. **Comparing Datasets:** Measures of dispersion allow you to compare a given attribute across different groups in a statistically meaningful manner. For instance, you might want to compare the income levels between two cities to understand the relative wealth of one city versus the other. You extract mean or median income for each city and compare them. Unfortunately, there is no way to tell whether this difference is statistically meaningful without having a grasp of the scale of income variation within each city. The illustration below demonstrates the issue at hand: 

   ![Two graphs comparing two cities and the effect of spread.](https://moringa.instructure.com/courses/1406/files/625046/download)

   Both panels contain histograms of income data with the same means for each city. However, for the left panel, the income distributions in each city have low dispersion relative to the difference in the mean incomes between the cities. The mean income is clearly higher in City A than in City B relative to the spread of incomes in each city. The right pane, on the other hand, shows a different situation. The dispersion in each city is considerably larger than the difference in means. In this regime, it is exceedingly difficult to tell whether the difference in mean income is of statistical significance whatsoever.  
     
   The example serves to illustrate that meaningful comparison between groups requires some measure of dispersion along with a measure of central tendency.

In essence, measures of dispersion provide a more complete picture of your data by revealing how tightly or loosely clustered the data points are around the central value. This knowledge is essential for drawing accurate conclusions from your data analysis.

The choice of dispersion measure depends on various considerations. While all three measures—mean absolute deviation (MAD), standard deviation (SD), and interquartile range (IQR)—describe the spread of data, they do so in different ways and with varying sensitivities to outliers.

### [Mean Absolute Deviation](#dpPanel0)

The **mean absolute deviation** quantifies how far away data points on average lie from the mean. The distance or deviation of a data point
![LaTeX: x\_i](https://bletchley.instructure.com/equation\_images/x\_i?scale=1)
xi from its mean
![LaTeX: \bar{x}](https://bletchley.instructure.com/equation\_images/%255Cbar%257Bx%257D?scale=1)
ˉx can be calculate as the absolute value of the difference between the value of the data point and the mean (i.e.
![LaTeX: \left| x\_i - \bar{x} \right| ](https://bletchley.instructure.com/equation\_images/%255Cleft%257C%2520%2520x\_i%2520-%2520%255Cbar%257Bx%257D%2520%255Cright%257C%2520?scale=1)
|xi−ˉx|). Averaging over these yields the formula for the mean absolute deviation (MAD):o.

```
![LaTeX: MAD = \frac{\sum_{i=1}^N |x_i - \bar{x}|}{N}](https://bletchley.instructure.com/equation_images/MAD%2520%253D%2520%255Cfrac%257B%255Csum_%257Bi%253D1%257D%255EN%2520%257Cx_i%2520-%2520%255Cbar%257Bx%257D%257C%257D%257BN%257D?scale=0.875)

\(MAD = \frac{\sum_{i=1}^N |x_i - \bar{x}|}{N}\)
```

Taking the absolute value is important here as you just want to focus on how big the deviation of each data point from the mean is, not its sign.

### [Variance and Standard Deviation](#dpPanel1)

The variance, often denoted as
![LaTeX: s^2](https://bletchley.instructure.com/equation\_images/s%255E2?scale=1)
s2,  is the mean of squared deviations of the sample from its mean. The computation is similar to the mean absolute deviation:

```
![LaTeX: s^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N}](https://bletchley.instructure.com/equation_images/s%255E2%2520%253D%2520%255Cfrac%257B%255Csum_%257Bi%253D1%257D%255EN%2520(x_i%2520-%2520%255Cbar%257Bx%257D)%255E2%257D%257BN%257D?scale=0.875)

\(s^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N}\)
```

Similar to what you saw with the average absolute deviation, each element of the sum is positive. The sign of the squared deviation does not depend on whether a particular value falls below or above the mean. Thus averaging squared deviations yields a measure of overall dispersion of the data about the mean. Note that the variance reflects the square of the deviation of the measured quantity as opposed to directly being a measure of the deviation itself. There are mathematical and theoretical reasons as to why the variance is a fundamental quantity when conducting statistical inference and assessing relationships between different variables. This is why one would want to compute the sample variance of a feature directly.

However, if you just want a direct measure of the deviation from the mean, you could just take the square root of the variance.

This results in the standard deviation:

```
![LaTeX:  s = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N}} ](https://bletchley.instructure.com/equation_images/%2520s%2520%253D%2520%255Csqrt%257B%255Cfrac%257B%255Csum_%257Bi%253D1%257D%255EN%2520(x_i%2520-%2520%255Cbar%257Bx%257D)%255E2%257D%257BN%257D%257D%2520?scale=0.875)

\( s = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N}} \)
```

The standard deviation is perhaps the most commonly used measure of dispersion—not in small part because of its connection to the variance and to many fundamental aspects of statistics.

Both the variance and the standard deviation tend to be sensitive to values that lie at high deviation from the mean. This can be seen by inspecting the sum in the numerator of the variance. Deviations get squared and then these squared deviations are what contribute to the sum. This has the effect that large deviations contribute in an even larger way (i.e., as the square) to the variance than smaller deviations. Thus the variance and the standard deviation, by extension, are sensitive to outliers and quantities at the edges of the main distribution. Using the standard deviation without taking into account the presence of outliers can potentially lead to drastic overestimates of the characteristic range of a given measurable. MAD, being proportional to a sum of just the absolute values of the deviations,  tends to be a bit more robust to this outlier-induced inflation.

### [The Interquartile Range](#dpPanel2)

The Interquartile Range (IQR) offers a distinct approach to measuring data spread compared to standard deviation and Mean Absolute Deviation (MAD). Unlike those measures, which can be swayed by outliers, IQR explicitly focuses on getting the core range of the data.

It does this by splitting the data into four equal parts:

 
![Interquartile range example demonstrating Q1 and Q3 numbers split into 4 quarters](https://moringa.instructure.com/courses/1406/files/625039/download)

The values in the data that separate each quarter of the data are called quartiles and are denoted as Q1, Q2 (the median) and Q3. Q1 is the 25th percentile (i.e. 25% of the data falls below Q1) and Q3 is the 75th percentile (i.e. 75% of the data lies below Q3). The Interquartile Range (IQR) is calculated by subtracting the value of the first quartile (Q1) from the third quartile (Q3).

```
![LaTeX: \text{IQR} = Q_3 - Q_1](https://bletchley.instructure.com/equation_images/%255Ctext%257BIQR%257D%2520%253D%2520Q_3%2520-%2520Q_1?scale=0.875)

\(\text{IQR} = Q_3 - Q_1\)
```

This essentially represents the **middle 50%** of the data, or the range within which half of the data points fall on either side of the median. As we can see, the IQR is a measure of dispersion about a value of central tendency. It gives us a characteristic scale for the variability present in our data. In the example above, the middle 50% of the data lies in the interval (53, 82). We can compute the IQR = 82 - 53 = 29. Thus the data above has a characteristic value of 69 (the median) with a range of 29 reflecting the bulk of variation in the data about the median.

The IQR is insensitive to the exact values of data lying below the lower quartile (Q1) and above the upper quartile (Q3). As an example, imagine changing the highest two values in the dataset above from 94 and 95 to 1082 and 11000.

While this change certainly affects the MAD and standard deviation, it is evident that the change leaves Q1, Q3, and consequently the IQR unchanged. This leads us to the conclusion that the IQR is robust to outliers. Of course, this robustness can be a weakness or a strength for a measure of dispersion. If we want our measure of dispersion to contain information about the extent of the edges of the data distribution, then we may want to use the standard deviation or MAD. However, if we are interested in the core of the distribution and want our measure of characteristic range to strictly reject information from the edges of the distribution, then we might want to use the IQR.

### [Measures of Deviation vs. Measures of Range](#dpPanel3)

One might want to compare the standard deviation, MAD, and IQR for a given sample. However, there is an important distinction that one must keep in mind when interpreting these measures of dispersion and comparing them against each other. The standard deviation and the MAD measure an expected deviation from the value of central tendency. This means that the characteristic range that the sample standard deviation, for example, defines is the interval
![LaTeX: [\bar{x} - s, \bar{x} + s]](https://bletchley.instructure.com/equation\_images/%255B%255Cbar%257Bx%257D%2520-%2520s%252C%2520%255Cbar%257Bx%257D%2520%252B%2520s%255D?scale=1)
[ˉx−s,ˉx+s]. The range is defined by the deviation on either side of the sample mean. The full length of this range is then 2*s*. The same is true for MAD where the characteristic interval defined is
![LaTeX: [\bar{x} - MAD,  \bar{x} + MAD]](https://bletchley.instructure.com/equation\_images/%255B%255Cbar%257Bx%257D%2520-%2520MAD%252C%2520%25C2%25A0%255Cbar%257Bx%257D%2520%252B%2520MAD%255D?scale=1)
[ˉx−MAD,ˉx+MAD] with the full length of the range being 2\*MAD. The IQR, on the other hand, already reports the full length of the range (Q1, Q3): the distance between the lower and upper quartiles.

The plot below shows the situation. The sample standard deviation is ~1 (as can be seen by the blue arrow and solid blue line). The standard deviation *s* can then be used to define a characteristic range of
![LaTeX: \pm s](https://bletchley.instructure.com/equation\_images/%255Cpm%2520s?scale=1)
±s about the sample mean
![LaTeX: \bar{x}](https://bletchley.instructure.com/equation\_images/%255Cbar%257Bx%257D?scale=1)
ˉx:

![Plot showing the comparison of standard deviation, MAD, and IQR](https://moringa.instructure.com/courses/1406/files/625078/download)

The IQR range (Q1, Q3), is the gray shaded area and already defines a characteristic range.

This implies that a direct comparison between the IQR vs. the standard deviation or MAD is not valid. One must compare the IQR to twice the MAD or standard deviation. Typically, what we will see is that estimates of the characteristic range displayed by the IQR tend to be smaller and more conservative than the ranges given by the other two measures. Again, the main reason for this is that the IQR explicitly rejects information from the edges of the distribution while outliers and/or tails do contribute to the other measures.

### [Sample Statistics and Population Parameters: Measures of Spread](#dpPanel4)

Just as the measure of central tendency for a sample can be used to estimate a characteristic value for a population, we can use measures of dispersion from a sample to estimate a characteristic spread of values for an underlying population. Theoretical considerations show that statistics like the IQR, MAD, variance and standard deviation tend to provide decent estimates of spread in the underlying population—particularly for sample sizes larger than ~ 30.

However, some care needs to be taken—particularly with regards to the variance and standard deviation at smaller sample sizes. It turns out that the formulas for the sample variance need to be corrected if they are to be good estimates of the underlying population variance. This population variance is denoted as
![LaTeX: \sigma^2](https://bletchley.instructure.com/equation\_images/%255Csigma%255E2?scale=1)
σ2 to differentiate it from the standard sample variance
![LaTeX: s^2](https://bletchley.instructure.com/equation\_images/s%255E2?scale=1)
s2.

Our original formula for the sample variance statistic goes as:

```
![LaTeX: s^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N}](https://bletchley.instructure.com/equation_images/s%255E2%2520%253D%2520%255Cfrac%257B%255Csum_%257Bi%253D1%257D%255EN%2520(x_i%2520-%2520%255Cbar%257Bx%257D)%255E2%257D%257BN%257D?scale=0.875)

\(s^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N}\)
```

In order for the sample variance statistic
![LaTeX: s^2](https://bletchley.instructure.com/equation\_images/s%255E2?scale=1)
s2 to be a good estimate of the population variance, we need to divide the numerator in our previous formula by N - 1 instead of N:

```
![LaTeX: s_{corr}^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}](https://bletchley.instructure.com/equation_images/s_%257Bcorr%257D%255E2%2520%253D%2520%255Cfrac%257B%255Csum_%257Bi%253D1%257D%255EN%2520(x_i%2520-%2520%255Cbar%257Bx%257D)%255E2%257D%257BN%2520-%25201%257D?scale=0.875)

\(s_{corr}^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}\)
```

This correction
![LaTeX: s\_{corr}^2](https://bletchley.instructure.com/equation\_images/s\_%257Bcorr%257D%255E2?scale=1)
s2corr provides a better estimate of
![LaTeX: \sigma^2](https://bletchley.instructure.com/equation\_images/%255Csigma%255E2?scale=1)
σ2 than
![LaTeX: s^2](https://bletchley.instructure.com/equation\_images/s%255E2?scale=1)
s2. Note that this correction becomes important for small samples and less important as the number of samples you have gets large. Since we are generally interested in using summary statistics on samples to infer something about the population at large, we will be using the above formula for the sample variance from now on.

The standard deviation also gets modified:

```
$ 

![LaTeX: s_{corr} = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}}](https://bletchley.instructure.com/equation_images/s_%257Bcorr%257D%2520%253D%2520%255Csqrt%257B%255Cfrac%257B%255Csum_%257Bi%253D1%257D%255EN%2520(x_i%2520-%2520%255Cbar%257Bx%257D)%255E2%257D%257BN%2520-%25201%257D%257D?scale=0.875)

\(s_{corr} = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}}\)
```

This modification to the sample standard deviation provides better estimates of the population standard deviation
![LaTeX: \sigma](https://bletchley.instructure.com/equation\_images/%255Csigma?scale=1)
σ.

### Conceptualization: Measures of Dispersion

Measure of Dispersion with definition and notation and sensitivity to outliers.

| Measure | Notation | Description | Sensitive to Outliers? | Units |
| --- | --- | --- | --- | --- |
| Variance | σ² (sigma squared) | Average squared deviations from the mean | Yes | Squared units of the data |
| Standard Deviation (SD) | σ (sigma) | Square root of the variance | Yes | Same units as the data |
| Mean Absolute Deviation | MAD | Average distance from the median | Less | Same units as the data |
| Interquartile Range (IQR) | Q3 - Q1 | Range between the 1st and 3rd quartiles | No | Same units as the data |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243540

Scraped At: 2026-05-14T20:51:09.879181
