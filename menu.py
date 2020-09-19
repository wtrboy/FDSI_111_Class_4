import os


def print_menu():
    print("--------------------------")
    print("Warehouse Mangement System")
    print("--------------------------")

    print('[1] Register New Item')
    print('[2] Display Catalog')
    print('[3] Items out of Stock')
    print('[4] Delete Item')
    print('[5] Update Item Stock')
    print('[6] Update Item Price')
    print('[7] Print the Stock Value')
    print('[8] Print Categories')

    print('[x] Close')

def clear():
    command = ''
    if(os.name == 'nt'):
        command = 'cls'
    else:
        command = 'clear'
    return os.system(command)

    # return os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    clear()
    print("----------------------------")
    print(title)
    print("----------------------------")

def print_item(item):
    print(
        str(item.id).rjust(3)
        + " | " + item.title.ljust(25)
        + " | " + item.category.ljust(12)
        + " | " + str(item.stock).rjust(11)
        + " | " + str(item.price).rjust(15)
    )