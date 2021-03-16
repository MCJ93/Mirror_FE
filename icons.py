import io
import base64
from urllib.request import urlopen
from PIL import Image  

class Icons:
  def __init__(self, dailyWeather):
    self.dailyWeather = dailyWeather
    self.icons = []

  def fetchIcons(self):
    for index in range(7):
      self.icons.append(self.getIcon(self.dailyWeather[index].icon))

  def getIcon(self, iconName):
    return 
    # baseUrl = f"http://openweathermap.org/img/wn/{iconName}@2x.png"
    # image_byt = urlopen(baseUrl).read()
    # return base64.encodestring(image_byt)

def cropImage(imagePath):
  # Image.open(imagePath)
  # image_byt = imagePath.read()
  # base = base64.encodestring(image_byt)
  img = Image.open(imagePath)

  w, h = img.size

  left = w/4
  right = 3*w/4
  upper = h/4
  lower = 3*h/4

  img.crop([ left, upper, right, lower])
  return base64.b64encode(img)
