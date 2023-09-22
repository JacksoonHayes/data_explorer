"""
Module for the DES 2 GUI
"""

import PySimpleGUI as sg
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import home_screen.home as home
import des.screen_one as des_one
import des.screen_three as des_three

def make_screen_two():
    """
    Create and display the main screen for DES 2 GUI.

    This function creates the main screen for the Data Explorer Screen 1 GUI, which includes a graph, navigation bar, and controls.
    Users can interact with the graph (zoom, pan) and navigate to other screens.

    Parameters:
        None

    Returns:
        None
    """

    # Create the graph
    fig, ax = plt.subplots()

    # Placeholder data for the graph
    x = [0, 2, 4, 6, 8, 10]
    y = [0, 5, 2, 6, 3, 5]
    ax.plot(x, y)
    ax.set_title('Placeholder Graph')

    sg.theme('DarkGrey5')

    # Set the default font for the GUI
    sg.set_options(font=('Century Gothic', 10))

    # Navigation bar at the top of the screen
    navbar = [
        [sg.Button('Home', size=(15, 1), key='Home', button_color=('white', '#4DA30F')),
        sg.Push(background_color='#6E6E6E'),
        sg.Button('Screen 1', size=(15, 1), key='Screen 1', button_color=('white', '#4DA30F')),
        sg.Button('Screen 3', size=(15, 1), key='Screen 3', button_color=('white', '#4DA30F'))]
    ]

    # Column 1 of the GUI. Main column for graph/chart and its controls
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

    # Column 2 of the GUI. Column for summary and chat
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

    window = sg.Window('Data Explorer 2', layout, finalize=True, background_color='#6E6E6E')

    # Draw the graph onto the canvas
    canvas_elem = window['-CANVAS-']
    canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        
        # Zoom in on the graph. changes the x and y limits of the graph        
        if event == 'Zoom In':
            current_xlim = ax.get_xlim()
            current_ylim = ax.get_ylim()
            if current_xlim[1] == 10 and current_ylim[1] == 10:
                ax.set_xlim(0, 5)
                ax.set_ylim(0, 5)
                canvas.draw()
            else:
                ax.set_xlim(0, 10)
                ax.set_ylim(0, 10)
                canvas.draw()

        # Zoom out on the graph. changes the x and y limits of the graph
        if event == 'Zoom Out':
            current_xlim = ax.get_xlim()
            current_ylim = ax.get_ylim()
            if current_xlim[1] == 10 and current_ylim[1] == 10:
                ax.set_xlim(-5, 15)
                ax.set_ylim(-5, 15)
                canvas.draw()
            else:
                ax.set_xlim(0, 10)
                ax.set_ylim(0, 10)
                canvas.draw()

        # Pan left on the graph. changes the x limits of the graph
        if event == 'Pan Left':
            current_xlim = ax.get_xlim()
            ax.set_xlim(current_xlim[0] - 1, current_xlim[1] - 1)
            canvas.draw()

        # Pan right on the graph. changes the x limits of the graph
        if event == 'Pan Right':
            current_xlim = ax.get_xlim()
            ax.set_xlim(current_xlim[0] + 1, current_xlim[1] + 1)
            canvas.draw()
        
        # Return to the home screen if button is clicked
        if event == 'Home':
            home.main()
            break
        
        # Open the first DES if button is clicked
        if event == 'Screen 1':
            des_one.make_screen_one()
            break
        
        # Open the third DES if button is clicked
        if event == 'Screen 3':
            des_three.make_screen_three()
            break

    window.close()

if __name__ == '__main__':
    make_screen_two()