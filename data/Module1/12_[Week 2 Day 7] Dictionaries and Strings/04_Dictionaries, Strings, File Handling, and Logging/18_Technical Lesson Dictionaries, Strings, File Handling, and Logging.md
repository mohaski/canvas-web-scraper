# Technical Lesson: Dictionaries, Strings, File Handling, and Logging

# Technical Lesson: Dictionaries, Strings, File Handling, and Logging

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Technical Lesson: Dictionaries, Strings, File Handling, and Logging

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time: 1 hour**

In this lesson, you'll explore how to manage inventory data using dictionaries in Python. Imagine you're a junior software engineer working for a retail store. Currently, the store's inventory information (product names, quantities, and prices) is stored in an unorganized list format. This makes it difficult to track stock levels and retrieve product details efficiently.

By utilizing dictionaries, you'll create a program that allows users to:

* Add new products to the inventory.
* View existing product information (name, quantity, price).
* Update product quantities.
* Remove products from the inventory (if out of stock).

### Resources

* Lesson content about dictionaries, strings, and file handling and logging.

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Instructions

These instructions will walk you through how to:

* Work with dictionaries to effectively store and retrieve data.
* Access and update dictionary values using keys.
* Utilize string operations to process product names and information.
* Apply problem-solving skills to design a user-friendly inventory management system.

### [Task 1: Setting Up the Inventory Dictionary](#dpPanel0)

Start by creating an empty dictionary inventory to store product information: `inventory = {}`

### [Task 2: Adding Products](#dpPanel1)

1. Add they key value pairs for adding products or new products. The key will be the product name and the value associated with that key will be a dictionary (an internal dictionary). That contains 2 keys quantity and price. The values for those keys are the perspective information- the product values and respective information.

* **name:** The product name (string)
* **quantity****:** The initial product quantity (integer)
* **price****:** The product price (float)

1. Inside the function

Check if the product name already exists in the dictionary using the in operator**.**

* If it doesn't exist, create a new key-value pair in the dictionary:
  + **Key:** The product name (string)
  + **Value:** A dictionary itself, containing quantity and price keys for that product
* If the product already exists, display a message indicating a duplicate entry.

```
if shirt not in inventory: "shirt"  
if inventory[name] = {"quantity": quantity, "price": price}  
[  
        print(f"Product '{name}' already exists in inventory.")
```

### [Task 3: Viewing Product Information](#dpPanel2)

1. Create a function `view_product(name)` that takes one argument

* **name****:** The product name to search for (string)

1. Inside the function

* Check if the product exists in the dictionary.
  + If it exists, retrieve the nested dictionary for that product and display the name, quantity, and price using clear formatting.
  + If it doesn't exist, display a message indicating the product is not found.

```
def view_product(name):  
    if name in inventory:  
        product_info = inventory[name]  
        print(f"Product: {name}")  
        print(f"\tQuantity: {product_info['quantity']}")  
        print(f"\tPrice: ${product_info['price']:.2f}")  # Format price with 2 decimal places  
    else:  
        print(f"Product '{name}' not found in inventory.")
```

### [Task 4: Updating Product Quantities](#dpPanel3)

1. Define a function `update_quantity` (name, new\_quantity) that takes two arguments

* **name:** The product name to update (string)
* **`new_quantity`:** The new quantity value (integer)

1. Inside the function

Check if the product exists in the dictionary.

* If it exists, update the quantity value in the nested dictionary for that product.
* If it doesn't exist, display a message indicating the product is not found.

```
def update_quantity(name, new_quantity):  
    if name in inventory:  
        inventory[name]["quantity"] = new_quantity  
        print(f"Product '{name}' quantity updated.")  
    else:  
        print(f"Product '{name}' not found in inventory.")
```

### [Task 5: Removing Products](#dpPanel4)

1. Create a function `remove_product(name)` that takes one argument

* **name****:** The product name to remove (string)

1. Inside the function - Check if the product exists in the dictionary.

* If it exists, use the pop method to remove the product's key-value pair from the inventory dictionary. The pop method removes the specified key and returns the corresponding value.
* Display a message confirming the product removal.
* If it doesn't exist, display a message indicating the product is not found.

```
def remove_product(name):  
    if name in inventory:  
        inventory.pop(name)  # Remove product using pop method  
        print(f"Product '{name}' removed from inventory.")  
    else:  
        print(f"Product '{name}' not found in inventory.")
```

### [Task 6: Main Program Loop](#dpPanel5)

Create a while loop to continuously prompt the user for actions until they exit. Inside the loop:

* Present a menu to the user with options for:
  + Adding a new product
  + Viewing an existing product
  + Updating product quantity
  + Removing a product
  + Exiting the program
* Use a conditional statement (if statements) to handle user input based on their chosen option.
* Call the appropriate function (`add_product`, `view_product`, `update_quantity`, `remove_product`) based on the user's selection.

```
def main():  
    while True:  
        print("\nInventory Management System")  
        print("1. Add New Product")  
        print("2. View Product Information")  
        print("3. Update Product Quantity")  
        print("4. Remove Product")  
        print("5. Exit")  
        choice = input("Enter your choice (1-5): ")  
  
        if choice == "1":  
            name = input("Enter product name: ")  
            quantity = int(input("Enter initial quantity: "))  
            price = float(input("Enter product price: "))  
            add_product(name, quantity, price)  
        elif choice == "2":  
            name = input("Enter product name to view: ")  
            view_product(name)  
        elif choice == "3":  
            name = input("Enter product name to update: ")  
            new_quantity = int(input("Enter new quantity: "))  
            update_quantity(name, new_quantity)  
        elif choice == "4":  
            name = input("Enter product name to remove: ")  
            remove_product(name)  
        elif choice == "5":  
            print("Exiting program...")  
            break  
        else:  
            print("Invalid choice. Please try again.")  
  
if __name__ == "__main__":  
    main()
```

### Considerations and Decisions

This lesson explored using dictionaries to manage inventory data in Python. Here are some common challenges and considerations to keep in mind:

#### Challenges

**Error Handling:** The provided code doesn't handle invalid user input gracefully. For example, if a user enters a non-numeric value for quantity or price, the program might crash.

**Addressing Challenges**

* Include input validation using `try-except` blocks to catch potential errors like non-numeric input.
* Provide informative error messages to guide the user towards correct input formats.

**Data Validation:** There are no checks to ensure product names are unique or that quantities are non-negative. Duplicate product entries or negative stock levels could lead to inconsistencies in the inventory data.

**Addressing Challenges**

* Implement checks within the `add_product` function to ensure product names are unique (e.g., using a set to store existing names).
* Validate that quantities are non-negative during updates using conditional statements (e.g.,  `if new_quantity < 0` ).

#### Decisions Points

**Using `pop`****method for removal:** The code utilizes the pop `pop` method to remove products. This approach is efficient but requires confirming the product exists before using it. An alternative would be to use `get` with a default value (e.g., `None`) to handle potential missing keys and avoid errors.

**Impact of Decisions**

* Using the `pop` method simplifies the removal process but requires the extra check for product existence. This ensures the program doesn't attempt to remove a non-existent key, potentially causing errors.
* The `get` method with a default value provides a more robust approach for handling missing keys but requires additional logic to differentiate between a missing product and a product with zero quantity.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239298

Scraped At: 2026-05-14T15:58:52.885252
