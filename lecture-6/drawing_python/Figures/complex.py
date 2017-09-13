import math
import logging
from drawing_python.Figures.base import Figure


class Rectangle(Figure):

    def __init__(self, height, width, **kwargs):
        super().__init__(**kwargs)
        self.height = height
        self.width = width

        if height is None or width is None:
            logging.warning('Missing data')

    def draw(self, turtle):
        half_height = self.height / 2
        half_width = self.width / 2
        x = self.center_x - half_width
        y = self.center_y + half_height

        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(270)
        for side in range(4):
            if side % 2 == 0:
                turtle.forward(self.height)
                turtle.left(90)
            else:
                turtle.forward(self.width)
                turtle.left(90)


class Pie(Figure):

    def __init__(self, radius, arg_degrees, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.arg_degrees = arg_degrees

    def draw(self, turtle):
        x = self.center_x - self.radius
        y = self.center_y

        turtle.penup()
        turtle.goto(self.center_x, self.center_y)
        turtle.pendown()
        turtle.setheading(270)
        turtle.color(self.color)
        turtle.goto(x, y)
        turtle.circle(self.radius, self.arg_degrees)
        turtle.goto(self.center_x, self.center_y)


class Polygon(Figure):

    def __init__(self, sides, radius, **kwargs):
        super().__init__(**kwargs)
        self.sides = sides
        self.radius = radius

    def draw(self, turtle):
# Зависимост между брой страни и ъгъл на правилен многоъгълник
        angle = (1 - (2 / self.sides)) * 180
        half_angle = angle / 2
# Зависимост между страна, апотема и радиус на описана окръжност
        side = 2 * self.radius * math.cos(math.pi / self.sides) * math.tan(math.pi / self.sides)

        turtle.penup()
        turtle.goto(self.center_x, self.center_y)
        turtle.left(90)
        turtle.forward(self.radius)
        turtle.left(180 - half_angle)
        turtle.pendown()
        for var in range(self.sides):
            turtle.forward(side)
            turtle.left(180 - angle)