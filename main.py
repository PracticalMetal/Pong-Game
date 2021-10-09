from turtle import Screen,Turtle
from screen_split import ScreenSplit
from sliders import Sliders
from ball import Ball

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
slider_one=Sliders()
slider_one.default_pos(x_cor = screen.window_width()/2)
slider_two=Sliders()
slider_two.default_pos(x_cor = -1*screen.window_width()/2)

#settin up the ball
ball=Ball()

# moving the sliders from the keyboard
screen.listen()
screen.onkey(fun=slider_one.move_up,key="Up")
screen.onkey(fun=slider_one.move_down,key="Down")
screen.onkey(fun=slider_two.move_up,key="w")
screen.onkey(fun=slider_two.move_down,key="s")

# game mechanism
game_is_one=True
while game_is_one:
    screen.update()

screen.update()


screen.exitonclick()