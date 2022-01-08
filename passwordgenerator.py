import random
import keyboard
import time

def random_password():
    # Variables values
    password_character = "!@#$%?&*()"
    password_number = "1234567890"
    password_lower_letters = "qwertyuiopasdfghjklzxcvbnmèà"
    password_upper_letters = "QWERTYUIOPASDFGHJKLZXCVBNMÈÀ"
    password = ""

    password_character_lenght = random.randint(4, 5)
    password_number_lenght = random.randint(4, 5)
    password_lower_letter_lenght = random.randint(4, 5)
    password_upper_letter_lenght = random.randint(4, 5)

    password_lenght = password_character_lenght + password_number_lenght + password_lower_letter_lenght + password_upper_letter_lenght

    # Characters
    for i in range(0, password_character_lenght):
        random_index = random.randint(0, len(password_character)-1)
        password += password_character[random_index]

    # Numbers
    for i in range(0, password_number_lenght):
        random_index = random.randint(0, len(password_number)-1)
        password += password_number[random_index]

    # Lower letter
    for i in range(0, password_lower_letter_lenght):
        random_index = random.randint(0, len(password_lower_letters)-1)
        password += password_lower_letters[random_index]

    # Upper letter
    for i in range(0, password_upper_letter_lenght):
        random_index = random.randint(0, len(password_upper_letters)-1)
        password += password_upper_letters[random_index]

    # Shuffle
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ""
    for char in password_list:
        final_password += char

    print(final_password)
    print("Press g to generate a new password or q to quit")

    while True:
        time.sleep(0.7)
        if keyboard.read_key() == "g":
            random_password()
            break
        elif keyboard.read_key() == "q":
            exit()
        else:
            continue


random_password()
