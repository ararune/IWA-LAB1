#!python.exe
import cgi
form = cgi.FieldStorage()
fname = form.getvalue("fname")

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
        <form action=V2C.py>
            <table class="styled-table">
                <tr>
                    <td><label for="Status">Status: </label></td>
                    <td><input type="radio" id="Redovan" name="Status" value="Redovan" required>
                        <label for="html">Redovan</label>
                        <input type="radio" id="Izvanredan" name="Status" value="Izvanredan" required>
                        <label for="css">Izvanredan</label></td>
                </tr>
                <tr>
                    <td><label for="email">E-mail: </label></td>
                    <td><input type="email" id="email" name="email" required></td>
                </tr>
                <tr>
                    <td><label for="smjer">Smjer: </label></td>                  
                    <td>
                        <select id="smjer" name="smjer" required>
                          <option name="smjer" value="Programiranje">Programiranje</option>
                          <option name="smjer" value="Baza Podataka">Baza Podataka</option>
                          <option name="smjer" value="Mreze">Mreze</option>
                        </select></td>
                </tr>
                <tr>
                    <td><label for="Zavrsni">Zavrsni: </label></td>                  
                    <td><input type="checkbox" id="Zavrsni" name="Zavrsni" value="Zavrsni"></td>                  
                    </td>
                </tr>
                <tr>
                    <td><input type="submit" value="Next" /></td>
                    <td><input type="hidden" id="nothing" name="nothing"></td>
                </tr>
            </table>
            <input type="hidden" id="fname" name="fname" value="{}">
        </form>
    </body>
</body>
</html>
""".format(fname))