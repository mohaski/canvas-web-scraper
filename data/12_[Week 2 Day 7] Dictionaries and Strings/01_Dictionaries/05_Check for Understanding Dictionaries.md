# Check for Understanding: Dictionaries

# Check for Understanding: Dictionaries

## ![](https://moringa.instructure.com/courses/1391/files/620140/preview?) Check for Understanding: Dictionaries

Icon Progress Bar (browser only)

Now is your opportunity to see how much you can recall from the topic! Take a moment to answer the questions below. These are not graded, but they will allow you to check how much you are putting together the content in this lesson and review before moving to a new topic. 

### Quick Check - CRM System

You are a software engineer working on a customer relationship management (CRM) system for a retail company. The system needs to store and retrieve customer information, such as names, email addresses, and purchase histories, efficiently. To achieve this, you decide to use a dictionary in Python where each customer's email address will serve as the key, and their details (name, purchase history, etc.) will be stored as the value.

The following Python code snippet is used to create and manage the customer information:

```
# Initial customer dictionary  
customers = {  
    "alice@example.com": {"name": "Alice", "purchases": ["Laptop", "Headphones"]},  
    "bob@example.com": {"name": "Bob", "purchases": ["Smartphone"]}  
}  
  
# Adding a new customer  
customers["charlie@example.com"] = {"name": "Charlie", "purchases": ["Tablet"]}  
  
# Updating Bob's purchase history  
customers["bob@example.com"]["purchases"].append("Smartwatch")
```

**After executing the code above, which of the following statements correctly describes the contents of the customers dictionary?**

The `customers` dictionary will contain three customers: Alice, Bob (with an updated purchase history), and Charlie.
:   **Correct:** The `customers` dictionary is initially created with two customers (Alice and Bob). A new customer (Charlie) is added with a new key ("charlie@example.com"), and Bob's purchase history is updated by appending "Smartwatch" to his list of purchases. The dictionary now contains three customers: Alice, Bob (with the updated purchase history), and Charlie.

The `customers` dictionary will contain two customers: Alice and Bob, with Charlie's information replacing Alice's.
:   Incorrect, because Charlie's information is added as a new entry and does not replace any existing customer.

The `customers` dictionary will contain two customers: Alice and Charlie, with Bob's information being removed
:   Incorrect because all three customers (Alice, Bob, and Charlie) remain in the dictionary, and none are removed.

The `customers` dictionary will contain three customers, but Bob's purchase history will not be updated because dictionaries are immutable.
:   Incorrect because while dictionary keys are immutable, the dictionary itself is mutable, allowing you to update the values (such as modifying Bob's purchase history).

[Check Answer


Links to an external site.](https://learning.flatironschool.com/#)

### Quick Check - Encrypted Passwords

As a junior cybersecurity professional, you're tasked with managing a database of encrypted passwords for a company's internal systems. To organize this data, you decide to use a dictionary in Python where each key represents a username, and each value represents the encrypted password for that user.

You write the following Python code to create and manage the password database:

```
# Initial password database  
passwords = {  
    "alice": "a1b2c3d4",  
    "bob": "e5f6g7h8",  
    "charlie": "i9j0k1l2"  
}  
  
# Adding a new user  
passwords["dave"] = "m3n4o5p6"  
  
# Updating Charlie's password  
passwords["charlie"] = "q7r8s9t0"
```

**After executing the code above, which of the following statements correctly describes the contents of the `passwords` dictionary?**

The `passwords` dictionary will contain four users: Alice, Bob, Charlie (with an updated password), and Dave.
:   **Correct:** The `passwords` dictionary is initially created with three users (Alice, Bob, and Charlie). A new user (Dave) is added with a new key ("dave"), and Charlie's password is updated. The dictionary now contains four users: Alice, Bob, Charlie (with the updated password), and Dave.

The `passwords` dictionary will contain three users: Alice, Bob, and Dave, with Charlie's information being removed.
:   Incorrect, because Charlie's information is not removed. The dictionary still contains information about all four users.

The `passwords` dictionary will contain four users, but Dave's password will overwrite Alice's password.
:   Incorrect because Dave's password is added as a new entry and does not overwrite any existing user's password.

The `passwords` dictionary will contain four users, but Charlie's password will remain unchanged because dictionaries are immutable.
:   Incorrect because, while dictionary keys are immutable, the dictionary itself is mutable, allowing you to update the values (such as modifying Charlie's password).

[Check Answer](#)

### Quick Check - Product Names

As a junior data scientist at a retail company, you are tasked with organizing customer feedback data. The feedback consists of product names as keys and their corresponding customer ratings as values. You decide to use a Python dictionary to store this information.

You write the following Python code to create and manage the feedback dictionary:

```
# Initial feedback dictionary  
product_feedback = {  
    "laptop": 4.5,  
    "smartphone": 4.7,  
    "headphones": 4.2  
}  
  
# Adding feedback for a new product  
product_feedback["tablet"] = 4.8  
  
# Updating the rating for headphones  
product_feedback["headphones"] = 4.3
```

**After executing the code above, which of the following statements correctly describes the contents of the `product_feedback` dictionary?**

The `product_feedback` dictionary will contain three products: laptop, smartphone, and tablet, with headphones being removed.
:   Incorrect, because the headphones product is not removed; its rating is updated.

The `product_feedback` dictionary will contain four products: laptop, smartphone, headphones (with an updated rating), and tablet.
:   **Correct:** The dictionary is initially created with three products (laptop, smartphone, and headphones). A new product (tablet) is added, and the rating for headphones is updated. The dictionary now contains four products: laptop, smartphone, headphones (with the updated rating), and tablet.

The `product_feedback` dictionary will contain four products, but the rating for the tablet will overwrite the rating for the smartphone.
:   Incorrect because the tablet is added as a new key-value pair and does not overwrite any existing product ratings.

The `product_feedback` dictionary will contain four products, but the rating for headphones will remain unchanged because dictionaries cannot be modified after creation.
:   Incorrect because dictionaries in Python are mutable, meaning you can update their contents, including modifying existing values (such as changing the rating for headphones).

[Check Answer](#)

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239272

Scraped At: 2026-05-14T15:57:16.269187
