# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25},
    {"id":21, "name": "Organic Bananas", "department": "Grocery pounds", "aisle": "fresh produce", "price": 0.79}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


#
#INPUT
#Handling Pricing per Pound
#what is # of item sold? 
# is the item sold per pound or quantity? 
product_ids = []

subtotal_price = 0

valid_ids = [str(p["id"]) for p in products]
selected_ids = []

while True:
    selected_id = input("Please input a product identifier, or 'DONE' if there are no more items:") 
    if selected_id == "DONE":
        break
    elif str(selected_id) in valid_ids:
        selected_ids.append(selected_id)
    else: 
        print("Detected invalid input! Please type a valid product identifier...")
        next


def lookup_product_by_id(product_id):
    matching_products = [product for product in products if product["id"] == product_id]
    return matching_products[0] 

#Configuring Sales Tax Rate

from dotenv import load_dotenv
import os
load_dotenv()
TAX_RATE = os.getenv("TAX_RATE")

print("-------------------------------")
print("This is the state tax rate:", float(TAX_RATE)*100, "%")
print("-------------------------------")


# PRINT RECEIPT

import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
running_total = 0

def to_usd(p):
    return "${0:,.2f}".format(p)

## A grocery store name of your choice

print("-------------------------------")
print("TS Grocery Store")
# A grocery store phone number and/or website URL and/or address of choice
print("-------------------------------")
print("Web: www.TSGroceryStore.com")
print("Phone: 1.123.456.7890")
#The date and time of the beginning of the checkout process, formatted in a human-friendly way 
##print checkout time 
print("---------------------------------")
print("CHECKOUT AT:" + str(now)) 



# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)
# The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
print("-------------------------------")
print("Shopping Cart Items:")
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    print("... " + matching_product["name"] + " " + "(" + to_usd(matching_product["price"]) + ")")

# The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% 
tax_price = subtotal_price * float(TAX_RATE)
total_price = subtotal_price + tax_price
print("---------------------------------")
print("SUBTOTAL PRICE:", to_usd(subtotal_price)) 
print("TAX:", to_usd(tax_price)) 
# The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
print("TOTAL PRICE:", to_usd(total_price)) 
# A friendly message thanking the customer and/or encouraging the customer to shop again
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")


