def imparative_menu():

    print("Welcome")

    while True:
        # Display Menu Options
        print("Please choose an option [e/d/a/q]:")
        print("  e) Encrypt some text")
        print("  d) Decrypt some text")
        print("  a) Automatically decrypt English text")
        print("  q) Quit")

        # Get User Input
        user_input = input(">")
            # Check to see if input is a valid command
        menu_options = ['e', 'd', 'a', 'q']
        if user_input not in menu_options:
            print("Invalid Command \n")
            continue

        # Execute user specified sub-program
        text = ""
        offset = 0
        text_mutated = ""

        if user_input == menu_options[0]:
            text = input("Please enter some text to encrypt:")
            offset = int(input("Please enter a shift offset (1-25):"))
            text_mutated = encrypt(text, offset)
            print("The encrypted text is: {}".format(text_mutated))

        elif user_input == menu_options[1]:
            text = input("Please enter some text to decrypt:")
            offset = int(input("Please enter a shift offset (1-25):"))
            text_mutated = decrypt(text, offset)
            print("The decrypted text is: {}".format(text_mutated))

        elif user_input == menu_options[2]:
            # Needs more options
            text = input("Please enter some text to decrypt:")
            offset = int(input("Please enter a shift offset (1-25):"))
            text_mutated = auto_decrypt(text, offset)
            print("The decrypted text is: {}".format(text_mutated))

        else:
            break

        # Repeat
        input()

##############################################################################
##############################################################################


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


# I could make the loop just functions calls to said commands
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


def mutated_msg():
    pass


##############################################################################
##############################################################################


# TODO: make funcs call print, Check docmentation
def oop_func_menu():
    pass

# Could make decrtypt a negative of encrypt: make offset negative??
def encrypt(text, offset):
    enctypted_string = ""

    if not text.isupper():
        text = text.upper()

    for char in text:
        # Find the Encrypted Char: current chat + offset (ASCII)
        encrypted_loc = ord(char) + offset
        print("Loc:", encrypted_loc)
        if encrypted_loc > ord('Z'):
            encrypted_loc -= 26
            print("Loc1:", encrypted_loc)

        enctypted_string += chr(encrypted_loc)
    return enctypted_string


def decrypt(text, offset):
    return "decrypt"


def auto_decrypt(text, offset):
    return "auto"



def testing():
    text = "ABzxc"
    print(encrypt(text, 1))


if __name__ == '__main__':
   # imparative_menu()
   #procedual_menu()
   testing()
