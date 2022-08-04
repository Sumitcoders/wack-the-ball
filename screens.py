import turtle


window = turtle
window.addshape('ball.gif')
window.addshape('cursor.gif')
window.addshape('images/move.gif')



def instruction():
    window.tracer(0)
    screen = turtle.Screen()
    screen.setup(600,400)
    screen.bgcolor('#fff')
    txt = window.Turtle()
    txt.penup()
    txt.hideturtle()
    #txt.goto(-90,150)
    def writer(msg,x,y):
        txt.goto(x,y)
        txt.write(msg,align='center',font=('Mono space', 20, 'italic'))
    """txt.write('''Move with w,a,s,d
    or arrow key
    ''',align='center',font=('Mono space', 20, 'italic'))"""
    writer('''Move with w,a,s,d
    or arrow key''',-90,150)

    # instructions
    window.addshape('images/g.gif')
    move = window.Turtle()
    move.shape('images/move.gif')
    move.penup()
    move.goto(-350,200)
    g = window.Turtle()
    g.shape('images/g.gif')
    g.penup()
    g.goto(-120,-100)
    writer('''Watch that bar to 
    turn green''',-380,-150)

    window.addshape('images/hide.gif')
    hide = window.Turtle()
    hide.penup()
    hide.shape('images/hide.gif')
    hide.goto(500,-50)
    writer('''Use the ablity to hide
    from the cursor''',220,-50)

    window.addshape('images/seed.gif')
    seed = window.Turtle()
    seed.shape('images/seed.gif')
    seed.penup()
    seed.goto(400,250)
    writer('''Eat that seed to 
    get invinsible''',140,250)


    while True:
        

        window.update()
        
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
            print('this is the prob')
            cursor.goto(-100,100)
            cursor.showturtle()
            cursor.speed(1)
            cursor.goto(-360,-7)
            ball.hideturtle()
            cursor.hideturtle()

            
        ball.turn += 1
        if ball.turn == 5:
            ball.turn = 1
            
        if ball.a == True:
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
    window.addshape('images/instructions.gif')
    def click_i(x,y):
        screen.clear()
        instruction()
    instruction_s = window.Turtle()
    instruction_s.shape('images/instructions.gif')
    instruction_s.penup()
    instruction_s.goto(0,-200)

    window.listen()
    screen.onclick(game)
    instruction_s.onclick(click_i)
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
