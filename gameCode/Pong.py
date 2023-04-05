import turtle

gs = turtle.Screen()
gs.title("Osinum Pong Game")
gs.bgcolor("black")
gs.setup(width=800, height=600)
gs.tracer(0)

# Paddle A

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)

dx_Value = 2
dy_Value = -2
ball.dx = dx_Value
ball.dy = dy_Value


# Functions
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard binding
gs.listen()
gs.onkeypress(paddleA_up, 'w')
gs.onkeypress(paddleA_down, 's')
gs.onkeypress(paddleB_up, 'Up')
gs.onkeypress(paddleB_down, 'Down')

# Main Game
while True:
    gs.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        
    # Paddle B and ball check
    checkX = ball.xcor() < 350 and ball.xcor() > 340
    checkY = ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40
    if (checkX and checkY):  # check for paddle B
        ball.setx(340)
        ball.dx *= -1

    # Paddle A and ball check
    checkX = ball.xcor() > -350 and ball.xcor() < -340
    checkY = ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40
    if (checkX and checkY):  # check for paddle A
        ball.setx(-340)
        ball.dx *= -1
