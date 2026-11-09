import random
import time
import turtle
from intitialize_components import initialize_components
from movements import add_body, check_collisions, move_body, reset_game


bodies = []
board, head, food = initialize_components()

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


while True:
    board.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game(head, bodies)

    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        food.goto(x, y)

        add_body(bodies)
    move_body(bodies, head)

    move()

    check_collisions(bodies, head)
    time.sleep(0.1)