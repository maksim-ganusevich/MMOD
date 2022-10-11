import re
from typing import Generator

import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import my_random
from distribution_checkers import checkUniform


def get_rand_values(n: int = 10 ** 6) -> Generator[bool, None, None]:
    r = my_random.XorShift128Plus()
    for _ in range(n):
        yield r.next_double()


def isfloat(s):
    find = re.findall(r"\d*\.\d+", s)
    if find:
        return True
    else:
        return False


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def open_window():
    layout = [[sg.Text('enter borders of uniform distribution:')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(70, 2), key='-OUTPUT-')],
              [sg.Button('Display'), sg.Button('Exit')]]
    window = sg.Window("Task1", layout, modal=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Display":
            borders = values['-IN-'].split(',')
            checker = [isfloat(s) for s in borders]
            output = ''
            if checker.count(False) == 0 and len(checker) == 2:
                borders = [float(p) for p in borders]
                a, b = borders[0], borders[1]
                if a < b:
                    probabilities = list(get_rand_values(10 ** 6))
                    dots = [a + p * (b - a) for p in probabilities]
                    dots.sort()
                    checkUniform(dots)
                else:
                    output = 'Error! the right border is larger than the left'
            else:
                output = 'Error! Enter two float values separated by commas'
        window['-OUTPUT-'].update(output)
    window.close()
