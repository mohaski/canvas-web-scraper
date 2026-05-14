# Example: Inheritance

# Example: Inheritance

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Example: Inheritance

Icon Progress Bar (browser only)

2 min read

### Game Development Example

**![Person playing a computer game and wearing a headset](https://moringa.instructure.com/courses/1406/files/625026/download)
Business Problem:**

Imagine you work for a game development studio. While trying to develop a game, you want to avoid as much repetition as possible. You don't want to code up every object independently.

**Solution: Inheritance**

Suppose you have a base class called "GameObject" that represents a generic game object with attributes like position, size, and methods like render() and update(). You can then create derived classes such as "Player," "Enemy," and "Obstacle" that inherit from the "GameObject" class. Note the use of super().\_\_init\_\_() to modify the existing parent init methods and include further parameters when instantiated, depending on the child class.

This allows for shared attributed/properties and object behavior to be coded once and reused throughout the game rather than having to rewrite 'boilerplate code' over and over again. It also allows all 'gameobjects' to interact and behave according to each other if necessary.

```
class GameObject:  
    def __init__(self, position, size):  
        self.position = position  
        self.size = size  
  
  
    def render(self):  
        # Render the game object on the screen  
  
  
    def update(self):  
        # Update the game object's state  
  
  
class Player(GameObject):  
    def __init__(self, position, size, name):  
        super().__init__(position, size)  
        self.name = name  
  
  
    def move(self):  
        # Move the player based on user input  
  
  
class Enemy(GameObject):  
    def __init__(self, position, size, type):  
        super().__init__(position, size)  
        self.type = type  
  
  
    def attack(self):  
        # Perform enemy attack behavior  
  
  
class Obstacle(GameObject):  
    def __init__(self, position, size, destroyable=False):  
        super().__init__(position, size)  
        self.destroyable = destroyable
```

In this example, the "Player", "Enemy", and “Obstacle” classes inherit from the "GameObject" class. They can access the attributes and methods of the base class and also modify the existing init methods using the super() function. Each child class also can add their own specific attributes and methods as needed.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243660

Scraped At: 2026-05-14T21:03:41.802247
