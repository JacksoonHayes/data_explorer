"""
Module for the Login Screen GUI
"""

import PySimpleGUI as sg
import subprocess

sg.theme('DarkGrey5')

title = ("Century Gothic", 18)
sg.set_options(font=('Century Gothic', 10))

# Hardcoded login credentials (username: password)
credentials = {
    'user1': 'password123',
    'user2': 'password123',
    'user3': 'password123'
}

layout = [
    [sg.T("Login", font=title)],
    [sg.HSeparator(pad=(70, (10, 40)))],
    [sg.Text("Username:"), sg.Input(key='-USERNAME-', size=(18,1))],
    [sg.Text("Password:"), sg.Input(key='-PASSWORD-', password_char='•', size=(18,1))],
    [sg.Text(size=(40,1), key='-OUTPUT-', pad=(0, 30), justification='c')],
    [sg.Button('Submit', key='-LOGIN-'), sg.Button('Quit')]
]

window = sg.Window('Login screen', layout, size=(400, 300), element_justification='c', margins=(0, 20))
logged_in = False

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == '-LOGIN-':
        username = values['-USERNAME-']
        password = values['-PASSWORD-']
        # Check if the entered credentials are in the dictionary
        if username in credentials and credentials[username] == password:
            logged_in = True
            # Run the home screen GUI
            subprocess.Popen(['python', 'home_screen/home.py'])
            break
        else:
            window['-OUTPUT-'].update('Error: Invalid credentials')

window.close()
