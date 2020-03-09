# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods

import os

class Config:
    ENV_PRODUCTION = 'production'
    ENV_DEVELOPMENT = 'development'
    def __init__(self):
        self.ENV = os.getenv('PYTHON_ENV', os.getenv('FLASK_ENV', self.ENV_DEVELOPMENT))
        if self.ENV == self.ENV_PRODUCTION:
            from .production import config
        elif self.ENV == self.ENV_DEVELOPMENT:
            from .development import config
        else:
            raise KeyError('Invliad environment variable %s' % self.ENV)
        for key in config:
            setattr(self, key, config[key])