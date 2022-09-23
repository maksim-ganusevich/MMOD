import random
import PySimpleGUI as sg
from lab1.task1 import get_rand_gen


class Match:
    def __init__(self):
        team1 = ()
        team2 = ()
        win = ()

    def get_match(self):
        return '{}: r = {}, {}: r = {}'.format(self.team1[0], self.team1[1], self.team2[0], self.team2[1])

    def get_result(self):
        return 'Team1: {}, rating: {}, Team2: {}, rating: {}\n win: {}\n'.format(
            self.team1[0], self.team1[1], self.team2[0], self.team2[1], self.win[0])


def get_teams(n: int):
    teams = [
        'Northwich',
        'Blackpool',
        'Bournemouth',
        'Liverpool',
        'Stoneham',
        'Sudbury',
        'Wimbledon',
        'Arsenal',
        'Aston Villa',
        'Barnsley',
        'Birmingham City',
        'Blackburn Rovers',
        'Blackpool',
        'Bolton Wanderers',
        'Brentford',
        'Brighton',
        'Bristol City',
        'Bristol Rovers',
        'Burnley',
        'Burton Albion',
        'Cambridge United',
        'Cardiff City',
        'Charlton Athletic',
        'Chelsea',
        'Cheltenham Town',
        'Coventry City',
        'Crystal Palace',
        'Everton',
        'Fulham',
        'Huddersfield Town',
        'Hull City',
        'Leeds United',
        'Leicester City',
        'Luton Town',
        'Manchester City',
        'Manchester United',
        'Middlesbrough',
        'Millwall',
        'Newcastle United',
        'Norwich City',
        'Nottingham Forest',
        'Preston North End',
        'Queens Park Rangers',
        'Reading',
        'Rotherham United',
        'Sheffield United',
        'Southampton',
        'Stoke City',
        'Sunderland',
        'Swansea City',
        'Tottenham Hotspur',
        'Watford',
        'West Bromwich Albion',
        'West Ham United',
        'Wigan Athletic',
        'Wolverhampton',
        'Shrewsbury Town',
        'Plymouth Argyle',
        'Peterborough United',
        'Oxford United',
    ]
    ret = []
    for t in teams:
        ret.append((t, random.randint(0, 100)))
    random.shuffle(ret)
    return ret[:n]


def open_window():
    layout = [[sg.Text('enter count of tours (less then 7):'),
               sg.Text(size=(15, 1), key='-OUTPUT-')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(60, 50), key='-ANS-OUTPUT-')],
              [sg.Button('Generate teams'), sg.Button('Simulate matches'), sg.Button('Get tour'), sg.Button('Exit')]]

    window = sg.Window("Tournament", layout, modal=True)

    k = None
    ans = ''
    output = ''
    tours = []
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Generate teams":
            if values['-IN-'].isdigit():
                k = int(values['-IN-'])
                if 0 < k < 7:
                    teams = get_teams(2 ** k)
                    output = ''
                    for team in teams:
                        output += "{}, rating: {}\n".format(team[0], team[1])

        if event == "Simulate matches":
            if k is None:
                continue

            for i in range(k):
                l = len(teams)
                matches = []
                for j in range(0, l, 2):
                    m = Match()
                    team1, team2 = teams[j], teams[j + 1]
                    p1 = team1[1] / (team1[1] + team2[1])
                    gen = get_rand_gen(p1, 1)
                    p = next(gen)
                    m.team1 = team1
                    m.team2 = team2

                    if p:
                        teams.append(team1)
                        m.win = team1
                    else:
                        teams.append(team2)
                        m.win = team2
                    matches.append(m)
                teams = teams[l:]
                tours.append(matches)

        if event == "Get tour":
            if values['-IN-'].isdigit():
                tour = int(values['-IN-'])
                if k is not None and 0 < tour <= k:
                    output = ''
                    for match in tours[tour-1]:
                        output += match.get_result()

        window['-OUTPUT-'].update(ans)
        window['-ANS-OUTPUT-'].update(output)
