FROM python:alpine
WORKDIR /app
COPY main.py /app
COPY init.py /app
COPY config.sample.json /app
VOLUME [/config]
VOLUME [/downloads]
RUN apk update && apk upgrade  && pip3 install --no-cache-dir requests schedule pytz && rm -rf /var/cache/apk/*
CMD ["python3","-u","/app/main.py"]
