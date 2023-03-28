#!python.exe
import cgi
form = cgi.FieldStorage()
fname = form.getvalue("fname")
email = form.getvalue("email")
Status = form.getvalue("Status")
smjer = form.getvalue("smjer")
Zavrsni = form.getvalue("Zavrsni")
napomene = form.getvalue("Napomene")

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
        table, th, td {{border:1px solid black;}}
    </style>
</head>
<body>
    <form>
        <table>
            <tr>
                <th><label for="fname">Ime: </label></th>
                <th><label for="fname">{}</label></th>
            </tr>
            <tr>
                <th><label for="email">E-mail: </label></th>
                <th><label for="email">{}</label></th>
            </tr>
            <tr>
                <th><label for="status">Status:</label></th>
                <th><label for="status">{}</label></th>
            </tr>
            <tr>
                <th><label for="smjer">Smjer: </label></th>
                <th><label for="smjer">{}</label></th>
            </tr>
            <tr>
                <th><label for="Zavrsni">Zavrsni: </label></th>
                <th><label for="Zavrsni">{}</label></th>
            </tr>
            <tr>
                <th><label for="napomena">Napomena: </label></th>
                <th><label for="napomena">{}</label></th>
            </tr>
        </table>
    </form>
    <a href="V2A.py">Na pocetak</a>
</body>
</html>
""".format(fname, email, Status, smjer, Zavrsni, napomene))