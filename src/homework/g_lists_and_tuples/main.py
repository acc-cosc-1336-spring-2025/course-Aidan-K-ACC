from lists import get_p_distance
from lists import get_p_distance_matrix

def hw7_menu():
    choice = 0
    while choice ==0:
        choice = int(input("Homework 6 Menu\n1 Get p distance matrix-\n2-Exit\n"))
        while choice == 1:
            data_matrix= []
            num= int(input("How many sequences are in the data set?\n"))
            for n in range(0, num):
                temp_list= []
                key= ''
                print("Enter the data for sequence " + str(n+1) + " and type end when complete.")
                while key != 'end':
                    key= input("")
                    if key != 'end':
                        temp_list.append(key)
                data_matrix.append(temp_list)
            ans = get_p_distance_matrix(data_matrix)
            print("P distance results: " + str(ans))
            exvar = input("Do you want to Exit?\ny or n\n")
            if exvar == "y":
                choice = 0
            else:
                choice = 1
        if choice == 2:
            print("Exiting Program...")
            exit

hw7_menu()