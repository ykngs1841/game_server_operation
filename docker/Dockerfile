FROM python:3.10-slim

WORKDIR /app

COPY game-server/server.py .

RUN pip install prometheus_client

EXPOSE 8080

CMD ["python", "server.py"]