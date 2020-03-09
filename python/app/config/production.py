# -*- coding: utf-8 -*-

import os

config = dict(
    DB_HOSTS = os.environ['MONGO_HOST'].split(','),
    DB_DATABASE_NAME = os.environ['DB_NAME'],
    DB_USER = os.environ['MONGO_USER'],
    DB_PASSWORD = os.environ['MONGO_PASSWORD'],
    DB_REPLICA_SET = os.environ['MONGO_REPLICASET'],
    POOL_MAX = int(os.getenv('POOL_MAX', '255')),
    MAX_URL_LENGTH = 2000,
    DEBUG = os.getenv('DEBUG', False)
)