"""
Module for the DES 1 GUI
"""

import PySimpleGUI as sg
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


fig, ax = plt.subplots()

# Placeholder data for the graph
x = [0, 2, 4, 6, 8, 10]
y = [0, 2, 4, 6, 8, 10]
ax.plot(x, y)
ax.set_title('Placeholder Graph')

sg.theme('DarkGrey5')

sg.set_options(font=('Century Gothic', 10))

navbar = [
    [sg.Button('Home', size=(15, 1), key='Home', button_color=('white', '#4DA30F')),
    sg.Push(background_color='#6E6E6E'),
    sg.Button('Screen 2', size=(15, 1), key='Screen 2', button_color=('white', '#4DA30F')),
    sg.Button('Screen 3', size=(15, 1), key='Screen 3', button_color=('white', '#4DA30F'))]
]

col1 = [
    [sg.Button('Chart Settings', size=(14, 1), key='Chart Settings'),
    sg.Push(),
    sg.Button('Set Data', size=(15, 1), key='Set Data'), 
    sg.Button('Upload Data', size=(15, 1), key='Upload Data')],
    
    [sg.Canvas(size=(600, 500), key='-CANVAS-')],
    
    [sg.Button('<', size=(10, 1), key='Pan Left'),
    sg.Push(),
    sg.Button('➖', size=(10, 1), key='Zoom Out'),
    sg.Button('➕', size=(10, 1), key='Zoom In'),
    sg.Push(),
    sg.Button('>', size=(10, 1), key='Pan Right')]
]

col2 = [
    [sg.Text('Summary', justification='center')],
    [sg.Multiline(key='-SUMMARY-', size=(32, 11), background_color='#C2C2C2', no_scrollbar=True, pad=(0, (6, 6)), write_only=True, disabled=True)],
    [sg.Text('Chat', justification='center')],
    [sg.Multiline(key='-CHAT-', size=(30, 16), background_color='#C2C2C2', write_only=True, disabled=True)],
    [sg.Input(size = (25, 1), background_color='#C2C2C2'), sg.Button('Send')]
]

layout = [
    [navbar], [sg.Column(col1, element_justification='c'), sg.Column(col2, element_justification='c')]
]

window = sg.Window('Data Explorer', layout, finalize=True, background_color='#6E6E6E')

canvas_elem = window['-CANVAS-']
canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
canvas.get_tk_widget().pack(side='top', fill='both', expand=1)


while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Zoom In':
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        canvas.draw()

    if event == 'Zoom Out':
        ax.set_xlim(-5, 15)
        ax.set_ylim(-5, 15)
        canvas.draw()

    if event == 'Pan Left':
        current_xlim = ax.get_xlim()
        ax.set_xlim(current_xlim[0] - 1, current_xlim[1] - 1)
        canvas.draw()

    if event == 'Pan Right':
        current_xlim = ax.get_xlim()
        ax.set_xlim(current_xlim[0] + 1, current_xlim[1] + 1)
        canvas.draw()

window.close()
