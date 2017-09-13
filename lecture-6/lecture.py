# Objects, class, method


class Figure:
    def __init__(self, center, color):
        self.center = center
        self.color = color

    def print(self):
        print('Figure center {} and color {}'.format(self.center, self.color))


class Circle(Figure):
    def __init__(self, center, color, radius):
        super().__init__(center, color)
        self.radius = radius

    def print(self, indent = 4):
        print('{}Figure center {} and color {}, radius {}'.format(
            ' ' * indent,
            self.center,
            self.color,
            self.radius
        ))


a = Circle((10, 15), 'red', 15)
a.print()
