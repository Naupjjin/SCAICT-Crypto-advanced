FROM alpine/socat

RUN apk add --no-cache python3 py3-pip

RUN python3 -m venv /opt/venv

RUN mkdir -p /app
WORKDIR /app

COPY ./src /app/

EXPOSE 30000
ENTRYPOINT ["socat", "tcp-listen:30000,fork", "EXEC:'/opt/venv/bin/python server.py'"]