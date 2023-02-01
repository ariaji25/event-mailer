import datetime

from config import Config

def get_datetime_now():
    return datetime.datetime.now(Config.timezone)