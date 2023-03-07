#!python.exe
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forma 3</title>
    <style>
        .styled-table,
        td {
            border: 1px black solid;
        }

        .text-area {
            padding: auto;
        }
    </style>
</head>

<body>
    <form>
        <table class="styled-table">
            <tr>
                <td><label for="napomene">Napomene: </label></td>
                <td>
                    <textarea name="napomene" placeholder="Prelazak na izvanredni studij.." class="text-area"
                        required></textarea>
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