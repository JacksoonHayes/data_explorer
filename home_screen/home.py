"""
Module for the Home Screen GUI
"""
import PySimpleGUI as sg
import subprocess

sg.theme('LightBrown12')

title = ("Century Gothic", 18)
sg.set_options(font=('Century Gothic', 10))

header = [
    [sg.Push(), sg.T("Home Screen", font=title, pad=((100, 0), (10, 0))),
    sg.Push(), sg.Button('Logout', key='-LOGOUT-', size=(12, 1), pad=(0, (10, 0)), button_color=('white', '#4DA30F'))]
]

col1 = [
    [sg.Image(r'./images/forest.png', size=(200, 200), pad=(0, (0, 15)), background_color='#363636')],
    [sg.Button('View Screen 1', size=(21, 1), key='Screen 1', pad=(0, (0, 10)), button_color=('white', '#636363'))]
]

col2 = [
    [sg.Image(r'./images/forest.png', size=(200, 200), pad=(0, (0, 15)), background_color='#363636')],
    [sg.Button('View Screen 2', size=(21, 1), key='Screen 2', pad=(0, (0, 10)), button_color=('white', '#636363'))]
]

col3 = [
    [sg.Image(r'./images/forest.png', size=(200, 200), pad=(0, (0, 15)), background_color='#363636')],
    [sg.Button('View Screen 3', size=(21, 1), key='Screen 3', pad=(0, (0, 10)), button_color=('white', '#636363'))]
]

layout = [
    [header],
    [sg.HSeparator(pad=(70, (20, 40)))],
    [sg.Column(col1, element_justification='c', background_color='#363636'), 
    sg.Column(col2, element_justification='c', pad=(20, 0), background_color='#363636'), 
    sg.Column(col3, element_justification='c', background_color='#363636')]
    
]

window = sg.Window('Home Screen', layout, size=(700, 450), element_justification='c')

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == '-LOGOUT-':
        window.close()
        # Run the login screen GUI
        subprocess.Popen(['python', 'app.py'])
        break
    
    
window.close()