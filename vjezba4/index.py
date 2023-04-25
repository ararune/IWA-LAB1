#!python.exe

import base
import sessions
import os

sessions.get_or_create_session_id()


print("Content-type:text/html")
print('Location: /cgi-bin/vjezba4/1st_year.py\r\n\r\n')