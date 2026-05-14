# Practice: Creating Classes

# Practice: Creating Classes

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Creating Classes

Icon Progress Bar (browser only)

5 min read

You've learned how to declare classes and create instances in the last lesson. Now it's time to put these new skills to the test! Remember the simple process introduced to create your own classes. We will investigate here how you can utilize and import a class from one module into another. In this scenario, the Ride class represents a specific ride requested by a Passenger and assigned to a Driver. The Passenger class represents a user who can request rides, cancel rides, and rate drivers. The Driver class represents a driver who can accept ride requests, complete rides, and view their ride history.

The classes interact with each other to facilitate the rideshare functionality. For example, when a Passenger requests a ride, a new Ride instance is created, and an available Driver is assigned to the ride. The Driver then accepts the ride, completes it, and the Passenger can rate the Driver after the ride ends.

This is a simplified scenario in that we won’t be writing the internal code within the classes to accomplish all of the above functionality just practicing defining the classes and creating instances. In a real-world implementation, there would be additional attributes, methods, and interactions between the classes to handle various aspects of the rideshare program, such as payment processing, location tracking, and user authentication.

### Resources

* Python or Jupyter Notebook

### Instructions

### Part 1: Classes

You're about to create your first package with class definitions! You've already seen how to import packages such as NumPy and Pandas, and you can organize your own code in a similar manner. Let’s create a folder for this lab where your files will live. Once the folder is created you can begin creating some classes within Python files.

1. Create a Python file ride.py and inside of it define the Ride class. We won’t give it any code internally so make sure to use pass.
2. Create a separate Python file driver.py and define a Driver class the same way.  
   By convention, Python programmers use CamelCase to name the class. Also, you can't create an "empty" class. At the least, you need to specify the pass keyword to ensure the class definition is syntactically valid.
3. In a new file (either Python or Jupyter notebook) within your folder you can import the classes from those files. Name this file whatever you want. For example, once you define the Ride class in a file ride.py, you can then import said code in another notebook or script using:  

   ```
   # Import the entire file  
   import ride
   ```

   ```
   # Import only the Ride class  
   from ride import Ride
   ```

   In addition to the ride.py file, you have also created another file driver.py that contains the Driver class. Go ahead and import that class into your file as well.
4. Create a Passenger class that doesn't contain anything within your new file.

### Part 2: Instances

Now practice using these classes to create instances.

1. First, make two instances of the Passenger class and assign them to the variables meryl and daniel, respectively. You can use the starter code below and replace None with the appropriate code.  

   ```
   # Two instances of the Passenger class  
   meryl = None  
   daniel = None  
     
   print(meryl)  
     
   print(daniel)
   ```
2. Next, make one instance of the Driver class and assign it to the variable, flatiron\_taxi  

   ```
   # One instance of the Driver class  
   flatiron_taxi = None  
   print(flatiron_taxi)
   ```
3. Finally, make two instances of the Ride class and assign them to ride\_to\_school and ride\_home.  

   ```
   # Two instances of the Ride class  
   ride_to_school = None  
   ride_home = None  
     
   print(ride_to_school)  
     
   print(ride_home)
   ```

### Solution

### Select for Solution

#### Part 1: Classes

1. ride.py file:

```
# Define the ride clase  
class Ride:  
    pass
```

1. driver.py file:

```
# Define the driver class  
class Driver:  
    pass
```

1. New file (notebook or Python)

```
# Import the entire file  
import ride  
  
# Import only the Ride class  
from ride import Ride
```

In addition to the ride.py file, we also created another file driver.py that contains the Driver class.

```
# Import only the Driver class  
from driver import Driver
```

By convention, Python programmers use CamelCase to name the class. Also, you can't create an "empty" class. At the least, you need to specify the pass keyword to ensure the class definition is syntactically valid.

1. Create a Passenger class that doesn't contain anything in the following cell:

```
# Create Passenger class  
class Passenger:  
    pass
```

#### Part 2: Instances

1. Make two instances of the Passenger class and assign them to the variables meryl and daniel, respectively.

```
# Two instances of the Passenger class  
meryl = Passenger()  
daniel = Passenger()  
  
print(meryl)  
print(daniel)
```

**Output:**

```
<__main__.Passenger object at 0x10814d3c8>  
<__main__.Passenger object at 0x10814d390>
```

1. Make one instance of the Driver class and assign it to the variable, flatiron\_taxi.

```
 # One instance of the Driver class  
flatiron_taxi = Driver()  
print(flatiron_taxi)
```

**Output:**

```
<driver.Driver object at 0x10814d4e0>
```

1. Make two instances of the Ride class and assign them to ride\_to\_school and ride\_home.

```
# Two instances of the Ride class  
ride_to_school = Ride()  
ride_home = Ride()  
  
print(ride_to_school)  
print(ride_home)
```

**Output:**

```
<ride.Ride object at 0x10814d908>  
<ride.Ride object at 0x10814d8d0>
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243645

Scraped At: 2026-05-14T21:02:33.032807
