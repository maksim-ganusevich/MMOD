import math
import re
from typing import Generator

import PySimpleGUI as sg

import my_random
from distribution_checkers import checkGeom


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


def open_window():
    layout = [[sg.Text('Enter the probability of success:')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(70, 2), key='-OUTPUT-')],
              [sg.Button('Display'), sg.Button('Exit')]]
    window = sg.Window("Task2", layout, modal=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Display":
            p = values['-IN-'].split(',')
            checker = [isfloat(s) for s in p]
            output = ''
            if checker[0] and len(checker) == 1:
                p = float(p[0])
                probabilities = list(get_rand_values(10 ** 6))
                dots = [math.ceil(math.log(prob)/math.log(1-p)) for prob in probabilities]
                dots.sort()
                checkGeom(dots, p)
            else:
                output = 'Error! Enter one float value'
        window['-OUTPUT-'].update(output)
    window.close()
