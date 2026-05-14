# Technical Lesson: CSV

# Technical Lesson: CSV

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: CSV

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[45-60 minutes]

This technical lesson covers the CSV (comma-separated values) data format. You will get familiar with the features of Python’s csv library and how to read and parse data from CSV files. You will also learn how to save tabular data to a csv file.

* The first section gives you an example of how CSVs are structured and walks you through writing and reading CSVs without the csv library.
* We then introduce the csv library which makes the processing of loading CSVs and parsing headers (column names) and data types a bit easier.
* You will then go through the process of using the csv reader and DictReader to load and parse a dataset. In this case, we have taken a csv file containing data about Olympic track and field medalists downloaded from Kaggle.

CSV is a plain text, delimited format, meaning its contents are just strings with a specified structure. This structure is used to encode the tabular nature of a given dataset. An easy way to see what a CSV is to just create one from tabular data.

Here is a video walkthrough of the technical lesson.

[VIDEO LINK](https://player.vimeo.com/video/989669023?h=cc308731d9)

### Instructions

### [Step 1](#dpPanel0)

Start with a tabular dataset representing the 100 meter dash times for 4 high school athletes across 3 track meets:

100 meter dash times for 4 athletes in 3 meets

| Meet 1 | Meet 2 | Meet 3 |
| --- | --- | --- |
| 13.10 | 13.59 | 13.44 |
| 13.93 | 13.85 | 13.47 |
| 14.12 | 14.41 | 13.89 |
| 14.42 | 13.55 | 13.43 |

We could represent this dataset by a nested list in Python:

```
track_times = [  
    [13.10, 13.59, 13.44],  
    [13.93, 13.85, 13.47],  
    [14.12, 14.41, 13.89],  
    [14.42, 13.55, 13.43]  
]  
track_times
```

```
[[13.1, 13.59, 13.44],  
 [13.93, 13.85, 13.47],  
 [14.12, 14.41, 13.89],  
 [14.42, 13.55, 13.43]]
```

### [Step 2](#dpPanel1)

Now let us convert this nested list to CSV format. This means that:

* The tabular data structure is converted to a string.
* Each row is on its own line of the string (i.e. separated by a newline special character “\n")
* Each element within a row is separated by a comma. The commas separate the values of each column for a given row.

```
# Initialize an empty string  
track_times_csv = ""
```

```
# Loop over all lists in the overall list  
  
for index, athlete_times in enumerate(track_times):  
  
    # Join together the values in the nested list using  
    # a comma as a separator  
  
       athlete_times_string = ",".join([str(time) for time in athlete_times])  
  
    # Append the values to the overall string  
       track_times_csv += athlete_times_string  
  
    # Append a newline, unless this is the last row  
       if index < (len(track_times) - 1):  
        track_times_csv += "\n"  
      
track_times_csv
```

**Output:**

```
[[13.1, 13.59, 13.44],  
 [13.93, 13.85, 13.47],  
 [14.12, 14.41, 13.89],  
 [14.42, 13.55, 13.43]]
```

...and that's it! That's a CSV. Each row is separated by the new line special character \n and thus will be on a different line in the text file. The comma delimiter separates values for each column within a given row. A string structured with a delimiter and newline character can be used to represent any tabular data regardless of the data's complexity.

### [Step 3](#dpPanel2)

The next step is just to write this string to a text file. Text files in CSV format are usually saved with a \*.csv file extension:

```
with open("track_times.csv", "w") as f:  
  
  f.write(track_times_csv)
```

We can open up the file at a later time and parse it back into a Python nested list. Without any parsing, opening the file and reading it as a string behaves as we might expect:

```
with open("track_times.csv") as f:  
    track_times_csv_string_from_disk = f.read()  
track_times_csv_string_from_disk
```

**Output:**

```
'13.1,13.59,13.44\n13.93,13.85,13.47\n14.12,14.41,13.89\n14.42,13.55,13.43'
```

### [Step 4](#dpPanel3)

Three operations are required in order to parse the csv file (and the string contained therein) directly into a nested list.

* The first is to split on newline characters. This is what the .readline() method does and Python call this implicitly when you iterate over a file object.
* The string for each line needs to be need to split on the delimiter “,”
* Values need to be converted to floats

```
track_times_from_disk = []  
  
with open("track_times.csv") as f:  
    # iterate over list of lines. each row is a string.  
    for row in f:  
        # list comprehension to split row into a list on delimiter  
        # and iterate over all elements converting them to float  
        times = [float(time) for time in row.split(",")]  
  
  
        # append to row (now a list of floats) to outer list  
        track_times_from_disk.append(times)  
     
track_times_from_disk
```

**Output:**

```
[[13.1, 13.59, 13.44],  
 [13.93, 13.85, 13.47],  
 [14.12, 14.41, 13.89],  
 [14.42, 13.55, 13.43]]
```

### [Step 5](#dpPanel4)

If we did everything correctly, this new list of lists should contain the exact same data as the original:

```
track_times_from_disk == track_times
```

**Output:**

```
True
```

Great!

#### csv Module

Splitting on delimiter and type conversion was fairly easy in the last case. All the columns corresponded to the same numeric type and the commas that appeared were all clearly delimiters. Unfortunately, processing real data can involve a bit more code to execute very common tasks:

* data type checking and appropriate conversion with different data types in each column
* processing headers (column names and metadata preceding the actual tabular data)
* properly handling text data inside a CSV, e.g. if your data contains the text `"Hello, World!"` you want to make sure that the `,` is treated as part of the contents of that cell, not treated as a delimiter separating the columns
* representing your data in different types of data structures (e.g., a list of dicts as opposed to a list of lists)

The csv module simplifies a lot of this with its reader functions and associated arguments. [Here is the full documentation


Links to an external site.](https://docs.python.org/3/library/csv.html) for this module.

### [Step 6](#dpPanel5)

To use the csv module, start by importing it:

```
import csv
```

#### csv.reader

If we wanted to replicate the previous example of opening the track times CSV, this time using the csv module, that would look like this:

```
with open("track_times.csv") as f:  
      
# Pass the file in to a "reader" object and specify that  
        # values without explicit quotes (i.e. all values in this  
        # dataset) should be treated as numbers  
          
# return reader object that can act as an iterator  
# each element of the iterator contains a fully processed line as a list with types already converted  
     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)  
# Get all of the data from the reader using `list`  
      
# list() explicitly converts iterator to a list  
     track_times_with_csv_module = list(reader)  
      
track_times_with_csv_module
```

**Output:**

```
[[13.1, 13.59, 13.44],  
 [13.93, 13.85, 13.47],  
 [14.12, 14.41, 13.89],  
 [14.42, 13.55, 13.43]]
```

We have simplified the code quite a bit. After opening the file in the context manager, we just pass the file into the reader and pass arguments to the reader to convert numeric values. The reader then just spits out what we want with a simple call to the list() function. A key point is that we are operating at a higher level of abstraction and are not explicitly dealing with string cleaning operations. That is nice.

The `csv.reader` object  has additional formatting parameters and capabilities for parsing different tabular formats (i.e. text files with different delimiters, excel files, etc.) Feel free to explore these options in the [documentation


Links to an external site.](https://docs.python.org/3/library/csv.html#csv.reader).

The csv module also has a parallel [`csv.writer` object


Links to an external site.](https://docs.python.org/3/library/csv.html#csv.writer) that can take a list of lists and write it to a CSV file. Again, the object operates at a higher level of abstraction and does not require you to join elements, explicitly convert to string and add delimiter and new line characters as we had to do before.

#### csv.DictReader

One defect of the nested list representation is that the column names are contained in the first element of the outer list (i.e. at the top of the structure) and nowhere else. It might be nice if the data was structured in a way where the keys (i.e. the column names) were contained along with the values in each row. This, of course, could be accomplished by representing each row with a dictionary – the keys being column names and the values being…well…the values. The entire dataset can then be represented as a list of dictionaries. The `csv.DictReader` takes care of all of this for us without us explicitly having to parse strings, create dictionaries, and perform list append operations.

Let's actually look at a real dataset about Olympic track and field medal-winners from [kaggle


Links to an external site.](https://www.kaggle.com/jayrav13/olympic-track-field-results). The first five rows look like this:

Olympic Track and Field medal winners data

| **Gender** | **Event** | **Location** | **Year** | **Medal** | **Name** | **Nationality** | **Result** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M | 10000M Men | Rio | 2016 | G | Mohamed FARAH | GBR | 25:05.17 |
| M | 10000M Men | Rio | 2016 | S | Paul Kipngetich TANUI | KEN | 27:05.64 |
| M | 10000M Men | Rio | 2016 | B | Tamirat TOLA | ETH | 27:06.26 |
| M | 10000M Men | Beijing | 2008 | G | Kenenisa BEKELE | ETH | 27:01.17 |
| M | 10000M Men | Beijing | 2008 | S | Sileshi SIHINE | ETH | 27:02.77 |

The column names are in the first row with the corresponding values for each record in the subsequent rows.

### [Step 7](#dpPanel6)

Opening this with csv.reader:

**Windows Users:**

The default encoding type set by Windows OS is different than that of MacOS or Linux. To ensure the proper encoding when loading the usa\_2016\_gold\_medals.csv dataset you will need specify the encoding type by adding the argument encoding='utf-8'.

```
with open("results.csv") as f:  
    reader = csv.reader(f)  
    # Printing only the header and first 5 rows of data  
    for _ in range(6):  
        print(next(reader))
```

**Output:**

```
['Gender', 'Event', 'Location', 'Year', 'Medal', 'Name', 'Nationality', 'Result']  
['M', '10000M Men', 'Rio', '2016', 'G', 'Mohamed FARAH', 'GBR', '25:05.17']  
['M', '10000M Men', 'Rio', '2016', 'S', 'Paul Kipngetich TANUI', 'KEN', '27:05.64']  
['M', '10000M Men', 'Rio', '2016', 'B', 'Tamirat TOLA', 'ETH', '27:06.26']  
['M', '10000M Men', 'Beijing', '2008', 'G', 'Kenenisa BEKELE', 'ETH', '27:01.17']  
['M', '10000M Men', 'Beijing', '2008', 'S', 'Sileshi SIHINE', 'ETH', '27:02.77']
```

Then we could use list indexing to access the gender field of a given row using `[0]` or the nationality field using `[-2]`. But you can see how that would create some hard-to-read and error-prone code!

### [Step 8](#dpPanel7)

Let us use `csv.DictReader` to parse the rows into a `dict` instead, so that we could look up the gender field using `["Gender"]` or the nationality field using `["Nationality"]`. Notice that the usage pattern is basically the same as the csv.reader except that first line of text is automatically parsed as the column names to be used for dictionary keys:

```
with open("usa_2016_gold_medals.csv") as f:  
  
  
    # pass the file object into the DictReader instead of the reader  
    reader = csv.DictReader(f) # creates an iterable  
    # now convert to list  
    olympics_data = list(reader)  
  
  
# Print the first 5 rows of data  
for index in range(5):  
    print(olympics_data[index])
```

**Output:**

```
{'Gender': 'M', 'Event': '10000M Men', 'Location': 'Rio', 'Year': '2016', 'Medal': 'G', 'Name': 'Mohamed FARAH', 'Nationality': 'GBR', 'Result': '25:05.17'}  
{'Gender': 'M', 'Event': '10000M Men', 'Location': 'Rio', 'Year': '2016', 'Medal': 'S', 'Name': 'Paul Kipngetich TANUI', 'Nationality': 'KEN', 'Result': '27:05.64'}  
{'Gender': 'M', 'Event': '10000M Men', 'Location': 'Rio', 'Year': '2016', 'Medal': 'B', 'Name': 'Tamirat TOLA', 'Nationality': 'ETH', 'Result': '27:06.26'}  
{'Gender': 'M', 'Event': '10000M Men', 'Location': 'Beijing', 'Year': '2008', 'Medal': 'G', 'Name': 'Kenenisa BEKELE', 'Nationality': 'ETH', 'Result': '27:01.17'}  
{'Gender': 'M', 'Event': '10000M Men', 'Location': 'Beijing', 'Year': '2008', 'Medal': 'S', 'Name': 'Sileshi SIHINE', 'Nationality': 'ETH', 'Result': '27:02.77'}
```

The number of rows in the dataset is just the length of the resulting list:

```
len(olympics_data)
```

**Output:**

```
2394
```

### [Step 9](#dpPanel8)

Now we can perform data analysis and cleaning tasks in a neater, clearer way.  
For example, if our task was filter the data so that it only includes gold medals, that logic would look something like this:

```
gold_medals = []  
  
for row in olympics_data:  
    if row["Medal"] == "G":  
        gold_medals.append(row)  
          
print(f"""Out of {len(olympics_data)} total medals, this dataset   
contains information about {len(gold_medals)} gold medals""")
```

**Output:**

```
Out of 2394 total medals, this dataset   
contains information about 799 gold medals
```

### [Step 10](#dpPanel9)

Or if it was for all USA gold medals in 2016, what were the events and the names of the athletes, that logic would look something like this:

```
usa_2016_gold_medals = []  
  
for row in olympics_data:  
    if row["Medal"] == "G" and row["Nationality"] == "USA" and row["Year"] == "2016":  
        usa_2016_gold_medals.append({"Event": row["Event"], "Name": row["Name"]})  
usa_2016_gold_medals
```

**Output:**

```
[{'Event': '1500M Men', 'Name': 'Matthew CENTROWITZ'},  
 {'Event': '400M Hurdles Men', 'Name': 'Kerron CLEMENT'},  
 {'Event': '4X400M Relay Men', 'Name': 'null'},  
 {'Event': 'Decathlon Men', 'Name': 'Ashton EATON'},  
 {'Event': 'Long Jump Men', 'Name': 'Jeff HENDERSON'},  
 {'Event': 'Shot Put Men', 'Name': 'Ryan CROUSER'},  
 {'Event': 'Triple Jump Men', 'Name': 'Christian TAYLOR'},  
 {'Event': '100M Hurdles Women', 'Name': 'Brianna ROLLINS'},  
 {'Event': '400M Hurdles Women', 'Name': 'Dalilah MUHAMMAD'},  
 {'Event': '4X100M Relay Women', 'Name': 'null'},  
 {'Event': '4X400M Relay Women', 'Name': 'null'},  
 {'Event': 'Long Jump Women', 'Name': 'Tianna BARTOLETTA'},  
 {'Event': 'Shot Put Women', 'Name': 'Michelle CARTER'}]
```

And we could write that result to a file using csv.DictWriter ([csv.DictWriter documentation


Links to an external site.](https://docs.python.org/3/library/csv.html#csv.DictWriter)):

**Windows Users:** When using csv.DictWriter to write to a file, the default settings may cause unnecessary blank lines to be saved to the file. This can be avoided by adding the argument dialect='unix'. While this does not affect the data, it will help to mitigate any issues which may be caused by the additional blank lines when doing other data processing tasks.

### [Step 11](#dpPanel10)

```
with open("usa_2016_gold_medals.csv", "w") as f:  
    writer = csv.DictWriter(f, fieldnames=["Event", "Name"])  
    writer.writeheader()  
    for row in usa_2016_gold_medals:  
        writer.writerow(row)
```

We can use the bash command cat in a Jupyter notebook code cell to visually inspect the file that was created:  
If you are running this lesson on a Windows or other non-Unix computer, you may need to open the file directly using your text editor.

```
! cat usa_2016_gold_medals.csv
```

**Output:**

```
Event,Name  
1500M Men,Matthew CENTROWITZ  
400M Hurdles Men,Kerron CLEMENT  
4X400M Relay Men,null  
Decathlon Men,Ashton EATON  
Long Jump Men,Jeff HENDERSON  
Shot Put Men,Ryan CROUSER  
Triple Jump Men,Christian TAYLOR  
100M Hurdles Women,Brianna ROLLINS  
400M Hurdles Women,Dalilah MUHAMMAD  
4X100M Relay Women,null  
4X400M Relay Women,null  
Long Jump Women,Tianna BARTOLETTA  
Shot Put Women,Michelle CARTER
```

### Data Schema and CSV Files

A data schema is, broadly, the structure that the data is stored in. As a part of the overall data science process, understanding the schema is an important element of \*\*data understanding\*\*.

It includes some things that can be determined automatically/programmatically:

* How many rows and columns are there?
* What are the column names?
* For a given column, what is the data type (e.g. string, integer, boolean)?
* Is one of the columns a unique identifier for that record?
* Which columns can contain missing data?

Then there are other things that you might need additional documentation to determine:

* What does a row (record) represent?
* What does each column (feature) represent?
* For a numeric column, what are the units (e.g. seconds, inches, kilograms)?

Despite the high degree of structure that a CSV possesses, there is still quite some potential for ambiguity in data definitions and organization. Not grappling with and having a handle on the high level organization of your data can inject these ambiguities into your analysis and cause erroneous data cleaning and inference further down the road.

#### Data Schema of the Olympic Medals Dataset

Let's take the Olympic medals dataset we've been working with as an example.

**Possibly the most important question to ask about any CSV dataset is: What does a row represent?**

This might seem extremely obvious but it can be important to make sure you understand the details.  
With this dataset, a row represents an Olympic medal win.

It does **not** represent:

* A country (the same country can appear multiple times if it has won medals in multiple years)
* A type of Olympic track and field event (the same event name can appear multiple times if it happened in multiple years)
* An Olympic athlete (the same athlete can appear multiple times if they have won multiple medals, and some rows are team events where the name is null)
* The performance ("Result") of a given athlete in a given event in a given year, if that performance did not win a medal  
  etc.

Therefore if you were trying to answer a question about a country, a type of event, or an athlete, you would need to perform some additional filtering and/or aggregation in order to form the correct units to answer that question.

If you were trying to answer a question about the performance of athletes who did not win medals vs. those who did win medals, that would not be possible with this dataset, since this dataset only includes medal winners. It also would not allow you to answer questions about the performance of these athletes at these events outside of the Olympics (e.g. at the national championship level).

Understanding what a row represents is crucial for being able to identify what questions you can and cannot answer with a given dataset.

##### What does each column represent?

To extract the basics of this information, you can just call the .keys() on one of the row dictionaries. In this case, the columns are:

* 'Gender'
* 'Event'
* 'Location'
* 'Year'
* 'Medal'
* 'Name'
* 'Nationality'
* 'Result'

If you need to understand further details such as the capitalization style of the names or the units of the results, you can often find this information in documentation about the dataset. If not, you may need to apply your own judgment.

For example, let's look at a record from this dataset:

```
{'Gender': 'M',  
 'Event': '100M Men',  
 'Location': 'Montreal',  
 'Year': '1976',  
 'Medal': 'S',  
 'Name': 'Donald QUARRIE',  
 'Nationality': 'JAM',  
 'Result': '10.08'}
```

What do we think are the units of the Result value?

Well, if we look at the Event value, it is a 100 meter dash. That is a track event, so these are some kind of units of time.

But are they hours? Minutes? Seconds?

At this point if you are unsure, you could look up recent 100 meter dash times, or the world record best time for that event. (Although you'll want to watch out for older data like this — sometimes data from the '70s is going to have a significantly different scale compared to data from today!)

With a bit of research, it's clear that the units are *seconds*.

But what if we look at a different record:

```
olympics_data[1100]
```

**Output:**

```
{'Gender': 'M',  
 'Event': 'Discus Throw Men',  
 'Location': 'Los Angeles',  
 'Year': '1984',  
 'Medal': 'B',  
 'Name': 'John POWELL',  
 'Nationality': 'USA',  
 'Result': '65.46'}
```

Is that Result also measured in seconds?

No, this is a discus throw, which is a field event. The goal is not to finish in the least amount of time, it's to throw the discus as far as possible. So this is a unit of distance.

If we look up some more information about this event, we find that the units are meters.

It appears that the Result column contains different units depending on the event, which makes sense, since the result needed to win is different depending on the event.

As you can see, this process can take a fair amount of time if you do not have domain knowledge related to the dataset. Sometimes it is a good strategy to learn more about the columns one at a time — only as you encounter business questions that seem related to them — rather than trying to understand all of the columns before performing any analysis.

##### Is there a unique identifier?

In some datasets, one of the columns is a unique identifier, also commonly shorted as just "ID" or "id".

For example, if each record represented a country, there might be a unique identifier like USA, KEN, etc. Or a zip code for a geographical area or a social security number for a person. These unique identifiers are genuine features of the rows, and they can be helpful for merging datasets together by connecting a feature of one dataset to an identifier of another.

In other cases, there are unique identifiers that are solely artifacts of the particular dataset and are not useful for merging. For example, if we went through all 2394 records in the Olympic medals dataset and assigned them IDs 0 through 2393, we would have a unique identifier, but it would not be a genuine feature of a given row and would not be useful for merging together additional data. SQL databases often have this type of unique identifier, called a "primary key".

This dataset does not have a unique identifier, since almost all of the values appear more than once. There are multiple gold medals, multiple events from 2016, multiple men's events, etc. Nevertheless we could potentially merge it with other tables if those tables had one or more of these features. For example, we could add in the GDP of the athlete's home country for that year if we found a table of countries labeled similarly and their GDP by year.

#### Schemas Conclusion

Now that you have the tools to start working with actual datasets, your tasks as a data scientist have expanded beyond just technical code implementation tasks into analysis tasks. Often there will not be a single "right answer" and you will need to contend with ambiguity and uncertainty about what is in your dataset and what questions you can answer.

Considering the schema is a great place to start when answering these questions.

One way to get more practice with this is open-ended data exploration. For example, check out this website for a list of open data portals, many of which offer CSV data. You can even explore the collection of data portals programmatically using a CSV!

### Summary

In this lesson, you learned the basics of the CSV data format and looked at an example using pure Python to read/write data from/to file. Then you were introduced to the simpler, more sophisticated technique of using the csv module. Finally, you were introduced to some of the concepts of data schemas in general, how they apply to CSV formats, and what questions to ask when you encounter a new dataset.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243506

Scraped At: 2026-05-14T20:47:51.487762
