# Introduction to Data Analysis with Pandas

# Introduction to Data Analysis with Pandas

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Introduction to Data Analysis with Pandas

Icon Progress Bar (browser only)

4 min read

So far, you have been pulling data from text-based files and loading them into various Python data structures (e.g., nested lists, arrays, and dictionaries) for cleaning, transformation and basic analysis. Leveraging objects like the CSV module’s DictReader has made some aspects of loading and parsing data a bit easier. However, particularly for tabular data, a foundational problem remains. List of lists and list of dictionaries are not particularly effective data structures for wrangling tabular data. You may have noticed this when trying to extract all the data in a particular column from a list of dictionaries. Such a simple operation requires writing a comprehension or for-loop. The situation only gets worse from here.

The joint tasks of data wrangling and analysis require routines that are common yet whose implementation on a base Python data structure would require quite a bit of function writing, looping, and complex control statements. Such routines might be the merging of two relevant tabular datasets; automatic and intelligent data type handling; finding and dealing with empty or corrupted values; eliminating duplicate records; getting summary statistics for a feature conditioned on a categorical (e.g., average petal length and standard deviation for different subspecies of Iris flowers); and . . . the list goes on and on. Perhaps what we need is a library built for tabular data wrangling and analysis*—*one that possesses native tabular data structures with built-in and standardized functionality for cleaning and statistical analysis.

Pandas is this library. In this module, you will explore its power and learn to wield it effectively. The first topic will introduce the core data structures of Pandas: the Series and the DataFrame.  As you will see, these structures are designed for storing, accessing, and manipulating tabular data. In the second topic you will explore Pandas’ functionality for data cleaning. Tasks like string cleaning, dealing with missing values and duplicate entries are all easily executed with functions already built into the Series and DataFrame. Finally, in the third topic, you will delve into Pandas’s functionality for merging datasets from multiple sources, reshaping and transforming data into suitable form, and analyzing data using grouping and statistical aggregation techniques.

Watch the videos below to learn more about Data Analysis with Pandas.

### Part 1

[VIDEO LINK](https://player.vimeo.com/video/1010393952?h=842b037980)

### Part 2

[VIDEO LINK](https://player.vimeo.com/video/1010394012?h=533df0f36c)

### Part 3

[VIDEO LINK](https://player.vimeo.com/video/1010394114?h=e3946bb521)

### Industry Examples

#### Retail

**![Full mini shopping cart on top of a cell phone](https://moringa.instructure.com/courses/1406/files/625148/download)
Business Problem:**

E-commerce companies strive to personalize product recommendations for each customer to increase sales and customer satisfaction. This requires analyzing customer purchase history, product attributes, and user behavior data.

**Solution with Pandas:**

Pandas enables e-commerce companies to:

* Load and clean customer purchase history data, including items bought, browsing behavior, and demographics.
* Analyze purchase patterns and identify relationships between products.
* Group customers with similar buying habits to create targeted recommendations.
* Integrate Pandas with recommendation algorithms for personalized product suggestions.

---

#### Sports Industry

**![Male athlete in a sprint pose with charts and lights overlayed on and around him](https://moringa.instructure.com/courses/1406/files/625131/download)
Business Problem:**

Professional sports teams collect a wealth of data on player performance, including statistics, game footage, and wearable sensor readings. This data needs to be analyzed to identify key performance indicators (KPIs) and optimize player training strategies.

**Solution with Pandas:**

Pandas allows sports analysts to:

* Load and integrate data from various sources like player statistics databases, wearable sensors, and video tracking systems.
* Clean and combine data sets, ensuring consistency and addressing missing values.
* Calculate advanced performance metrics based on complex formulas and statistical analysis.
* Group data by player position, opponent, or game context to identify trends and patterns in player performance.
* Use Pandas' visualization capabilities to create charts and heatmaps that highlight strengths and weaknesses in player performance.

### Learning Outcomes

After completing this lesson, you should be able to:

* Load/write .csv and .json files into/from pandas DataFrames.
* Use pandas methods and attributes to access high level information and summary statistics about data contained in Series and DataFrames.
* Access pandas data using row and column indexing for Series and DataFrames and boolean mask techniques.
* Apply functions to data in Series and DataFrames using the  .map() and .apply() methods.
* Perform operations to change the structure of pandas DataFrames.
* Merge pandas DataFrames and reshape using hierarchical indexing, pivoting, and melting.
* Calculate summary statistics across categorical variables using the split-apply-combine paradigm and groupby/aggregation operations.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243579

Scraped At: 2026-05-14T20:55:51.836436
