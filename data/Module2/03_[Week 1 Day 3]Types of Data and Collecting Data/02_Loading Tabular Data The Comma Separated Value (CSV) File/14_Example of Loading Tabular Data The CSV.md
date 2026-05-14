# Example of Loading Tabular Data: The CSV

# Example of Loading Tabular Data: The CSV

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Example of Loading Tabular Data: The CSV

Icon Progress Bar (browser only)

2 min read

### Exxon

![Oil rig with sunset in background](https://moringa.instructure.com/courses/1406/files/625259/download)

**Problem**

Imagine you're a junior data scientist at Exxon. The senior data scientist on your team  has just handed you a CSV file named "well\_data.csv" containing critical information about oil well production in the Permian basin for the past five months. Data included are well identifiers, dates on which production at a well was recorded, oil and water production in barrels per day, natural gas extracted in the volumetric measure of thousand cubic feet per day, and downhole pressure (pressure of the oil and gas reservoir beneath the wellbore). You have been tasked with initial data cleaning and exploration.

**Data Science Solution**

First, you might use the `csv.DictReader` object to load in the "well\_data.csv" file into a dictionary, parse the string column names, and convert numeric data types to float. Then you will execute any required cleaning tasks. Missing entries and data outliers are very possible here as the sensors are acquiring their measurements under high temperature and pressure environments.

Once the data is clean, you could use the `csv.writer` or `csv.DictWriter` to save your data to a CSV file ("cleaned\_well\_data.csv") . The CSV can then act as a starting point for your exploratory data analysis as well as a common data source that the senior data scientist can use to check on and build off your work.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243501

Scraped At: 2026-05-14T20:47:25.563723
