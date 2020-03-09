from shortener import app
from config import Config

# Get config 
config = Config()

#if __name__ == "__main__":
#    app.run()

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=5000, debug=config.DEBUG)