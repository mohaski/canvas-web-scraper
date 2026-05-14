# Examples: Using Operators in Business

# Examples: Using Operators in Business

## ![](https://moringa.instructure.com/courses/1391/files/620354/preview) Examples: Using Operators in Business

* [Page: Introduction to Operators and Control Flow Statements (1 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239144 "Page: Introduction to Operators and Control Flow Statements (1 of 12)")
* [Page: Introduction to Operators (2 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239147 "Page: Introduction to Operators (2 of 12)")
* [Page: What are Operators? (3 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239149 "Page: What are Operators? (3 of 12)")
* [Page: Current: Examples: Using Operators in Business (4 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239150 "Page: Current: Examples: Using Operators in Business (4 of 12)")
* [Page: Process: Python Operators (5 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239151 "Page: Process: Python Operators (5 of 12)")
* [Page: Summary: Operators (6 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239152 "Page: Summary: Operators (6 of 12)")
* [Page: Check for Understanding: Operators (7 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239153 "Page: Check for Understanding: Operators (7 of 12)")
* [Page: Technical Lesson: Operators (8 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239154 "Page: Technical Lesson: Operators (8 of 12)")
* [Page: Practice: Rock-Paper-Scissors Game (9 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239155 "Page: Practice: Rock-Paper-Scissors Game (9 of 12)")
* [Discussion: Operators (10 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239159 "Discussion: Operators  (10 of 12)")
* [Lab: Coding with Operators and Control Flow Statements (11 of 12), Assignment](https://moringa.instructure.com/courses/1391/modules/items/239161 "Lab: Coding with Operators and Control Flow Statements (11 of 12), Assignment")
* [Operators and Control Flow Quiz (12 of 12)](https://moringa.instructure.com/courses/1391/modules/items/239163 "Operators and Control Flow Quiz (12 of 12)")

3 min read

Let's consider the real-world scenarios discussed in the introduction of this module. Consider the following examples of how to implement control flow if-elif-else statements with Python logical operators in a few different scenarios:

* In an e-commerce website that implement a checkout system
* In a retail company, and you have been tasked with analyzing the sales data to gain insights into the company's performance

### E-Commerce Website

**Step 1:** Identify the decision-making scenario

* During the checkout process, you want to apply certain discounts based on specific conditions.

**Step 2:** Define the conditions

* Apply a 10% discount for members with a total amount of $100 or more.
* Apply a 15% discount if the customer has a coupon or the total amount is $200 or more.

**Step 3:** Construct the if-elif-else statement

```
    if is_member and total_amount >= 100:  
        discount = 0.1  # Apply a 10% discount for members with a total amount of $100 or more  
    elif has_coupon or total_amount >= 200:  
        discount = 0.15  # Apply a 15% discount if the customer has a coupon or the total amount is $200 or more
```

**Step 4**: Write the code blocks for each condition

```
def apply_discount(total_amount, is_member, has_coupon):  
    discount = 0  
      
    if is_member and total_amount >= 100:  
        discount = 0.1  # Apply a 10% discount for members with a total amount of $100 or more  
    elif has_coupon or total_amount >= 200:  
        discount = 0.15  # Apply a 15% discount if the customer has a coupon or the total amount is $200 or more  
      
    discounted_amount = total_amount - (total_amount * discount)  
    return discounted_amount
```

**Step 5**: Test and refine

* The function calculates the discounted amount by subtracting the discount from the total amount and returns the result. You could use this function in your checkout system to automatically apply discounts based on the specified conditions.

**Step 6:** Document and maintain

### Retail Company

**Step 1:** Identify the decision-making scenario

* The sales data includes information such as the quantity of products sold and the price per unit as well as the cost per unit.

**Step 2:** Define the conditions

* Calculate the total revenue, profit, gross profit margin, and also create a sales target for next month based on a 10% increase.

**Step 3:** Construct the arithmetic operator statement

```
# Sales data for a particular product  
quantity_sold = 500  
price_per_unit = 9.99  
cost_per_unit = 7.50  
  
# Calculate the total revenue  
total_revenue = quantity_sold * price_per_unit  
print("Total revenue: $", total_revenue)
```

**Step 4:** Write the code blocks for each condition

```
# Calculate the total revenue  
total_revenue = quantity_sold * price_per_unit  
print("Total revenue: $", total_revenue)  
  
# Calculate the total cost  
total_cost = quantity_sold * cost_per_unit  
print("Total cost: $", total_cost)  
  
# Calculate the profit  
profit = total_revenue - total_cost  
print("Profit: $", profit)  
  
# Calculate the profit margin  
profit_margin = (profit / total_revenue) * 100  
print("Profit margin: {:.2f}%".format(profit_margin))  
  
# Calculate the sales target for next month (10% increase)  
next_month_target = total_revenue * 1.1  
print("Next month's sales target: $", next_month_target)
```

**Step 5**: Test and refine

* Your code output would return with these values:

```
Total revenue: $ 4995.0  
Total cost: $ 3750.0  
Profit: $ 1245.0  
Profit margin: 24.92%  
Next month's sales target: $ 5494.5
```

**Step 6:** Document and maintain

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1391/modules/items/239150

Scraped At: 2026-05-14T00:28:14.122720
