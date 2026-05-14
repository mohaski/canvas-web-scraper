# What is the Comma Separated Value (CSV) File?

# What is the Comma Separated Value (CSV) File?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What is the Comma Separated Value (CSV) File?

Icon Progress Bar (browser only)

3 min read

**CSVs (Comma-Separated Values) Files** are a file format for storing tabular data in a plain text format. Some defining characteristics are:

* **Structure:** Data is organized in rows and columns, similar to a spreadsheet.
* **Values:** Each data point within the table is called a value.
* **Delimiters:** Commas are the most common delimiter, separating values within a row. Other delimiters like semicolons or tabs can also be used.
* **Rows:** Horizontal units of data representing individual records.
* **Columns:** Vertical units of data representing specific attributes or categories for the data points in each row.

We will be using the **Python csv Library.** This library provides tools to interact with CSV files in Python programs and can be helpful in data type handling. The following objects provided by the csv library are particularly useful for file input and output.

* **csv.reader:** This object is used to **read** data from a CSV file. It iterates over the file, returning each row as a list of values.
* **csv.DictReader:** An extension of `csv.reader`, specifically designed to read CSV files where the first row contains column names. This object returns each row as an ordered dictionary, where the keys are the column names and the values are the corresponding data points in that row.
* **csv.writer:** This object is used to **write** data from a Python program into a CSV file. It takes a list of rows (where each row is a list of values) and writes them to the specified file.

### How Does it Work?

CSVs are a common format that you will encounter when getting data from collaborators or from publicly accessible data repositories. Examples of such repositories are Kaggle or the UCI Machine Learning Repository. As a precursor to working on such datasets, you will need to load your CSVs into Python data structures. The reader and DictReader from the csv library will be a workhorse in these operations when using base Python.

CSVs are also commonly used to share cleaned and transformed tabular data that you have with others. Remember that you will often be getting raw data that is dirty and with a variety of inconsistencies. The data also may not be shaped in a way apt for a particular analysis task. After you have cleaned and transformed your tabular dataset accordingly, it is a good idea to save the cleaned data onto disk as a CSV. The writer from the csv module provides a convenient way of doing this. The CSV containing your cleaned data can then be used as a starting point for your own analysis downstream. Your collaborators can also pull this data and work on the same project with the assurance that they are starting from the same point as you are.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243500

Scraped At: 2026-05-14T20:47:19.034105
