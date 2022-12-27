from flask import jsonify,g
import datetime

class HandleError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.time_stamp = datetime.datetime.utcnow()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload


    def to_dict(self):
        rv = dict(())
        rv['statusCode'] = str(self.status_code)
        rv['timestamp'] = self.time_stamp.isoformat()
        rv['error']={}
        rv['error']['errors']=[{'code':None, 'message':self.message}]
        return rv

    def handle_invalid_usage(self):
        response = jsonify(self.to_dict())
        response.status_code = self.status_code
        return response
