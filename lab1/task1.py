import random
import re
from typing import Generator
import PySimpleGUI as sg


def get_rand_gen(k: float, n: int = 10 ** 6) -> Generator[bool, None, None]:
    for _ in range(n):
        yield random.uniform(0, 1) <= k


def isfloat(s):
    find = re.findall(r"\d*\.\d+", s)
    if find:
        return True
    else:
        return False


def open_window():
    layout = [[sg.Text('enter the probability of a random event:'),
               sg.Text(size=(15, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(60, 1), key='-ANS-OUTPUT-')],
              [sg.Button('Display'), sg.Button('Exit')]]
    window = sg.Window("Task1", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Display":
            if isfloat(values['-IN-']):
                ans = float(values['-IN-'])
                if 0 <= ans <= 1.0:
                    random_values = list(get_rand_gen(ans))
                    practical_probability = random_values.count(True) / len(random_values)
                    output = 'theoretical probability - {0} practical - {1}'.format(ans, practical_probability)
                else:
                    ans = 'Value not in range [0, 1]'
            else:
                ans = 'Error! Enter float value in range [0, 1]'

            window['-OUTPUT-'].update(ans)
            window['-ANS-OUTPUT-'].update(output)

    window.close()
