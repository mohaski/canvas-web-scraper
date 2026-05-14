# Practice: Dictionaries, Strings, File Handling, and Logging

# Practice: Dictionaries, Strings, File Handling, and Logging

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Practice: Dictionaries, Strings, File Handling, and Logging

Icon Progress Bar (browser only)

6 min read

Imagine you're a junior software engineer working for a retail store. The store needs a system to manage its inventory data, which includes product names, quantities, and prices. Currently, this information is stored in an unorganized list format, making it difficult to efficiently track stock levels and retrieve product details.

Your task is to create a Python program that utilizes dictionaries to store and manage the inventory data. This program should allow users to:

* Add new products to the inventory.
* View existing product information (name, quantity, price).
* Update product quantities.
* Remove products from the inventory (if out of stock).

### Instructions

### [Task 1: Setting Up the Inventory Dictionary](#dpPanel0)

Start by creating an empty dictionary inventory to store product information: `inventory = {}`

### [Task 2: Adding Products](#dpPanel1)

Define a function add\_product (name, quantity, price) that takes three arguments:

* **name:** The product name (string)
* **quantity:** The initial product quantity (integer)
* **price:** The product price (float)

Inside the function:

* Check if the product name already exists in the dictionary using the in operator. If it doesn't exist, create a new key-value pair in the dictionary:
* **Key:** The product name (string)
* **Value:** A dictionary itself, containing quantity and price keys for that product.

If the product already exists, display a message indicating a duplicate entry.

```
def add_product(name, quantity, price):  
    if name not in inventory:  
        inventory[name] = {"quantity": quantity, "price": price}  
    else:  
        print(f"Product '{name}' already exists in inventory.")
```

### [Task 3: Viewing Product Information](#dpPanel2)

Create a function view\_product(name) that takes one argument:

* **name****:** The product name to search for (string)

Inside the function: Check if the product exists in the dictionary.

* If it exists, retrieve the nested dictionary for that product and display the name, quantity, and price using clear formatting.
* If it doesn't exist, display a message indicating the product is not found.

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

Define a function `update_quantity`(name, new\_quantity) that takes two arguments:

* **name****:** The product name to update (string)
* **new\_quantity**: The new quantity value (integer)

Inside the function: Check if the product exists in the dictionary.

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

Create a function `remove_product`(name) that takes one argument:

* **name:** The product name to remove (string)

Inside the function: Check if the product exists in the dictionary.

* If it exists, exists, use the pop method to remove the product's key-value pair from the inventory dictionary.
* The pop method removes the specified key and returns the corresponding value.
* Display a message confirming the product removal.
* If it doesn't exist, display a message indicating the product is not found.

```
inventory.pop(name)
```

### [Task 6: Main Program Loop](#dpPanel5)

Create a while loop to continuously prompt the user for actions until they exit.

Inside the loop: Present a menu to the user with options for:

* Adding a new product
* Viewing an existing product
* Updating product quantity
* Removing a product
* Exiting the program

Use a conditional statement (if statements) to handle user input based on their chosen option.

* Call the appropriate function (add\_product, view\_product, update\_quantity, remove\_product) based on the user's selection.

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

### Resources

* Lesson content about dictionaries, strings, and file handling and logging.

### Tools

* Python IDE, [Visual Studio Code](https://moringa.instructure.com/courses/1391/pages/process-using-visual-studio-code-as-ide "Integrated Development Environment Process - Visual Studio Code").

### Solution

### [Select for Solution](#dpPanel6)

```
def add_product(name, quantity, price):  
    """Adds a new product to the inventory dictionary.  
  
    Args:  
        name (str): The product name.  
        quantity (int): The initial quantity of the product.  
        price (float): The product price.  
    """  
  
    if name not in inventory:  
        inventory[name] = {"quantity": quantity, "price": price}  
    else:  
        print(f"Product '{name}' already exists in inventory.")  
  
def view_product(name):  
    """Displays information about a product in the inventory.  
  
    Args:  
        name (str): The name of the product to view.  
    """  
  
    if name in inventory:  
        product_info = inventory[name]  
        print(f"Product: {name}")  
        print(f"\tQuantity: {product_info['quantity']}")  
        print(f"\tPrice: ${product_info['price']:.2f}")  # Format price with 2 decimal places  
    else:  
        print(f"Product '{name}' not found in inventory.")  
  
def update_quantity(name, new_quantity):  
    """Updates the quantity of a product in the inventory.  
  
    Args:  
        name (str): The name of the product to update.  
        new_quantity (int): The new quantity value.  
    """  
  
    if name in inventory:  
        inventory[name]["quantity"] = new_quantity  
        print(f"Product '{name}' quantity updated.")  
    else:  
        print(f"Product '{name}' not found in inventory.")  
  
def remove_product(name):  
    """Removes a product from the inventory.  
  
    Args:  
        name (str): The name of the product to remove.  
    """  
  
    if name in inventory:  
        inventory.pop(name)  # Remove product using pop method  
        print(f"Product '{name}' removed from inventory.")  
    else:  
        print(f"Product '{name}' not found in inventory.")  
  
def main():  
    """Main program loop for user interaction."""  
  
    inventory = {}  # Empty dictionary to store inventory data  
  
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

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239300

Scraped At: 2026-05-14T15:59:00.225488
