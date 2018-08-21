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
    return offset.isdigit()

def mutated_msg():
    pass




##############################################################################
##############################################################################
# TODO: make funcs call print, Check docmentation
def oop_func_menu():
    pass


def encrypt(text, offset):
    return "encrypt"


def decrypt(text, offset):
    return "decrypt"


def auto_decrypt(text, offset):
    return "auto"

if __name__ == '__main__':
   # imparative_menu()
   procedual_menu()
