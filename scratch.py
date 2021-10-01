from turtle import Screen, exitonclick
import turtle

screen=Screen()
screen_split=turtle.Turtle()
for i in range (10):
    screen_split.fd(10)
    screen_split.pendown()

    screen_split.fd(10)
    screen_split.penup()

screen,exitonclick()