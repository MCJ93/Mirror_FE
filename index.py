from dateTime import DateTime
from layout import layout, elementKeys

import PySimpleGUI as gui

dateTimeObject = DateTime()

windowElement = gui.Window(title="Hello World", layout=layout, margins=(100, 50))

while True:
  event, values = windowElement.read(timeout=1000)
  # End program if user closes window or
  # presses the OK button
  windowElement[elementKeys["currentTime"]].update(dateTimeObject.currentTime) 

  if event == "OK" or event == gui.WIN_CLOSED:
    break

windowElement.close()

print("test")
# print(DateTime())
