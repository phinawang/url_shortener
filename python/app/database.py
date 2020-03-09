# -*- coding: utf-8 -*-
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from flask_restful import abort

class Db:
    def __init__(self, config):
        client = MongoClient(host=config.DB_HOSTS,
                            username=config.DB_USER,
                            password=config.DB_PASSWORD,
                            replicaSet=config.DB_REPLICA_SET,
                            authSource=config.DB_DATABASE_NAME
                            )
        self.db = client[config.DB_DATABASE_NAME]      
        
