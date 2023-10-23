import sqlite3
vt=sqlite3.connect("users.db")
cur=vt.cursor()


class User:
    username=""
    password=""
    name=""
    surname=""
    def __init__(self):
        cur.execute("CREATE TABLE IF NOT EXISTS USER(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "NAME varchar(20),SURNAME varchar(20),USERNAME varchar(20),PASSWORD varchar(20)) ")


