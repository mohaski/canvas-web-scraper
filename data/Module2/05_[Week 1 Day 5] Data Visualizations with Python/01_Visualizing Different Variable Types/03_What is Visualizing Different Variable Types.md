# What is Visualizing Different Variable Types?

# What is Visualizing Different Variable Types?

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) What is Visualizing Different Variable Types?

Icon Progress Bar (browser only)

4 min read

### Visualizing Numeric Variables

Numeric variables can be either continuous or discrete.

**Continuous numeric variables** represent quantities that can take on any value within a specific range. Imagine a Number Line: Think of a ruler stretching infinitely in both directions. Any point on that ruler represents a possible value for a continuous variable.

**Discrete numeric variables** represent whole numbers that can be counted and have distinct, separate values. Imagine Counting Objects: Think of counting apples in a basket. You can have 0 apples, 1 apple, 2 apples, and so on. There are no "in-between" values like 1.5 apples.

Below are two images to represent the two types of numeric variables*—*Continuous (on the left) and Discrete (on the right). Notice how the continuous numeric variable of weight is easier to visualize in scatter plot form, whereas the categorical variable model year is harder to interpret. This will be important to note later on in this module when we discuss using specific visuals for specific variable types.

![Side-by-side example of continuous and discrete numeric variables in scatter plot form](https://moringa.instructure.com/courses/1406/files/625127/download)

#### Visualizing Categorical Variables

Categorical variables can actually be strings or numbers.

String categorical variables will be fairly obvious due to their data type. For example, the type of pizza\_topping is a categorical variable represented by text. Notice how the x-axis uses the actual word and not a coded number.

![Example of string categorical variables using a bar chart mapping a count of pizza toppings.](https://moringa.instructure.com/courses/1406/files/625158/download)

Numeric categorical variables can still be visualized using a bar chart. In the pizza\_topping example above, we can code Pepperoni as 1, Cheese as 2, and so forth. Notice the bar heights do not change, just the x-axis labels:

![Example of numeric categorical variables using a bar chart mapping a count of pizza toppings.](https://moringa.instructure.com/courses/1406/files/625117/download)

### How Does Visualizing Different Variable Types Work?

#### Identifying Numeric vs. Categorical Variables

In some cases, the data type clearly indicates what kind of variable it should be. A continuous variable is essentially always numeric, and a string variable is essentially always categorical.

For discrete variables, you need to investigate the values as well as any provided documentation. Then, ask yourself:

* Is an increase of 2 in this variable twice as much as an increase of 1?
* If 2 is "twice as much" as 1, that means it is reasonable to treat the variable as a numeric discrete variable. If not, the variable should be treated as categorical.

### Example of Visualizing Different Variable Types

![Mixed breed dog face close-up](https://moringa.instructure.com/courses/1406/files/625192/download)
Imagine you're a new data analyst at a pet store. The data you see comes in two flavors: number data (weight in kg, age in months) and category data (cat, dog, fur color). Number data lets you measure things, like how heavy a hamster is. Category data sorts things into groups, like fluffy vs. feathery pets.

Knowing the difference is key to choosing the right picture (chart or graph) to show the data. This helps you and your boss understand the data better, like what kind of pets to stock! Number data: "how much," Category data: "what kind." Both are important for smart pet store decisions.

### Conceptualize Visualizing Different Variable Types

![Diagram showing the associations between numeric and categorical variables](https://moringa.instructure.com/courses/1406/files/624939/download)

Variable type defined with example

| Term | Definition | Example |
| --- | --- | --- |
| Numeric (Continuous) | Can take any value within a range. These values are often measured and can have decimal points. | Temperature |
| Numeric (Discrete) | Represents countable data that can take specific integer values. | Number of Children in a Family (1, 2, 3, etc.) |
| Categorical (String) | Data that can be divided into distinct groups or categories, which are often represented as text. | Marital Status (e.g., "Single", "Married", "Divorced") |
| Categorical (Numeric) | Represents data that can be divided into distinct groups or categories, which are often represented as numbers that don't have mathematical meaning. | Zip Code (e.g., 94107, 10001, 60614) |
| \_\_init\_\_ method (double underscores) | A ‘magic’ method of classes that allows you to define attribute values when you instantiate an object from a class. | honda = Cars(make=’honda’, model=’crv’, year=2012, doors=4)  The parameters for instantiation are set by the \_\_init\_\_ method defined in the Cars class |
| Inheritance | Concept that describes the process of using an existing class (and its attributes and methods) to define a new class that shares those properties. The new child class ‘inherits’ from the existing parent class. The new class can then be further customized with new attributes/methods or updates/changes to the existing ones. | Using the Cars class we could create separate classes for different makes/companies and have them inherit attributes and methods from the parent Cars that are shared across all makes.  class BMW(Cars): class Honda(Cars): |
| Super class | Refers to the parent class when inheritance is being used. Allows a child class to update existing methods (like the \_\_init\_\_) that it has inherited from its parent. | class Honda(Cars):       def \_\_init\_\_(self, …):            super().\_\_init\_\_(...)  The Honda child class will inherit parameters from the parent class \_\_init\_\_ method but can include new ones as well. |

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243553

Scraped At: 2026-05-14T20:52:53.874518
