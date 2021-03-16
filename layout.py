import PySimpleGUI as gui

# find a way to loop future hourly weather, right now it's horrible
elementKeys = {
  "currentTime": "_currentTime_",
  "currentDate": "_currentDate",
  "currentDayOfWeek": "_currentDayOfWeek_",
  "currentTemperature": "_currentTemperature_",
  "futureHourlyWeatherTime1": "_futureHourlyWeather1_",
  "futureHourlyWeatherTime2": "_futureHourlyWeather2_",
  "futureHourlyWeatherTime3": "_futureHourlyWeather3_",
  "futureHourlyWeatherTime4": "_futureHourlyWeather4_",
  "futureHourlyWeatherTime5": "_futureHourlyWeather5_",
  "futureHourlyWeatherTime6": "_futureHourlyWeather6_",
  "futureHourlyWeatherTime7": "_futureHourlyWeather7_",
  "futureHourlyWeatherTime8": "_futureHourlyWeather8_"
}

fontBig = ("Bebas Neue", 60)
fontMedium = ("Bebas Neue", 25)
fontSmall = ("Bebas Neue", 10)

baseText = "                   "

class BaseElement(gui.Text):
  def __init__(
    self,
    key,
    font
  ):
    super().__init__(
      text=baseText,
      key=key,
      background_color="#000",
      font=font
    ) 

class FutureHourlyWeatherTimeText(BaseElement):
  def __init__(self, key):
    super().__init__(
      key,
      font=fontSmall
    )

class BigText(BaseElement):
  def __init__(self, key):
    super().__init__(
      key,
      font=fontBig
    )

class MediumText(BaseElement):
  def __init__(self, key):
    super().__init__(
      key,
      font=fontMedium
    )

leftColumn = [
  [
    gui.Text(
      "",
      size=(0, 32),
      background_color="#000"
    ),
  ],
  [
    BigText(elementKeys["currentTime"])
  ],
  [
    MediumText(elementKeys["currentDayOfWeek"]),
    MediumText(elementKeys["currentDate"]),
    gui.Button("OK")
  ]
]

rightColumn = [
  [
    gui.Text(
      "",
      size=(0, 32),
      background_color="#000"
    ),
  ],
  [
    BigText(elementKeys["currentTemperature"])
  ],
  [
    FutureHourlyWeatherTimeText(elementKeys["futureHourlyWeatherTime1"]),
    FutureHourlyWeatherTimeText(elementKeys["futureHourlyWeatherTime2"]),
    FutureHourlyWeatherTimeText(elementKeys["futureHourlyWeatherTime3"]),
    FutureHourlyWeatherTimeText(elementKeys["futureHourlyWeatherTime4"]),
    FutureHourlyWeatherTimeText(elementKeys["futureHourlyWeatherTime5"]),
    FutureHourlyWeatherTimeText(elementKeys["futureHourlyWeatherTime6"]),
    FutureHourlyWeatherTimeText(elementKeys["futureHourlyWeatherTime7"]),
    FutureHourlyWeatherTimeText(elementKeys["futureHourlyWeatherTime8"]),
  ]
]

layout = [
  [
    gui.Column(
      leftColumn,
      size=(800, 800),
      background_color="#000"
    ),
    gui.Column(
      rightColumn,
      size=(400, 800),
      background_color="#000"
    )
  ]
]
