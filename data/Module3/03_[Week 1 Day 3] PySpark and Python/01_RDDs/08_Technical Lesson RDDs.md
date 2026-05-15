# Technical Lesson: RDDs

# Technical Lesson: RDDs

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: RDDs

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In Spark, we first create a base RDD and then apply one or more transformations to that base RDD following our processing needs. Being immutable means, once an RDD is created, it cannot be changed. As a result, each transformation of an RDD creates a new RDD. Finally, we can apply one or more actions to the RDDs. Spark uses lazy evaluation, so transformations are not actually executed until an action occurs.

![RDD Flowchart with Create RDD, Transformation, RDD Lineage, Action, and Result steps.](https://moringa.instructure.com/courses/1426/files/631482/download)

### Transformations

Transformations create a new dataset from an existing one by passing each dataset element through a function and returning a new RDD representing the results. In short, creating an RDD from an existing RDD is ‘transformation’. All transformations in Spark are lazy. They do not compute their results right away.

Instead, they just remember the transformations applied to some base dataset (e.g. a file). The transformations are only computed when an action requires a result that needs to be returned to the driver program. A transformation is an RDD that returns another RDD, like map, flatMap, filter, reduceByKey, join, cogroup, etc.

### Actions

Actions return final results of RDD computations. Actions trigger execution using lineage graph to load the data into original RDD and carry out all intermediate transformations and return the final results to the driver program or writes it out to the file system. An action returns a value (to a Spark driver - the user program).

Here are some key transformations and actions that we will explore.

RDD Transformations & Actions

| Transformations | Actions |
| --- | --- |
| map(func) | reduce(func) |
| filter(func) | collect() |
| groupByKey() | count() |
| reduceByKey(func) | first() |
| mapValues(func) | take() |
| sample() | countByKey() |
| distinct() | foreach(func) |
| sortByKey() |  |

Let's see how transformations and actions work through a simple example. In this lesson, we will perform several actions and transformations on RDDs in order to obtain a better understanding of Spark processing.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of RDDs.

[VIDEO LINK](https://player.vimeo.com/video/1058081192?badge=0&autopause=0&player\_id=0&app\_id=58479)

### Instructions

### Step 1. Create a Python Collection

We need some data to start experimenting with RDDs. Let's create some sample data and see how RDDs handle it. To practice working with RDDs, we're going to use a simple Python list.

* Create a Python list data of integers between 1 and 1000 using the range() function.
* Sanity check: confirm the length of the list (it should be 1000)

```
data = list(range(1,1001))  
len(data)
```

**Output:**

```
1000
```

### Step 2. Initialize a RDD

When using Spark to make computations, **datasets are treated as lists of entries**. Those lists are split into different partitions across different cores or different computers. Each list of data held in memory is a partition of the RDD.

The reason why **Spark is able to make computations far faster than other big data processing languages is that it allows all data to be stored in-memory**, which allows for easy access to the data and, in turn, high-speed processing.

Here is an example of how the alphabet might be split into different RDDs and held across a distributed collection of nodes:

![Diagram of initializing an RDD.](https://moringa.instructure.com/courses/1426/files/631373/download)

**To initialize an RDD**, we first import pyspark and then create a SparkContext assigned to the variable sc. Use 'local[\*]' as the master.

```
import pyspark  
sc = pyspark.SparkContext('local[*]', 'RDD practice')  
rdd = sc.parallelize(data) # Create RDD
```

**Output:**

```
<class 'pyspark.rdd.RDD'>
```

**Determine how many partitions are being used** with this RDD with the .getNumPartitions() method.

```
rdd.getNumPartitions()
```

* The number of partitions may be different each time `.getNumPartitions()` is run."

**Output:**

```
10
```

### Step 3. Basic Descriptive RDD Actions

Let's perform some basic operations on our RDD. In the cell below, use the methods:

* **count:** returns the total count of items in the RDD
* **first:** returns the first item in the RDD
* **take:** returns the first n items in the RDD
* **top:** returns the top n items
* **collect:** returns everything from your RDD

It's important to note that in a big data context, calling the collect method will often take a very long time to execute and should be handled with care.

```
rdd.count()
```

**Output:**

```
1000
```

```
rdd.first()
```

**Output:**

```
1
```

```
rdd.take(10)
```

**Output:**

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```
rdd.top(10)
```

**Output:**

```
[1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]
```

```
## Note: When you are dealing with big data, this could make your computer crash! It's best to avoid using the collect() method  
rdd.collect()
```

**Output:**

```
[1,  
 2,  
 3,  
 4,  
 5,  
 6,  
 7,  
 8,  
 9,  
 10,  
 11,  
 12,  
 13,  
 14,  
 15,  
 16,  
 17,  
 18,  
 19,  
 20,  
 ...  
 997,  
 998,  
 999,  
 1000]
```

### Step 4. Map Functions

Now that you've been working a little bit with RDDs, let's make this a little more interesting. Imagine you're running a hot new e-commerce startup called BuyStuff, and you're trying to keep track of how much it charges customers from each item sold.

In the next cell, we're going to **create simulated data** by multiplying the values 1-1000 with a random number from 0-1.

```
import numpy as np  
  
np.random.seed(1)  
nums = np.array(range(1, 1001))  
sales_figures = nums * np.random.rand(1000)  
sales_figures
```

**Output:**

```
array([4.17022005e-01, 1.44064899e+00, 3.43124452e-04, 1.20933029e+00,  
       7.33779454e-01, 5.54031569e-01, 1.30382148e+00, 2.76448582e+00,  
       3.57090727e+00, 5.38816734e+00, 4.61113966e+00, 8.22263400e+00,  
       2.65787925e+00, 1.22936441e+01, 4.10813898e-01, 1.07274802e+01,  
       7.09418164e+00, 1.00564169e+01, 2.66735183e+00, 3.96202978e+00,  
       1.68156359e+01, 2.13017547e+01, 7.20875610e+00, 1.66157428e+01,  
       2.19097288e+01, 2.32597733e+01, 2.29619371e+00, 1.09353393e+00,  
       4.92508217e+00, 2.63442751e+01, 3.04875185e+00, 1.34754440e+01,  
       3.16103545e+01, 1.81276197e+01, 2.42156990e+01, 1.13585627e+01,  
       2.54005343e+01, 3.17157755e+01, 7.13242816e-01, 3.00057726e+01,  
       4.05433046e+01, 3.14229575e+01, 1.20590917e+01, 3.47282905e+01,  
       4.64517030e+00, 2.06031022e+01, 4.27039886e+01, 1.40934791e+01,  
       1.41009916e+01, 6.50142861e+00, 9.87714851e-01, 3.52994477e+01,  
       1.12162901e+01, 1.43395196e+01, 2.70365238e+01, 2.98830253e+00,  
       3.27247035e+01, 8.51025734e+00, 3.47690267e+01, 4.19855016e+01,  
       6.24240016e+00, 2.56714712e+01, 4.37472099e+01, 2.65074732e+01,  
       3.24697483e+00, 3.53691628e+01, 4.44742412e+01, 3.50124596e+01,  
       6.51770382e+01, 4.10588528e+01, 6.41415360e+01, 9.89817870e+00,  
       1.01671733e+01, 5.97469554e+01, 2.98257628e+01, 1.25669190e+01,  
       7.14181607e+01, 2.71257371e+01, 5.93141561e+01, 5.80798388e+01,  
       7.15477934e+01, 5.11411210e+01, 6.23282220e+01, 2.93074607e+01,  
       2.29438708e+01, 7.70462148e+01, 3.72439335e+01, 8.49059241e+01,  
       ...  
       9.08197248e+02, 4.74878012e+02, 5.23999286e+02, 8.70193075e+02,  
       4.34575900e+02, 8.54231495e+02, 2.47242206e+02, 2.67238271e+02,  
       3.20809078e+02, 5.35517857e+02, 2.15505972e+02, 6.58000588e+02,  
       1.40080210e+02, 9.24064696e+01, 8.55398487e+02, 2.33078804e+02,  
       3.80213951e+02, 5.63540503e+02, 5.18966544e+02, 7.51115929e+01,  
       8.64510550e+02, 9.41624262e+02, 8.05194738e+02, 2.81531420e+02,  
       5.24151869e+02, 3.37380224e+02, 5.51893974e+02, 9.70505855e+02,  
       3.10767809e+02, 6.67459013e+02, 3.25641240e+02, 7.74477266e+02])
```

We now have sales prices for 1000 items currently for sale at BuyStuff. Now **create an RDD called price\_items** using the newly created data Set the numSlices argument to equal 10 slices, this will create 10 partitions in your new RDD. After you create it, use one of the basic actions to see what's in the RDD.

```
price_items = sc.parallelize(sales_figures, numSlices=10)  
price_items.take(4)
```

**Output:**

```
[0.417022004702574,  
 1.4406489868843162,  
 0.0003431244520346599,  
 1.209330290527359]
```

Now let's perform some operations on this simple dataset. To begin with, we'll **create a function that will take into account how much money BuyStuff will receive after sales tax has been applied**. Assume a sales tax of 8%, i.e. that the current price data is actually 108% of what it should be.

To make this happen, we create a function called sales\_tax() that returns the amount of money our company will receive after the sales tax has been applied. The function will have this parameter:

* **num:** (float) number to be multiplied by the sales tax.

**Apply that function to the RDD** by using the .map() method and assign it to a variable renenue\_minus\_tax

```
def sales_tax(num):  
    return num / 1.08  
  
revenue_minus_tax = price_items.map(sales_tax)
```

Remember, Spark has lazy evaluation, which means that the sales\_tax() function is a transformer that is not executed until we call an action. **Use one of the collection methods to execute the transformer now a part of the RDD** and observe the contents of the revenue\_minus\_tax RDD.

```
revenue_minus_tax.take(10)
```

**Output:**

```
[0.38613148583571666,  
 1.3339342471151074,  
 0.0003177078259580184,  
 1.119750269006814,  
 0.6794254204495974,  
 0.5129921931599878,  
 1.2072421107812004,  
 2.559709089207761,  
 3.306395618588916,  
 4.989043833364416]
```

### Step 5. Lambda Functions

Note that we can also use lambda functions if we want to quickly perform simple operations on data without creating a function. Let's assume that BuyStuff has also decided to offer a 10% discount on all of their items on the pre-tax amounts of each item. **Use a lambda function within a .map() method to apply the additional 10% loss in revenue** for BuyStuff and assign the transformed RDD to a new RDD called discounted.

```
discounted = revenue_minus_tax.map(lambda x : x*0.9)
```

```
discounted.take(10)
```

**Output:**

```
[0.347518337252145,  
 1.2005408224035967,  
 0.0002859370433622166,  
 1.0077752421061326,  
 0.6114828784046377,  
 0.461692973843989,  
 1.0865178997030804,  
 2.303738180286985,  
 2.9757560567300243,  
 4.490139450027975]
```

### Step 6. Chaining Methods

We are also able to chain methods together with Spark. **In one line, remove the tax and discount from the revenue of BuyStuff and use a collection method** to see the 15 costliest items.

```
price_items.map(sales_tax).map(lambda x : x*0.9).top(15)
```

**Output:**

```
[808.7548791977921,  
 795.5962541991298,  
 784.6868851954209,  
 756.8310401687224,  
 753.4277907153834,  
 752.0937136346447,  
 747.1368663633596,  
 737.66773326942,  
 730.5313349924388,  
 725.1608962422889,  
 720.4254585887082,  
 718.7262188305615,  
 716.2342491392883,  
 712.8320720999051,  
 711.8595792911022]
```

### Step 7 RDD Lineage

**We are able to see the full lineage of all the operations that have been performed on an RDD by using the RDD.toDebugString() method**. As your transformations become more complex, you are encouraged to call this method to get a better understanding of the dependencies between RDDs. Try calling it on the discounted RDD to see what RDDs it is dependent on.

```
discounted.toDebugString()
```

**Output:**

```
b'(10) PythonRDD[10] at RDD at PythonRDD.scala:53 []\n |     
ParallelCollectionRDD[5] at readRDDFromFile at PythonRDD.scala:274 []'
```

### Step 8. Map vs. Flatmap

**Depending on how we want our data to be outputted, we might want to use .flatMap() rather than a simple .map().** Let's take a look at how it performs operations versus the standard map.

Let's say we wanted to maintain the original amount BuyStuff receives for each item as well as the new amount after the tax and discount are applied. Create a map function that will return a tuple with (original price, post-discount price).

```
mapped = price_items.map(lambda x: (x, x / 1.08 * 0.9))  
print(mapped.count())  
print(mapped.take(10))
```

**Output:**

```
1000  
[(0.417022004702574, 0.347518337252145), (1.4406489868843162, 1.2005408224035967), (0.0003431244520346599, 0.0002859370433622166), (1.209330290527359, 1.0077752421061326), (0.7337794540855652, 0.6114828784046377), (0.5540315686127868, 0.461692973843989), (1.3038214796436964, 1.0865178997030804), (2.764485816344382, 2.303738180286985), (3.5709072680760294, 2.9757560567300243), (5.3881673400335695, 4.490139450027975)]
```

Note that we have 1000 tuples created to our specification. Let's take a look at how .flatMap() differs in its implementation. **Use the .flatMap() method with the same function you created above.**

```
flat_mapped = price_items.flatMap(lambda x : (x, x / 1.08 * 0.9 ))  
print(flat_mapped.count())  
print(flat_mapped.take(10))
```

**Output:**

```
2000  
[0.417022004702574, 0.347518337252145, 1.4406489868843162, 1.2005408224035967, 0.0003431244520346599, 0.0002859370433622166, 1.209330290527359, 1.0077752421061326, 0.7337794540855652, 0.6114828784046377]
```

Rather than being represented by tuples, all of the values are now on the same level.

**Note:** When we are trying to combine different items together, it is sometimes necessary to use .flatMap() rather than .map() in order to properly reduce to our specifications. This is not one of those instances, but in the upcoming lab, you just might have to use it.

### Step 9. Filter

After meeting with some external consultants, BuyStuff has determined that its business will be more profitable if it focuses on higher ticket items. Now, **use the .filter() method to select items that bring in more than $300 after tax and discount have been removed.** A filter method is a specialized form of a map function that only returns the items that match a certain criterion.

In the cell below:

* we use a lambda function within a .filter() method to meet the consultant's suggestion's specifications. set RDD = selected\_items
* calculate the total number of items remaining in BuyStuff's inventory

```
selected_items = discounted.filter(lambda x: x > 300)  
selected_items.count()
```

**Output:**

```
272
```

### Step 10. Reduce

Reduce functions are where you are in some way combining all of the variables that you have mapped out. Here is an example of **how a reduce function works when the task is to sum all values**:

![Diagram of Partition 1 and Partition 2 reducing the number of variables.](https://moringa.instructure.com/courses/1426/files/631434/download)

As you can see, the operation is performed within each partition first, after which, the results of the computations in each partition are combined to come up with one final answer.

Now it's time to figure out how much money BuyStuff would make from selling one of all of its items after they've reduced their inventory. **Use the .reduce() method with a lambda function to add up all of the values in the RDD.** Your lambda function should have two variables.

```
selected_items.reduce(lambda x, y: x + y)
```

**Output:**

```
123432.4660522227
```

The time has come for BuyStuff to open up shop and start selling its goods. It only has one of each item, but it's allowing 50 lucky users to buy as many items as they want while they remain in stock. Within seconds, BuyStuff is sold out.

Below, you'll find the sales data in an RDD with tuples of (user, item bought).

```
import random  
random.seed(42)  
# generating simulated users that have bought each item  
sales_data = selected_items.map(lambda x: (random.randint(1, 50), x))  
  
sales_data.take(7)
```

**Output:**

```
[(8, 303.9717333600381),  
 (36, 315.8957533626659),  
 (29, 320.6109689548023),  
 (18, 320.58739183867544),  
 (48, 329.4565433918027),  
 (36, 352.7343621192842),  
 (4, 336.5077558595325)]
```

It's time to determine some basic statistics about BuyStuff users. Let's start off by creating an RDD that determines how much each user spent in total.

To do this we can **use a method called .reduceByKey()** to perform reducing operations while grouping by keys.

**After we have calculated the total,** we'll use the .sortBy() method on the RDD to rank the users from the highest spending to the least spending.

```
total_spent = sales_data.reduceByKey(lambda x, y: x + y)  
total_spent.take(10)
```

**Output:**

```
[(10, 2505.4128261985734),  
 (30, 3382.449750500504),  
 (20, 2162.532818544579),  
 (40, 2733.835414659196),  
 (50, 1009.1271615645499),  
 (41, 2288.6328380275563),  
 (21, 1511.275378505312),  
 (1, 2752.542147304854),  
 (31, 3056.504120650862),  
 (11, 1511.8044372912896)]
```

```
total_spent.sortBy(lambda x: x[1], ascending = False).collect()
```

**Output:**

```
[(37, 6058.32282961381),  
 (35, 5147.3165498027965),  
 (14, 4718.853598241101),  
 (3, 4577.11556237689),  
 (32, 3661.5914194018924),  
 (39, 3590.199456355873),  
 (34, 3584.8861644479093),  
 (4, 3450.7117495281045),  
 (30, 3382.449750500504),  
 (42, 3314.794549097422),  
 (19, 3258.7620596071074),  
 (22, 3200.1246013611844),  
 (31, 3056.504120650862),  
 (36, 3053.623359721479),  
 (45, 3010.218962331668),  
 (8, 2912.0427078664316),  
 (46, 2837.3218299486853),  
 (44, 2832.057231700557),  
 (1, 2752.542147304854),  
 (40, 2733.835414659196),  
 (13, 2699.181298186921),  
 (26, 2663.0870131901474),  
 (2, 2634.2461944306783),  
 (10, 2505.4128261985734),  
 (17, 2474.19078593852),  
 (12, 2380.99877057044),  
 (41, 2288.6328380275563),  
 (29, 2271.601948461445),  
 (49, 2206.520353564143),  
 (20, 2162.532818544579),  
 (16, 2070.5342988892085),  
 (5, 1988.2251520732625),  
 (24, 1926.9060030801184),  
 (33, 1899.7417139575373),  
 (48, 1717.7722170913798),  
 (43, 1653.3750643830203),  
 (28, 1639.9325449739288),  
 (23, 1593.6702466360014),  
 (11, 1511.8044372912896),  
 (21, 1511.275378505312),  
 (15, 1497.4823720659315),  
 (18, 1472.6619623487884),  
 (47, 1451.1062895771497),  
 (6, 1413.623445906109),  
 (25, 1097.048421376119),  
 (50, 1009.1271615645499),  
 (7, 905.4233605392121),  
 (38, 837.0751484844222),  
 (9, 816.0019218480354)]
```

Next, let's **determine how many items were bought per user**. This can be solved in one line using an RDD method. After you've counted the total number of items bought per person, sort the users from most number of items bought to least number of items. Time to start a customer loyalty program.

```
sorted(sales_data.countByKey().items(), key=lambda kv:kv[1], reverse=True)
```

**Output:**

```
[(49, 11),  
 (22, 11),  
 (11, 10),  
 (23, 10),  
 (28, 9),  
 (13, 8),  
 (38, 8),  
 (44, 8),  
 (18, 8),  
 (35, 8),  
 (48, 8),  
 (2, 7),  
 (43, 7),  
 (46, 7),  
 (37, 7),  
 (20, 7),  
 (32, 7),  
 (47, 7),  
 (17, 7),  
 (8, 6),  
 (40, 6),  
 (16, 5),  
 (4, 5),  
 (33, 5),  
 (6, 5),  
 (26, 5),  
 (34, 5),  
 (5, 5),  
 (36, 5),  
 (30, 4),  
 (24, 4),  
 (42, 4),  
 (9, 4),  
 (31, 4),  
 (19, 4),  
 (27, 4),  
 (25, 4),  
 (21, 3),  
 (10, 3),  
 (50, 3),  
 (41, 3),  
 (3, 3),  
 (7, 3),  
 (29, 3),  
 (14, 2),  
 (1, 2),  
 (45, 2),  
 (12, 2),  
 (39, 2),  
 (15, 2)]
```

### Step 11. Stop the SparkContext

Now that we are finished with our analysis, stop the sc.

```
sc.stop()
```

### Considerations

1. **Fault Tolerance and Resilience**  
   * **Challenge:** While RDDs are fault-tolerant, the initial setup for distributed systems can be complex for beginners, especially when dealing with large-scale systems.
   * **Consideration:** Learners should focus on the concept of “resilience” within Spark to understand the value of RDDs in preserving data across nodes.
   * **Pros:** Built-in fault tolerance is a significant advantage, allowing Spark to handle node failures without data loss.
   * **Cons:** Initial configuration of nodes for optimal fault tolerance can require extensive setup.
2. **Immutable and Lazy Evaluation**  
   * **Challenge:** RDDs are immutable, meaning any transformation creates a new RDD. Lazy evaluation means transformations aren’t executed until an action is called, which can be confusing at first.
   * **Consideration:** Emphasize the value of lazy evaluation for efficiency; only the necessary computations are carried out, minimizing resource usage.
   * **Pros:** Lazy evaluation allows learners to avoid unnecessary computation, saving memory and processing time.
   * **Cons:** Debugging can be challenging since transformations only execute when an action is triggered, making it harder to track errors early.
3. **Partitioning and Parallel Processing**  
   * **Challenge:** Setting the correct number of partitions for an RDD can impact performance. Too few partitions can underutilize resources, while too many can lead to overhead.
   * **Consideration:** Learners should experiment with different partition settings to understand the effect on performance and processing speed.
   * **Pros:** Optimizing partitions can drastically improve processing efficiency and speed.
   * **Cons:** Without proper configuration, learners may encounter bottlenecks that reduce Spark’s processing advantages.
4. **Actions vs. Transformations**  
   * **Challenge:** Differentiating between actions and transformations is essential since actions trigger execution while transformations do not.
   * **Consideration:** Introduce learners to common actions (e.g., collect, count) and transformations (map, filter) early, so they can experiment and see how each affects data processing.
   * **Pros:** Understanding these two types of operations can help learners structure workflows for optimized performance.
   * **Cons:** Confusion between the two can lead to unintended results and performance issues, especially if too many actions are called without need.
5. **In-Memory Data Processing**  
   * **Challenge:** While RDDs allow for in-memory processing, large datasets can still exceed memory, leading to performance slowdowns or failures.
   * **Consideration:** Encourage learners to use the persist and cache methods to retain RDDs in memory when necessary but also to be cautious about memory limits.
   * **Pros:** In-memory processing is fast and ideal for iterative tasks like machine learning.
   * **Cons:** Mismanagement of memory can quickly lead to system crashes, especially when working with very large datasets.
6. **Trade-offs Between Map and FlatMap**  
   * **Challenge:** Choosing between map and flatMap can be confusing when learners need to decide how data should be outputted.
   * **Consideration:** Practical examples can illustrate when flatMap is necessary for tasks like tokenizing text or generating new records from existing ones.
   * **Pros:** flatMap can provide flexibility when dealing with nested data structures or when transformations yield multiple records.
   * **Cons:** Overuse of flatMap can complicate RDD transformations and increase processing requirements.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248280

Scraped At: 2026-05-15T09:54:21.342443
