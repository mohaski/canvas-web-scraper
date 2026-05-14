# Technical Lesson: Methods and Attributes

# Technical Lesson: Methods and Attributes

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Methods and Attributes

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

In this lesson, we'll dive into the fundamentals of working with objects in OOP and explore how to define and use methods and attributes effectively.

Objects are at the core of OOP, and they encapsulate both data (attributes) and behavior (methods). Attributes represent the state or properties of an object, while methods define the actions or operations that an object can perform. By combining attributes and methods within a class, we can create powerful and reusable code structures.

Throughout this lesson, we'll cover the following key topics:

1. **Defining attributes:**  
   1. Understanding what attributes are and how they store object-specific data
   2. Declaring and initializing attributes within a class
2. **Creating methods:**  
   1. Understanding the purpose and structure of methods in a class
   2. Defining methods to perform specific actions or computations
   3. Utilizing the self keyword to access object attributes and other methods
3. **The \_\_init\_\_ method:**  
   1. Understanding the significance of the \_\_init\_\_ method as a constructor
   2. Initializing object attributes using the \_\_init\_\_ method
   3. Customizing object creation by accepting arguments in the \_\_init\_\_ method
4. **Accessing attributes and invoking methods:**  
   1. Using dot notation to access object attributes
   2. Calling methods on an object to perform specific actions
   3. Modifying object attributes through methods

By the end of this lesson, you'll have a solid understanding of how to define and work with object attributes and methods. You'll be able to create your own classes, initialize objects with specific attributes, and define methods to manipulate and interact with those objects.

OOP is a powerful paradigm that allows you to organize and structure your code in a logical and reusable manner. By mastering the concepts of object attributes, methods, and the \_\_init\_\_ method, you'll be well-equipped to build robust and maintainable software systems.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of methods and attributes.

[VIDEO LINK](https://player.vimeo.com/video/995574355?h=6236786d95)

### Instructions

* [Part 1: Object Attributes](#dpPanel0Content)
* [Part 2: Object Methods](#dpPanel1Content)
* [Part 3: Magic Methods](#dpPanel2Content)

### Part 1: Object Attributes

Objects can have **properties** that contain information about the object. Also called **attributes** (typically used interchangeably with properties).

This encapsulates something that belongs to an object after it's instantiated from a class.

#### Examples of Properties We've Seen

Take our familiar friend, the [Pandas DataFrame


Links to an external site.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) for example.

```
#Dataframes are another type of object.  
  
df = pd.DataFrame({'price': [50, 40, 30],'sqft': [1000, 950, 500]})  
  
df
```

Instance attributes are associated with each unique object. They describe characteristics of the object, and are accessed with dot notation like so:

```
df.shape
```

What are some other DataFrame attributes we know?

* .columns
* .dtypes
* .index

#### Building Up Our Class with Properties

We can define properties after instantiating our object. Think of it as customization.

```
my_robot = Robot()  
  
my_robot.name = 'Wall-E'  
my_robot.height = 100  # cm
```

```
# It lives!!!!!  
print(my_robot.name, my_robot.height)
```

**Output:**

```
Wall-E 6 ft
```

But we can't call up properties it doesn't have:

```
# Uh oh, we didn't give it this property  
try:  
    print(my_robot.purpose)  
except Exception as err:  
    print(err)
```

**Output:**

```
'Robot' object has no attribute 'purpose'
```

Wouldn't it be nice to have some built-in properties when we instantiated? We can!

```
class Robot:  
    '''Robot class''' # docstring is similar to functions; documents our class  
    purpose = 'To love humans'  
    name = None
```

```
# Give them life!  
my_robot = Robot()  
my_robot.name = 'Wall-E 2.0'  
my_robot.height = 100  # cm  
  
your_robot = Robot()  
your_robot.height = 200 # cm  
  
   
  
print('What is your name?')  
print(my_robot.name)  
print()  
print('What is your purpose?')  
print(my_robot.purpose)
```

**Output:**

```
What is your name?  
Wall-E  
  
What is your purpose?  
To love humans
```

##### Robot Override!!!

You can of course override attributes manually after instantiation.

```
# Rogue robot!!!  
evil_robot = Robot()  
evil_robot.name = 'Bender'  
evil_robot.purpose = 'TO KILL ALL HUMANS!!!'
```

```
print('What is your name and your purpose?\n')  
print(f'My name is {evil_robot.name} and my purpose is {evil_robot.purpose}')
```

**Output:**

```
What is your name and your purpose?  
  
My name is Bender and my purpose is TO KILL ALL HUMANS!!!
```

### Part 2: Object Methods

We can also write functions that are associated with each class. As said above, a function associated with a class is called a method. A method is a function attached to an object.

#### Examples of Methods We've Seen

```
df.info()
```

```
df.isna()
```

What other DataFrame methods do we know?

* .describe()
* .head()
* .groupby()

#### Building Up Our Class with Methods

We can also define our own methods for our class. This requires us to use **self** in our method.

Every method should include self as its first parameter, **which refers to the individual object, i.e. to the instance of the class.**

```
class Robot:  
    '''Robot class'''  
    ## These variables will belong to the Object  
    purpose = 'To love humans'  
    name = None  
  
## These methods belong to the Object (its "self")  
      
    # Method that takes some inputs and returns like a normal function  
    def add_numbers(self, num0, num1):  
        total = num0 + num1  
        return total  
  
     # No parameters; uses attributes of the Object  
    def speak(self):  
        print(f'I am {self.name}!')  
          
    # Modifies the Object  
    def change_name(self, new_name):  
        self.name =  new_name
```

```
walle = Robot()
```

```
print(f'''  
Name: {walle.name}  
Purpose: {walle.purpose}  
''')
```

**Output:**

```
Name: None  
Purpose: To love humans
```

Let's look at those fancy methods the object has:

```
walle.add_numbers(100, 1)
```

**Output:**

```
101
```

```
# Let's give this robot an identity  
walle.change_name("Wall-e")  
# Now what does it say?  
walle.speak()
```

**Output:**

```
I am Wall-e!
```

### Part 3: Magic Methods

It is common for a class to have magic methods. These are identifiable by the "dunder" (i.e. double underscore) prefixes and suffixes, such as **\_\_init\_\_()**. These methods will get called **automatically** as a result of a different call, as we'll see below.

#### \_\_init\_\_()

When we create an instance of a class, Python invokes the **init** to initialize the object. Let's add init to our class.

```
class Robot:  
    '''New and improved robot!'''  
    # We can still define attributes here  
    purpose = 'To love humans'  
    name = None  
      
    # We'd like to start off with some initial attributes  
    def __init__(self, first_name='Generic', last_name=''):  
        # Clean the names of extra spaces at beginning & end  
        first_name = first_name.strip()  
        last_name = last_name.strip()  
          
        # Setting properties  
        self._first_name = first_name  
        self._last_name = last_name  
          
        # Combine first and last names and remove any extra spacing  
        self.name = ' '.join([first_name, last_name]).strip()  
  
  
    # Method that takes some inputs and returns like a normal function  
    def add_numbers(self, num0, num1):  
        total = num0 + num1  
        return total  
  
  
    # No parameters; uses attributes of the Object  
    def speak(self):  
        print(f'I am {self.name}!')  
          
    # Modifies the Object  
    def change_name(self, new_name):  
        self.name = new_name
```

```
walle = Robot('Wall-E')  
bender = Robot('Bender', 'Rodriguez')  
  
walle.speak()  
print(walle.name)
```

**Output:**

```
I am Wall-E Robot!  
Wall-E Robot
```

```
bender.speak()  
print(bender.name)
```

**Output:**

```
I am Bender Rodriguez!  
Bender Rodriguez
```

*ASIDE:* You might notice that if you change the \_first\_name or \_last\_name property of the object, the name property won't update as might be desired. We can adjust this functionality using setters and getters in Python. This is getting a bit deeper into OOP so we won't go into this now.

#### \_\_str\_\_()

The \_\_str\_\_() magic method allows us to customize the string representation of the object. For example, when we use print() on the object, this magic method is called.

```
class Robot:  
    '''New and improved robot!'''  
    # We can still define attributes here  
    purpose = 'To love humans'  
    name = None  
      
    # We'd like to start off with some initial attributes  
    def __init__(self, first_name='Generic', last_name=''):  
        # Clean the names of extra spaces at beginning & end  
        first_name = first_name.strip()  
        last_name = last_name.strip()  
          
        # Setting properties  
        self._first_name = first_name  
        self._last_name = last_name  
          
        # Combine first and last names and remove any extra spacing  
        self.name = ' '.join([first_name,last_name]).strip()  
  
  
    # Method that takes some inputs and returns like a normal function  
    def add_numbers(self, num0, num1):  
        total = num0 + num1  
        return total  
  
  
    # No parameters; uses attributes of the Object  
    def speak(self):  
        print(f'I am {self.name}!')  
          
    # Modifies the Object  
    def change_name(self, new_name):  
        self.name =  new_name  
          
    # We can define how it's string representation!  
    def __str__(self):  
        obj_str_rep = f'Robot: "{self.name}"'  
        return obj_str_rep
```

```
walle = Robot('Wall-E')  
bender = Robot('Bender', 'Rodriguez')  
# Now we can see the string representation!  
print(walle)  
print(bender)
```

**Output:**

```
Robot Wall-E Robot  
Robot Bender Rodriguez
```

```
str(bender)
```

**Output:**

```
'Robot Bender Rodriguez'
```

### Common Challenges and Solutions

**Accessing attributes from outside the class:**

* **Challenge:** Trying to access or modify object attributes directly from outside the class can lead to encapsulation violations and break the principle of data hiding.
* **Solution:** Use getter and setter methods to provide controlled access to attributes. This allows for better encapsulation and maintains the integrity of the object's internal state.

**Forgetting to initialize attributes in the \_\_init\_\_ method:**

* **Challenge:** If you forget to initialize certain attributes in the \_\_init\_\_ method, they may have unexpected default values or cause errors when accessed later.
* **Solution:** Make sure to initialize all the necessary attributes in the \_\_init\_\_ method, either with default values or by accepting arguments during object creation. Double-check your code to ensure all required attributes are properly initialized.

**Overcomplicating methods:**

* **Challenge:** Writing overly complex methods that try to do too much can make the code harder to understand, maintain, and debug.
* **Solution:** Follow the Single Responsibility Principle (SRP) and aim for methods that have a clear and focused purpose. Break down complex tasks into smaller, more manageable methods to improve code readability and maintainability.

### Pros and Cons of Design Decisions

**Using public vs. private attributes:**

* **Pros** of public attributes**:**
  + Easier to access and modify attributes directly.
  + Requires less code overhead compared to using getter and setter methods.
* **Cons** of public attributes**:**
  + Violates encapsulation and allows external code to directly modify object state.
  + Can lead to unexpected behavior and make the code more fragile.
* **Decision:** It's generally recommended to use private attributes (denoted by a leading underscore in Python) and provide controlled access through methods. This promotes better encapsulation and maintains the integrity of the object's internal state.

**Initializing attributes in the \_\_init\_\_ method vs. class-level attributes:**

* **Pros** of initializing attributes in \_\_init\_\_**:**
  + Allows for object-specific attribute values.
  + Provides flexibility to initialize attributes with different values for each object instance.
* **Pros** of class-level attributes**:**
  + Shared among all instances of the class.
  + Useful for defining constants or default values that apply to all objects.
* **Decision:** Use \_\_init\_\_ to initialize attributes that may vary across object instances, and use class-level attributes for shared or default values that remain constant for all objects.

**Implementing methods as instance methods vs. class methods:**

* **Pros** of instance methods**:**
  + Can access and modify object-specific attributes.
  + Operate on individual object instances.
* **Pros** of class methods**:**
  + Can access and modify class-level attributes.
  + Operate on the class itself rather than individual instances.
* **Decision:** Use instance methods when the method needs to work with object-specific attributes or perform actions related to a particular object instance. Use class methods when the method operates on the class as a whole or needs to access class-level attributes.

### Summary

By considering these challenges, pros and cons, and design decisions, you can make informed choices when working with OOP methods, attributes, and the \_\_init\_\_ method. It's important to strike a balance between encapsulation, flexibility, and maintainability to create well-structured and robust classes.

Remember, these are general guidelines, and the specific decisions you make may vary depending on your project requirements and the problem domain you're working with.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243655

Scraped At: 2026-05-14T21:03:18.773885
