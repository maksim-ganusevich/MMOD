import random
import re
from typing import Generator
import PySimpleGUI as sg


def get_rand_gen(probability_list: list) -> Generator[list, None, None]:
    sum_list = [0.0]
    for p in range(len(probability_list)):
        sum_list.append(sum_list[-1] + probability_list[p])
    for _ in range(10 ** 6):
        event = random.uniform(0, 1)
        for p in range(len(sum_list)):
            if event <= sum_list[p]:
                ans = [False] * len(sum_list)
                ans[p] = True
                yield ans[1:]
                break


def isfloat(s):
    find = re.findall(r"\d*\.\d+", s)
    if find:
        return True
    else:
        return False


def open_window():
    layout = [[sg.Text('Enter probabilities separated by commas:'),
               sg.Text(size=(40, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(70, 2), key='-ANS-OUTPUT-')],
              [sg.Button('Display'), sg.Button('Exit')]]
    window = sg.Window("Task4", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Display":
            probabilities = values['-IN-'].split(',')
            checker = [isfloat(s) for s in probabilities]
            ans = None
            output = ''

            if checker.count(False) == 0:
                probabilities = [float(p) for p in probabilities]
                if abs(sum(probabilities) - 1) < 0.0000001:
                    for probability in probabilities:
                        if 0 <= probability <= 1.0:
                            pass
                        else:
                            ans = 'someone probability not in range [0, 1]'

                    if ans is None:

                        events = [0] * len(probabilities)
                        gen = get_rand_gen(probabilities)
                        for event in gen:
                            ind = event.index(True)
                            events[ind] += 1
                        events = [i / 10 ** 6 for i in events]
                        output = 'theoretical probabilities - {} ' \
                                 '\npractical - {}'.format(probabilities, events)
                else:
                    ans = 'sum of probabilities is not 1'

            else:
                ans = 'Error! Enter float value in range [0, 1] separated by commas'

            window['-OUTPUT-'].update(ans)
            window['-ANS-OUTPUT-'].update(output)

    window.close()
