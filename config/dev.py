from datetime import timedelta

from config import config

class Config(config.Config):
    DEBUG = True
    ENV = 'dev'    
    APP_URL = 'http://localhost:19011'
    API_URL = '{}/swagger.json'.format(APP_URL)
    APP_NAME = "project"
    
    REDIS_URL = "redis://localhost:6379"
    REDIS_HOST = "localhost"
    REDIS_PORT_SSL = 6380
    REDIS_PORT = 6379
    REDIS_ABORTCONNECT = False
    REDIS_PASSWORD=""

    DATABASE_USER = "postgres"
    DATABASE_PASSWORD = "postgres"
    DATABASE_NAME = "project-api"
    DATABASE_HOST = "172.25.0.2"


    SQLALCHEMY_DATABASE_URI='postgresql://{}:{}@{}/{}'.format(DATABASE_USER,DATABASE_PASSWORD,DATABASE_HOST,DATABASE_NAME)
    
    OAUTHLIB_INSECURE_TRANSPORT=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_ACCESS_TOKEN_EXPIRES =  timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES =  timedelta(days=30)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    

    