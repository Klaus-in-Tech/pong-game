import turtle

wn = turtle.Screen()
wn.title('Pong by Klaus')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape('square')
paddle_A.color('white')
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape('square')
paddle_B.color('white')
paddle_B.shapesize(stretch_wid=5,stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

# Move Paddle A up
def paddle_A_up():
    y= paddle_A.ycor()
    y+=20
    paddle_A.sety(y)

# Move Paddle A down
def paddle_A_down():
    y= paddle_A.ycor()
    y-=20
    paddle_A.sety(y)

# Move Paddle B up
def paddle_B_up():
    y= paddle_B.ycor()
    y+=20
    paddle_B.sety(y)
    
# Move Paddle B down
def paddle_B_down():
    y= paddle_B.ycor()
    y-=20
    paddle_B.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_A_up ,"w")
wn.onkeypress(paddle_A_down,"z")
wn.onkeypress(paddle_B_up ,"o")
wn.onkeypress(paddle_B_down,"m")

# Main game loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40)  and (ball.ycor() > paddle_B.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40)  and (ball.ycor() > paddle_B.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1