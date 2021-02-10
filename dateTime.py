from datetime import datetime

daysOfWeekNo = [
  "monday", "tuesday", "wenesday", "thursday", "friday", "saturday", "sunday"
]

class DateTime:
  @property
  def currentTime(self):
    return datetime.time(datetime.now()).strftime('%H:%M:%S')

  @property
  def currentDate(self):
    return datetime.date(datetime.now()).strftime('%d.%m.%Y')

  @property
  def dayOfWeekNo(self):
    return datetime.today().weekday()

  @property
  def dayOfWeek(self):
    return daysOfWeekNo[datetime.today().weekday()]
