# Practice: SparkContext

# Practice: SparkContext

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Practice: SparkContext

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

Imagine you’re a junior data engineer at a healthcare analytics company. You’ve been tasked with analyzing large volumes of patient visit data across hospitals to identify trends in diagnosis and treatment patterns. This dataset is extensive, containing information from numerous locations and providers, so processing it on a single machine is impractical. Here’s where SparkContext in PySpark becomes invaluable.

In this scenario, your goal is to set up a SparkContext that allows you to work with distributed datasets, manage resources effectively, and perform parallel computations across available machine cores. This exercise aligns directly with the skills introduced in this lesson, providing hands-on experience in setting up and configuring SparkContext.

### **Challenge**

The main challenge is to configure and utilize SparkContext to load, manage, and process large datasets efficiently. Specifically, you’ll explore key attributes and configurations within SparkContext, such as adjusting application settings, checking resource availability, and optimizing task distribution. These steps are foundational for working on large datasets in a production environment, where efficiency and accuracy are critical.

This exercise is designed to simulate a real-world data engineering challenge in the healthcare industry, helping you build foundational skills in distributed data processing with SparkContext.

### Instructions

#### Step 1

* Import the necessary modules: SparkConf and SparkContext from PySpark, and os for environment variable manipulation.
* If you are missing any libraries you need to (possibly) ! pip install, e.g. ‘! pip install findspark`

**Note:** Java needs to be installed in order to pip install pyspark, details can be found [here on the PySpark documentation page


Links to an external site.](https://spark.apache.org/docs/latest/api/python/getting_started/install.html).

#### Step 2

* Set the JAVA\_HOME environment variable, which is required for Spark to run.
* Replace /path/to/your/java/home with your actual Java installation path.

#### Step 3

* Create a SparkConf object, setting the application name to "SparkContextDemo" and the master URL to "local[\*]", which means Spark will run locally using all available cores.

#### Step 4

* Create a SparkContext using the configuration we just set up.

#### Step 5

* Use the various attributes and settings of SparkContext to learn more about the SparkContext:

* + appName: The name of the Spark application
  + master: The URL of the cluster manager
  + getConf().getAll(): All configuration parameters
  + defaultParallelism: Default number of partitions in RDDs
  + defaultMinPartitions: Default minimum number of partitions for RDDs
  + sparkHome: The directory where Spark is installed
  + sparkUser(): The user running the Spark application
  + version: Spark version
  + pythonVer: Python version used
  + statusTracker = sc.statusTracker()

    active\_jobs = statusTracker.getActiveJobsIds()

    : The tracker for job progress
  + \_jsc.getPersistentRDDs(): List of registered RDDs
  + \_jsc.sc().resources(): Available resources for the Spark application

#### Step 6

* Modify the log level using setLogLevel() and retrieve it with getLogLevel().

#### Step 7

* Create a simple RDD using parallelize(), perform an action (sum()), and print the result to show that the SparkContext is working correctly.

#### Step 8

* Stop the SparkContext to release the resource.

### Solution

### Select for Solution

#### Steps 1-4

```
import os  
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64' # Replace with your Java installation path  
  
import findspark  
from pyspark import SparkConf, SparkContext  
from py4j.protocol import Py4JError # Import the Py4JError exception class  
  
# Initialize findspark to add PySpark to the system path  
findspark.init()  
  
  
# Create a SparkConf object  
conf = SparkConf().setAppName("SparkContextDemo").setMaster("local[*]")  
  
  
# Create a SparkContext  
sc = SparkContext(conf=conf)
```

  

#### Steps 5-7

```
# Demonstrate various SparkContext attributes and settings  
  
  
# Application Name  
print("Application Name:", sc.appName)  
  
  
# Master URL  
print("Master URL:", sc.master)  
  
  
# SparkConf  
print("SparkConf:", sc.getConf().getAll())  
  
  
# Default Parallelism  
print("Default Parallelism:", sc.defaultParallelism)  
  
  
# Default Minimum Partitions  
print("Default Minimum Partitions:", sc.defaultMinPartitions)  
  
  
# Spark Home  
print("Spark Home:", sc.sparkHome)  
  
  
# Spark User  
print("Spark User:", sc.sparkUser())  
  
  
# Spark Version  
print("Spark Version:", sc.version)  
  
  
# Python Version  
print("Python Version:", sc.pythonVer)  
  
statusTracker = sc.statusTracker()  
active_jobs = statusTracker.getActiveJobsIds()  
print("Active Job IDs:", active_jobs)  
  
# List of Registered RDDs  
print("Registered RDDs:", sc._jsc.getPersistentRDDs())  
  
  
# Available Resources  
print("Available Resources:", sc._jsc.sc().resources())  
  
  
# Modify Log Level  
sc.setLogLevel("WARN")  
  
  
# Instead of using sc.getLogLevel(), you can access the log level from SparkConf:  
log_level = sc.getConf().get("spark.logConf")  
print("Current Log Level:", log_level)  
  
  
# Alternatively, you can check the current log level using the following approach:  
# import logging  
# log_level = logging.getLogger("py4j").getEffectiveLevel()  
# print("Current Log Level:", logging.getLevelName(log_level))  
  
  
# Create a simple RDD and perform an action  
rdd = sc.parallelize(range(10))  
sum_result = rdd.sum()  
print("Sum of RDD:", sum_result)
```

**Note**: In the output below the `SparkConf` line has been truncated, which is denoted by the ellipses.

**Expected Output:**

```
Application Name: SparkContextDemo  
Master URL: local[*]  
SparkConf: [('spark.driver.extraJavaOptions', ...  
Default Parallelism: 2  
Default Minimum Partitions: 2  
Spark Home: None  
Spark User: root  
Spark Version: 3.5.3  
Python Version: 3.10  
Registered RDDs: {}  
Available Resources: Map()  
Current Log Level: None  
Sum of RDD: 45
```

#### Step 8

```
# Stop the SparkContext  
sc.stop()
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248255

Scraped At: 2026-05-15T09:52:25.385143
