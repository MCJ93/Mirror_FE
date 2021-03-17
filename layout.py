import PySimpleGUI as gui

# find a way to loop future hourly weather, right now it's horrible
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
  "futureHourlyWeatherTemp1": "_futureHourlyWeatherTemp1_",
  "futureHourlyWeatherTemp2": "_futureHourlyWeatherTemp2_",
  "futureHourlyWeatherTemp3": "_futureHourlyWeatherTemp3_",
  "futureHourlyWeatherTemp4": "_futureHourlyWeatherTemp4_",
  "futureHourlyWeatherTemp5": "_futureHourlyWeatherTemp5_",
  "futureHourlyWeatherTemp6": "_futureHourlyWeatherTemp6_",
  "futureHourlyWeatherTemp7": "_futureHourlyWeatherTemp7_",
  "futureHourlyWeatherTemp8": "_futureHourlyWeatherTemp8_",
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

fontBig = ("Bebas Neue", 60)
fontMedium = ("Bebas Neue", 25)
fontSmall = ("Bebas Neue", 8)

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
      size=(4, 1),
      justification='center'
    )

class FutureDailyValue(BaseElement):
  def __init__(self, key):
    super().__init__(
      key,
      font=fontSmall,
      size=(7, 3),
      justification='left'
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

class Icon(gui.Image):
  def __init__(self, key):
    super().__init__(
      key=key,
      background_color="#000"
    )

leftColumn = [
  [
    gui.Text(
      "",
      size=(0, 28),
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
      size=(0, 28),
      background_color="#000"
    ),
  ],
  [
    BigText(elementKeys["currentTemperature"])
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
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTemp1"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTemp2"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTemp3"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTemp4"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTemp5"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTemp6"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTemp7"]),
    FutureHourlyWeatherText(elementKeys["futureHourlyWeatherTemp8"])
  ],
  [
    Icon(elementKeys["futureDailyIcon1"]),
    Icon(elementKeys["futureDailyIcon2"]),
    Icon(elementKeys["futureDailyIcon3"]),
    Icon(elementKeys["futureDailyIcon4"]),
    Icon(elementKeys["futureDailyIcon5"]),
    Icon(elementKeys["futureDailyIcon6"]),
  ],
  [
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
