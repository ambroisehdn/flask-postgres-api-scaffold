from flask_swagger_ui import get_swaggerui_blueprint

from app.routes.users_route import users

API_VERSION = 'v1'

API_VERSION_PATH = "/api/{}/service/".format(API_VERSION)

# Swagger ui
SWAGGER_URL = '/api/{}/docs'.format(API_VERSION)  # URL for exposing Swagger UI (without trailing '/')

API_URL='/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "project API"
    }
)

def register_routes(app):
    #Setup blueprint for routing

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
        
