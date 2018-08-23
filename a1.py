#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english
import a1_support as a1

__author__ = "Brad Kent, S45355194"


FLAG_QUIT = False


def menu():
    num_of_its: int = 0
    while True:
        print("-"* 20)
        num_of_its += 1
        print("Iterations:", num_of_its)
        # Display Sub-Programs w/ Key
        display_options()

        # Get Users Choice
        users_choice = input(">")

        # Validate Input
        if not is_user_choice_valid(users_choice):
            print("Invalid Command")
            continue

        # Execute Users Request
        if users_choice == 'e':
            encrypt_text()
        elif users_choice == 'd':
            decrypt_text()
        elif users_choice == 'a':
            decrypt_text_auto()
        else:
            break


def display_options():
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


def is_user_choice_valid(users_choice):
    """
    Did the user input a valid option

    :param users_choice: The users option
    :return:  True if input is valid, False if not valid
    """

    return users_choice in ['e', 'd', 'a', 'q']


def encrypt_text():
    data = get_crypto_data('e')
    print_result('e', encrypt(data[0], data[1]))


def decrypt_text():
    data = get_crypto_data('d')
    print_result('d', decrypt(data[0], data[1]))


def decrypt_text_auto():
    data = get_crypto_data('a')
    find_encryption_offsets(data[0])


def get_crypto_data(user_option):
    input_data = []

    options = {"e": "text to encrypt", "d": "text to decrypt", "a": "encrypted text"}
    action = options[user_option]

    input_data.append( input("Please enter some {}".format(action)) )

    if user_option == 'e' or user_option == 'd':
        input_data.append( int(input("Please enter a shift offset (1-25):")) )

    return input_data


def print_result(user_option, mutated_text):
    options = {'e' : "encrypted", 'd' : "decrypted"}
    if user_option == 'e' or user_option == 'd':
        print("The {} text is: {}".format(options[user_option], mutated_text))

    elif user_option == 'a':
        # if 1                                              # if many                          # if none
        a = ( "Encryption offset:" + "Decrypted message:") + "Multiple encryption offsets:" + "No valid encryption offset"
    else:
        print("Bye!")


def is_offset_valid(offset):

    if not offset.isdigit():
        print("not a digit:")
        FLAG_QUIT = True

    offset = int(offset)

    if offset > 25 or offset < 1:
        print("not in range")
        FLAG_QUIT = True


def format_text(text, offset):
    MIN = 'a'
    MAX = 'z'
    formated_text = ""

    print("Begining format")
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

        # ord('A') + offset :: new_offset =  offset_char - ord('Z') + ord('A')
        # is_char_out_of_range: if True: calculate new char range -> new char value in range
        if offset_char > MAX:  # Encrypt
            print("> MAX")
            # Go to Start of Range
            offset_char = chr( ord(offset_char) - 26)
        elif offset_char < MIN:  # Decrypt
            print("< MIN")
            # Go to End
            offset_char = chr( ord(offset_char) +  26)  # ord('Z') + offset

        formated_text += offset_char

    return formated_text


# Assignment: 4 Functions
def main():
    menu()


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
    print(type(text))
    for word in text:
        print('='*20)
        for i in range(1, 26):
            new_format = format_text(word, i)


            #print("New Format: Old: {}, New: {}".format(word, new_format))






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


