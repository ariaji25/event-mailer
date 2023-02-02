import pytz
import os


class Config:
    app_port = 8000
    timezone = pytz.timezone("Asia/Singapore")
    debug_mode = True
    db_user = os.environ["DB_USER"]
    db_name = os.environ["DB_NAME"]
    db_pass = os.environ["DB_PASS"]
    db_host = os.environ["DB_HOST"]
    SMTP_EMAIL = os.environ['SMTP_EMAIL']
    SMTP_PW = os.environ['SMTP_PW'] 
