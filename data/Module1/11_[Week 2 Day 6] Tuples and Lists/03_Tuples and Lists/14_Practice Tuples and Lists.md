# Practice: Tuples and Lists

# Practice: Tuples and Lists

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Tuples and Lists

Icon Progress Bar (browser only)

5 min read

Imagine you're working as a data analyst for a music streaming service. You're tasked with analyzing user data to identify popular music genres and artists. The data is provided in a list format, where each element represents a user's listening history for a specific week. Each listening history is a tuple containing two elements:

* Genre (string)
* List of artists listened to (list of strings)

Your challenge is to write Python code that will:

1. **Identify the most popular genre:** This means finding the genre that appears most frequently across all user listening histories.
2. **Find users who listen to a specific artist:** The service wants to target users who listen to a particular artist for marketing campaigns. You need to identify the users (by index in the data list) who listened to that artist in the past week.

### Instructions

### Task 1: Data Preparation

1. Define a list named `user_data` to store user listening histories.
2. Each element of `user_data` will be a tuple containing two elements.
3. Populate `user_data` with sample data manually (provided below).

```
# Sample user data (replace with your own data creation)  
user_data = [  
    ("Rock", ["Metallica", "Guns N' Roses", "AC/DC"]),  
    ("Pop", ["Taylor Swift", "Ed Sheeran", "BTS"]),  
    ("Hip Hop", ["Drake", "Kendrick Lamar", "J. Cole"]),  
    ("Rock", ["Led Zeppelin", "Pink Floyd", "The Who"]),  
    ("Pop", ["Ariana Grande", "The Weeknd", "Olivia Rodrigo"]),  
]
```

### Task 2: Finding the Most Popular Genre

1. Iterate through the `user_data` list.
2. For each user's listening history (represented by a tuple):

* + Extract the genre from the tuple.
  + Use a dictionary to keep track of genre frequencies. Increment the count for the current genre in the dictionary.

1. After iterating through all users, identify the genre with the highest count in the `genre_counts` dictionary.

### Task 3: Finding Users Who Listen to a Specific Artist

1. Define a variable `targeted_artist` with the name of the artist you want to find.
2. Iterate through the `user_data` list.
3. For each user's listening history (represented by a tuple):

* + Extract the list of artists from the tuple. You can access elements by position within the tuple.
  + Use the in operator to check if target\_artist is present in the list of artists.
  + If found, store the user's index (position in the user\_data list) in a separate list. Use enumerate to iterate with an index and append the index to a list named users\_listening if the artist is found.

### Resources

* Review the technical lesson and module contents on tuples and lists to prepare for this practice.

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Solution

### Select for Solution

```
# Sample user data (replace with your own data creation)  
user_data = [  
    ("Rock", ["Metallica", "Guns N' Roses", "AC/DC"]),  
    ("Pop", ["Taylor Swift", "Ed Sheeran", "BTS"]),  
    ("Hip Hop", ["Drake", "Kendrick Lamar", "J. Cole"]),  
    ("Rock", ["Led Zeppelin", "Pink Floyd", "The Who"]),  
    ("Pop", ["Ariana Grande", "The Weeknd", "Olivia Rodrigo"]),  
]  
  
# Finding most popular genre  
genre_counts = {}  
for genre, _ in user_data:  
  if genre in genre_counts:  
    genre_counts[genre] += 1  
  else:  
    genre_counts[genre] = 1  
  
most_popular_genre = max(genre_counts, key=genre_counts.get)  
print("Most popular genre:", most_popular_genre)  
  
# Finding users who listen to a specific artist  
target_artist = "BTS"  
users_listening = []  
for i, (_, artists) in enumerate(user_data):  
  if target_artist in artists:  
    users_listening.append(i)  
  
if users_listening:  
  print(f"Users who listened to {target_artist}:", users_listening)  
else:  
  print(f"No users listened to {target_artist} this week.")
```

### Select for Explanation

Let’s explore the solution through each step.

#### Step 1: Sample User Data

This section defines a list named user\_data.

* Each element in this list represents a user's listening history for a week.
* It's a tuple containing two elements:
  + **Genre (as a string)**: This represents the music genre the user listened to most during the week.
  + **List of artists (as a list of strings)**: This contains the names of artists the user listened to during the week.

#### Step 2: Finding the Most Popular Genre

Here's how this section identifies the genre that appears most frequently across all user listening histories.

* An empty dictionary named genre\_counts is created. This dictionary will store the frequency of each genre.
* A loop iterates through each user's listening history (represented by a tuple) in the user\_data list.

Here is what happens inside the loop:

* The genre is extracted from the current user's tuple.
* We check if the genre already exists as a key in the genre\_counts dictionary.
  + If it exists (genre in genre\_counts):
    - The count for that genre is incremented by 1 (genre\_counts[genre] += 1).
    - If it doesn't exist (else): A new key-value pair is added to the dictionary. The key is the genre, and the value is set to 1 (initial count).

Once you iterate through all users, the max function is used to find the genre with the highest count in the genre\_counts dictionary.

* The key argument of max specifies a function to use for comparison. Here, genre\_counts.get is used to retrieve the value (count) associated with each genre.
* Finally, the genre with the highest count is printed along with a message.

#### Step 3:  Finding Users Who Listen to a Specific Artist

This section identifies users who listened to a particular artist in the past week.

Here's the step breakdown:

* A variable target\_artist is defined with the name of the artist we want to find (e.g., "BTS").
* An empty list named users\_listening is created to store the indices of users who listened to the target artist.
* A loop iterates through each user's listening history in the user\_data list. Similar to the previous loop, it uses unpacking to access elements within the tuple.

Here is what happens in the loop:

* The list of artists from the current user's tuple is extracted.
* The in operator is used to check if the target\_artist is present in the list of artists for this user.
* If the artist is found (target\_artist in artists), the index (position) of the user in the user\_data list is added to the users\_listening list.

Finally, the code checks if any users listened to the target artist.

* If users were found (users\_listening is not empty), a message is printed listing the user indices.
* If no users listened to the artist, a message indicating that is displayed.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239254

Scraped At: 2026-05-14T15:55:29.200471
