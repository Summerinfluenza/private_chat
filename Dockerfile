FROM python:3.8

ENV APP_HOME=/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME/
RUN pip install --no-cache-dir -r requirements.txt

ADD . $APP_HOME/
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]