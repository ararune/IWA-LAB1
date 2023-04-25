#!python.exe

import base
import os
import sessions
import subjects


def handle_year():
    year = get_year()
    if (os.environ["REQUEST_METHOD"].upper() == "POST"):
        sessions.add_to_session(base.params)
    data = sessions.get_session_data()
    base.print_all_subjects(year, data)


def get_year():
    # Extract year parameter from URL or form data
    year = base.params.getvalue('year', None)
    if year is None:
        year = sessions.get_session_data().get('year', None)
    if year is None:
        year = '1'
    # Update session data with current year
    sessions.add_to_session({'year': year})
    return year