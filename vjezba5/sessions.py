#!python.exe

import cgi
import os
import db
from http import cookies

params = cgi.FieldStorage()

def get_or_create_session_id():
    cookie_string = os.environ.get('HTTP_COOKIE')
    all_cookies_object = cookies.SimpleCookie(cookie_string)
    session_id = all_cookies_object.get('session_id').value if all_cookies_object.get('session_id') else None
    if session_id is None:
        session_id = db.create_session()
        cookie = cookies.SimpleCookie()
        cookie['session_id'] = session_id
        print(cookie.output())
    return session_id

def add_to_session(params):
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)
    for subject_id in params.keys():
        data[subject_id] = params[subject_id].value
    db.replace_session(session_id, data)

def get_session_data():
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)
    return data