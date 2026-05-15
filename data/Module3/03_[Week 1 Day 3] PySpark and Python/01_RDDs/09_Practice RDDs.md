# Practice: RDDs

# Practice: RDDs

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Practice: RDDs

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

You’re a data analyst at a major transportation logistics company, TransLogic, which handles the delivery of goods across the country. TransLogic collects data from hundreds of sensors on each truck, capturing details like speed, fuel efficiency, and engine temperature. Your team needs to process and analyze this sensor data to improve fuel efficiency and reduce maintenance costs. Using RDDs in PySpark, your goal is to clean and transform this raw data to identify patterns and provide actionable insights.

**Problem-Solving Process:** This scenario uses a process similar to previous examples, focusing on cleaning, transforming, and summarizing large datasets. Key steps include:

1. Initializing and partitioning RDDs
2. Applying transformations and actions
3. Filtering and selecting data
4. Summarizing results

This practice should help you to gain experience with the essential steps in setting up, partitioning, and analyzing data with RDDs.

### Instructions

### Step 1: Initialize the Spark Context

Start by setting up the Spark context and creating RDDs. You’ll use simulated data for simplicity, but keep in mind how this applies to real sensor data.

### Step 2: Load and Partition Data

Use `.parallelize()` to create an RDD from a sample list of data that represents sensor readings (i.e., speed, temperature, fuel consumption). Partition the data for efficient parallel processing. Use three slices for the RDD and use the following for your data:

```
# Sample data representing speed, engine temperature in Celsius, and fuel efficiency (mpg)  
sensor_data = [  
    [60, 75, 7.5], [70, 80, 8.2], [65, 77, 7.8], [80, 90, 6.9],  
    [50, 68, 9.1], [75, 88, 7.0], [62, 74, 7.7], [78, 85, 6.8]  
]
```

### Step 3: Apply Transformations

* Use transformations like `map()` to adjust or filter data values (i.e., convert temperature readings from Celsius to Fahrenheit).
* Use `filter()` to retain only readings with certain conditions (i.e, speed over a threshold).   
  In particular,

```
# Convert temperature to Fahrenheit and filter by speed > 65 MPH
```

### Step 4: Trigger Actions

Apply the action `collect()` to execute transformations and summarize data results.

### Step 5: Aggregate Data

Use reduce() to calculate the average fuel efficiency of trucks going over 65 mph.

### Solution

#### Select for Solution

```
# Step 1: Initialize the Spark Context  
import pyspark  
sc = pyspark.SparkContext('local[*]', 'TransLogic RDD Analysis')  
  
# Step 2: Load and Partition Data  
# Sample data representing [speed, temperature in Celsius, fuel efficiency in MPG]  
sensor_data = [  
    [60, 75, 7.5], [70, 80, 8.2], [65, 77, 7.8], [80, 90, 6.9],  
    [50, 68, 9.1], [75, 88, 7.0], [62, 74, 7.7], [78, 85, 6.8]  
]  
rdd = sc.parallelize(sensor_data, numSlices=3)  
  
# Step 3: Apply Transformations  
# Convert temperature to Fahrenheit and filter by speed > 65 MPH  
def celsius_to_fahrenheit(temp):  
    return (temp * 9/5) + 32  
  
rdd_converted = rdd.map(lambda x: [x[0], celsius_to_fahrenheit(x[1]), x[2]])  
filtered_rdd = rdd_converted.filter(lambda x: x[0] > 65)  
  
# Step 4: Trigger Actions  
# Take a sample of the data to verify transformations  
sample_data = filtered_rdd.take(3)  
print("Sample Data After Transformations:", sample_data)  
  
# Step 5: Aggregate Data  
# Calculate total fuel efficiency using reduce  
total_fuel_efficiency = filtered_rdd.map(lambda x: x[2]).reduce(lambda x, y: x + y)  
average_fuel_efficiency = total_fuel_efficiency / filtered_rdd.count()  
print("Average Fuel Efficiency of Trucks Going Over 65 MPH:", average_fuel_efficiency)  
  
# Step 6: Stop the Spark Context  
sc.stop()  
  
 
```

**Expected Output:**

```
Data After Transformations: [[70, 176.0, 8.2], [80, 194.0, 6.9], [75, 190.4, 7.0], [78, 185.0, 6.8]]  
Average Fuel Efficiency of Trucks Speeding Over 65 MPH: 7.225
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248281

Scraped At: 2026-05-15T09:54:26.546080
