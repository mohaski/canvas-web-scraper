# Examples: While Loops

# Examples: While Loops

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Examples: While Loops

Icon Progress Bar (browser only)

3 min read

Lets look at a basic example of using a while loop. Throughout this topic, you will apply your learning to this specific guessing game example in a few different ways. In the following video you will learn about how to construct a while loop.

[VIDEO LINK](https://player.vimeo.com/video/995532011?h=9411e72ec6)

Imagine a guessing game where you have three (3) tries to guess a secret number. The loop continues as long as your guess count is less than 3 (condition is True). Inside the loop, you take a guess and increment the counter. If your guess is correct (if statement), the loop exits using break. If you run out of guesses (condition becomes False), the loop terminates, and the program displays a message.

Python Feature and Game Analogy

| **Python Feature** | **Guessing Game Analogy** |
| --- | --- |
| Condition | Guess count < 3 |
| Loop Body | Taking a guess |
| Loop Termination | Guess count reaches 3 or guess is correct |

This code sample below demonstrates this while loop.

```
guess_count = 0  # Initialize a guess counter  
secret_number = 7  # The secret number to guess  
  
while guess_count < 3:  # Loop continues until 3 guesses are made  
  guess = int(input("Guess a number between 1 and 10: "))  
  guess_count += 1  # Increment guess counter  
  
  if guess == secret_number:  
    print("You guessed it!")  
    break  # Exit the loop if the guess is correct  
  
# Code after the loop (executes only if the guess wasn't correct in 3 tries)  
print("Sorry, you ran out of guesses. The number was", secret_number)
```

### Industry Examples of While Loops

The following examples use while loops across industries and tech skills to solve business problems. Learning basic coding foundations like while loops will help you develop more complex skills to be able to collaborate on teams.

#### ![&#34;&#34;](https://moringa.instructure.com/courses/1391/files/620273/download) Feature Engineering

* While loops can be used to create new features from existing data.
* For instance, a loop can iterate through a dataset and calculate the average price for each product category within a specific time frame.

#### ![&#34;&#34;](https://moringa.instructure.com/courses/1391/files/620324/download) Machine Learning Model Training

* While loops are a common way to control the training process for machine learning models.
* A loop can be used to iterate through training epochs (repetitions) until a stopping criterion is met, such as achieving a desired level of accuracy.

#### ![&#34;&#34;](https://moringa.instructure.com/courses/1391/files/620282/download) Intrusion Detection

* While loops can be used in a Python script to continuously monitor network traffic for suspicious activity.
* The loop can iterate through incoming packets, checking for patterns that might indicate a security breach.

#### ![&#34;&#34;](https://moringa.instructure.com/courses/1391/files/620239/download) Password Cracking

* While loops are a part of some brute-force password cracking scripts.
* A loop can be used to systematically try different combinations of characters until the correct password is found.

#### ![&#34;&#34;](https://moringa.instructure.com/courses/1391/files/620275/download) Security Information and Event Management (SIEM)

* SIEM systems often use while loops in their source code to process security logs continuously.
* The loop can iterate through new log entries, analyze them for threats, and trigger alerts if necessary.

#### ![&#34;&#34;](https://moringa.instructure.com/courses/1391/files/620352/download)

#### User Input Validation

* While loops can be used to ensure that user input meets specific criteria.
* For example, a loop can keep prompting the user for input until they enter a valid email address format.

#### ![&#39;&#39; &#34;](https://moringa.instructure.com/courses/1391/files/620297/download)

#### Game Development

* While loops are essential for creating game mechanics and animations.
* A loop can be used to continuously update the game world, move characters, and handle player interactions.

#### ![&#34;&#34;](https://moringa.instructure.com/courses/1391/files/620306/download)

#### User Interface (UI) Automation

* While loops can be used to automate repetitive tasks within a user interface.
* For instance, a loop can be used to click through a series of menus or buttons in a specific order.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239171

Scraped At: 2026-05-14T15:21:32.016645
