# Practice: Inheritance

# Practice: Inheritance

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Practice: Inheritance

Icon Progress Bar (browser only)

*​*

Estimated completion time: 30-60 minutes

Consider the following scenario: You've been hired by a zookeeper to build a program that keeps track of all the animals in the zoo. This is a great opportunity to make use of inheritance and object-oriented programming.

Remember our process for inheritance:

1. 1. Identify common attributes and behaviors among related classes.
   2. Create a base class that encapsulates the common attributes and behaviors.
   3. Define the derived classes that inherit from the base class.
   4. Use the super() function in the derived classes to call the base class's constructor and methods if you want to modify them.
   5. Add specific attributes and methods to the derived classes as needed.
   6. Use polymorphism to treat objects of the derived classes as objects of the base class when appropriate.

**Objective:** By completing this practice exercise, you will create a domain model using OOP and use inheritance to write non redundant code.

### Resources

* Python or Jupyter Notebook

### Instructions

Remember to implement the methods according to the provided instructions and test your code thoroughly. Feel free to add more attributes or methods to the Student class as needed, such as a method to update the student's major or year of study.

### Step 1: Create an Abstract Superclass

In a Python or Jupyter notebook file, start by creating an abstract superclass, Animal(). When your program is complete, all subclasses of Animal() will have the following attributes:

* name, which is a string set at instantiation time
* size, which can be 'small', 'medium', 'large', or 'enormous'
* weight, which is an integer set at instantiation time
* species, a string that tells us the species of the animal
* food\_type, which can be 'herbivore', 'carnivore', or 'omnivore'
* nocturnal, a boolean value that is True if the animal sleeps during the day, otherwise False

They'll also have the following behaviors:

* sleep, which prints a string saying if the animal sleeps during day or night
* eat, which takes in the string 'plants' or 'meat', and returns '{animal name} the {animal species} thinks {food} is yummy!' or 'I don't eat this!' based on the animal's food\_type attribute

NOTE: For some attributes in an abstract superclass such as size, the initial value doesn't matter*—*just make sure that you remember to override it in each of the subclasses! Here is some provided starter code.

```
class Animal(object):  
    None
```

### Step 2: Build Out Specific Classes

Now that you have your abstract superclass, begin building out the specific animal classes.

In the same file, complete the Elephant() class. This class should:

* Inherit from Animal
* Have a species of 'elephant'
* Have a size of 'enormous'
* Have a food type of 'herbivore'
* Set nocturnal to False

Hint: Remember to make use of .super() during initialization, and be sure to pass in the values it expects at instantiation time!

```
class Elephant(Animal):  
    None
```

Now create a Tiger() class. This class should:

* Inherit from Animal
* Have a species of 'tiger'
* Have a size of 'large'
* Have a food type of 'carnivore'
* Set nocturnal to True

```
class Tiger(Animal):  
    None
```

In the cell below, create a Raccoon() class. This class should:

* Inherit from Animal
* Have a species of raccoon
* Have a size of 'small'
* Have a food type of 'omnivore'
* Set nocturnal to True

```
class Raccoon(Animal):  
    None
```

Finally, create a Gorilla() class. This class should:

* Inherit from Animal
* Have a species of gorilla
* Have a size of 'large'
* Have a food type of 'herbivore'
* Set nocturnal to False

```
class Gorilla(Animal):  
    None
```

### Step 3: Create the Objects

Now it's time to populate the zoo. To ease the creation of animal instances, create a function add\_animal\_to\_zoo(). This function should take in the following parameters:

* zoo, an array/list representing the current animals in the zoo
* animal\_type, a string. Can be 'Gorilla', 'Raccoon', 'Tiger', or 'Elephant'
* name, the name of the animal being created
* weight, the weight of the animal being created

The function should then:

* use animal\_type to determine which object to create
* Create an instance of that animal, passing in the name and weight
* Append the newly created animal instance object to zoo
* Return zoo

```
def add_animal_to_zoo(zoo, animal_type, name, weight):  
    pass
```

Now, add some animals to your zoo.

Create the following animals and add them to your zoo. The names and weights are up to you.

* 2 Elephants
* 2 Raccoons
* 1 Gorilla
* 3 Tigers

### Step 4: Use the Objects

Now that you have a populated zoo, you can do what the zookeeper hired you to do*—*write a program that feeds the correct animals the right food at the right times.

To do this, write a function called feed\_animals(). This function should take in two arguments:

* zoo, the zoo array containing all the animals
* time, which can be 'Day' or 'Night'. This should default to day if nothing is entered for time

This function should:

* Feed only the non-nocturnal animals if time='Day', or only the nocturnal animals if time='Night'
* Check the food type of each animal before feeding. If the animal is a carnivore, feed it 'meat'; otherwise, feed it 'plants'. Feed the animals by using their .eat() method

```
def feed_animals(zoo, time='Day'):  
    pass
```

Now, test out your program. Call the function for a daytime feeding. If the elephants and gorillas were fed then things should be good.

Next, call feed\_animals() again, but this time set time='Night'

That's it! You've used OOP and inheritance to build a working program to help the zookeeper feed his animals with the right food at the correct times.

### Solution

### Select for Solution

#### Step 1: Create an Abstract Superclass

Create an abstract superclass, Animal():

```
class Animal(object):  
      
    def __init__(self, name, weight):  
        self.name = name  
        self.weight = weight  
        self.species = None  
        self.size = None  
        self.food_type = None  
        self.nocturnal = False  
          
    def sleep(self):  
        if self.nocturnal:  
            print("{} sleeps during the day!".format(self.name))  
        else:  
            print("{} sleeps during the night!".format(self.name))  
              
    def eat(self, food):  
        if self.food_type == 'omnivore':  
            print("{} the {} thinks {} is Yummy!".format(self.name, self.species, food))  
        elif (food == 'meat' and self.food_type == "carnivore") or (food == 'plants' and self.food_type == 'herbivore'):  
            print("{} the {} thinks {} is Yummy!".format(self.name, self.species, food))  
        else:  
            print("I don't eat this!")
```

#### Step 2: Build Out Specific Classes

Elephant subclass:

```
class Elephant(Animal):  
      
    def __init__(self, name, weight):  
        super().__init__(name, weight)  
        self.size = 'enormous'  
        self.species = 'elephant'  
        self.food_type = 'herbivore'  
        self.nocturnal = False
```

Tiger subclass:

```
class Tiger(Animal):  
      
    def __init__(self, name, weight):  
        super().__init__(name, weight)  
        self.size = 'large'  
        self.species = 'tiger'  
        self.food_type = 'carnivore'  
        self.nocturnal = True
```

Raccoon subclass:

```
class Raccoon(Animal):  
      
    def __init__(self, name, weight):  
        super().__init__(name, weight)  
        self.size = 'small'  
        self.species = 'raccoon'  
        self.food_type = 'omnivore'  
        self.nocturnal = True
```

Gorilla subclass:

```
class Gorilla(Animal):  
      
    def __init__(self, name, weight):  
        super().__init__(name, weight)  
        self.size = 'large'  
        self.species = 'gorilla'  
        self.food_type = 'herbivore'  
        self.nocturnal = False
```

#### Step 3: Create the Objects

 Function to create animals in zoo using the different classes:

```
def add_animal_to_zoo(zoo, animal_type, name, weight):  
    animal = None  
    if animal_type == 'Gorilla':  
        animal = Gorilla(name, weight)  
    elif animal_type == 'Raccoon':  
        animal = Raccoon(name, weight)  
    elif animal_type == 'Tiger':  
        animal = Tiger(name, weight)  
    else:  
        animal = Elephant(name, weight)  
      
    zoo.append(animal)  
      
    return zoo
```

 Populate the zoo with the requested animals:

```
to_create = [{'Type': 'Elepant', 'name': 'Joe', 'weight': 200},   
 {'Type': 'Elepant', 'name': 'Tim', 'weight': 220},  
 {'Type': 'Raccoon', 'name': 'Dan', 'weight': 30},  
 {'Type': 'Raccoon', 'name': 'Roxy', 'weight': 40},  
 {'Type': 'Gorilla', 'name': 'Kim', 'weight': 130},  
 {'Type': 'Tiger', 'name': 'Bob', 'weight': 70},  
 {'Type': 'Tiger', 'name': 'Fred', 'weight': 90},  
 {'Type': 'Tiger', 'name': 'Molly', 'weight': 85}]  
  
   
  
  
zoo = []  
  
   
  
  
for animal in to_create:  
    zoo = add_animal_to_zoo(zoo, animal['Type'], animal['name'], animal['weight'])  
      
zoo
```

#### Step 4: Use the Objects

Function to feed the animals:

```
def feed_animals(zoo, time='Day'):  
    for animal in zoo:  
        if time == 'Day':  
            # CASE: Daytime feeding -- Only feed the animals that aren't nocturnal  
            if animal.nocturnal == False:  
                # If the animal is a carnivore, feed it "meat".  Otherwise, feed it "plants"  
                if animal.food_type == 'carnivore':  
                    animal.eat('meat')  
                else:  
                    animal.eat('plants')  
        else:  
            # CASE: Night-time feeding -- feed only the nocturnal animals!   
            if animal.nocturnal == True:  
                if animal.food_type == 'carnivore':  
                    animal.eat('meat')  
                else:  
                    animal.eat('plants')
```

```
feed_animals(zoo, time='Day')
```

```
Joe the elephant thinks plants is Yummy!  
Tim the elephant thinks plants is Yummy!  
Kim the gorilla thinks plants is Yummy!
```

```
feed_animals(zoo, time='Night')
```

```
Dan the raccoon thinks plants is Yummy!  
Roxy the raccoon thinks plants is Yummy!  
Bob the tiger thinks meat is Yummy!  
Fred the tiger thinks meat is Yummy!  
Molly the tiger thinks meat is Yummy!
```

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243666

Scraped At: 2026-05-14T21:04:14.620592
