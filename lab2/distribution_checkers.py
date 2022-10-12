import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def M(s):
    ans = float(0)
    for i in s:
        ans += i
    return ans / len(s)


def D(s):
    ans = float(0)
    for i in s:
        ans += i ** 2
    ans /= len(s)
    return (ans - M(s) ** 2) * len(s) / (len(s) - 1)


def ToPpobArr(s):
    tempArr, i, j = [], 0, 0
    while i < 25:
        temp = 0
        while j < len(s) and s[j] < s[0] + (s[-1] - s[0]) / 25 * (i + 1):
            temp += 1
            j += 1
        tempArr.append(temp / len(s))
        i += 1
    return tempArr


def uniformF(x, a, b):
    if x < a:
        return float(0)
    elif x < b:
        return (x - a) / (b - a)
    else:
        return float(1)


def Kolmog(lamb):
    with open("Kolmogorov.txt", 'r') as file:
        kol = {}
        for line in file:
            line = line.strip().split()
            kol[float(line[0])] = float(line[1])
        for key in kol.keys():
            if key >= lamb:
                return kol[key]
        return 0.0


def Trust(p):
    with open("Trust.txt", 'r') as f4:
        kol = {}
        for line in f4:
            line = line.strip().split()
            kol[float(line[0])] = float(line[1])
        for key in kol.keys():
            if key >= p:
                return kol[key]
        return 0.0


def checkUniform(s):
    a, b = M(s) - ((3 * D(s)) ** 0.5), M(s) + ((3 * D(s)) ** 0.5)
    probArr = ToPpobArr(s)
    value1, value2, maxDeviat, i = s[0], s[0] + (s[-1] - s[0]) / 25, 0, 0
    while i < 25:
        maxDeviat = max(maxDeviat, abs(probArr[i] - (uniformF(value2, a, b) - uniformF(value1, a, b))))
        value1 += (s[-1] - s[0]) / 25
        value2 += (s[-1] - s[0]) / 25
        i += 1
    ans = "Лямбда для равномерного распределения - {}\nВероятность равномерного распределения - {}".format(
        maxDeviat * (len(s) ** 0.5), Kolmog(maxDeviat * (len(s) ** 0.5)), "\n")
    check_window(s, ans)


def ToOneStepArr(s):
    tempArr, i, j = [], 0, 0
    while i < s[-1] - s[0] + 1:
        temp = 0
        while j < len(s) and s[j] < s[0] + (i + 1):
            temp += 1
            j += 1
        tempArr.append(temp / len(s))
        i += 1
    return tempArr


def checkGeom(s, P):
    probArr = ToOneStepArr(s)
    value1, value2, maxDeviat, i = s[0] - 1, s[0], 0, 0
    while i < s[-1] - s[0] + 1:
        maxDeviat = max(maxDeviat, abs(probArr[i] - (geomF(value2, P) - geomF(value1, P))))
        value1 += 1
        value2 += 1
        i += 1
    ans = "Лямбда для равномерного распределения - {}\nВероятность равномерного распределения - {}".format(
        maxDeviat * (len(s) ** 0.5), Kolmog(maxDeviat * (len(s) ** 0.5)), "\n")
    check_window(s, ans)


def geomF(x, P):
    return 1 - (1 - P) ** x


def check_window(s, ans):
    plt.title('Plot Title')
    plt.hist(s, bins=s[-1]-s[0]+1)
    plt.ylabel('Probability')
    plt.xlabel('Data')
    fig = plt.gcf()
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    layout = [[sg.Text('Uniform test', font='Any 18')],
              [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')],
              [sg.Text(size=(70, 2), key='-OUTPUT-')],
              [sg.Button('Exit')]]
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI',
                       layout, force_toplevel=True, finalize=True)
    draw_figure(window['-CANVAS-'].TKCanvas, fig)
    window['-OUTPUT-'].update(ans)
    plt.show()
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            window.close()
            break


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
