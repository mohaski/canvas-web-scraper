# Lab: Prepare Data for Analyzing the Relationship Between Population and World Cup Performance

## ![](https://moringa.instructure.com/courses/1406/files/625182/preview) Lab: Prepare Data for Analyzing the Relationship Between Population and World Cup Performance

![World Cup trophy and soccer ball on a field](https://moringa.instructure.com/courses/1406/files/625274/download)
You are an analyst for GolStats Soccer Technologies, a soccer (football) analytics agency. They are interested in an analysis of various recent FIFA world cups -- specifically looking at the performance of a country in World cups in relation to their population. You have been tasked with looking specifically at the sample of World Cup games in 2018 and seeing whether this has any relationship with the corresponding 2018 populations of the participating nations.

Your goal will be to create a data structure containing the requisite information for your analysis. Specifically, you'll build a dictionary where each key is the name of a country, and each value is a nested dictionary containing information about the number of 2018 World Cup wins and the country's population in 2018.  
The final result will look something like this:

```
{  
  'Argentina': { 'wins': 1, 'population': 44494502 },  
  ...  
  'Uruguay':   { 'wins': 4, 'population': 3449299  }  
}
```

You will be using what you have learned about Python data types, data cleaning tasks, and CSV/JSON file formats to bear on this endeavor. You will be following a similar process to what you have been doing in the practice labs:

* Read serialized JSON and CSV data from files into Python objects
* Extract information from nested data structures
* Clean data (filtering, normalizing locations, converting types)
* Combine data from multiple sources into a single data structure

The data sources for this analysis will be pulled from two separate files.

* **world\_cup\_2018.json**
  + **Source:** This dataset comes from football.db, a "free and open public domain football database & schema for use in any (programming) language"
  + **Contents:** Data about all games in the 2018 World Cup, including date, location (city and stadium), teams, goals scored (and by whom), and tournament group
  + **Format:** Nested JSON data (dictionary containing a list of rounds, each of which contains a list of matches, each of which contains information about the teams involved and the points scored)
* **country\_populations.csv**
  + **Source:** This dataset comes from a curated collection by DataHub.io, originally sourced from the World Bank
  + **Contents:** Data about populations by country for all available years from 1960 to 2018
  + **Format:** CSV data, where each row contains a country name, a year, and a population

### Tools and Resources

* [GitHub repository


  Links to an external site.](https://github.com/learn-co-curriculum/DS_Course0_Week1_Module2_DataTypes)
* Jupyter Notebook
* CodeGrade (for assignment submission)

### Instructions

We have imported the json and csv modules, which will be used for reading from world\_cup\_2018.json and country\_populations.csv, respectively.

```
# Run this cell without changes  
  
import json  
import csv
```

* [Step 1](#dpPanel0Content)
* [Step 2](#dpPanel1Content)
* [Step 3](#dpPanel2Content)
* [Step 4](#dpPanel3Content)
* [Step 5](#dpPanel4Content)
* [Step 6](#dpPanel5Content)
* [Step 7](#dpPanel6Content)
* [Step 8](#dpPanel7Content)
* [Step 9](#dpPanel8Content)
* [Step 10](#dpPanel9Content)
* [Step 11](#dpPanel10Content)

### Step 1

Using context managers, appropriate modules, load the data in the json to a data structure world\_cup\_data and the data in the csv to population\_data.

population\_data should be structured as a list of dicts.

```
# Replace None with appropriate code  
  
with open("data/world_cup_2018.json", encoding='utf8') as world_cup_file:  
    world_cup_data = None  
  
with open("data/country_populations.csv") as population_file:  
    # make sure this is converted to a list  
    population_data = None
```

Make sure the assert passes, ensuring that world\_cup\_data has the correct type.

```
# Run this cell without changes  
  
# Check that the overall data structure is a dictionary  
assert type(world_cup_data) == dict  
  
# Check that the dictionary has 2 keys, 'name' and 'rounds'  
assert list(world_cup_data.keys()) == ['name', 'rounds']
```

Make sure the asserts pass, ensuring that population\_data has the correct type.

```
# Run this cell without changes  
  
# Check that the overall data structure is a list  
assert type(population_data) == list  
  
# Check that the 0th element is a dictionary  
# (csv.DictReader interface differs slightly by Python version;  
# element should be of type Dict)  
assert type(population_data[0]) == dict
```

### Step 2

Exploring the structure of the World Cup Data JSON: Get the highest level keys:

```
# Replace your code with None  
highest_lvl_keys = world_cup_data.keys()  
print(highest_lvl_keys)
```

The data contained in the two keys are:

```
# Run this cell without changes  
print(world_cup_data['name'])  
print(world_cup_data['round'][0])
```

Organization of the world cup data, if you have done everything correctly, should be:

* world\_cup\_data is a dictionary with two keys, 'name' and 'rounds'.
* The 'name' key contains the name of the dataset.
* The 'round' key contains all match info organized by match day.

### Step 3

Extracting Matches: Go one level deeper and extract all of the matches in the tournament. Put these, regardless of the round, into a list called matches  
***Hint:*** This is a good use case for using the .extend list method rather than .append.

```
# Replace None with appropriate code  
matches = []  
  
# "round" is a built-in function in Python so we use "round_" instead  
for round_ in rounds:  
    # Extract the list of matches for this round  
    round_matches = None  
    # Add them to the overall list of matches  
    None  
      
matches[0]
```

Make sure the asserts pass before moving on to the next step.

```
# Run this cell without changes  
  
# There should be 64 matches. If the length is 20, that means  
# you have a list of lists instead of a list of dictionaries  
assert len(matches) == 64  
  
# Each match in the list should be a dictionary  
assert type(matches[0]) == dict
```

### Step 4

Each match has a team1 and a team2 -- each with an associated name. Loop through all the matches and create a Python set() containing the names of all unique teams playing in the World Cup. This set should be named team\_set. This set will be used to create an alphabetically ordered list teams.

```
# Replace None with appropriate code  
teams_set = set()  
  
for match in matches:  
    # Add team1 name value to teams_set  
    None  
    # Add team2 name value to teams_set  
    None  
  
# convert set to list and sort alphabetically.  
teams = sorted(list(teams_set))
```

Make sure the asserts pass before moving on to the next step.

```
# Run this cell without changes  
  
# teams should be a list, not a set  
assert type(teams) == list  
  
# 32 teams competed in the 2018 World Cup  
assert len(teams) == 32  
  
# Each element of teams should be a string  
# (the name), not a dictionary  
assert type(teams[0]) == str
```

We now have unique identifiers (names) for each of our countries. These will be the keys in our dictionary that we want to create. The values will be the 2018 World Cup performance to the 2018 population data.

### Step 5

Start by initializing a dictionary called combined\_data containing:

* keys being the strings from teams
* values each being a dictionary containing the key 'wins' with the associated value 0.

Initially combined\_data will look something like this:

```
{  
  'Argentina': { 'wins': 0 },  
  ...  
  'Uruguay':   { 'wins': 0 }  
}
```

```
# Replace None with appropriate code  
  
# Create the variable combined_data as described above  
combined_data = None
```

Check that the asserts pass.

```
# Run this cell without changes  
  
# combined_data should be a dictionary  
assert type(combined_data) == dict  
  
# the keys should be strings  
assert type(list(combined_data.keys())[0]) == str  
  
# the values should be dictionaries  
assert combined_data["Japan"] == {"wins": 0}
```

### Step 6

Write a function find\_winner that return the name of the winner (i.e. the country name) for a given match. If the values are the same, there is no winner, so return None.

***Hint:*** An example of a match entry is below. The key score1 corresponds to team1 and key score2 corresponds to team2. Comparison operators and conditional statements will be your friend:

```
{  
  'num': 1,  
  'date': '2018-06-14',  
  'time': '18:00',  
  'team1': { 'name': 'Russia',       'code': 'RUS' },  
  'team2': { 'name': 'Saudi Arabia', 'code': 'KSA' },  
  'score1': 5,  
  'score2': 0,  
  'score1i': 2,  
  'score2i': 0,  
  'goals1': [  
    { 'name': 'Gazinsky',  'minute': 12, 'score1': 1, 'score2': 0 },  
    { 'name': 'Cheryshev', 'minute': 43, 'score1': 2, 'score2': 0 },  
    { 'name': 'Dzyuba',    'minute': 71, 'score1': 3, 'score2': 0 },  
    { 'name': 'Cheryshev', 'minute': 90, 'offset': 1, 'score1': 4, 'score2': 0 },  
    { 'name': 'Golovin',   'minute': 90, 'offset': 4, 'score1': 5, 'score2': 0 }  
  ],  
  'goals2': [],  
  'group': 'Group A',  
  'stadium': { 'key': 'luzhniki', 'name': 'Luzhniki Stadium' },  
  'city': 'Moscow',  
  'timezone': 'UTC+3'  
}
```

```
# Replace None with appropriate code  
  
def find_winner(match):  
    """  
    Given a dictionary containing information about a match,  
    return the name of the winner (or None in the case of a tie)  
    """  
    None  
# Run this cell without changes  
assert find_winner(matches[0]) == "Russia"  
assert find_winner(matches[1]) == "Uruguay"  
assert find_winner(matches[2]) == None
```

### Step 7

Now that we have this helper function, loop over every match in matches, find the winner, and add 1 to the associated count of wins in combined\_data. If the winner is None, skip adding it to the dictionary.

```
# Replace None with appropriate code  
  
for match in matches:  
    # Get the name of the winner  
    winner = None  
    # Only proceed to the next step if there was  
    # a winner  
    if winner:  
        # Add 1 to the associated count of wins  
        None  
          
# Visually inspect the output to ensure the wins are  
# different for different countries  
combined_data
```

Next, you will need to add the 2018 population for each country to the existing data structure so that it also connects each country name to its 2018 population.

And the goal is for it to look something like this:

```
{  
  'Argentina': { 'wins': 1, 'population': 44494502 },  
  ...  
  'Uruguay':   { 'wins': 4, 'population': 3449299  }  
}
```

### Step 8

The required data is contained within the population data CSV. The data contains country population data for many years. Filter the population data to include only the relevant records where the country name is one of the countries in the teams list, and the year is "2018".

```
# Replace None with appropriate code  
  
population_data_filtered = []  
  
for record in population_data:  
    # Add record to population_data_filtered if relevant  
    None  
      
len(population_data_filtered) # 27
```

### Step 9

There are only 27 countries in this filtered set as opposed to the 32 teams that played in the World Cup. Running the two cells below reveals the issue:

```
# Run this cell without changes  
population_record_samples[2]
```

And compare that with the value for Iran in teams:

```
# Run this cell without changes  
teams[13]
```

There is a string normalization issue. One dataset refers to this country as 'Iran, Islamic Rep.', while the other refers to it as 'Iran'. This is a common issue faced with categorical data in real datasets. We will give you the function that makes the appropriate substitutions.

```
# Run this cell without changes  
def normalize_location(country_name):  
    """  
    Given a country name, return the name that the  
    country uses when playing in the FIFA World Cup  
    """  
    name_sub_dict = {  
        "Russian Federation": "Russia",  
        "Egypt, Arab Rep.": "Egypt",  
        "Iran, Islamic Rep.": "Iran",  
        "Korea, Rep.": "South Korea",  
        "United Kingdom": "England"  
    }  
    # The .get method returns the corresponding value from  
    # the dict if present, otherwise returns country_name  
    return name_sub_dict.get(country_name, country_name)  
  
# Example where normalized location is different  
print(normalize_location("Russian Federation"))  
# Example where normalized location is the same  
print(normalize_location("Argentina"))
```

Your task is to re-create population\_data\_filtered with country names normalized appropriately.

```
# Replace None with appropriate code  
  
population_data_filtered = []  
  
for record in population_data:  
    # Get normalized country name  
    None  
    # Add record to population_data_filtered if relevant  
    if None:  
        # Replace the country name in the record  
        None  
        # Append to list  
        None  
          
len(population_data_filtered) # 32
```

If you did this correctly, the number of records in population\_data\_filtered should match the number in teams.

### Step 10

Go through the population\_data\_filtered and convert the population data to the correct data type:

```
# Replace None with appropriate code  
for record in population_data_filtered:  
    # Convert the population value from str to int  
    None  
      
# Look at the last record to make sure the population  
# value is an int  
population_data_filtered[-1]
```

Check that it worked with the assert statement below:

```
# Run this cell without changes  
assert type(population_data_filtered[-1]["Value"]) == int
```

### Step 11

Add the population data to combined\_data. Recall that the data structure currently looks like this:

```
# Run this cell without changes  
combined_data
```

The goal is for it to be structured like this:

```
{  
  'Argentina': { 'wins': 1, 'population': 44494502 },  
  ...  
  'Uruguay':   { 'wins': 4, 'population': 3449299  }  
}
```

In the cell below, loop over population\_data\_filtered and add information about population to each country in combined\_data:

```
# Replace None with appropriate code  
for record in population_data_filtered:  
    # Extract the country name from the record  
    country = None  
    # Extract the population value from the record  
    population = None  
    # Add this information to combined_data  
    None  
      
# Look combined_data  
combined_data
```

Check that the types are correct with these assert statements:

```
# Run this cell without changes  
assert type(combined_data["Uruguay"]) == dict  
assert type(combined_data["Uruguay"]["population"]) == int
```

Congratulations! That was a long lab, pulling together a lot of material. You read data into Python, extracted the relevant information, cleaned the data, and combined the data into a new format to be used in analysis. While we will continue to introduce new tools and techniques, these essential steps will be present for the rest of your data science projects from here on out!

### Submission and Grading Criteria

1. Review the rubric below as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade using your Jupyter notebook upload. Remember to make sure you have your final version of your notebook before submitting your assignment.
3. When you are ready to submit, launch CodeGrade.
   * Click on + Create Submission. Upload your Jupyter notebook file for this lab.
   * For additional information on submitting assignments in CodeGrade: [Getting Started in CanvasLinks to an external site.


     Links to an external site.](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas)
   * You can review your submission in CodeGrade and see your score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243524

Scraped At: 2026-05-14T20:49:30.416200
