# Import Functions
from repetition import get_factorial
from repetition import sum_odd_numbers

def hw3_menu():
    choice = 0
    while choice ==0:
        choice = int(input("Homework 3 Menu\n1-Factorial\n2-Sum odd numbers\n3-Exit\n"))
        while choice == 1:
            num = int(input("Enter a number\n"))
            if num > 0 and num <10:
                print("Tested")#get_factorial(num)
            else:
                while num <= 0 or num >= 10:
                    num = int(input("Enter a different number between 0 and 10\n"))
            ans = get_factorial(num)
            print("Answer: " + str(ans))
            exvar = input("Do you want to exit?\ny or n\n")
            if exvar == "y":
                choice = 0
            else:
                choice = 1
        while choice == 2:
            num = int(input("Enter a number\n"))
            if num > 0 and num <10:
                print("Tested")#get_factorial(num)
            else:
                while num <= 0 or num >= 100:
                    num = int(input("Enter a different number between 0 and 100\n"))
            ans = get_factorial(num)
            print("Answer: " + str(ans))
            exvar = input("Do you want to exit?\ny or n\n")
            if exvar == "y":
                choice = 0
            else:
                choice = 2
        if choice == 3:
            print("Exiting Program...")
            exit

hw3_menu()