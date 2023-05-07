#!python.exe
import cgi
import os
import base
import Predmeti
import db


def print_table(year, subjects, session_dict):
    status_names = Predmeti.status_names
    if year == "Upisni List":
        print_enrollment_form(subjects, session_dict)
    else:
        year_num = int(year[0])
        filtered_subjects = [subject for subject in subjects if subject["godina"] == year_num]
        print('<table class="styled-table">')
        print(f"<tr><th>{year} Subjects</th><th>ECTS</th><th>Status</th></tr>")
        for subject in filtered_subjects:
            status = session_dict.get(subject["kod"], "not")
            ects = subject["bodovi"]
            status_radio_inputs = "".join([f'<input type="radio" name="{subject["kod"]}" value="{status_name}" {"checked" if status == status_name else ""}>{status_str}' for status_name, status_str in status_names.items()])
            print(f"<tr><td>{subject['ime']}</td><td>{ects}</td><td>{status_radio_inputs}</td></tr>")
        print("</table>")



def print_enrollment_form(subjects, session_dict):
    total_ects = 0
    print('<table class="styled-table">')
    print("<tr><th>Enrollment Form Subjects</th><th>Status</th><th>Bodovi</th></tr>")

    for subject in subjects:
        status = session_dict.get(subject["kod"], "Not selected")
        
        if status == "enr":
            status_str = "Enrolled"
        elif status == "pass":
            status_str = "Passed"
        else:
            status_str = "Not Selected"
        
        print("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(subject["ime"], status_str, subject["bodovi"]))
        
        if status == "enr":
            total_ects += subject["bodovi"]
    
    print("<tr><td></td><td>Total ECTS</td><td>{}</td></tr>".format(total_ects))
    print("</table>")


params = cgi.FieldStorage()
email = params.getvalue("email")
year = params.getvalue("year", "1st Year")

user_id = db.get_user_id(email)
mydb = db.get_DB_connection()
session_id = db.get_or_create_session_id(user_id)
db.add_to_session(params, session_id)
session_dict= db.get_data(mydb,session_id)
subjects = db.get_subjects()

if os.environ['REQUEST_METHOD'] == 'POST':
    if params.getvalue("odjava") == "Odjava":
        db.logout()
        print("Location: login.py\r\n\r\n")
    
    elif params.getvalue("change_password") == "Change password":
        print("Location: change.py?email=" + email + "\r\n\r\n")

base.start_html()
print("""<p>Hej """+db.get_name(session_id)+"""!</p>""")
base.buttons()
base.print_navigation()
if year:
    print_table(year, subjects, session_dict)
else:
    print_table("Upisni List", subjects, session_dict)
base.end_html()
