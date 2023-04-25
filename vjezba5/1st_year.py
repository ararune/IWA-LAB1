#!python.exe

import base
import os
import sessions


if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    sessions.add_to_session(base.params)
data = sessions.get_session_data()
print()

base.start_html()
base.print_navigation()
base.print_all_subjects('1st Year', data)
base.end_html()
