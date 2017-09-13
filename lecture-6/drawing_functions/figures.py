def draw_circle(turtle_instance, center_x, center_y, radius, color):
    turtle_instance.penup()
    turtle_instance.goto(center_x - radius, center_y)  # From docs: The center is radius units left of the turtle;
    turtle_instance.pendown()
    turtle_instance.color(color)
    turtle_instance.circle(radius)


def draw_square(turtle_instance, center_x, center_y, side, color):
    half_side = side / 2
    left = center_x - half_side
    top = center_y + half_side

    turtle_instance.penup()
    turtle_instance.goto(left, top)
    turtle_instance.pendown()
    turtle_instance.color(color)
    turtle_instance.forward(1)
    turtle_instance.setheading(270)  # point the turtle down
    for _ in range(4):
        turtle_instance.forward(side)
        turtle_instance.left(90)
