from turtle import Screen
import turtle

# initializations
screen=Screen()

# creating the output screen
screen.screensize()
screen.setup(height=0.99,width=1.0)
screen.bgcolor("black")
screen.title("Pong Arcade Game")
screen.tracer(0)

# screen splitting 
screen_split=turtle.Turtle()
screen_split.penup()
screen_split.color("white")
screen_split.hideturtle()
# screen_split.goto(x=-1.0,y=-2.0)
screen_split.pensize(15)
screen_split.setheading(90)
while True:
    screen_split.pendown()
    screen_split.fd(10)
    screen_split.penup()
    screen_split.fd(10)

screen.update()


screen.exitonclick()