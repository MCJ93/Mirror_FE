import requests, json 
from mockup import mockup

class Weather:
  def __init__(self, weatherObject):
    self.temp = weatherObject["temp"]
    self.feelTemp = weatherObject["feels_like"]
    self.description = weatherObject["weather"][0]["description"]
    self.windSpeed = weatherObject["wind_speed"]
    self.pressure = weatherObject["pressure"]


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

  @property
  def current(self):
    return Weather(mockup["current"])

  @property
  def futureHourly(self):
    mappedFutureHourly = list(map(lambda hourlyWeather : self.mapWeather(hourlyWeather), mockup["hourly"]))
    print(mappedFutureHourly[0].temp)
    # return map(lambda hourlyWeather : self.mapWeather(hourlyWeather), mockup["hourly"])
