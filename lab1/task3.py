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
    layout = [[sg.Text('Enter 2 probabilities separated by commas'),
               sg.Text(size=(40, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(70, 2), key='-ANS-OUTPUT-')],
              [sg.Button('Display'), sg.Button('Exit')]]
    window = sg.Window("Task3", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Display":
            probabilities = values['-IN-'].split(',')
            checker = [isfloat(s) for s in probabilities]
            ans = None
            output = ''

            if checker.count(False) == 0 and len(checker) == 2:
                probabilities = [float(p) for p in probabilities]
                for probability in probabilities:
                    if 0 <= probability <= 1.0:
                        pass
                    else:
                        ans = 'someone probability not in range [0, 1]'

                if ans is None:
                    p_A, p_B_at_A = probabilities[0], probabilities[1]
                    p_A_B = p_A * p_B_at_A
                    p_n_A, p_B_at_n_A = 1 - p_A, 1 - p_B_at_A
                    p_n_A_B = p_n_A * p_B_at_n_A
                    p_B = p_A_B + p_n_A_B
                    gen_A, gen_B = get_rand_gen(p_A), get_rand_gen(p_B)
                    events = {0: 0, 1: 0, 2: 0, 3: 0}
                    for _ in range(10 ** 6):
                        check_A, check_B = next(gen_A), next(gen_B)
                        if check_A and check_B:
                            events[0] += 1
                        elif check_A and not check_B:
                            events[1] += 1
                        elif not check_A and check_B:
                            events[2] += 1
                        elif not check_A and not check_B:
                            events[3] += 1
                    frequency = [0] * 4
                    for key, val in events.items():
                        frequency[key] = round(val / 10 ** 6, 6)
                    output = 'theoretical probability - P(AB) = {0} P(AB¯) = {1} P(A¯B) = {2} P(A¯B¯) = {3}' \
                             '\npractical - P(AB) = {4} P(AB¯) = {5} P(A¯B) = {6} P(A¯B¯) = {7}'. \
                        format(round(p_A * p_B, 6), round(p_A * (1 - p_B), 6), round((1 - p_A) * p_B, 6),
                               round((1 - p_A) * (1 - p_B), 6), frequency[0], frequency[1], frequency[2], frequency[3])

            else:
                ans = 'Error! Enter float value in range [0, 1] separated by commas'

            window['-OUTPUT-'].update(ans)
            window['-ANS-OUTPUT-'].update(output)

    window.close()
