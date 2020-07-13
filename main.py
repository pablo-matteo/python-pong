import turtle

field = turtle.Screen()
field.title('Pong')
field.bgcolor('black')
field.setup(width=800, height=600)
field.tracer(0)

player_1_pts = 0
player_2_pts = 0

player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape('square')
player_1.color('white')
player_1.penup()
player_1.goto(-350,0)
player_1.shapesize(stretch_wid=5, stretch_len=1)

player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape('square')
player_2.color('white')
player_2.penup()
player_2.goto(350,0)
player_2.shapesize(stretch_wid=5, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

mid_line = turtle.Turtle()
mid_line.color('white')
mid_line.goto(0,400)
mid_line.goto(0,-400)

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.hideturtle()
pen.goto(0,260)
pen.write(f'player_1: 0          player_2: 0', align='center', font=('Courier', 25, 'normal'))

def player_1_up():
    y = player_1.ycor()
    y+=20
    player_1.sety(y)

def player_1_down():
    y = player_1.ycor()
    y-=20
    player_1.sety(y)

def player_2_up():
    y = player_2.ycor()
    y+=20
    player_2.sety(y)

def player_2_down():
    y = player_2.ycor()
    y-=20
    player_2.sety(y)

field.listen()
field.onkeypress(player_1_up, "w")
field.onkeypress(player_1_down, "s")

field.onkeypress(player_2_up, "Up")
field.onkeypress(player_2_down, "Down")

while True:
    field.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if (ball.ycor() > 290):
        ball.dy *= -1
    if (ball.ycor() < -290):
        ball.dy *= -1
    if (ball.xcor() > 390):
        ball.goto(0,0)
        ball.dx *= -1
        player_1_pts += 1
        pen.clear()
        pen.write(f'player_1: {player_1_pts}            player_2: {player_2_pts}', align='center', font=('Courier', 25, 'normal'))
    if (ball.xcor() < -390):
        ball.goto(0,0)
        ball.dx *= -1
        player_2_pts += 1
        pen.clear()
        pen.write(f'player_1: {player_1_pts}            player_2: {player_2_pts}', align='center', font=('Courier', 25, 'normal'))
        
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< player_2.ycor() + 50) and (ball.ycor()> player_2.ycor()-50):
        ball.dx *= -1
        
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< player_1.ycor() + 50) and (ball.ycor()> player_1.ycor()-50):
        ball.dx *= -1