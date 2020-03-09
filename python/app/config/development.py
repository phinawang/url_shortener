# -*- coding: utf-8 -*-

import os

config = dict(
    API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost'),
    API_PORT = os.getenv('API_PORT', '5000'),
    DB_HOSTS = os.getenv('MONGO_HOST', 'mongodb').split(','),
    DB_DATABASE_NAME = os.getenv('DB_NAME', 'projectDB'),
    DB_USER = os.getenv('MONGO_USER', None),
    DB_PASSWORD = os.getenv('MONGO_PASSWORD', None),
    DB_REPLICA_SET = os.getenv('MONGO_REPLICASET', None),
    POOL_MAX = int(os.getenv('POOL_MAX', '255')),
    MAX_URL_LENGTH = 2000,
    DEBUG = os.getenv('DEBUG', True)
)