FROM python:alpine
WORKDIR /app
COPY main.py /app
VOLUME [/config]
VOLUME [/downloads]
RUN pip3 install --no-cache-dir requests schedule pytz
CMD ["python3","-u","/app/main.py"]
