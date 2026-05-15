# Technical Lesson: Big Data

# Technical Lesson: Big Data

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: Big Data

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

The mrjob package is a Python library designed to simplify the process of writing and running MapReduce jobs. It provides a high-level interface for defining MapReduce tasks, allowing users to focus on the core data processing logic without worrying about the underlying complexities. Whether you're running jobs on Hadoop, Amazon Elastic MapReduce (EMR), or even a local machine, mrjob handles the details of job execution and platform management.

In this lesson, you’ll follow the process of setting up a MapReduce job using mrjob. The package abstracts away the complexities of managing Hadoop or other distributed systems, enabling you to quickly prototype, test, and run your jobs efficiently.

By using mrjob, you can focus on solving data processing challenges without getting bogged down in the technical setup of distributed systems, making it an ideal tool for rapid development and learning.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of big data.

[VIDEO LINK](https://player.vimeo.com/video/1038328914?h=467a041459)

### Resources

* [song\_count.py


  Links to an external site.](https://drive.google.com/file/d/13iRn4mpS-7ZrJQWbH6Acq7KSNGnazI4l/view?usp=drive_link)
* [wordcount.py


  Links to an external site.](https://drive.google.com/file/d/151s_VM1R85zVg5Fslau82Vu1QPF3L9uQ/view?usp=drive_link)
* [songplays.txt


  Links to an external site.](https://drive.google.com/file/d/1tWTOYhO0rsXOQSrhHgKjI6izYXeIZz9n/view?usp=drive_link)

### Instructions

* [Step 1. Install mrjob](#dpPanel0Content)
* [Step 2. Define MapReduce Logic](#dpPanel1Content)
* [Step 3. Inspect Data](#dpPanel2Content)
* [Step 4. MapReduce in Action](#dpPanel3Content)
* [Step 5. Deep Dive: Mapper Step](#dpPanel4Content)
* [Step 6. A Second Example - Defining the MapReduce](#dpPanel5Content)
* [Step 7. Running the MapReduce Wordcount](#dpPanel6Content)

#### Step 1. Install mrjob

mrjob is a package that allows you to write MapReduce jobs in Python which can be useful for testing on your local machine.

* Checkout the [mrjob documentation


  Links to an external site.](https://mrjob.readthedocs.io/en/latest/index.html) for more information.

**Install it by running this cell (uncommented):**

```
# # This package is for running MapReduce jobs with Python  
# ! pip install mrjob 
```

#### Step 2. Define MapReduce Logic

Here's what's in the `song_count.py` file:

```
from mrjob.job import MRJob  
  
class MRCountSongs(MRJob):  
      
    # Each line in will be read as a key, value  
    # Each line has no key, so we ignore it with `_`  
    def mapper(self, _, song):  
        # Each line is a tuple: (song_names, 1)   
        yield (song, 1)  
  
    # Combine all tuples with the same key  
    def reducer(self, key, values):  
        # Key is the song name  
        # Sum up values in the tuple to get total song plays  
        yield (key, sum(values))  
          
# Runs this if I call it via the terminal          
if __name__ == "__main__":  
    MRCountSongs.run()
```

**Here is an explanation of the code that is designed to count the occurrences of songs.**

1. First, the code imports the `MRJob` class from the `mrjob.job` module:  

   ```
   from mrjob.job import MRJob
   ```
2. A new class `MRCountSongs` is defined, which inherits from `MRJob`:  

   ```
   class MRCountSongs(MRJob):
   ```
3. The `mapper` function is defined:  

   ```
   def mapper(self, _, song):  
          yield (song, 1)
   ```

   This function takes two parameters: `\_` (which is ignored and conventionally used for unused variables) and `song`. For each input line (assumed to be a song name), it yields a tuple `(song, 1)`.
4. The `reducer` function is defined:  

   ```
   def reducer(self, key, values):  
          yield (key, sum(values))
   ```

   This function takes a key (song name) and an iterable of values. It sums up all the values for each key and yields a tuple of `(key, sum)`.
5. Finally, there's a conditional block to run the job:  

   ```
   if __name__ == "__main__":  
          MRCountSongs.run()
   ```

   This checks if the script is being run directly (not imported as a module). If so, it runs the MapReduce job.

**In summary, this code sets up a MapReduce job that:**

1. Takes input lines, each representing a song.
2. Maps each song to a key-value pair of (song\_name, 1).
3. Reduces by summing up all the 1s for each unique song name.
4. Outputs the result as (song\_name, total\_count) for each song.

This is useful for counting how many times each song appears in a large dataset, potentially representing play counts or popularity.

#### Step 3. Inspect Data

```
# The top of the list from the data file  
! head songplays.txt
```

```
Deep Dreams  
Data House Rock  
Deep Dreams  
Data House Rock  
Broken Networks  
Data House Rock  
Deep Dreams  
Deep Dreams  
Data House Rock  
Deep Dreams
```

#### Step 4. MapReduce in Action

Now let’s count the number of times each song occurs using MapReduce.

```
# Counts how many time each song occurs  
! python song_count.py songplays.txt
```

The essential output is given here:

```
"Deep Dreams"    1131  
"Broken Networks"    510  
"Data House Rock"    828
```

#### Step 5. Deep Dive: Mapper Step

By repeating the previous code  by adding the -- mapper tag, one can get a better understanding of what is happening in the mapper step.

```
# You can see more closely what's happening in the mapper step  
! python song_count.py songplays.txt --mapper
```

#### Step 6. A Second Example - Defining the MapReduce

**Word Count**

Here's what's in the wordcount.py file:

```
from mrjob.job import MRJob  
import string  
  
class MRWordFreqCount(MRJob):  
  
    def mapper(self, _, line):  
        line = line.strip()  
        # Remove punctuations  
        for s in string.punctuation:  
            line = line.replace(s, '')  
        words = line.split()  
        for word in words:  
            yield (word.lower(), 1)  
  
    def reducer(self, word, counts):  
        yield (word, sum(counts))  
  
  
if __name__ == '__main__':  
    MRWordFreqCount.run()
```

This code is another MapReduce job using the mrjob library in Python, but this time it's designed to count the frequency of words in a text. Here is what the code is doing.

1. Import statements  

   ```
   from mrjob.job import MRJob  
      import string
   ```

   This imports the `MRJob` class from mrjob and the `string` module, which will be used for punctuation removal.
2. Class definition:  

   ```
      class MRWordFreqCount(MRJob):
   ```

   This defines a new class `MRWordFreqCount` that inherits from `MRJob`.
3. Mapper function:  

   ```
   def mapper(self, _, line):  
          line = line.strip()  
          # Remove punctuations  
          for s in string.punctuation:  
              line = line.replace(s, '')  
          words = line.split()  
          for word in words:  
              yield (word.lower(), 1)
   ```

   This function processes each line of input:  
   * It strips leading/trailing whitespace
   * Removes all punctuation characters
   * Splits the line into words
   * For each word, it yields a key-value pair of (word in lowercase, 1)
4. Reducer function:

   ```
   def reducer(self, word, counts):  
          yield (word, sum(counts))
   ```

   This function takes a word and an iterable of counts and then It sums up all the counts for each word and yields the result.
5. Main execution block:  

   ```
   if __name__ == '__main__':  
          MRWordFreqCount.run()
   ```

   This runs the MapReduce job if the script is executed directly.

**In summary, this code:**

1. Reads input text line by line.
2. Processes each line by removing punctuation and splitting into words.
3. Maps each word to a key-value pair of (word, 1).
4. Reduces by summing up all the 1s for each unique word.
5. Outputs the result as (word, total\_count) for each word.

This job would be useful for analyzing the frequency of words in a large body of text, which could be helpful in tasks like text analysis, creating word clouds, or identifying common terms in a document.

#### Step 7. Running the MapReduce Wordcount

```
! python wordcount.py songplays.txt
```

The essential output is given here:

```
"dreams"    1131  
"house"    828  
"broken"    510  
"data"    828  
"deep"    1131  
"networks"    510  
"rock"    828
```

Again, if one would like to see the details of the process one could add ‘--mapper’ to the previous code chunk.

### Summary

By making thoughtful decisions around how to run, debug, and preprocess data in MapReduce jobs, you can gradually build your skills while avoiding common pitfalls, ensuring you're prepared for larger-scale applications in the future.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248210

Scraped At: 2026-05-15T09:49:41.909652
