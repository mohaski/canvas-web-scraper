# Introduction to Object-Oriented Programming (OOP)

# Introduction to Object-Oriented Programming (OOP)

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Introduction to Object-Oriented Programming (OOP)

Icon Progress Bar (browser only)

7 min read

![OOP example with a dog: showing its class, objects, attributes, and methods](https://moringa.instructure.com/courses/1406/files/625083/download)
**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around objects, which are instances of classes. It focuses on creating reusable code structures and promotes code modularity, making it easier to maintain and extend software systems.

OOP languages, such as Java, C++, Python, and C#, provide mechanisms to implement these concepts. By utilizing OOP principles, developers can create modular, reusable, and maintainable code, making it easier to develop and modify large-scale software systems. OOP also promotes collaboration among developers, as different parts of the system can be developed independently and integrated later.

Object-oriented programming (OOP) is one of several high-level ways to structure and conceptualize computer programs, called *programming paradigms*. OOP treats all creations of code as objects, with specific methods and attributes that describe what an object can do and how it can be used in a program. Python is primarily an object-oriented programming language, although it can be used with other paradigms in mind.

### Programming Paradigms

**Programming paradigms** are formal approaches for structuring code to achieve the desired results.

#### Why Do We Need Them?

For very simple programming tasks, there is essentially only one "correct" way to structure the code. For example, if you needed to print the string "Hello, world!", this is how you would do it:

```
print("Hello, world!")
```

```
Hello, world!
```

But once your code starts to get more complex, the structure gets less intuitive and obvious. For example, if you needed to reshape some data then display a bar graph, or fit a model then use it to make predictions, how would you design that?

Deciding on a paradigm and sticking to it helps to guide your code design choices, and helps others to understand what your code is doing.

### [Procedural Programming](#dpPanel0)

The oldest (and probably most intuitive) modern programming paradigm is procedural programming. This involves writing a series of sequential steps to be executed, possibly with the use of techniques for **control flow** (i.e., `if` statements) and **modular procedures** (i.e., functions).

Data science code written in a **notebook** is almost always following a procedural programming paradigm. It is useful for telling a story with a single thread, but less useful for building libraries or software that runs without human intervention. Once code starts to get more complicated, we start incorporating more complicated paradigms like functional programming or OOP.

### [Functional Programming](#dpPanel1)

"Purely functional" programming, using a language like Haskell or Clojure, means that procedural programming is abandoned entirely*—*rather than a series of steps, the program consists only of functions, which in turn can be composed of functions or apply functions.

In the development of data science libraries, developers tended not to use purely functional programming, but still incorporated some functional principles.

For example, here is the functional interface to Matplotlib:

```
import matplotlib.pyplot as plt  
  
plt.figure()  
plt.bar(range(5), [3, 4, 4, 7, 8])  
plt.title("My Graph")  
plt.xlabel("x Label")  
plt.ylabel("y Label");
```

![Example functional interface graph for Matplotlib](https://moringa.instructure.com/courses/1406/files/625160/download)

Note that we created this graph without instantiating any variables. We just imported the library, then called a series of functions to create the desired graph. We could rewrite that code snippet like this, to make that aspect even clearer:

```
from matplotlib.pyplot import figure, bar, title, xlabel, ylabel  
  
figure()  
bar(range(5), [3, 4, 4, 7, 8])  
title("My Graph")  
xlabel("x Label")  
ylabel("y Label");
```

![Example Functional Interface Graph for Matplotlib with variables](https://moringa.instructure.com/courses/1406/files/625029/download)

This approach is still preferred by some "old school" data science practitioners, but it has some issues.

It uses **global variables**, which can get messy as code gets more complex. When the `title()` function is called in the above snippet, for example, the internal logic first has to find the current global axis object, then apply the label to that object. For a programmer to understand what axes object that is, they would need to closely follow the steps of the code, since there is no unique variable assigned to it. With no variable assigned, that also means that the code is less flexible and steps must be performed **one at a time**.

### [Object-Oriented Programming (OOP)](#dpPanel2)

Object-oriented programming takes these global variables and functions and makes them into "member variables" (AKA **attributes**) and "member functions" (AKA **methods**). This allows code to be more organized and clear.

For example, in the previous functional Matplotlib example, you might ask *What is* `title()` *being called on? Is it the figure or the axes?*

To answer this, we could look at the [Matplotlib source code


Links to an external site.](https://github.com/matplotlib/matplotlib/blob/v3.5.1/lib/matplotlib/pyplot.py#L3024-L3027), which shows this:

```
def title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs):  
    return gca().set_title(  
        label, fontdict=fontdict, loc=loc, pad=pad, y=y, **kwargs)
```

`gca()` means "get current axes", so we can tell that this is being applied to the axes.

Or, if we use the object-oriented Matplotlib interface instead, the answer becomes much clearer, just by looking at our code:

```
import matplotlib.pyplot as plt  
# OOP interface  
fig, ax = plt.subplots() # Creates fig, and ax variables  
ax.bar(range(5), [3, 4, 4, 7, 8])  
ax.set_title("My Graph")  
ax.set_xlabel("x Label")  
ax.set_ylabel("y Label");
```

![Example graph showing oop Matplotlib results with axes](https://moringa.instructure.com/courses/1406/files/625103/download)

As you can see, the title is being applied to the axes, not the figure. We can tell because the method call is structured like `ax.<method name>()` and `ax` is our axes variable.

A key takeaway here is that **you can often do the exact same thing using different paradigms**. They are just different approaches to structuring code, and different people might prefer different approaches.

### Industry Example

OOP is one of the dominant programming paradigms. Take a look at this chart of the most in-demand programming languages (as of 2022):

![Chart of the most in-demand programming languages of 2022](https://moringa.instructure.com/courses/1406/files/625231/download)

The top five in this list*—*Python Java, JavaScript, C++, C#*—*plus Ruby, are mostly or entirely OOP, while PHP and Perl have been adding OOP-style functionality in their latest versions. Knowing OOP will help you become comfortable reading other people's code, an essential part of working in a data or software engineering environment.

#### Example:

A data scientist working for an e-commerce company is tasked with building a recommendation system that suggests products to customers based on their browsing and purchase history.

The data scientist decides to use OOP to design and implement the recommendation system. Here's how they might approach it:

1. **Creating a Customer Class:**  
   1. The data scientist creates a Customer class that represents a customer of the e-commerce platform.
   2. The Customer class has attributes such as customer\_id, name, email, purchase\_history, and browsing\_history.
   3. The class also has methods like add\_purchase() and add\_browsed\_item() to update the customer's purchase and browsing history.
2. **Creating a Product Class:**  
   1. The data scientist creates a Product class that represents a product available on the e-commerce platform.
   2. The Product class has attributes such as product\_id, name, description, price, and category.
   3. The class also has methods like get\_details() to retrieve product information.
3. **Creating a Recommendation Class**:  
   1. The data scientist creates a Recommendation class that encapsulates the logic for generating product recommendations.
   2. The Recommendation class has methods like get\_collaborative\_recommendations() and get\_content\_based\_recommendations() that implement different recommendation algorithms.
   3. These methods take a Customer object as input and return a list of recommended Product objects based on the customer's purchase and browsing history.
4. **Utilizing Inheritance:**  
   1. The data scientist realizes that there are different types of customers, such as regular customers and premium customers.
   2. They create a PremiumCustomer class that inherits from the Customer class and adds additional attributes and methods specific to premium customers, such as loyalty\_points and get\_discount().
5. **Implementing the Recommendation System:**  
   1. The data scientist instantiates Customer objects for each customer in the database, populating their purchase and browsing history.
   2. They also instantiate Product objects for each product in the catalog.
   3. When a customer visits the e-commerce website, the system retrieves their Customer object and passes it to the Recommendation class to generate personalized product recommendations.
   4. The recommended Product objects are then displayed to the customer on the website.

By using OOP, the data scientist can create modular and reusable code components. The Customer, Product, and Recommendation classes encapsulate specific functionalities and can be easily extended or modified as needed. The use of inheritance allows for the creation of specialized customer types without duplicating code.

This scenario demonstrates how a data scientist can leverage OOP principles to design and implement a recommendation system in a structured and maintainable way, making it easier to update and scale the system as the e-commerce platform grows.

### Learning Outcomes

After completing this lesson, you should be able to:

* Explain the utility of the object-oriented programming paradigm.
* Implement and instantiate classes in Python.
* Explain the value of code abstraction and DRY code.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243636

Scraped At: 2026-05-14T21:01:47.500620
