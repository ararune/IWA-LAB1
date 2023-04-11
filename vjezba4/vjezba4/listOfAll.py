#!python.exe

import cgi
import os
import subjects
import base
from http import cookies

params = cgi.FieldStorage()
year = subjects.decide_year(params.getvalue('year'))

cookies_str = os.environ.get('HTTP_COOKIE', '')
cookie = cookies.SimpleCookie(cookies_str)

base.start_html()
subjects.display_year()

subjects.get_all(cookie)
base.end_html()