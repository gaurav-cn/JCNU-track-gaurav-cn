FROM python:3

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install -r /app/python-flask-server/requirements.txt

EXPOSE 8000
EXPOSE 8080

CMD sh entrypoint.sh
