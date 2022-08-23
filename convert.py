# This program will be heavily commented because it is for my learning, I want to know what I did and why I did it when
# I have long forgotten why I did them

import PySimpleGUI as sg

# They layout is a list that is going to contain other lists
# Think of the screen broken up into 3 rows, the first list is the top row (top of the screen).
# The second list is the middle row of the screen (middle of the screen), and list 3 is the bottom row (bottom of the screen)
layout = [
    [sg.Input(), sg.Spin(["km to miles", "kg to pounds", "seconds to minuets"])],
    [sg.Button("Button")]
]

# Converter is the string for the title parameter for sg.Window().
window = sg.Window("Converter", layout)

while True:
    # .read() listens for any kind of input on the window, so if this is the last
    # line in the program, once you click a button or something, the program will end
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # Handling the event of sg.("Button") being pressed, we use "Button" as the event because
    # we named it sg.("Button")
    if event == "Button":
        # If you put a key on your layout elements, you can print that value specifically by its key
        print(values)

window.close()
