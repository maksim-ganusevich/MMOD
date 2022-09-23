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
    layout = [[sg.Text('Enter probabilities separated by commas'),
               sg.Text(size=(40, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(60, 2), key='-ANS-OUTPUT-')],
              [sg.Button('Display'), sg.Button('Exit')]]
    window = sg.Window("Task2", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Display":
            probabilities = values['-IN-'].split(',')
            checker = [isfloat(s) for s in probabilities]
            generators = []
            ans = None
            output = ''

            if checker.count(False) == 0:
                probabilities = [float(p) for p in probabilities]
                for probability in probabilities:
                    if 0 <= probability <= 1.0:
                        generators.append(get_rand_gen(probability))
                    else:
                        ans = 'someone probability not in range [0, 1]'

                if ans is None:
                    events = []
                    # for _ in range(10 ** 6):
                    # events.append([next(i) for i in generators])
                    for g in generators:
                        events.append(sum(list(g))/10**6)
                    output = 'theoretical probability - {0} \npractical - {1}'.format(probabilities, events)
            else:
                ans = 'Error! Enter float value in range [0, 1] separated by commas'

            window['-OUTPUT-'].update(ans)
            window['-ANS-OUTPUT-'].update(output)

    window.close()
