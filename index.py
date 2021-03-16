from dateTime import DateTime
from layout import layout, elementKeys
from weather import CombinedWeather
from translator import Translator

import PySimpleGUI as gui

degree_sign= u'\N{DEGREE SIGN}'
lngKey = "pl"


translatorObject = Translator(lngKey)
dateTimeObject = DateTime()
weatherObject = CombinedWeather()

gui.theme("Black")

windowElement = gui.Window(
  title="Hello World",
  layout=layout,
  margins=(30, 30),
  no_titlebar=True,
  location=(0,0),
  size=(1280,800),
  keep_on_top=True,
).Finalize()

windowElement.Maximize()
print(translatorObject.getTranslation(dateTimeObject.dayOfWeek))
print(degree_sign)
while True:
  event, values = windowElement.read(timeout=1000)

  currentTime = dateTimeObject.currentTime
  currentDate = dateTimeObject.currentDate
  dayOfWeek = translatorObject.getTranslation(dateTimeObject.dayOfWeek)
  currentTemperature = f"{weatherObject.current.temp}{degree_sign}C"
  print(currentTemperature)

  windowElement[elementKeys["currentTime"]].update(currentTime)
  windowElement[elementKeys["currentDate"]].update(currentDate)
  windowElement[elementKeys["currentDayOfWeek"]].update(dayOfWeek)

  windowElement[elementKeys["currentTemperature"]].update(currentTemperature)

  if event == "OK" or event == gui.WIN_CLOSED:
    break

windowElement.close()

print("test")
# print(DateTime())
