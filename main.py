from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

raceOngoing = False

user_choice = screen.textinput(title="Choose your turtle!", prompt="Which turtle will win the race?")
colors = ['red','orange','yellow','green','blue','purple']
y_coordinates = [-100, -60, -20, 20, 60, 100]
turtleList = []

for t in range(0,6):
    racerTurtle = Turtle(shape="turtle")
    racerTurtle.color(colors[t])
    racerTurtle.penup()
    racerTurtle.goto(x=-230, y= y_coordinates[t])
    turtleList.append(racerTurtle)    

if user_choice:
    raceOngoing = True                          # raceOngoing check starts here because the game should only start after the user has chosen a choice

while raceOngoing:
    for turtle in turtleList:
        randomDistance = random.randint(0,10)
        turtle.forward(randomDistance)
        if turtle.xcor() > 230:
            winner = turtle.color()[0]
            raceOngoing = False 

if winner == user_choice:
    print(f"Congrats, your turtle {winner} won!")
else:
    print(f"You lost! The winner is {winner}")

screen.exitonclick()