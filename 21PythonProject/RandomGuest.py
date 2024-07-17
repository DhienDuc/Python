import random

# get user input
top_of_range = input("Type a number: ")

# check user input is a digit
if top_of_range.isdigit():
    # convert string from input to int
    top_of_range = int(top_of_range)
    # check top of range
    if top_of_range <= 0:
        print("Please type a number > 0 next time.")
        quit()
# incase input not a digit     
else:
    print("Please type a number next time.")
    quit()

# create random number
random_num = random.randint(0, top_of_range)

# count guess time
guess = 0

# user input guess number process
while True:
    # update guess time
    guess += 1

    # get guess input
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    # check random vs guess number to break
    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess > random_num:    
        print("It's somewhere above!")
    else:
        print("It's somewhere below!")

print("You got it in", guess, "times")
