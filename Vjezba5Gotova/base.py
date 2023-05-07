#!python.exe

def start_html():
    print("""
        <!DOCTYPE html>
        <html>
            <head><title>Vjezba 5</title></head>
            <link href="http://localhost/style.css" rel="stylesheet" type="text/css" /> 
            <body>
    """)

def end_html():
    print("""
        </body>
    </html>
    """)

def print_navigation():
    print("""
        <form action="" method="post">
            <div class="tab">
                <input type="submit" name="year" value="1st Year">
                <input type="submit" name="year" value="2nd Year">
                <input type="submit" name="year" value="3rd Year">
                <input type="submit" name="year" value="Upisni List">
            </div>
    """)

def buttons():
    print("""
        <form action="" method="post">
                <input type="submit" name="odjava" value="Odjava" />
                <input type="submit" name="change_password" value="Change password" />
        </form>
        <br><br>
    """)

