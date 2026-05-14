# Summative Lab: SQL

## ![](https://moringa.instructure.com/courses/1406/files/625319/preview?) Summative Lab: SQL

In Part 1 of this assessment, you will complete several requested SQL queries in order to extract data, analyze, and provide insights from a single provided SQL database. You will also visualize the key results of 3 of these queries. There are also several 'Reflection' questions that ask you to write out a text based answer in the provided markdown cell.

In Part 2 you will explore a second dataset on your own using SQL in order to conduct a preliminary analysis. You will be asked to produce a very short slide presentation highlighting the work you did for this second section.

You will be able to:

* Interpret "word problems" and translate them into SQL queries.
* Decide and perform whichever type of JOIN is best for retrieving desired data.
* Use GROUP BY statements to apply aggregate functions like COUNT, MAX, MIN, and SUM.
* Use the HAVING clause to compare different aggregates.
* Write subqueries to decompose complex queries.
* Visualize data using matplotlib, seaborn, or pandas.
* Choose the correct chart type based on the given data.

The video below will guide you through each step of the lab. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of the lab.

[VIDEO LINK](https://player.vimeo.com/video/1009278968?h=b641dca276)

### Tools and Resources

* [GitHub Repository


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-sql-summative-lab/tree/main)

### Instructions Part 1: Guided SQL Series

For this assessment you are expected to make use of both sqlite3 and the Pandas libraries in order to write, execute, and return SQL queries as a Pandas DataFrame. Assign each returned answer as it's own explicit variable. The queries you are asked to write will become more complex over the course of the lab.

For the visualization piece you are expected to utilize either Pandas, Seaborn, or Matplotlib to create your visuals. Make sure you are providing verbose labels and titles according to the data you are being asked to visualize. Do not worry too much about choosing a 'style' or 'context' instead focus on conveying the requested information correctly.

Using the Jupyter Notebooks file in the repo link above, complete all of the steps for Parts 1 and 2.

#### Part 1: Guided SQL Series

##### Querying a Customer Database

**Business Understanding:** Your employer sells wholesale miniature models of products such as classic cars, motorcycles, and planes. They want you to pull several reports on different segments of their past customers, in order to better understand past sales as well as determine which customers will receive promotional material. They are also interested in investigating which products have performed the best, as well as having several smaller asks.

In addition to providing the requested data from the SQL database you have also been asked to create some basic visuals to display some of the more insightful information. It is up to your discretion to choose the correct plot/chart type for the data in question. Questions that want you to visualize the results will be explicitly marked.

**Data Understanding:** You may remember this database from a previous lab. As a refresher, here's the ERD diagram for this database:

[![ERD diagram of the database](https://moringa.instructure.com/courses/1406/files/625425/download?)](https://moringa.instructure.com/courses/1406/files/625425/download? "ERD diagram of the database")

###### [Step 1: Connect to Data](#dpPanel0)

* Import the necessary libraries.
* Establish a connection to the database data.sqlite.

###### [Step 2: Limited Edition California Product](#dpPanel1)

The California sales rep team is interested in running promotional material for a new limited edition model they are releasing based on the famous San Francisco Cable Cars. This product will only be available to customer stores based in California and given its high price value they want to first target promotional material to existing California customers with a high credit limit. Upon communicating with the accounting department, a credit limit of over 25,000 is considered to be high.

Execute a SQL query that returns which customers the sales rep team wants to market to first.

###### [Step 3: International Collectable Campaign](#dpPanel2)

The international sales rep team has reached out to you to help them identify partners for a 'Collectable' marketing campaign that highlights the potential collectors value in purchasing these model kits. They want to try and promote a 'collect them all' mentality. The team had a great idea to partner with any of their international customers (non-US) who have "Collect" in their name as a tie in to the larger theme.  
Execute a SQL that returns the customers in question.

**Reflection (Type your answer in the cell provided in the file):** Describe the WHERE clause you used in the above query to a non-technical manager who wants to be ensured that you are properly filtering and only selecting the requested data. How is the operator and conditional expression you are using acting to accomplish this?

###### [Step 4: USA Credit and Inventory Policy - Visual Required](#dpPanel3)

The USA based product team is planning to adjust its credit policies and inventory allocation strategy based on the average credit limit of its customers. They would like to target this strategy at a state level with several goals in mind.

1. Optimize inventory distribution:  
   1. States with higher average credit limits might be able to place larger orders, justifying priority in inventory allocation.
   2. This could help ensure that states with more purchasing power always have products in stock.
2. Tailor credit policies:  
   1. Adjust credit limits for new customers based on the state average.
   2. Identify states where they might be too conservative or too liberal with credit limits.
3. Target marketing and sales efforts:  
   1. Focus promotional campaigns on states with higher credit limits, potentially leading to larger orders.
   2. Develop strategies to increase sales in states with lower average credit limits.

Execute a SQL query that returns the information required to address this ask.

Once you have the information returned in a dataframe, select an appropriate visualization to represent this data. You are welcome to utilize matplotlib, seaborn, or pandas plotting to produce your visual. Ensure that it has a verbose title and axis labels!

###### [Step 5: Top Customers - Visual Required](#dpPanel4)

The company is approaching its 10 year anniversary and wants to acknowledge and thank its top customers with personalized communication. They have asked you to determine the top 10 customers based on the total amount of payments made, making sure to return the customer name for clarity.

Execute a SQl query that returns the information required to address this ask.

Once you have the information returned in a dataframe, select an appropriate visualization to represent this data. You are welcome to utilize matplotlib, seaborn, or pandas plotting to produce your visual. Ensure that it has a verbose title and axis labels.

###### [Step 6: Top Customer + Product Quantities](#dpPanel5)

The product team is running an analysis on popular and common products sold to each customer in order to try and determine what new products they should be looking at to include in their catalog. This data will also be used by individual sales reps to recommend similar products to each customer next time they place an order.

They have asked you to query information, for each customer, about any product they have purchased 10 or more units of. In addition they would like the full set of data to be sorted in ascending order by the total amount purchased.

Execute a SQL query that returns the information required to address this ask.

*Hint: For this one, you'll need to make use of HAVING, GROUP BY, and ORDER BY — make sure you get the order of them correct.*

###### [Step 7: Product Analysis - Visual Required](#dpPanel6)

The product team is looking into the demand across its different product lines. They are conducting a comprehensive review of its product portfolio and inventory management strategies. You have been asked to query data pertaining to each different product line, that contains the total quantity ordered and the total number of products for each respective product line. By examining the number of products and total quantity ordered for each product line, the company aims to:

1. Optimize product mix:  
   1. Identify which product lines have the most diverse offerings (high number of products).
   2. Determine which lines are most popular (high total quantity ordered).
   3. Compare if lines with more products necessarily lead to more orders.
2. Improve inventory management:  
   1. Adjust stock levels based on the popularity of each product line.
   2. Identify potential overstocking in lines with low order quantities.
   3. Ensure adequate variety in high-performing product lines.
3. Adjust marketing strategy:  
   1. Focus promotional efforts on product lines with high potential (many products but lower order quantities).
   2. Capitalize on the popularity of high-performing lines in marketing campaigns.
4. Advise Product development:  
   1. Invest in expanding product ranges for lines with high order quantities.
   2. Consider phasing out or revamping product lines with low numbers of products and low order quantities.

*Hint: Think about how you can and might have to utilize SQL DISTINCT statement.*

Execute a SQL query that returns the information required to address this ask.

Once you have the information returned in a dataframe, select an appropriate visualization to represent the relationship between total quantity ordered and the number of products in order to perform a preliminary investigation into the question of if more products lead to more orders. You are welcome to utilize matplotlib, seaborn, or pandas plotting to produce your visual. Ensure that it has a verbose title and axis labels.

**Reflection (Type your answer in the cell provided in the file):** Please explain your choice in the type of visual you used in order to highlight and represent the data from the above query. In a non-technical manner explain why that chart type makes sense for the information being conveyed. What does this visual convey in the context of the question it was asked for?

###### [Step 8: Remote Offices](#dpPanel7)

Upper management is considering a shift to hybrid and remote work for certain locations and roles. They have tasked you with providing them data about employees who work in any office that has fewer than 5 total employees so they can better understand how to support those employees remotely when offices are shut down.

Be sure to include information about the employees job and supervisor so management can adjust everyone to remote work properly.

*Hint: Utilize a subquery to find the relevant offices.*

Execute a SQL query that returns the information required to address this ask.

**Reflection (Type your answer in the cell provided in the file):** Describe how you decided on the subquery that you used in the query above? This answer can be technically in nature, describing your thought process in how the main query is utilizing the subquery to return the correct data.

###### [Step 9: Close the Connection](#dpPanel8)

Now that you are finished executing your queries and retrieving the required information you always want to make sure to close the connection to your database.

In this initial portion of the assessment, you produced several data queries and visualizations for a model company, mainly focused around its customer and product data. You wrote and engineered specific SQL queries to address pertinent questions and asks from the company. Along the way, you utilized many of the major concepts and keywords associated with SQL SELECT queries: FROM, WHERE, GROUP BY, HAVING, ORDER BY, JOIN, SUM, COUNT, and AVG.

### Instructions Part 2: Exploratory Analysis with SQL

In this open-ended exploratory section, you will analyze real-world data from the movie industry. As a data analyst, you have the freedom to investigate questions and topics that intrigue you within this dataset. The database schema and Entity-Relationship Diagram (ERD) are provided below for your reference. A general overview and instructions are also provided below.

#### Objectives

* Initial Exploration:  
  + Use SQL in combination with Pandas to explore the database.
  + Identify interesting trends, patterns, or relationships in the data.
* Business Question Formulation:  
  + Develop at least one substantial business question for deeper analysis.
  + Ensure the question is relevant, specific, and can be addressed with the available data.
* Data Cleaning Assessment:  
  + Identify potential data cleaning tasks necessary for your deeper analysis.
  + Note: You are not required to perform the cleaning, only to recognize and list the necessary tasks.
* Null Value Handling:  
  + Be aware that the dataset contains null values in certain fields.
  + Exclude these null values from your exploration.
  + Do not attempt to input or fill in missing information.

#### Deliverables

You need to produce a short slide presentation (3-5 slides) that highlights the three key deliverables below. Utilize a data visualization to support the second deliverable.

1. A summary of your initial data exploration findings: Can be bulleted or in sentence form.
2. At least one well-formulated business question for further analysis: Should stem from a relevant trend or pattern your initial exploration identified.
3. A list of potential data cleaning tasks identified during your exploration: This can and should include things like data normalization/standardization and null handling.

**Tips for Success:**

Begin with broad exploratory queries to understand the data's scope and content. Then focus on honing in on interesting relationships between different data categories. Consider industry trends, audience preferences, or financial aspects when formulating your business question. Pay attention to data quality issues, inconsistencies, or limitations that might affect your analysis. Remember, the goal is to demonstrate your analytical thinking and ability to derive meaningful insights from complex datasets. Good luck with your exploration!

**NOTE:** You do not need to explore every aspect of this database. Find something that you think is interesting or relevant about the data and focus your exploration there.

```
# Run this cell without changes  
import zipfile  
  
zip_file_path = 'im.db.zip'  
extract_to_path = './'  
  
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:  
    zip_ref.extractall(extract_to_path)  
  
# Connection  
conn4 = sqlite3.connect('im.db')  
  
# Schema  
schema_df = pd.read_sql("""  
SElECT * FROM sqlite_master                          
""", conn4)  
schema_df
```

**Output:**

Output: Initial Query

|  | type | name | tbl\_name | rootpage | sql |
| --- | --- | --- | --- | --- | --- |
| 0 | table | movie\_basics | movie\_basics | 2 | CREATE TABLE "movie\_basics" (\n"movie\_id" TEXT... |
| 1 | table | directors | directors | 3 | CREATE TABLE "directors" (\n"movie\_id" TEXT,\n... |
| 2 | table | known\_for | known\_for | 4 | CREATE TABLE "known\_for" (\n"person\_id" TEXT,\... |
| 3 | table | movie\_akas | movie\_akas | 5 | CREATE TABLE "movie\_akas" (\n"movie\_id" TEXT,\... |
| 4 | table | movie\_ratings | movie\_ratings | 6 | CREATE TABLE "movie\_ratings" (\n"movie\_id" TEX... |
| 5 | table | persons | persons | 7 | CREATE TABLE "persons" (\n"person\_id" TEXT,\n ... |
| 6 | table | principals | principals | 8 | CREATE TABLE "principals" (\n"movie\_id" TEXT,\... |
| 7 | table | writers | writers | 9 | CREATE TABLE "writers" (\n"movie\_id" TEXT,\n ... |

#### The Data

[![Movie data ERD](https://moringa.instructure.com/courses/1406/files/625358/download?)](https://moringa.instructure.com/courses/1406/files/625358/download? "Movie data ERD")

##### Database Content:

* Source: IMDB
* Time Range: Movies released between 2010 and 2019
* Note: Exclude any movies with a start\_year after 2019 as this data is not current or accurate

Available Data Categories:

* Genre
* Runtime
* Personnel (writers, directors, actors)
* Movie ratings

### Submission and Grading Criteria

1. Use the rubric below to review the grading criteria and expectations for this assessment.
2. Complete this assignment using the provided GitHub repository files and slide presentation software of your choosing (PowerPoint, Google Slides, etc.).
3. When you are ready to submit, click **Start Assignment**.
4. Upload your slide presentation and include the link to your Jupyter Notebooks file in the comments section of the upload submission screen.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243962

Scraped At: 2026-05-14T21:24:44.894902
