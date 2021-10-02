from turtle import Turtle,Screen

screen=Screen()

class Sliders:
    def __init__(self):
        self.segments_one=[]
        self.segments_two=[]
        

    def default_pos(self):
        
        x_cor=screen.window_width()/2
        y_cor=90
        for i in range(14):
            if i<7:
                new_obj=Turtle("square")
                new_obj.color("white")
                new_obj.penup()
                new_obj.goto(x=-x_cor+30,y=y_cor)
                y_cor-=20
                self.segments_one.append(new_obj)
            
            else:
                new_obj=Turtle("square")
                new_obj.color("white")
                new_obj.penup()
                new_obj.goto(x=x_cor-30,y=y_cor)
                y_cor+=20
                self.segments_one.append(new_obj)
                # reversing the list to make both the lists homogeneous
                self.segments_two=self.segments_two[::-1]

    
        
