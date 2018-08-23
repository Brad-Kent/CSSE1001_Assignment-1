#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english
import a1_support as a1

__author__ = "Brad Kent, s45355194"


def procedual_menu():
    print("Welcome")

    while True:
        # Display Menu Options
        display_user_options()

        # Get User Menu Option
        user_option = input(">")

        # Check to see if input is a valid command
        if not is_user_option_valid(user_option):
            print("Invalid Command \n")
            continue

        # Execute user specified sub-program
        if user_option == "q":
            break

        # if not 'Quit', execute crypto program
        user_input = get_user_input(user_option)
        text = user_input[0]

        if not is_user_input_valid(user_input[1]):
            # TODO: Check documentation to see what to do
            print("Bit shift range is 1-25")
            continue

        offset = int(user_input[1])

        text_mutated = ""
        if user_option == 'e':
            text_mutated = encrypt(text, offset)
        elif user_option == 'd':
            text_mutated = decrypt(text, offset)
        else:
            text_mutated = auto_decrypt(text, offset)

        print(text_mutated)


def display_user_options():
    """ This could be a modular method"""
    print("Please choose an option [e/d/a/q]:")
    print("  e) Encrypt some text")
    print("  d) Decrypt some text")
    print("  a) Automatically decrypt English text")
    print("  q) Quit")


def is_user_option_valid(user_input):
    menu_options = ['e', 'd', 'a', 'q']

    if user_input in menu_options:
        return True

    return False


def get_user_input(user_option):
    options = {"e": "text to encrypt", "d": "text to decrypt", "a": "encrypted text"}
    action = options[user_option]

    text = input("Please enter some {}".format(action))
    # This needs to be protected with int wrapping
    offset = input("Please enter a shift offset (1-25):")

    return [text, offset]


def is_user_input_valid(offset):
    if offset.isdigit():
        return False
    elif offset > 25 or offset < 1:
        return False

    return True


def format_text(text, offset):
    # Range: ord('A') -- ord('Z')
    formated_text = ""

    for char in text:
        # If Current Char is not in Range, skip over it
        ## is_char_a_letter()
        if char < 'A' or char > 'Z':
            formated_text += char
            print("FUCJ")
            continue
        offset_char = ord(char) + offset

        ## is_char_out_of_range
        ### if T: calculate new char range -> new char value in range
        if offset_char > ord('Z'):
            print(">")
            offset_char -= 26  # ord('A') + offset:::: new_offset =  offset_char - ord('Z') + ord('A')
        elif offset_char < ord('A'):
            print("<")
            offset_char += 26  # ord('Z') + offset

        formated_text += chr(offset_char)
    return formated_text


# Assignment: 4 Functions
def main():
    procedual_menu()


def encrypt(text, offset):
    """
    Encrypts by replacing each letter with the letter some fixed number of positions down the alphabet. Returns the encrypted text.

    :param text: The text to be encrypted
    :param offset: Shift text offset amounts of times
    :return: Encrypted Text
    """

    return format_text(text, offset)

def decrypt(text, offset):
    """
    Decrypts text that was encrypted by the encrypt function above. Returns the decrypted text.

    :param text: Encrypted Text
    :param offset: Letter Offset
    :return: Decrypted Text
    """
    return format_text(text, -offset)

def auto_decrypt(text, offset):
    # Test Text with offset entire range
    # if text >> Offset is in words(), then is valid offset
    ## Many text inputs are multi valued, so\ have to check each <> per white space
    # Split string into List. or could keep state of index, then splice string for each word then push to func:: Lambda in function argument
    return "auto"


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

