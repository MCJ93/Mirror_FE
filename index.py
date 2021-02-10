from dateTime import DateTime
from layout import layout, elementKeys
from weather import CombinedWeather
from translator import Translator

import PySimpleGUI as gui

lngKey = "pl"

translatorObject = Translator(lngKey)
dateTimeObject = DateTime()
weatherObject = CombinedWeather()

windowElement = gui.Window(title="Hello World", layout=layout, margins=(100, 50))
print(translatorObject.getTranslation(dateTimeObject.dayOfWeek))
while True:
  event, values = windowElement.read(timeout=1000)
  windowElement[elementKeys["currentTime"]].update(dateTimeObject.currentTime)
  windowElement[elementKeys["currentDate"]].update(dateTimeObject.currentDate)
  windowElement[elementKeys["currentDayOfWeek"]].update(translatorObject.getTranslation(dateTimeObject.dayOfWeek))

  if event == "OK" or event == gui.WIN_CLOSED:
    break

windowElement.close()

print("test")
# print(DateTime())
