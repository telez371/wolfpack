FROM python:3.11.2-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN apt-get update && apt-get install libpq-dev gcc -y

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD .. /app/

ADD entrypoint.sh /app/
ENTRYPOINT ["./entrypoint.sh"]