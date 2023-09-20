"""
Module for the DES 1 GUI
"""

import PySimpleGUI as sg
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(5, 3.9))

# Placeholder data for the initial graph
x = [0, 2, 4, 6, 8, 10]
y = [0, 2, 4, 6, 8, 10]
ax.plot(x, y)
ax.set_title('Placeholder Graph')

# Column layout for the GUI

col1 = [
    [sg.Button('Chart Settings', size=(10, 1), button_color=('white', 'navy'), key='Chart Settings'),
    sg.Button('Set data', size=(15, 1), button_color=('white', 'navy'), key='Set data'), 
    sg.Button('Input', size=(15, 1), button_color=('white', 'navy'), key='Input')],
    
    [sg.Canvas(key='-CANVAS-')],
    
    [sg.Button('<', size=(10, 1), key='Pan Left'),
    sg.Button('➖', size=(10, 1), key='Zoom Out'),
    sg.Button('➕', size=(10, 1), key='Zoom In'),
    sg.Button('>', size=(10, 1), key='Pan Right')]
]

col2 = [
    [sg.Text('Summary', justification='center')],
    [sg.Multiline(key='-SUMMARY-', size=(30, 8))],
    [sg.Text('Chat', justification='center')],
    [sg.Multiline(key='-CHAT-', size=(30, 12))],
    [sg.Button('Send')]  
]

# Create a PySimpleGUI window layout with two columns
layout = [
    [sg.Button('Home', size=(15, 1), button_color=('white', 'navy'), key='Home'),],
    [sg.Column(col1, element_justification='c'), sg.Column(col2, element_justification='c')]
]

# Create the PySimpleGUI window
window = sg.Window('Data Explorer', layout, finalize=True, background_color='grey')

# Embed the Matplotlib plot into the PySimpleGUI window
canvas_elem = window['-CANVAS-']
canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

while True:
    event, values = window.read(timeout=100)  # Add a timeout value

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    # Add event handlers for buttons or menu items as needed
    if event == 'Zoom In':
        ax.set_xlim(0, 10)  # Modify the limits accordingly
        ax.set_ylim(0, 10)
        canvas.draw()

    if event == 'Zoom Out':
        ax.set_xlim(-5, 15)  # Modify the limits accordingly
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
