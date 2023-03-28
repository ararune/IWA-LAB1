#!python.exe
import cgi
form = cgi.FieldStorage()
fname = form.getvalue("fname")
email = form.getvalue("email")
Status = form.getvalue("Status")
smjer = form.getvalue("smjer")
Zavrsni = form.getvalue("Zavrsni")

print ("Content-Type: text/html")
print("")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table, td {{border:1px solid black;}}
    </style>
</head>
<body>
    <body>
        <form action="V2D.py">
            <table class="styled-table">
                <tr>
                    <td><label for="Napomene">Napomene: </label></td>
                    <td><textarea id="Napomene" name="Napomene" rows="4" cols="50">Prelazak na izvanredne...</textarea></td>
                </tr>

                <tr>
                    <td><input type="submit" value="Next" /></td>
                    <td><input type="hidden" id="nothing" name="nothing"></td>
                </tr>
            </table>
            <input type="hidden" name="fname" id="fname" value="{}">
            <input type="hidden" name="email" id="email" value="{}">
            <input type="hidden" name="Status" id="Status" value="{}">
            <input type="hidden" name="smjer" id="smjer" value="{}">
            <input type="hidden" name="Zavrsni" id="Zavrsni" value="{}">
        </form>
    </body>
</body>
</html>
""".format(fname, email, Status, smjer, Zavrsni))