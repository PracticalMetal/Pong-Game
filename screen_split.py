from turtle import Turtle,Screen

screen=Screen()

class ScreenSplit():
    def __init__(self):
        self.screen_split=Turtle()
        self.screen_split.color("white")
        self.screen_split.penup()
        self.screen_split.setheading(90)
        self.screen_split.hideturtle()
        self.screen_split.goto(x=0,y=-screen.window_height()/2+20)
        self.screen_split.pensize(5)

    def split(self):
        while self.screen_split.ycor()<screen.window_height()/2-20:
            self.screen_split.pendown()
            self.screen_split.fd(20)
            self.screen_split.penup()
            self.screen_split.fd(20)