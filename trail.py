import turtle

window = turtle




#shapes

window.addshape('ball.gif')

win = turtle.Screen()

win.setup(width=600,height=300)
win.bgcolor('black')
ball = window.Turtle()
ball.shape('ball.gif')
ball.color('#fff')
ball.direction = 'stop'
ball.speed = 10
ball.penup()
ball.a = True
ball.hide_status = 'no'
#functions

def up():
    ball.direction = 'up'
def down():
    ball.direction = 'down'
def left():
    ball.direction = 'left'
def right():
    ball.direction = 'right'
def stop():
    ball.direction = 'stop'
def boost_over():
    
    ball.showturtle()
    ball.clear()
    ball.penup()
def boost_again():
    ball.hide_status = 'no'
def boost():
    if ball.hide_status != 'yes':
        ball.hideturtle()
        ball.pencolor('#fff')
        ball.pendown()
        ball.hide_status = 'yes'
    window.ontimer(boost_over,5000)
    window.ontimer(boost_again,15000)

def over(x,y):
    ball.a = False
        

#keys
window.listen()
window.onkeypress(up, 'w')
window.onkeypress(down, 's')
window.onkeypress(left, 'a')
window.onkeypress(right, 'd')
window.onkeypress(stop,'f')
window.onkeypress(boost,'l')

ball.onclick(over)





while ball.a:






    #movements
        
    if ball.direction == 'up':
        ball.goto(ball.xcor(),ball.ycor()+ball.speed)
    if ball.direction == 'down':
        ball.goto(ball.xcor(),ball.ycor()-ball.speed)
    if ball.direction == 'left':
        ball.goto(ball.xcor()-ball.speed,ball.ycor())
    if ball.direction == 'right':
        ball.goto(ball.xcor()+ball.speed,ball.ycor())
        
        
    #boundary
    if ball.xcor() >  600 :
        ball.direction = 'left'
    if ball.xcor() <  -600 :
        ball.direction = 'right'
    if ball.ycor() >  300 :
        ball.direction = 'down'
    if ball.ycor() <  -300 :
        ball.direction = 'up'

    window.update()