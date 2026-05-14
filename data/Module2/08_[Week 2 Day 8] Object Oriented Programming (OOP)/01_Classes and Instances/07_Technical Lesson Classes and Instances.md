# Technical Lesson: Classes and Instances

# Technical Lesson: Classes and Instances

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Classes and Instances

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[10 minutes]

Classes and instances allow you to DRY (Don’t Repeat Yourself) your code, making it more readable for other users, and avoiding unnecessary repetition. *Classes* serve as blueprints for *instances* that need to be created often and share similar *methods* and *attributes*.

* A class is like a blueprint or mold.
* An object is made from the class (called instantiation because it creates an instance), similar to making an item from the blueprint.
* The class tells us how to make objects. We can make many objects based on the class, but our object (or instance) is still an individual and can be modified after being created (or instantiated).

This technical lesson will walk through the process of creating and defining classes.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of classes and instances.

[VIDEO LINK](https://player.vimeo.com/video/995574328?h=a514551de2)

### Classes and Objects in Python

We can create our own classes and instantiate their related objects in Python.

#### Step 1:

We can define new classes of objects altogether by using the keyword class:

```
class Robot:  
  # Essentially a blank template since we never defined any attributes  
  pass
```

#### Step 2:

With the Robot class object defined, we can instantiate it:

```
# Instantiate the object  
my_robot = Robot()  
type(my_robot)
```

**Output:**

```
'__main__.Robot'
```

```
my_robot
```

**Output:**

```
<__main__.Robot object at 0x100d00d60>
```

```
# My little army of many robots  
robot_army = [Robot() for _ in range(5)]  
robot_army
```

**Output:**

```
[<__main__.Robot object at 0x100d00cd0>, <__main__.Robot object at 0x100d00f70>, <__main__.Robot object at 0x100d00f40>, <__main__.Robot object at 0x100d00f10>, <__main__.Robot object at 0x100d00ee0>]
```

```
# Remember each robot is an individual, a special snowflake ❄️  
robot_army[0] is robot_army[1]
```

**Output:**

False

In the next sections, we'll go over expanding and customizing our class with something called attributes and methods.

#### Considerations

Using classes in Python has both advantages and disadvantages, but two stand out:

* **Advantage:** Using classes can DRY your code, eliminate unnecessary redundancy and repetition. It doesn’t fit every situation, but it can be a big help.
* **Disadvantage:** There is a risk of too much abstraction. Remember that one of the essential features of Pythonic code is that it is human-readable. Abstractions like classes reduce the amount of code in in a program, but can make it harder to understand at a glance. Overuse of classes and inheritance hierarchies can lead to complex, difficult-to-maintain code. It's important to strike a balance between abstraction and readability, ensuring that the code remains clear and comprehensible to other developers (including your future self).

When using classes, it's crucial to:

* Keep class hierarchies relatively shallow.
* Use clear, descriptive names for classes and methods.
* Document your code thoroughly, especially for complex class structures.
* Consider whether a simpler solution (like functions) might suffice for your needs.
* Regularly review and refactor your code to maintain clarity and simplicity.

Remember, the goal is to write code that solves problems efficiently while remaining maintainable and understandable to humans. Classes are a powerful tool, but they should be used judiciously and with careful consideration of their impact on code readability and maintainability.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243644

Scraped At: 2026-05-14T21:02:28.016136
