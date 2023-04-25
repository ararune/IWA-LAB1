#!python.exe

import cgi
import base


params = cgi.FieldStorage()

base.start_html()

print("""
    <form method="POST">
        <table>
        <tr>
            <td>Lozinka:</td>
            <td><input type="password" name="password"></td>
        </tr>
        <tr>
            <td>Nova lozinka:</td>
            <td><input type="password" name="newpassword"></td>
        </tr>
        <tr>
            <td><input type="submit" value="Change Password"></td>
        </tr>
        </table>
    </form>
""")

base.end_html()
