#!python.exe
import cgi
form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
 <style>
    .styled-table,
    td {
        border: 1px black solid;
    }
</style>
</head>
<body>
    <form action=V2B.py>
        <table class="styled-table">
            <tr>
                <td><label for="fname">Ime: </label></td>
                <td><input type="text" id="fname" name="fname" placeholder="Unesite ime..."required></td>
            </tr>
            <tr>
                <td><label for="password">Lozinka: </label></td>
                <td><input type="password" id="password" name="password" placeholder="Unesite lozinku..." required></td>
            </tr>
            <tr>
                <td><label for="repeatPassword">Ponovi lozinku: </label></td>                  
                <td><input type="password" id="repeatPassword" placeholder="Ponovite lozinku..." name="password" required></td>
            </tr>
            <tr>
                <td><input type="submit" value="Next" /></td>
                <td><input type="hidden" id="nothing" name="nothing"></td>
            </tr>
        </table>
    </form>
</body>
</html>
""")