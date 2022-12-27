from os import environ


class Config:
    '''The default configuration object for the app.
    '''
    DB_NAME = environ.get('DB_NAME')