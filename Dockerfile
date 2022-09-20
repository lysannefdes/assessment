FROM python:latest

COPY server.py /

EXPOSE 8080

CMD python3 server.py


# Build docker image as simple-server:v1
