# Practice: JSON

# Practice: JSON

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: JSON

Icon Progress Bar (browser only)

10 min read

JSON files are widely used in data science and in this practice, we'll see how they can be used in a real-life example of NYC campaign finance auditing. Without knowledge of these types of data files, it would be a struggle to do this analysis.

### NYC Campaign Finance Auditor: Monitoring Campaign Payment Matching for Each Candidate

You are an independent auditor for the NYC Campaign Finance program. The City of New York provides matching funds for eligible contributions made to candidates, using various ratios depending on the contribution amount (more details here). As an auditor you want to get the details on the amounts that NYC gives to each candidate’s campaign through this program. You have extracted relevant data from NYC’s Open data portal for matching contributions. This dataset has been downloaded via API request as a JSON file: nyc\_2001\_campaign\_finance.json, (same as in the previous lesson).

The dataset is separated into meta, which contains metadata, and data, which contains the actual campaign finance records. You will need to use the information in meta to understand how to interpret the information in data.

Your goal is to extract a list containing the name of a candidate in the 2001 election along with the total payments they received. This should be structured as a list of tuples (candidate\_name, amount) as shown below:

```
[  
    ("John Smith", 62184.00),  
    ("Jane Doe", 133146.00),  
    ...  
]
```

The list should contain 284 tuples, since there were 284 candidates.

### Resources

* [GitHub Repository (Practice 3 file)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m2)

### Instructions

* [Step 1](#dpPanel0Content)
* [Step 2](#dpPanel1Content)
* [Step 3](#dpPanel2Content)

#### Open the Dataset

* Import the json module.
* Open the nyc\_2001\_campaign\_finance.json file using the built-in Python open function.
* Load all of the data from the file into a Python object using json.load.
* Assign the result of `json.load` to the variable name data.

```
# Your code here
```

Recall the overall structure of this dataset:

```
# Run this cell without changes  
  
print(f"The overall data type is {type(data)}")  
print(f"The keys are {list(data.keys())}")  
print()  
print("The value associated with the 'meta' key has metadata, including all of these attributes:")  
print(list(data['meta']['view'].keys()))  
print()  
print(f"The value associated with the 'data' key is a list of {len(data['data'])} records")
```

#### Find the Column Names

We know that each record in the data list looks something like this:

```
# Run this cell without changes  
data['data'][1]
```

We could probably guess which of those values is the candidate name, but it's unclear which value is the total payments received. To get that information, we need to look at the metadata.

Investigate the value of data['meta']['view']['columns'].

##### 1. Let data['meta']['view']['columns'] be called column\_data. Verify that column\_data results in a list.

```
# Your code here (create more cells as needed)  
column_data = None
```

##### 2. Now look at the first few entries of column\_data.

The result should look something like this:

```
 [  
    "sid",  
    "id",  
    "position",  
    ...  
]
```

```
# Your code here (create more cells as needed)  
  
# With a list, it's often useful to look at the  
# first entry, or first few entries
```

column\_data currently contains significantly more information than we need. Extract just the values associated with the name keys using list comprehension, so we have a list of the column names.

##### 3. Now name this variable column\_names.

```
# Your code here (create more cells as needed)
```

```
column_names = None  
# Run this cell without changes  
  
# There should be 19 names  
assert len(column_names) == 19  
# CANDNAME and TOTALPAY should be in there  
assert "CANDNAME" in column_names and "TOTALPAY" in column_names
```

Ok, now we know what each of the columns represents.

The columns we are looking for are called CANDNAME and TOTALPAY. Now that we have this list, we should be able to figure out which of the values in each record lines up with those column names.

#### Loop Over the Records to Find the Names and Payments

The data records are contained in data['data'].

To loop over the records to find the names and payments, first we need to determine the indices of the candidate names and the total payments.

Let name\_index be the column names of CANDNAME and total\_payments\_index be the column names of TOTALPAY. After correctly defining name\_index and total\_payments\_index, print their respective indices.

```
# Your code here (create more cells as needed)  
  
# In theory we could just look at the list and  
# count by hand to figure out the index of these  
# strings, but Python can do it for us  
  
name_index = None  
total_payments_index = None
```

Now loop over the records in data['data'] and extract the name from name\_index and total payment from total\_payments\_index. Make sure you convert the total payment to a float, then make a tuple representing that candidate. Append the tuple to an overall list of results called candidate\_total\_payments.

Recall that the first (0-th) one is more of a header and should be skipped over.

To verify that your loop worked, print the first five and the last five records.

```
# Your code here (create more cells as needed)  
  
candidate_total_payments = []  
  
# Loop over records starting at index 1 to skip header  
  
   
  
# Print the first five and last five  
# Run this cell without changes  
  
# There should be 284 records  
assert len(candidate_total_payments) == 284  
  
# Each record should contain a tuple  
assert type(candidate_total_payments[0]) == tuple  
  
# That tuple should contain a string and a number  
assert len(candidate_total_payments[0]) == 2  
assert type(candidate_total_payments[0][0]) == str  
assert type(candidate_total_payments[0][1]) == float
```

Now that we have this result, we can answer questions like: *which candidates received the most total payments from the city?*

```
# Run this cell without changes  
  
# Print the top 10 candidates by total payments  
sorted(candidate_total_payments, key=lambda x: x[1], reverse=True)[:10]
```

### Solution

### [Select for Solution](#dpPanel3)

1. **Open the Dataset**

* Import the json module.
* Open the nyc\_2001\_campaign\_finance.json file using the built-in Python open function.
* Load all of the data from the file into a Python object using json.load.
* Assign the result of `json.load` to the variable name data.

**Input:**

```
import json  
  
with open('nyc_2001_campaign_finance.json') as f:  
    data = json.load(f)
```

Recall the overall structure of this dataset:

```
print(f"The overall data type is {type(data)}")  
print(f"The keys are {list(data.keys())}")  
print()  
print("The value associated with the 'meta' key has metadata, including all of these attributes:")  
print(list(data['meta']['view'].keys()))  
print()  
print(f"The value associated with the 'data' key is a list of {len(data['data'])} records")
```

```
The overall data type is <class 'dict'>  
The keys are ['meta', 'data']  
The value associated with the 'meta' key has metadata, including all of these attributes:  
  
['id', 'name', 'attribution', 'averageRating', 'category', 'createdAt', 'description', 'displayType', 'downloadCount', 'hideFromCatalog', 'hideFromDataJson', 'indexUpdatedAt', 'newBackend', 'numberOfComments', 'oid', 'provenance', 'publicationAppendEnabled', 'publicationDate', 'publicationGroup', 'publicationStage', 'rowClass', 'rowsUpdatedAt', 'rowsUpdatedBy', 'tableId', 'totalTimesRated', 'viewCount', 'viewLastModified', 'viewType', 'columns', 'grants', 'metadata', 'owner', 'query', 'rights', 'tableAuthor', 'tags', 'flags']  
  
The value associated with the 'data' key is a list of 285 records
```

1. **Find the Column Names**

We know that each record in the data list looks something like this:

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

We could probably guess which of those values is the candidate name, but it's unclear which value is the total payments received. To get that information, we need to look at the metadata.

Investigate the value of data['meta']['view']['columns'].

Let data['meta']['view']['columns'] be called column\_data. Verify that column\_data results in a list.

**Input:**

```
# First, we look at data['meta']['view']['columns']  
# What is the data type?  
  
column_data = data['meta']['view']['columns']  
type(column_data)
```

**Output:**

```
list
```

Now look at the first few entries of column\_data.  
The result should look something like this:

**Output:**

```
[  
    "sid",  
    "id",  
    "position",  
    ...  
]  
  
# With a list, it's often useful to look at the  
# first entry, or first few entries
```

**Input:**

```
column_data[:3]
```

**Output:**

```
[{'id': -1,  
  'name': 'sid',  
  'dataTypeName': 'meta_data',  
  'fieldName': ':sid',  
  'position': 0,  
  'renderTypeName': 'meta_data',  
  'format': {},  
  'flags': ['hidden']},  
 {'id': -1,  
  'name': 'id',  
  'dataTypeName': 'meta_data',  
  'fieldName': ':id',  
  'position': 0,  
  'renderTypeName': 'meta_data',  
  'format': {},  
  'flags': ['hidden']},  
 {'id': -1,  
  'name': 'position',  
  'dataTypeName': 'meta_data',  
  'fieldName': ':position',  
  'position': 0,  
  'renderTypeName': 'meta_data',  
  'format': {},  
  'flags': ['hidden']}]
```

column\_data currently contains significantly more information than we need. Extract just the values associated with the name keys using list comprehension, so we have a list of the column names.

Now name this variable column\_names.

**Input:**

```
# So, we have a list of dictionaries. We note that  
# each dictionary has the key 'name' like was mentioned  
# previously  
  
# To extract the names, let's use a list comprehension  
  
column_names = [info['name'] for info in column_data]  
column_names
```

**Output:**

```
['sid',  
 'id',  
 'position',  
 'created_at',  
 'created_meta',  
 'updated_at',  
 'updated_meta',  
 'meta',  
 'ELECTION',  
 'CANDID',  
 'CANDNAME',  
 'OFFICECD',  
 'OFFICEBORO',  
 'OFFICEDIST',  
 'CANCLASS',  
 'PRIMARYPAY',  
 'GENERALPAY',  
 'RUNOFFPAY',  
 'TOTALPAY']
```

Ok, now we know what each of the columns represents.

The columns we are looking for are called CANDNAME and TOTALPAY. Now that we have this list, we should be able to figure out which of the values in each record lines up with those column names.

1. **Loop Over the Records to Find the Names and Payments**

The data records are contained in data['data'].

To loop over the records to find the names and payments, first we need to determine the indices of the candidate names and the total payments.

Let name\_index be the column names of CANDNAME and total\_payments\_index be the column names of TOTALPAY. After correctly defining name\_index and total\_payments\_index, print their respective indices.

**Input:**

```
# In theory we could just look at the list and  
# count by hand to figure out the index of these  
# stringsp, but Python can do it for us  
  
name_index = column_names.index("CANDNAME")  
total_payments_index = column_names.index("TOTALPAY")  
  
print("The candidate name is at index", name_index)  
print("The total payment amount is at index", total_payments_index)
```

**Output:**

```
The candidate name is at index 10  
The total payment amount is at index 18
```

Now loop over the records in data['data'] and extract the name from name\_index and total payment from total\_payments\_index. Make sure you convert the total payment to a float, then make a tuple representing that candidate. Append the tuple to an overall list of results called candidate\_total\_payments.

Recall that the first (0-th) one is more of a header and should be skipped over.

To verify that your loop worked, print the first five and the last five records.

**Input:**

```
candidate_total_payments = []  
  
# Loop over records starting at index 1 to skip header  
  
for record in data['data'][1:]:  
    name = record[name_index]  
    total_payments = float(record[total_payments_index])  
    candidate_total_payments.append((name, total_payments))  
      
# Print the first five and last five  
  
print(candidate_total_payments[:5])  
print(candidate_total_payments[-5:])
```

**Output:**

```
[('Aboulafia, Sandy', 45410.0), ('Adams, Jackie R', 11073.0), ('Addabbo, Joseph P', 149320.0), ('Alamo-Estrada, Agustin', 27400.0), ('Allen, William A', 62990.0)]  
[('Wilson, John H', 0.0), ('Wooten, Donald T', 0.0), ('Yassky, David', 150700.0), ('Zapiti, Mike', 12172.0), ('Zett, Lori M', 0.0)]
```

Now that we have this result, we can answer questions like: *which candidates received the most total payments from the city?*

**Input:**

```
# Print the top 10 candidates by total payments  
  
sorted(candidate_total_payments, key= lambda x: x[1], reverse=True)[:10]
```

**Output:**

```
[('Green, Mark', 4534230.0),  
 ('Ferrer, Fernando', 2871933.0),  
 ('Hevesi, Alan G', 2641247.0),  
 ('Vallone, Peter F', 2458534.0),  
 ('Gotbaum, Betsy F', 1625090.0),  
 ('Berman, Herbert E', 1576860.0),  
 ('DiBrienza, Stephen', 1336655.0),  
 ('Stringer, Scott M', 1223721.0),  
 ('Markowitz, Marty', 1166294.0),  
 ('Thompson, Jr., William C', 1096359.0)]
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243516

Scraped At: 2026-05-14T20:48:44.441656
