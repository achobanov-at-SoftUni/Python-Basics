import turtle
side = 40
turtle.forward(side)
fill = 1
newline = 1
for i in range(1, 64 * 4 + 1):
    if newline % 8 == 0:
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side * 8)
        turtle.left(90)
        fill += 1
    if i % 5 == 0:
        turtle.forward(side)
        newline += 1
    else:
        #if fill % 2 == 0:
        #    turtle.begin_fill()
        turtle.left(90)
        turtle.forward(side)
        turtle.end_fill()
        #fill += 1





