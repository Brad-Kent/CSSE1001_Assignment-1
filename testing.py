# Menu

main_menu_options = {
    "e": "e) Encrypt some text",
    "d": "d) Decrypt some text",
    "a": "a) Automatically decrypt English text",
    "q": "q) Quit"
}





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

main_menu_sub = {
    "enter" : "Please enter some text to {}:",
    "result" : "The {} text is:",
    "offset" : "Please enter a shift offset (1-25):",
    "options" : "Please choose an option [e/d/a/q]:",
    "q" : "Bye!"
}

main_menu_sub1 = {
    "inputs" : ["Please enter some text to {}:", "The {}ed text is:", "Please enter a shift offset (1-25):"],
    "e" : "encrypt",
    "d" : "decrypt"
}

sub_menu = []


def menu_loop():
    print("Welcome")

    while True:
        # Display Menu Options
        print(main_menu_sub["options"])
        for text in main_menu_options.values():
            print(text)

        # Get User Input
        user_choice = input(">")

        # Check to see if input is a valid command
        if user_choice not in main_menu_options.keys():
            print("Invalid Command")
            continue


        # Options Determine
        if user_choice == 'a':




def get_main_menu_subs(sub_menu):
    pass


if __name__ == '__main__':
    menu_loop()