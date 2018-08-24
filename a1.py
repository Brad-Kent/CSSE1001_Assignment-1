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
    """
    Runs the Main Menu loop
    :return: None
    """
    while True:
        print("-"* 20)

        # Display Sub-Programs w/ Key
        display_options()

        # Get Users Choice
        user_choice = input(">")

        # Validate Input
        if not is_user_choice_valid(user_choice):
            print("Invalid Command")
            continue

        # Execute Users Request
        if user_choice == 'e':
            encrypt_text()
        elif user_choice == 'd':
            decrypt_text()
        elif user_choice == 'a':
            decrypt_text_auto()
        else:
            break


def display_options():
    """
    Displays the Menu keys and options to terminal
    :return: None
    """
    
    # TODO: This could be a modular structure
    print("Please choose an option [e/d/a/q]:")
    print("  e) Encrypt some text")
    print("  d) Decrypt some text")
    print("  a) Automatically decrypt english text")
    print("  q) Quit")


def is_user_choice_valid(user_choice):
    """
    Did the user input a valid option

    :param user_choice: The users option
    :return:  True if input is valid, False if not valid
    """

    return user_choice in ['e', 'd', 'a', 'q']

# Main Program Methods
def encrypt_text():
    data = get_crypto_data('e')
    print_result('e', encrypt(data[0], data[1]))


def decrypt_text():
    data = get_crypto_data('d')
    print_result('d', decrypt(data[0], data[1]))


def decrypt_text_auto():
    data = get_crypto_data('a')
    a_result = list(find_encryption_offsets(data[0]))
    a_result.append(data[0])
    print_result('a', a_result)

# I/O Methods
def get_crypto_data(user_option):
    # The struct to hold the user input data
    input_data = []

    # User option
    options = {"e": "text to encrypt", "d": "text to decrypt", "a": "encrypted text"}
    action = options[user_option]

    # Get the text
    input_data.append( input("Please enter some {}: ".format(action)) )

    # If user option is e (Encrypt) or d (Decrypt) get a offset value, Else no offset needed
    if user_option == 'e' or user_option == 'd':
        input_data.append( int(input("Please enter a shift offset (1-25):")) )

    return input_data


def print_result(user_option, result):
    options = {'e' : "encrypted", 'd' : "decrypted"}

    if user_option == 'e' or user_option == 'd':
        print("The {} text is: {}".format(options[user_option], result))

    elif user_option == 'a':
        if len(result) == 1:  # if none
            print("No valid encryption offset")
        elif len(result) == 2:  # if 1
            print("Encryption offset: {}".format( result[0]))
            print("Decrypted message: {}".format(( format_text(result[1], result[0]))))
        else:  # if many
            print("Multiple encryption offsets: {}".format(result[:-1]))
    else:
        print("Bye!")

# Validation Methods: Future Updates 
def is_offset_valid(offset):

    if not offset.isdigit():
        print("not a digit:")
        FLAG_QUIT = True

    offset = int(offset)

    if offset > 25 or offset < 1:
        print("not in range")
        FLAG_QUIT = True


def format_text(text, offset):
    """
    The main method that `mutates` the input text. If offset is positive, encrypt: move up/ forward, ...
    :param text:
    :param offset:
    :return: The Formatted text
    """

    MIN = 'a'
    MAX = 'z'
    formatted_text = ""

    #print("Beginning format")
    # Loops over the current Word, Either: Encrypts or Decrypts Word based on Offset
    for char in text:
        # If Current Char is not in Range, skip over it. ! Lower_Case Letter
        if char < MIN or char > MAX:
            formatted_text += char
            #print("Out Of Range")
            continue

        # if char is in range, it is a letter
        # Calculate the Encrypted / Decrypted Char
        offset_char = chr(ord(char) + offset)

        # ord('A') + offset :: new_offset =  offset_char - ord('Z') + ord('A')
        # is_char_out_of_range: if True: calculate new char range -> new char value in range
        if offset_char > MAX:  # Encrypt
            #print("> MAX")
            # Go to Start of Range
            offset_char = chr( ord(offset_char) - 26)
        elif offset_char < MIN:  # Decrypt
            #print("< MIN")
            # Go to End
            offset_char = chr( ord(offset_char) +  26)  # ord('Z') + offset

        formatted_text += offset_char

    return formatted_text


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
    :param offset: Int Offset
    :return: Decrypted Text
    """
    return format_text(text, -offset)


def find_encryption_offsets(text):
    """
    Returns a tuple containing all possible offsets that could have been used if to encrypt some English text into encrypted_text .
    :param text:
    :return: (Tuple) containing all possible data offsets
    """
    # Remove whitespace between words in multi word inputs
    text = text.split(' ')
    #print("Finding offsets")

    # Find valid offsets for word: Explain logic!
    valid_offsets = []
    for i in range(1, 26):
        new_format = format_text(text[0], i)

        if is_word_english(new_format):
            valid_offsets.append(i)
        #print("Valid Word? {}".format(is_word_english(new_format)))

    # Test every word for valid word
    checked_offsets = []  # Checked Offsets that work for every word in input
    is_offset_legal = True # If current offset has been validated

    # Loop over found offsets
    for offset in valid_offsets:
        # Check words w/ possible valid offset
        for word in text:
            new_word = format_text(word, offset)

            if not is_word_english(new_word):
                is_offset_legal = False
                break

        if is_offset_legal:
            checked_offsets.append(offset)
            #print("Found offset")
        else:
            is_offset_legal = True
            #print("no offset")


    #print("offsets: ", tuple(checked_offsets))
    return tuple(checked_offsets)




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


