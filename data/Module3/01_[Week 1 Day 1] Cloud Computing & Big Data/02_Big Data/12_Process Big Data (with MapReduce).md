# Process: Big Data (with MapReduce)

# Process: Big Data (with MapReduce)

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Process: Big Data (with MapReduce)

Icon Progress Bar (browser only)

5 min read

MapReduce is a programming model that processes large datasets by splitting data across multiple machines. Each machine performs three key actions:

1. **Map:** The dataset is split into chunks and each chunk is processed to produce key-value pairs.
2. **Shuffle:** All key-value pairs are automatically sorted and grouped by key.
3. **Reduce:** The grouped pairs are processed to aggregate the values for each key into the final output.

![General overview of the 3-step mapreduce process.](https://moringa.instructure.com/courses/1426/files/631371/preview)

Let's look at each of these steps in more detail:

### 1. MAP Task (Splitting & Mapping)

The dataset is first divided into smaller fragments that are distributed across multiple machines for parallel processing. Each computing cluster is assigned several map tasks, which are allocated to individual nodes. The system processes each fragment independently, applying a map function that converts the raw data into key-value pairs.

This transformation enables structured data processing for the subsequent steps. For example, in an animal word count problem, each machine processes lines of text and outputs pairs where the key is each word (animal name) and the value is 1.

1. **Split the dataset** into multiple fragments, distributing them across available nodes.
2. **Apply the map function** to transform raw data into key-value pairs.
3. **Generate key-value pairs** where each word (animal) is a key, and its occurrence count (1) is the value.

#### **Example (Zoo File, below):**

The map function creates key:value pairs represented by - *Animal : # of Animal*

**Input Data:** "Lion Tiger Wolf"

* **Processing on Node 1:** ("Lion", 1), ("Tiger", 1), ("Wolf", 1)
* **Processing on Node 2:** ("Lion", 1), ("Giraffe", 1)
* **Processing on Node 3:** ("Giraffe", 1), ("Penguin", 1)

**Output:**

![Animal word count simple example, splitting and mapping steps](https://moringa.instructure.com/courses/1426/files/631501/download)

#### 2. Shuffling

After the key-value pairs are generated during the Map step, the system automatically sorts and redistributes them across machines based on their keys. This ensures that all values associated with the same key are grouped together on the same machine. By organizing the mapped data into structured groupings, the Shuffle step prepares it for efficient aggregation in the Reduce step.

For example, all occurrences of "Lion" from different nodes are shuffled together so they can be counted in one place. The number of grouped key-value sets corresponds to the number of reduce tasks.

1. **Sort the key-value pairs** by their keys.
2. **Group all occurrences of the same key** so they can be processed together.
3. **Distribute grouped data** to designated machines for the Reduce step.

**Example Output from Zoo File:**

**![Animal word count simple example, shuffling step](https://moringa.instructure.com/courses/1426/files/631474/download)**

#### 3. REDUCE Task (Reducing)

In the Reduce step, each machine processes its assigned group of keys using a reduce function that aggregates the values associated with each key into a final result. The reduce function defines how to summarize or compute the grouped values, such as summing all occurrences of a word. Once reduction is complete, the final aggregated results from all reducers are combined and stored in a distributed file system, typically HDFS (Hadoop Distributed File System).

For example, the reduce function sums up all 1s for "Lion" to get a final count of 3.

1. **Apply the reduce function** to aggregate values for each key.
2. **Compute the final count or summary** for each unique key.
3. **Store the final output** in a distributed file system.

**Output:**

**![Animal word count simple example, Reducing](https://moringa.instructure.com/courses/1426/files/631376/download)**

The **pseudocode** below demonstrates the core logic behind MapReduce operations:

```
# Count word frequency  
def map( doc ) :  
    for word in doc.split( ' ' ) :  
    emit ( word , 1 )  
  
  
def reduce( key , values ) :  
    emit ( key , sum( values ) )
```

* The **map function** breaks down a document into words and assigns each word a count of 1.
* The **reduce function** sums all the counts for each word, providing the total word frequency across the dataset.

### Best Practices for Using MapReduce

#### **Use MapReduce for Large Datasets:**

It's important to note that MapReduce will generally only be powerful when dealing with large amounts of data. When working with a small dataset, it will be faster not to perform operations in the MapReduce framework.

#### **Understand the Roles of Job Tracker & Task Tracker:**

There are two groups of entities involved in this process that ensure MapReduce tasks get done properly:

* **Job Tracker:** a "master" node that informs the other nodes which map and reduce jobs to complete
* **Task Tracker:** the "worker" nodes that complete the map and reduce operations

Depending on the technology used, these roles may have different names, but there will always be a master node that informs worker nodes what tasks to perform.

#### **Chaining Multiple MapReduce Jobs:**

We can consider combining multiple MapReduce jobs in order to complete a more complex task. This means that once the **first MapReduce job** is finished, the output will become an input for the **second MapReduce job** and that **output** could be the final result (or fed into another MapReduce job).

**Example:** Let's assume that we would like to extend the word count program and we would like to count all words in a given Twitter dataset. The **first MapReduce** will read our twitter data and extract the tweets' text. The **second MapReduce** is the word count Map-Reduce which will analyze the Twitter dataset and produce the statistics about it. So it is simply chaining together multiple jobs.

**InputFile -> Map-1 -> Reduce-1 -> Output-1 -> Map-2 - > Reduce-2 -> Output-2 -> ... Map-x -> Reduce-x**

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248205

Scraped At: 2026-05-15T09:49:20.657516
