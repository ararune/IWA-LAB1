#!python.exe
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forma 2</title>
</head>
<style>
    .styled-table,
    td {
        border: 1px black solid;
    }
</style>

<body>
    <form action="vjezba2C.py" method="POST">
        <table class="styled-table">
            <tr>
                <td><label for="status">Status: </label></td>
                <td><label for="redovni">Redovan</label>
                    <input type="radio" id="redovni" name="status" value="redovan" required>
                    <label for="izvanredni">Izvanredan</label><input type="radio" id="izvanredni" name="status"
                        value="izvanredan">
                </td>
            </tr>
            <tr>
                <td><label for="mail">E-mail: </label></td>
                <td><input type="email" name="mail" placeholder="e-mail" required></td>
            </tr>
            <tr>
                <td><label for="module">Smjer: </label></td>
                <td>
                    <select name="module" required>
                        <option value="bp">Baze Podataka</option>
                        <option value="prog">Programiranje</option>
                        <option value="rm">Racunalne mreze</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td><label for="zavrsni">Zavrsni: </label></td>
                <td>
                    <input type="checkbox" name="zavrsni" required>
                </td>
            </tr>
            <tr>
                <td>
                    <input type="submit" value="Next">
                </td>
                <td></td>
            </tr>
        </table>
    </form>
</body>

</html>
""")