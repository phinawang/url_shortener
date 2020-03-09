# URL Shortener
- Hi, This is Python Flask Project on uWSGI and Nginx. :)
- Database: MongoDB
- Encrypt: 

## Table of Contents

  * [Pre requisite](#pre-requisite)
  * [Installation](#installation)
  * [Run](#run)
  * [API](#api)
     * [1. [POST] /shortener ](#1._[post]_/shortener)
     * [2. [GET] /{short_code}](#2.[get]_/{short_code})

## Pre requisite
- docker 
- docker-compose

## Installation
 1. Clone repository
```
git clone https://github.com/phinawang/url_shortener.git
```
2. Build docker-compose
```
cd url_shortener
docker-compose build --force-rm  --no-cache
```

## Run
1. Run docker-compose
```
docker-compose up
```
Server will run by default under http://localhost:5000


## API

### User List:
- api url: POST http://localhost:5000/

|  | METHOD | URL | DESCRIPTION |
|---| ---------- | --- | --- |
| 1 | POST | /shortener                              | Register a long URL, will return a shorten URL |
| 2 | GET | /{short_code}                        | Redirct shorten URL to long URL |

### 1. [POST] /shortener 

  #### Request:
```json
{
  "url":"http://www.google.com"
}
```

  #### Response: 
  ##### Success
```http
HTTP/1.1 200 OK
Content-Type: application/json
Server: localhost:5000
{
  "short_code": "gqZ882", 
  "short_url": short_url,
  "status": 200
}
```
  ##### False
```http
HTTP/1.1 400 BAD REQUEST
Content-Type: application/json
Server: localhost:5000
{
  "message": "This url too long", 
}
```
### 2. [GET] /{short_code}
#### Request:
http://localhost:5000/{short_code}
#### Response: 
##### Success:
Redirct to long url
##### False:
```http
HTTP/1.1 400 BAD REQUEST
Content-Type: application/json
Server: localhost:5000
{
  "message": "This shorten url is invalid"
}


