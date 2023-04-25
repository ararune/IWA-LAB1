#!python.exe

import cgi
import base


params = cgi.FieldStorage()

base.start_html()

print("""
    <form method="POST">
        <table>
        <tr>
            <td>Ime:</td>
            <td><input type="text" name="name"></td>
        </tr>
        <tr>
            <td>Lozinka:</td>
            <td><input type="password" name="password"></td>
        </tr>
        <tr>
            <td><input type="submit" value="Login"></td>
        </tr>
        </table>
    </form>
""")

base.end_html()
