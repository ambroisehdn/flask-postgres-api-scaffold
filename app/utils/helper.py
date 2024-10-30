# -*- coding: utf-8 -*-
"""
This module is an extension of helper

"""
import os
from flask import jsonify,request,url_for
import json
import re
from flask import current_app

APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def is_email(input_string):
    # Regular expression pattern for a simple email validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_pattern, input_string) is not None

def is_number(input_string):
    try:
        # Attempt to convert the input string to a float
        int(input_string)
        return True
    except ValueError:
        return False

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

def encode_json(data):
    return json.dumps(data)

def decode_json(data):
    return json.loads(data)

def remove_special_characters_and_replace_with_underscore(input_string):
    # Remove special characters using regex and replace them with an underscore
    return re.sub(r'[^a-zA-Z0-9\s]', '_', input_string)

def http_response(message=None,statusCode=200,data=None,encode=False):
    error=False
    if statusCode in range(400,500):error = True
    response = {
        "error":error,
        "statusCode":statusCode,
        "message":message
    }
    if data or isinstance(data, list) :
        response["data"] = data
    if encode : return encode_json(response)
    return response

def get_ressource_path(path, filenmae) :
    return url_for('static/{}'.format(path), filename=filenmae)


def format_date(today, lasconnection):
    seconds = (today - lasconnection).total_seconds()

    if seconds < 60:
        return str(int(seconds)) + " s"

    elif seconds < 3600:
        return str(int(seconds / 60)) + " mm"

    elif seconds < 86400:
        return str(int(seconds / 3600)) + " h"

    else:
        day = (today - lasconnection).days
        if day == 1:
            return "1 day"
        else:
            return str(day) + " days"

def get_app_root() :
    return APP_ROOT