#!python.exe

import base
import sessions

data = sessions.get_session_data()

base.start_html()
base.print_navigation()
base.print_enrollment_form(data)
base.end_html()