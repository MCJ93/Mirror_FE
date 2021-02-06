from timeDate import DateTime
import PySimpleGUI as gui

dateTime = DateTime()

# layout = [[gui.Text(dateTime.currentTime)], [gui.Button("OK")]]
# windowElement = gui.Window(title="Hello World", layout=layout, margins=(100, 50)).read()

while True:
    print(dateTime.currentTime)
#     event, values = windowElement.read()
#     # End program if user closes window or
#     # presses the OK button
#     if event == "OK" or event == gui.WIN_CLOSED:
#         break

# windowElement.close()

print("test")
# print(DateTime())
