#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english
import a1_support as a1

__author__ = "Brad Kent, S45355194"


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

        text_mutated = ""

        if user_option == 'e':
            inputs = get_values(user_option)
            text_mutated = encrypt(inputs[0], inputs[1])

        elif user_option == 'd':
            inputs = get_values(user_option)
            text_mutated = decrypt(text, offset)

        else:
            text_mutated = find_encryption_offsets(text)


        print(text_mutated)

def get_values(user_option):
    # if not 'Quit', execute crypto program
    user_input = get_user_crypto_input(user_option)
    # The Text to Operate on
    text = user_input[0]

    if not is_offset_valid(user_input[1]):
        # TODO: Check documentation to see what to do
        print("not valid input")
        continue

def display_user_options():
    """
    Displays the Menu keys and options to terminal
    :return:
    """

    """ This could be a modular method"""
    print("Please choose an option [e/d/a/q]:")
    print("  e) Encrypt some text")
    print("  d) Decrypt some text")
    print("  a) Automatically decrypt English text")
    print("  q) Quit")


def is_user_option_valid(user_input):
    """
    Did the user input a valid option

    :param user_input: The users option
    :return:  True if input is valid, False if not valid
    """

    menu_options = ['e', 'd', 'a', 'q']

    if user_input in menu_options:
        return True

    return False


def is_offset_valid(offset):

    if not offset.isdigit():
        print("not a digit:")
        return False

    offset = int(offset)

    if offset > 25 or offset < 1:
        print("not in range")
        return False

    return True


def get_user_crypto_input(user_option):
    options = {"e": "text to encrypt", "d": "text to decrypt", "a": "encrypted text"}
    action = options[user_option]

    text = input("Please enter some {}".format(action))
    offset = input("Please enter a shift offset (1-25):")

    return [text, offset]


def format_text(text, offset):
    MIN = 'a'
    MAX = 'z'
    formated_text = ""

    # Loops over the current Word, Either: Encrypts or Decrypts Word based on Offset
    for char in text:
        # If Current Char is not in Range, skip over it. ! Lower_Case Letter
        if char < MIN or char > MAX:
            formated_text += char
            print("Out Of Range")
            continue

        # if char is in range, it is a letter
        # Calculate the Encrypted / Decrypted Char
        offset_char = chr(ord(char) + offset)

        # is_char_out_of_range: if True: calculate new char range -> new char value in range  # ord('A') + offset :: new_offset =  offset_char - ord('Z') + ord('A')
        if offset_char > MAX:  # Encrypt
            print(">")
            # Go to Start of Range
            offset_char -= 26
        elif offset_char < MIN:  # Decrypt
            print("<")
            # Go to End
            offset_char += 26  # ord('Z') + offset

        formated_text += offset_char

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


def find_encryption_offsets(text):
    # Test Text with offset entire range

    text = text.split(' ')

    for i in range(1, 26):
        new_format = format_text(text, i)
        print("New Format:", new_format)






    # if text >> Offset is in words(), then is valid offset
    ## Many text inputs are multi valued, so\ have to check each <> per white space
    # Split string into List. or could keep state of index, then splice string for each word then push to func:: Lambda in function argument


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


