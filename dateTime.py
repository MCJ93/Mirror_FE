from datetime import datetime
import threading

class DateTime:
    @property
    def currentTime(self):
        return datetime.time(datetime.now()).strftime('%H:%M:%S')

    @property
    def currentDate(self):
        return datetime.date(datetime.now()).strftime('%d.%m.%Y')
