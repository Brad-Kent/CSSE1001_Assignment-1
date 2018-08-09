#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english

__author__ = "Brad Kent, s45355194"


main_menu_options = {
    "greeting": "Please choose an option [e/d/a/q]:",
    "e": "e) Encrypt some text",
    "d": "d) Decrypt some text",
    "a": "a) Automatically decrypt English text",
    "q": "q) Quit"
}

main_menu_input_steps = {
    1: "Please enter some text to encrypt:",
    2: "Please enter a shift offset (1-25):",
    3: "The encrypted text is:"
}

def main():
    # Add your main code here
    pass

def main_menu():
    user_input = "q"

    while True:

        if len(user_input) != 1:
            print("Invalid command")
        else:
            if user_input in main_menu_options:
                pass


items = [1, 2, 3, 4, 5]

def lambda_tutorial():

    lambda_func = lambda key: key in main_menu_options

    # test = lambda dictt: for x in dictt

    # True to loop with lambda
    # if !, lambda : lambda

    squared = list(map(lambda x: x + 1, items))  # Converting
    print(squared)

    x = map(lambda x: x, items)

    # print(list(x))

    # map

    x = lambda y: print(y)
    x("hellp")
    print("done")
    lol = map(lambda y: print(y + 1), items)
    print("done")
    # print(list(lol))

def map_tutorial():


##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get a
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()

