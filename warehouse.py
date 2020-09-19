
"""
    Program: Warehouse Management System
     Author: M. Lane Thompson
      Func: 
            1 - Register Items
                - id (auto generated) (int)
                - title (str)
                - category (str)
                - stock (int)
                - price (float)
"""
# imports
from menu import print_menu, clear, print_header
from item import Item
import pickle

# global variables
catalog = []

# functions

def serialize_catalog():
    writer = open('warehouse.data', 'wb') 
    pickle.dump(catalog, writer)
    writer.close()
    print("Data Serialized!")

def deserialize_catalog():
    reader = open('warehouse.data', 'rb')
    temp_list = pickle.load(reader)

    for item in temp_list:
        catalog.append(item)

    how_many = len(catalog)
    print("Deserialized" + str(how_many) + "items")


def register_item():
    try:
        print_header("Register Item")
        title = input('Please provide the Title: ')
        cat = input("Please provide the category: ")
        stock = int(input("Please provide initial stock: "))
        price = float(input("Please provide the price: "))

        item = Item(0, title, cat, stock, price)
        # add item to the catalog list
        catalog.append(item)

        print("** Item Saved! **")

    except ValueError:
        print("** Error, incorrect input, fix and try again")
    except:
        print('** Error, something went wrong! **')

def print_catalog():
    print_header("Items on Catalog")

    if(len(catalog) == 0):
        print("** Your catalog is empty ** \nUse option 1 to create items\n")
    else:
        for item in catalog:
            print(item.title)

def print_no_stock():
    for item in catalog:
        if(item.stock == 0):
            print(item.title)

def delete_item():
    item = choose_item("Please choose teh ID to delete: ")
    if(item !=0):
        catalog.remove(item)
        print("Item removed")

def update_stock():
    item = choose_item("Please choose the ID to update: ")
    if(item !=0):
        stock = int(input("Provide new stock value: "))
        item.stock = stock
        print("Stock updated!")

def update_price():
    item = choose_item("Please choose the ID to update: ")
    if(item !=0):
        price = float(input("Provide new price: "))
        item.price = price
        print("Price Updated!")

def choose_item(message):
    try:
        print_catalog()
        id = int(input("Please choose the ID to delete: "))
        found = False
        for item in catalog:
            if(item.id == id):
                found = True
                return item

            if(not found):
                print("**Error, invalid ID, verify and try again")
                return 0

    except:
        print("**Error, verify and try again")
        return 0

def total_stock_value():
    print_header("Total stock value")
    total = 0.0
    for item in catalog:
        total = total + (item.price * item.stock)
    
    print("Total: " +str(total))

def delete_item():
    try:
        print_catalog()
        id = int(input ("Please choose the ID to delete: "))
        found = False
        for item, in catalog:
            if(item.id == id):
                found = True
                catalog.remove(item)
                print("Item has been removed!")

        if(not found):
            print("Error, invalid ID, verify and try again")

    except:
        print("Error, verify and try again")

def update_stock():
    try:
        print_catalog()
        id = int(input ("Please choose the ID to update: "))
        found = False
        for item in catalog:
            if(item.id == id):
                found = True
                stock = int(input("Please provide new Stock value: "))
                item.stock = stock
                print("Stock Updated!")

            if(not found):
                print("Error, invalid ID, verify and try again")
    except:
        print("Error, verify and try again")

# Instructions 
deserialize_catalog()

opc = ''
while(opc !='x'):
    clear()
    print_menu()

    opc = input('Please select an option: ')

    if(opc == '1'):
            register_item()
            serialize_catalog()
    elif(opc == '2'):
            print_catalog()
    elif(opc == '3'):
            print_no_stock()
    elif(opc == '4'):
            delete_item()
            serialize_catalog()
    elif(opc == '5'):
            update_stock()
            serialize_catalog()
    elif(opc == '6'):
        update_price()
        serialize_catalog()
    elif(opc == '7'):
        total_stock_value()

    input("Press Enter to continue")

print("Thank you, good bye!")