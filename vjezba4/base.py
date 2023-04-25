#!python.exe
import base
import subjects
import cgi

params = cgi.FieldStorage()

def start_html():
    print("""
        <!DOCTYPE html>
        <html>
            <head><title>Vjezba 3</title></head>
            <link href="http://localhost/style.css" rel="stylesheet" type="text/css" /> 
            <body>
            <form method="post">
    """)

def end_html():
    print("""
    </form>
        </body>
    </html>
    """)


def print_navigation():
    print("""
        <input type="submit" formaction="1st_year.py" value='1st year'>
        <input type="submit" formaction="2nd_year.py" value='2nd year'>
        <input type="submit" formaction="3rd_year.py" value='3rd year'>
        <input type="submit" formaction="enrollment_form.py" value='Enrollment Form'>
    """)

def print_all_subjects(year, data):
    all_subjects = subjects.get_all_subjects_by_year(year)
    all_statuses = [(k, v) for k,v in subjects.status_names.items()]
    all_subject_statuses = subjects.get_all_statuses_from_session(all_subjects, data)
    all_subject_statuses = dict(all_subject_statuses)
    print('<table class="styled-table">')
    for subject in all_subjects:
        print('<tr>')
        print('<td>' + subject[1]['name'] + '</td>')
        print('<td>')
        for status in all_statuses:
            print('<input type="radio" name="' + subject[0] + '" value="' + status[0] + '"')
            if status[0] == all_subject_statuses[subject[0]]:
                print('checked')
            print('>' + status[1])
        print('</td>')
        print('</tr>')
    print('</table>')

def print_enrollment_form(data):
    all_subjects_touples = [(k, v) for k, v in subjects.subjects.items()]
    ects_total = get_ects_total(data, all_subjects_touples)
    print_form_header()
    print_table_header()
    for subject in all_subjects_touples:
        print_subject_row(subject, data)
    print_total_row(ects_total)
    print('</form>')

def get_ects_total(data, all_subjects_touples):
    ects_total = 0
    for subject in all_subjects_touples:
        if data[subject[0]] == 'enr':
            ects_total += subject[1]['ects']
    return ects_total

def print_form_header():
    print('<form method="post">')

def print_table_header():
    print("""<table class="styled-table">
        <tr>
        <td>Subject</td>
        <td>Status</td>
        <td>ECTS</td>
        </tr>
    """)

def print_subject_row(subject, data):
    subject_name = subject[1]['name']
    subject_status = data[subject[0]]
    print('<tr>')
    print('<td>' + subject_name + '</td>')
    print('<td>' + subjects.status_names.get(subject_status) + '</td>')
    print('<td>' + str(subject[1]['ects']) + '</td>')
    print("</tr>")

def print_total_row(ects_total):
    print('<tr>')
    print('<td></td>')
    print('<td>Total</td>')
    print(f'<td>{ects_total}</td>')
    print('</tr>')
