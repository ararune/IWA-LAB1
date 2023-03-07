#!python.exe
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forma 1</title>
</head>

<style>
    .styled-table,
    td {
        border: 1px black solid;
    }
</style>

<body>
    <form action="vjezba2B.py" method="POST">
        <table class="styled-table">
            <tr>
                <td><label for="ime">Ime: </label></td>
                <td><input type="text" name="ime" placeholder="ime" required></td>
            </tr>
            <tr>
                <td><label for="password">Lozinka: </label></td>
                <td><input type="password" name="password" placeholder="lozinka" required></td>
            </tr>
            <tr>
                <td><label for="repeatPassword">Ponovi lozinku: </label></td>
                <td><input type="password" name="repeatPassword" placeholder="ponovite lozinku" required></td>
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