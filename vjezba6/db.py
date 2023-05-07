#!python.exe
import mysql.connector # "C:\ProgramData\Anaconda3\python.exe" -m pip install mysql-connector 
import json
import os
import hashlib
from http import cookies

def get_DB_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="vjezba6"
    )
    return mydb

def create_user(name, email, password, uloga):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    if result:
        return True #If a user exists
    else:
        hashed_password = hash_password(password)
        query = "INSERT INTO users (ime, email, password, uloga) VALUES (%s, %s, %s, %s)"
        values = (name, email, hashed_password, uloga)
        cursor.execute(query, values)
        mydb.commit()
        return False

def add_to_session(params, session_id):
    _, data = get_session(session_id)#vracanje do sada odabranih podataka
    for article_id in params.keys():
        data[article_id] = params[article_id].value
    replace_session(session_id, data)
     
def create_session(user_id):
    query = "INSERT INTO sessions (session_id) VALUES (%s)"
    values = (user_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor(buffered=True)
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid

def get_or_create_session_id(user_id):
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    if session_id is None:
        session_id = create_session(user_id)
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print (cookies_object.output()) #upisivanje cookie-a u header
    return session_id

def get_user_id(email):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    sql = "SELECT id FROM users WHERE email=%s"
    val = (email,)
    cursor.execute(sql, val)
    user_id = cursor.fetchone()
    cursor.close()
    mydb.close()
    return user_id[0]

def get_user(email, password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE email=%s"
    val = (email,)
    cursor.execute(sql, val)
    #cursor.execute("SELECT * FROM users WHERE email = " + email)
    user = cursor.fetchone()
    cursor.close()
    mydb.close()
    if user != None:
        stored_password_hash = user[3]
        if verify_password(password, stored_password_hash):
            return True
    return False

def get_name(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor(buffered=True)
    query = "SELECT ime FROM users WHERE id= %s"
    values = (session_id,)
    cursor.execute(query, values)
    user_name = cursor.fetchone()[0]
    return user_name


def delete_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = %s"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor(buffered=True)
    cursor.execute(query, values)
    mydb.commit()

def logout():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    if session_id is not None:
        delete_session(session_id)
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = ""
        cookies_object["session_id"]["expires"] = 'Thu, 01 Jan 1970 00:00:00 GMT'
        print(cookies_object.output())

def get_subjects():
    mydb = get_DB_connection()
    cursor = mydb.cursor(buffered=True)
    query = "SELECT * FROM subjects"
    cursor.execute(query)
    result = cursor.fetchall()

    subjects = []
    for row in result:
        subject_dict = {
            'id': row[0],
            'kod': row[1],
            'ime': row[2],
            'bodovi': row[3],
            'godina': row[4]
        }
        subjects.append(subject_dict)

    cursor.close()
    mydb.close()
    return subjects

def get_data(mydb,session_id):
    cursor = mydb.cursor(buffered=True)
    query = "SELECT data FROM sessions WHERE session_id= %s"
    values = (session_id,)
    cursor.execute(query, values)
    session_data = cursor.fetchone()
    session_dict = json.loads(session_data[0].decode('utf-8'))
    return session_dict

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()



def check_password_exists(session_id, check_input_password):
    mydb = get_DB_connection()
    cursor = mydb.cursor(buffered=True)
    query = "SELECT password FROM users WHERE id= %s"
    values = (session_id,)
    cursor.execute(query, values)
    password = cursor.fetchone()
    password_str = password[0] if password else None
    cursor.close()
    mydb.close()
    if verify_password(check_input_password, password_str):
        return True
    return False

def change_password(session_id, new_password):
    mydb = get_DB_connection()
    cursor = mydb.cursor(buffered=True)
    hashed_password = hash_password(new_password)
    query = "UPDATE users SET password = %s WHERE id = %s"
    values = (hashed_password, session_id)
    cursor.execute(query, values)
    mydb.commit()

def hash_password(password):
    password_bin = password.encode('utf-8')
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac(
        'sha256', password_bin, salt, 100000
    )
    return salt + hash

def verify_password(password_plain_text, stored_password_hash):
    salt = stored_password_hash[:32]
    key = stored_password_hash[32:]
    new_hash = hashlib.pbkdf2_hmac('sha256', password_plain_text.encode('utf-8'), salt, 100000)
    return (key == new_hash)