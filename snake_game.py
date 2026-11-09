import random
import time
import turtle

# board
board = turtle.Screen()
board.title("Snake Game")
board.bgcolor("black")
board.setup(width=600, height=600)
board.setworldcoordinates(-300, -300, 300, 300)
board.tracer(0)

# snake_head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
x = random.randint(-14, 14)*20
y = random.randint(-14, 14)*20
food.goto(x,y)

bodies = []

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

board.listen()
board.onkeypress(go_up, "Up")
board.onkeypress(go_down, "Down")
board.onkeypress(go_left, "Left")
board.onkeypress(go_right, "Right")

def add_body(bodies):
    new_body = turtle.Turtle()
    new_body.speed(0)
    new_body.shape("square")
    new_body.color("lightgreen")
    new_body.penup()
    bodies.append(new_body)

def move_body(bodies):
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

def check_collisions(bodies):
    for body in bodies:
        if body.distance(head) < 20:
            reset_game()

def reset_game():
    head.goto(0, 0)
    head.direction = "stop"
    
    for body in bodies:
        body.goto(1000, 1000)
    
    bodies.clear()

while True:
    board.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        food.goto(x, y)

        add_body(bodies)
    move_body(bodies)

    move()

    check_collisions(bodies)
    time.sleep(0.1)