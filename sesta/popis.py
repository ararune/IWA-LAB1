#!python.exe
import cgi
import base
import db


params = cgi.FieldStorage()
email = params.getvalue("email")

user_id = db.get_user_id(email)
mydb = db.get_DB_connection()
students_list = db.get_students(mydb)
subjects = db.get_subjects()

base.start_html()
print("<table>")
print("<tr><th>Name</th></tr>")
for student in students_list:
    print("<tr>")
    print("<td>{}</td>".format(student["ime"]))
    print("</tr>")
print("</table>")
base.end_html()
