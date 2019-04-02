from datetime import datetime
import pytz

class TimeConversion:
    def __init__(self, unix_time):
        self.unix_time = self.nanoseconds_to_seconds(unix_time)
        self.date = self.convert_unix_time() 
        self.utc_time = self.get_utc_time()
        self.cern_time = self.get_cern_time()

    def nanoseconds_to_seconds(self, n_seconds):
        seconds = n_seconds/10**9
        return seconds

    def convert_unix_time(self):
        date = datetime.utcfromtimestamp(self.unix_time)
        return date

    def get_utc_time(self):
        datetime_in_utc = self.date.astimezone(pytz.utc)
        return datetime_in_utc

    def get_cern_time(self):
        datetime_in_cern = self.date.astimezone(pytz.timezone('Europe/Zurich'))
        return datetime_in_cern

