# Practice: Big Data

# Practice: Big Data

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Practice: Big Data

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

In this practice, you will work with the text of Romeo and Juliet using MapReduce to perform basic text analysis, such as word counting and identifying the most common words. This exercise reinforces the fundamental skill of working with MapReduce, which is crucial for processing large datasets in real-world scenarios. While the text analysis here is simple, the same principles can be applied to more complex Big Data tasks in the workplace.

Follow the steps below to apply MapReduce to analyze the text, reinforcing the connection between theoretical concepts and practical application:

### Resources

* [wordcount.py


  Links to an external site.](https://drive.google.com/file/d/151s_VM1R85zVg5Fslau82Vu1QPF3L9uQ/view?usp=drive_link)
* [song\_count.py


  Links to an external site.](https://drive.google.com/file/d/13iRn4mpS-7ZrJQWbH6Acq7KSNGnazI4l/view?usp=drive_link)
* [wordcountmax.py


  Links to an external site.](https://drive.google.com/file/d/1PdMH4n4Gy7Lv7gCXuKuXFLLsa2o2vuEV/view?usp=drive_link)
* [top5.py


  Links to an external site.](https://drive.google.com/file/d/1yksFpS0njWre_cjiH1XK9nphDYyjjPEW/view?usp=drive_link)
* [countrj.py


  Links to an external site.](https://drive.google.com/file/d/171yq21NhyiZwjZ0Dtaqe2k_wKyND6AD7/view?usp=drive_link)
* [romeoandjuliet.txt


  Links to an external site.](https://drive.google.com/file/d/1oIJ2KsdSgzotEGXhOxuxtDCedDT_jC9b/view?usp=drive_link)
* **Note:** `mrjob` is currently **not compatible with Python 3.13** due to the removal of the `pipes` module in the standard library. Please use **Python 3.11** or earlier versions to ensure full functionality when running `mrjob` scripts using `python=3.11`

### Instructions

### [Step 1: Install the mrjob Package](#dpPanel0)

**Objective:** Ensure you have the mrjob package installed to run the MapReduce jobs in Python. This package simplifies running MapReduce tasks and will allow you to execute them on your local machine.

**Action:** If the package is not already installed, uncomment and run the following line to install it:

```
# ! pip install mrjob
```

### [Step 2: Review the Romeo and Juliet Text File](#dpPanel1)

**Objective:** Familiarize yourself with the text file that will be processed. This step gives context to the type of data you will process using MapReduce.

**Action:** Open the text file but focus on the end of the file rather than the beginning to get a sense of its structure and content.

### [Step 3: List the Lines in the Play Using MapReduce](#dpPanel2)

**Objective:** Use the existing "song\_count.py" file to list the lines from Romeo and Juliet. This helps you see how MapReduce can process input text line by line, no matter the content.

**Action:** Execute the Python file (song\_count.py) to list the text lines. While the file is originally named for counting songs, it can be repurposed for text analysis in this context.

### [Step 4: Review the Mapper Output](#dpPanel3)

**Objective:** Deepen your understanding of how the mapper function works in MapReduce. Understanding this output will clarify the role of the mapper in transforming the input data for subsequent reduction.

**Action:** Repeat the previous code execution, but this time append the --mapper flag to observe the output from the mapper step. This shows how the mapper processes each line into key-value pairs.

### [Step 5: Count the Number of Words in Romeo and Juliet](#dpPanel4)

**Objective:** Use MapReduce to count the number of words in the play. This step reinforces the basic functionality of MapReduce for text analysis, which is crucial in handling large-scale datasets in data science tasks.

**Action:** Execute a MapReduce job that uses the wordcount.py file to count the occurrences of each word in Romeo and Juliet.

### [Step 6: Identify the Most Frequent Word](#dpPanel5)

**Objective:** Determine the word that occurs most frequently in the text. This gives insight into how MapReduce can be adapted to identify specific patterns or trends in large datasets, such as finding dominant terms in a text corpus.

**Action:** Run the wordcountmax.py file to find the most frequent word in the play and note how many times it appears.

### [Step 7: Find the Top 5 Most Common Words](#dpPanel6)

**Objective:** Use MapReduce to list the top 5 most frequent words in the text along with their counts. This demonstrates how MapReduce can prioritize data for insights, which is useful for business tasks like identifying the most popular items or keywords in a dataset. Note that this excludes certain very popular words that are not meaningful to a text analysis of this play.

**Action:** Run the top5.py file to generate the top 5 words and their corresponding frequencies.

### [Step 8: Modify to Show the Top 10 Most Common Words](#dpPanel7)

**Objective:** Modify the existing code to display the top 10 most frequent words. This exercise highlights how MapReduce scripts can be adapted and customized based on analytical needs in a workplace environment. This includes all of the words unlike the previous step.

**Action:** Edit the top5.py file and rename it to top10.py. Modify the logic to show the top 10 most common words in Romeo and Juliet, along with their counts.

### [Step 9: Count the Occurrences of "Romeo" and "Juliet"](#dpPanel8)

**Objective:** Use MapReduce to count how many times Romeo and Juliet are mentioned in the play. This task simulates real-world data comparison, such as analyzing customer mentions or product usage in a dataset.

**Action:** Run the countrj.py file to compare the number of times each name appears. Identify whose name is mentioned more frequently.

### Solution

### [Select for Solution](#dpPanel9)

#### Step 1

Begin by installing mrjob, if necessary, by uncommenting it.

```
 # Run this code, if necessary  
 # ! pip install mrjob
```

#### Step 2

Look at the Romeo and Juliet text file, but look at the end rather than the beginning.

```
! tail romeoandjuliet.txt
```

**Expected Output:**

```
       Prin. A glooming peace this morning with it brings,  
    The Sunne for sorrow will not shew his head;  
    Go hence, to haue more talke of these sad things,  
    Some shall be pardon'd, and some punished.  
    For neuer was a Storie of more Wo,  
    Then this of Iuliet, and her Romeo.  
      
    Exeunt. omnes  
  
    FINIS. THE TRAGEDIE OF ROMEO and IVLIET
```

#### Step 3

While the python file is still called "song\_count", we can use it to list the lines in the play.

```
! python song_count.py romeoandjuliet.txt
```

#### Step 4

Repeat the previous code but append the "tick tick mapper".

```
! python song_count.py romeoandjuliet.txt --mapper
```

#### Step 5

Now use MapReduce to count the number of words in Romeo and Juliet.

```
! python wordcount.py romeoandjuliet.txt
```

#### Step 6

Consider the 'wordcountmax.py" file that finds the word that shows the most often. What is the word? And how many times?

```
! python wordcountmax.py romeoandjuliet.txt
```

**Expected Output:**

```
    No configs found; falling back on auto-configuration  
    No configs specified for inline runner  
    Creating temp directory /tmp/wordcountmax.root.20240717.150912.274245  
    Running step 1 of 2...  
    Running step 2 of 2...  
    job output is in /tmp/wordcountmax.root.20240717.150912.274245/output  
    Streaming final output from /tmp/wordcountmax.root.20240717.150912.274245/output...  
    692    "and"  
    Removing temp directory /tmp/wordcountmax.root.20240717.150912.274245...
```

#### Step 7

The top5.py uses MapReduce to give the 5 most common words along with their frequencies. What are they and how many times does each occur?

```
! python top5.py romeoandjuliet.txt
```

**Expected Output:**

```
  No configs found; falling back on auto-configuration  
    No configs specified for inline runner  
    Creating temp directory /tmp/top5.root.20240717.151044.166756  
    Running step 1 of 2...  
    Running step 2 of 2...  
    job output is in /tmp/top5.root.20240717.151044.166756/output  
    Streaming final output from /tmp/top5.root.20240717.151044.166756/output...  
    "is"    340  
    "in"    316  
    "you"    289  
    "thou"    277  
    "me"    264  
    Removing temp directory /tmp/top5.root.20240717.151044.166756...
```

#### Step 8

Now modify the top5.py file and make it so that it shows the top 10 most common words used along with their counts. Call this file top10.py.

```
! python top10.py romeoandjuliet.txt
```

**Expected Output:**

```
  No configs found; falling back on auto-configuration  
    No configs specified for inline runner  
    Creating temp directory /tmp/top10.root.20240717.151138.457659  
    Running step 1 of 2...  
    Running step 2 of 2...  
    job output is in /tmp/top10.root.20240717.151138.457659/output  
    Streaming final output from /tmp/top10.root.20240717.151138.457659/output...  
    "and"    692  
    "the"    659  
    "i"    597  
    "to"    548  
    "a"    471  
    "of"    382  
    "my"    374  
    "that"    343  
    "is"    340  
    "in"    316  
    Removing temp directory /tmp/top10.root.20240717.151138.457659...
```

#### Step 9

Use the countrj.py file to find out how many times Romeo and Juliet's names are used. Whose name is used more?

```
! python countrj.py romeoandjuliet.txt
```

**Expected Output:**

```
  No configs found; falling back on auto-configuration  
    No configs specified for inline runner  
    Creating temp directory /tmp/countrj.root.20240717.153040.387283  
    Running step 1 of 1...  
    job output is in /tmp/countrj.root.20240717.153040.387283/output  
    Streaming final output from /tmp/countrj.root.20240717.153040.387283/output...  
    "romeo"    138  
    "iuliet"    54  
    Removing temp directory /tmp/countrj.root.20240717.153040.387283...
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248212

Scraped At: 2026-05-15T09:49:49.228219
