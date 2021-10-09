from turtle import Turtle,Screen

screen=Screen()

class Ball:
    def __init__(self):
        self.ball=Turtle("circle")
        self.ball.color("white")
        self.ball.penup()
