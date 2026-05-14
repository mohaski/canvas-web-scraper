# Practice: Data Cleaning with Pandas

# Practice: Data Cleaning with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Data Cleaning with Pandas

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

Austin Animal Center is the municipal shelter for Austin, TX. You are a consulting data scientist helping the shelter understand the factors contributing to various final outcomes of sheltered animals (adoption, euthanasia, etc.). They want a tool that will use this information to automatically flag animals that are at risk of ending up being euthanized. You have been provided with the data source.

Before conducting EDA and model building, you will need to clean your data. This will require you to:

* Handle missing data, and recognize when different strategies for handling missing data would be appropriate
* Deal with duplicate data
* Use string vectorized methods to transform object-type columns
* Use DataFrame vectorized methods to apply custom transformations to data

### Resources

* [Austin Animal Center Data Source


  Links to an external site.](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)
* [GitHub Repository (Practice 2)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m5)

### Instructions

Before you begin, import the necessary libraries: pandas, numpy, and matplotlib pyplot using correct aliases.

```
# Imports  
  
import pandas as pd  
import numpy as np  
  
import matplotlib.pyplot as plt
```

### Step 1

Load the animal center outcomes data as df.

### Step 2

Inspect the head.

### Step 3

Get information on columns: null count and data types in DataFrame.

### Step 4

DateTime and Date of Birth are dtype object. Convert them to an appropriate data type.

### Step 5

The Outcome Subtype has a lot of nulls (more than half). It's not reasonable to impute these many missing values with a simple imputation strategy. Drop this feature.

### Step 6

Return a dataframe with all duplicated rows in the dataset.

### Step 7

Remove all duplicates from the dataframe.

Age has a few nulls. Notice that the dtype for the column is object and the entries are strings:

```
# run this cell without changes  
print(df['Age upon Outcome'].isna().sum()) # there are 5 NaNs  
print(df['Age upon Outcome'].dtype)   
print(df['Age upon Outcome'].head())
```

The ages are strings with the number and a particular unit of time (days, months, or years). This needs to be cleaned up.

### Step 8

Split the number and unit and put these into two new columns named Age Number and Age Unit respectively.

```
# your code here  
  
print(df.columns)
```

### Step 9

Convert the Ages to be in units of days. First convert the Age Unit column to its corresponding number in days. The dictionary for unit conversion is provided:

```
# Providing this dictionary to capture age values in # days (not perfect)  
age_vals = {  
    'years': 365,  
    'year': 365,  
    'months': 30,  
    'month': 30,  
    'weeks': 7,  
    'week': 7,  
    'days': 1,  
    'day': 1  
}  
  
# your code here
```

### Step 10

Convert the Age Number column to 'Int16' datatype. Then express the Age Upon Outcome in days using the Age Number and converted Age Unit columns.

### Step 11

Plot a histogram of Age upon Outcome along with the median of the column.

### Step 12

The median looks to be a measure of central tendency. Impute `Age upon Outcome' with the median.

### Step 13

The string cleaning and statistical imputation did work OK, but in this case there's a much better option: computing the Age upon Outcome from two other columns in the dataset, DateTime and Date of Birth. Neither of these columns have nulls. Take the difference of the two columns, convert to days (use the vectorized dt.days attribute), and assign the resulting series to Age upon Outcome.

```
# your code here  
  
  
print("There are " + str(df['Age upon Outcome'].isna().sum()) + " missing values.")  
print(df['Age upon Outcome'].head())
```

### Step 14

Use .map() to turn the Sex upon Outcome column into a category with three values: Fixed, Intact, or Unknown. You have been provided with a function fixed\_mapper that transforms the distinct categories to our desired three values (Fixed, Intact, Unknown). This function will turn any NaNs to category Unknown*—*explicitly making missing values its own category.

Create a new column Grouped Sex upon Outcome that results from transforming Sex upon Outcome with fixed\_mapper.

```
# run cell without changes  
  
# print Categories in column  
print(df['Sex upon Outcome'].unique())  
  
# Provided function  
def fixed_mapper(status):  
    '''  
    Takes in the current status of animals and outputs whether they have been fixed  
    '''  
    if status in ['Neutered Male', 'Spayed Female']:  
        return 'Fixed'  
    elif status in ['Intact Male', 'Intact Female']:  
        return 'Intact'  
    else:  
        return 'Unknown'
```

### Step 15

Create a bar graph to display the counts in each category for Grouped Sex upon Outcome.

### Step 16

Outcome Type is the target we are trying to predict. Count the number of nulls here.

### Step 17

Drop all rows containing nulls in the Outcome Type column.

Printing nulls in the dataset now:

```
# Sanity Check. Run cell without changes.  
df.isna().sum()
```

### Step 18

There are a lot of nulls in the Name column. While the exact name of an animal might not matter too much, maybe whether the animal has a name might indicate whether it was owned before. This might conceivably impact outcome for adoption.

Thus, build a binary categorical variable that indicates whether a name is missing (i.e., an indicator for whether a value is null or not). This should be a new column Name Missing.

### Step 19

Create a new dataframe clean\_df where all columns with NaNs have been dropped.

### Step 20

Print info on the cleaned DataFrame and save the cleaned DataFrame to a file cleaned\_animal\_data.csv.

### Solution

### Select for Solution

#### Step 1

```
df = pd.read_csv('data/Austin_Animal_Center_Outcomes_022822.csv')
```

#### Step 2

```
df.head()
```

**Expected Output:**

```
  Animal ID   Name                DateTime MonthYear Date of Birth  \  
0   A794011  Chunk  05/08/2019 06:20:00 PM  May 2019    05/02/2017     
1   A776359  Gizmo  07/18/2018 04:02:00 PM  Jul 2018    07/12/2017     
2   A821648    NaN  08/16/2020 11:38:00 AM  Aug 2020    08/16/2019     
3   A720371  Moose  02/13/2016 05:59:00 PM  Feb 2016    10/08/2015     
4   A674754    NaN  03/18/2014 11:47:00 AM  Mar 2014    03/12/2014     
  
  Outcome Type Outcome Subtype Animal Type Sex upon Outcome Age upon Outcome  \  
0    Rto-Adopt             NaN         Cat    Neutered Male          2 years     
1     Adoption             NaN         Dog    Neutered Male           1 year     
2   Euthanasia             NaN       Other          Unknown           1 year     
3     Adoption             NaN         Dog    Neutered Male         4 months     
4     Transfer         Partner         Cat      Intact Male           6 days     
  
                                Breed              Color    
0              Domestic Shorthair Mix  Brown Tabby/White    
1             Chihuahua Shorthair Mix        White/Brown    
2                             Raccoon               Gray    
3  Anatol Shepherd/Labrador Retriever               Buff    
4              Domestic Shorthair Mix       Orange Tabby  
```

#### Step 3

```
df.info()
```

**Expected Output:**

```
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 137100 entries, 0 to 137099  
Data columns (total 12 columns):  
 #   Column            Non-Null Count   Dtype   
---  ------            --------------   -----   
 0   Animal ID         137100 non-null  object  
 1   Name              96098 non-null   object  
 2   DateTime          137100 non-null  object  
 3   MonthYear         137100 non-null  object  
 4   Date of Birth     137100 non-null  object  
 5   Outcome Type      137076 non-null  object  
 6   Outcome Subtype   62656 non-null   object  
 7   Animal Type       137100 non-null  object  
 8   Sex upon Outcome  137098 non-null  object  
 9   Age upon Outcome  137095 non-null  object  
 10  Breed             137100 non-null  object  
 11  Color             137100 non-null  object  
dtypes: object(12)  
memory usage: 12.6+ MB
```

#### Step 4

```
# your code here  
df['DateTime']=pd.to_datetime(df['DateTime']) # warning may be thrown -- it's fine.  
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])
```

```
# inspect after changing data types  
df.info()
```

**Expected Output:**

```
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 137100 entries, 0 to 137099  
Data columns (total 12 columns):  
 #   Column            Non-Null Count   Dtype           
---  ------            --------------   -----           
 0   Animal ID         137100 non-null  object          
 1   Name              96098 non-null   object          
 2   DateTime          137100 non-null  datetime64[ns]  
 3   MonthYear         137100 non-null  object          
 4   Date of Birth     137100 non-null  datetime64[ns]  
 5   Outcome Type      137076 non-null  object          
 6   Outcome Subtype   62656 non-null   object          
 7   Animal Type       137100 non-null  object          
 8   Sex upon Outcome  137098 non-null  object          
 9   Age upon Outcome  137095 non-null  object          
 10  Breed             137100 non-null  object          
 11  Color             137100 non-null  object          
dtypes: datetime64[ns](2), object(10)  
memory usage: 12.6+ MB
```

#### Step 5

```
# your code here  
df = df.drop(columns=['Outcome Subtype'])  
  
# outcome subtype should no longer be in the list of columns  
print(df.columns)
```

**Expected Output:**

```
Index(['Animal ID', 'Name', 'DateTime', 'MonthYear', 'Date of Birth',  
       'Outcome Type', 'Animal Type', 'Sex upon Outcome', 'Age upon Outcome',  
       'Breed', 'Color'],  
      dtype='object')
```

#### Step 6

```
df[df.duplicated()]
```

**Expected Output:**

```
       Animal ID      Name            DateTime MonthYear Date of Birth  \  
29       A698049     Luigi 2015-03-16 14:50:00  Mar 2015    2014-06-05     
237      A698049     Luigi 2015-03-16 14:50:00  Mar 2015    2014-06-05     
395      A698049     Luigi 2015-03-16 14:50:00  Mar 2015    2014-06-05     
9087     A815987  Princess 2020-04-13 16:56:00  Apr 2020    2019-04-02     
16881    A761936       NaN 2017-11-16 12:54:00  Nov 2017    2017-01-12     
24054    A783234  Princess 2019-01-13 16:39:00  Jan 2019    2016-10-27     
50932    A682781       NaN 2014-07-03 09:00:00  Jul 2014    2013-01-02     
56950    A683782       NaN 2014-07-16 09:00:00  Jul 2014    2014-02-15     
65106    A686827       NaN 2014-08-28 09:00:00  Aug 2014    2012-02-27     
75009    A755687       NaN 2017-08-07 13:50:00  Aug 2017    2014-08-07     
76421    A660948      *Roy 2013-11-03 18:16:00  Nov 2013    2013-07-08     
85290    A748204       Bob 2017-05-04 18:04:00  May 2017    2017-02-04     
91386    A755088   Machete 2017-08-19 00:00:00  Aug 2017    2016-09-29     
92570    A811566     Bubby 2020-01-09 17:22:00  Jan 2020    2018-07-09     
103917   A696688      Mari 2015-03-26 19:05:00  Mar 2015    2012-02-10     
105682   A764464    Pepper 2018-09-18 14:28:00  Sep 2018    2017-10-15     
111474   A797007      Ummi 2019-06-09 16:33:00  Jun 2019    2009-12-08     
127033   A773428   *Atreyu 2018-06-07 09:31:00  Jun 2018    2018-05-04     
130074   A695798       Jim 2015-01-23 12:34:00  Jan 2015    2014-02-23     
134101   A846569   A846569 2021-12-04 10:34:00  Dec 2021    2021-06-15     
  
           Outcome Type Animal Type Sex upon Outcome Age upon Outcome  \  
29             Transfer         Cat    Spayed Female         9 months     
237            Transfer         Cat    Spayed Female         9 months     
395            Transfer         Cat    Spayed Female         9 months     
9087    Return to Owner         Dog    Intact Female           1 year     
16881          Transfer         Dog      Intact Male        10 months     
24054         Rto-Adopt         Dog    Spayed Female          2 years     
50932          Transfer         Cat    Neutered Male           1 year     
56950          Transfer         Cat    Neutered Male         4 months     
65106          Transfer         Cat    Spayed Female          2 years     
75009          Disposal       Other          Unknown          3 years     
76421          Adoption         Cat    Neutered Male         3 months     
85290          Adoption         Cat    Neutered Male         2 months     
91386          Adoption         Dog    Spayed Female        10 months     
92570   Return to Owner         Cat    Neutered Male           1 year     
103917         Adoption         Cat    Spayed Female          3 years     
105682         Transfer         Dog    Spayed Female        11 months     
111474             Died         Dog    Neutered Male          9 years     
127033             Died         Cat      Intact Male          4 weeks     
130074       Euthanasia         Cat    Neutered Male        10 months     
134101         Adoption         Dog    Neutered Male         5 months     
  
                                  Breed              Color    
29             Domestic Medium Hair Mix        Black/White    
237            Domestic Medium Hair Mix        Black/White    
395            Domestic Medium Hair Mix        Black/White    
9087                      Cairn Terrier        White/Brown    
16881              Scottish Terrier Mix      Brown Brindle    
24054             Collie Smooth/Pointer              Brown    
50932            Domestic Shorthair Mix        White/Black    
56950            Domestic Shorthair Mix        Brown Tabby    
65106            Domestic Shorthair Mix             Calico    
75009                           Bat Mix              Brown    
76421            Domestic Shorthair Mix  Brown Tabby/White    
85290            Domestic Shorthair Mix         White/Blue    
91386             Australian Kelpie Mix        Black/White    
92570                Domestic Shorthair              White    
103917           Domestic Shorthair Mix       Calico/White    
105682  Soft Coated Wheaten Terrier Mix     Black/Tricolor    
111474                 Miniature Poodle              White    
127033           Domestic Shorthair Mix       Orange Tabby    
130074           Domestic Shorthair Mix             Orange    
134101        Australian Cattle Dog Mix           Red Tick  
```

#### Step 7

```
# your code here  
df = df.drop_duplicates()
```

Age has a few nulls. Notice that the dtype for the column is object and the entries are strings:

```
# run this cell without changes  
print(df['Age upon Outcome'].isna().sum()) # there are 5 NaNs  
print(df['Age upon Outcome'].dtype)   
print(df['Age upon Outcome'].head())
```

**Expected Output:**

```
5  
object  
0     2 years  
1      1 year  
2      1 year  
3    4 months  
4      6 days  
Name: Age upon Outcome, dtype: object
```

#### Step 8

```
# In order to create the histogram, we need to drop the nas  
df = df.dropna()  
  
# Split out the age number and age unit - using string methods!  
df['Age Number'] = df['Age upon Outcome'].str.split(" ").str[0]  
df['Age Unit'] = df['Age upon Outcome'].str.split(" ").str[1]  
  
print(df.columns)
```

**Expected Output:**

```
Index(['Animal ID', 'Name', 'DateTime', 'MonthYear', 'Date of Birth',  
       'Outcome Type', 'Animal Type', 'Sex upon Outcome', 'Age upon Outcome',  
       'Breed', 'Color', 'Age Number', 'Age Unit'],  
      dtype='object')
```

#### Step 9

```
# Providing this dictionary to capture age values in # days (not perfect)  
age_vals = {  
    'years': 365,  
    'year': 365,  
    'months': 30,  
    'month': 30,  
    'weeks': 7,  
    'week': 7,  
    'days': 1,  
    'day': 1  
}  
  
# replace None with your code  
df['Age Unit'] = df['Age Unit'].map(age_vals)  
  
print(df['Age Unit'].head())
```

**Expected Output:**

```
0    365.0  
1    365.0  
2    365.0  
3     30.0  
4      1.0  
Name: Age Unit, dtype: float64
```

#### Step 10

```
# convert to integer  
df['Age Number'] = df['Age Number'].astype('Int16')  
  
# recalculate Age Upon Outcome in days  
df['Age upon Outcome'] = df['Age Number']*df['Age Unit']  
  
print(df['Age upon Outcome'].head())
```

**Expected Output:**

```
0    730.0  
1    365.0  
2    365.0  
3    120.0  
4      6.0  
Name: Age upon Outcome, dtype: Float64
```

#### Step 11

```
import matplotlib.pyplot as plt  
  
fig, ax = plt.subplots()  
ax.hist(df['Age upon Outcome'],bins = 30)  
ax.axvline(df['Age upon Outcome'].median(), c = 'r', linestyle = '--')  
plt.show()
```

**Expected Output:**

#### ![Histogram of age upon outcome](https://moringa.instructure.com/courses/1406/files/625042/download) Step 12

```
# your code here  
  
df['Age upon Outcome'] = df['Age upon Outcome'].fillna(df['Age upon Outcome'].median())  
  
# this should now be zero.  
df['Age upon Outcome'].isna().sum()
```

**Expected Output:**

```
0
```

#### Step 13

```
df['Age upon Outcome'] = (df['DateTime'] - df['Date of Birth']).dt.days  
  
print("There are " + str(df['Age upon Outcome'].isna().sum()) + " missing values.")  
print(df['Age upon Outcome'].head())
```

**Expected Output:**

```
There are 0 missing values.  
0    736  
1    371  
2    366  
3    128  
4      6  
Name: Age upon Outcome, dtype: int64
```

There was no guesswork that was required to impute the values in the Age upon Outcome value.

#### Step 14

```
# print Categories in column  
print(df['Sex upon Outcome'].unique())  
  
# Provided function  
def fixed_mapper(status):  
    '''  
    Takes in the current status of animals and outputs whether they have been fixed  
    '''  
    if status in ['Neutered Male', 'Spayed Female']:  
        return 'Fixed'  
    elif status in ['Intact Male', 'Intact Female']:  
        return 'Intact'  
    else:  
        return 'Unknown' 
```

**Expected Output:**

```
['Neutered Male' 'Unknown' 'Intact Male' 'Spayed Female' 'Intact Female'  
 nan]
```

```
# Your code here  
df['Grouped Sex upon Outcome'] = df['Sex upon Outcome'].map(fixed_mapper)  
  
df[['Grouped Sex upon Outcome']].head()
```

**Expected Output:**

```
  Grouped Sex upon Outcome  
0                    Fixed  
1                    Fixed  
2                  Unknown  
3                    Fixed  
4                   Intact
```

#### Step 15

```
df['Grouped Sex upon Outcome'].value_counts().plot(kind='bar');
```

**Expected Output:**

 
![Bar chart showing animal numbers and grouped sex upon outcome](https://moringa.instructure.com/courses/1406/files/625170/download)

#### Step 16

```
# Your code here  
df['Outcome Type'].isna().sum()
```

**Expected Output:**

```
24
```

#### Step 17

```
# Your code here  
df.dropna(subset=['Outcome Type'], inplace=True)
```

Printing nulls in the dataset now:

```
# Sanity Check  
df.isna().sum()
```

**Expected Output:**

```
Animal ID                       0  
Name                        40987  
DateTime                        0  
MonthYear                       0  
Date of Birth                   0  
Outcome Type                    0  
Animal Type                     0  
Sex upon Outcome                1  
Age upon Outcome                0  
Breed                           0  
Color                           0  
Age Number                      4  
Age Unit                        4  
Grouped Sex upon Outcome        0  
dtype: int64
```

#### Step 18

```
# Your code here  
df['Name Missing'] = df['Name'].isna()  
df.head()
```

**Expected Output:**

```
  Animal ID   Name            DateTime MonthYear Date of Birth Outcome Type  \  
0   A794011  Chunk 2019-05-08 18:20:00  May 2019    2017-05-02    Rto-Adopt     
1   A776359  Gizmo 2018-07-18 16:02:00  Jul 2018    2017-07-12     Adoption     
2   A821648    NaN 2020-08-16 11:38:00  Aug 2020    2019-08-16   Euthanasia     
3   A720371  Moose 2016-02-13 17:59:00  Feb 2016    2015-10-08     Adoption     
4   A674754    NaN 2014-03-18 11:47:00  Mar 2014    2014-03-12     Transfer     
  
  Animal Type Sex upon Outcome  Age upon Outcome  \  
0         Cat    Neutered Male               736     
1         Dog    Neutered Male               371     
2       Other          Unknown               366     
3         Dog    Neutered Male               128     
4         Cat      Intact Male                 6     
  
                                Breed              Color  Age Number  \  
0              Domestic Shorthair Mix  Brown Tabby/White           2     
1             Chihuahua Shorthair Mix        White/Brown           1     
2                             Raccoon               Gray           1     
3  Anatol Shepherd/Labrador Retriever               Buff           4     
4              Domestic Shorthair Mix       Orange Tabby           6     
  
   Age Unit Grouped Sex upon Outcome  Name Missing    
0     365.0                    Fixed         False    
1     365.0                    Fixed         False    
2     365.0                  Unknown          True    
3      30.0                    Fixed         False    
4       1.0                   Intact          True  
```

#### Step 19

```
df_clean = df.dropna(axis = 1)
```

#### Step 20

```
# print cleaned data info  
print(df_clean.info())  
  
#save to file  
df_clean.to_csv('cleaned_animal_data.csv')
```

**Expected Output:**

```
<class 'pandas.core.frame.DataFrame'>  
Index: 137056 entries, 0 to 137099  
Data columns (total 11 columns):  
 #   Column                    Non-Null Count   Dtype           
---  ------                    --------------   -----           
 0   Animal ID                 137056 non-null  object          
 1   DateTime                  137056 non-null  datetime64[ns]  
 2   MonthYear                 137056 non-null  object          
 3   Date of Birth             137056 non-null  datetime64[ns]  
 4   Outcome Type              137056 non-null  object          
 5   Animal Type               137056 non-null  object          
 6   Age upon Outcome          137056 non-null  int64           
 7   Breed                     137056 non-null  object          
 8   Color                     137056 non-null  object          
 9   Grouped Sex upon Outcome  137056 non-null  object          
 10  Name Missing              137056 non-null  bool            
dtypes: bool(1), datetime64[ns](2), int64(1), object(7)  
memory usage: 11.6+ MB  
None
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243598

Scraped At: 2026-05-14T20:57:33.141425
