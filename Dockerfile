FROM continuumio/anaconda3:4.4.0
COPY . /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app