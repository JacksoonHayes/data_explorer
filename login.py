"""
Module for the GUI and initializing the windows
"""
import PySimpleGUI as sg


sg.theme('DarkBlue4')

# Define the window's contents
layout = [
    [sg.Text("Login"), sg.Text(size=(15,1))],
    [sg.Text("Username:"), sg.Input(key='-USERNAME-')],
    [sg.Text("Password:"),sg.Input(key='-PASSWORD-', password_char='*')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Submit'), sg.Button('Quit')]
]

window = sg.Window('Login', layout, size=(400, 300))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-USERNAME-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()