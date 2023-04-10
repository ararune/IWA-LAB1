#!python.exe
import subjects
import os
from http import cookies

def start_html():
    print("""
        <!DOCTYPE html>
        <html>
            <head><title>Vjezba 3</title></head>
            <style>
input {
  border: 1px solid #999;
  background: #EEE;
  padding: 4px 12px;
  border-radius: 4px 4px 0 0;
  position: relative;
  top: 1px;
  cursor: pointer;
}

.styled-table {
    border-collapse: collapse;
    width: 50%;
    margin-bottom: 1em;
}

.styled-table th,
.styled-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.styled-table th {
    background-color: #f2f2f2;
}

.styled-table tr:nth-child(even) {
    background-color: #f2f2f2;
}

            </style>
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
    all_statuses = [(k, v) for k,v in subjects.status_names.items()]
    all_subject_statuses = subjects.get_all_statuses_from_cookie(all_subjects)
    all_subject_statuses = dict(all_subject_statuses)
    print('<form method="post">')
    print_navigation()
    print('<table class="styled-table">')
    for subject in all_subjects:
        print("<tr>")
        print('<td>' + subject[1]['name'] + '</td>')
        print('<td>')
        for status in all_statuses:
            print('<input type="radio" name="' + subject[0] + '" value="' + status[0] + '"')
            if status[0] == all_subject_statuses[subject[0]]:
                print(' checked')
            print('>' + status[1])
        print('</td>')
        print("</tr>")
    print('</table>')
    print("</form>")

def print_enrollment_form():
    ects_total = 0
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    all_subjects_touples = [(k, v) for k, v in subjects.subjects.items()]
    print('<form method="post">')
    print_navigation()
    print("""<table class="styled-table">
        <tr>
        <td>Subject</td>
        <td>Status</td>
        <td>ECTS</td>
        </tr>
    """)
    for subject in all_subjects_touples:
        subject_name = subject[1]['name']
        subject_status = all_cookies_object.get(subject[0]).value
        if subject_status == 'enr':
            ects_total += subject[1]['ects']
        print('<tr>')
        print('<td>' + subject_name + '</td>')
        print('<td>' + subjects.status_names.get(subject_status) + '</td>')
        print('<td>' + str(subject[1]['ects']) + '</td>')
        print("</tr>")
    print('<tr>')
    print('<td>' + '' + '</td>')
    print('<td>' + 'Total' + '</td>')
    print('<td>' + str(ects_total) + '</td>')
    print("</tr>")
    print("</table>")
    print('</form>')