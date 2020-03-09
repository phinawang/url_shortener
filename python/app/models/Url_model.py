import datetime

class UrlModel:
    # Connect to database
    def __init__(self, db):
        self.db = db

    def getUrl(self, shortCode):  
        try:
            result = self.db['urls'].find_one({
                "short_code": shortCode
            })
            return result
        except:
            raise

    def insertUrl(self, url, shortCode):
        try:
            self.db['urls'].insert({
                "url": url,
                "short_code": shortCode,
                "datetime": datetime.datetime.utcnow()
            })
        except:
            raise