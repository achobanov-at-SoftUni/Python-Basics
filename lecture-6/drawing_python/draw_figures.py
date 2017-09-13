import os
import sys
import turtle

from drawing_python.input import JSONLoader, YAMLLoader
from drawing_python.Figures.simple import Circle, Square
from drawing_python.Figures.complex import Rectangle, Pie, Polygon

FIGURE_TYPES = {
    'circle': Circle,
    'square': Square,
    'rectangle': Rectangle,
    'pie': Pie,
    'polygon': Polygon
}
SUPPORTED_FILETYPES = {
    '.json': JSONLoader,
    '.yaml': YAMLLoader
}


def main():
    if len(sys.argv) < 2:
        print("Usage: {} input-file.json".format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        figures = create_figures(input_data)
        draw_figures(figures)
    except Exception as e:
        print("Invalid input file provided! Error: " + str(e))
        return 2


def load_input_data(input_filename):
    _, extension = os.path.splitext(input_filename)
    if extension in SUPPORTED_FILETYPES:
        file_type = SUPPORTED_FILETYPES[extension](input_filename)
        input_data = file_type.load()

    return input_data


def create_figures(input_data: dict):
    result =[]
    for f_info in input_data:
        figure_type = f_info['type']
        if figure_type in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[figure_type]
            result.append(figure_class(**f_info))
        else:
            print('Not supported figure: {}'.format(f_info['type']))

    return result


def draw_figures(figures):
    t = turtle.Turtle()
    t.speed('fast')
    for f in figures:
        f.draw(t)
    turtle.exitonclick()

if __name__ == "__main__":
    sys.exit(main())


##################################################################################################################
# Version 3
##################################################################################################################

# import json
# import sys
# import turtle
#
# from drawing_python.Figures.simple import Circle, Square
#
#
# def main():
#     if len(sys.argv) < 2:
#         print("Usage: {} input-file.json".format(sys.argv[0]))
#         return 1
#
#     try:
#         input_data = load_input_data(sys.argv[1])
#         figures = create_figures(input_data)
#         draw_figures(figures)
#     except Exception as e:
#         print("Invalid input file provided! Error: " + str(e))
#         return 2
#
#
# def load_input_data(input_filename):
#     with open(input_filename) as f:
#         input_data = json.load(f)
#         return input_data
#
#
# def create_figures(input_data: dict):
#     result =[]
#     for f_info in input_data:
#         figure_type = f_info['type']
#         if figure_type == 'square':
#             c = Square(**f_info)
#             result.append(c)
#         elif figure_type == 'circle':
#             c = Circle(**f_info)
#             result.append(c)
#         else:
#             print('Not supported figure: {}'.format(f_info['type']))
#
#     return result
#
#
# def draw_figures(figures):
#     t = turtle.Turtle()
#     t.speed('fast')
#     for f in figures:
#         f.draw(t)
#     turtle.exitonclick()
#
# if __name__ == "__main__":
#     sys.exit(main())


##################################################################################################################
# Version 2 ( Version 1 in drawing_objects )
##################################################################################################################

# import json
# import sys
# import turtle
#
# from drawing_python.Figures.simple import Circle, Square
#
#
# def main():
#     if len(sys.argv) < 2:
#         print("Usage: {} input-file.json".format(sys.argv[0]))
#         return 1
#
#     try:
#         input_data = load_input_data(sys.argv[1])
#         figures = create_figures(input_data)
#         draw_figures(figures)
#     except Exception as e:
#         print("Invalid input file provided! Error: " + str(e))
#         return 2
#
#
# def load_input_data(input_filename):
#     with open(input_filename) as f:
#         input_data = json.load(f)
#         return input_data
#
#
# def create_figures(input_data: dict):
#     result =[]
#     for f_info in input_data:
#         figure_type = f_info['type']
#         if figure_type == 'square':
#             c = Square(
#                 center_x = f_info['center_x'],
#                 center_y = f_info['center_y'],
#                 side = f_info['side'],
#                 color = f_info['color']
#             )
#             result.append(c)
#         elif figure_type == 'circle':
#             c = Circle(
#                 center_x = f_info['center_x'],
#                 center_y = f_info['center_y'],
#                 radius = f_info['radius'],
#                 color = f_info['color']
#             )
#             result.append(c)
#         else:
#             print('Not supported figure: {}'.format(f_info['type']))
#
#     return result
#
#
# def draw_figures(figures):
#     t = turtle.Turtle()
#     t.speed('fast')
#     for f in figures:
#         f.draw(t)
#     turtle.exitonclick()
#
# if __name__ == "__main__":
#     sys.exit(main())
