from strings import get_hamming_distance
from strings import get_dna_complement

def hw5_menu():
    choice = 0
    while choice ==0:
        choice = int(input("Homework 5 Menu\n1-Hamming Distance\n2-Dna Complement\n3-Exit\n"))
        while choice == 1:
            dna1 = str(input("Enter First Dna Sequence\n"))
            dna2 = str(input("Enter Second Dna Sequence\n"))
            ans = get_hamming_distance(dna1,dna2)
            print("Answer: " + str(ans))
            exvar = input("Do you want to exit?\ny or n\n")
            if exvar == "y":
                choice = 0
            else:
                choice = 1
        while choice == 2:
            dna = str(input("Enter a Dna Sequence\n"))
            ans = get_dna_complement(dna)
            print("Answer: " + str(ans))
            exvar = input("Do you want to exit?\ny or n\n")
            if exvar == "y":
                choice = 0
            else:
                choice = 2
        if choice == 3:
            print("Exiting Program...")
            exit

hw5_menu()