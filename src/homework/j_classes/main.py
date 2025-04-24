from class_a import die

def Homework_9_Menu():
    userin_yn= input("Would you like to roll the dice? y/n\n")
    while userin_yn == 'y':
        die.roll()
        print(die.get_rolled_value())
        userin_yn= input("Would you like to roll again? y/n\n")
    if userin_yn == 'n':
        print("Exiting...")

Homework_9_Menu()