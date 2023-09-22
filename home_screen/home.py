"""
Module for the Home Screen GUI
"""
import PySimpleGUI as sg
import subprocess

import des.screen_one as des_one
import des.screen_two as des_two
import des.screen_three as des_three

def make_home_screen():
    """
    Create and display the home screen GUI.

    This function creates the home screen GUI, which includes three columns, one for each of the data exploration screens.
    Users can click on buttons to navigate to different screens or log out.

    Parameters:
        None

    Returns:
        sg.Window: The PySimpleGUI window object for the home screen.
    """
    
    sg.theme('LightBrown12')

    # Set the default font for the GUI
    title = ("Century Gothic", 18)
    sg.set_options(font=('Century Gothic', 10))

    header = [
        [sg.Push(), sg.T("Home Screen", font=title, pad=((100, 0), (10, 0))),
        sg.Push(), sg.Button('Logout', key='-LOGOUT-', size=(12, 1), pad=(0, (10, 0)), button_color=('white', '#4DA30F'))]
    ]

    col1 = [
        [sg.Image(r'./images/DES1.png', size=(200, 200), pad=(0, (0, 15)), background_color='#363636')],
        [sg.Button('View Screen 1', size=(21, 1), key='Screen 1', pad=(0, (0, 10)), button_color=('white', '#636363'))]
    ]

    col2 = [
        [sg.Image(r'./images/DES2.png', size=(200, 200), pad=(0, (0, 15)), background_color='#363636')],
        [sg.Button('View Screen 2', size=(21, 1), key='Screen 2', pad=(0, (0, 10)), button_color=('white', '#636363'))]
    ]

    col3 = [
        [sg.Image(r'./images/DES3.png', size=(200, 200), pad=(0, (0, 15)), background_color='#363636')],
        [sg.Button('View Screen 3', size=(21, 1), key='Screen 3', pad=(0, (0, 10)), button_color=('white', '#636363'))]
    ]

    layout = [
        [header],
        [sg.HSeparator(pad=(70, (20, 40)))],
        [sg.Column(col1, element_justification='c', background_color='#363636'), 
        sg.Column(col2, element_justification='c', pad=(20, 0), background_color='#363636'), 
        sg.Column(col3, element_justification='c', background_color='#363636')]  
    ]

    return sg.Window('Home Screen', layout, size=(700, 450), element_justification='c')

def main():
    """
    Start the Home Screen application.

    This function starts the Home Screen application and handles user interactions.
    It creates the home screen, and navigates to different screens or logs the user out on button clicks.

    Parameters:
        None

    Returns:
        None
    """    
    # Display and interact with the Window using an Event Loop
    window = make_home_screen()
    
    while True:
        
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:  
            window.close()
            break
        
        if event == '-LOGOUT-':
            window.close()
            subprocess.Popen('python login.py')
            # Run the login screen GUI
            break
        
        # View screen 1 when the button is clicked
        if event == "Screen 1":
            des_one.make_screen_one()
        
        # View screen 2 when the button is clicked
        if event == "Screen 2":
            des_two.make_screen_two()
        
        # View screen 3 when the button is clicked
        if event == "Screen 3":
            des_three.make_screen_three()
            
    window.close()
    
if __name__ == '__main__':
    main()