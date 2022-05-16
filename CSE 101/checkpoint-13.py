the_message = input('What to do today?')

def display_regular():
    print(the_message)


def display_uppercase():
    message_upper = the_message.upper()
    print(message_upper)


def display_lowercase():
    print(the_message.lower())

display_regular()

display_uppercase()

display_lowercase()