#!python.exe
import cgi
import os
import db
import base

def login():
    print("""
        <form action="" method="post">
            <table class="styled-table">
                <tr>
                    <th><label for="email">Email: </label></th>
                    <th><input type="text" id="email" name="email"></th>
                </tr>
                <tr>
                    <th><label for="password">Lozinka: </label></th>
                    <th><input type="password" id="password" name="password"></th>
                </tr>
            </table>
            <th><input type="submit" name="Log" value="Login"></th>
            <br><br>
            <th><input type="submit" name="Reg" value="Register"></th>
        </form>
        """ + message + """
    """)

params = cgi.FieldStorage()

message = ""
user_id = None
if os.environ['REQUEST_METHOD'] == 'POST':
    if params.getvalue("Log") == "Login":
        email = params.getvalue("email")
        password = params.getvalue("password")
        if(db.get_user(email, password)):
            user_id = db.get_user_id(email)
            db.get_or_create_session_id(str(user_id))
            print("Location: index.py?email=" + email + "\r\n\r\n")
        else:
            message = "<p>Invalid input</p>"
    elif params.getvalue("Reg") == "Register":
        print("Location: register.py\r\n\r\n")


base.start_html()
login()
base.end_html()
