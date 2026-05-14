# Example: Aggregating, Reshaping, and Combining Dataframes

# Example: Aggregating, Reshaping, and Combining Dataframes

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Example: Aggregating, Reshaping, and Combining Dataframes

* [Page: Introduction to Data Analysis with Pandas (1 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243579 "Page: Introduction to Data Analysis with Pandas (1 of 26)")
* [Page: Introduction to Pandas Dataframes and Series (2 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243581 "Page: Introduction to Pandas Dataframes and Series (2 of 26)")
* [Page: What are Pandas Dataframes and Series? (3 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243582 "Page: What are Pandas Dataframes and Series? (3 of 26)")
* [Page: Process: Using Pandas Series and Dataframes (4 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243583 "Page: Process: Using Pandas Series and Dataframes (4 of 26)")
* [Page: Summary: Pandas Series and Dataframes (5 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243584 "Page: Summary: Pandas Series and Dataframes (5 of 26)")
* [Page: Check for Understanding: Pandas Dataframes and Series (6 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243586 "Page: Check for Understanding: Pandas Dataframes and Series (6 of 26)")
* [Page: Technical Lesson: Pandas Dataframe and Series (7 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243587 "Page: Technical Lesson: Pandas Dataframe and Series (7 of 26)")
* [Page: Practice: Pandas Dataframes and Series (8 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243588 "Page: Practice: Pandas Dataframes and Series (8 of 26)")
* [Page: Introduction to Data Cleaning with Pandas (9 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243590 "Page: Introduction to Data Cleaning with Pandas (9 of 26)")
* [Page: What is Data Cleaning with Pandas? (10 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243591 "Page: What is Data Cleaning with Pandas? (10 of 26)")
* [Page: Example: Data Cleaning in Healthcare Using Pandas (11 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243592 "Page: Example: Data Cleaning in Healthcare Using Pandas (11 of 26)")
* [Page: Process: Data Cleaning with Pandas (12 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243594 "Page: Process: Data Cleaning with Pandas (12 of 26)")
* [Page: Summary: Data Cleaning with Pandas (13 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243595 "Page: Summary: Data Cleaning with Pandas (13 of 26)")
* [Page: Check for Understanding: Data Cleaning with Pandas (14 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243596 "Page: Check for Understanding: Data Cleaning with Pandas (14 of 26)")
* [Page: Technical Lesson: Data Cleaning with Pandas (15 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243597 "Page: Technical Lesson: Data Cleaning with Pandas (15 of 26)")
* [Page: Practice: Data Cleaning with Pandas (16 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243598 "Page: Practice: Data Cleaning with Pandas (16 of 26)")
* [Page: Introduction to Aggregating, Reshaping, and Combining Dataframes (17 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243600 "Page: Introduction to Aggregating, Reshaping, and Combining Dataframes (17 of 26)")
* [Page: What is Aggregating, Reshaping, and Combining Dataframes? (18 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243602 "Page: What is Aggregating, Reshaping, and Combining Dataframes? (18 of 26)")
* [Page: Current: Example: Aggregating, Reshaping, and Combining Dataframes (19 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243603 "Page: Current: Example: Aggregating, Reshaping, and Combining Dataframes (19 of 26)")
* [Page: Process: How to Aggregate, Reshape, and Combine DataFrames (20 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243604 "Page: Process: How to Aggregate, Reshape, and Combine DataFrames (20 of 26)")
* [Page: Summary: Aggregating, Reshaping, and Combining Dataframes (21 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243605 "Page: Summary: Aggregating, Reshaping, and Combining Dataframes (21 of 26)")
* [Page: Check for Understanding: Aggregating, Reshaping, and Combining Dataframes (22 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243606 "Page: Check for Understanding: Aggregating, Reshaping, and Combining Dataframes (22 of 26)")
* [Page: Technical Lesson: Aggregating, Reshaping, and Combining Dataframes (23 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243607 "Page: Technical Lesson: Aggregating, Reshaping, and Combining Dataframes (23 of 26)")
* [Page: Practice: Aggregating, Reshaping, and Combining Dataframes (24 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243609 "Page: Practice: Aggregating, Reshaping, and Combining Dataframes (24 of 26)")
* [Lab: Data Analysis with Pandas (25 of 26), Assignment](https://moringa.instructure.com/courses/1406/modules/items/243611 "Lab: Data Analysis with Pandas (25 of 26), Assignment")
* [Quiz: Data Analysis with Pandas (26 of 26)](https://moringa.instructure.com/courses/1406/modules/items/243612 "Quiz: Data Analysis with Pandas (26 of 26)")

2 min read

### Scenario: Patient Outcomes and Treatment Plans

![Patient and doctor looking at a glucose meter together.](https://moringa.instructure.com/courses/1406/files/624762/download)
A hospital aims to improve patient outcomes and personalize treatment plans for chronic diseases like diabetes. They have data collected from various sources:

* **Patient Records:** This dataset holds demographic information about patients (age, gender, ethnicity), along with medical history and diagnoses.
* **Lab Results:** This dataset contains results from various laboratory tests performed on patients, including blood sugar levels, cholesterol levels, and other relevant biomarkers.
* **Treatment Records:** This dataset tracks treatment plans administered to patients, including medication details (type, dosage, frequency), and treatment duration.

#### Business Goal

Identify correlations between patient demographics, lab test results, and treatment responses to personalize treatment plans for better patient outcomes.

* **Joining Datasets:** Pandas' joining functions (like merge) becomes crucial. Patient records can be merged with lab results based on a unique patient ID, and then further merged with treatment records using the same patient ID. This consolidates all relevant information into a single, unified dataset.
* **Data Reshaping:** It is often advantageous to experiment with reshaping the data in particular ways. For example, the analyst in this case might want to display the average metrics of various lab measurements (blood sugar, cholesterol) as a function of  a patient demographic (e.g., age group).   
  One could use pivot table reshaping to represent this data with the rows indexed by demographic, the columns as the lab measurement type, and the average response metrics as the values within each cell.
* **Groupby Aggregation:**  Alternatively, one could use other types of organization such as multi-indexing to display this same data in a different way. Using groupby, the data can be grouped by patient demographics (e.g., age group), patient conditions, and specific lab tests organized by a multi-index. Aggregate statistics like average post-treatment lab values, average reduction in blood sugar levels  can then be calculated and organized by group/sub-group.

By analyzing the joined and grouped data, valuable insights can be gleaned. For instance, the hospital might discover that a specific medication works best for younger, diabetic patients with high initial blood sugar levels. This knowledge equips healthcare professionals to personalize treatment plans by tailoring medication types and dosages based on a patient's unique demographics and lab results. This data-driven approach can ultimately lead to improved patient outcomes and more effective chronic disease management.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243603

Scraped At: 2026-05-14T20:58:02.623136
