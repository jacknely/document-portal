FROM python:3.8-slim

RUN mkdir /app

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "manage.py", "runserver"]
