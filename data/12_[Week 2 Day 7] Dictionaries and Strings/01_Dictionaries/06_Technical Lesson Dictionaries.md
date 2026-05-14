# Technical Lesson: Dictionaries

# Technical Lesson: Dictionaries

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Technical Lesson: Dictionaries

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time: 30 min.**

Imagine you're developing a program for a music streaming service. You want to recommend songs to users based on their favorite artists. Dictionaries can efficiently store artist names as keys and their popular songs as values.

Here is a brief overview of the steps you will complete in this lesson:

1. Define the Dictionary
2. Add Key/Value Pairs
3. Accessing Data
4. Iterating Through Songs
5. Conditional Recommendation (Decision Point)

### Resources

* Review the content about dictionaries within this module.

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Instructions

### Step 1: Define the Dictionary

* **Action:** Use curly braces `{}` to define a dictionary named `artist_songs`.
* **Explanation:** The empty curly braces represent the initial structure of the dictionary.

**Sample Code:**

```
artist_songs = {}
```

### Step 2: Add Key-Value Pairs

* **Action:** Inside the curly braces, specify artist names separated by commas, followed by a colon `:` and then a list of their popular songs enclosed in square brackets `[]`.
* **Explanation of the Sample Code**: Each line creates a key-value pair. The artist name becomes the key (used for accessing data), and the song list becomes the value associated with that key.

**Sample Code:**

```
artist_songs = {  
    "The Beatles": ["Hey Jude", "Let It Be", "Yesterday"],  
    "Taylor Swift": ["Shake It Off", "Love Story", "Blank Space"],  
    "Ed Sheeran": ["Perfect", "Thinking Out Loud", "Photograph"]  
}
```

### Step 3: Accessing Data

* **Action:** Use the artist name (key) enclosed in square brackets `[]` to retrieve the corresponding value (song list).
* **Explanation of the Sample Code:** By providing the key "The Beatles", we access the value associated with it, which is the list of Beatles' songs.

**Sample Code:**

```
beatles_songs = artist_songs["The Beatles"]  
  
print(beatles_songs)  # Output: ["Hey Jude", "Let It Be", "Yesterday"]
```

### Step 4: Iterating Through Songs

* **Action:** Once you have the song list (value), you can use a for loop to iterate through each song and potentially perform actions like printing them.
* **Explanation of the Sample Code:** The for loop iterates through each song in the beatles\_songs list, and inside the loop, we print each song with a hyphen for better formatting.

**Sample Code:**

```
for song in beatles_songs:  
  
    print(f"- {song}")
```

### Step 5: Conditional Recommendation (Decision Point)

* **Action:** Use an if statement to check if the user's favorite artist exists as a key in the dictionary.
  + **If the Artist Exists:** Recommend songs from that artist.
  + **If the Artist Doesn't Exist:** Handle the case by providing a message and potentially suggesting songs from similar artists (covered later in practice labs).

### Considerations

Dictionaries offer a powerful way to manage data with key-value pairs, but there are some key considerations around challenges and decisions to keep in mind:

#### Key Errors Issue

Trying to access a value using a non-existent key will raise a KeyError.

**Solution**

* **Validation**: Before accessing values, use if key in my\_dict: to check if the key exists.
* **Default values**: Assign a default value (e.g., an empty list) for missing keys to avoid errors.

#### Unordered Nature

Unlike lists, dictionaries don't guarantee the order in which key-value pairs are stored or iterated through.

**Solution**

* **Maintain order:** If order matters, consider using an alternative data structure like an ordered dictionary (available in Python 3.7+).
* **Focus on keys:** If the order doesn't matter, focus on using the keys to access specific values.

#### Mutable Values

While keys must be immutable, values in a dictionary can be mutable (e.g., lists). Modifying a value within the dictionary can affect other parts of your program that reference that value.

**Solution**

* **Be mindful of changes:** If modifying values is necessary, understand the impact on other parts of your code.
* **Consider copying:** If extensive modifications are needed, consider creating a copy of the value to avoid unintended consequences.

### Decisions

#### **Default Values for Missing Keys:**

**Decision:**  Choose whether to handle missing keys with validation errors or provide default values.

**Impact**

* **Validation errors:**  Catches potential mistakes early but might require more handling in your code.
* **Default values:**  Provides a fallback but requires defining appropriate defaults for all possible missing keys.

#### **Maintaining Order (if necessary):**

**Decision:** Determine if the order of key-value pairs is crucial for your program logic.

**Impact**

* **No order needed:** Dictionaries are efficient for unordered data access.
* **Order required:** Consider using ordered dictionaries (Python 3.7+) or alternative data structures like lists with custom indexing if order is critical.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239273

Scraped At: 2026-05-14T15:57:23.729878
