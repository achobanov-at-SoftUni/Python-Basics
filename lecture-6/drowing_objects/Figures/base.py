class Figure:

    def __init__(self, center_x, center_y, color='black'):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def __str__(self):
        return 'Figure center: {}:{}, color: {}'.format(
            self.center_x,
            self.center_y,
            self.color
        )

    def draw(self, turtle):
        pass
