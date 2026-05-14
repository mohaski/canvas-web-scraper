# Technical Lesson: Numeric and Boolean Data Types in Data Science

# Technical Lesson: Numeric and Boolean Data Types in Data Science

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Numeric and Boolean Data Types in Data Science

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[15-20 minutes]

You will often encounter tabular data involving numeric and True/False information. A classical example might be census data that includes, for a given district, the average number of people in a household, square mileage of the district area, median income, and  whether a district is urban or rural. Other examples might be engineering or scientific data.

Below we have an example from extrasolar planetary astronomy where various characteristics of confirmed extrasolar planets are tabulated.  Typical numeric measurements involve the number of moons that the planet has been measured to possess, orbital characteristics (i.e. orbital period in solar days), and whether a planet is in the habitable zone about its parent star. This type of data can be represented in Python respectively by integers (int), floats (float), and booleans (bool). We will see how to represent each type of data with the right Python data type, use cases for converting from one type to another, and the various methods that can be used to transform numeric and boolean types to a form one desires.

Here is a video walkthrough of the technical lesson.

[VIDEO LINK](https://player.vimeo.com/video/989669306?h=da3b2b333d)

### Instructions

Using the small selection of data from the Kepler Telescope Exoplanet Catalog below, we will navigate

* Integers
* Floats
* Binary Variables (Booleans)

Small selection of data from the Kepler Telescope Exoplanet Catalog

| Name | Distance (LY) | Orbital Period (Days) | Number of Moons | Habitable Zone | Potential for Liquid Water |
| --- | --- | --- | --- | --- | --- |
| Kepler-186f | 512 | 136 | 1 | TRUE | High |
| TRAPPIST-1d | 40 | 4.05 | 0 | TRUE | High |
| Gliese 581 g | 20 | 37 | 0 | FALSE | Possible |
| LHS 1140b | 40.5 | 38.1 | 0 | FALSE | Possible |
| KOI-3140b | 178 | 4.5 | 0 | FALSE | Low |
| Kepler-1708b | 5600 | 131 | 2 | FALSE | None |
| Kepler-452b | 1400 | 385 | 0 | FALSE | Likely |
| Kepler-10b | 186 | 0.8 | 0 | FALSE | None |
| HD 132563 b | 218 | 259.4 | 1 | FALSE | Possible |
| Kepler-442b | 1120 | 112 | 0 | FALSE | Possible |

We have loaded this data from a file into a list of lists using Python’s IO. It looks like this after the data loading is complete:

```
exo_data
```

```
[['Name',  
  'Distance (LY)',  
  'Orbital Period (Days)',  
  'Number of Moons',  
  'Habitable Zone',  
  'Potential for Liquid Water'],  
 ['Kepler-186f', '512', '136', '1', 'True', 'High'],  
 ['TRAPPIST-1d', '40', '4.05', '0', 'True', 'High'],  
 ['Gliese 581 g', '20', '37', '0', 'False', 'Possible'],  
 ['LHS 1140b', '40.5', '38.1', '0', 'False', 'Possible'],  
 ['KOI-3140b', '178', '4.5', '0', 'False', 'Low'],  
 ['Kepler-1708b', '5600', '131', '2', 'False', 'None'],  
 ['Kepler-452b', '1400', '385', '0', 'False', 'Likely'],  
 ['Kepler-10b', '186', '0.8', '0', 'False', 'None'],  
 ['HD 132563 b', '218', '259.4', '1', 'False', 'Possible'],  
 ['Kepler-442b', '1120', '112', '0', 'False', 'Possible']]
```

### Step 1

#### Dealing with Integers

The int variable type can be used to encode discrete  numeric quantities. The above data contains features that are explicitly expressed as integers or can be encoded as integers. These examples showcase the kinds of information that int is used to encode in data science.

##### 1. Recognizing and Converting Count Data to Integer Data Type

**Count Data: Number of Moons**

The number of moons a planet has must come in a whole number. Thus, it is stored as an int. This is true for all count data. Other examples include: the number of children someone has, age in its most commonly represented form: the number of whole years someone has lived through, the counts per minute of radioactive emission from an unstable nucleus, or the number of times a given word appears in a sentence.

**Converting count data to the int datatype**

A common issue when using base Python's file IO is that data loaded in from a text file will be in string format. We will need to convert the "Number of Moons" count data to int. This can be done with a for loop:

**Input:**

```
# loop over words. keep track of index so we can skip the first row  
for ix, row in enumerate(exo_data):  
    if ix > 0: # this skips the header line  
        row[3] = int(row[3]) # perform int conversion of the string
```

Now we perform a type check to see if elements of the column were converted.

**Input:**

```
type(exo_data[6][3]) is int
```

**Output:**

```
True
```

**Input:**

```
exo_data
```

**Output:**

```
 [['Name',  
  'Distance (LY)',  
  'Orbital Period (Days)',  
  'Number of Moons',  
  'Habitable Zone',  
  'Potential for Liquid Water'],  
 ['Kepler-186f', '512', '136', 1, 'True', 'High'],  
 ['TRAPPIST-1d', '40', '4.05', 0, 'True', 'High'],  
 ['Gliese 581 g', '20', '37', 0, 'False', 'Possible'],  
 ['LHS 1140b', '40.5', '38.1', 0, 'False', 'Possible'],  
 ['KOI-3140b', '178', '4.5', 0, 'False', 'Low'],  
 ['Kepler-1708b', '5600', '131', 2, 'False', 'None'],  
 ['Kepler-452b', '1400', '385', 0, 'False', 'Likely'],  
 ['Kepler-10b', '186', '0.8', 0, 'False', 'None'],  
 ['HD 132563 b', '218', '259.4', 1, 'False', 'Possible'],  
 ['Kepler-442b', '1120', '112', 0, 'False', 'Possible']]
```

So far so good. Inspecting the output from our table, we can see that the ‘Number of Moons’ column is no longer a string: there are no quotation marks around the numeric entries.

##### 2. Recognizing Ordinal Categoricals and Encoding as Integers

**Potential for Liquid Water: Ordinal Integer Encoding**

The 'Potential for Liquid Water' is an example of a **categorical**. However, this sort of categorical is distinct from the **nominal categorical** data that we have seen before. Let us inspect the 'Potential for Liquid Water' categorical attribute in more detail.

First we run a for loop to extract the values (ignoring the column name) and put these into a list **lqwater**:

**Input:**

```
lqwater = []  
for i, elem in enumerate(exo_data):  
    if i >0: # ignores header  
        lqwater.append(elem[5]) # desired categorical is the 6th column  
lqwater
```

**Output:**

```
 ['High',  
 'High',  
 'Possible',  
 'Possible',  
 'Low',  
 'None',  
 'Likely',  
 'None',  
 'Possible',  
 'Possible']
```

The planets are grouped by likelihood of their having water. The key point here is that there is an implied order here.

None < Low < Possible < Likely < High

Categoricals that possess this notion of a sequential progression are called **ordinal categoricals**. We can use integers to encode a progression or sequence like this (provided it makes sense to represent the category on a uniform scale). Thus in our case:

None < Low < Possible < Likely < High --> 0 < 1 < 2 < 3 < 4

One way to implement this in Base Python is to create a dictionary that defines the categorical string-to-integer mapping and then to loop through the rows of the exoplanet data replacing the string values of the categorical with the integer. This is what we do below:

**Input:**

```
value_mapper = {'None': 0, 'Low': 1, 'Possible': 2, 'Likely': 3, 'High': 4}  
for i, row in enumerate(exo_data):  
    if i > 0:  
        row[5] = value_mapper[row[5]] # get the integer value corresponding to the ordinal categorical and reassign entry  
exo_data
```

**Output:**

```
 [['Name',  
  'Distance (LY)',  
  'Orbital Period (Days)',  
  'Number of Moons',  
  'Habitable Zone',  
  'Potential for Liquid Water'],  
 ['Kepler-186f', '512', '136', 1, 'True', 4],  
 ['TRAPPIST-1d', '40', '4.05', 0, 'True', 4],  
 ['Gliese 581 g', '20', '37', 0, 'False', 2],  
 ['LHS 1140b', '40.5', '38.1', 0, 'False', 2],  
 ['KOI-3140b', '178', '4.5', 0, 'False', 1],  
 ['Kepler-1708b', '5600', '131', 2, 'False', 0],  
 ['Kepler-452b', '1400', '385', 0, 'False', 3],  
 ['Kepler-10b', '186', '0.8', 0, 'False', 0],  
 ['HD 132563 b', '218', '259.4', 1, 'False', 2],  
 ['Kepler-442b', '1120', '112', 0, 'False', 2]]
```

A planet's potential for possessing liquid water is now integer encoded on a scale from 0-4 ranging from None to High. Integers are used commonly for this kind of ordinal encoding in data science. One example might be a customer survey where respondents can answer Dissatisfied, Neutral, Satisfied encoded as 0,1, 2.

### Step 2

#### Dealing with Continuous Numeric Data

1. Converting to Floats

Floats are used to represent fractional quantities or variables whose value could fall in a continuous range. Taking a look at the data above, we can see that the following quantities could be represented by floats:

* Distance (LY): Distance in light years from Earth
* Orbital Period (Days): Days exoplanet takes to make a revolution about its sun.

These quantities are known at a greater precision than integer value in the given units. The first thing that needs to be done is to convert the columns from strings to floats. Again, we can use a for-loop to do this:

**Input:**

```
for i, row in enumerate(exo_data):  
    if i > 0:  
        row[1] = float(row[1]) # convert Distance (LY) to float  
        row[2] = float(row[2]) # convert Orbital Periods (Days) to float  
print("Distance (LY) is a : " + str({type(exo_data[1][1])}))  
print("Orbital Period (Days) is a : " + str({type(exo_data[1][2])}))  
exo_data
```

**Output:**

```
Distance (LY) is a : {<class 'float'>}  
Orbital Period (Days) is a : {<class 'float'>}  
  
[['Name',  
  'Distance (LY)',  
  'Orbital Period (Days)',  
  'Number of Moons',  
  'Habitable Zone',  
  'Potential for Liquid Water'],  
 ['Kepler-186f', 512.0, 136.0, 1, 'True', 4],  
 ['TRAPPIST-1d', 40.0, 4.05, 0, 'True', 4],  
 ['Gliese 581 g', 20.0, 37.0, 0, 'False', 2],  
 ['LHS 1140b', 40.5, 38.1, 0, 'False', 2],  
 ['KOI-3140b', 178.0, 4.5, 0, 'False', 1],  
 ['Kepler-1708b', 5600.0, 131.0, 2, 'False', 0],  
 ['Kepler-452b', 1400.0, 385.0, 0, 'False', 3],  
 ['Kepler-10b', 186.0, 0.8, 0, 'False', 0],  
 ['HD 132563 b', 218.0, 259.4, 1, 'False', 2],  
 ['Kepler-442b', 1120.0, 112.0, 0, 'False', 2]]
```

1. Transforming Continuous Numeric Variables

We have successfully converted the strings to floats. We can now apply arithmetic operations (e.g., multiply or add a constant) or mathematical functions (e.g., square, square root, log) to these numeric columns. Changing units of a numeric feature is a fairly common example of this. Let's say that we want to convert the units of orbital period from days to years. This involves dividing all the elements in the 'orbital period' column by a scale factor. That scale factor is 365.242374 days/year (365 days, 5 hours, 49 minutes, 1.1 seconds in a year). We can do this by some good old for-looping.

**Input:**

```
for i, row in enumerate(exo_data):  
    if i > 0:  
        row[2] = row[2]/365.242374  # the 3rd column is orbital period  
# We need to update our column label to reflect the change in units!  
exo_data[0][2] = 'Orbital Period (Years)'    
exo_data
```

**Output:**

```
 [['Name',  
  'Distance (LY)',  
  'Orbital Period (Years)',  
  'Number of Moons',  
  'Habitable Zone',  
  'Potential for Liquid Water'],  
 ['Kepler-186f', 512.0, 0.37235548140424696, 1, 'True', 4],  
 ['TRAPPIST-1d', 40.0, 0.011088527203582353, 0, 'True', 4],  
 ['Gliese 581 g', 20.0, 0.10130259420556718, 0, 'False', 2],  
 ['LHS 1140b', 40.5, 0.10431429295221918, 0, 'False', 2],  
 ['KOI-3140b', 178.0, 0.01232058578175817, 0, 'False', 1],  
 ['Kepler-1708b', 5600.0, 0.3586659416467379, 2, 'False', 0],  
 ['Kepler-452b', 1400.0, 1.0540945613281991, 0, 'False', 3],  
 ['Kepler-10b', 186.0, 0.0021903263612014527, 0, 'False', 0],  
 ['HD 132563 b', 218.0, 0.7102133226195709, 1, 'False', 2],  
 ['Kepler-442b', 1120.0, 0.30664569056820334, 0, 'False', 2]]
```

**Input:**

```
type(exo_data[1][2])
```

**Output:**

```
float
```

The orbital period is now in years and is still represented as a float.

Python also offer supports for many mathematical functions through the math module:

* math.sqrt
* math.sin
* math.cos
* math.log
* and more...

Let's apply the log function to the Distance (LY). This is an operation done on astrophysical distances which can vary orders of magnitude. Here we for-loop again and apply our math function to the float values -- getting floats back in return.

**Input:**

```
import math # you need to import the module before you can use the functions  
for i, row in enumerate(exo_data):  
    if i > 0:  
        row[1] = math.log(row[1])  # the 2rd column is distance to Earth  
  
# We need to update our column label to reflect the change in units!  
exo_data[0][1] = 'log(D [ly])'    
exo_data
```

**Output:**

```
 [[['Name',  
  'log(D [ly])',  
  'Orbital Period (Years)',  
  'Number of Moons',  
  'Habitable Zone',  
  'Potential for Liquid Water'],  
 ['Kepler-186f', 6.238324625039508, 0.37235548140424696, 1, 'True', 4],  
 ['TRAPPIST-1d', 3.6888794541139363, 0.011088527203582353, 0, 'True', 4],  
 ['Gliese 581 g', 2.995732273553991, 0.10130259420556718, 0, 'False', 2],  
 ['LHS 1140b', 3.7013019741124933, 0.10431429295221918, 0, 'False', 2],  
 ['KOI-3140b', 5.181783550292085, 0.01232058578175817, 0, 'False', 1],  
 ['Kepler-1708b', 8.630521876723241, 0.3586659416467379, 2, 'False', 0],  
 ['Kepler-452b', 7.24422751560335, 1.0540945613281991, 0, 'False', 3],  
 ['Kepler-10b', 5.225746673713202, 0.0021903263612014527, 0, 'False', 0],  
 ['HD 132563 b', 5.384495062789089, 0.7102133226195709, 1, 'False', 2],  
 ['Kepler-442b', 7.02108396428914, 0.30664569056820334, 0, 'False', 2]]
```

The distance has successfully been log transformed. You can see that the scale of variation in this feature has been squashed (whereas before it varied three orders of magnitude).

### Step 3

#### Dealing with and Creating Binary Variables

1. Converting String Entities to Boolean Data Types

Examining the data, there is a column that tells us whether an exoplanet is or is not in the Habitable zone around its parent star. This is an example of a \*\*binary categorical\*\* where each option is currently encoded as 'True' and 'False' strings and are boolean in nature. It makes sense to convert the string entries to boolean datatypes. A conditional check using if, elif structures checking on string matching will do what we want: yield the boolean True if the string is 'True', and False if 'False'.

**Input:**

```
for i, row in enumerate(exo_data):  
  
    if i > 0:  
  
        if row[4] == 'True': # 5th column is whether planet is in Habitable zone  
  
            row[4] = True    
  
        elif row[4] == 'False':  
  
            row[4] = False  
  
   
  
print(type(exo_data[1][4])) # print type on element in column for checking  
  
exo_data
```

**Output:**

```
<class 'bool'>  
  
[['Name',  
  'log(D [ly])',  
  'Orbital Period (Years)',  
  'Number of Moons',  
  'Habitable Zone',  
  'Potential for Liquid Water'],  
 ['Kepler-186f', 6.238324625039508, 0.37235548140424696, 1, True, 4],  
 ['TRAPPIST-1d', 3.6888794541139363, 0.011088527203582353, 0, True, 4],  
 ['Gliese 581 g', 2.995732273553991, 0.10130259420556718, 0, False, 2],  
 ['LHS 1140b', 3.7013019741124933, 0.10431429295221918, 0, False, 2],  
 ['KOI-3140b', 5.181783550292085, 0.01232058578175817, 0, False, 1],  
 ['Kepler-1708b', 8.630521876723241, 0.3586659416467379, 2, False, 0],  
 ['Kepler-452b', 7.24422751560335, 1.0540945613281991, 0, False, 3],  
 ['Kepler-10b', 5.225746673713202, 0.0021903263612014527, 0, False, 0],  
 ['HD 132563 b', 5.384495062789089, 0.7102133226195709, 1, False, 2],  
 ['Kepler-442b', 7.02108396428914, 0.30664569056820334, 0, False, 2]]
```

1. Convert Boolean to Binary Integer

The Habitable zone column is now of type bool. This sort of binary data can also be integer encoded: 0 for False, 1 for True. In fact, Python already understands this conversion. When you call the int() method on a bool it will return 0 if False and 1 if True.

**Input:**

```
print(int(False))  
print(int(True))
```

**Output:**

```
0  
1
```

1. Creating a Binary Categorical

The 'Habitable Zone' was included in the dataset as an explicit binary categorical. There are cases where we may want to create a binary categorical from other kinds of data. A common scenario where we want to create a boolean from a numeric feature encoding quantity (like a float). We might be interested in recording whether a given numeric feature lies above or below a certain threshold. That threshold might denote an important qualitative shift in the behavior of the data at large.

Let us say that we are interested in binning our exoplanetary data into two regimes: close and distant. Some thinking and domain knowledge might tell us that a threshold of 5.0 on our log-transformed scale is what we want. Planets that lie at log-distances greater than 5.0 are bucketed as distant and those less than or equal to 5.0 will be bucketed as close. We can create a new binary categorical Is\_Close that measures True if the planet is close (log D <= 5.0) and False otherwise.

We will use Python comparison operators to yield the required booleans based off of the threshold. We will need to take care of the fact that we are creating a new column, thus we will be appending the new column name and boolean values onto each row.

**Input:**

```
for i, row in enumerate(exo_data):  
    if i == 0:  
        row.append('Is_Close') # create the new column name  
    else:  
        # the 2nd row is log distance.  
        # The grouped comparison statement yields the required Boolean  
        row.append((row[1] <= 5.0 ))  
  
exo_data
```

**Output:**

```
[['Name',  
  'log(D [ly])',  
  'Orbital Period (Years)',  
  'Number of Moons',  
  'Habitable Zone',  
  'Potential for Liquid Water',  
  'Is_Close'],  
 ['Kepler-186f', 6.238324625039508, 0.37235548140424696, 1, True, 4, False],  
 ['TRAPPIST-1d', 3.6888794541139363, 0.011088527203582353, 0, True, 4, True],  
 ['Gliese 581 g', 2.995732273553991, 0.10130259420556718, 0, False, 2, True],  
 ['LHS 1140b', 3.7013019741124933, 0.10431429295221918, 0, False, 2, True],  
 ['KOI-3140b', 5.181783550292085, 0.01232058578175817, 0, False, 1, False],  
 ['Kepler-1708b', 8.630521876723241, 0.3586659416467379, 2, False, 0, False],  
 ['Kepler-452b', 7.24422751560335, 1.0540945613281991, 0, False, 3, False],  
 ['Kepler-10b', 5.225746673713202, 0.0021903263612014527, 0, False, 0, False],  
 ['HD 132563 b', 5.384495062789089, 0.7102133226195709, 1, False, 2, False],  
 ['Kepler-442b', 7.02108396428914, 0.30664569056820334, 0, False, 2, False]] 
```

We can see that we have successfully binned the continuous log-distance data into two groups encoded by a boolean.

### Summary

In this lesson, you saw how to convert your imported data (by default in string format) to appropriate numeric and boolean data types. You also saw how Python could be used to transform your data to and from numeric form in a variety of ways (e.g., numeric to binary categorical, ordinal categorical to integer)  and induce useful mathematical transformations on your data (e.g., log transformation of exoplanet distance).  In particular you gained familiarity with the `int`, `float`, and `bool` data types and how to use associated methods to make transformations of use in analyzing exoplanetary data.

Understanding variable types – integers, floats, strings, and booleans – empowered you to transform raw data into a usable format. Upon import, data may not be optimized. You identified and saw how to convert each element into an appropriate type based on the information it represents (e.g., numerical data as integers/floats, categorical data as strings). Choosing the correct type ensures both accurate representation and efficient manipulation during analysis.

Once data was assigned the appropriate type, Python's functionalities for cleaning and transformation became readily available. We could call on built-in methods for stripping and case normalization applicable to string data, or mathematical functions for unit and scale conversion on numerical data.

By mastering these concepts and their applications, you will have gained the capability to effectively work with and prepare data for further exploration and analysis within the Python environment. This newfound skillset empowers you to tackle real-world data challenges and extract valuable insights. But you are no master yet. So it is time to stretch a bit, crack your Python knuckles, and get some practice in.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243496

Scraped At: 2026-05-14T20:46:58.743964
