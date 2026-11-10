import turtle
from unittest.mock import patch

from movements import add_body, move, reset_game

def create_head():
        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")
        head.color("green")
        head.penup()
        head.goto(9,9)
        head.direction = "stop"
        return head


def test_reset_game__head_resets_to_origin():
    turtle.getscreen().getcanvas().master.withdraw() 
    turtle.tracer(0, 0)

    with patch('turtle.mainloop'), patch('turtle.done'):
        head = create_head()

        bodies = [turtle.Turtle(), turtle.Turtle()]
        reset_game(head, bodies)

        assert head.pos() == (0.00, 0.00)

def test_reset_game__head_stops():
    turtle.getscreen().getcanvas().master.withdraw() 
    turtle.tracer(0, 0)

    with patch('turtle.mainloop'), patch('turtle.done'):
        head = create_head()

        bodies = [turtle.Turtle(), turtle.Turtle()]
        reset_game(head, bodies)

        assert head.direction == "stop"

def test_reset_game__bodies_cleared():
    turtle.getscreen().getcanvas().master.withdraw() 
    turtle.tracer(0, 0)

    with patch('turtle.mainloop'), patch('turtle.done'):
        head = create_head()

        bodies = [create_head(), create_head()]
        reset_game(head, bodies)

        assert bodies == []


def test_move__head_up__moves_up():
     head = create_head()
     head.direction = "up"
     head.goto(0,0)

     move(head)

     assert head.pos() == (0.00, 20.00)

def test_move__head_down__moves_down():
     head = create_head()
     head.direction = "down"
     head.goto(0,0)

     move(head)

     assert head.pos() == (0.00, -20.00)

def test_move__head_left__moves_left():
     head = create_head()
     head.direction = "left"
     head.goto(0,0)

     move(head)

     assert head.pos() == (-20.00, 0.00)

def test_move__head_right__moves_right():
     head = create_head()
     head.direction = "right"
     head.goto(0,0)

     move(head)

     assert head.pos() == (20.00, 0.00)

def test_move__head_erroneous_dir__no_movement():
     head = create_head()
     head.direction = "erroneous_dir"
     head.goto(0,0)

     move(head)

     assert head.pos() == (0.00, 0.00)


def test_add_body__no_body__adds_a_body():
     bodies = []
     add_body(bodies)
     
     assert len(bodies) == 1

def test_add_body__one_body__adds_a_body():
     bodies = [create_head()]
     add_body(bodies)

     assert len(bodies) == 2


def test_move_body__():
     pass