import random
import time

user_pts = 0
computer_pts = 0

def reveal_answers():
    print("rock")
    time.sleep(1)
    print("paper")
    time.sleep(1)
    print("scissors")
    time.sleep(1)
    print("shoot")
    print("Your choice: " + user_choice)
    print("Computer choice: " + computer_choice)
    if computer_choice == "scissors" and user_choice == "scissors":
        print("Tie!")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You won the round!")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lost the round!")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("You lost the round!")
    elif computer_choice == "rock" and user_choice == "rock":
        print("Tie!")
    elif computer_choice == "rock" and user_choice == "paper":
        print("You won the round!")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You won the round!")
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lost the round!")
    elif computer_choice == "paper" and user_choice == "paper":
        print("Tie!")

while True:
    want_to_play = input("Do you want to play 'rock, paper, scissors' ? Answer yes or no: ")
    if want_to_play == "yes":
        break
    elif want_to_play == "no":
        quit()
    else:
        print("Invalid answer")
        continue

while True:

    computer_options = ["rock", "paper", "scissors"]
    computer_choice = computer_options[random.randint(0,2)]

    user_choice = input("Enter your choice or enter 'end' to end the game: ")

    if user_choice == "end":
        if computer_pts > user_pts:
            print("-----------------------")
            print("You lost!")
            print("Your point: " + str(user_pts))
            print("Computer points: " + str(computer_pts))
        elif computer_pts < user_pts:
            print("-----------------------")
            print("You won!")
            print("Your point: " + str(user_pts))
            print("Computer points: " + str(computer_pts))
        elif computer_pts == user_pts:
            print("-----------------------")
            print("Tie!")
            print("Your point: " + str(user_pts))
            print("Computer points: " + str(computer_pts))
        break
    elif user_choice == "rock" or user_choice == "scissors" or user_choice == "paper":
        if computer_choice == "scissors" and user_choice == "scissors":
            reveal_answers()
        elif computer_choice == "scissors" and user_choice == "rock":
            reveal_answers()
            user_pts += 1
        elif computer_choice == "scissors" and user_choice == "paper":
            reveal_answers()
            computer_pts += 1
        elif computer_choice == "rock" and user_choice == "scissors":
            reveal_answers()
            computer_pts += 1
        elif computer_choice == "rock" and user_choice == "rock":
            reveal_answers()
        elif computer_choice == "rock" and user_choice == "paper":
            reveal_answers()
            user_pts += 1
        elif computer_choice == "paper" and user_choice == "scissors":
            reveal_answers()
            user_pts += 1
        elif computer_choice == "paper" and user_choice == "rock":
            reveal_answers()
            computer_pts += 1
        elif computer_choice == "paper" and user_choice == "paper":
            reveal_answers()
    else:
        print("Invalid choice")
        continue



quitting_winow = input("Press enter to exit \n\n\n")
