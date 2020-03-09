FROM python:3.6.5-alpine3.7

RUN apk add --no-cache \
  gcc \
  build-base \
  linux-headers \
  python3-dev \
  uwsgi \
  uwsgi-python3 \
  uwsgi-http \
  build-base \
  libffi-dev \
  openssl-dev \
  supervisor

RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

RUN addgroup -S www-data && adduser -S -G www-data www-data 

# install uwsgi now because it takes a little while
RUN pip install --upgrade pip

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.
COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt

# add (the rest of) our code
COPY ./app /usr/src/app/
COPY app.ini /usr/src/app/
COPY app.service /usr/src/app/
COPY app-entrypoint.sh /
RUN mkdir /var/log/flask/
RUN chmod -R 755 /var/log/flask/
RUN chown -R www-data:www-data /var/log/flask/

RUN chmod 755 /app-entrypoint.sh
WORKDIR /usr/src/app/

CMD ["sh", "/app-entrypoint.sh"]

EXPOSE 5000
