from dateTime import DateTime
from layout import layout, elementKeys
from weather import CombinedWeather
from translator import Translator
from icons import Icons, cropImage
import tkinter as Tk

import PySimpleGUI as gui

degree_sign= u'\N{DEGREE SIGN}'
lngKey = "pl"


translatorObject = Translator(lngKey)
dateTimeObject = DateTime()
weatherObject = CombinedWeather()
icons = Icons(weatherObject.futureDaily)

icons.fetchIcons()
print(icons.icons)

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
while True:
  event, values = windowElement.read(timeout=1000)

  currentTime = dateTimeObject.currentTime
  currentDate = dateTimeObject.currentDate
  dayOfWeek = translatorObject.getTranslation(dateTimeObject.dayOfWeek)
  currentTemperature = weatherObject.current.temp
  futureWeather = weatherObject.futureHourly

  windowElement[elementKeys["currentTime"]].update(currentTime)
  windowElement[elementKeys["currentDate"]].update(currentDate)
  windowElement[elementKeys["currentDayOfWeek"]].update(dayOfWeek)

  windowElement[elementKeys["currentTemperature"]].update(currentTemperature)

  for index in range(1, 8):
    windowElement[elementKeys[f"futureHourlyWeatherTime{index}"]].update(futureWeather[index - 1]["hour"])
    windowElement[elementKeys[f"futureHourlyWeatherTemp{index}"]].update(futureWeather[index - 1]["temperature"])

  for dailyIndex in range(0, 1):
    windowElement[elementKeys[f"futureDailyIcon{dailyIndex + 1}"]].update(data=Tk.PhotoImage(
      # data=icons.icons[dailyIndex], height = 100, width=100).zoom(1, 1)
      cropImage("/home/macjej/Workspace/mirror/assets/10d@2x.png")
    ))

  

  if event == "OK" or event == gui.WIN_CLOSED:
    break

windowElement.close()

print("test")
