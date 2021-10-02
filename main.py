from turtle import Screen,Turtle
from screen_split import ScreenSplit
from sliders import Sliders

# initializations
screen=Screen()

# creating the output screen
screen.screensize()
screen.setup(height=0.99,width=1.0)
screen.bgcolor("black")
screen.title("Pong Arcade Game")
screen.tracer(0)

# spliting screen
split=ScreenSplit()
split.split()

#setting default sliders position
sliders=Sliders()
sliders.default_pos()


screen.update()


screen.exitonclick()