""" Попытка в <150 строчек решить КМЗИ """
import PySimpleGUI as sg
from base import get_input, change_text, count_frequency, format_text_string

# pylint: disable=invalid-name
layout = [
    [
        sg.Text('Input:'),
        sg.InputText(),
        sg.FileBrowse(),
        sg.Button('Load')
    ],
    [
        sg.Text('From:'),
        sg.InputText(),
        sg.Text('To:'),
        sg.InputText(),
        sg.Button('Cancel'),
        sg.Button('Change')
    ],
    [
        sg.Text(size=(64, 20), key='-OUTPUT-'),
        sg.Text(size=(10, 10)), sg.Text(size=(64, 20), key='-FREQUENCY-')
    ],
]

changes = []
window = sg.Window('Cracking the code', layout)

while True:
    event, values = window.read()
    if event == 'Load':
        filepath = 'result.txt' if values[0] == '' else values[0]
        text = get_input(filepath)
        str_text = ''

        window['-OUTPUT-'].update(format_text_string(text))
        frequency_stat = count_frequency(text)
        window['-FREQUENCY-'].update(frequency_stat)
    elif event == 'Change':
        if len(values[1].split()) != len(values[2].split()):
            raise Exception('Different amount of elements')

        substitute = {}
        for s, d in zip(values[1].split(), values[2].split()):
            substitute.update({s: d + ' '})

        changes.append(substitute)
        text = change_text(text, substitute)

        window['-OUTPUT-'].update(format_text_string(text))

    elif event == 'Cancel':
        if len(changes) == 0:
            continue
        substitute = {changes[-1][i]: i for i in changes[-1]}
        text = change_text(text, substitute)
        del changes[-1]

        window['-OUTPUT-'].update(format_text_string(text))

    if event in (None, 'Exit'):
        break

window.close()
