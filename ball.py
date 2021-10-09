from turtle import Turtle,Screen

screen=Screen()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.ball=Turtle("circle")
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1.5,stretch_wid=1.5)
        self.penup()
        self.multiplier_x=1
        self.multiplier_y=1

    def move_ball(self):
        self.goto(self.xcor()+(self.multiplier_x*0.35),self.ycor()+(self.multiplier_y*0.35))
        
    def collision(self):
        if self.ycor()<(-1*screen.window_height()/2)+28:
            self.multiplier_y*=-1
        elif self.ycor()>(screen.window_height()/2)-28:
            self.multiplier_y*=-1

        # elif self.ball.xcor()>screen.window_width()/2-50 :
        #     self.multiplier_x*=-1

        # elif self.ball.xcor()<-1*screen.window_width()/2+50:
        #     self.multiplier_x*=-1