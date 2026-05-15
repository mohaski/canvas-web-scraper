# Summary: RDDs

# Summary: RDDs

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Summary: RDDs

Icon Progress Bar (browser only)

2 min read

### Terms Recap

* **Resilient Distributed Dataset (RDD):** A fundamental data structure in Spark, enabling distributed processing of large datasets.
* **Resilient:** RDDs have fault tolerance, allowing recovery from node failures by recreating lost data.
* **Distributed:** Data is partitioned across nodes in a cluster for parallel processing.
* **Dataset:** RDDs are immutable collections that can include diverse data types from various sources..

### Key Concepts

RDDs form the backbone of distributed data processing in Spark. They are key for managing big data in a cluster by partitioning data, ensuring fault tolerance, and allowing lazy evaluations to optimize memory and processing.

Understanding transformations (like `map`, `filter`) and actions (like `collect`, `count`) within the context of RDDs allows for efficient data analysis and preparation.

### Brief Process Overview

1. **Initialize Spark and Load Data:** Start Spark and load data into RDDs, distributing it across the cluster.
2. **Partition Data:** Enable parallel processing by splitting data across nodes.
3. **Apply Transformations:** Use transformations to shape and prepare data for analysis.
4. **Trigger Actions:** Execute the transformations through actions to generate final results.
5. **Fault Tolerance and Lineage:** Spark tracks RDD transformations, enabling recovery if a node fails.
6. **Collect and Save Results:** Gather and store processed data and terminate the Spark session to free up resources.

### Resources

For a deeper dive into RDDs and Spark fundamentals, explore [Apache Spark documentation on RDDs


Links to an external site.](https://spark.apache.org/docs/latest/rdd-programming-guide.html) or seek open educational resources that cover distributed data frameworks.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248277

Scraped At: 2026-05-15T09:54:09.534674
