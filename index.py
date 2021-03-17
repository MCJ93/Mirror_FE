from dateTime import DateTime, daysOfWeekNo
from layout import layout, elementKeys
from weather import CombinedWeather
from translator import Translator
from icons import Icons, cropImage, cropImageMockup
import tkinter as Tk

import PySimpleGUI as gui

degree_sign= u'\N{DEGREE SIGN}'
lngKey = "pl"


translatorObject = Translator(lngKey)
dateTimeObject = DateTime()
weatherObject = CombinedWeather()
icons = Icons(weatherObject.futureDaily)
icons.fetchIcons()

gui.theme("Black")



windowElement = gui.Window(
  title="Hello World",
  layout=layout,
  margins=(30, 30),
  no_titlebar=True,
  location=(0,0),
  size=(1366,768),
  keep_on_top=True,
).Finalize()

windowElement.Maximize()
while True:
  event, values = windowElement.read(timeout=1000)

  currentTime = dateTimeObject.currentTime
  currentDate = dateTimeObject.currentDate
  dayOfWeek = translatorObject.getTranslation(dateTimeObject.dayOfWeek)
  currentTemperature = weatherObject.current.temp
  futureWeatherHourly = weatherObject.futureHourly
  futureWeatherDaily = weatherObject.futureDaily

  windowElement[elementKeys["currentTime"]].update(currentTime)
  windowElement[elementKeys["currentDate"]].update(currentDate)
  windowElement[elementKeys["currentDayOfWeek"]].update(dayOfWeek)

  windowElement[elementKeys["currentTemperature"]].update(currentTemperature)

  for index in range(1, 8):
    windowElement[elementKeys[f"futureHourlyWeatherTime{index}"]].update(f"{futureWeatherHourly[index - 1]['hour']} \n {futureWeatherHourly[index - 1]['temperature']}")

  for dailyIndex in range(0, 5):
    # croppedImage = cropImageMockup("/home/macjej/Workspace/mirror/assets/10d@2x.png")
    croppedImage = cropImage(icons.icons[dailyIndex])
    windowElement[elementKeys[f"futureDailyIcon{dailyIndex + 1}"]].update(data=Tk.PhotoImage(
      data=croppedImage
    ))
    futureDayOfWeek = translatorObject.getTranslation(daysOfWeekNo[futureWeatherDaily[dailyIndex].weekDay])[0:3]
    windowElement[elementKeys[f"futureDailyValues{dailyIndex + 1}"]].update(
      f"{futureDayOfWeek} \n {futureWeatherDaily[dailyIndex].temp_min_degrees} \n {futureWeatherDaily[dailyIndex].temp_max_degrees}"
    )

  

  if event == "OK" or event == gui.WIN_CLOSED:
    break

windowElement.close()
