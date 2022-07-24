
import turtle
tr = turtle.Turtle()
tr.hideturtle()
tr.x = 0
class enemy(turtle.Turtle):
        
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        shape = ['circle','square'] 
        turtle.shape(shape[tr.x])   
        tr.x = tr.x+1   
        if tr.x > 1:
            tr.x = 0
        self.shapesize(stretch_len=1,stretch_wid=1)
        turtle.ontimer(self.__init__,500)
    

t = enemy()

while True:
    
    
    turtle.update()
