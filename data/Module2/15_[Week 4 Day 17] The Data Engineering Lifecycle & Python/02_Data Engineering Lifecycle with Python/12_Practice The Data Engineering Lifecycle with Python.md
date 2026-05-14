# Practice: The Data Engineering Lifecycle with Python

# Practice: The Data Engineering Lifecycle with Python

## ![](https://moringa.instructure.com/courses/1406/files/625387/preview) Practice: The Data Engineering Lifecycle with Python

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

In this practice, you will delve into the fundamental stages of the data engineering pipeline, all within the context of Python programming, with a particular emphasis on the powerful libraries NumPy and Pandas. By constructing a simple yet comprehensive data pipeline for weather data analysis, you will gain hands-on experience in each critical step of the process, from the initial generation of data to its final presentation in a meaningful format.

After going through the code, you will also be required to interpret the code you write and the output it generates. This will involve understanding the purpose and functionality of each line of code, predicting and verifying the output at various stages, and troubleshooting any issues that arise.

By engaging with both the construction and analysis of the data pipeline, you will develop a deeper understanding of how data engineering principles are applied in real-world scenarios, and how Python can be leveraged to handle data efficiently and effectively. This comprehensive approach will equip you with the skills needed to manage data pipelines in more complex projects, preparing you for challenges you may encounter as a data scientist in the industry.

Imagine you're working as a junior data scientist at a retail company that sells a variety of products, including electronics, clothing, and books. The company has been collecting sales data over a period of time and now wants to analyze this data to gain insights into sales trends, customer preferences, and overall revenue generation.

The provided dataset represents a snapshot of sales transactions over a 10-day period in May 2023. Each transaction records the following details:

* **Order ID:** A unique identifier for each sales transaction.
* **Order Date:** The date on which the transaction took place.
* **Product ID:** A unique identifier for each product sold.
* **Product Category:** The category to which the product belongs, such as Electronics, Clothing, or Books.
* **Quantity:** The number of units of the product sold in that transaction.
* **Unit Price:** The price per unit of the product.
* **Customer ID:** A unique identifier for the customer who made the purchase.

In particular, the code does the following:

* **Generation:** You will start by generating sample weather data in CSV format. This step simulates the process of collecting raw data from weather stations or sensors.
* **Storage:** Once generated, the data will be stored in a local file system. This step represents how data is typically saved in storage solutions like data lakes or databases, ensuring that it is organized and accessible.
* **Ingestion:** In this stage, you will read the stored weather data into a Pandas DataFrame. This mimics the process of loading data from storage into a data processing environment where it can be further manipulated.
* **Transformation:** Here, you will clean, format, and engineer features from the ingested data. This stage is crucial as it prepares the data for analysis, ensuring it is accurate, consistent, and ready for insights to be drawn.
* **Serving Data:** Finally, you will serve the transformed data by creating a simple visualization using Matplotlib. This step illustrates how processed data is often presented to stakeholders in a meaningful way, enabling data-driven decision-making.

### Resources

* [GitHub Repository


  Links to an external site.](https://github.com/bpurdy-ds/dsc-c1w1m6)

### Instructions

Run the code below on your own and then answer the questions that follow. When you are finished, you can check your answers in the Solution section.

```
import csv  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
# Step 1: Generation  
sales_data = [  
    ['1001', '2023-05-01', 'P001', 'Electronics', 2, 99.99, 'C001'],  
    ['1002', '2023-05-02', 'P002', 'Clothing', 1, 29.95, 'C002'],  
    ['1003', '2023-05-03', 'P003', 'Books', 3, 14.99, 'C001'],  
    ['1004', '2023-05-04', 'P004', 'Electronics', 1, 249.99, 'C003'],  
    ['1005', '2023-05-05', 'P005', 'Clothing', 2, 39.95, 'C002'],  
    ['1006', '2023-05-06', 'P001', 'Electronics', 1, 99.99, 'C004'],  
    ['1007', '2023-05-07', 'P002', 'Clothing', 3, 29.95, 'C001'],  
    ['1008', '2023-05-08', 'P003', 'Books', 2, 14.99, 'C003'],  
    ['1009', '2023-05-09', 'P004', 'Electronics', 1, 249.99, 'C002'],  
    ['1010', '2023-05-10', 'P005', 'Clothing', 1, 39.95, 'C004']  
]  
  
with open('sales_data.csv', 'w', newline='') as file:  
    writer = csv.writer(file)  
    writer.writerow(['order_id', 'order_date', 'product_id', 'product_category', 'quantity', 'unit_price', 'customer_id'])  
    writer.writerows(sales_data)  
  
# Step 2: Storage  
# Data is stored in the 'sales_data.csv' file  
  
# Step 3: Ingestion  
df = pd.read_csv('sales_data.csv')  
print(df.head())  
print(df.info())  
  
# Step 4: Transformation  
# Data cleaning  
df = df.dropna()  
df = df.drop_duplicates()  
  
# Formatting  
df['order_date'] = pd.to_datetime(df['order_date'])  
  
# Feature engineering  
df['total_revenue'] = df['quantity'] * df['unit_price']  
  
# Data manipulation  
grouped = df.groupby('product_category')[['total_revenue', 'quantity']].agg({'total_revenue': 'sum', 'quantity': 'mean'}).reset_index()  
print(grouped)  
  
# Step 5: Serving Data  
plt.figure(figsize=(10, 6))  
sns.barplot(x='product_category', y='total_revenue', data=grouped, palette='viridis')  
plt.xlabel('Product Category')  
plt.ylabel('Total Revenue')  
plt.title('Total Revenue by Product Category')  
plt.show()
```

1. What is the purpose of the csv.writer function in the code?
2. What will be the output of df.head() immediately after the data is ingested?
3. What does the df.dropna() function do in the data transformation step?
4. What is the significance of the df['order\_date'] = pd.to\_datetime(df['order\_date']) line?
5. What will the grouped DataFrame contain after the groupby operation?
6. What will happen if there are duplicate rows in the DataFrame before running the transformation step?
7. Which of the following best describes the data visualization created by the code?
8. What is the purpose of the plt.figure(figsize=(10, 6)) line in the visualization code?
9. If the grouped DataFrame has missing values for some product categories after aggregation, what could be the reason?
10. What would happen if the total\_revenue column was not created before the aggregation step?

### Solution

### [Select for Solution](#dpPanel0)

1. To write data into a CSV file. The csv.writer function is used to write data into a CSV file, as seen in the code where the sales\_data is being written to sales\_data.csv.
2. The first five rows of the sales data from the CSV file. df.head() returns the first five rows of the DataFrame created from the CSV file, which contains the sales data.
3. Drops rows with any missing values. df.dropna() removes rows that contain any missing (NaN) values.
4. It converts the order\_date column from string to datetime format. The pd.to\_datetime function converts the order\_date column from string format to a datetime object, which is essential for date-related operations.
5. The sum of total\_revenue and the mean of quantity for each product category. The code uses groupby to calculate the sum of total\_revenue and the mean of quantity for each product category.
6. The duplicate rows will be automatically removed. The df.drop\_duplicates() function is used specifically to remove any duplicate rows in the DataFrame.
7. A bar chart showing the total revenue for each product category. The code uses sns.barplot to create a bar chart that visualizes total revenue by product category.
8. To set the size of the plot. The figsize parameter sets the dimensions of the plot, in this case, 10 inches wide and 6 inches tall.
9. The dropna() function removed rows with missing values. If there were missing values in the original data, dropna() would have removed those rows, potentially leading to some categories being excluded in the final grouped DataFrame.
10. The grouped DataFrame would only contain the quantity column. If total\_revenue is not created before the groupby operation, the grouped DataFrame would only include the quantity column, as the aggregation function was not applied to total\_revenue.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243917

Scraped At: 2026-05-14T21:21:02.021581
