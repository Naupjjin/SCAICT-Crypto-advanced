FROM alpine/socat

RUN apk add --no-cache python3 py3-pip

RUN python3 -m venv /opt/venv

RUN mkdir -p /app
WORKDIR /app

COPY ./src /app/
RUN  /opt/venv/bin/pip install -r requirements.txt

EXPOSE 60003
ENTRYPOINT ["socat", "tcp-listen:60003,fork", "EXEC:'/opt/venv/bin/python server.py'"]