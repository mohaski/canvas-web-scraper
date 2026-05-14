# Practice: Dictionaries

# Practice: Dictionaries

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Dictionaries

Icon Progress Bar (browser only)

3 min read

Imagine you're working as a junior programmer for a music streaming service. One of your tasks is to develop a program that recommends songs to users based on their favorite artists. Users can provide a list of their favorite artists, and the program should suggest songs from those artists or similar genres.

In this scenario, dictionaries can be a powerful tool to store and manage artist-song relationships. We'll create a program that uses dictionaries to:

* Store artist names as keys and a list of their popular songs as values.
* Get user input for their favorite artists.
* Recommend songs based on the user's input and similar artists.

### Instructions

### Step 1: Define Dictionaries

**Create an Artist-Song Dictionary**

1. Define a dictionary named `artist_songs`.
2. Use curly braces `{}` to create the dictionary.
3. Add artist names as keys and lists of their popular songs as values.

```
artist_songs = {  
    "The Beatles": ["Hey Jude", "Let It Be", "Yesterday"],  
    "Taylor Swift": ["Shake It Off", "Love Story", "Blank Space"],  
    "Ed Sheeran": ["Perfect", "Thinking Out Loud", "Photograph"]  
}
```

### Step 2: Get User Input

1. Use the input function to prompt the user to enter their favorite artist.
2. Store the user's input in a variable named favorite\_artist.

```
favorite_artist = input("Enter your favorite artist: ")
```

### Step 3: Recommend Songs

Use an if statement to check if the user's favorite artist exists as a key in the artist\_songs dictionary.

* **If the artist exists:**
* + Use the `[]`operator to access the list of songs associated with the artist.
  + Print a message recommending songs from that list.
* **If the artist doesn't exist:**
* + Print a message suggesting songs from similar artists (you can pre-define a dictionary for similar artists or handle this in a more advanced way later).

```
if favorite_artist in artist_songs:  
    recommended_songs = artist_songs[favorite_artist]  
    print(f"Here are some recommendations from {favorite_artist}:")  
    for song in recommended_songs:  
        print(f"- {song}")  
else:  
    print(f"Sorry, we don't have songs from {favorite_artist} yet. Here are some recommendations from similar artists:")  
    # Add logic to recommend songs from similar artists (replace with your implementation)  
    print("- Similar artist song 1")  
    print("- Similar artist song 2")
```

### Resources

* Review the technical lesson and module content about dictionaries.

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Solution

### Select for Solution

```
# Create an artist-song dictionary  
artist_songs = {  
    "The Beatles": ["Hey Jude", "Let It Be", "Yesterday"],  
    "Taylor Swift": ["Shake It Off", "Love Story", "Blank Space"],  
    "Ed Sheeran": ["Perfect", "Thinking Out Loud", "Photograph"]  
}  
  
# Get user input  
favorite_artist = input("Enter your favorite artist: ")  
  
# Recommend songs  
if favorite_artist in artist_songs:  
    recommended_songs = artist_songs[favorite_artist]  
    print(f"Here are some recommendations from {favorite_artist}:")  
    for song in recommended_songs:  
        print(f"- {song}")  
else:  
    print(f"Sorry, we don't have songs from {favorite_artist} yet. Here are some recommendations from similar artists:")  
    # Add logic to recommend songs from similar artists (replace with your implementation)  
    print("- Similar artist song 1")  
    print("- Similar artist song 2")
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239275

Scraped At: 2026-05-14T15:57:31.295591
