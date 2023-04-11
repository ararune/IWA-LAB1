#!python.exe

import subjects

def start_html():
    print("""
    <!DOCTYPE html>
    <html>
    <style>
    table, th, td {
      border:1px solid black;
    }
    </style>
    <body>
    <table style="width:30%">
     """)
    
def end_html():
    print("""
    </table>
    </body>
    </html>
    """)
  