#!python.exe
import cgi
form = cgi.FieldStorage()
fname = form.getvalue("fname")
password = form.getvalue("password")
repassword = form.getvalue("repassword")

print ("Content-Type: text/html")
print("")

if(password == repassword):
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
        <body>
            <form action="http://localhost/cgi-bin/Vjezba2c.py">
                <table>
                    <tr>
                        <th><label for="Status">Status: </label></th>
                        <th><input type="radio" id="Redovan" name="Status" value="Redovan">
                            <label for="html">Redovan</label>
                            <input type="radio" id="Izvanredan" name="Status" value="Izvanredan">
                            <label for="css">Izvanredan</label></th>
                    </tr>
                    <tr>
                        <th><label for="email">E-mail: </label></th>
                        <th><input type="email" id="email" name="email"></th>
                    </tr>
                    <tr>
                        <th><label for="smjer">Smjer: </label></th>                  
                        <th>
                            <select id="smjer" name="smjer">
                            <option name="smjer" value="Programiranje">Programiranje</option>
                            <option name="smjer" value="Baza Podataka">Baza Podataka</option>
                            <option name="smjer" value="Mreze">Mreze</option>
                            </select></th>
                    </tr>
                    <tr>
                        <th><label for="Zavrsni">Zavrsni: </label></th>                  
                        <th><input type="checkbox" id="Zavrsni" name="Zavrsni" value="Zavrsni"></th>                  
                        </th>
                    </tr>
                    <tr>
                        <th><input type="submit" value="Next" /></th>
                        <th><input type="hidden" id="nothing" name="nothing"></th>
                    </tr>
                </table>
                <input type="hidden" id="fname" name="fname" value="{}">
            </form>
        </body>
    </body>
    </html>
    """.format(fname))

if(password != repassword):
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <body>
            <p>Wrong password!</p>
            <a href="http://localhost/cgi-bin/Vjezba2a.py">  
                <input value="Try again!" type="submit"/> 
            </a>
        </body>
    </body>
    </html>
    """.format(fname))
