from flask import Flask, jsonify, request, redirect, Blueprint, flash, render_template
from flask_restful import Api, Resource, reqparse, inputs, abort
from pymongo import MongoClient
import base62
import hashlib
import logging
import functools
from models import Url_model as UrlModel
from config import Config
from database import Db
from errors import register_error_handler_for_app
import time


app = Flask(__name__)
api = Api(app, catch_all_404s=True)

# Get config 
config = Config()

# Init db
db = Db(config).db
if db == None:
    abort(500, message = 'Cannot connect to Database')

# Register error handler
register_error_handler_for_app(app)

# Log format
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s [%(thread)d][%(levelname)s] [%(filename)s:%(lineno)d] [%(thread)d] - %(message)s',datefmt='%d/%m/%Y %H:%M:%S',filename='/var/log/flask/flask.log')


class RegisterURL(Resource):

    def __init__(self, db):
        self.parser = reqparse.RequestParser()
        result = self.parser.add_argument('url', required=True, type=inputs.url, help='URL format error')
        self.db = db

    def post(self):      
        # Get posted data
        arg = self.parser.parse_args()
        url = arg["url"]
        
        if len(url) > config.MAX_URL_LENGTH:
            abort(400, message = 'This url is too long')
        else:
            # Encrypt url 
            url = url + str(time.time())
            encodeUrl = url.encode()
            shortCode = base62.encodebytes(hashlib.md5(encodeUrl).digest()[-5:])

            # Insert record to database
            urls = UrlModel.UrlModel(db)
            result = urls.insertUrl(url, shortCode)

            # Return successful result
            retJosn = {
                "status": 200,
                "short_url": shortCode 
            }
            app.logger.info("Register url success")
            return jsonify(retJosn)

class RedirctShortURL(Resource):

    def __init__(self, db):
        self.db = db
        self.parser = reqparse.RequestParser()

    def get(self, shortCode):
        if len(shortCode) == 7:

            # Get long URL in database
            urls = UrlModel.UrlModel(db)
            result = urls.getUrl(shortCode)

            # If long URL exist, redirect.
            if result and 'url' in result:
                app.logger.info("Redirect url: %s",result['url'])
                return redirect(result['url'])
            else:
                app.logger.error("Redirect url: %s",result['url'])
                abort(400, message = 'This shorten url is invalid')
        else:
            app.logger.error("This shorten url is invalid")
            abort(400, message = 'This shorten url is invalid')


class Home(Resource):
    def __init__(self):
        pass

    def get(self):
        bp = Blueprint('template', __name__, url_prefix='/')
        app.register_blueprint(bp)

        return render_template('view/index.html')

#API routing
api.add_resource(RegisterURL, '/shortener', resource_class_kwargs={'db': db})
api.add_resource(RedirctShortURL, '/<shortCode>', resource_class_kwargs={'db': db})
api.add_resource(Home, '/')

#if __name__ == "__main__":
#    app.run(host='0.0.0.0',port=5000, debug=config.DEBUG)
