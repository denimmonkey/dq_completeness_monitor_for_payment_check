FROM python:3.8.3-slim 
COPY . /myapp
WORKDIR /myapp
RUN apt-get update \
    && sh .env \
    && apt-get -y install libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install psycopg2 \
    && pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]