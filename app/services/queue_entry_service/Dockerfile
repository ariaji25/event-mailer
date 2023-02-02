FROM python:3.10.9

RUN apt-get update && apt-get -y install cron vim
WORKDIR /src/app
COPY ./app/services/queue_entry_service/crontab /etc/cron.d/crontab

RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
COPY ../app ./
COPY ../requierments.txt ./

RUN pip install -r /src/app/requierments.txt