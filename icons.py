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
  img = Image.open(open(imagePath, "rb"))
  x, y = img.size

  imgAfterCrop = img.crop(( 15, 15, x - 5, y - 15 ))
  imgAfterResize = imgAfterCrop.resize([50, 40])
  img_byte_arr = io.BytesIO()
  imgAfterResize.save(img_byte_arr, format=img.format)
  img_byte_arr = img_byte_arr.getvalue()
  return img_byte_arr
