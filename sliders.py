from turtle import Turtle,Screen

screen=Screen()

class Sliders:
    def __init__(self):
        self.segments=[]
        for i in range(3):
            new_obj=Turtle("square")            
            new_obj.color("white")
            new_obj.penup()
            self.segments.append(new_obj)

    def default_pos(self):
        
        x_cor=screen.window_width()/2
        y_cor=30
        for i in range(3):
            new_obj_one=Sliders()
            new_obj_one.segments[i].goto(x=-x_cor+30,y=y_cor)
            y_cor-=20
    
        x_cor=screen.window_width()/2
        y_cor=30
        for i in range(3):
            new_obj_two=Sliders()
            new_obj_two.segments[i].goto(x=x_cor-30,y=y_cor)
            y_cor-=20
