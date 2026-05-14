# Technical Lesson: Inheritance

# Technical Lesson: Inheritance

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Inheritance

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[30-60 minutes]

![The Beatles band wall art outlines of each member and filled in a different color](https://moringa.instructure.com/courses/1406/files/625184/download)
In this lesson, you'll learn about how you can use inheritance to create relationships between Superclasses and Subclasses to further save you from writing redundant code.

### Writing D.R.Y. code

Assume that you are going to build a data model around one of the most popular bands of the last century, the Beatles!

Using the skills you've learned so far, you could absolutely create classes for each of the different roles in the band. If you created a class for each different musician, it would probably look something like this:

```
class Drummer(object):  
      
    def __init__(self):  
        self.name = "Ringo"  
        self.role = "Drummer"  
      
    def tune_instrument(self):  
        #some code  
        pass  
      
    def practice(self):  
        # some code  
        pass  
      
    def perform(self):  
        #some code  
        pass  
      
class Singer(object):  
      
    def __init__(self):  
        self.name = "John"  
        self.role = "Singer"  
          
    def tune_instrument(self):  
        # some code  
        pass  
      
    def practice(self):  
        # some code  
        pass  
      
    def perform(self):  
        # some code  
        pass  
      
# Class Guitarist code...  
  
  
# Class Bass_Guitarist code...
```

If you're thinking about what it would be like to write this code, the first thing you'll notice is probably that there's a lot of redundant code that you can fill in using copy and paste. If this makes you nervous, it should*—*copying and pasting is usually a sign that your program can be improved. After all, good programmers are lazy!

> "I will always choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it." - Bill Gates

Good programmers try to follow the D.R.Y. rule (Don't Repeat Yourself). In the example above, you have to type the same lines of code over and over again*—*the attributes in each class, the same method names (even though the bodies of the functions will likely be different), again and again. This violates the D.R.Y. rule. Luckily, we can restructure our code in an intelligent way that will allow us to accomplish the same thing without repeating everything by using Inheritance.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of inheritance.

[VIDEO LINK](https://player.vimeo.com/video/995574570?h=eb40a453ea)

### Instructions

* [Step 1: Basic Inheritance](#dpPanel0Content)
* [Step 2: Changing Methods/Attributes with Inheritance](#dpPanel1Content)
* [Step 3: Further Abstraction](#dpPanel2Content)

### Step 1: Basic Inheritance

The Guitarist class and the Bass\_Guitarist class are extremely similar. In fact, we could say that bass guitarists are a special case of guitarists. With a few notable exceptions, the Bass\_Guitarist class is generally going to be more similar than different to the Guitarist class.

In Python, we can make Bass\_Guitarist a subclass of Guitarist. This will mean that the Bass\_Guitarist class will inherit the attributes and methods of its superclass, Guitarist. This will save us a lot of redundant code.

See the example in the cell below.

```
# Define the base/parent/super class  
class Guitarist(object):  
    def __init__(self, name):  
        self.name = name  
        self.role = 'Guitarist'  
        self.instrument_type = 'Stringed Instrument'  
          
    def tune_instrument(self):  
        print('Tune the strings!')  
          
    def practice(self):  
        print('Strumming the old 6 string!')  
          
    def perform(self):  
        print('Hello, New  York!')  
  
# Pass the base class as arugment to the child class for inheritance          
class Bass_Guitarist(Guitarist):  
    pass  
  
george = Guitarist('George')  
paul = Bass_Guitarist('Paul')  
print(george.instrument_type)  
print(paul.instrument_type)
```

**Output:**

```
Stringed Instrument  
Stringed Instrument
```

```
george.tune_instrument()  
paul.tune_instrument()
```

**Output:**

```
Tune the strings!  
Tune the strings!
```

```
george.practice()  
paul.practice()
```

**Output:**

```
Strumming the old 6 string!  
Strumming the old 6 string!
```

```
george.perform()  
paul.perform()
```

**Output:**

```
Hello, New  York!  
Hello, New  York!
```

Take a look at the way the classes were created and the corresponding outputs in the cells above. A few things stand out:

* The .tune\_instrument() method was never declared for class Bass\_Guitarist(), but the paul instance still has access to this method.
* The .instrument\_type attribute was never set for the Bass\_Guitarist() class, but the paul instance nonetheless has that attribute, and the attribute has the same value as it had in the Guitarist class. This is because it inherited it from the Guitarist() calls through the super().\_\_init\_\_() method first.
* With inheritance, you can still change or overwrite specific attributes or methods. Let’s take this example and further improve it by changing the role and some of the methods.

### Step 2: Changing Methods/Attributes with Inheritance

Let’s take the existing code using basic inheritance above and modify it slightly to improve our subclass. The Bass\_Guitarist should have a different role, “Bass Guitarist”, and also contain a new attribute called string\_type which should equal “bass”. Go ahead and change the practice and perform methods as well by redefining them in the new subclass. It should still inherit from the Guitarist class defined above.

```
class Bass_Guitarist(Guitarist):  
    
   def __init__(self, name):  
       super().__init__(name)  
       self.role = 'Bass Guitarist'  
       self.string_type = 'bass'  
    
   def practice(self):  
       print('I play the Seinfeld theme song when I practice!')  
        
   def perform(self):  
       super().perform()  
       print('This is the bass line!')  
  
  
george = Guitarist('George')  
paul = Bass_Guitarist('Paul')  
print(george.string_type)  
print(paul.string_type)
```

**Output:**

```
AttributeError: 'Guitarist' object has no attribute 'string_type'  
bass
```

#### Using .super()

The super() method gives you access to the superclass of the object that calls super(). In this case, you saw how super() was used in the \_\_init\_\_() method to initialize the object just as if we were creating a new guitar object. Afterward, you can modify attributes as needed. It is worth noting that you can also add attributes and methods to a subclass that a superclass does not have. For instance, we added the attribute self.string\_type = 'bass' inside the Bass\_Guitarist.\_\_init\_\_() method, all bass guitarist objects would have that attribute, but guitarist objects would not. Conversely, any changes that you make to the superclass Guitarist() will always be reflected in the subclass Bass\_Guitarist().

#### Changing Values and Methods

Note that in both of these classes, you have methods named .practice() and .perform() that have the same name, but different behaviors. This is an example of Polymorphism, meaning that you can have methods that have the same name, but contain different code inside their bodies. This is not a naming collision because these methods exist attached to different classes.

```
george.perform()  
paul.perform()
```

**Output:**

```
Hello, New  York!  
  
Hello, New  York!  
This is the bass line!
```

Also, take note of the way the .perform() method is written inside of Bass\_Guitarist(). If you want a method in a subclass to do everything that method does in a superclass and then do something else, you can accomplish this by simply calling the superclass's version of the method by accessing it with super() and then adding any remaining behavior afterward in the body of the function. In this case Paul, our Bass\_Guitarist, prints out the original perform message “Hello, New York!” just like George but continues into the next statement as well to print “This is the bass line!”.

#### Abstract Superclasses

When you make use of a subclass and a superclass, you are defining levels of Abstraction. In this case, the superclass Guitarist() is one level of abstraction higher than the subclass Bass\_Guitarist(). Intuitively, this makes sense*—*bass guitarists are a kind of guitarist, but not all guitarists are bass guitarists.

It's also worth noting that you can always go a level of abstraction higher by defining a class that is more vague but still captures the common thread amongst the subclasses. Here's an example to demonstrate. Think back to the defining process for inheritance.

1. Identify common attributes and behaviors among related classes.
2. Create a base class that encapsulates the common attributes and behaviors.
3. Define the derived classes that inherit from the base class.
4. Use the super() function in the derived classes to call the base class's constructor and methods if you want to modify them.
5. Add specific attributes and methods to the derived classes as needed.
6. Use polymorphism to treat objects of the derived classes as objects of the base class when appropriate.

At first glance, it may seem that guitarists, singers, and drummers don't have enough in common with each other to make use of inheritance*—*a drummer is not a type of singer, etc. However, one thing they all have in common is they are all a type of Musician(). No matter what sort of musician you are, you:

* have a name
* have an instrument
* know how to tune\_instrument
* can practice and perform

In this way, you can write a single superclass that will be useful for all of the subclasses in our band: Drummer(), Guitarist(), Bass\_Guitarist(), and Singer() are all types of musicians!

This is called an *Abstract Superclass*. The superclass being used is at a level of abstraction where it does not make sense for it to exist on its own. For example, it makes sense to instantiate drummers, singers, and guitarists*—*they are members of a band, and by playing these instruments, they are musicians.

However, you cannot be a musician without belonging to one of these subclasses*—*there is no such thing as a musician that doesn’t play any instruments or sing! It makes no sense to instantiate a Musician(), because they don't really exist in the real world*—*you only create this *Abstract Superclass* to define the commonalities between our subclasses and save ourselves some redundant code.

#### Creating The Beatles Using an Abstract Superclass

The cell below models the Beatles by making use of the abstract superclass Musician(), and then subclassing it when creating Drummer(), Singer(), and Guitarist(). Note that since you can have multiple layers of abstraction, it makes sense to keep Bass\_Guitarist() as a subclass of Guitarist().

```
class Musician(object):  
      
    def __init__(self, name):  
        self.name = name  
        self.band = "The Beatles"  
      
    def tune_instrument(self):  
        print("Tuning Instrument!")  
      
    def practice(self):  
        print("Practicing!")  
          
    def perform(self):  
        print("Hello New York!")  
          
class Singer(Musician):  
      
    def __init__(self, name):  
        super().__init__(name)  
        self.role = "Singer"  
          
    def tune_instrument(self):  
        print("No tuning needed -- I'm a singer!")  
      
class Guitarist(Musician):  
      
    def __init__(self, name):  
        super().__init__(name)  
        self.role = "Guitarist"  
          
    def practice(self):  
        print("Strumming the old 6 string!")  
          
class Bass_Guitarist(Guitarist):  
      
    def __init__(self, name):  
        super().__init__(name)  
        self.role = "Bass Guitarist"  
          
    def practice(self):  
        print("I play the Seinfeld Theme Song when I get bored")  
          
    def perform(self):  
        super().perform()  
        print("Thanks for coming out!")  
          
class Drummer(Musician):  
      
    def __init__(self, name):  
        super().__init__(name)  
        self.role = "Drummer"  
          
    def tune_instrument(self):  
        print('Where did I put those drum sticks?')  
          
    def practice(self):  
        print('Why does my chair still say "Pete Best"?')  
  
  
john = Singer('John Lennon')  
paul = Bass_Guitarist('Paul McCartney')  
ringo = Drummer('Ringo Starr')  
george = Guitarist('George Harrison')  
  
  
the_beatles = [john, ringo, george, paul]  
for musician in the_beatles:  
    print('{} is the {}!'.format(musician.name, musician.role))
```

**Output:**

```
John Lennon is the Singer!  
Ringo Starr is the Drummer!  
George Harrison is the Guitarist!  
Paul McCartney is the Bass Guitarist!
```

```
for musician in the_beatles:  
    musician.tune_instrument()
```

**Output:**

```
No tuning needed--I'm a singer!  
Where did I put those drum sticks?  
Tuning Instrument!  
Tuning Instrument!
```

```
for musician in the_beatles:  
    musician.practice()
```

**Output:**

```
Practicing!  
Why does my chair still say "Pete Best"?  
Strumming the old 6 string!  
I play the Seinfeld Theme Song when I get bored
```

```
for musician in the_beatles:  
    musician.perform()
```

**Output:**

```
Hello New York!  
Hello New York!  
Hello New York!  
Hello New York!  
Thanks for coming out
```

### Considerations

When applying inheritance in OOP, there are several common challenges and considerations to keep in mind:

1. **Overusing Inheritance:**  
   * Challenge: Inheritance can be overused or misused, leading to complex and deeply nested class hierarchies. This can make the codebase harder to understand, maintain, and modify.
   * Solution: Use inheritance judiciously and only when there is a clear "is-a" relationship between classes. Consider alternative approaches like composition or mixins when inheritance is not the best fit.
2. **Incorrectly Modeling Relationships:**  
   * Challenge: Incorrectly identifying the relationships between classes can lead to improper use of inheritance. If the relationship is not truly an "is-a" relationship, inheritance may not be the appropriate choice.
   * Solution: Carefully analyze the relationships between classes and ensure that inheritance is used only when the derived class is a specialized version of the base class. If the relationship is more of a "has-a" or "uses-a" relationship, composition or other design patterns might be more suitable.
3. **Tightly Coupled Classes:**  
   * Challenge: Inheritance can create tight coupling between the base class and its derived classes. Changes made to the base class can potentially affect all the derived classes, making the system less flexible and harder to modify.
   * Solution: Strive for loose coupling by using inheritance sparingly and favoring composition when possible. Use interfaces or abstract base classes to define common behavior without tightly coupling the implementation details.
4. **Liskov Substitution Principle (LSP) Violation:**  
   * Challenge: The LSP states that objects of a derived class should be able to replace objects of the base class without affecting the correctness of the program. Violating the LSP can lead to unexpected behavior and design flaws.
   * Solution: Ensure that derived classes adhere to the contract defined by the base class. Derived classes should not alter the behavior of inherited methods in a way that violates the expectations of the base class. Use inheritance only when the derived classes truly specialize the behavior of the base class.
5. **Multiple Inheritance Complexity:**  
   * Challenge: Multiple inheritance, where a class inherits from multiple base classes, can introduce complexity and potential issues like the "diamond problem" (ambiguity when inheriting from multiple paths).
   * Solution: Use multiple inheritance cautiously and only when necessary. Consider alternative approaches like composition or mixins to achieve code reuse and modularity. If multiple inheritance is used, be aware of the potential complications and design the class hierarchy carefully to avoid ambiguity.

### Pros and Cons of Inheritance

#### Pros

* **Code Reuse:** Inheritance allows for code reuse by inheriting common attributes and methods from the base class, reducing duplication and promoting consistency.
* **Extensibility:** Inheritance enables the creation of specialized classes based on existing classes, facilitating the extension and customization of functionality.
* **Polymorphism:** Inheritance supports polymorphism, allowing objects of derived classes to be treated as objects of the base class, enabling flexible and dynamic behavior.

#### Cons

* **Tight Coupling:** Inheritance can create tight coupling between classes, making the system less flexible and harder to modify. Changes to the base class can propagate to the derived classes.
* **Complexity:** Overusing inheritance or creating deep inheritance hierarchies can lead to increased complexity, making the codebase harder to understand and maintain.
* **Fragile Base Class Problem:** Modifying the base class can potentially break the derived classes, especially if the changes alter the expected behavior or interface.

When deciding whether to use inheritance, consider the following:

* Is there a clear "is-a" relationship between the classes?
* Will inheritance provide significant code reuse and promote consistency?
* Can the derived classes substitute the base class without violating the LSP?
* Is the resulting class hierarchy manageable and maintainable?

If the answer to these questions is yes, inheritance can be a powerful tool. However, if inheritance introduces more complexity than benefits, alternative approaches like composition or mixins should be considered.

**Summary:**

By considering these challenges, pros and cons, and design decisions, you can make informed choices when working with OOP methods, attributes, and the \_\_init\_\_ method. It's important to strike a balance between encapsulation, flexibility, and maintainability to create well-structured and robust classes.

Remember, these are general guidelines, and the specific decisions you make may vary depending on your project requirements and the problem domain you're working with.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243665

Scraped At: 2026-05-14T21:04:08.391564
