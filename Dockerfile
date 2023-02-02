FROM python:3.10.9

WORKDIR /src/app
COPY ../app ./
COPY ../requierments.txt ./

RUN pip install -r /src/app/requierments.txt
EXPOSE 8000

