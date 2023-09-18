"""
Module for the GUI and initializing the windows
"""
import PySimpleGUI as sg


sg.theme('DarkBlue4')

# Define the window's contents
layout = [
    [sg.T("Login", font="any 16")],
    [sg.HSeparator(pad=(70, 20))],
    [sg.Text("Username:"), sg.Input(key='-USERNAME-', size=(18,1))],
    [sg.Text("Password:"),sg.Input(key='-PASSWORD-', password_char='•', size=(18,1))],
    [sg.Text(size=(40,1), key='-OUTPUT-', pad=(0, 30), justification='c')],
    [sg.Button('Submit',), sg.Button('Quit')]
]

window = sg.Window('Login screen', layout, size=(400, 300), element_justification='c', margins=(0, 20))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-USERNAME-'] + ", Login successful!")

# Finish up by removing from the screen
window.close()