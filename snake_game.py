import random
import time
from intitialize_components import initialize_components
from movements import add_body, check_collisions, move, move_body, reset_game


bodies = []
board, head, food = initialize_components()

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

    move(head)

    check_collisions(bodies, head)
    time.sleep(0.1)