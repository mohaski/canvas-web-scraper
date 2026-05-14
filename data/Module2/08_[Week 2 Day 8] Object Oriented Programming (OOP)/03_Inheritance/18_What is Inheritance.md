# What is Inheritance?

# What is Inheritance?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What is Inheritance?

Icon Progress Bar (browser only)

2 min read

Attributes are the characteristics or properties that define an object of a class. They represent the state of an object and store relevant data. Attributes can be of different data types, such as strings, numbers, booleans, or even other objects. Examples of attributes include name, age, color, size, price, or any other relevant information that describes an object.

Methods are functions or actions that an object of a class can perform. They define the behavior of an object and encapsulate the logic and operations that can be applied to the object's attributes. Methods can have input parameters and can return values. They are used to interact with the object, modify its state, or perform specific tasks. Examples of methods include calculating a value, updating an attribute, performing a specific action, or retrieving information about the object.

### How Does Inheritance Work?

​​In inheritance, the derived (child) class inherits all the non-private attributes and methods of the base (parent) class. This means that the derived class can access and use those attributes and methods as if they were defined within the derived class itself. Inheritance allows for code reuse, as common attributes and behaviors can be defined in the base class and shared by multiple derived classes.

It also supports polymorphism, where objects of the derived classes can be treated as objects of the base class. Inheritance is very easy to accomplish within python and OOP in general. All you need to do is provide the parent class as an argument when defining/creating your child class.

```
class Inheritance_Child_Class(Parent_Class):  
 # New code for child class here
```

### Conceptualization: Measures of Dispersion

Looking at the image below we can see how inheritance might work conceptually. We have a parent/base/super class for all musicians that contains general attributes like name, instrument and band, as well as general methods. We can then have child class pertaining to the different types/genres of musicians where each child class has there own unique methods and/or attributes while also sharing all the general information from the parent class, avoiding having to rewrite that code for each child class.

![Inheritance example using Musician as parent class and jazz, rock, and country musician as child classes](https://moringa.instructure.com/courses/1406/files/625209/download)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243659

Scraped At: 2026-05-14T21:03:35.767877
