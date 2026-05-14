# Practice: Pandas Dataframes and Series

# Practice: Pandas Dataframes and Series

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Pandas Dataframes and Series

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

In this practice, we'll look at a dataset which contains information on World Cup matches. You will use the pandas commands we've covered to learn more about our data.

After completing this lab, you should be able to:

* Use pandas methods and attributes to access information about a dataset.
* Index pandas dataframes with .loc, .iloc, and column names.
* Use a boolean mask to index pandas series and dataframes.

### Resources

* [GitHub Repository (Practice 1)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m5)

### Instructions

Load the file 'WorldCupMatches.csv' as a DataFrame in pandas.

```
# Import pandas using the standard alias
```

```
# Load 'WorldCupMatches.csv' as a DataFrame
```

### Part 1: Common Methods and Attributes

1. Use the correct method to display the first 7 rows of the dataset.  

   ```
   # Display the first 7 rows of df
   ```
2. Display the last 3 rows of the dataset.  

   ```
   # Display the last 3 rows of df
   ```
3. Get a concise summary of the data using .info().  

   ```
   # Print a concise summary of df
   ```
4. Obtain a tuple representing the number of rows and number of columns.  

   ```
   # Display the number of rows and columns in df
   ```
5. Use the appropriate attribute to get the column names.  

   ```
   # Display the column names of df
   ```

### Part 2: Selecting Dataframe Information

When looking at the DataFrame's .head() and .tail(), you might have noticed that the games are structured chronologically in the DataFrame.

1. Use the right selection method to display all the information from the 3rd to the 5th game (i.e. select rows 3 through 5 inclusive).
2. Now, display the info from games labeled 5-9 in the index (inclusive), but only the "Home Team Name" and the "Away Team Name" columns.
3. Next, we'd like the information on all the games played in Group 3 for the 1950 World Cup.  
   Hint: You can combine conditions like this:  

   ```
   df[(condition1) | (condition2)] -> Returns rows where either condition is true
   ```

   ```
   df[(condition1) & (condition2)] -> Returns rows where both conditions are true
   ```

   ```
   # Display all info for games played in 1950 for Group 3
   ```
4. Let's repeat the command above, but this time display only the attendance column for the Group 3 games.
5. Throughout the entire history of the World Cup as recorded in this dataset, how many home games were played by the Netherlands? (Remember that you can use the len() built-in function to find the number of rows in a DataFrame.)
6. How many games were played by the Netherlands in total?
7. Next, let's try and figure out how many games the USA played in the 2014 World Cup.
8. The Match ID is a unique match identifier for international games: set this to the index and inspect the head to verify changes.
9. Select data from Home Team Name to Half-time Away Goals for Match ID 1085. Use slicing here.
10. Reset the index back to integer index and move the 'MatchID' back to a column in the DataFrame.

### Part 3: Changing Data and Data Types, Dropping and Creating New Columns

1. For your analysis, you realized that you don't need information on Referee Assistants and Win Conditions. Remove these columns and modify the original dataframe in-place. Print the column list to verify that these changes have taken place.
2. Check the data type of the DateTime column using the appropriate Series method.
3. The dtype 'O' is the object data type. Here it is indicating that we have a column of strings. Now, convert this column to a datetime data type and make sure the changes are administered to the original dataframe df:
   * Note: the string formatting for datetimes in this column are not all exactly the same (i.e. they are mixed)
   * Use the 'mixed' option for the format keyword argument in the pandas conversion function.
   * Note: This is covered in the [Supplementary Pandas Content](https://moringa.instructure.com/courses/1406/pages/supplementary-pandas-content "Supplementary Pandas Content") page.
4. In World Cup history, how many matches had 5 goals or more in total? First, create a new column "Total Goals".
5. Filter the dataset based on the "Total Goals" column and save it to a new dataframe high\_score\_df. Then get the number of matches satisfying the above condition.
6. In the dataframe df, create a new column "High\_Total\_Score" that has value 0 if the total number of goals in a match was less than 5 and 1 if the there were 5 or more goals scored in total.
7. Now create a new column "Half-time Goals" in df that includes both home and away values.
8. Select all records that contain matches where North-Korea (Korea DPR) and South-Korea (Korea Republic) were involved.

### Part 4: Calculating Statistics and Applying Functions

1. Calculate the average number of goals South Korea (Korea Republic) scored when it was the Home Team. Save this to a variable mean\_home\_SK.
2. Also, estimate the average spread on this by calculating the standard deviation. Save the standard deviation to a variable std\_home\_SK.
3. What is the maximum number of goals that North Korea has scored when it has been away?
4. Get the average attendance, home team goals, away team goals, and total goals scored over all home games for South Korea.
5. Short answer question: Does South Korea's scoring indicate that it benefits strongly from home advantage?
6. Get a list of the unique teams that South Korea has played when it has been on the road.
7. Create a Series with the teams that South Korea has played against and the number of matches against each team in the dataset*—*when South Korea has been away. Save this in a variable away\_match\_teamcount.

### Solution

### Select for Solution

Load the file 'WorldCupMatches.csv' as a DataFrame in pandas.

```
# Import pandas using the standard alias  
import pandas as pd
```

```
# Load 'WorldCupMatches.csv' as a DataFrame  
df = pd.read_csv('WorldCupMatches.csv')
```

#### Part 1: Common Methods and Attributes

```
# Display the first 7 rows of df  
df.head(7)
```

**Expected Output:**

```
   Year              Datetime    Stage         Stadium         City  \  
0  1930  13 Jul 1930 - 15:00   Group 1         Pocitos  Montevideo      
1  1930  13 Jul 1930 - 15:00   Group 4  Parque Central  Montevideo      
2  1930  14 Jul 1930 - 12:45   Group 2  Parque Central  Montevideo      
3  1930  14 Jul 1930 - 14:50   Group 3         Pocitos  Montevideo      
4  1930  15 Jul 1930 - 16:00   Group 1  Parque Central  Montevideo      
5  1930  16 Jul 1930 - 14:45   Group 1  Parque Central  Montevideo      
6  1930  17 Jul 1930 - 12:45   Group 2  Parque Central  Montevideo      
  
  Home Team Name  Home Team Goals  Away Team Goals Away Team Name  \  
0         France                4                1         Mexico     
1            USA                3                0        Belgium     
2     Yugoslavia                2                1         Brazil     
3        Romania                3                1           Peru     
4      Argentina                1                0         France     
5          Chile                3                0         Mexico     
6     Yugoslavia                4                0        Bolivia     
  
  Win conditions  Attendance  Half-time Home Goals  Half-time Away Goals  \  
0                     4444.0                     3                     0     
1                    18346.0                     2                     0     
2                    24059.0                     2                     0     
3                     2549.0                     1                     0     
4                    23409.0                     0                     0     
5                     9249.0                     1                     0     
6                    18306.0                     0                     0     
  
                    Referee               Assistant 1  \  
0    LOMBARDI Domingo (URU)     CRISTOPHE Henry (BEL)     
1         MACIAS Jose (ARG)  MATEUCCI Francisco (URU)     
2       TEJADA Anibal (URU)   VALLARINO Ricardo (URU)     
3     WARNKEN Alberto (CHI)       LANGENUS Jean (BEL)     
4       REGO Gilberto (BRA)      SAUCEDO Ulises (BOL)     
5     CRISTOPHE Henry (BEL)   APHESTEGUY Martin (URU)     
6  MATEUCCI Francisco (URU)    LOMBARDI Domingo (URU)     
  
                  Assistant 2  RoundID  MatchID Home Team Initials  \  
0         REGO Gilberto (BRA)      201     1096                FRA     
1       WARNKEN Alberto (CHI)      201     1090                USA     
2         BALWAY Thomas (FRA)      201     1093                YUG     
3    MATEUCCI Francisco (URU)      201     1098                ROU     
4  RADULESCU Constantin (ROU)      201     1085                ARG     
5         LANGENUS Jean (BEL)      201     1095                CHI     
6       WARNKEN Alberto (CHI)      201     1092                YUG     
  
  Away Team Initials    
0                MEX    
1                BEL    
2                BRA    
3                PER    
4                FRA    
5                MEX    
6                BOL  
```

```
# Display the last 3 rows of df  
df.tail(3)
```

**Expected Output:**

```
     Year              Datetime                     Stage  \  
849  2014  09 Jul 2014 - 17:00                Semi-finals     
850  2014  12 Jul 2014 - 17:00   Play-off for third place     
851  2014  13 Jul 2014 - 16:00                      Final     
  
                 Stadium             City Home Team Name  Home Team Goals  \  
849   Arena de Sao Paulo       Sao Paulo     Netherlands                0     
850     Estadio Nacional        Brasilia          Brazil                0     
851  Estadio do Maracana  Rio De Janeiro         Germany                1     
  
     Away Team Goals Away Team Name                       Win conditions  \  
849                0      Argentina  Argentina win on penalties (2 - 4)      
850                3    Netherlands                                          
851                0      Argentina        Germany win after extra time      
  
     Attendance  Half-time Home Goals  Half-time Away Goals  \  
849     63267.0                     0                     0     
850     68034.0                     0                     2     
851     74738.0                     0                     0     
  
                   Referee            Assistant 1              Assistant 2  \  
849     C�neyt �AKIR (TUR)   DURAN Bahattin (TUR)        ONGUN Tarik (TUR)     
850  HAIMOUDI Djamel (ALG)   ACHIK Redouane (MAR)  ETCHIALI Abdelhak (ALG)     
851   Nicola RIZZOLI (ITA)  Renato FAVERANI (ITA)     Andrea STEFANI (ITA)     
  
     RoundID    MatchID Home Team Initials Away Team Initials    
849   255955  300186490                NED                ARG    
850   255957  300186502                BRA                NED    
851   255959  300186501                GER                ARG  
```

```
# Print a concise summary of df  
df.info()
```

```
Expected Output:  
  
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 852 entries, 0 to 851  
Data columns (total 20 columns):  
 #   Column                Non-Null Count  Dtype    
---  ------                --------------  -----    
 0   Year                  852 non-null    int64    
 1   Datetime              852 non-null    object   
 2   Stage                 852 non-null    object   
 3   Stadium               852 non-null    object   
 4   City                  852 non-null    object   
 5   Home Team Name        852 non-null    object   
 6   Home Team Goals       852 non-null    int64    
 7   Away Team Goals       852 non-null    int64    
 8   Away Team Name        852 non-null    object   
 9   Win conditions        852 non-null    object   
 10  Attendance            850 non-null    float64  
 11  Half-time Home Goals  852 non-null    int64    
 12  Half-time Away Goals  852 non-null    int64    
 13  Referee               852 non-null    object   
 14  Assistant 1           852 non-null    object   
 15  Assistant 2           852 non-null    object   
 16  RoundID               852 non-null    int64    
 17  MatchID               852 non-null    int64    
 18  Home Team Initials    852 non-null    object   
 19  Away Team Initials    852 non-null    object   
dtypes: float64(1), int64(7), object(12)  
memory usage: 133.3+ KB
```

```
# Display the number of rows and columns in df  
df.shape
```

**Expected Output:**

```
(852, 20)
```

```
# Display the column names of df  
df.columns
```

**Expected Output:**

```
Index(['Year', 'Datetime', 'Stage', 'Stadium', 'City', 'Home Team Name',  
       'Home Team Goals', 'Away Team Goals', 'Away Team Name',  
       'Win conditions', 'Attendance', 'Half-time Home Goals',  
       'Half-time Away Goals', 'Referee', 'Assistant 1', 'Assistant 2',  
       'RoundID', 'MatchID', 'Home Team Initials', 'Away Team Initials'],  
      dtype='object')
```

#### Part 2: Selecting DataFrame Information

```
# Display rows 3 through 5  
# .iloc interval is "half open", does not include 6 in the output  
df.iloc[3:6]
```

**Expected Output:**

```
   Year              Datetime    Stage         Stadium         City  \  
3  1930  14 Jul 1930 - 14:50   Group 3         Pocitos  Montevideo      
4  1930  15 Jul 1930 - 16:00   Group 1  Parque Central  Montevideo      
5  1930  16 Jul 1930 - 14:45   Group 1  Parque Central  Montevideo      
  
  Home Team Name  Home Team Goals  Away Team Goals Away Team Name  \  
3        Romania                3                1           Peru     
4      Argentina                1                0         France     
5          Chile                3                0         Mexico     
  
  Win conditions  Attendance  Half-time Home Goals  Half-time Away Goals  \  
3                     2549.0                     1                     0     
4                    23409.0                     0                     0     
5                     9249.0                     1                     0     
  
                 Referee              Assistant 1                 Assistant 2  \  
3  WARNKEN Alberto (CHI)      LANGENUS Jean (BEL)    MATEUCCI Francisco (URU)     
4    REGO Gilberto (BRA)     SAUCEDO Ulises (BOL)  RADULESCU Constantin (ROU)     
5  CRISTOPHE Henry (BEL)  APHESTEGUY Martin (URU)         LANGENUS Jean (BEL)     
  
   RoundID  MatchID Home Team Initials Away Team Initials    
3      201     1098                ROU                PER    
4      201     1085                ARG                FRA    
5      201     1095                CHI                MEX  
```

```
# Display rows 5 through 9 and columns 'Home Team Name' and 'Away Team Name'  
# .loc interval is not "half open", it includes the endpoint  
df.loc[5:9, ['Home Team Name', 'Away Team Name']]
```

**Expected Output:**

```
  Home Team Name Away Team Name  
5          Chile         Mexico  
6     Yugoslavia        Bolivia  
7            USA       Paraguay  
8        Uruguay           Peru  
9          Chile         France
```

```
# Display all info for games played in 1950 for Group 3  
# This time we don't need .loc because we are applying a  
# boolean mask and our indexing uses rows only (all  
# columns are selected)  
  
df[(df["Year"] == 1950) & (df["Stage"] == "Group 3")]
```

**Expected Output:**

```
    Year              Datetime    Stage           Stadium        City  \  
56  1950  25 Jun 1950 - 15:00   Group 3          Pacaembu  Sao Paulo      
61  1950  29 Jun 1950 - 15:30   Group 3  Durival de Brito   Curitiba      
65  1950  02 Jul 1950 - 15:00   Group 3          Pacaembu  Sao Paulo      
  
   Home Team Name  Home Team Goals  Away Team Goals Away Team Name  \  
56         Sweden                3                2          Italy     
61         Sweden                2                2       Paraguay     
65          Italy                2                0       Paraguay     
  
   Win conditions  Attendance  Half-time Home Goals  Half-time Away Goals  \  
56                    36502.0                     2                     1     
61                     7903.0                     2                     1     
65                    25811.0                     1                     0     
  
                  Referee             Assistant 1                Assistant 2  \  
56        LUTZ Jean (SUI)     BERANEK Alois (AUT)        TEJADA Carlos (MEX)     
61  MITCHELL Robert (SCO)       LEMESIC Leo (YUG)     GARCIA Prudencio (USA)     
65     ELLIS Arthur (ENG)  GARCIA Prudencio (USA)  DE LA SALLE Charles (FRA)     
  
    RoundID  MatchID Home Team Initials Away Team Initials    
56      208     1219                SWE                ITA    
61      208     1228                SWE                PAR    
65      208     1218                ITA                PAR  
```

```
# Print the 'Attendance' column for games played in 1950  
# for Group 3  
# This time we want to use df.loc instead of just  
# df[boolean mask] in order to select certain rows AND  
# certain columns  
df.loc[(df['Year'] == 1950) & (df['Stage'] == 'Group 3'), 'Attendance']
```

**Expected Output:**

```
56    36502.0  
61     7903.0  
65    25811.0  
Name: Attendance, dtype: float64
```

```
# Number of home games played by the Netherlands  
# Here we are just using df[boolean mask] again  
neth_home = len(df[df['Home Team Name'] == ('Netherlands')])  
neth_home
```

**Expected Output:**

```
32
```

```
# Number of games played by the Netherlands in total  
# Conveniently we already saved neth_home as a variable  
# so we just need to find the number of times they were  
# the away team and sum them  
len(df[df['Away Team Name']==('Netherlands')]) + neth_home
```

**Expected Output:**

```
54
```

```
# Number of games the USA played in the 2014 world cup  
  
# Mask will return True or False for each row of df  
usa_2014_mask = (  
    # USA is home team OR away team  
    (  
        (df['Home Team Name'] == 'USA') |  
        (df['Away Team Name'] == 'USA')  
    ) &  
    # AND year is 2014  
    (df['Year'] == 2014)  
)  
  
# Filter df using mask and find its length  
len(df[usa_2014_mask])
```

**Expected Output:**

```
5
```

```
df.set_index('MatchID', inplace = True)  
df.head()
```

Output table is too wide for Canvas, so we've [provided it as an Excel file](https://moringa.instructure.com/courses/1406/files/624744?wrap=1 "DS-C0M5-Pandas-Dataframes-and-Series-Practice-Matchid-Output.xlsx")[Download provided it as an Excel file](https://moringa.instructure.com/courses/1406/files/624744/download?download_frd=1).

```
df.loc[1085, 'Home Team Name': 'Half-time Away Goals']
```

**Expected Output:**

```
Home Team Name          Argentina  
Home Team Goals                 1  
Away Team Goals                 0  
Away Team Name             France  
Attendance                23409.0  
Half-time Home Goals            0  
Half-time Away Goals            0  
Name: 1085, dtype: object
```

```
df.reset_index(inplace = True)
```

---

#### Part 3: Changing Data and Data Types, Dropping and Creating New Columns

```
df.drop(columns = ['Assistant 1', 'Assistant 2', 'Win conditions'], inplace=True)  
print(df.columns)
```

**Expected Output:**

```
Index(['Year', 'Datetime', 'Stage', 'Stadium', 'City', 'Home Team Name',  
       'Home Team Goals', 'Away Team Goals', 'Away Team Name', 'Attendance',  
       'Half-time Home Goals', 'Half-time Away Goals', 'Referee', 'RoundID',  
       'MatchID', 'Home Team Initials', 'Away Team Initials'],  
      dtype='object')
```

```
df['Datetime'].dtype
```

**Expected Output:**

```
dtype('O')
```

```
df['Datetime'] = pd.to_datetime(df['Datetime'], format= 'mixed')  
df['Datetime'].head()
```

**Expected Output:**

```
0   1930-07-13 15:00:00  
1   1930-07-13 15:00:00  
2   1930-07-14 12:45:00  
3   1930-07-14 14:50:00  
4   1930-07-15 16:00:00  
Name: Datetime, dtype: datetime64[ns]
```

```
# Number of matches that had more than 5 goals in total  
  
# New column created by summing the other two  
# We don't need a loop because pandas will automatically create  
# one and "broadcast" each value from the columns being summed  
  
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
```

```
high_score_df = df[df['Total Goals']>=5]  
len(high_score_df)
```

**Expected Output:**

```
147
```

```
df['High_Total_Score'] = (df['Total Goals'] >= 5).astype('int')  
  
print(df['High_Total_Score'].head())
```

**Expected Output:**

```
0    1  
1    0  
2    0  
3    0  
4    0  
Name: High_Total_Score, dtype: int32
```

```
# Create a new column 'Half-time Goals' in df  
df['Half-time Goals'] = df['Half-time Home Goals'] + df['Half-time Away Goals']  
df.columns
```

**Expected Output:**

```
Index(['Year', 'Datetime', 'Stage', 'Stadium', 'City', 'Home Team Name',  
       'Home Team Goals', 'Away Team Goals', 'Away Team Name', 'Attendance',  
       'Half-time Home Goals', 'Half-time Away Goals', 'Referee', 'RoundID',  
       'MatchID', 'Home Team Initials', 'Away Team Initials', 'Total Goals',  
       'High_Total_Score', 'Half-time Goals'],  
      dtype='object')
```

```
# just printing head here  
df.loc[df['Home Team Name'].str.contains('Korea') | df['Away Team Name'].str.contains('Korea')].head()
```

**Expected Output:**

```
     Year            Datetime    Stage        Stadium            City  \  
80   1954 1954-06-17 18:00:00  Group 2       Hardturm         Zurich      
88   1954 1954-06-20 17:00:00  Group 2     Charmilles         Geneva      
171  1966 1966-07-12 19:30:00  Group 4  Ayresome Park  Middlesbrough      
179  1966 1966-07-15 19:30:00  Group 4  Ayresome Park  Middlesbrough      
187  1966 1966-07-19 19:30:00  Group 4  Ayresome Park  Middlesbrough      
  
    Home Team Name  Home Team Goals  Away Team Goals  Away Team Name  \  
80         Hungary                9                0  Korea Republic     
88          Turkey                7                0  Korea Republic     
171   Soviet Union                3                0       Korea DPR     
179      Korea DPR                1                1           Chile     
187      Korea DPR                1                0           Italy     
  
     Attendance  Half-time Home Goals  Half-time Away Goals  \  
80      13000.0                     4                     0     
88       4000.0                     4                     0     
171     23006.0                     2                     0     
179     13792.0                     0                     1     
187     17829.0                     1                     0     
  
                      Referee  RoundID  MatchID Home Team Initials  \  
80     VINCENTI Raymond (FRA)      211     1294                HUN     
88       MARINO Esteban (URU)      211     1304                TUR     
171    GARDEAZABAL Juan (ESP)      238     1710                URS     
179  KANDIL Aly Hussein (EGY)      238     1609                PRK     
187     SCHWINTE Pierre (FRA)      238     1679                PRK     
  
    Away Team Initials  Total Goals  High_Total_Score  Half-time Goals    
80                 KOR            9                 1                4    
88                 KOR            7                 1                4    
171                PRK            3                 0                2    
179                CHI            2                 0                1    
187                ITA            1                 0                1 
```

---

#### Part 4: Calculating Statistics and Applying Functions

```
mean_home_SK = df.loc[df['Home Team Name'] == 'Korea Republic',  'Home Team Goals'].mean()  
mean_home_SK
```

**Expected Output:**

```
1.2857142857142858
```

```
std_home_SK = df.loc[df['Home Team Name'] == 'Korea Republic',  'Home Team Goals'].std(ddof=1)  
std_home_SK
```

**Expected Output:**

```
0.8254203058555569
```

```
max_away_NK = df.loc[df['Away Team Name'] == 'Korea DPR',  'Away Team Goals'].max()  
max_away_NK
```

**Expected Output:**

```
3
```

```
df.loc[df['Home Team Name'] == 'Korea Republic',  ['Attendance', 'Home Team Goals', 'Away Team Goals', 'Total Goals']].mean()
```

```
Expected Output:  
  
Attendance         43969.714286  
Home Team Goals        1.285714  
Away Team Goals        1.571429  
Total Goals            2.857143  
dtype: float64
```

Based on Home Team Goals vs. Away Team Goals, there doesn’t seem to be a home advantage for South Korea.

```
df.loc[df['Away Team Name'] == 'Korea Republic',  'Home Team Name'].unique()
```

**Expected Output:**

```
array(['Hungary', 'Turkey', 'Argentina', 'Belgium', 'Spain', 'Germany',  
       'Netherlands', 'Portugal', 'France', 'Switzerland', 'Nigeria',  
       'Uruguay', 'Russia'], dtype=object)
```

```
away_match_teamcount = df.loc[df['Away Team Name'] == 'Korea Republic',  'Home Team Name'].value_counts()  
away_match_teamcount
```

**Expected Output:**

```
Home Team Name  
Argentina      2  
Belgium        2  
Spain          2  
Germany        2  
Hungary        1  
Turkey         1  
Netherlands    1  
Portugal       1  
France         1  
Switzerland    1  
Nigeria        1  
Uruguay        1  
Russia         1  
Name: count, dtype: int64
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243588

Scraped At: 2026-05-14T20:56:39.504578
