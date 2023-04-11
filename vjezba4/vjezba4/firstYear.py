#!python.exe

import base
import cgi
import os
import subjects, session

params = cgi.FieldStorage()
year = subjects.decide_year(params.getvalue('year'))

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

##data = session.get_session_data()


base.start_html()

subjects.display_year()

print("""
    </td>
  </tr>
  <tr>
    <td>""")
print (year)
print("""
    </td>
    <td>Ects</td>
    </td>
    <td>Status</td>""")

subjects = subjects.get_subjects()

##subjects.display_subjects_of_year(year, params)

for key, status in subjects.items():
    subjects.display(year, key, status)

print('<input type="submit" name="year" value="List all">')

print("</form>")

base.end_html()