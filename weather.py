import requests, json 
from mockup import mockup
from datetime import datetime

degree_sign= u'\N{DEGREE SIGN}'

class Weather:
  def __init__(self, weatherObject):
    self.date = weatherObject["dt"]
    self.temp_raw = round(weatherObject['temp'])
    self.temp_degrees = f"{round(weatherObject['temp'], 1)}{degree_sign}"
    self.temp = f"{round(weatherObject['temp'], 1)}{degree_sign}C"
    self.feelTemp = weatherObject["feels_like"]
    self.description = weatherObject["weather"][0]["description"]
    self.windSpeed = weatherObject["wind_speed"]
    self.pressure = weatherObject["pressure"]

class FutureDailyWeather:
  def __init__(self, weatherObject):
    self.date = weatherObject["dt"]
    self.icon = weatherObject["weather"][0]["icon"]
    self.weekDay= datetime.fromtimestamp(weatherObject["dt"]).weekday()
    self.temp_max_raw = round(weatherObject['temp']['max'])
    self.temp_min_raw = round(weatherObject['temp']['min'])
    self.temp_max_degrees = f"{round(weatherObject['temp']['max'])}{degree_sign}"
    self.temp_min_degrees = f"{round(weatherObject['temp']['min'])}{degree_sign}"

class CombinedWeather:
  bytomLat = 50.348
  bytomLon = 18.9328

  completeUrl = (
    'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={apiKey}&units={unit}&lang={lang}&exclude={exclude}'
      .format(
        lat = bytomLat,
        lon = bytomLon,
        apiKey = 'ad2fa9d2857e20a17e0d2b6363e6dab7',
        unit='metric',
        lang='pl',
        exclude='minutely,alerts'
      )
  )

  def mapWeather(self, weatherObject):
    return Weather(weatherObject)

  def mapDailyFutureWeather(self, weatherObject):
    return FutureDailyWeather(weatherObject)

  @property
  def current(self):
    return Weather(mockup["current"])

  def formatFutureHourly(self, weather):
    futureDate = datetime.utcfromtimestamp(3600 * ((weather.date + 1800) // 3600))
    return { "hour": f"{futureDate.strftime('%H')}'", "temperature": weather.temp_degrees }

  @property
  def futureHourly(self):
    return list(
      map(
        lambda hourlyWeather : self.formatFutureHourly(self.mapWeather(hourlyWeather)),
        mockup["hourly"]
      )
    )


  @property
  def futureDaily(self):
    return list(map (lambda dailyWeather : self.mapDailyFutureWeather(dailyWeather), mockup["daily"]))
