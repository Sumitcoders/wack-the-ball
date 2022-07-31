from re import S
import turtle


window = turtle
window.addshape('ball.gif')
window.addshape('cursor.gif')
def title_screen():
    screen = window.Screen()
    screen.bgcolor('black')
    screen.setup(width=600,height=400)
    ball = window.Turtle()
    ball = window.Turtle()
    ball.shape('ball.gif')
    ball.direction = 'stop'
    ball.turn = 1
    ball.penup()
    ball.speed(0)
    ball.speed = 1
    ball.goto(-200,0)
    ball.a = True
    cursor = window.Turtle()
    cursor.shape('cursor.gif')
    cursor.hideturtle()
    cursor.penup()
    def direction():
        if ball.turn == 1:
            ball.showturtle()
            ball.direction = 'up'
        elif ball.turn == 2:
            ball.direction = 'left'
        elif ball.turn == 3:
            ball.direction = 'down'
        else:
            ball.direction = 'right'
            cursor.goto(-100,100)
            cursor.showturtle()
            cursor.speed(1)
            cursor.goto(-360,-7)
            ball.hideturtle()
            cursor.hideturtle()
            
        ball.turn += 1
        if ball.turn == 5:
            ball.turn = 1
        window.ontimer(direction, 3000)
    def game(x,y):
        print('ok')
        ball.a = False
        screen.clear()
        
    direction()
    txt = window.Turtle()
    txt.hideturtle()
    txt.color('#fff')
    txt.shape('square')
    txt.penup()
    txt.shapesize(20,20)
    txt.write('Wack the ball',align='center',font=('Mono space', 40, 'italic'))
    txt.goto(0,-100)
    txt.write('Click anywhere to start',align='center',font=('Mono space',10,'italic'))

    

    window.listen()
    screen.onclick(game)
    while ball.a:
        if ball.direction == 'up':
            ball.goto(ball.xcor(),ball.ycor()+ball.speed)
        if ball.direction == 'down':
            ball.goto(ball.xcor(),ball.ycor()-ball.speed)
        if ball.direction == 'left':
            ball.goto(ball.xcor()-ball.speed,ball.ycor())
        if ball.direction == 'right':
            ball.goto(ball.xcor()+ball.speed,ball.ycor())
        print(ball.xcor(),ball.ycor())
        window.update()

