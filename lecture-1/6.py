import turtle
i = 10
a = 0
while True:
    while i in range(197, 218):
        if a % 5 == 0:
            turtle.left(45)
            turtle.forward(100)
        else:
            turtle.right(90)
            turtle.forward(50)
        a += 1
        i += 1
        if i == 218:
            i = 0
            a = 0
    turtle.left(i % 48)
    turtle.forward(10)
    i+=1