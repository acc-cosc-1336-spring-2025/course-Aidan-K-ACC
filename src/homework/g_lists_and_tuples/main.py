from lists import get_highest_list_value
from lists import get_lowest_list_value

def hw6_menu():
    choice = 0
    while choice ==0:
        choice = int(input("Homework 6 Menu\n1 Show the list low/high values-\n2-Exit\n"))
        while choice == 1:
            list= []
            while len(list) < 3:
                list+= input("Enter a number.\n")
            choice2= input("Do you want to enter another value? y or n\n")
            if choice2 == 'y':
                while choice2 == 'y':
                    kbin= input("Enter a number, or press 'n' \n")
                    if kbin != 'n':
                        list+= kbin
                    if kbin == 'n':
                        choice2= 'n'
            ans = "Highest: "+get_highest_list_value(list)+"   "+"Lowest: "+get_lowest_list_value(list)
            print("Answer: " + str(ans))
            exvar = input("Do you want to Exit?\ny or n\n")
            if exvar == "y":
                choice = 0
            else:
                choice = 1
        if choice == 2:
            print("Exiting Program...")
            exit

hw6_menu()