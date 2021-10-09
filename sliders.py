from turtle import Turtle, Screen

screen = Screen()


class Sliders:
    def __init__(self):
        self.slider = Turtle()

    def default_pos(self, x_cor):

        if x_cor < 0:
            self.slider.shape("square")
            self.slider.color("white")
            self.slider.shapesize(stretch_len=1, stretch_wid=6)
            self.slider.penup()
            self.slider.goto(x=x_cor+30, y=0)

        else:
            self.slider.shape("square")
            self.slider.color("white")
            self.slider.shapesize(stretch_len=1, stretch_wid=6)
            self.slider.penup()
            self.slider.goto(x=x_cor-30, y=0)



    def move_up(self):
        self.slider.goto(self.slider.xcor(),self.slider.ycor()+20)

    def move_down(self):
        self.slider.goto(self.slider.xcor(),self.slider.ycor()-20)
