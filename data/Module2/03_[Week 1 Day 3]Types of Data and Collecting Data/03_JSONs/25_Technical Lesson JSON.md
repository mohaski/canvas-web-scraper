# Technical Lesson: JSON

# Technical Lesson: JSON

## ![Blue FS Logo](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: JSON

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[45-60 minutes]

JSON is not a tabular format with one set of rows and one set of columns. JSON files are often nested in a hierarchical structure and will have data structures analogous to Python dictionaries and lists.

Rather than write code to parse the contents of a file, we will use JSON since it is much more efficient to do so. JSON files are ubiquitous in data science, so it is important that we learn how to deal with this type of data file.

Here is a video walkthrough of the technical lesson.

[VIDEO LINK](https://player.vimeo.com/video/989669370?h=f17e136441)

### Instructions

In this technical lesson you’ll be taken through using the json module to load and extract information in a text-formatted .json file. The file contains campaign finance information for a variety of candidates who have run for office.

1. First, you will load the data using the json.load() method.
2. Once loaded, you will use your knowledge of Python data structures to navigate your way down the parsed JSON.
3. Navigating keys, you will then extract the specific data that you want.

### Step 1: JSON Module

In theory we could write our own custom code to parse the contents of the file into the appropriate Python data structures. However, this is not easy. Instead, we'll go ahead and use the pre-built Python json module designed for this purpose. The package can automatically parse jsons and interpret primitive data types so that you don’t have to deal with conversions.  
You can find full documentation for this module [in the python documentation


Links to an external site.](https://docs.python.org/3/library/json.html).

To use the json module, start by importing it:

**Input:**

```
import json
```

### Step 2: Loading a JSON File

To load data from a JSON file, you first open the file using Python's built-in open function. Then you pass the file object to the `json.load` function, which returns a Python object representing the contents of the file.

In the cell below, open the campaign finance JSON file:

**Input:**

```
with open('nyc_2001_campaign_finance.json') as f:  
    data = json.load(f)  
print(type(data))
```

**Output:**

```
<class 'dict'>
```

As you can see, this loaded the data as a dictionary. You can begin to investigate the contents of a JSON file by using our traditional Python methods.

### Step 3: Parsing a JSON File

Since we have a dictionary, check its keys:

**Input:**

```
data.keys()
```

**Output:**

```
dict_keys(['meta', 'data'])
```

Investigate what data types are stored within the values associated with those keys:

**Input:**

```
for v in data.values():  
    print(type(v))
```

**Output:**

```
<class 'dict'>  
<class 'list'>
```

### Step 4: Parsing Metadata

Then we can dig a level deeper. What are the keys of the nested dictionary?

**Input:**

```
data['meta'].keys()
```

**Output:**

```
dict_keys(['view'])
```

And what is the type of the value associated with that key?

**Input:**

```
type(data['meta']['view'])
```

**Output:**

```
dict
```

Again, what are the keys of that twice-nested dictionary?

**Input:**

```
data['meta']['view'].keys()
```

**Output:**

```
dict_keys(['id', 'name', 'attribution', 'averageRating', 'category', 'createdAt', 'description', 'displayType', 'downloadCount', 'hideFromCatalog', 'hideFromDataJson', 'indexUpdatedAt', 'newBackend', 'numberOfComments', 'oid', 'provenance', 'publicationAppendEnabled', 'publicationDate', 'publicationGroup', 'publicationStage', 'rowClass', 'rowsUpdatedAt', 'rowsUpdatedBy', 'tableId', 'totalTimesRated', 'viewCount', 'viewLastModified', 'viewType', 'columns', 'grants', 'metadata', 'owner', 'query', 'rights', 'tableAuthor', 'tags', 'flags'])
```

### Step 5: Extracting a Value from a JSON File

First let us extract a description of the dataset.

We know from our initial exploration that this JSON file contains meta and data, and that meta has this kind of high-level information whereas data has the actual records relating to campaign finance.

Looking at the keys of meta again:

**Input:**

```
data['meta']['view'].keys()
```

**Output:**

```
dict_keys(['id', 'name', 'attribution', 'averageRating', 'category', 'createdAt', 'description', 'displayType', 'downloadCount', 'hideFromCatalog', 'hideFromDataJson', 'indexUpdatedAt', 'newBackend', 'numberOfComments', 'oid', 'provenance', 'publicationAppendEnabled', 'publicationDate', 'publicationGroup', 'publicationStage', 'rowClass', 'rowsUpdatedAt', 'rowsUpdatedBy', 'tableId', 'totalTimesRated', 'viewCount', 'viewLastModified', 'viewType', 'columns', 'grants', 'metadata', 'owner', 'query', 'rights', 'tableAuthor', 'tags', 'flags'])
```

Ok, `description` is the 7th one. Let's pull the value associated with the description key:

**Input:**

```
data['meta']['view']['description']
```

**Output:**

```
'A listing of public funds payments for candidates for City office during the 2001 election cycle'
```

We have thus extracted the value from the metadata containing a description of the dataset. Indeed, this returned string is telling us exactly what the dataset is about.

### Step 6: Confronting Heterogenous Nested Data Types in JSONs

An interesting point is that the values inside the nested ‘view’ dictionary is of mixed type. Some are just values like strings like the example above. Others, like the number of comments posted on the dataset, are numeric:

**Input:**

```
print(data['meta']['view']['numberOfComments'])  
print(type(data['meta']['view']['numberOfComments']))
```

**Output:**

```
0  
<class 'int'>
```

Other keys, like the tags key, actually contain lists of what general topics the extracted dataset is relevant to:

**Input:**

```
print(data['meta']['view']['tags'])  
print(type(data['meta']['view']['tags']))
```

**Output:**

```
['finance', 'campaign finance board', 'cfb', 'nyccfb', 'campaign finance', 'elections', 'contributions', 'politics', 'campaign', 'funding']  
<class 'list'>
```

Other values actually reveal more structured information in a dictionary: for example, information about the author of the table.

**Input:**

```
print(data['meta']['view']['tableAuthor'])  
print(type(data['meta']['view']['tableAuthor']))
```

**Output:**

```
{'id': '5fuc-pqz2', 'displayName': 'NYC OpenData', 'profileImageUrlLarge': '/api/users/5fuc-pqz2/profile_images/LARGE', 'profileImageUrlMedium': '/api/users/5fuc-pqz2/profile_images/THUMB', 'profileImageUrlSmall': '/api/users/5fuc-pqz2/profile_images/TINY', 'screenName': 'NYC OpenData', 'type': 'interactive', 'flags': ['mayBeStoriesCoOwner']}  
<class 'dict'>
```

We would then have to go down yet another level if we wanted to extract the author’s display name:

**Input:**

```
print(data['meta']['view']['tableAuthor']['displayName'])  
print(type(data['meta']['view']['tableAuthor']['displayName']))
```

**Output:**

```
NYC OpenData  
<class 'str'>
```

We can see that the metadata is encoded in a logical but non-tabular format. To get the information might involve crawling down a hierarchy of data structures, exploring, and then extracting the actual values we want.

Now let's look at the main data.

### Step 7: Parsing the Main Data

This time, let's look at the value associated with the data key. Recall that we previously identified that this had a `list` data type, so let's look at the length:

**Input:**

```
len(data['data'])
```

**Output:**

```
285
```

Now let's look at a couple different values:

**Input:**

```
data['data'][0]
```

**Output:**

```
[1,  
 'E3E9CC9F-7443-43F6-94AF-B5A0F802DBA1',  
 1,  
 1315925633,  
 '392904',  
 1315925633,  
 '392904',  
 '{\n  "invalidCells" : {\n    "1519001" : "TOTALPAY",\n    "1518998" : "PRIMARYPAY",\n    "1519000" : "RUNOFFPAY",\n    "1518999" : "GENERALPAY",\n    "1518994" : "OFFICECD",\n    "1518996" : "OFFICEDIST",\n    "1518991" : "ELECTION"\n  }\n}',  
 None,  
 'CANDID',  
 'CANDNAME',  
 None,  
 'OFFICEBORO',  
 None,  
 'CANCLASS',  
 None,  
 None,  
 None,  
 None]
```

**Input:**

```
data['data'][1]
```

**Output:**

```
[2,  
 '9D257416-581A-4C42-85CC-B6EAD9DED97F',  
 2,  
 1315925633,  
 '392904',  
 1315925633,  
 '392904',  
 '{\n}',  
 '2001',  
 'B4',  
 'Aboulafia, Sandy',  
 '5',  
 None,  
 '44',  
 'P',  
 '45410.00',  
 '0',  
 '0',  
 '45410.00']
```

**Input:**

```
data['data'][2]
```

**Output:**

```
[3,  
 'B80D7891-93CF-49E8-86E8-182B618E68F2',  
 3,  
 1315925633,  
 '392904',  
 1315925633,  
 '392904',  
 '{\n}',  
 '2001',  
 '445',  
 'Adams, Jackie R',  
 '5',  
 None,  
 '7',  
 'P',  
 '11073.00',  
 '0',  
 '0',  
 '11073.00']
```

This looks more like some kind of tabular data, where the first (0-th) row is some kind of header. You may have some work to do to understand what all of the columns are supposed to mean and clean the data, but at least a general sense of what the data looks like. Note that the metadata actually contained the information the main data was tabular in nature:

**Input:**

```
data['meta']['view']['viewType']
```

**Output:**

```
'tabular'
```

Knowledge of where to look in the metadata to get layout of main data could have come in two ways:

* You were given some data schema concerning the json layout prior to wrangling.
* You figured this schema out by exploring the json layer by layer, as we basically did.

This is the general process you will use when extracting information from a JSON file.

### Summary

This is the general process you will use when extracting information from a JSON file. First you'll load the data using the json library, get a feel for the layout of the json by navigating up and down the structure (or by looking at a pre-made schema), and then extract the data you need with relevant integer/key indexing on the nested dict structure.

These extracted values can be put into your own smaller data structure (maybe another dictionary or a nested list) and then saved as a text file for further data exploration. If the data you extract can be organized in a tabular way then you might even put it into a csv.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243515

Scraped At: 2026-05-14T20:48:37.485521
