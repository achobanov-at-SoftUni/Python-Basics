import logging
from drawing_python.Figures.base import Figure


class Circle(Figure):

    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

        if radius is None:
            logging.warning('Missing data')

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x - self.radius, self.center_y)  # Locating a starting point for circle
        turtle.pendown()
        turtle.setheading(270)
        turtle.color(self.color)
        turtle.circle(self.radius)


class Square(Figure):

    def __init__(self, side, **kwargs):
        super().__init__(**kwargs)
        self.side = side

        if side is None:
            logging.warning('Missing data')

    def draw(self, turtle):
        half_side = self.side / 2
        left = self.center_x - half_side
        top = self.center_y + half_side

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        # turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)