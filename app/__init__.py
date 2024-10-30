from logging import Logger
import os
from flask import Flask,make_response,request
from werkzeug.exceptions import BadRequest
from flask_jwt_extended import JWTManager
import logging.config
from flask_migrate import Migrate

from app.utils.helper import http_response
from app.models.database import db  
from config import get_config
from config import logger
from app.routes import register_routes

os.environ.setdefault('FLASK_ENV', 'dev')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def create_app():
    app = Flask(__name__)

    # Load the configuration based on your environment
    config = get_config()
    app.config.from_object(config)
    app.config['APP_ROOT'] = APP_ROOT

    # Initialize db with app
    db.init_app(app)
      
    with app.app_context():
        from app.models.users_model import UsersModel
        from app.models.projects_model import ProjectsModel
        from app.models.tasks_model import TasksModel

        db.create_all() 
    #Logging configuration
    logging.config.dictConfig(logger.APP_LOG_CONFIG)
    
    # Register routes (blueprints)
    register_routes(app)
    
    return app

app = create_app()

app.secret_key = "lIxlPq8PYgjQHfXOcsIxzix2FWMX6yE2fUACzL1DoJFuTr2PKtF0ArVDFE"

# Enable CORS for all origins
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#General log variable
app_log = logging.getLogger('app')
database_log = logging.getLogger('database')

config = app.config

#run migration 
migrate = Migrate(app, db)

# JWT instances
jwt = JWTManager(app)

@app.errorhandler(400)
def bad_request_error(error):
  if isinstance(error, BadRequest):
    response = http_response(message=str(error.description),statusCode=400,encode=False)
  else :
    if not error :
      error = 'Required parameters missing'
    response = http_response(message=error,statusCode=400)
  return make_response(response, 400)

@app.errorhandler(404)
def page_not_found(e):
  """Send message to the user with notFound 404 status."""
  # Message to the user
  error = "This route is currently not supported. Please refer API documentation."
  response = http_response(message=error,statusCode=404)
  return make_response(response, 404)

# CORS configuration
def add_cors_headers(response):
   response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Realms'  # Set the allowed headers
   response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH'  # Set the allowed HTTP methods
   return response

app.after_request(add_cors_headers)

if __name__ == '__main__':
  app.run(debug=True)

