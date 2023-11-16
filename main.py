from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)

user_choice = screen.textinput(title="Choose your turtle!", prompt="Which turtle will win the race?")
colors = ['red','orange','yellow','green','blue','purple']
y_coordinates = [-100, -60, -20, 20, 60, 100]

for t in range(0,6):
    carl = Turtle(shape="turtle")
    carl.color(colors[t])
    carl.penup()
    carl.goto(x=-230, y= y_coordinates[t])



screen.exitonclick()