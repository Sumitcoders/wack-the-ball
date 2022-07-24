import turtle
import random
import bot
window = turtle




mode = input('type 1 for manual game and 2 to play the game with bot: ')
if mode == '1':
    bot.manual()
elif mode == '2':
    bot.bot()
else:
    print('sorry')





















'''

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
    


    '''
