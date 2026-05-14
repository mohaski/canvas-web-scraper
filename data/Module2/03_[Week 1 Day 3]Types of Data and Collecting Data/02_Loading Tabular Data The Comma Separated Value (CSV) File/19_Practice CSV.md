# Practice: CSV

# Practice: CSV

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: CSV

Icon Progress Bar (browser only)

6 min read

You are a junior analyst for a real estate brokerage operating around the Kings County area in Washington state. This is the area including Seattle and suburban environs. You are trying to analyze housing sale prices based off of a variety of factors – including the type of property it is, whether it is a historical landmark, etc. You have just pulled a CSV that contains the information you need.

You are going to have to practice some skills you have just learned:

* Loading the contents of a .csv file into a Python data structure
* Exploring and cleaning the data
* Saving your cleaned data / writing to .csv file

### Resources

* [GitHub Repository (Practice 2 file)


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-c0w1m2)

### Instructions

### Step 1

Get the file Path for the Kings county dataset. Save it to a variable csv\_file\_path. Make sure you have the path to your data file. For this example, it is in the root folder of this repository.

### Step 2

Import the csv module.

### Step 3

Load the csv into a structure where each row is represented as a dictionary. Store it in a variable `data` and inspect the first element.

### Step 4

There are a bunch of columns that should have numeric entries.

* 'SalePrice' is quantiative
* 'PropertyType', 'PrincipalUse', 'SaleInstrument' are integers encoding categoricals. These are types -- so this is an example of label encoding a nominal categorical.
* 'PropertyClass' is an ordinal encoding the quality and condition of a property.

'ExciseTaxNbr' is a unique identifiers for a row.

Convert all of these columns that are currently strings to their appropriate datatype.

### Step 5

Clean the buyer and seller name strings by removing whitespace.

### Step 6

Create new columns for the month, day, and year of the sale transaction and include these in the dataset. Save these into `Month`, `Day`, and `Year` columns. Represent these as numbers of the correct type.

### Step 7

For the column 'AFHistoricProperty': cast 'Y' and 'N' as booleans.

### Step 8

We are only interested in using the data we have just cleaned for our analysis. Create a new version of our dataset with just the columns we cleaned. Save this to a variable called `cleaned\_data`. For your convenience we have created a list of the columns to be extracted.

```
col_list = ['ExciseTaxNbr', 'Month', 'Day', 'Year', 'SalePrice', 'PropertyType', 'PropertyClass', 'PrincipalUse', 'SaleInstrument', 'SaleReason', 'AFHistoricProperty']
```

### Step 9

Save this dictionary to a  new csv called `cleaned\_data.csv`. Use the `csv` DictWriter to do this.

You can now pick up with further cleaning, transformation, and analysis on the subset of the data we just saved at a later time.

### Solution

### Select for Solution

1. Get the file Path for the Kings county dataset. Make sure you have the path to your data file. For this example, it is in the root folder of this repository.

We use `.` to indicate the root folder of the repository when working within this notebook.

```
csv_file_path = "./King_County_Real_Estate_Sales.csv"
```

1. Import the csv module.

```
import csv
```

1. Load the csv into a structure where each row is represented as a dictionary. Store it in a variable `data` and inspect the first element.

```
with open(csv_file_path) as csvfile:  
    reader = csv.DictReader(csvfile)  
    data = list(reader)  
  
  
data[0]
```

**Output:**

```
{'ExciseTaxNbr': '2687551',  
 'Major': '138860',  
 'Minor': '110',  
 'DocumentDate': '08/21/2014',  
 'SalePrice': '245000',  
 'RecordingNbr': '20140828001436',  
 'Volume': '   ',  
 'Page': '   ',  
 'PlatNbr': '      ',  
 'PlatType': ' ',  
 'PlatLot': '              ',  
 'PlatBlock': '       ',  
 'SellerName': 'WENKLE NOEL SMITH -TRUSTEE                        ',  
 'BuyerName': 'ALEXANDER APRIL                                   ',  
 'PropertyType': '3',  
 'PrincipalUse': '6',  
 'SaleInstrument': '3',  
 'AFForestLand': 'N',  
 'AFCurrentUseLand': 'N',  
 'AFNonProfitUse': 'N',  
 'AFHistoricProperty': 'N',  
 'SaleReason': '1',  
 'PropertyClass': '8',  
 'SaleWarning': ' '}
```

1. There are a bunch of columns that should have numeric entries.

* 'SalePrice' is quantiative
* 'PropertyType', 'PrincipalUse', 'SaleInstrument' are integers encoding categoricals. These are types -- so this is an example of label encoding a nominal categorical.
* 'PropertyClass' is an ordinal encoding the quality and condition of a property.

'ExciseTaxNbr' is a unique identifiers for a row.

Convert all of these columns that are currently strings to their appropriate datatype.

```
for row in data:  
    row['SalePrice'] = int(row['SalePrice'])  
    row['PropertyType'] = int(row['PropertyType'])  
    row['PrincipalUse'] = int(row['PrincipalUse'])  
    row['SaleInstrument'] = int(row['SaleInstrument'])  
    row['SaleReason'] = int(row['SaleReason'])  
    row['PropertyClass'] = int(row['PropertyClass'])  
  
  
    row['ExciseTaxNbr'] = int(row['ExciseTaxNbr'] )  
  
  
data[0]
```

**Output:**

```
{'ExciseTaxNbr': 2687551,  
 'Major': '138860',  
 'Minor': '110',  
 'DocumentDate': '08/21/2014',  
 'SalePrice': 245000,  
 'RecordingNbr': '20140828001436',  
 'Volume': '   ',  
 'Page': '   ',  
 'PlatNbr': '      ',  
 'PlatType': ' ',  
 'PlatLot': '              ',  
 'PlatBlock': '       ',  
 'SellerName': 'WENKLE NOEL SMITH -TRUSTEE                        ',  
 'BuyerName': 'ALEXANDER APRIL                                   ',  
 'PropertyType': 3,  
 'PrincipalUse': 6,  
 'SaleInstrument': 3,  
 'AFForestLand': 'N',  
 'AFCurrentUseLand': 'N',  
 'AFNonProfitUse': 'N',  
 'AFHistoricProperty': 'N',  
 'SaleReason': 1,  
 'PropertyClass': 8,  
 'SaleWarning': ' '}
```

1. Clean the buyer and seller name strings by removing whitespace.

```
for row in data:  
    row['BuyerName'] = row['BuyerName'].strip()  
    row['SellerName'] = row['SellerName'].strip()  
  
  
data[0]
```

**Output:**

```
{'ExciseTaxNbr': 2687551,  
 'Major': '138860',  
 'Minor': '110',  
 'DocumentDate': '08/21/2014',  
 'SalePrice': 245000,  
 'RecordingNbr': '20140828001436',  
 'Volume': '   ',  
 'Page': '   ',  
 'PlatNbr': '      ',  
 'PlatType': ' ',  
 'PlatLot': '              ',  
 'PlatBlock': '       ',  
 'SellerName': 'WENKLE NOEL SMITH -TRUSTEE',  
 'BuyerName': 'ALEXANDER APRIL',  
 'PropertyType': 3,  
 'PrincipalUse': 6,  
 'SaleInstrument': 3,  
 'AFForestLand': 'N',  
 'AFCurrentUseLand': 'N',  
 'AFNonProfitUse': 'N',  
 'AFHistoricProperty': 'N',  
 'SaleReason': 1,  
 'PropertyClass': 8,  
 'SaleWarning': ' '}  
{'ExciseTaxNbr': 268
```

1. Create new columns for the month, day, and year of the sale transaction and include these in the dataset. Save these into `Month`, `Day`, and `Year` columns. Represent these as numbers of the correct type.

```
for row in data:  
    mmddyy_list = row['DocumentDate'].split('/')  
    row['Month'], row['Day'], row['Year'] = int(mmddyy_list[0]),int(mmddyy_list[1]), int(mmddyy_list[2])  
  
  
data[0]
```

```
{'ExciseTaxNbr': 2687551,  
 'Major': '138860',  
 'Minor': '110',  
 'DocumentDate': '08/21/2014',  
 'SalePrice': 245000,  
 'RecordingNbr': '20140828001436',  
 'Volume': '   ',  
 'Page': '   ',  
 'PlatNbr': '      ',  
 'PlatType': ' ',  
 'PlatLot': '              ',  
 'PlatBlock': '       ',  
 'SellerName': 'WENKLE NOEL SMITH -TRUSTEE',  
 'BuyerName': 'ALEXANDER APRIL',  
 'PropertyType': 3,  
 'PrincipalUse': 6,  
 'SaleInstrument': 3,  
 'AFForestLand': 'N',  
 'AFCurrentUseLand': 'N',  
 'AFNonProfitUse': 'N',  
 'AFHistoricProperty': 'N',  
 'SaleReason': 1,  
 'PropertyClass': 8,  
 'SaleWarning': ' ',  
 'Month': 8,  
 'Day': 21,  
 'Year': 2014}
```

1. For the following column 'AFHistoricProperty': cast 'Y' and 'N' as booleans.

```
for row in data:  
  
  
    if row['AFHistoricProperty'] == 'N':  
        row['AFHistoricProperty'] = False  
    elif row['AFHistoricProperty'] == 'Y':  
        row['AFHistoricProperty'] = True
```

1. We are only interested in using the data we have just cleaned for our analysis. Create a new version of our dataset with just the columns we cleaned. Save this to a variable called `cleaned\_data`. For your convenience we have created a list of the columns to be extracted.

```
col_list = ['ExciseTaxNbr', 'Month', 'Day', 'Year', 'SalePrice', 'PropertyType', 'PropertyClass', 'PrincipalUse', 'SaleInstrument', 'SaleReason', 'AFHistoricProperty']  
  
  
cleaned_data = []  
for row in data:  
  # Create a new dictionary to store cleaned data  
  cleaned_row = {}  
  for col in col_list:  
    # Include only columns from the list and handle potential missing values  
    cleaned_row[col] = row.get(col)  # Use get() to avoid KeyError for missing columns  
  # Append the cleaned dictionary to the cleaned_data list  
  cleaned_data.append(cleaned_row)
```

1. Save this dictionary to a  new csv called `cleaned\_data.csv`. Use the `csv` DictWriter to do this.

```
 with open('cleaned_data.csv', 'w') as f:  
    csv.DictWriter(f, cleaned_data)
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243507

Scraped At: 2026-05-14T20:47:57.206300
