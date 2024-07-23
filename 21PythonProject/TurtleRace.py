import turtle
import time
import random

# define window dimension
WIDTH, HEIGHT = 500, 500

# turtle color list
COLOR = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

# initial window
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race!")

# get number of racers from input
def get_number_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in range 2-10!")

# create object
def create_turtle(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        # create object
        racer = turtle.Turtle()
        # set color
        racer.color(color)
        # set shape
        racer.shape('turtle')
        # turn left 90 degrees
        racer.left(90)
        # not draw moment line
        racer.penup()
        # set object position
        racer.setpos(-WIDTH//2 + (i+1)* spacing, -HEIGHT//2 + 20)
        racer.pendown()
        # add to list
        turtles.append(racer)
    return turtles

# racer funtion
def race(colors):
    turtles = create_turtle(colors)
    # move turtle
    while True:
        for racer in turtles:
            # make turtle move with random speed
            speed = random.randrange(1, 20)
            racer.forward(speed)

            # check pos of turtle
            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]

# call function
racers = get_number_racers()
init_turtle()
# make random color list
random.shuffle(COLOR)
colors = COLOR[:racers]
# race and announce winner
winner = race(colors)
print("Winner is", winner)
time.sleep(5)








 

    