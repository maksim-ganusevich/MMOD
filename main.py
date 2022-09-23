import PySimpleGUI as sg
from lab1 import task1, task2, task3, task4, unreal_tournament


sg.theme('BluePurple')

layout = [[sg.Text('Select a task:'),
           sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Button('Task1'), sg.Button('Task2'), sg.Button('Task3'),
           sg.Button('Task4'), sg.Button('Task5'), sg.Button('Exit')]]

window = sg.Window('Lab1', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event in (None, 'Exit'):
        break

    if event == 'Task1':
        task1.open_window()

    if event == 'Task2':
        task2.open_window()

    if event == 'Task3':
        task3.open_window()

    if event == 'Task4':
        task4.open_window()

    if event == 'Task5':
        unreal_tournament.open_window()

window.close()
