import datetime

from app.config import Config

def log_info(*data: object):
    if Config.debug_mode:
        log = "[INFO:{d}] ".format(d=datetime.datetime.now())
        print(log, data)