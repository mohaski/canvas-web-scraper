# Technical Lesson: Data Cleaning with Pandas

# Technical Lesson: Data Cleaning with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Data Cleaning with Pandas

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

![Jack and Rose in the water in the Titanic movie](https://moringa.instructure.com/courses/1406/files/624770/download)

*Photograph: 20th Century Fox/Paramount*

In this technical lesson, we will walk through how to systematically clean a dataset. We will use the canonical Titanic dataset.

Can data science tell us whether Jack will live or die? Maybe . . . but first we have to clean the data!

We will load in the dataset, inspect the dataset, summary statistics on various features, plot distributions and use what we've learned to guide the cleaning. This will include removing duplicate entries, dropping rows or whole columns as necessary and making calls on when and how to impute nulls with statistical measures. Finally, we’ll save the cleaned dataset to file. The dataset will be ready for further analysis.

### Instructions

Here is a video walkthrough of the technical lesson steps that follow.

[VIDEO LINK](https://player.vimeo.com/video/995574473?h=11e45ecdb1)

### [Step 1](#dpPanel0)

The first thing to do is to import necessary libraries. Let's import pandas, numpy, and matplotlib pyplot using correct aliases.

```
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
```

### [Step 2](#dpPanel1)

Loading in the titanic dataset to a Pandas DataFrame named titanic\_df:

```
titanic_df = pd.read_csv('titanic.csv')
```

### [Step 3](#dpPanel2)

We want to inspect the dataframe to see what column we have, data types for each feature, and nulls:

```
titanic_df.info()
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 895 entries, 0 to 894  
Data columns (total 12 columns):  
 #   Column       Non-Null Count  Dtype    
---  ------       --------------  -----    
 0   PassengerId  895 non-null    int64    
 1   Survived     895 non-null    int64    
 2   Pclass       895 non-null    int64    
 3   Name         895 non-null    object   
 4   Sex          895 non-null    object   
 5   Age          716 non-null    float64  
 6   SibSp        895 non-null    int64    
 7   Parch        895 non-null    int64    
 8   Ticket       895 non-null    object   
 9   Fare         895 non-null    float64  
 10  Cabin        205 non-null    object   
 11  Embarked     893 non-null    object   
dtypes: float64(2), int64(5), object(5)  
memory usage: 84.0+ KB
```

There are nulls in three columns:

* Age
* Cabin
* Embarked

We will have to deal with these.

### [Step 4](#dpPanel3)

A quick inspection of the column names reveal that we might want to rename these columns so that it is more explicit as to what they mean. Some column names to consider renaming are:

* Pclass to 'Passenger\_Class'
* SibSp to 'Sibling\_Spouse\_Count'
* Parch to 'Parents\_Children\_Count'

```
titanic_df.rename(columns={'Pclass': 'Passenger_Class', 'SibSp': 'Sibling_Spouse_Count', 'Parch': 'Parents_Children_Count'}, inplace=True)  
titanic_df.columns
```

**Output:**

```
Index(['PassengerId', 'Survived', 'Passenger_Class', 'Name', 'Sex', 'Age',  
       'Sibling_Spouse_Count', 'Parents_Children_Count', 'Ticket', 'Fare',  
       'Cabin', 'Embarked'],  
      dtype='object')
```

### [Step 5](#dpPanel4)

Inspect distribution in the Cabin column.

```
titanic_df['Cabin'].value_counts()
```

**Output:**

```
Cabin  
B96 B98        4  
G6             4  
C23 C25 C27    4  
E101           3  
F33            3  
              ..  
C32            1  
E34            1  
C7             1  
C54            1  
C148           1  
Name: count, Length: 147, dtype: int64
```

### [Step 6](#dpPanel5)

Get the number of nulls in the Cabin column:

```
titanic_df['Cabin'].isna().sum()
```

**Output:**

```
690
```

### [Step 7](#dpPanel6)

The .value\_counts() and the null counting tells us that:

1. The category is too granular and the mode is not sufficiently dominant to impute with.
2. The vast majority of the column are nulls.

This is a case where imputation would lead to severe data skewing. It is best just to drop this column. Let's do it:

```
titanic_df.drop(columns= ['Cabin'], inplace=True)  
titanic_df.columns
```

**Output:**

```
Index(['PassengerId', 'Survived', 'Passenger_Class', 'Name', 'Sex', 'Age',  
       'Sibling_Spouse_Count', 'Parents_Children_Count', 'Ticket', 'Fare',  
       'Embarked'],  
      dtype='object')
```

### [Step 8](#dpPanel7)

Before doing any kind of statistical imputation, it is good to check if you have any duplicates in your data. Significant duplicates can skew imputations based off calculated statistics, so let's take care of this first. Create a boolean mask and filter to return any duplicated rows as a DataFrame:

```
titanic_df[titanic_df.duplicated()]
```

**Output:**

```
     PassengerId  Survived  Passenger_Class                           Name  \  
54             7         0                1        McCarthy, Mr. Timothy J     
90            74         0                3    Chronopoulos, Mr. Apostolos     
146          141         0                3  Boulos, Mrs. Joseph (Sultana)     
625          141         0                3  Boulos, Mrs. Joseph (Sultana)     
  
        Sex   Age  Sibling_Spouse_Count  Parents_Children_Count Ticket  \  
54     male  54.0                     0                       0  17463     
90     male  26.0                     1                       0   2680     
146  female   NaN                     0                       2   2678     
625  female   NaN                     0                       2   2678     
  
        Fare Embarked    
54   51.8625        S    
90   14.4542        C    
146  15.2458        C    
625  15.2458        C  
```

### [Step 9](#dpPanel8)

There are some duplicates here. Let's use pandas magic and clean them. We can check if we have any duplicates afterwards:

```
titanic_df.drop_duplicates(inplace=True)  
  
# this sums over all instances of rows as to whether they are duplicates of another row or not.  
  
titanic_df.duplicated().sum() # gets number of duplicates left after drop duplicate operation
```

**Output:**

```
0
```

We have taken care of any duplicates in the dataframe. Now let's turn to statistical imputation tasks.

### [Step 10](#dpPanel9)

Let's take a look at the Age column. Compute the number of NaNs in Age.

```
titanic_df['Age'].isna().sum()
```

**Output:**

177

### [Step 11](#dpPanel10)

While the column has a significant number of nulls, there are enough non-null values that it might be worth trying to impute. First, compute the following summary statistics on Age:

* median
* mean
* standard deviation

```
print(titanic_df['Age'].median())  
print(titanic_df['Age'].mean())  
print(titanic_df['Age'].std(ddof=1))
```

**Output:**

```
28.0  
29.69911764705882  
14.526497332334044
```

### [Step 12](#dpPanel11)

The mean has been pulled a bit up from the median. Let's see why and then ascertain whether imputing with the mean or the median or possibly some other value might be the best strategy. To do this, we are going to use matplotlib to get a histogram of the Age. Let's also plot the median and mean as dashed vertical lines colored red and green.

```
fig, ax = plt.subplots()  
ax.hist(x = titanic_df['Age'], histtype='step', bins = 20)  
ax.set_xlabel('Age')  
ax.set_ylabel('Count')  
ax.set_title('Distribution of Ages')  
ax.axvline(titanic_df['Age'].median(), c = 'r', linestyle = '--', label = 'Median')  
ax.axvline(titanic_df['Age'].mean(), c = 'g', linestyle = '--', label = 'Mean')  
ax.legend()  
plt.show()
```

![Histogram of distribution of ages with the mean and median marked](https://moringa.instructure.com/courses/1406/files/624749/download)

### [Step 13](#dpPanel12)

The distribution clearly has a range of age values (~20-40) that dominate the distribution. It is a decent bet that if we impute with a good value of central tendency, our imputed value might not be too far off from the true, unknown value. The median looks like a better measure of central tendency than the mean. This is due to the skew at higher ages (> 40). Let's impute with the median:

```
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].median())
```

### [Step 14](#dpPanel13)

Calculate the new mean and standard deviation. Compare the old mean and standard deviation above with the new mean and standard deviation. What happened?

```
print(titanic_df['Age'].mean())  
print(titanic_df['Age'].std(ddof = 1))
```

**Output:**

```
29.36158249158249  
13.019696550973194
```

We imputed all 179 null values with the median. This had the effect of pulling the mean down and lowering the standard deviation*—*as the median is lower than the mean and the imputed nulls all have the same value. Be aware that simple imputation alters summary statistics.

### [Step 15](#dpPanel14)

Print the unique categories and value counts for Embarked:

```
print(titanic_df['Embarked'].unique())  
print(titanic_df['Embarked'].value_counts())
```

**Output:**

```
['S' 'C' 'Q' nan]  
Embarked  
S    644  
C    168  
Q     77  
Name: count, dtype: int64
```

This distribution is completely dominated by the category S*—*i.e., those who embarked from Southampton. There are only 2 nulls in this column. We could drop the corresponding rows and not lose too much data. But given the clear mode in Embarked it might be a good bet that these individuals came from Southampton. Imputation is nice because we retain all the data contained in the other columns. Let's code out both strategies.

### [Step 16](#dpPanel15)

Return a new dataframe with all rows with nulls in Embarked. Save it to the variable mod\_df. **Do not modify the original dataframe in-place.** Then inspect the new dataframe with the .info() method.

```
mod_df = titanic_df.dropna(subset=['Embarked'])  
mod_df.info()
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>  
Index: 889 entries, 0 to 894  
Data columns (total 11 columns):  
 #   Column                  Non-Null Count  Dtype    
---  ------                  --------------  -----    
 0   PassengerId             889 non-null    int64    
 1   Survived                889 non-null    int64    
 2   Passenger_Class         889 non-null    int64    
 3   Name                    889 non-null    object   
 4   Sex                     889 non-null    object   
 5   Age                     889 non-null    float64  
 6   Sibling_Spouse_Count    889 non-null    int64    
 7   Parents_Children_Count  889 non-null    int64    
 8   Ticket                  889 non-null    object   
 9   Fare                    889 non-null    float64  
 10  Embarked                889 non-null    object   
dtypes: float64(2), int64(5), object(4)  
memory usage: 83.3+ KB
```

There are no nulls left in the DataFrame.

### [Step 17](#dpPanel16)

Now let's try and impute the mode in the original dataframe. First use the mode function on the Embarked column in titanic\_df.

```
titanic_df['Embarked'].mode()
```

**Output:**

```
0    S  
Name: Embarked, dtype: object
```

### [Step 18](#dpPanel17)

Notice this is Series*—*there can be more than one mode. Let's extract the first value in this series and save it to a variable embarked\_mode.

```
embarked_mode = titanic_df['Embarked'].mode().iloc[0]  
embarked_mode
```

**Output:**

'S'

### [Step 19](#dpPanel18)

Now we impute with the embarked\_mode in the original dataframe titanic\_df and inspect the dataframe:

```
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(embarked_mode)  
titanic_df.info()
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>  
Index: 891 entries, 0 to 894  
Data columns (total 11 columns):  
 #   Column                  Non-Null Count  Dtype    
---  ------                  --------------  -----    
 0   PassengerId             891 non-null    int64    
 1   Survived                891 non-null    int64    
 2   Passenger_Class         891 non-null    int64    
 3   Name                    891 non-null    object   
 4   Sex                     891 non-null    object   
 5   Age                     891 non-null    float64  
 6   Sibling_Spouse_Count    891 non-null    int64    
 7   Parents_Children_Count  891 non-null    int64    
 8   Ticket                  891 non-null    object   
 9   Fare                    891 non-null    float64  
 10  Embarked                891 non-null    object   
dtypes: float64(2), int64(5), object(4)  
memory usage: 83.5+ KB
```

### [Step 20](#dpPanel19)

We now have no nulls and have retained the two rows with nulls in Embarked. Our data is now ready for further exploratory data analysis. Let's save the cleaned data to csv data and call the file cleaned\_titanic.csv

```
titanic_df.to_csv('clean_titanic.csv')
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243597

Scraped At: 2026-05-14T20:57:26.561256
