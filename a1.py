#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english
import a1_support as a1

__author__ = "Brad Kent, s45355194"

# Good Idea
main_menu_options = {
    "greeting": "Please choose an option [e/d/a/q]:",
    "e": "e) Encrypt some text",
    "d": "d) Decrypt some text",
    "a": "a) Automatically decrypt English text",
    "q": "q) Quit"
}
# Could work, but too complicated/ Fragile
main_menu_input_responses = {
    "e_0": "Please enter some text to encrypt:",
    "d_0": "Please enter some text to decrypt:",
    "offset": "Please enter a shift offset (1-25):",
    "e_2": "The encrypted text is:",
    "d_2": "The decrypted text is:",
    "q": "Bye!",
    "!input": "Invalid Command",
    "a_!": "No Valid encrypton offset",
    "a_#" : "Multiple encryption offsets:",
    "a_*": "Decryption offset"
}

def main():
    # Add your main code here
    encrypt("abcd", 1)
    #create_alpabet()

# Assignment Functions


def check_input(input):
    # Check for weired symbols
    # Check for upper case
    pass


def create_alpabet():
    for alp in range(ord('a'), ord('z') + 1 ):
        print(chr(alp))


def encrypt(text, offset):
    """
    Encrypts text by the offset \
    :param text:
    :param offset:
    :return encrypted text
    """
    encrypted_text = ""

    # Only problem is going to be z -> a

    for char in text:
        encrypted_text += chr(ord(char) + offset)

    print("Text {} : New {}".format(text, encrypted_text))

    return encrypted_text


def decrypt(text, offset):
    pass


def find_encryption_offsets(encrypted_text):
    pass


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

