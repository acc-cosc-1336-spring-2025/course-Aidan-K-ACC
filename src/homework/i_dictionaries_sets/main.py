from dictionary import add_inventory
from dictionary import remove_inventory_widget

def hw8_menu():
    dictionary= {}
    choice = 0
    while choice ==0:
        choice = int(input("Inventory Menu\n\n1-Add or Update Item\n2-Delete Item\n3-Exit\n"))
        while choice == 1:
            key= input("What is the item?\n")
            val= input("What is the value of the item?\n")
            ans = add_inventory(dictionary, key, val)
            print("Inventory: " + str(dictionary))
            exvar = input("Do you want to add another item?\ny or n\n")
            if exvar == "y":
                choice = 1
            else:
                choice = 0
        while choice == 2:
            key= input("What item is being removed?\n")
            print(remove_inventory_widget(dictionary, key))
            ans = remove_inventory_widget(dictionary, key)
            print("Inventory: " + str(dictionary))
            exvar = input("Do you want to remove another item?\ny or n\n")
            if exvar == "y":
                choice = 2
            else:
                choice = 0
        if choice == 3:
            print("Exiting Program...")
            exit

hw8_menu()