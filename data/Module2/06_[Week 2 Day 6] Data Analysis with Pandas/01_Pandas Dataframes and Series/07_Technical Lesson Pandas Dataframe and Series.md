# Technical Lesson: Pandas Dataframe and Series

# Technical Lesson: Pandas Dataframe and Series

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Pandas Dataframe and Series

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

This technical lesson will walk you through the basics of dealing with Pandas DataFrames and Series. We will follow a general pattern:

1. Load and then inspect your data quickly to get a feel for its schema and get a high level statistical summary of the dataset. This information will guide you in subsequent steps.
2. Access and alter your data as needed. This process will introduce some key attributes of Series and DataFrames like the index and column labels as well as the machinery of the accessors and Boolean masking/selection.
3. Transform your data in pandas Series or DataFrames in a computationally efficient manner with far fewer lines of code than you have been using in the previous module. This will include employing built-in, vectorized methods for pandas Series of various data types (string, datetimes, etc.) as well as applying your own custom functions.

In what follows, you will gain experience with a myriad of the tools with the Pandas toolkit. While these are listed as steps to help you understand each one of the concepts, when it comes to applying these tools on data when facing a data science problem, you only need to use the ones that are helpful. You’ll gain experience with applying only what is necessary for a given data set and problem throughout the rest of the module. It should be noted that when learning about widely used Python libraries like Pandas, we often need to learn about a number of the libraries capabilities before we can apply them in a particular context.

### Videos: Technical Lesson Steps

Review the following videos for a walkthrough of the technical lesson step that follow.

#### **Part 1:**

[VIDEO LINK](https://player.vimeo.com/video/995574422?h=a7c4042f8c)

#### **Part 2:**

[VIDEO LINK](https://player.vimeo.com/video/997899168?h=0b16a31c7a)

#### **Part 3:**

[VIDEO LINK](https://player.vimeo.com/video/997899324?h=afd387389f)

### Resources

* [Pandas DataFrame Documentation


  Links to an external site.](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
* [Pandas Series Documentation


  Links to an external site.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)
* [Supplementary Pandas Content](https://moringa.instructure.com/courses/1406/pages/supplementary-pandas-content "Supplementary Pandas Content")

### Instructions

### [Step 1: Pandas & Series](#dpPanel0)

When we use Pandas or any library in Python, we want to import it.

```
# import pandas library  
import pandas as pd 
```

Now that we have imported Pandas, we can consider its data structures: series and data frames.

* **Series:** 1D array with native support for many data operations that numpy arrays don't.
* **DataFrames:** Tabular data with various tabular manipulation operations. Individual columns/rows are pandas Series.

We’ll begin with series and then turn to data frames.

#### Pandas Series

Here is an example of a Panda series. Suppose we have data on the highest number of cars that a few famous people have owned.

| **Person** | **Max Number of Cars** |
| --- | --- |
| Muammar Qaddafi | 25000 |
| Mohandas Gandhi | 0 |
| Saddam Hussein | 4500 |
| Kevin Bacon | 2 |
| Billy Bob Thornton | 8 |

Create a Pandas series by inputting a list of values and passing in the names as a list of indices, as follows:

```
pd.Series([25000,0,4500,2,8],  
          index = ['Muammar Qaddafi', 'Mohandas Gandhi', 'Saddam Hussein', 'Kevin Bacon', 'Billy Bob Thornton'],   
          name = 'Max Number Cars Owned')
```

Which gives this output:

```
Muammar Qaddafi       25000  
Mohandas Gandhi           0  
Saddam Hussein         4500  
Kevin Bacon               2  
Billy Bob Thornton        8  
Name: Max Number Cars Owned, dtype: int64
```

A series can naturally be inputted from a dict:

```
car_dict = {'Muammar Qaddafi': 25000, 'Mohandas Gandhi': 0,   
            'Saddam Hussein': 4500, 'Kevin Bacon': 2, 'Billy Bob Thornton': 8}  
  
car_owner_series = pd.Series(car_dict, name='Max Number Cars Owned')  
car_owner_series
```

**Output:**

```
Muammar Qaddafi       25000  
Mohandas Gandhi           0  
Saddam Hussein         4500  
Kevin Bacon               2  
Billy Bob Thornton        8  
dtype: int64
```

Using Pandas series combines:

* Dictionary style fast lookup
* Numpy style vectorized operations on the values

To illustrate that Pandas share fast lookup with dictionary, note that the series are indexed on sensible keys:

```
car_owner_series['Billy Bob Thornton']
```

**Output:**

```
8
```

As such, one can also slice on these keys:

```
car_owner_series["Mohandas Gandhi"  
                 :"Kevin Bacon"]
```

**Output:**

```
Mohandas Gandhi       0  
Saddam Hussein     4500  
Kevin Bacon           2  
dtype: int64
```

To illustrate how series can exploit Numpy style operations. As an example, let’s say that Kevin Bacon bought an extra car and Billy Bob bought two more. We can represent this change as a pandas Series:

```
delta_cars = {'Mohandas Gandhi': 0, 'Billy Bob Thornton': 2,   
              'Saddam Hussein': 0, 'Kevin Bacon': 1, 'Muammar Qaddafi': 0}  
delta_cars_series = pd.Series(delta_cars, name='Max Number Cars Owned')
```

Now let’s print this change and compare to the original series:

```
print(delta_cars_series)
```

**Output:**

```
Mohandas Gandhi       0  
Billy Bob Thornton    2  
Saddam Hussein        0  
Kevin Bacon           1  
Muammar Qaddafi       0  
dtype: int64
```

```
print(car_owner_series)
```

**Output:**

```
Muammar Qaddafi       25000  
Mohandas Gandhi           0  
Saddam Hussein         4500  
Kevin Bacon               2  
Billy Bob Thornton        8  
dtype: int64
```

While we want to update the original Series, we can see that the two series are not in the same order. This is no problem for Pandas. It adds the elements automatically by the named index as we can see here.

```
new_car_series = car_owner_series + delta_cars_series  
print(new_car_series)
```

**Output:**

```
Billy Bob Thornton       10  
Kevin Bacon               3  
Mohandas Gandhi           0  
Muammar Qaddafi       25000  
Saddam Hussein         4500  
dtype: int64
```

#### Series attributes

Now that we have considered series and see how they combine Dictionary style fast lookup Numpy style vectorized operations on the values, we can look at the following attributes of series:

* The Series.index attribute: list of indices (keys)  

  ```
  new_car_series.index
  ```

  ```
  Output:  
  Index(['Billy Bob Thornton', 'Kevin Bacon', 'Mohandas Gandhi',  
    
         'Muammar Qaddafi', 'Saddam Hussein'],  
    
        dtype='object')
  ```

* The Series.values attribute: series values returns as numpy array  

  ```
  new_car_series.values
  ```

  ```
  Output:  
  array([   10,     3,     0, 25000,  4500], dtype=int64)
  ```
* The Series.name attribute: the name of the series  

  ```
  new_car_series.name
  ```

  ```
  Output:  
  'max cars owned'
  ```
* We can re-assign the output of the series.name attribute if we wish. Lets try it:  

  ```
  new_car_series.name = 'total cars owned'  
  new_car_series.name
  ```

  ```
  Output:  
  'total cars owned'
  ```
* The Series.dtype: data type for Series values  

  ```
  new_car_series.dtype
  ```

  ```
  Output:  
  dtype('int64')
  ```

This signifies that each value in our Series is in 64-bit integer representation.

Series also has various attached methods. Example: Sorting by max cars in descending order.

```
new_car_series.sort_values(ascending = False)
```

**Output:**

```
Muammar Qaddafi       25000  
Saddam Hussein         4500  
Billy Bob Thornton       10  
Kevin Bacon               3  
Mohandas Gandhi           0  
Name: Max cars owned, dtype: int64
```

Series also have the subsequent that we’ll see later:

* Native methods for handling time series data
* Whole host of other nice methods

### [Step 2: Pandas DataFrames](#dpPanel1)

Pandas DataFrames are tabular data structures, which are the most common way that you’ll work with data within Python. As such, it is appropriate to begin with looking at a dataset.

Suppose you are working for a marketing company and you need to use a breakfast cereals dataset. You can use the pd.read\_csv() command to load in data directly from a CSV file into a DataFrame. The basic pattern for this command is to specify the file path. Here, we have also specified that one of the column names (the column ‘name’) will be a unique identifier (or index) for rows in this dataset.

```
cereal_df = pd.read_csv('Data/cereal.csv', index_col = 'name')
```

There are many options for the .read\_csv() command which will be discussed later in the module. For now we are going to dig into the DataFrame we have just created.

* Often, we want a quick view of the first few entries in the table data. The .head(n) method does the trick by outputting the first n rows of the dataset. The default .head() with no argument returns the first 5 elements.  

  ```
  cereal_df.head(2) # returns first two rows
  ```

  ```
  Output:  
    
                    mfr type  calories  protein  fat  sodium  fiber  carbo  \  
    
  name                                                                         
    
  100% Bran           N    C        70        4    1     130   10.0    5.0     
    
  100% Natural Bran   Q    C       120        3    5      15    2.0    8.0     
    
                     sugars  potass  vitamins  shelf  weight  cups     rating    
    
  name                                                                           
    
  100% Bran               6     280        25      3     1.0  0.33  68.402973    
    
  100% Natural Bran       8     135         0      3     1.0  1.00  33.983679  
  ```
* Less commonly, you can also take a look at the end with the .tail() method:  

  ```
  cereal_df.tail()
  ```

    

  ```
  Output:  
    
                     mfr type  calories  protein  fat  sodium  fiber  carbo  \  
    
  name                                                                           
    
  Triples               G    C       110        2    1     250    0.0   21.0     
    
  Trix                  G    C       110        1    1     140    0.0   13.0     
    
  Wheat Chex            R    C       100        3    1     230    3.0   17.0     
    
  Wheaties              G    C       100        3    1     200    3.0   17.0     
    
  Wheaties Honey Gold   G    C       110        2    1     200    1.0   16.0     
    
                      sugars  potass  vitamins  shelf  weight  cups     rating    
    
  name                                                                             
    
  Triples                   3      60        25      3     1.0  0.75  39.106174    
    
  Trix                     12      25        25      2     1.0  1.00  27.753301    
    
  Wheat Chex                3     115        25      1     1.0  0.67  49.787445    
    
  Wheaties                  3     110        25      1     1.0  1.00  51.592193    
    
  Wheaties Honey Gold       8      60        25      1     1.0  0.75  36.187559  
  ```

Good common practice involves using the .head() and .tail() methods along with two other methods that provide metadata and descriptive statistics on the given DataFrame.

* The .info() method outputs column names, the data type for each column, non-null counts.
* .describe() method: statistics for each column.

```
cereal_df.info()
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>  
Index: 77 entries, 100% Bran to Wheaties Honey Gold  
Data columns (total 15 columns):  
 #   Column    Non-Null Count  Dtype    
---  ------    --------------  -----    
 0   mfr       77 non-null     object   
 1   type      77 non-null     object   
 2   calories  77 non-null     int64    
 3   protein   77 non-null     int64    
 4   fat       77 non-null     int64    
 5   sodium    77 non-null     int64    
 6   fiber     77 non-null     float64  
 7   carbo     77 non-null     float64  
 8   sugars    77 non-null     int64    
 9   potass    77 non-null     int64    
 10  vitamins  77 non-null     int64    
 11  shelf     77 non-null     int64    
 12  weight    77 non-null     float64  
 13  cups      77 non-null     float64  
 14  rating    77 non-null     float64  
dtypes: float64(5), int64(8), object(2)  
memory usage: 9.6+ KB
```

The .info() method conveys a lot of important information. It can be used to identify which columns have a lot of missing information. Here, there is no missing data but in general this will not be the case. Our loaded data has also been parsed automatically with data types assigned intelligently to each column.

### [Step 3: Summary Statistics](#dpPanel2)

Since our data is now in a DataFrame, we can find summary statistics across all numeric columns:

```
cereal_df.describe()
```

**Output:**

```
        calories    protein        fat      sodium      fiber      carbo  \  
count   77.000000  77.000000  77.000000   77.000000  77.000000  77.000000     
mean   106.883117   2.545455   1.012987  159.675325   2.151948  14.597403     
std     19.484119   1.094790   1.006473   83.832295   2.383364   4.278956     
min     50.000000   1.000000   0.000000    0.000000   0.000000  -1.000000     
25%    100.000000   2.000000   0.000000  130.000000   1.000000  12.000000     
50%    110.000000   3.000000   1.000000  180.000000   2.000000  14.000000     
75%    110.000000   3.000000   2.000000  210.000000   3.000000  17.000000     
max    160.000000   6.000000   5.000000  320.000000  14.000000  23.000000     
  
          sugars      potass    vitamins      shelf     weight       cups  \  
count  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000     
mean    6.922078   96.077922   28.246753   2.207792   1.029610   0.821039     
std     4.444885   71.286813   22.342523   0.832524   0.150477   0.232716     
min    -1.000000   -1.000000    0.000000   1.000000   0.500000   0.250000     
25%     3.000000   40.000000   25.000000   1.000000   1.000000   0.670000     
50%     7.000000   90.000000   25.000000   2.000000   1.000000   0.750000     
75%    11.000000  120.000000   25.000000   3.000000   1.000000   1.000000     
max    15.000000  330.000000  100.000000   3.000000   1.500000   1.500000     
  
          rating    
count  77.000000    
mean   42.665705    
std    14.047289    
min    18.042851    
25%    33.174094    
50%    40.400208    
75%    50.828392    
max    93.704912 
```

### [Step 4: Scale of Numeric Columns](#dpPanel3)

The .describe() method is useful in understanding the scale of each of your numeric columns quickly. It can also tell you whether there are signs of outliers in a given column.

There are some other important basic DataFrame attributes:

* DataFrame.index: list of index names for rows  

  ```
  cereal_df.index[0:10] # just return the first ten
  ```

  ```
  Output:  
    
  Index(['100% Bran', '100% Natural Bran', 'All-Bran',  
    
         'All-Bran with Extra Fiber', 'Almond Delight',  
    
         'Apple Cinnamon Cheerios', 'Apple Jacks', 'Basic 4', 'Bran Chex',  
    
        'Bran Flakes'],  
    
        dtype='object', name='name')
  ```
* DataFrame.columns: list of column names  

  ```
  cereal_df.columns
  ```

  ```
  Output:  
    
  Index(['mfr', 'type', 'calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo',  
    
         'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups', 'rating'],  
    
        dtype='object')
  ```
* DataFrame.shape: returns (number rows, number columns) tuple.  

  ```
  cereal_df.shape
  ```

  ```
  Output:  
    
  (77, 15)
  ```

### [Step 5: Accessing Data in a DataFrame](#dpPanel4)

Naturally, we would like to access the data in a DataFrame.

Accessing an entry in a Series by named index was straightforward:

```
new_car_series['Billy Bob Thornton']
```

**Output:**

```
10
```

For DataFrames, you can access entire columns in a similar way. Let’s access the calories column.

```
cereal_df['calories']
```

**Output:**

```
name  
100% Bran                     70  
100% Natural Bran            120  
All-Bran                      70  
All-Bran with Extra Fiber     50  
Almond Delight               110  
                            ...   
Triples                      110  
Trix                         110  
Wheat Chex                   100  
Wheaties                     100  
Wheaties Honey Gold          110  
Name: calories, Length: 77, dtype: int64
```

For column names that are contiguous (i.e. contain no spaces) you can also address the column in an equivalent way:

```
cereal_df.calories # equivalent to cereal_df['calories']
```

Note that this is returning a Series with the name "calories". This is because individual columns/rows are extracted as pandas Series from the DataFrame architecture.

You can also extract data from a subset of the columns by passing in a list of column names.

DataFrame[list of column names in subset]: returns a DataFrame

```
col_list = ['calories', 'fat', 'sugars']  
cereal_df[col_list]
```

```
Output:  
  
                           calories  fat  sugars  
  
name                                              
  
100% Bran                        70    1       6  
  
100% Natural Bran               120    5       8  
  
All-Bran                         70    1       5  
  
All-Bran with Extra Fiber        50    0       0  
  
Almond Delight                  110    2       8  
  
...                             ...  ...     ...  
  
Triples                         110    1       3  
  
Trix                            110    1      12  
  
Wheat Chex                      100    1       3  
  
Wheaties                        100    1       3  
  
Wheaties Honey Gold             110    1       8  
  
[77 rows x 3 columns]
```

This is a new dataframe with just the accessed columns in the list.

We can access a particular row and column as follows:

DataFrame[column\_name][row\_name]

```
cereal_df['sugars']['Fruity Pebbles']
```

**Output:**

```
12
```

Note that this pattern, while commonly used, is not recommended in general. When accessing rows or particular rows and columns you will want to use a particular DataFrame attribute known as the .loc[] accessor.

### [Step 6: Accessing Rows by Name](#dpPanel5)

We have just seen how to access data, but now we would like to be able access a single row or even a particular item within a Pandas DataFrame by using the .loc[] accessor.

The .loc[] accessor:

* Easily access single row in a DataFrame by named index.
* Allows for complex selections: enables slicing on index labels across both rows and columns.
* Really important to use when assigning values to a selection; we will see this later.

The general pattern for .loc[] accessor is:

1. DataFrame.loc[row\_accessor]
2. DataFrame.loc[row\_accessor, column\_accessor]

To see how we can access a single row with .loc[], let’s select the cereal All-Bran:

```
cereal_df.loc['All-Bran']
```

**Output:**

```
mfr                 K  
type                C  
calories           70  
protein             4  
fat                 1  
sodium            260  
fiber             9.0  
carbo             7.0  
sugars              5  
potass            320  
vitamins           25  
shelf               3  
weight            1.0  
cups             0.33  
rating      59.425505  
Name: All-Bran, dtype: object
```

We can also select rows by passing in a list of index names to the row accessor.

```
row_list = ['All-Bran', 'Almond Delight', 'Apple Jacks']  
cereal_df.loc[row_list]
```

**Output:**

```
              mfr type  calories  protein  fat  sodium  fiber  carbo  sugars  \  
name                                                                              
All-Bran         K    C        70        4    1     260    9.0    7.0       5     
Almond Delight   R    C       110        2    2     200    1.0   14.0       8     
Apple Jacks      K    C       110        2    0     125    1.0   11.0      14     
  
                potass  vitamins  shelf  weight  cups     rating    
name                                                                
All-Bran           320        25      3     1.0  0.33  59.425505    
Almond Delight      -1        25      3     1.0  0.75  34.384843    
Apple Jacks         30        25      2     1.0  1.00  33.174094
```

### [Step 7: Slicing Rows by Name](#dpPanel6)

Pandas also allows slicing on row indices. The slicing on the named index with the .loc[] accessor is inclusive of start and end labels.

```
# slice rows by name  
  
cereal_df.loc['All-Bran':'Apple Jacks']
```

**Output:**

```
                          mfr type  calories  protein  fat  sodium  fiber  \  
name                                                                          
All-Bran                    K    C        70        4    1     260    9.0     
All-Bran with Extra Fiber   K    C        50        4    0     140   14.0     
Almond Delight              R    C       110        2    2     200    1.0     
Apple Cinnamon Cheerios     G    C       110        2    2     180    1.5     
Apple Jacks                 K    C       110        2    0     125    1.0     
  
                           carbo  sugars  potass  vitamins  shelf  weight  \  
name                                                                          
All-Bran                     7.0       5     320        25      3     1.0     
All-Bran with Extra Fiber    8.0       0     330        25      3     1.0     
Almond Delight              14.0       8      -1        25      3     1.0     
Apple Cinnamon Cheerios     10.5      10      70        25      1     1.0     
Apple Jacks                 11.0      14      30        25      2     1.0     
  
                           cups     rating    
name                                          
All-Bran                   0.33  59.425505    
All-Bran with Extra Fiber  0.50  93.704912    
Almond Delight             0.75  34.384843    
Apple Cinnamon Cheerios    0.75  29.509541    
Apple Jacks                1.00  33.174094
```

Accessing multiple columns at the same time as selecting a row can be done by passing a list into the column part of the accessor. Let us say that we wanted calories, protein, fat, and sodium information for the cereal All-Bran.

```
# select columns by list  
  
listcol = ["calories", "protein", "fat","sodium"]  
cereal_df.loc["All-Bran", listcol]
```

**Output:**

```
calories     70  
protein       4  
fat           1  
sodium      260  
Name: All-Bran, dtype: object
```

You can also slice contiguous columns in the column part of the .loc[] accessor:

```
# slice on columns by name  
  
cereal_df.loc["All-Bran",   
              "calories":"sodium"]
```

**Output:**

```
calories     70  
protein       4  
fat           1  
sodium      260  
Name: All-Bran, dtype: object
```

### [Step 8: Selections on Rows and Columns](#dpPanel7)

Let’s slice on rows and columns to get all cereals from All-Bran to Almond Delight with columns from calories to sodium:

```
cereal_df.loc["All-Bran":"Almond Delight",   
              "calories":"sodium"]
```

**Output:**

```
                           calories  protein  fat  sodium  
name                                                       
All-Bran                         70        4    1     260  
All-Bran with Extra Fiber        50        4    0     140  
Almond Delight                  110        2    2     200
```

We can also use the .loc[] accessor to get all rows “:” and a column subset. For example, if I wanted just the protein and fat data for all cereals:

```
cereal_df.loc[:, ['protein', 'fat']]
```

**Output:**

```
                           protein  fat  
name                                     
100% Bran                        4    1  
100% Natural Bran                3    5  
All-Bran                         4    1  
All-Bran with Extra Fiber        4    0  
Almond Delight                   2    2  
...                            ...  ...  
Triples                          2    1  
Trix                             1    1  
Wheat Chex                       3    1  
Wheaties                         3    1  
Wheaties Honey Gold              2    1  
  
[77 rows x 2 columns]
```

Note that when wanting to extract all rows and column subset you could have also employed the pattern we introduced before by passing the list of columns directly in without the .loc[] accessor:

```
cereal_df[['calories','protein']]
```

 Output:

```
                          calories  protein  
name                                          
100% Bran                        70        4  
100% Natural Bran               120        3  
All-Bran                         70        4  
All-Bran with Extra Fiber        50        4  
Almond Delight                  110        2  
...                             ...      ...  
Triples                         110        2  
Trix                            110        1  
Wheat Chex                      100        3  
Wheaties                        100        3  
Wheaties Honey Gold             110        2  
  
[77 rows x 2 columns]
```

But if you want to slice on columns, you will need the .loc[] accessor for this:

```
cereal_df.loc[:, 'calories':'sodium']
```

**Output:**

```
                          calories  protein  fat  sodium  
name                                                       
100% Bran                        70        4    1     130  
100% Natural Bran               120        3    5      15  
All-Bran                         70        4    1     260  
All-Bran with Extra Fiber        50        4    0     140  
Almond Delight                  110        2    2     200  
...                             ...      ...  ...     ...  
Triples                         110        2    1     250  
Trix                            110        1    1     140  
Wheat Chex                      100        3    1     230  
Wheaties                        100        3    1     200  
Wheaties Honey Gold             110        2    1     200  
  
[77 rows x 4 columns]
```

Trying this without the .loc[] accessor yields an empty result:

```
cereal_df['calories':'sodium']
```

**Output:**

```
Empty DataFrame  
Columns: [mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups, rating]  
Index: []
```

#### Accessing rows by position

We have seen how to access rows by name as well as slice rows by name with .loc[]. Let’s now learn how to access rows by position with .iloc[].

The .iloc[] accessor:

* Access rows and columns by their integer position instead of named index.
* Everything else pretty much the same as .loc[]

Taking a look at the head or our dataset again:

```
cereal_df.head()
```

**Output:**

```
                          mfr type  calories  protein  fat  sodium  fiber  \  
name                                                                          
100% Bran                   N    C        70        4    1     130   10.0     
100% Natural Bran           Q    C       120        3    5      15    2.0     
All-Bran                    K    C        70        4    1     260    9.0     
All-Bran with Extra Fiber   K    C        50        4    0     140   14.0     
Almond Delight              R    C       110        2    2     200    1.0     
  
                           carbo  sugars  potass  vitamins  shelf  weight  \  
name                                                                          
100% Bran                    5.0       6     280        25      3     1.0     
100% Natural Bran            8.0       8     135         0      3     1.0     
All-Bran                     7.0       5     320        25      3     1.0     
All-Bran with Extra Fiber    8.0       0     330        25      3     1.0     
Almond Delight              14.0       8      -1        25      3     1.0     
  
                           cups     rating    
name                                          
100% Bran                  0.33  68.402973    
100% Natural Bran          1.00  33.983679    
All-Bran                   0.33  59.425505    
All-Bran with Extra Fiber  0.50  93.704912    
Almond Delight             0.75  34.384843
```

Using the .iloc[] accessor we can slice rows and columns by positional index. The positional indices are zero-indexed and the last index is *NOT included* in the slice.

If we want to access the rows between 100% Natural Bran and All-Bran with Extra Fiber and columns from calories to sodium with the .iloc[] accessor:

```
cereal_df.iloc[1:4, 2:6]
```

**Output:**

```
                           calories  protein  fat  sodium  
name                                                       
100% Natural Bran               120        3    5      15  
All-Bran                         70        4    1     260  
All-Bran with Extra Fiber        50        4    0     140
```

### [Step 9: Changing Attributes and Values with Pandas](#dpPanel8)

There are a few ways in which you will want to modify a DataFrame you have imported or Series you have created:

* Cleaning and altering column/index names
* Creating and removing columns/rows
* Altering values
* Changing data types

Let's walk through how to do all of these. Let's take a look at the column names with the .column DataFrame attribute:

```
cereal_df.columns 
```

**Output**:

```
Index(['name', 'mfr', 'type', 'calories', 'protein', 'fat', 'sodium', 'fiber',  
       'carbo', 'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups',  
       'rating'],  
      dtype='object')
```

#### Renaming columns

Some of these names (e.g. "mfr") are abbreviated. Let's say we want to rename some of these columns to their full name:

* DataFrame.rename(columns = \_\_\_)
* columns takes in a dict that maps column names.

```
cereal_df.rename(columns = {'mfr': 'manufacturer', 'carbo': 'carbohydate', 'potass': 'potassium  '})
```

Truncated sample output is given.

```
                         name manufacturer type  calories  protein  fat  \  
0                   100% Bran            N    C        70        4    1     
1           100% Natural Bran            Q    C       120            
..                        ...          ...  ...       ...      ...  ...     
      3    1     
76        Wheaties Honey Gold            G    C       110        2    1     
  
    sodium  fiber  carbohydate  sugars  potassium    vitamins  shelf  weight  \  
0      130   10.0          5.0       6          280        25      3     1.0     
  
..     ...    ...          ...     ...          ...       ...    ...     ...     
  
76     200    1.0         16.0       8           60        25      1     1.0     
  
    cups     rating    
0   0.33  68.402973    
1   1.00  33.983679     
..   ...        ...    
76  0.75  36.187559    
  
[77 rows x 16 columns]
```

Lets print the head and show the original column names to note the difference from above.

```
cereal_df.head(2)
```

**Output:**

```
               name mfr type  calories  protein  fat  sodium  fiber  carbo  \  
0          100% Bran   N    C        70        4    1     130   10.0    5.0     
1  100% Natural Bran   Q    C       120        3    5      15    2.0    8.0     
  
   sugars  potass  vitamins  shelf  weight  cups     rating    
0       6     280        25      3     1.0  0.33  68.402973    
1       8     135         0      3     1.0  1.00  33.983679  
```

Column names are still the same. Why?

Dataframe.rename() method creates a new dataframe by default. We need to reassign our original DataFrame to reflect these changes i.e. actually assign or save them in the  `cereal\_df` variable.

```
cereal_df = cereal_df.rename(columns = {'mfr': 'manufacturer', 'carbo': 'carbohydate', 'potass': 'potassium  '})
```

You could alternatively just use the (inplace = ... argument) so that it modifies the DataFrame in place (in this case variable assignment isn’t necessary).

```
cereal_df.rename(columns = {'mfr': 'manufacturer', 'carbo': 'carbohydate', 'potass': 'potassium  '}, inplace = True)  
cereal_df.head(2)
```

**Output:**

```
               name manufacturer type  calories  protein  fat  sodium  fiber  \  
0          100% Bran            N    C        70        4    1     130   10.0     
1  100% Natural Bran            Q    C       120        3    5      15    2.0     
  
   carbohydate  sugars  potassium    vitamins  shelf  weight  cups     rating    
0          5.0       6          280        25      3     1.0  0.33  68.402973    
1          8.0       8          135         0      3     1.0  1.00  33.983679  
```

Let's take a look at the potassium column.

```
cereal_df['potassium']
```

You will get an error in your output when you run the above code, it will be discussed why immediately below. The output is truncated below to show the most useful part of the error, the last line, which tells you what kind of error it is.

```
...  
 #  InvalidIndexError. Otherwise we fall through and re-raise  
   3816     #  the TypeError.  
   3817     self._check_indexing_error(key)  
  
KeyError: 'potassium'
```

Why did we get the error? Let’s run the following code and see why.

```
cereal_df.columns
```

**Output:**

```
Index(['name', 'manufacturer', 'type', 'calories', 'protein', 'fat', 'sodium',  
       'fiber', 'carbohydate', 'sugars', 'potassium  ', 'vitamins', 'shelf',  
       'weight', 'cups', 'rating'],  
      dtype='object')
```

We accidently introduce trailing white space into the column name. Many imports from files have this problem.

What string command do we need to trim white space? Use .strip() with list comprehension.

```
[col.strip() for col in cereal_df.columns]
```

**Output:**

```
['name',  
 'manufacturer',  
 'type',  
 'calories',  
 'protein',  
 'fat',  
 'sodium',  
 'fiber',  
 'carbohydate',  
 'sugars',  
 'potassium',  
 'vitamins',  
 'shelf',  
 'weight',  
 'cups',  
 'rating']
```

It's generally better to use Pandas native vectorized str methods as these are faster and use less code:

```
cereal_df.columns = cereal_df.columns.str.strip()  
print(cereal_df.columns)
```

**Output:**

```
Index(['name', 'manufacturer', 'type', 'calories', 'protein', 'fat', 'sodium',  
       'fiber', 'carbohydate', 'sugars', 'potassium', 'vitamins', 'shelf',  
       'weight', 'cups', 'rating'],  
      dtype='object')
```

Now look at potassium column:

```
cereal_df['potassium'].head(3)
```

**Output:**

![Cereal potassium level chart](https://moringa.instructure.com/courses/1406/files/624734/download)

It worked.

#### Removing and Creating New Columns

Let’s practice removing a column and in particular the shelf column shelf in the cereal aisle of a particular grocery store.

Let's say we don't care about this column. We will drop it with the .drop() command specifying columns to be dropped. We specify the in-place = True argument so that the changes are applied to the original dataframe:

```
cereal_df.drop(columns = ['shelf'], inplace = True)  
cereal_df.columns
```

**Output:**

```
Index(['name', 'manufacturer', 'type', 'calories', 'protein', 'fat', 'sodium',  
       'fiber', 'carbohydate', 'sugars', 'potassium', 'vitamins', 'weight',  
       'cups', 'rating'],  
      dtype='object')
```

So that’s removing a column, how do we create a new column?

The 'type' column has only two unique entries 'C' and 'H' (cold or hot cereal?). We can use Boolean condition to create a series and then encode it by integer.

Is this a hot cereal? Convert Boolean to integer.

* False = 0
* True = 1

N.B. In general, this only works appropriately for a column with two distinct values. In the case where there are more than two distinct values, the code below will encode one of the values as 1 and the rest as 0.

```
#astype converts the Boolean series to int  
is_hot = (cereal_df.type == 'H').astype('int')   
print(is_hot)  
print(is_hot.value_counts())
```

**Output:**

```
0     0  
1     0  
2     0  
3     0  
4     0  
     ..  
72    0  
73    0  
74    0  
75    0  
76    0  
Name: type, Length: 77, dtype: int32  
type  
0    74  
1     3  
Name: count, dtype: int64
```

Store this as a new column by:

DataFrame[new\_column\_name] = series

```
cereal_df['is_hot'] = is_hot  
cereal_df.head()
```

The output below has been truncated to only show the last two trailing columns.

```
...  
      rating  is_hot    
0  68.402973       0    
1  33.983679       0    
2  59.425505       0    
3  93.704912       0    
4  34.384843       0  
```

### [Step 10: Dealing with the Index and Alternating Series & DataFrames](#dpPanel9)

#### Dealing with index, rows, and columns

Let’s now see how we can deal with the index, columns, and rows.

Sometimes we want to reset the index, which takes the index to a column again. The dataframe index will then be integer-indexed.

```
cereal_df.reset_index(inplace = True)  
cereal_df.head()
```

**Output:**

```
                        name manufacturer type  calories  protein  fat  \  
0                  100% Bran            N    C        70        4    1     
1          100% Natural Bran            Q    C       120        3    5     
2                   All-Bran            K    C        70        4    1     
3  All-Bran with Extra Fiber            K    C        50        4    0     
4             Almond Delight            R    C       110        2    2     
  
   sodium  fiber  carbohydate  sugars  potassium  vitamins  weight  cups  \  
0     130   10.0          5.0       6        280        25     1.0  0.33     
1      15    2.0          8.0       8        135         0     1.0  1.00     
2     260    9.0          7.0       5        320        25     1.0  0.33     
3     140   14.0          8.0       0        330        25     1.0  0.50     
4     200    1.0         14.0       8         -1        25     1.0  0.75     
  
      rating  is_hot    
0  73.402973       0    
1  38.983679       0    
2  64.425505       0    
3  98.704912       0    
4  39.384843       0  
```

```
cereal_df.index
```

**Output:**

```
RangeIndex(start=0, stop=77, step=1)
```

Since we have manipulated the columns and rows and we’d like to perform further analysis, we will now use a command similar to reset\_index(), which is set\_index. This will allow us to remove the “All-Bran” cereal. This will allow us to remove the “All-Bran” cereal after setting the index.

The 'name' column should be our index

* .set\_index(col\_name) will set that column to the row index.
* .set\_index() can also take in a list or an index object.

```
cereal_df.set_index('name', inplace = True)  
cereal_df.head()
```

**Output:**

```
                         manufacturer type  calories  protein  fat  sodium  \  
name                                                                            
100% Bran                            N    C        70        4    1     130     
100% Natural Bran                    Q    C       120        3    5      15     
All-Bran                             K    C        70        4    1     260     
All-Bran with Extra Fiber            K    C        50        4    0     140     
Almond Delight                       R    C       110        2    2     200     
  
                           fiber  carbohydate  sugars  potassium  vitamins  \  
name                                                                           
100% Bran                   10.0          5.0       6        280        25     
100% Natural Bran            2.0          8.0       8        135         0     
All-Bran                     9.0          7.0       5        320        25     
All-Bran with Extra Fiber   14.0          8.0       0        330        25     
Almond Delight               1.0         14.0       8         -1        25     
  
                           weight  cups     rating  is_hot    
name                                                          
100% Bran                     1.0  0.33  68.402973       0    
100% Natural Bran             1.0  1.00  33.983679       0    
All-Bran                      1.0  0.33  59.425505       0    
All-Bran with Extra Fiber     1.0  0.50  93.704912       0    
Almond Delight                1.0  0.75  34.384843       0  
```

Checking the index we see that the ‘name’ column is now our DataFrame index:

```
cereal_df.index
```

**Output:**

```
Index(['100% Bran', '100% Natural Bran', 'All-Bran',  
       'All-Bran with Extra Fiber', 'Almond Delight',  
       'Apple Cinnamon Cheerios', 'Apple Jacks', 'Basic 4', 'Bran Chex',  
       'Bran Flakes', 'Cap'n'Crunch', 'Cheerios', 'Cinnamon Toast Crunch',  
       'Clusters', 'Cocoa Puffs', 'Corn Chex', 'Corn Flakes', 'Corn Pops',  
       'Count Chocula', 'Cracklin' Oat Bran', 'Cream of Wheat (Quick)',  
       'Crispix', 'Crispy Wheat & Raisins', 'Double Chex', 'Froot Loops',  
       'Frosted Flakes', 'Frosted Mini-Wheats',  
       'Fruit & Fibre Dates; Walnuts; and Oats', 'Fruitful Bran',  
       'Fruity Pebbles', 'Golden Crisp', 'Golden Grahams', 'Grape Nuts Flakes',  
       'Grape-Nuts', 'Great Grains Pecan', 'Honey Graham Ohs',  
       'Honey Nut Cheerios', 'Honey-comb', 'Just Right Crunchy  Nuggets',  
       'Just Right Fruit & Nut', 'Kix', 'Life', 'Lucky Charms', ... , 'Wheat Chex', 'Wheaties',  
       'Wheaties Honey Gold'],  
      dtype='object', name='name')
```

We can also drop rows by index name. Let’s drop the cereal All-Bran:

```
# set the index back to name  
cereal_df.set_index('name', inplace = True)   
  
  
allbran_dropped = cereal_df.drop('All-Bran')   
  
allbran_dropped.head(4)
```

**Output:**

```
                          manufacturer type  calories  protein  fat  sodium  \  
name                                                                            
100% Bran                            N    C        70        4    1     130     
100% Natural Bran                    Q    C       120        3    5      15     
All-Bran with Extra Fiber            K    C        50        4    0     140     
Almond Delight                       R    C       110        2    2     200     
  
                           fiber  carbohydate  sugars  potassium  vitamins  \  
name                                                                           
100% Bran                   10.0          5.0       6        280        25     
100% Natural Bran            2.0          8.0       8        135         0     
All-Bran with Extra Fiber   14.0          8.0       0        330        25     
Almond Delight               1.0         14.0       8         -1        25     
  
                           weight  cups     rating  is_hot    
name                                                          
100% Bran                     1.0  0.33  68.402973       0    
100% Natural Bran             1.0  1.00  33.983679       0    
All-Bran with Extra Fiber     1.0  0.50  93.704912       0    
Almond Delight                1.0  0.75  34.384843       0  
```

The .drop command can drop multiple rows by taking in a list of indices. Let’s drop the cereals '100% Bran' and 'Almond Delight':

```
two_dropped = cereal_df.drop(['100% Bran', 'Almond Delight'])  
two_dropped.head()
```

**Output:**

```
                          manufacturer type  calories  protein  fat  sodium  \  
name                                                                            
100% Natural Bran                    Q    C       120        3    5      15     
All-Bran                             K    C        70        4    1     260     
All-Bran with Extra Fiber            K    C        50        4    0     140     
Apple Cinnamon Cheerios              G    C       110        2    2     180     
Apple Jacks                          K    C       110        2    0     125     
  
                           fiber  carbohydate  sugars  potassium  vitamins  \  
name                                                                           
100% Natural Bran            2.0          8.0       8        135         0     
All-Bran                     9.0          7.0       5        320        25     
All-Bran with Extra Fiber   14.0          8.0       0        330        25     
Apple Cinnamon Cheerios      1.5         10.5      10         70        25     
Apple Jacks                  1.0         11.0      14         30        25     
  
                           weight  cups     rating  is_hot    
name                                                          
100% Natural Bran             1.0  1.00  33.983679       0    
All-Bran                      1.0  0.33  59.425505       0    
All-Bran with Extra Fiber     1.0  0.50  93.704912       0    
Apple Cinnamon Cheerios       1.0  0.75  29.509541       0    
Apple Jacks                   1.0  1.00  33.174094       0  
```

#### Altering dataframe/series values

It's really important to use the .loc[] accessor when assigning data to dataframe/series selections.

Let’s see why with this example. Select all cold cereals and look at their rating:

```
cereal_df[cereal_df["type"] == 'C']["rating"] 
```

**Output:**

```
name  
100% Bran                    68.402973  
100% Natural Bran            33.983679  
All-Bran                     59.425505  
All-Bran with Extra Fiber    93.704912  
Almond Delight               34.384843  
                               ...      
Triples                      39.106174  
Trix                         27.753301  
Wheat Chex                   49.787445  
Wheaties                     51.592193  
Wheaties Honey Gold          36.187559  
Name: rating, Length: 74, dtype: float64
```

Now, add 5 to this selection.

```
cereal_df[cereal_df["type"] == 'C']["rating"] + 5
```

**Output:**

```
name  
100% Bran                    73.402973  
100% Natural Bran            38.983679  
All-Bran                     64.425505  
All-Bran with Extra Fiber    98.704912  
Almond Delight               39.384843  
                               ...      
Triples                      44.106174  
Trix                         32.753301  
Wheat Chex                   54.787445  
Wheaties                     56.592193  
Wheaties Honey Gold          41.187559  
Name: rating, Length: 74, dtype: float64
```

Assign this modification to our original selection:

```
cereal_df[cereal_df["type"] == 'C']["rating"] = cereal_df[cereal_df["type"] == 'C']["rating"] + 5 
```

**Output:**

```
C:\Users\Praveen\AppData\Local\Temp\ipykernel_17712\465635476.py:1: SettingWithCopyWarning:   
A value is trying to be set on a copy of a slice from a DataFrame.  
Try using .loc[row_indexer,col_indexer] = value instead  
  
See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy  
  cereal_df[cereal_df["type"] == 'C']["rating"] = cereal_df[cereal_df["type"] == 'C']["rating"] + 5
```

A warning was issued. Let's see what our assignment did:

```
cereal_df[cereal_df["type"] == 'C']["rating"]
```

**Output:**

```
name  
100% Bran                    68.402973  
100% Natural Bran            33.983679  
All-Bran                     59.425505  
All-Bran with Extra Fiber    93.704912  
Almond Delight               34.384843  
                               ...      
Triples                      39.106174  
Trix                         27.753301  
Wheat Chex                   49.787445  
Wheaties                     51.592193  
Wheaties Honey Gold          36.187559  
Name: rating, Length: 74, dtype: float64
```

No change was made to the original dataframe.

The .loc accessor[] accesses the original dataframe in memory while standard selectors will create a copy of your selection (i.e., a new dataframe). Modifying the selection modifies the copy but not the original dataframe. Using the .loc[] accessor does the trick:

```
cereal_df.loc[cereal_df["type"] == 'C', "rating"] += 5  
cereal_df.loc[cereal_df["type"] == 'C', "rating"]
```

**Output:**

```
name  
100% Bran                    73.402973  
100% Natural Bran            38.983679  
All-Bran                     64.425505  
All-Bran with Extra Fiber    98.704912  
Almond Delight               39.384843  
                               ...      
Triples                      44.106174  
Trix                         32.753301  
Wheat Chex                   54.787445  
Wheaties                     56.592193  
Wheaties Honey Gold          41.187559  
Name: rating, Length: 74, dtype: float64
```

### [Step 11: Descriptive Statistics and Applying Functions in Pandas](#dpPanel10)

Descriptive statistics are among the most essential aspects of data science and we also need to be able to apply functions. We need to see how we can do this in Pandas when we have a series or a DataFrame. Thus, let’s:

* Calculate summary statistics for a series or a subset of a DataFrame.
* Apply a function to a pandas series or DataFrame.

Let's look at the canonical Titanic passenger dataset.

```
df = pd.read_csv('Data/titanic.csv', index_col=0)  
df.info()
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>  
Index: 891 entries, 1 to 891  
Data columns (total 11 columns):  
 #   Column    Non-Null Count  Dtype    
---  ------    --------------  -----    
 0   Survived  891 non-null    int64    
 1   Pclass    891 non-null    int64    
 2   Name      891 non-null    object   
 3   Sex       891 non-null    object   
 4   Age       714 non-null    float64  
 5   SibSp     891 non-null    int64    
 6   Parch     891 non-null    int64    
 7   Ticket    891 non-null    object   
 8   Fare      891 non-null    float64  
 9   Cabin     204 non-null    object   
 10  Embarked  889 non-null    object   
dtypes: float64(2), int64(4), object(5)  
memory usage: 83.5+ KB
```

```
df.head()
```

**Output:**

```
             Survived  Pclass  \  
PassengerId                       
1                   0       3     
2                   1       1     
3                   1       3     
4                   1       1     
5                   0       3     
  
                                                          Name     Sex   Age  \  
PassengerId                                                                      
1                                      Braund, Mr. Owen Harris    male  22.0     
2            Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0     
3                                       Heikkinen, Miss. Laina  female  26.0     
4                 Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0     
5                                     Allen, Mr. William Henry    male  35.0     
  
             SibSp  Parch            Ticket     Fare Cabin Embarked    
PassengerId                                                            
1                1      0         A/5 21171   7.2500   NaN        S    
2                1      0          PC 17599  71.2833   C85        C    
3                0      0  STON/O2. 3101282   7.9250   NaN        S    
4                1      0            113803  53.1000  C123        S    
5                0      0            373450   8.0500   NaN        S  
```

#### Calculating Column Statistics

For columns, we often are interested in calculating a particular statistic for one or a few columns. Happily, DataFrames and Series objects have many built-in methods that can calculate these summary statistics.

First, we can use the .select\_dtypes() method to select columns from a DataFrame of a particular data type. Here we will insist that the columns we extract are numeric only. This can be by passing in the 'number' string to include keyword argument.

```
df_numeric = df.select_dtypes(include='number')  
df_numeric.info()
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>  
Index: 891 entries, 1 to 891  
Data columns (total 6 columns):  
 #   Column    Non-Null Count  Dtype    
---  ------    --------------  -----    
 0   Survived  891 non-null    int64    
 1   Pclass    891 non-null    int64    
 2   Age       714 non-null    float64  
 3   SibSp     891 non-null    int64    
 4   Parch     891 non-null    int64    
 5   Fare      891 non-null    float64  
dtypes: float64(2), int64(4)  
memory usage: 48.7 KB
```

The general pattern for calculating a statistic across many columns of a DataFrame or for a particular column (i.e. a Series) goes as follows:

* DataFrame.particular\_statistic()
* Series.particular\_statistic()

Let's do this for the mean.

If we want to calculate the mean across these columns:

```
df_numeric.mean()
```

**Output:**

```
Survived     0.383838  
Pclass       2.308642  
Age         29.699118  
SibSp        0.523008  
Parch        0.381594  
Fare        32.204208  
dtype: float64
```

#### Mean

Calculating the mean for a particular column, where across a Series is the same syntax):

```
df_numeric['Fare'].mean()
```

**Output:**

```
32.204207968574636
```

The pattern is the same for statistics like the median, calculating percentiles, or the standard deviation, which should all remind you of numpy syntax.

#### Median

```
df_numeric.median()
```

**Output:**

```
Survived     0.0000  
Pclass       3.0000  
Age         28.0000  
SibSp        0.0000  
Parch        0.0000  
Fare        14.4542  
dtype: float64
```

```
df_numeric['Age'].median()
```

**Output:**

```
28.0
```

#### Percentiles/Quantiles

Now that we have looked at the mean and median, let’s consider percentiles and quartiles.

* The .quantile() method is similar to numpy's np.percentile function.
* The function takes in a decimal value between 0 and 1 with decimal value corresponding to a given percentile.
* The following calculates the tenth percentile:

```
# applied to a DataFrame -- calculates across many columns  
  
df_numeric.quantile(.1)
```

**Output:**

```
Survived     0.00  
Pclass       1.00  
Age         14.00  
SibSp        0.00  
Parch        0.00  
Fare         7.55  
Name: 0.1, dtype: float64
```

```
# applied to a Series  
  
df_numeric['Age'].quantile(.1)
```

**Output:**

```
14.0
```

#### Standard Deviation

The standard deviation can be computed for a series in a similar way.

```
# applied to a Series  
  
df_numeric.std(ddof=1)
```

**Output:**

```
Survived     0.486592  
Pclass       0.836071  
Age         14.526497  
SibSp        1.102743  
Parch        0.806057  
Fare        49.693429  
dtype: float64
```

```
df_numeric['Age'].std(ddof=1)
```

**Output:**

```
14.526497332334044
```

#### Other important statistics

Here other important descriptive statistics that you should be familiar with:

* .mode() -- the mode of the column
* .count() -- the count of the total number of entries in a column
* .var() -- the variance for the column
* .sum() -- the sum of all values in the column
* .cumsum() -- the cumulative sum, where each cell index contains the sum of all indices lower than, and including, itself

#### Useful summary methods for categorical columns

While we often seem focused on numeric data, in addition to .mode() there are a couple more descriptive statics we can use for categorical data:

* Unique entries in categorical column
* Counts for each unique entry

'Embarked' is a categorical column in our Titanic dataset:

```
df['Embarked'].head()
```

**Output:**

```
PassengerId  
1    S  
2    C  
3    S  
4    S  
5    S  
Name: Embarked, dtype: object
```

We often want to know the unique values that a categorical can take on: Series.unique()

```
df['Embarked'].unique()
```

**Output:**

```
array(['S', 'C', 'Q', nan], dtype=object)
```

It'd be good to know the breakdown of the counts in each class: Series.value\_counts()

```
df['Embarked'].value_counts()
```

**Output:**

```
Embarked  
S    644  
C    168  
Q     77  
Name: count, dtype: int64
```

Note that nan is not a class but stands for 'Not a Number' and signifies empty or missing value in pandas. This is why it is not included in the value\_counts().

### [Step 12: Transforming Series and DataFrames](#dpPanel11)

Sometimes we want to do more than simple pre-defined aggregations. Want to implement our own functions on pandas data structures.

* Series.map()
* Series.apply()
* DataFrame.apply()

#### Series.map()

Used for substituting each value in a Series with another value, that may be derived from:

* a dict
* a mapping function

Returns a new object. This can be a Series or a DataFrame depending on the form of the function. Let's create a new Series to see how this works:

```
orig_series = pd.Series([2,5,8], index = ['A', 'B', 'C'])  
orig_series
```

**Output:**

```
A    2  
B    5  
C    8  
dtype: int64
```

Creating the mapping dictionary and then applying it to our Series.

```
dict_mapper = {2: 2.5, 5: 7.2, 8: 3.9}  
orig_series.map(dict_mapper) 
```

**Output:**

```
A    2.5  
B    7.2  
C    3.9  
dtype: float64
```

We can also define a function that applies a numeric transformation and use the .map() method to transform each value in the Series accordingly.

```
def func(x):  
    return 2*x  
orig_series.map(func)
```

**Output:**

```
A     4  
B    10  
C    16  
dtype: int64
```

In general, you would use the .map() method for more complex mappings. A simple arithmetic operation like this can be accomplished via using Pandas vectorization implicitly (i.e., just multiply the Series directly by a constant).

```
2*orig_series
```

**Output:**

```
A     4  
B    10  
C    16  
dtype: int64
```

A more interesting use-case might be when you create mappings for binning continuous data using conditional logic. Here we define a function that checks whether a value for a paid Fare lies in a range and then returns a string denoting what bin that Fare belongs to:

```
def bin_fare(input):  
    if input <= 10:  
        return 'Low Fare'  
    elif (input > 10) & (input <= 40):  
        return 'Medium Fare'  
    elif input > 40:  
        return 'High Fare'
```

Applying this function to our Fare data in the titanic dataset yields the binning:

```
df_numeric['Fare'].map(bin_fare)
```

**Output:**

```
PassengerId  
1         Low Fare  
2        High Fare  
3         Low Fare  
4        High Fare  
5         Low Fare  
          ...       
887    Medium Fare  
888    Medium Fare  
889    Medium Fare  
890    Medium Fare  
891       Low Fare  
Name: Fare, Length: 891, dtype: object
```

```
df_numeric
```

**Output:**

```
             Survived  Pclass   Age  SibSp  Parch     Fare  
PassengerId                                                 
1                   0       3  22.0      1      0   7.2500  
2                   1       1  38.0      1      0  71.2833  
3                   1       3  26.0      0      0   7.9250  
4                   1       1  35.0      1      0  53.1000  
5                   0       3  35.0      0      0   8.0500  
...               ...     ...   ...    ...    ...      ...  
887                 0       2  27.0      0      0  13.0000  
888                 1       1  19.0      0      0  30.0000  
889                 0       3   NaN      1      2  23.4500  
890                 1       1  26.0      0      0  30.0000  
891                 0       3  32.0      0      0   7.7500  
  
[891 rows x 6 columns]
```

#### Series.apply():

Applies function elementwise to Series:

* Only applies functions
* Can do what map does w/ functions
* Can use functions that simply return a Series or even DataFrames

```
orig_series
```

**Output:**

```
A    2  
B    5  
C    8  
dtype: int64
```

*# did this with map. map is faster for this.*

```
orig_series.apply(func)
```

**Output:**

```
A     4  
B    10  
C    16  
dtype: int64
```

Series.apply() really shines when you want to do something a little more complicated.

For each element in original Series, compute powers of elements up to some order. Return these powers as a series.

```
# this returns a series [x, x**2, x**3,...up to highest order] for each value  
def new_func(x, highest_order = 5):  
      
    polynomial_series = pd.Series({'Order ' + str(n+1): x**(n+1) for n in range(highest_order)})  
      
    return polynomial_series
```

Using the .apply() method with new\_func, Pandas will run through each element of the original series:

* for each, element return a series of the powers from order 1 to order 5
* combine the series of powers for each element into a DataFrame

```
orig_series
```

```
A    2  
B    5  
C    8  
dtype: int64
```

```
# start with a Series. End up with a DataFrame.  
orig_series.apply(new_func)
```

**Output:**

```
   Order 1  Order 2  Order 3  Order 4  Order 5  
A        2        4        8       16       32  
B        5       25      125      625     3125  
C        8       64      512     4096    32768
```

#### DataFrame.apply()

As an extension of series.apply(), there is DataFrame.applu(). Takes in entire columns (or rows) of dataframe into function and applies transformations:

* Transformations can be applied column-wise or row-wise.
* The function can return a number, a Series, or a Dataframe.

As such the DataFrame.apply() method is pretty useful, flexible, and is capable of complex transformations.

Let's see an example. Suppose, for some reason we want the sum of the squares of all entries in the Age and Fares column respectively. Then we want to log transform the result for each column.

The function below breaks this down in steps. Each function is designed to accept a Series (representing a given column). Then we square each entry in the column and then take the sum of these squares. Finally, the log of this sum of squares is computed. Thus if the function takes in the data in the Age column (a Series) it will return a single value representing the log-squared-sum.

```
def log_sq_trans(x):  
    x_sq = x**2  
    summed_sq = np.sum(x_sq)  
    logsquaredsum = np.log(1 + summed_sq)  
      
    return logsquaredsum
```

Now we subset the DataFrame on Age and Fare and apply this function to the DataFrame. The .apply() method then takes in each column (Age and Fare) and computes the log-sum-squared for each. The axis = 0 (the default argument) ensures that the Series being accepted by the function are columns.

```
# axis = 0: applies function to each column   
df[['Age', 'Fare']].apply(log_sq_trans, axis = 0)
```

**Output:**

```
Age     13.567347  
Fare    14.953941  
dtype: float64
```

If for some reason you wanted to have the function accept the rows as argument (i.e., add the squares of Age and Fare for each row and log transforms the result), then you could just change to axis = 1.

```
df[['Age', 'Fare']].apply(log_sq_trans, axis = 1)
```

**Output:**

```
PassengerId  
1      6.287045  
2      8.783597  
3      6.606387  
4      8.305388  
5      7.163019  
         ...     
887    6.801283  
888    7.140453  
889    6.311558  
890    7.363280  
891    6.989393  
Length: 891, dtype: float6
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243587

Scraped At: 2026-05-14T20:56:33.047731
