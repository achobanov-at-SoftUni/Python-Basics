import turtle

side = 40
fill = 1

for i in range(1, 65):
    if i % 8 == 1 and i != 1:
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side * 8)
        turtle.left(180)
        fill += 1

    if fill % 2 == 0:
        turtle.begin_fill()
    turtle.forward(side)

    for y in range(4):
        turtle.left(90)
        turtle.forward(side)
    turtle.end_fill()
    fill += 1

turtle.exitonclick()
