# This program will be heavily commented because it is for my learning, I want to know what I did and why I did it when
# I have long forgotten why I did them

import PySimpleGUI as sg

# They layout is a list that is going to contain other lists
# Think of the screen broken up into 3 rows, the first list is the top row (top of the screen).
# The second list is the middle row of the screen (middle of the screen), and list 3 is the bottom row (bottom of the screen)
layout = [
    [
        sg.Input(key = "-INPUT-"),
        sg.Spin(["km to miles", "kg to pounds", "seconds to minutes"], key = "-UNITS-"),
        sg.Button("Convert", key = "-CONVERT-")
    ],
    [sg.Text("Output", key = "-OUTPUT-")]
]

# Converter is the string for the title parameter for sg.Window().
window = sg.Window("Converter", layout)

while True:
    # .read() listens for any kind of input on the window, so if this is the last
    # line in the program, once you click a button or something, the program will end
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # Handling the event of sg.Button("Convert") being pressed, we use "Button" as the event because
    # we named it sg.Button("Convert")
    if event == "-CONVERT-":
        input_value = values["-INPUT-"]

        if input_value.isnumeric():
            match values["-UNITS-"]:
                case "km to miles":
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f"{input_value} km are {output} miles."
                case "kg to pounds":
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f"{input_value} kg are {output} pounds."
                case "seconds to minutes":
                    output = round(float(input_value) / 60, 2)
                    output_string = f"{input_value} seconds are {output} minutes."

            window["-OUTPUT-"].update(output_string)

window.close()
