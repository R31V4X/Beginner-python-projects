import random

# Starting
print("Hi user! Wanna play GuessTheNumber?")

wanna_play = False
while wanna_play == False:
    yes_no = input("Enter yes to play or no to quit: ")
    if yes_no == "yes":
        wanna_play = True
    elif yes_no == "no":
        exit()
    else:
        print("invalid answer")

# Game
computer_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter your guess: "))
    except:
        print("Error: your input is invalid")
        break

    if guess == computer_number:
        print("You won!")
        break
    elif guess < computer_number:
        print("Number too low")
        continue
    elif guess > computer_number:
        print("Number too high")
        continue
        



