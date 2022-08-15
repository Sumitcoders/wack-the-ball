from fileinput import close
import time
import screens
import turtle
import random
import pyautogui
from data import *

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
ball.hideturtle()
ball.shape('ball.gif')
ball.color('#fff')
ball.direction = 'stop'
ball.speed = 100
ball.penup()
ball.goto((random.randint(-6,6)*100),(random.randint(-3,3)*100))
ball.a = True
ball.status = 'yes'
ball.invinsible = 'no'
ball.heart = 3
ball.pr = 'resume'
window.ontimer(ball.showturtle,2000)
#hearts
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
window.addshape('images/heart.gif')

heart = window.Turtle()
heart.penup()
heart.speed(0)
heart.shape('images/heart.gif')
heart.goto(500,330)
heart_1 = window.Turtle()
heart_1.penup()
heart_1.speed(0)
heart_1.shape('images/heart.gif')
heart_1.goto(520,330)
heart_2 = window.Turtle()
heart_2.penup()
heart_2.speed(0)
heart_2.shape('images/heart.gif')
heart_2.goto(540,330)


def heart_count():
    if ball.heart == 3:
        heart.showturtle()
        heart_1.showturtle
        heart_2.showturtle()
    elif ball.heart == 2:
        heart.showturtle()
        heart_1.showturtle
        heart_2.hideturtle()
    elif ball.heart == 1:
        heart.showturtle()
        heart_1.hideturtle()
        heart_2.hideturtle()
    elif ball.heart == 0:
        heart.hideturtle()
        heart_1.hideturtle()
        heart_2.hideturtle()
    else:
        exit()

#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````




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
seed.goto(1000,1000)
seed.eaten = 'yes'
seed.x_s = 0
def write(msg):
    txt.clear()
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
    if seed.eaten != 'no' and ball.pr == 'resume':
        x = random.randint(-6,6)
        y = random.randint(-3,3)
        x = x*100
        y = y*100
        seed.goto(x,y)
        seed.showturtle()
        seed.eaten = 'no'
    window.ontimer(summon_seed,25000)
def invinsiblity_over():
    ball.invinsible = 'no'
    ball.shape('ball.gif')
    write('Invinsiblity over')
def seed_collosion():
    if ball.invinsible != 'yes':
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

    
ball.po = 0

def pause_resume(x,y):
    if ball.pr == 'resume':
        ball.pr = 'pause'
        ball.po = pyautogui.position()
    else:
        ball.pr = 'resume'
        
        
        pyautogui.moveTo(ball.po)
    

ball.g = True

        

def over(x,y):
    if ball.invinsible != 'yes' and ball.pr == 'resume':
        ball.heart -= 1
        heart_count()
        if ball.heart == 0:
            ball.g = False
            ball.hideturtle()
            write('GAME OVER')
            time.sleep(3)
            ball.a = False
            exit()


    elif ball.pr == 'pause':
        write("""Don't try to be over smart 
    The game is paused""")
    elif ball.invinsible == 'yes':
        write('The ball is now invinsible')
    else:
        pass 
        

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
win.onclick(pause_resume,2)


window.ontimer(time_over,5000)
###############################################################################################################################
def position():
    window.ontimer(position,1000)
timer = 0
ball.g_timer = random.randint(1000,2000)
score = 0
#position()
shape_seed()

ball.time_s = 0
ball.time_m = 0
def survival():
    if ball.pr != 'pause' and ball.g == True:
        ball.time_s += 1
        if ball.time_s == 60:
            ball.time_s = 0
            ball.time_m += 1
    window.ontimer(survival,1000)
survival()


time_t = window.Turtle()
time_t.penup()
time_t.goto(-600,300)
time_t.color('white')
time_t.hideturtle()

def time_writer():
    time_t.clear()
    msg = str(ball.time_m) + ':' + str(ball.time_s)
    time_t.write(msg,align='center',font=('Mono space', 20, 'bold'))
    window.ontimer(time_writer,1000)
time_writer()
window.ontimer(summon_seed,20000)
################################################################################################################################
while ball.a:
    if ball.pr == 'pause':
        while True:
            window.update()
            if ball.pr == 'resume':
                break
#################################################################################################################################
    '''
    if seed.eaten == 'yes':
        if ball.direction != 'stop':
            timer += 10
            
        timer += 1
        if timer > 100:
            if timer > ball.g_timer:
                ball.g_timer = random.randint(100,200)
                timer = 0
                summon_seed()

    else:
        pass
        seed_collosion()'''
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

print(f'You survived {ball.time_m} minutes and {ball.time_s} seconds')


if minutes == 0 and ball.time_s > seconds:
    seconds = ball.time_s
    f = open('data.py',"w")
    f.write(f'''minutes = 0
seconds = {seconds}''')
    f.close()
if ball.time_m > minutes:
    minutes = ball.time_m
    f = open('data.py',"w")
    f.write(f'''minutes = {minutes}
seconds = {ball.time_s}''')
    f.close()
