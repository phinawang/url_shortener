FROM nginx:1.14.0-alpine

ADD nginx.conf /etc/nginx/
ADD app.conf /etc/nginx/conf.d/

RUN addgroup -S www-data && adduser -S -G www-data www-data

CMD ["nginx"]

EXPOSE 5000
EXPOSE 443
