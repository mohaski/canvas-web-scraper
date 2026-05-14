# What are Methods and Attributes?

# What are Methods and Attributes?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What are Methods and Attributes?

Icon Progress Bar (browser only)

14 min read

### Attributes

Attributes are the characteristics or properties that define an object of a class. They represent the state of an object and store relevant data. Attributes can be of different data types, such as strings, numbers, booleans, or even other objects. Examples of attributes include name, age, color, size, price, or any other relevant information that describes an object.

Additional Attributes Resource: [*PyDocs Definition: Attribute*


Links to an external site.](https://docs.python.org/3/glossary.html#term-attribute)

### Methods

Methods are functions or actions that an object of a class can perform. They define the behavior of an object and encapsulate the logic and operations that can be applied to the object's attributes. Methods can have input parameters and can return values. They are used to interact with the object, modify its state, or perform specific tasks. Examples of methods include calculating a value, updating an attribute, performing a specific action, or retrieving information about the object.

* **Class:** A bundle of data and functionality. Can be copied and modified to accomplish a wide variety of programming tasks.
* **Method:** A function that is defined inside of a class.
* **Attribute:** Variables (data) that belong to an object.
* **Function:** A series of steps that create, transform, and move data.
* **Magic Method:** A special type of method in Python that starts and ends with double underscores (\_\_). These methods are called on objects under certain conditions without needing to use their names explicitly. Also called dunder methods (for Double UNDERscore).
* **Object:** the more common name for an instance. The two can usually be used interchangeably. Everything in Python is an object.
* **Object-Oriented Programming:** Programming that is oriented around data (made mobile and changeable in objects) rather than functionality. Python is an object-oriented programming language.
* **Procedural Programming:** Programming that is oriented around procedures that are called in sequential order. Fortran and C are procedural programming languages.
* **Property:** Attributes that are controlled by methods, often used interchangeably with attributes.

Additional Methods Resource: [*PyDocs Definition: Method*


Links to an external site.](https://docs.python.org/3/glossary.html#term-method)

### How Do Methods and Attributes Work?

### [Attributes](#dpPanel0)

In Python's object-oriented programming, attributes are variables that store data within a class or its instances. They form the core of an object's state and can be manipulated and accessed throughout the class's methods. Attributes come in two primary varieties: instance attributes and class attributes. Instance attributes are unique to each object created from the class, typically defined within the init method, and can vary between different instances. Class attributes, on the other hand, are shared among all instances of a class and are usually defined at the class level, outside of any method.

Attributes in Python OOP work as follows:

* **Creation and Assignment:**  
  1. Instance attributes are typically created in the init method using self.attribute\_name = value.
  2. Class attributes are defined directly in the class body, outside of any method.
* **Access**:  
  + Attributes are accessed using dot notation: object.attribute for instance attributes, or ClassName.attribute for class attributes.
  + When accessing an attribute, Python first checks for an instance attribute, then falls back to class attributes if not found.
* **Modification:**  
  + Instance attributes can be modified directly on the object.
  + Modifying a class attribute affects all instances, unless an instance has its own attribute with the same name.
* **Inheritance:**  
  + Attributes are inherited by subclasses.
  + Subclasses can override inherited attributes by redefining them.
* **Dynamic nature:**  
  + New attributes can be added to instances at runtime.
  + The dict attribute stores an object's attributes in a dictionary.

```
class Dog:  
    # Class attribute  
    species = "Canis familiaris"  
      
    def __init__(self, name, age):  
        # Instance attributes  
        self.name = name  
        self.age = age  
      
    def description(self):  
        return f"{self.name} is {self.age} years old"  
      
    def speak(self, sound):  
        return f"{self.name} says {sound}"  
  
  
# Creating instances  
dog1 = Dog("Buddy", 5)  
dog2 = Dog("Max", 3)  
  
  
# Accessing instance attributes  
print(dog1.name)  # Output: Buddy  
print(dog2.age)   # Output: 3  
  
  
# Accessing class attribute  
print(dog1.species)  # Output: Canis familiaris  
print(dog2.species)  # Output: Canis familiaris  
print(Dog.species)   # Output: Canis familiaris  
  
  
# Modifying instance attribute  
dog1.age = 6  
print(dog1.age)  # Output: 6  
print(dog2.age)  # Output: 3 (unchanged)  
  
  
# Modifying class attribute  
Dog.species = "Canis lupus familiaris"  
print(dog1.species)  # Output: Canis lupus familiaris  
print(dog2.species)  # Output: Canis lupus familiaris
```

This code illustrates:

1. The class attribute species is shared by all instances of the Dog class.
2. Instance attributes name and age are unique to each Dog instance.
3. Class attributes can be accessed through the class or any instance.
4. Modifying an instance attribute only affects that instance.
5. Modifying a class attribute affects all instances.

### [Methods](#dpPanel1)

Methods in Python are functions defined within a class that operate on objects of that class.

Here's an overview of how methods work in Python:

1. **Definition:** Methods are defined inside a class body, similar to regular functions but with an additional first parameter, typically named 'self'.
2. **The 'self' parameter:** In instance methods, 'self' refers to the instance the method is called on. It's automatically passed when the method is called.
3. **Calling methods:** Methods are called using dot notation on an instance or class (for class methods).
4. **Inheritance:** Methods can be inherited by subclasses and can be overridden.

To define an instance method and later call it on an instance object, you will need to include at least one parameter in the method definition, self.  As with any function or method, you can name the parameters however you want, but the convention in Python is to name this first parameter of all method classes as self, which makes sense since it is the object itself on which you are calling the method.

**Note:** Parameters are the variable names you give to the method or function's future data. They are called parameters when you talk about the definition of a method or function, but when you pass the data, they are referred to as arguments.

Let's play around with it to give you a better idea:

```
class Dog:  
      
    def bark(self):  
        return 'I am actually going to bark this time. bark!'  
          
    def who_am_i(self):  
        return self  
  
  
fido = Dog()  
print("1.", fido.who_am_i()) # Check return value of method  
print("2.", fido) # Comparing return of the fido instance object
```

**Output:**

```
1. <__main__.Dog object at 0x7f7f70659dc0>  
2. <__main__.Dog object at 0x7f7f70659dc0>
```

As you can see our who\_am\_i() method is returning the same instance object as fido, which makes sense because we called this method on fido, and if you look at the method all it does is return the first argument (self), which is the instance object on which the method was called. Again, don't worry if self still seems a bit confusing. It will become clearer through practice. For now, you can just go forward with the knowledge that to define an instance method and later call it on an instance object, you will need to include at least one parameter in the method definition, self.

So far you've seen that self is always explicitly defined as the instance method's first parameter. You've also seen that instance methods implicitly use the instance object as the first argument when you call the method. By convention, you name this first parameter self since it is a reference to the object on which you are operating. Let's take a look at some code that uses self. If you wanted a method that introduces oneself, it would need to include the person's name. To do this, referencing a call to self to retrieve an object attribute is essential.

```
class Person():  
      
    def introduce(self):  
        return f'Hi, my name is {self.name}. It is a pleasure to meet you!'  
      
    def say_hello(self):  
        return 'Hi, how are you?'  
          
    def eat_breakfast(self):  
        self.hungry = False  
        return 'Yum that was delish!'  
          
gail = Person()  
gail.name = 'Gail'  
the_snail = Person()  
the_snail.name = 'the Snail'  
print('1. ', gail.introduce())  
print('2. ', the_snail.introduce())
```

**Output:**

```
1.  Hi, my name is Gail. It is a pleasure to meet you!  
2.  Hi, my name is the Snail. It is a pleasure to meet you!
```

The method is the same for both instance objects, but self is not the same. Self always refers to the object which is being operated on. So, in the case of gail, the method returns the string with the name attribute of the instance object gail. Additionally, note that you also can add instance attributes to gail by using self inside our instance methods (as in the eat\_breakfast() method).

Now let's think about some of our other behaviors that might be a bit more involved in order to make them dynamic. For example, everyone's favorite default conversation, the weather. It changes rapidly and seems to always be a choice topic for small talk. How would we create a method to introduce ourselves and make a comment about the weather?

```
class Person():  
    def say_hello_and_weather(self, weather_pattern):  
        # we are using self instead of instance_obj because we know self represents the instance object  
        return f"Hi, my name is {self.name}! What wildly {weather_pattern} weather we're having, right?!"  
the_snail = Person()  
the_snail.name = 'the Snail'  
print('1. ', the_snail.say_hello_and_weather('humid'))  
# notice that we are ONLY passing in the weather pattern argument  
# instance methods **implicitly** pass in the instance object as the **first** argument
```

**Output:**

```
1.  Hi, my name is the Snail! What wildly humid weather we're having, right?!
```

Again, note that the only arguments you pass in are those that come after self when you define an instance method's parameters.

Now that you've seen how to leverage self and even use instance methods with more than just self as an argument, let's look at how you can use self to operate on and modify an instance object. Let's say it is Gail's birthday. Gail is 29 and she is turning 30. Let’s ensure the instance object reflects that you can define an instance method that updates gail's age:

```
class Person():  
    def happy_birthday(self):  
        self.age += 1  
        return f"Happy Birthday to {self.name} (aka ME)! Can't believe I'm {self.age}?!"  
gail = Person()  
gail.name = 'Gail'  
gail.age = 29  
print('1. ', gail.age)  
print('2. ', gail.happy_birthday())  
print('3. ', gail.age)
```

**Output:**

```
1.  29  
2.  Happy Birthday to Gail (aka ME)! Can't believe I'm 30?!  
3.  30
```

While this method could be improved, the important note is self can be used to not only read attributes from the instance object, but can also change the attributes of the instance object. self is simply the means by which to access underlying attributes stored within the object whether you want to retrieve said information or update it.

Let's take this a step further and look at how you can call other methods using self. Another very important behavior people have is eating. It is something that we all do and it helps prevent us from getting hangry, or angry because we're hungry.

```
class Person():  
    def eat_sandwhich(self):  
        if (self.hungry):  
            self.relieve_hunger()  
            return "Wow, that really hit the spot! I am so full, but more importantly, I'm not hangry anymore!"  
        else:  
            return "Oh, I don't think I can eat another bite. Thank you, though!"  
      
    def relieve_hunger(self):  
        print("Hunger is being relieved")  
        self.hungry = False  
the_snail = Person()  
the_snail.name = 'the Snail'  
the_snail.hungry = True  
print('1. ', the_snail.hungry)  
print('2. ', the_snail.eat_sandwhich())  
print('3. ', the_snail.hungry)  
print('4. ', the_snail.eat_sandwhich())
```

**Output:**

```
1.  True  
Hunger is being relieved  
2.  Wow, that really hit the spot! I am so full, but more importantly, I'm not hangry anymore!  
3.  False  
4.  Oh, I don't think I can eat another bite. Thank you, though!
```

In this code the hungry attribute is being used to check if the object/person is hungry and then subsequently run the relieve\_hunger method if needed. The call to self is necessary in order to reference the individual object/instance on which you want the method to run. Note the self.relieve\_hunger() call within the eat\_sandwich method. The class method relieve\_hunger is being called within another class method eat\_sandwich and therefore the use of self is necessary to call the 2nd method inside.

### [Object Initialization](#dpPanel2)

The \_\_init\_\_ method allows classes to have default behaviors and attributes. It's called automatically when a new instance of the class is instantiated, if that class has an \_\_init\_\_ method, and defines what parameters/arguments are needed when you instantiate an object using that class.

#### Introducing \_\_init\_\_

The \_\_init\_\_ method in Python is a special method, also known as a constructor. It plays a crucial role in object initialization. By using the \_\_init\_\_ method, you can initialize instances of objects with defined attributes. Without this, attributes are not defined until other methods are called to populate these fields, or you set attributes manually. This can be problematic. Here's an example to demonstrate:

```
class Person:  
    def set_name(self, name):  
        self.name = name  
    def set_job(self, job):  
        self.job = job  
bob = Person()
```

If we try to access an attribute before setting it we'll get an error.

```
bob.name
```

```
---------------------------------------------------------------------------  
  
  
AttributeError                            Traceback (most recent call last)  
  
  
<ipython-input-3-b123a67a06c2> in <module>()  
----> 1 bob.name  
  
   
  
  
AttributeError: 'Person' object has no attribute 'name'
```

```
bob.set_name('Bob')  
bob.name
```

```
'Bob'
```

To avoid errors such as this, you can use the \_\_init\_\_ method to set attributes on instantiation. The \_\_init\_\_ method will take in parameters/arguments and assign attributes accordingly via the use of self as seen below. It is vitally important to note that the \_\_init\_\_ method, just as every other method does, passes itself first in order to refer to the individual object instance, hence the self parameter to start.

```
def __init__(self, param1, param2, ...):  
    # initialization code  
    self.attribute1 = param1  
    self.attribute2 = param2
```

1. **The self parameter:**  
   * self refers to the instance being created.
   * It's automatically passed by Python when the object is instantiated.
2. **Instance Attribute Creation:**  
   * Typically used to set initial values for instance attributes.
   * Attributes are assigned using self.attribute\_name = value.
3. **Optional Parameters:**  
   * Can have any number of parameters beyond self.
   * These parameters allow customization of the object during creation.
4. **Calling:**  
   * Not called directly; invoked when creating a new object.
5. **Return Value:**  
   * Should not return any value explicitly.

```
class Person:  
    def __init__(self, name, job):  
        self.name = name  
        self.job = job  
bob = Person('Bob', 'Carpenter')  
print(bob.name)  
print(bob.job)
```

**Output:**

```
Bob  
Carpenter
```

Written like this, these arguments then become required:

```
someone = Person()
```

```
---------------------------------------------------------------------------  
  
  
TypeError                                 Traceback (most recent call last)  
  
  
<ipython-input-8-1ac56b0c183e> in <module>()  
----> 1 someone = Person()  
  
   
  
  
TypeError: __init__() missing 2 required positional arguments: 'name' and 'job'
```

#### Setting default arguments in the \_\_init\_\_ method

To circumvent this, we can also define \_\_init\_\_ to have default arguments. This allows parameters to be specified if desired but are not required.

```
class Person:  
    def __init__(self, name=None, job=None):  
        self.name = name  
        self.job = job  
someone = Person()  
print(someone.name)  
print(someone.job)  
  
print('\n')  
governer = Person(job = 'Carpenter')  
print(governer.name)  
print(governer.job)  
  
print('\n')  
bob = Person('Bob', 'Carpenter')  
print(bob.name)  
print(bob.job)  
  
  
None  
None  
  
   
  
  
None  
Carpenter  
  
   
  
Bob  
Carpenter
```

The \_\_init\_\_ method in Python serves as a constructor for class instances, automatically called when an object is created. It initializes the object's attributes and performs any necessary setup. Typically, you define \_\_init\_\_ with parameters that allow customization of the object during instantiation. Inside \_\_init\_\_, you use the self keyword to create and set instance attributes, like self.attribute = value. You can also include default values for parameters and perform other initialization tasks. When creating an object, you pass the required arguments to the class, which are then used by \_\_init\_\_ to set up the instance. This method is crucial for establishing the initial state of an object and ensuring it's ready for use immediately after creation. While \_\_init\_\_ is called automatically, it's your responsibility to design it to properly initialize your objects based on your class's specific needs.

### Conceptualize Methods and Attributes

  

Methods and Attributes terms defined with example

| Term | Definition | Example |
| --- | --- | --- |
| Attributes | Characteristics of a class and its instances that contain information/data about the objects. | Could be things like engine size, # of wheels, # of doors, towing capacity, weight, make, model, year, and lots of others. |
| Methods | Functions that are defined inside a class and used by the instance objects. Make the object ‘do’ something. | Start the car, accelerate, brake, open the trunk, play radio etc. |
| \_\_init\_\_ method (double underscores) | A ‘magic’ method of classes that allows you to define attribute values when you instantiate an object from a class. | honda = Cars(make=’honda’, model=’crv’, year=2012, doors=4)  The parameters for instantiation are set by the \_\_init\_\_ method defined in the Cars class |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243649

Scraped At: 2026-05-14T21:02:47.098511
