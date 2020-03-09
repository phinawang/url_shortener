# -*- coding: utf-8 -*-
import traceback
from werkzeug.exceptions import HTTPException, Forbidden, BadRequest
from flask import jsonify

class ForbiddenError(Forbidden):
    def __init__(self, reason=None):
        super().__init__('Forbidden', reason)


def register_error_handler_for_app(app):
    def handle_default_error(e):
        traceback.print_exc()
        return jsonify({'message': e.description, 'reason': e.response}), e.code

    app.register_error_handler(ForbiddenError, handle_default_error)

    @app.errorhandler(Exception)
    def handle_all_error(error):
        print(error)
        traceback.print_exc()
        return jsonify({'message': 'InternalServerError', 'reason': str(error)}), 500