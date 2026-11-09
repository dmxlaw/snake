import random
import turtle


def initialize_components():
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

    return (board, head, food)