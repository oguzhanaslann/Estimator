
import datetime
import json

def current_time_millis():
    dt = datetime.datetime.now()
    return dt.microsecond / 1000