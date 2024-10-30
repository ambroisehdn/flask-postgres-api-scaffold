from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt
from flask import jsonify
from flask import current_app

from app.models.pymongo_helper import find_one
from app.utils.helper import httpResponse

user_collection = 'users'

def has_role(role:str):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            dbname =  current_app.config['MONGO_DB_NAME']
            verify_jwt_in_request()
            claims = get_jwt()
            user_id = claims['sub']
            user = find_one(dbname,user_collection,{'record_id':user_id})
            if not user :
                return jsonify(httpResponse(f"You dont have access to this ressource",403)),403
            roles = user['roles']
            if role not in roles :
                role_string = ",".join(roles)
                return jsonify(httpResponse(f"You dont have access to this ressource as {role_string}",403)),403
            
            return fn(*args, **kwargs)

        return decorator
    return wrapper