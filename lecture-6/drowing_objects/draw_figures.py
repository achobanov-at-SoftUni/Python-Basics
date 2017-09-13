import json
import sys
import turtle

from drowing_objects.Figures.simple import Circle, Square


def main():
    if len(sys.argv) < 2:
        print("Usage: {} input-file.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        draw_figures(input_data)
    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2


def load_input_data(input_filename):
    with open(input_filename) as f:
        input_data = json.load(f)
        return input_data


def draw_figures(figures_info):
    t = turtle.Turtle()
    t.speed('slow')
    for f_info in figures_info:
        figure_type = f_info['type']
        if figure_type == 'square':
            s = Square(
                center_x = f_info['center_x'],
                center_y = f_info['center_y'],
                side = f_info['side'],
                color = f_info['color']
            )
            s.draw(t)
        elif figure_type == 'circle':
            c = Circle(
                center_x=f_info['center_x'],
                center_y=f_info['center_y'],
                radius=f_info['radius'],
                color=f_info['color']
            )
            c.draw(t)
        else:
            print('Not supported figure: {}'.format(f_info['type']))

    turtle.exitonclick()

if __name__ == "__main__":
    sys.exit(main())