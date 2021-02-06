from datetime import datetime
import threading

class DateTime:
    currentTime = ""
    currentDate = ""

    def __init__(self):
        threading.Timer(1, self.getTimeDate).start()

    def getTimeDate(self):
        print("TRY")
        # currentTime = datetime.time(datetime.now()).strftime('%H:%M')
        currentTime = datetime.time(datetime.now())
        currentDate = datetime.date(datetime.now()).strftime('%d.%m.%Y')

        print(currentTime)
        print(currentDate)

        self.currentTime = currentTime
        self.currentDate = currentDate

