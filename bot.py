import turtle
import random
window = turtle



def manual():
    #shapes

    window.addshape('ball.gif')

    win = turtle.Screen()

    win.setup(width=600,height=300)
    win.bgcolor('black')
    ball = window.Turtle()
    ball.shape('ball.gif')
    ball.direction = 'stop'
    ball.speed = 1
    ball.penup()
    ball.a = True
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
    def boost():
        ball.speed = ball.speed + 1

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
def bot():
    import turtle
    import random
    window = turtle




    #shapes

    window.addshape('ball.gif')
    win = turtle.Screen()
    #win.bgpic('background.gif')
    win.setup(width=600,height=300)
    win.bgcolor('black')
    ball = window.Turtle()
    ball.shape('ball.gif')
    ball.color('white')
    ball.direction = 'stop'
    ball.speed = 1
    ball.penup()
    ball.a = True
    #functions


    def boost():
        ball.speed = ball.speed + 1

    def over(x,y):
        ball.a = False
    def random_direction():
        rd = random.randint(1,4)
        if rd == 1:
            ball.direction = 'right'
        if rd == 2:
            ball.direction = 'left'
        if rd == 3:
            ball.direction = 'up'
        if rd == 4:
            ball.direction = 'down'
        window.ontimer(random_direction,random.randint(500,700))
    

    #keys
    window.listen()
    window.onkeypress(boost,'l')

    ball.onclick(over)




    random_direction()
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
        
