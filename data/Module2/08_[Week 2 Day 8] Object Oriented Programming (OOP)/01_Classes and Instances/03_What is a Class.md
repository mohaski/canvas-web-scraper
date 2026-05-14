# What is a Class?

# What is a Class?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What is a Class?

Icon Progress Bar (browser only)

7 min read

**Classes** in OOP are a programming abstraction that enable us to combine both data storage and functionality. We can think of them as a blueprint or mold for code objects that we might need to have multiple copies (called “instances”) of, all sharing some essential characteristics (called “attributes” and “methods,” depending whether the characteristic contains information or does something).

### Example of a Class

![Rideshare driver using a GPS app on a road](https://moringa.instructure.com/courses/1406/files/625220/download)
Imagine you are starting a rideshare business. Let's call it *fuber*. All rides generally have the same basic information. They have a driver, passenger(s), origin, destination, car information, and price. You plan on having a pretty large client base, so you could imagine having many rides being taken every day.

So, you will need to have a way to bundle up and operate on all the above information about a particular ride. And as the business would take off, you are going to need to create rides over and over. It would be a huge time suck to have to re-code those essential attributes (driver, passenger, &c.) over and over again.

Python classes make this process much easier. You can create a Ride class that can produce ride instance objects, which would bundle all the information and common operations for a particular ride.

Recall that a class can be thought of as a blueprint that defines how to build an instance object. The Ride class is different from an actual ride instance object just as the blueprint for a car is different from the actual car.

### How Do Classes and Instances Work?

Here is what our Ride class would look like in Python:

```
class Ride:  
   # code for distance attribute  
   # code for time attribute  
   # code for price attribute  
   # code to start a ride  
   # code to end a ride
```

You can see that you use the keyword class to define a Python class. Similar to functions, all the code in a class should be indented. To end the class, you simply stop indenting.

**Note:** Python's convention is that all classes should follow the UpperCaseCamelCase convention. The class name should begin with a capital letter and all other words in the name should also be capitalized. This is also referred to as CamelCase.

It's not enough to simply declare a class in Python. All classes need to have a block of code inside them or else you will get an error. Let's see this below:

```
class Ride:
```

```
File "<ipython-input-1-81f6a00d9a7f>", line 2  
      
    ^  
SyntaxError: unexpected EOF while parsing
```

So, let's add a block of code to our Ride class and see what happens. Python has a keyword pass which you can use in this instance to tell our code to do nothing and continue executing. Pass can be used for times where a block of code is syntactically necessary, like defining a class or function. You can read more about pass [in the Python documentation


Links to an external site.](https://docs.python.org/2/tutorial/controlflow.html#pass-statements).

```
class Ride:  
    pass
```

Woo! No errors! So, you have now successfully defined our Ride class. Let's try to create an instance of this class. Again, you can think of these instances as objects of the Ride class that contain information about a single ride.

```
first_ride = Ride()  
print(first_ride)
```

```
<__main__.Ride object at 0x103a05d30>
```

Okay, you *instantiated* your first ride! You did this by invoking or calling the Ride() class. You invoke a class the same way you do with functions, by adding parentheses () to the end of the class name, (i.e. Ride()).

**Instantiate** means to bring a new object to life (or off the assembly line in our car metaphor). You instantiated a new ride when you invoked the class, Ride(), which made a new ride in our rideshare program.

Each individual object produced from a class is known as an instance or instance object. Our variable, first\_ride, points to an instance of the ride class. You can be sure it is an instance of the Ride class by looking at the object you created.

When you printed first\_ride above, you saw that it says it is a Ride object. This tells us not only which class it comes from, the Ride class, but also that it is an instance since it says object. You can see this distinction more clearly by printing both the class and an instance of that class:

```
print(Ride)  
print(first_ride)
```

```
<class '__main__.Ride'>  
<__main__.Ride object at 0x103a05d30>
```

Great, now let's dive a little deeper into instances. You made one already, let's make a couple more and compare them:

```
second_ride = Ride()  
third_ride = Ride()  
print(first_ride)  
print(second_ride)  
print(third_ride)
```

```
<__main__.Ride object at 0x103a05d30>  
<__main__.Ride object at 0x103a314a8>  
<__main__.Ride object at 0x103a31470>
```

Three rides! Alright, let's look at these. They seem pretty much the same, except the funny numbers at the end. Those are the IDs that represent a place in memory where the computer stores these objects. Additionally, since the IDs are unique, this means that each instance object is a completely unique object although they are all created from the same Ride class. You can prove this by comparing the objects below:

```
print(first_ride is second_ride)  
print(first_ride == second_ride)  
print(first_ride is first_ride)
```

```
False  
False  
True
```

As you can see, first\_ride is only equal to itself even though at this point these objects all have identical attributes and methods (or lack thereof) with the exception of their IDs in our computer's memory.

### Conceptualization: Classes and Instances

Classes and Instances Terms Defined with Examples

| Term | Definition | Example |
| --- | --- | --- |
| Class | A high-level ‘blueprint’ for instantiating objects. Allows for different instances/objects to share methods and attributes. | **Cars:** The Cars class would contain shared information across different types of car*—*wheels, doors, engine, seats, accelerate, brake etc. |
| Instance/Object | Individual objects instantiated from a class. Each object is unique and separate from other instances in memory. | **BMW:** Cars class used to create a BMW object with specific attribute values and methods.  **Honda:** Cars class used to create a different Honda object with its own specific attribute values and methods |
| Attributes | Characteristics of a class and its instances that contain information/data about the objects. | Could be things like engine size, # of wheels, # of doors, towing capacity, weight, make, model, year, and lots of others. |
| Methods | Functions that are defined inside a class and used by the instance objects. Make the object ‘do’ something. | Start the car, accelerate, brake, open the trunk, play radio etc. |
| \_\_init\_\_ method (double underscores) | A ‘magic’ method of classes that allows you to define attribute values when you instantiate an object from a class. | honda = Cars(make=’honda’, model=’crv’, year=2012, doors=4)  The parameters for instantiation are set by the \_\_init\_\_ method defined in the Cars class. |
| Inheritance | Concept that describes the process of using an existing class (and its attributes and methods) to define a new class that shares those properties. The new child class ‘inherits’ from the existing parent class. The new class can then be further customized with new attributes/methods or updates/changes to the existing ones. | Using the Cars class we could create separate classes for different makes/companies and have them inherit attributes and methods from the parent Cars that are shared across all makes.  class BMW(Cars): class Honda(Cars): |
| Super class | Refers to the parent class when inheritance is being used. Allows a child class to update existing methods (like the \_\_init\_\_) that it has inherited from its parent. | class Honda(Cars):       def \_\_init\_\_(self, …):            super().\_\_init\_\_(...)  The Honda child class will inherit parameters from the parent class \_\_init\_\_ method but can include new ones as well. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243639

Scraped At: 2026-05-14T21:02:00.801133
