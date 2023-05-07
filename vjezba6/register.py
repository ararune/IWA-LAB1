#!python.exe
import cgi
import os
import db
import base

def register():
    print("""
        <form action="" method="post">
            <table class="styled-table">
                <tr>
                    <th><input type="text" id="ime" name="ime" placeholder="Enter name..."></th>
                </tr>
                <tr>
                    <th><input type="text" id="email" name="email" placeholder="Enter email..."></th>
                </tr>
                <tr>
                    <th><input type="password" id="password" name="password" placeholder="Enter password..."></th>
                </tr>
                <tr>           
                    <th><input type="password" id="repassword" name="repassword" placeholder="Repeat password..."></th>
                </tr> 
                <tr>
                 <th>
                    <input type="radio" id="admin" name="uloga" value="admin">
                    <label for="admin">Admin</label>
                    <input type="radio" id="student" name="uloga" value="student" checked>
                    <label for="student">Student</label>
                </th>
                </tr>
            </table>
                <input type="submit" name="Reg" value="Register">
                <br><br>
                <input type="submit" name="Log" value="Login">
        </form>
        """ + message + """
    """)

params = cgi.FieldStorage()

message = ""
if os.environ['REQUEST_METHOD'] == 'POST':
    if params.getvalue("Reg") == "Register":
        name = params.getvalue("ime")
        email = params.getvalue("email")
        password = params.getvalue("password")
        repassword = params.getvalue("repassword")
        uloga = params.getvalue("uloga")

        if not (name and email and password and repassword):
            message = "<p>Invalid input</p>"
        elif password != repassword:
            message = "<p>Passwords do not match!</p>"
        else:
            if(db.create_user(name, email, password, uloga)):
                message = "<p>User already exists</p>"
            else:
                print("Location: login.py\r\n\r\n")

    elif params.getvalue("Log") == "Login":
        print("Location: login.py\r\n\r\n")


base.start_html()              
register()
base.end_html()
