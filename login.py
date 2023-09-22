"""
Module for the Login Screen GUI and start of the application.
"""

import PySimpleGUI as sg

import home_screen.home as home

def make_login():
    sg.theme('DarkGrey5')

    title = ("Century Gothic", 18)
    sg.set_options(font=('Century Gothic', 10))

    layout = [
        [sg.T("Login", font=title)],
        [sg.HSeparator(pad=(70, (10, 40)))],
        [sg.Text("Username:"), sg.Input(key='-USERNAME-', size=(18,1))],
        [sg.Text("Password:"), sg.Input(key='-PASSWORD-', password_char='•', size=(18,1))],
        [sg.Text(size=(40,1), key='-OUTPUT-', pad=(0, 30), justification='c')],
        [sg.Button('Submit', key='-LOGIN-'), sg.Button('Quit')]
    ]

    return sg.Window('Login screen', layout, size=(400, 300), element_justification='c', margins=(0, 20))

# Hardcoded login credentials (username: password)
# credentials = {
#     'user1': 'password123',
#     'user2': 'password123',
#     'user3': 'password123'
# }

# logged_in = False

while True:
    window = make_login()
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        window.close()
        break
    if event == '-LOGIN-':
        window.close()
        home.main()
        # username = values['-USERNAME-']
        # password = values['-PASSWORD-']
        # # Check if the entered credentials are in the dictionary
        # if username in credentials and credentials[username] == password:
        #     logged_in = True
        #     # Run the home screen GUI
        #     home.main()
        break
    else:
        window['-OUTPUT-'].update('Error: Invalid credentials')

window.close()
