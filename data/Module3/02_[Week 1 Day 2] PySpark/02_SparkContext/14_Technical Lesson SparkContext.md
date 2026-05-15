# Technical Lesson: SparkContext

# Technical Lesson: SparkContext

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: SparkContext

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

In this lesson, you’ll learn how to create and interact with a SparkContext object, which is essential for managing Spark applications in PySpark. SparkContext acts as the primary connection between your code (driver program) and the Spark environment, enabling you to leverage distributed computing capabilities by instantiating SparkContext, accessing SparkContext attributes and methods, investigating SparkContext properties, and shutting down the SparkContext.

This process ensures efficient resource management and provides foundational insights into Spark’s distributed processing, helping you use SparkContext to initiate, configure, and monitor your Spark applications effectively.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of SparkContext.

[VIDEO LINK](https://player.vimeo.com/video/1038329397?h=c107531713)

### Instructions

* [Step 1. Instantiate SparkContext](#dpPanel0Content)
* [Step 2. Access SparkContext Attributes and Methods](#dpPanel1Content)
* [Step 3. Investigate SparkContext Properties](#dpPanel2Content)
* [Step 4. Shut Down SparkContext](#dpPanel3Content)

#### Step 1. Instantiate SparkContext

**Note:** When you "pip install PySpark", you will need to Java installed, which is discussed in the following practice.

In the cell below, we instantiate a variable sc using the SparkContext class, a master of "`local[*]`", and an appName of "`sc practice`".

```
# Install the pyspark package using pip  
  
# !pip install pyspark  
  
# Import the SparkContext class from the pyspark module  
  
from pyspark import SparkContext  
  
# Instantiate sc  
  
sc = SparkContext("local[*]", "sc practice")
```

Some Java warnings may appear below this line of code (or other lines of code). In general you can safely ignore these warnings, although they may provide relevant information for debugging.

##### One SparkContext at a Time

Note that you can only have one SparkContext at a time. If you try to make another one without stopping the first one, you will get an error:

```
# Bad idea - creating a second SparkContext  
try:  
    another_sc = SparkContext("local[*]", "double trouble")  
except Exception as e:  
    print(type(e))  
    print(e)
```

#### Step 2. Access SparkContext Attributes and Methods

Now we have a SparkContext object Let's investigate it like any other Python object.

##### Type

What is the type of our SparkContext?

```
# Type of sc  
print(type(sc))
```

**Output:**

```
pyspark.context.SparkContext
```

##### All Attributes

We'll use Python's dir built-in function ([documentation here


Links to an external site.](https://docs.python.org/3/library/functions.html#dir)) to get a list of all attributes (including methods) accessible through the sc object.

```
# Get a list of all attributes  
dir(sc)
```

**Output:**

```
# Get a list of all attributes  
['PACKAGE_EXTENSIONS',  
 '__class__',  
 '__delattr__',  
 '__dict__',  
 '__dir__',  
 '__doc__',  
 '__enter__',  
 '__eq__',  
 '__exit__',  
 '__format__',  
 '__ge__',  
 '__getattribute__',  
 '__getnewargs__',  
 '__gt__',  
 '__hash__',  
 '__init__',  
 '__init_subclass__',  
 '__le__',  
 '__lt__',  
 '__module__',  
 '__ne__',  
 '__new__',  
 '__reduce__',  
 '__reduce_ex__',  
 '__repr__',  
 '__setattr__',  
 '__sizeof__',  
 '__str__',  
 '__subclasshook__',  
 '__weakref__',  
 '_accumulatorServer',  
 '_active_spark_context',  
 '_assert_on_driver',  
 '_batchSize',  
 '_callsite',  
 '_checkpointFile',  
 '_conf',  
 '_dictToJavaMap',  
 '_do_init',  
 '_encryption_enabled',  
 '_ensure_initialized',  
 '_gateway',  
 '_getJavaStorageLevel',  
 '_initialize_context',  
 '_javaAccumulator',  
 '_jsc',  
 '_jvm',  
 '_lock',  
 '_next_accum_id',  
 '_pickled_broadcast_vars',  
 '_python_includes',  
 '_repr_html_',  
 '_serialize_to_jvm',  
 '_temp_dir',  
 '_unbatched_serializer',  
 'accumulator',  
 'addFile',  
 'addPyFile',  
 'appName',  
 'applicationId',  
 'binaryFiles',  
 'binaryRecords',  
 'broadcast',  
 'cancelAllJobs',  
 'cancelJobGroup',  
 'defaultMinPartitions',  
 'defaultParallelism',  
 'dump_profiles',  
 'emptyRDD',  
 'environment',  
 'getCheckpointDir',  
 'getConf',  
 'getLocalProperty',  
 'getOrCreate',  
 'hadoopFile',  
 'hadoopRDD',  
 'master',  
 'newAPIHadoopFile',  
 'newAPIHadoopRDD',  
 'parallelize',  
 'pickleFile',  
 'profiler_collector',  
 'pythonExec',  
 'pythonVer',  
 'range',  
 'resources',  
 'runJob',  
 'sequenceFile',  
 'serializer',  
 'setCheckpointDir',  
 'setJobDescription',  
 'setJobGroup',  
 'setLocalProperty',  
 'setLogLevel',  
 'setSystemProperty',  
 'show_profiles',  
 'sparkHome',  
 'sparkUser',  
 'startTime',  
 'statusTracker',  
 'stop',  
 'textFile',  
 'uiWebUrl',  
 'union',  
 'version',  
 'wholeTextFiles']
```

##### Python Help

We have a list of attributes, but no explanation of how to use them. Use Python's help function ([documentation here


Links to an external site.](https://docs.python.org/3/library/functions.html#help)) to get an easier-to-read list of all the attributes, including examples, that the sc object has.

```
# Use Python's help function to get information on attributes and methods for sc object  
help(sc)
```

**Output (truncated for this example):**

```
Help on SparkContext in module pyspark.context object:  
  
class SparkContext(builtins.object)  
 |  SparkContext(master=None, appName=None, sparkHome=None, pyFiles=None, environment=None, batchSize=0, serializer=PickleSerializer(), conf=None, gateway=None, jsc=None, profiler_cls=<class 'pyspark.profiler.BasicProfiler'>)  
 |    
 |  Main entry point for Spark functionality. A SparkContext represents the  
 |  connection to a Spark cluster, and can be used to create :class:`RDD` and  
 |  broadcast variables on that cluster.  
 |    
 |  When you create a new SparkContext, at least the master and app name should  
 |  be set, either through the named parameters here or through `conf`.  
 |    
 |  Parameters  
 |  ----------
```

##### Investigating Specific Attributes

Refer to the [PySpark documentation


Links to an external site.](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.html) to find the appropriate attributes to answer these questions.

##### Spark Version

What version of Spark is the application running?

```
# Spark version  
sc.version
```

##### Start Time

What time was the Spark Context created?

```
# Start time  
sc.startTime
```

* Note that this is the epoch time so it will appear as a large integer.

##### All Configuration Settings

We can access the complete configuration settings (including all defaults) for the current SparkContext by chaining together the getConf() method and the getAll() method.

```
# All configuration settings  
sc.getConf().getAll()
```

#### Step 4. Shut Down SparkContext

When finished using a SparkContext, we must be sure to call the stop method. This will allow us to create another SparkContext in the future.

```
# Shut down SparkContext  
sc.stop()
```

Once shut down, we can no longer access Spark functionality before starting a new SparkContext.

### Challenges and Solutions Using SparkContext in PySpark

**Note:** some of the challenges have what can be better phrases suggestions since the challenges are open-ended, rather than solutions.

---

#### Managing One SparkContext at a Time

When working with PySpark, it's important to remember that Spark only allows one active `SparkContext` per session. If you try to create another one without stopping the first, you’ll get an error.

**What to Do:**  
Always call `sc.stop()` before creating a new `SparkContext`. To avoid errors, you can use `SparkContext.getOrCreate()` instead of directly instantiating it — this checks if one already exists and reuses it.

**Why This Matters:**  
Spark limits you to a single `SparkContext` to manage resources effectively. Running multiple contexts at once could cause conflicts and consume more memory than necessary.

* **✅ Pros:** Keeps system resource usage efficient and avoids memory issues.
* **⚠️ Cons:** You'll need to restart the context for each new session, which might slow down your workflow if you're experimenting a lot.

---

#### Recognizing Naming Conventions

PySpark methods and attributes often follow **Java-style camelCase** rather than the Pythonic snake\_case you're probably used to.

**What to Do:**  
Understand that this is due to PySpark’s Java roots. If you’re unsure about a method or attribute, use `help(sc)` to explore documentation directly in your environment.

---

#### Configuring SparkContext

At first, Spark’s configuration options may feel overwhelming — there are a lot of parameters you can adjust.

**What to Do:**  
Focus on the two most essential ones to get started:

* `master`: Specifies the execution environment (use `"local[*]"` to run locally on all cores).
* `appName`: A name for your application that shows up in logs and Spark’s UI.

**Why This Matters:**  
Keeping configuration simple allows you to get started quickly without diving into advanced settings.

* **✅ Pros:** Quick setup and less complexity.
* **⚠️ Cons:** You won’t use advanced features right away, which limits customization until you're more confident.

---

#### Interpreting SparkContext Properties

Some properties, like `sc.startTime`, return values in formats like **epoch time**, which can be hard to read at first.

**What to Do:**  
Use Python’s `datetime` module to convert these values into a human-readable format. For example:

```
from datetime import datetime
datetime.fromtimestamp(sc.startTime / 1000)
```

---

#### Shutting Down SparkContext Properly

If you forget to stop the `SparkContext` before creating a new one, you’ll hit a resource error.

**What to Do:**  
Always call `sc.stop()` when you're done with your Spark job. Make it a habit to clean up your Spark session to prevent errors and system slowdowns.

---

Through these considerations, learners can navigate SparkContext’s functionality with a clearer understanding of Spark’s distributed environment while maintaining efficient and resource-conscious Spark sessions.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248253

Scraped At: 2026-05-15T09:52:19.074173
