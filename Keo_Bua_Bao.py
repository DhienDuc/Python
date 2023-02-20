import random

def get_choices():
    player_choice = input("Enter a choice (Rock,Paper,Scissors) : ")
    option = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(option)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "-> It's a tie!"
    elif player == "Rock":
        if computer == "Scissors":
            return "-> Player win!"
        else:
            return "-> Computer win!"
    elif player == "Paper":
        if computer == "Scissors":
            return "-> Computer win!"
        else:
            return "-> Player win!"
    elif player == "Scissors":
        if computer == "Rock":
            return "-> Computer win!"
        else:
            return "-> Player win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)