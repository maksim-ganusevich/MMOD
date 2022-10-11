import PySimpleGUI as sg
from lab2 import task1


sg.theme('BluePurple')

layout = [[sg.Text('Select a task:'),
           sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Button('Task1'), sg.Button('Task2'), sg.Button('Exit')]]

window = sg.Window('Lab1', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event in (None, 'Exit'):
        break

    if event == 'Task1':
        task1.open_window()

window.close()
