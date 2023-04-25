#!python.exe

import cgi
import base


params = cgi.FieldStorage()

base.start_html()

print("""
    <form method="POST">
    Click to logout!
        <table>
        <tr>
            <td><input type="submit" value="Logout"></td>
        </tr>
        </table>
    </form>
""")

base.end_html()
