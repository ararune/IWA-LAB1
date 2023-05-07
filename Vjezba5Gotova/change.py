#!python.exe
import cgi
import os
import db
import base

def change():
    print("""
            <form action="" method="post">
                <table class="styled-table">
                    <tr>
                        <th><label for="current">Current Password: </label></th>
                        <th><input type="text" id="current" name="current"></th>
                    </tr>
                    <tr>
                        <th><label for="new_password">New Password: </label></th>
                        <th><input type="text" id="new_password" name="new_password"></th>
                    </tr>
                    <tr>
                        <th><label for="repassword">Retype new Password: </label></th>
                        <th><input type="password" id="repassword" name="repassword"></th>
                    </tr>
                    <tr>
                        <th><input type="submit" name="mainPage" value="Back"></th>
                        <th><input type="submit" name="change" value="Change password"></th>
                    </tr>
                </table>
            </form>
            """ + message + """
        """)

params = cgi.FieldStorage()
email = params.getvalue("email")

user_id = db.get_user_id(email)
mydb = db.get_DB_connection()
session_id = db.get_or_create_session_id(user_id)

message = ""
if os.environ['REQUEST_METHOD'] == 'POST':
        if params.getvalue("change") == "Change password":
            current = params.getvalue("current")
            new_password = params.getvalue("new_password")
            repassword = params.getvalue("repassword")
            if not (current and new_password and repassword):
                message = "<p>Empty fields</p>"
            if new_password != repassword:
                message = "<p>New passwords do not match!</p>"
            else:
                if(db.check_password_exists(session_id, current)):
                    db.change_password(session_id, new_password)
                    message = "<p>Password changed successfully!</p>"
                else:
                    message = "<p>The password is incorrect.</p>"

        elif params.getvalue("mainPage") == "Back":
            print("Location: index.py?email=" + email + "\r\n\r\n")

base.start_html()          
change()
base.end_html()