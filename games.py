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
paddle_A.penup()
paddle_A.goto(-350,0)

# Paddle B

# Ball


# Main game loop
while True:
    wn.update()