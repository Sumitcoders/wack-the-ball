import winsound
import screens
import turtle
import random


window = turtle


############################################################################################################################
































screens.title_screen()







#shapes

window.addshape('ball.gif')
window.addshape('ball_invinsible.gif')
window.addshape('ball_invisible.gif')
win = turtle.Screen()

win.setup(width=600,height=300)
win.bgcolor('black')
ball = window.Turtle()
ball.shape('ball.gif')
ball.color('#fff')
ball.direction = 'stop'
ball.speed = 100
ball.penup()
ball.a = True
ball.status = 'yes'
ball.invinsible = 'no'




txt = window.Turtle()
txt.color('white')
txt.hideturtle()

b = window.Turtle()
b.shape('square')
b.color('#fff')
b.penup()
b.speed(100)
b.goto(650,0)
b.l = 10
b.w = 0.5

#invinsiblity seed
###################################################################################################
window.addshape('images/mystry.gif')
window.addshape('images/mystry_1.gif')

shape = ['images/mystry.gif','images/mystry_1.gif']



seed = window.Turtle()
seed.shape('square')
seed.color('#f90233')
#seed.hideturtle()
seed.penup()
seed.speed(1000)
# seed.shapesize(1.6,1.6)
seed.goto(1000,1000)
seed.eaten = 'yes'
seed.x_s = 0
def write(msg):
    txt.write(msg,align='center',font=('Mono space', 14, 'italic'))
    window.ontimer(txt.clear,3000)
def shape_seed():
    if seed.x_s < len(shape):
        seed.shape(shape[seed.x_s])
        seed.x_s += 1
        if seed.x_s == len(shape):
            seed.x_s = 0
    window.ontimer(shape_seed,500)

def summon_seed():
    x = random.randint(-6,6)
    y = random.randint(-3,3)
    x = x*100
    y = y*100
    seed.goto(x,y)
    seed.showturtle()
    seed.eaten = 'no'
def invinsiblity_over():
    ball.invinsible = 'no'
    ball.shape('ball.gif')
    write('Invinsiblity over')
def seed_collosion():
    if ball.xcor() + 2 > seed.xcor() - 10 and ball.xcor() - 2 < seed.xcor() + 10:
        if ball.ycor() + 2 >seed.ycor() - 10 and ball.ycor() - 2 < seed.ycor() + 10:
            seed.eaten = 'yes'
            seed.goto(1000,1000)
            ball.invinsible = 'yes'
            write('The ball is now invinsible')
            ball.shape('ball_invinsible.gif')
            window.ontimer(invinsiblity_over,10000)
            #summon_seed()











####################################################################################################

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
def time_over():
    ball.status = 'no'
def size():
    if b.l > 4:
        b.l -= 0.01
        window.ontimer(size,1)

def boost_over():
    ball.pensize(0)
    window.ontimer(ball.clear, 2000)
    ball.showturtle()
    ball.penup()
    ball.clear()
    b.l = 10
    window.ontimer(time_over,10000)
    size()
    if ball.shape() == 'ball_invisible.gif':
        ball.shape('ball.gif')

    
    
def boost():
    if ball.status == 'no':
        ball.status = 'yes'
        ball.shape('ball_invisible.gif')
        ball.pendown()
        window.ontimer(boost_over,5000)
    else:
        write("can't use, boost on timer")

        
# msg1 = 'hello'
# ball.write(msg1, align="center", font=("Mono Space",14,"bold"))
# window.ontimer(ball.clear,1000)

    


    
    



        

def over(x,y):
    if ball.invinsible != 'yes':
        ball.a = False
        exit()
    else:
        write('The ball is now invinsible')
        

#keys
window.listen()
#alphabets
window.onkeypress(up, 'w')
window.onkeypress(down, 's')
window.onkeypress(left, 'a')
window.onkeypress(right, 'd')
#window.onkeypress(stop,'c')
window.onkeypress(boost,'f')

#arrow keys

window.onkeypress(up, 'Up')
window.onkeypress(down, 'Down')
window.onkeypress(left, 'Left')
window.onkeypress(right, 'Right')
#window.onkeypress(stop,'c')
window.onkeypress(boost,'0')

ball.onclick(over)


window.ontimer(time_over,5000)
###############################################################################################################################
def position():
    window.ontimer(position,1000)
timer = 0
score = 0
#position()
shape_seed()
################################################################################################################################
while ball.a:
#################################################################################################################################
    if seed.eaten == 'yes':
        if ball.direction != 'stop':
            timer += 10
            
        timer += 1
        if timer > 200:
            if timer > random.randint(200,250):
                timer = 0
                summon_seed()

    else:
        pass
        seed_collosion()
    
#################################################################################################################################
    
    b.shapesize(b.l,b.w)
    if ball.status == 'no':
        b.l = 4
        b.color('green')
    else:
        b.color('red')
    if ball.direction != 'stop':
        score += 1






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


print(score)
