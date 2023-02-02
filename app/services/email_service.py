import smtplib
import ssl
from typing import List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.utils import loger
from app.config import Config


def send_email(data, func):
    try:
        loger.log_info("Send email {d}".format(d=data))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
            server.login(Config.SMTP_EMAIL, Config.SMTP_PW)

            loger.log_info("Subject {}".format(data['subject']))
            loger.log_info("Content {}".format(data['body']))
            loger.log_info("To {}".format(data['recepient']))

            # Prepare message body
            message = MIMEMultipart("alternative")
            message["Subject"] = data['subject']
            message["From"] = Config.SMTP_EMAIL
            message["To"] = data['recepient']
            message_text = MIMEText(data['body'], 'plain')
            message.attach(message_text)
            # Send email
            server.sendmail(Config.SMTP_EMAIL,
                            data['recepient'], message.as_string())
            loger.log_info("Success send email {d}".format(d=data))
            # Close server
            server.quit()
            func(True)
    except:
        func(False)
