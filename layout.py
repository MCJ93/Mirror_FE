import PySimpleGUI as gui

elementKeys = {
  "currentTime": "_currentTime_",
  "currentDate": "_currentDate",
  "currentDayOfWeek": "_currentDayOfWeek_",
  "currentTemperature": "_currentTemperature_",
  "futureHourlyWeatherTime1": "_futureHourlyWeatherTime1_",
  "futureHourlyWeatherTime2": "_futureHourlyWeatherTime2_",
  "futureHourlyWeatherTime3": "_futureHourlyWeatherTime3_",
  "futureHourlyWeatherTime4": "_futureHourlyWeatherTime4_",
  "futureHourlyWeatherTime5": "_futureHourlyWeatherTime5_",
  "futureHourlyWeatherTime6": "_futureHourlyWeatherTime6_",
  "futureHourlyWeatherTime7": "_futureHourlyWeatherTime7_",
  "futureHourlyWeatherTime8": "_futureHourlyWeatherTime8_",
  "futureDailyIcon1": "_futureDailyIcon1",
  "futureDailyIcon2": "_futureDailyIcon2",
  "futureDailyIcon3": "_futureDailyIcon3",
  "futureDailyIcon4": "_futureDailyIcon4",
  "futureDailyIcon5": "_futureDailyIcon5",
  "futureDailyIcon6": "_futureDailyIcon6",
  "futureDailyValues1": "_futureDailyValues1_",
  "futureDailyValues2": "_futureDailyValues2_",
  "futureDailyValues3": "_futureDailyValues3_",
  "futureDailyValues4": "_futureDailyValues4_",
  "futureDailyValues5": "_futureDailyValues5_",
  "futureDailyValues6": "_futureDailyValues6_",
}

fontBig = ("Bebas Neue", 80)
fontMedium = ("Bebas Neue", 40)
fontSmall = ("Bebas Neue", 12)

baseText = "                   "

class BaseElement(gui.Text):
  def __init__(
    self,
    key,
    font,
    size=(None, None),
    justification=None
  ):
    super().__init__(
      text=baseText,
      key=key,
      background_color="#000",
      font=font,
      size=size,
      justification=justification
    ) 

class FutureHourlyWeatherText(BaseElement):
  def __init__(self, key):
    super().__init__(
      key,
      font=fontSmall,
      size=(6, 2),
      justification='right'
    )

class FutureDailyValue(BaseElement):
  def __init__(self, key):
    super().__init__(
      key,
      font=fontSmall,
      size=(8, 3),
      justification='right'
    )

class BigText(BaseElement):
  def __init__(self, key, size=(None, None), justification=None):
    super().__init__(
      key,
      font=fontBig,
      size=size,
      justification=justification
    )

class CurrentTemp(BigText):
  def __init__(self, key):
    super().__init__(
      key,
      size=(7, 1),
      justification="right"
    )

class MediumText(BaseElement):
  def __init__(self, key):
    super().__init__(
      key,
      font=fontMedium
    )

class Icon(gui.Image):
  def __init__(self, key):
    super().__init__(
      key=key,
      background_color="#000"
    )

class IconsSeparator(gui.Text):
  def __init__(self):
    super().__init__(
      size=(2, 1),
      background_color="#000"
    )

leftColumn = [
  [
    gui.Text(
      "",
      size=(0, 24),
      background_color="#000"
    ),
  ],
  [
    BigText(elementKeys["currentTime"])
  ],
  [
    gui.Text(
      "",
      size=(0, 6),
      background_color="#000"
    ),
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
      size=(0, 24),
      background_color="#000"
    ),
  ],
  [
    CurrentTemp(elementKeys["currentTemperature"])
  ],
  [
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTime1"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTime2"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTime3"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTime4"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTime5"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTime6"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTime7"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTime8"]),
  ],
  [
    gui.Text(
      "",
      size=(10, 1),
      background_color="#000"
    ),
    Icon(elementKeys["futureDailyIcon1"]),
    IconsSeparator(),
    Icon(elementKeys["futureDailyIcon2"]),
    IconsSeparator(),
    Icon(elementKeys["futureDailyIcon3"]),
    IconsSeparator(),
    Icon(elementKeys["futureDailyIcon4"]),
    IconsSeparator(),
    Icon(elementKeys["futureDailyIcon5"]),
    IconsSeparator(),
    Icon(elementKeys["futureDailyIcon6"]),
  ],
  [
    gui.Text(
      "",
      size=(5, 1),
      background_color="#000"
    ),
    FutureDailyValue(elementKeys["futureDailyValues1"]),
    FutureDailyValue(elementKeys["futureDailyValues2"]),
    FutureDailyValue(elementKeys["futureDailyValues3"]),
    FutureDailyValue(elementKeys["futureDailyValues4"]),
    FutureDailyValue(elementKeys["futureDailyValues5"]),
    FutureDailyValue(elementKeys["futureDailyValues6"])
  ],
]

layout = [
  [
    gui.Column(
      leftColumn,
      size=(700, 700),
      justification='left',
      background_color="#000"
    ),
    gui.Column(
      rightColumn,
      size=(800, 900),
      justification='right',
      background_color="#000"
    )
  ]
]
