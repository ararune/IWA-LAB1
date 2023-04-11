#!python.exe
import subjects
import os
from http import cookies

def start_html():
    print("""
        <!DOCTYPE html>
        <html>
            <head><title>Vjezba 3</title></head>
            <link href="http://localhost/style.css" rel="stylesheet" type="text/css" /> 
            <body>
    """)

def end_html():
    print("""
        </body>
    </html>
    """)

def print_navigation():
    print("""
        <input type="submit" name="year" value="1st Year" />
        <input type="submit" name="year" value="2nd Year" />
        <input type="submit" name="year" value="3rd Year" />
        <input type="submit" name="year" value="Upisni List" />
    """)

def print_table():
    all_subjects = subjects.get_all_subjects_by_year(subjects.year)
    all_statuses = [(status_id, status_name) for status_id, status_name in subjects.status_names.items()]

    # Get statuses of all subjects from cookies
    all_subject_statuses = subjects.get_all_statuses_from_cookie(all_subjects)
    all_subject_statuses = dict(all_subject_statuses)

    # Print the table
    print('<form method="post">')
    print_navigation()
    print('<table class="styled-table">')
    for subject_id, subject_info in all_subjects:
        print_subject_row(subject_info['name'])
        print('<td>')
        for status_id, status_name in all_statuses:
            print_status_radio_button(subject_id, status_id, status_name, all_subject_statuses)
        print('</td>')
        print("</tr>")
    print('</table>')
    print("</form>")


def print_subject_row(subject_name):
    """Prints a row for a subject"""
    print("<tr>")
    print(f"<td>{subject_name}</td>")


def print_status_radio_button(subject_id, status_id, status_name, all_subject_statuses):
    """Prints a radio button for a status"""
    checked = 'checked' if status_id == all_subject_statuses.get(subject_id) else ''
    print(f'<input type="radio" name="{subject_id}" value="{status_id}" {checked}>{status_name}')


def get_ects_total(all_subjects_touples, all_cookies_object):
    ects_total = 0
    for subject_info in all_subjects_touples:
        subject_status = all_cookies_object.get(subject_info[0]).value
        if subject_status == 'enr':
            ects_total += subject_info[1]['ects']
    return ects_total

def print_enrollment_form():
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    all_subjects_touples = [(k, v) for k, v in subjects.subjects.items()]
    ects_total = get_ects_total(all_subjects_touples, all_cookies_object)
    print('<form method="post">')
    print_navigation()
    print("""<table class="styled-table">
        <tr>
        <td>Subject</td>
        <td>Status</td>
        <td>ECTS</td>
        </tr>
    """)
    for subject_info in all_subjects_touples:
        subject_name = subject_info[1]['name']
        subject_status = all_cookies_object.get(subject_info[0]).value
        print('<tr>')
        print(f'<td>{subject_name}</td>')
        print(f'<td>{subjects.status_names.get(subject_status)}</td>')
        print(f'<td>{subject_info[1]["ects"]}</td>')
        print('</tr>')
    print('<tr>')
    print('<td></td>')
    print('<td>Total</td>')
    print(f'<td>{ects_total}</td>')
    print('</tr>')
    print('</table>')
    print('</form>')