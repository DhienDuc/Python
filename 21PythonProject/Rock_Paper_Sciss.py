import random

# initial variables
user_wins, computer_wins = 0, 0
options = ["rock", "paper", "scissor"]

while True:
    # get user input in lowercase
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()

    # quit if ipunt = 'q'
    if user_input == "q":
        break

    # check input not valid
    if user_input not in options:
        continue

    # random number
    rand_num = random.randint(0, 2)
    # rock : 0, paper : 1, scissor : 2
    computer_pick = options[rand_num]

    # check user vs computer
    if user_input == computer_pick:
        print("Computer pick {}. Nobody win!".format(computer_pick))
    elif user_input == "rock" and computer_pick == "scissor":
        print("Computer pick {}. You win!".format(computer_pick))
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("Computer pick {}. You win!".format(computer_pick))
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("Computer pick {}. You win!".format(computer_pick))
        user_wins += 1
    else:
        print("Computer pick {}. You lost!".format(computer_pick))
        computer_wins += 1

# Result output
print("User won :", user_wins)
print("Computer won :", computer_wins)