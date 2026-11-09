import turtle

def reset_game(head, bodies):
    head.goto(0, 0)
    head.direction = "stop"
    
    for body in bodies:
        body.goto(1000, 1000)
    
    bodies.clear()

def add_body(bodies):
    new_body = turtle.Turtle()
    new_body.speed(0)
    new_body.shape("square")
    new_body.color("lightgreen")
    new_body.penup()
    bodies.append(new_body)

def move_body(bodies, head):
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

def check_collisions(bodies, head):
    for body in bodies:
        if body.distance(head) < 20:
            reset_game(head, bodies)