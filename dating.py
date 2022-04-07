#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: April, 06, 2022
# Find if you can date the grandchild


import sys


def age_check():
    # get the users age
    age_int = input("How old are you? ")
    # make sure the users number is an int
    try:
        age = int(age_int)
    except:
        print("that is not a valid age")
        main()
    # age check
    if age > 25 and age < 40:
        print("Congragulations you can date my grandchild!")
    elif age < 0:
        print("your age has to be above 0")
        main()
    else:
        print("I'm sorry you do not meet the requirements to date my grandchild")
    # ask the user to try again?
    try_again = str(input("Would you like to try again? \n"))
    if try_again == "Y" or try_again == "y" or try_again == "yes" or try_again == "YES":
        main()
    elif try_again == "N" or try_again == "n" or try_again == "no" or try_again == "NO":
        print("All right Good bye!")
        input("p.s If you change you mind and want to try again just press <enter> ")
        main()


def main():

    # check the age
    age_check()


# run main
if __name__ == "__main__":
    main()
