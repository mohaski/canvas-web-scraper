# Technical Lesson: Using PySpark and Python

# Technical Lesson: Using PySpark and Python

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: Using PySpark and Python

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In the previous lessons, you were introduced to SparkContext as the primary way to connect with a Spark Application.

Here, we will be using SparkSession, which is from the SQL component of PySpark. The SparkSession acts the same way as SparkContext; it is a bridge between Python and the Spark Application. It's just built on top of the Spark SQL API, a higher-level API than RDDs. In fact, a SparkContext object is spun up around which the SparkSession object is wrapped.

Let's go through the process of manipulating some data here. We will be using the [Forest Fire dataset from UCI


Links to an external site.](https://archive.ics.uci.edu/ml/datasets/Forest+Fires), which contains data about the area burned by wildfires in the Northeast region of Portugal in relation to numerous other factors.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of using PySpark and Python.

[VIDEO LINK](https://player.vimeo.com/video/1058080918?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

### Step 1. SparkSession

* Create a SparkSession so that we can spin up our spark application.

```
# importing the necessary libraries  
from pyspark import SparkContext  
from pyspark.sql import SparkSession  
# sc = SparkContext('local[*]')  
# spark = SparkSession(sc)
```

To create a SparkSession:

```
spark = SparkSession.builder.master('local').getOrCreate()
```

* Next, load the data into a PySpark DataFrame:

```
## reading in pyspark df  
spark_df = spark.read.csv('./forestfires.csv', header='true', inferSchema='true')  
  
## observing the datatype of df  
type(spark_df)
```

You'll notice that some of the methods are extremely similar or the same as those found within Pandas.

```
spark_df.head()
```

**Output:**

```
Row(X=7, Y=5, month='mar', day='fri', FFMC=86.2, DMC=26.2, DC=94.3, ISI=5.1, temp=8.2,   
RH=51, wind=6.7, rain=0.0, area=0.0)
```

```
spark_df.columns
```

**Output:**

```
['X',  
 'Y',  
 'month',  
 'day',  
 'FFMC',  
 'DMC',  
 'DC',  
 'ISI',  
 'temp',  
 'RH',  
 'wind',  
 'rain',  
 'area']
```

* Selecting multiple columns is similar as well:

```
spark_df[['month','day','rain']].show()
```

**Output:**

```
+-----+---+----+  
|month|day|rain|  
+-----+---+----+  
|  mar|fri| 0.0|  
|  oct|tue| 0.0|  
|  oct|sat| 0.0|  
|  mar|fri| 0.2|  
|  mar|sun| 0.0|  
|  aug|sun| 0.0|  
|  aug|mon| 0.0|  
|  aug|mon| 0.0|  
|  sep|tue| 0.0|  
|  sep|sat| 0.0|  
|  sep|sat| 0.0|  
|  sep|sat| 0.0|  
|  aug|fri| 0.0|  
|  sep|mon| 0.0|  
|  sep|wed| 0.0|  
|  sep|fri| 0.0|  
|  mar|sat| 0.0|  
|  oct|mon| 0.0|  
|  mar|wed| 0.0|  
|  apr|sat| 0.0|  
+-----+---+----+  
only showing top 20 rows
```

* **Selecting one column is different.** If you want to maintain the methods of a spark DataFrame, you should use the .select() method. If you want to just select the column, you can use the same method you would use in pandas (this is primarily what you would use if you're attempting to create a boolean mask).

```
spark_df.select('rain')
```

```
spark_df['rain']
```

Let's take a look at all of our data types in this dataframe.

```
spark_df.dtypes
```

**Output:**

```
[('X', 'int'),  
 ('Y', 'int'),  
 ('month', 'string'),  
 ('day', 'string'),  
 ('FFMC', 'double'),  
 ('DMC', 'double'),  
 ('DC', 'double'),  
 ('ISI', 'double'),  
 ('temp', 'double'),  
 ('RH', 'int'),  
 ('wind', 'double'),  
 ('rain', 'double'),  
 ('area', 'double')]
```

### Step 2. Aggregations with our DataFrame

* Let's investigate to see if there is any correlation between what month it is and the area of fire:

```
spark_df_months = spark_df.groupBy('month').agg({'area': 'mean'})  
spark_df_months
```

**Output:**

```
DataFrame[month: string, avg(area): double]
```

* Notice how the grouped DataFrame is not returned when you call the aggregation method. Remember, this is still Spark! The transformations and actions are kept separate so that it is easier to manage large quantities of data. You can perform the transformation by calling .collect():

```
spark_df_months.collect()
```

**Output:**

```
[Row(month='jun', avg(area)=5.841176470588234),  
 Row(month='aug', avg(area)=12.489076086956521),  
 Row(month='may', avg(area)=19.24),  
 Row(month='feb', avg(area)=6.275),  
 Row(month='sep', avg(area)=17.942616279069753),  
 Row(month='mar', avg(area)=4.356666666666667),  
 Row(month='oct', avg(area)=6.638),  
 Row(month='jul', avg(area)=14.3696875),  
 Row(month='nov', avg(area)=0.0),  
 Row(month='apr', avg(area)=8.891111111111112),  
 Row(month='dec', avg(area)=13.33),  
 Row(month='jan', avg(area)=0.0)]
```

As you can see, there seem to be larger area fires during what would be considered the summer months in Portugal. On your own, practice more aggregations and manipulations that you might be able to perform on this dataset.

### Step 3. Boolean Masking

Boolean masking also works with PySpark DataFrames just like Pandas DataFrames, the only difference being that the .filter() method is used in PySpark.

* To try this out, let's compare the amount of fire in those areas with absolutely no rain to those areas that had rain.

```
no_rain = spark_df.filter(spark_df['rain'] == 0.0)  
some_rain = spark_df.filter(spark_df['rain'] > 0.0)
```

* To perform calculations to find the mean of a column, we'll have to import functions from pyspark.sql. As always, to read more about them, check out the documentation.

```
from pyspark.sql.functions import mean  
  
print('no rain fire area: ', no_rain.select(mean('area')).show(),'\n')  
  
print('some rain fire area: ', some_rain.select(mean('area')).show(),'\n')
```

**Output:**

```
+------------------+  
|         avg(area)|  
+------------------+  
|13.023693516699408|  
+------------------+  
  
no rain fire area:  None   
  
+---------+  
|avg(area)|  
+---------+  
|  1.62375|  
+---------+  
  
some rain fire area:  None 
```

Yes there's definitely something there! Unsurprisingly, rain plays a big factor in the spread of wildfire.

* Obtain data from only the summer months in Portugal (June, July, and August). We can also do the same for the winter months in Portugal (December, January, February).

```
summer_months = spark_df.filter(spark_df['month'].isin(['jun','jul','aug']))  
winter_months = spark_df.filter(spark_df['month'].isin(['dec','jan','feb']))  
  
print('summer months fire area', summer_months.select(mean('area')).show())  
print('winter months fire areas', winter_months.select(mean('area')).show())
```

**Output:**

```
+------------------+  
|         avg(area)|  
+------------------+  
|12.262317596566525|  
+------------------+  
  
summer months fire area None  
+-----------------+  
|        avg(area)|  
+-----------------+  
|7.918387096774193|  
+-----------------+  
  
winter months fire areas None
```

### Step 4. Binning

There is a way that we can combine categories together, which is called binning. The **binning approach is similar to the CASE WHEN technique in SQL**. If this were a SQL query, it would look something like this:

```
SELECT CASE  
       WHEN EDUCATION = '0' THEN 'Other'  
       WHEN EDUCATION = '5' THEN 'Other'  
       WHEN EDUCATION = '6' THEN 'Other'  
       ELSE EDUCATION  
       END AS EDUCATION  
  FROM credit_card_default;
```

**With Spark SQL DataFrames, this is achieved using .withColumn()** (documentation linked in the Summary page) in conjunction with .when()  and .otherwise() (documentation linked in the Summary page).

* So let’s bin the Summer and Winter months together, respectively, and then the Spring and Fall months together.

```
from pyspark.sql import functions as F  
  
# Bin months by season  
df_months_binned = spark_df.withColumn('month',  
                                         F.when(spark_df['month'] == 'jun', 'Summer') \  
                                         .when(spark_df['month'] == 'jul', 'Summer') \  
                                         .when(spark_df['month'] == 'aug', 'Summer') \  
                                         .when(spark_df['month'] == 'jan', 'Winter') \  
                                         .when(spark_df['month'] == 'feb', 'Winter') \  
                                         .when(spark_df['month'] == 'dec', 'Winter') \  
                                         .otherwise('Spring/Fall')  
                                        )  
  
  
# Select both 'month' and 'area' before grouping and aggregating  
result = df_months_binned.select('month', 'area').groupBy('month').agg({'area': 'mean'}).distinct()  
result.show() # To display the results
```

**Output:**

```
+-----------+------------------+  
|      month|         avg(area)|  
+-----------+------------------+  
|     Summer|12.262317596566525|  
|Spring/Fall|13.989960474308296|  
|     Winter| 7.918387096774193|  
+-----------+------------------+
```

### Considerations

1. **Setting Up SparkSession**

#### Challenge

You may encounter issues when setting up SparkSession, particularly with understanding the master parameter. For instance, master('local') runs Spark on a local machine, but larger data or distributed setups require configuration for clusters.

### Insight

master('local') is ideal for learning and smaller datasets, while master('yarn') or master('spark://host:port') are for distributed environments.

### Decision Point

The choice of master configuration affects scalability. Working locally is simpler for experimentation but limits Spark’s power. Pros of master('local') include simplicity and direct control, while cons involve limited computational capacity.

1. **Loading Data into DataFrames**

#### Challenge

You may face issues with file paths, especially in various environments like Jupyter Notebooks, standalone scripts, or cloud systems.

### Insight

Relative paths (e.g., './forestfires.csv') aid portability, but in cloud or distributed setups, you may need fully qualified paths (e.g., s3://bucket/path/file.csv).

### Decision Point

While inferSchema='true' automatically detects data types, this can slow down performance for very large datasets. Setting data types manually may be more efficient, especially with well-known schemas.

1. **Data Manipulation Similarities with Pandas**

#### Challenge

PySpark DataFrame methods can appear very similar to Pandas, but PySpark performs transformations lazily, meaning results aren’t computed until an action (e.g., .collect(), .show()) is called. This may be confusing initially.

#### Insight

Lazy evaluation allows Spark to optimize operations, especially on large datasets. However, it requires a new mindset if you're accustomed to eager evaluation (e.g., pandas).

#### Decision Point

Using .collect() or .show() materializes the DataFrame but also brings data to the driver’s memory, which can be limiting with large datasets. Use .collect() sparingly and only on manageable data sizes.

1. **Aggregation and Grouping Data**

#### Challenge

Unlike Pandas, aggregated results in PySpark aren’t automatically returned or immediately visible until .collect() or .show() is called, which can be confusing if you're expecting instant feedback.

#### Insight

This structure enables Spark to delay operations until necessary, saving memory and enhancing efficiency on big data.

#### Decision Point

When calling .collect(), you should be aware of memory constraints. Pros include the convenience of inspecting smaller datasets, but for large datasets, better practices involve saving results to files or visualizing summaries instead.

1. **Boolean Masking and Filtering Data**

#### Challenge

Transitioning from Pandas-style masking to PySpark’s .filter() method can be tricky, especially when you try to chain multiple filters together.

#### Insight

PySpark’s .filter() function enables efficient filtering without immediately loading data into memory, which is advantageous for large-scale processing.

#### Decision Point

Using .filter() over repeatedly chaining methods is usually more efficient in Spark. Build filters using multiple conditions within a single .filter() expression to optimize performance.

1. **Handling Aggregations, to include Binning, on Subsets of Data (e.g., summer/winter months)**

#### Challenge

Aggregations or binning by specific conditions, such as mean('area') for seasonal data, may tempt you to use multiple .collect() calls, which can consume excessive memory. Further, binning statements are often long and/or complicated.

#### Insight

For analyzing subsets, it’s often more efficient to filter once and then perform aggregations rather than repeatedly collecting small subsets. You should consider caching when subsets will be reused, as it optimizes performance.

#### Decision Point

Caching data subsets, like summer\_months and winter\_months, may be beneficial when performing multiple operations on these data segments. While caching saves time on recomputation, it does consume memory, so its pros are speed at the expense of higher resource usage.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248294

Scraped At: 2026-05-15T09:55:05.755287
