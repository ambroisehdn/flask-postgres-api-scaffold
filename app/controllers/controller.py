from flask import jsonify
import sys
from marshmallow import ValidationError

from app.utils.helper import http_response
from app.models.database_helper import DatabaseHelper

class Controller :
    
    def _return_success(self,message,data,status) :
        return jsonify(http_response(message=message,data=data,statusCode=status)), status
    
    def _return_400(self, e:ValidationError) :
        return jsonify(http_response("Missing required body parameters",400,{"error": e.messages})), 400
        
    def _return_500(self, e:Exception) :
        exc_type, exc_obj, exc_tb = sys.exc_info()
        return jsonify(http_response('Process failed unintendedly ' + str(e) + ' at line ' +str(exc_tb.tb_lineno)+ ' on ' +__class__.__name__ , 500)), 500 
    
    def _database_helper(self):
        return  DatabaseHelper
