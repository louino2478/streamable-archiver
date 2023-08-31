FROM python:alpine
WORKDIR /app
COPY main.py /app
VOLUME [/config]
VOLUME [/downloads]
RUN pip3 install --no-cache-dir requests
CMD ["python3","/app/main.py"]
