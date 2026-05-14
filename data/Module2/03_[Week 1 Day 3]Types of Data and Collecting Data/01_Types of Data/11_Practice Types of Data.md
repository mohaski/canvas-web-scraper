# Practice: Types of Data

# Practice: Types of Data

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Types of Data

Icon Progress Bar (browser only)

5 min read

You are given a record of dogs that have visited a small vet clinic in the past few hours. The clinic is currently very busy. There is a new virus that turns some dogs (who are usually by default all good boys and girls) into bad doggies. Also a very nasty doggy flu has been going around at the same time.

* Given the situation, data entry has been rushed and there are some inconsistencies that need to be addressed and type conversion you will need to do to get the data into your organization's standard.
* Your direct manager (who is not a data person) is European and wants the dog length to be converted to metric because he thinks that the inch is a preposterous unit of measurement.
* The head veterinarian wants a flagging system for dogs that come in running a fever.

You, the only data analyst at this small clinic, have been assigned these tasks. Exercise your knowledge of string cleaning, mathematical operations on numeric quantities, and booleans in order to complete the work.

### Resources

* [GitHub Repository  (Practice 1 file)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m2)

### Instructions

Fork and clone the linked repository ( https://github.com/learn-co-curriculum/dsc-course0-m3-topic1-practicelab ) on your local system. Start the analysis in the provided Jupyter notebook (index.ipynb). The tabular veterinary clinic data has been provided in a list of lists for you and appears as follows:

```
dog_data = [['Name', 'Breed', 'Good Doggy?', 'Length [in]', 'Weight Range', 'Body Temp [F]'],  
    ["Buddy", "Golden Retriever", "Good", 24, 'Overweight', 101.5],  
    ["Cooper", "Doberman Pinscher", "Bad", 28, 'Normal',  105.2],  
    ["Max", "GERMAN Shepherd", "Good", 26, 'Normal', 100.2],  
    ["Bella", "Chow Chow", "Bad", 20, 'Normal', 100.5],  
    ["Lucy", " Yorkshire Terrier", "Good", 9, 'Normal', 102.0],  
    ["Charlie", "Beagle", "Good", 13, 'Overweight', 100.4],  
    ["Daisy", "Akita", "Bad", 24, 'Normal',99.8],  
    ["Bailey", "JACK russell terrier", "Bad", 10, 'Underweight', 101.2],  
    ["Lola", "Rottweiler   ", "Good", 27, 'Normal', 102.5],  
    ["Sadie", "Siberian_Husky", "Bad", 23, 'Normal', 99.5],  
    ["Penny", "STANDARD Poodle", "Good", 18, 'Underweight', 100.7],  
    ["Bruno", "Bulldog", "Bad", 14, 'Normal', 104.1],  
    ["Rosie", "Beagle", "Good", 13, 'Normal', 100.6],  
    ["Duke", "    DOBERMAN PINSCHER", "Good", 28,  'Normal',100.1],  
    ["Luna", "Shiba Inu", "Good", 17, 'Obese',  100.3],  
    ["Scout", "Golden_Retriever", "Good", 22, 'Normal', 103.5],  
    ["Rex", "Rottweiler", "Bad", 23, 'Normal', 100.2],  
]
```

In order to conform to your organization’s standards: you will be cleaning and standardizing any strings with errors and styling inconsistencies, converting any ordinal categoricals to integer representations, and making sure that any binary variables are represented as Booleans. You will get to execute the following steps in your notebook writing the relevant code directly below the requested task:

### Step 1

Write a clean\_string function that takes in a string and removes leading/trailing spaces, replaces underscores with spaces, and capitalizes the first letter of each word. Use this function to replace the values in the 'Breed' column with the new cleaned values.

### Step 2

Transform lengths from inches to centimeters.

### Step 3

Convert Good/Bad doggy column to boolean.

### Step 4

Convert the ‘Weight’ column to an integer representation.

### Step 5

Create a new column called Has\_Fever. The value should yield False if a dog has normal body temperature and True if a dog is running a fever. A dog should be flagged as having a fever if their body temperature is above 102 F.

### Step 6

Run cell to display all changes you have made.

### Resources

* [GitHub Repository


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-course0-m3-topic1-practicelab)

### Tools

* Working locally with Jupyter notebook and GitHub

### Solution

### Select for Solution

1. Write a clean\_string function that takes in a string and removes leading/trailing spaces, replaces underscores with spaces, and capitalizes the first letter of each word. Use this function to replace the values in the 'Breed' column with the new cleaned values.

```
# Function to clean strings (remove whitespace, replace '_' with spaces, capitalize words)  
# uses method chaining  
def clean_string(text):  
  return text.strip().replace("_", " ").title()  
  
  
for row in dog_data[1::]:  
    row[1] = clean_string(row[1])
```

1. Transform lengths from inches to centimeters.

```
for row in dog_data[1::]:  
    row[1] = row[3] * 2.54 # conversion from in to cm.  
  
  
dog_data[0][3] = 'Length [cm]'
```

1. Convert Good/Bad doggy column to boolean.

```
 for i, row in enumerate(dog_data):  
    if i > 0:  
        row[2] = (row[2] == 'Good')
```

1. Convert the ‘Weight’ column to an integer representation.

```
# the weight column is clearly an ordinal categorical  
# we create a dictionary and then map it to integers accordingly  
  
  
value_mapper = {'Underweight': 0, 'Normal': 1, 'Overweight': 2, 'Obese': 3}  
  
  
for i, row in enumerate(dog_data):  
    if i > 0:  
        row[4] = value_mapper[row[4]] # get the integer value corresponding to the ordinal categorical and reassign entry
```

1. Create a new column called Has\_Fever. The value should yield 0 if a dog has normal body temperature and 1 if a dog is running a fever. A dog should be flagged as having a fever if their body temperature is above 102 F.

```
for i, row in enumerate(dog_data):  
    if i == 0:  
       row.append('Has_Fever')  
    else:  
       # check condition on body temp  
       row.append(row[-1] > 102) # get Boolean then append to row
```

1. Run cell to display all changes you have made.

```
dog_data 
```

```
[['Name',  
  'Breed',  
  'Good Doggy?',  
  'Length [cm]',  
  'Weight Range',  
  'Body Temp [F]',  
  'Has_Fever'],  
 ['Buddy', 60.96, True, 24, 2, 101.5, False],  
 ['Cooper', 71.12, False, 28, 1, 105.2, True],  
 ['Max', 66.04, True, 26, 1, 100.2, False],  
 ['Bella', 50.8, False, 20, 1, 100.5, False],  
 ['Lucy', 22.86, True, 9, 1, 102.0, False],  
 ['Charlie', 33.02, True, 13, 2, 100.4, False],  
 ['Daisy', 60.96, False, 24, 1, 99.8, False],  
 ['Bailey', 25.4, False, 10, 0, 101.2, False],  
 ['Lola', 68.58, True, 27, 1, 102.5, True],  
 ['Sadie', 58.42, False, 23, 1, 99.5, False],  
 ['Penny', 45.72, True, 18, 0, 100.7, False],  
 ['Bruno', 35.56, False, 14, 1, 104.1, True],  
 ['Rosie', 33.02, True, 13, 1, 100.6, False],  
 ['Duke', 71.12, True, 28, 1, 100.1, False],  
 ['Luna', 43.18, True, 17, 3, 100.3, False],  
 ['Scout', 55.88, True, 22, 1, 103.5, True],  
 ['Rex', 58.42, False, 23, 1, 100.2, False]]
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243497

Scraped At: 2026-05-14T20:47:04.745141
