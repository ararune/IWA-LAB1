#!python.exe
import base
import subjects
import os

subjects.create_cookie()
base.start_html()

if subjects.params.getvalue('year') != 'Upisni List':
    base.print_table()
else:
    base.print_enrollment_form()

base.end_html()
